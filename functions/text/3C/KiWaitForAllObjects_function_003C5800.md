# KiWaitForAllObjects

- RVA: `0x003C5800`–`0x003C5FAB` (길이 `1,963` bytes)
- VA: `0x00000001403C5800`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008E47C`
- 디코드: `475`개 명령, `1,963/1,963` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003C5873` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003C58E2` → [KiCheckWaitNext](KiCheckWaitNext_function_003C5FC0.md) (function, `0x003C5FC0`)
- `0x003C598C` → [KiPerformWaitDeferredWork](../22/KiPerformWaitDeferredWork_function_00220480.md) (function, `0x00220480`)
- `0x003C59AD` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003C5A10` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x003C5A35` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x003C5B72` → [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) (function, `0x00220BB0`)
- `0x003C5B83` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003C5BEE` → [KiCheckDueTimeExpired](KiCheckDueTimeExpired_function_003C6400.md) (function, `0x003C6400`)
- `0x003C5C39` → [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) (function, `0x00220BB0`)
- `0x003C5CD0` → [KiWaitSatisfyMutant](KiWaitSatisfyMutant_function_003C6490.md) (function, `0x003C6490`)
- `0x003C5D39` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C5D48` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C5DF2` → [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) (function, `0x0020DFE0`)
- `0x003C5E70` → [KiReleaseThreadLockLowerIrql](KiReleaseThreadLockLowerIrql_function_003C65D0.md) (function, `0x003C65D0`)
- `0x003C5E7C` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x003C5EA5` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003C5ECD` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C5EDD` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C5EEB` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003C5F0C` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x003C5F3A` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x003C5F62` → [KiUnlockKobjectArray](../46/KiUnlockKobjectArray_function_004611EC.md) (function, `0x004611EC`)
- `0x003C5F70` → [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) (function, `0x00220BB0`)
- `0x003C5F7A` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- [sub_0020D579](../20/Unknown_function_0020D579.md) at `0x0020D59B`

### Static image references
- `0x003C581F` → RVA `0x00E0A740` (`.data`; read)
- `0x003C592B` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003C599D` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003C5D2B` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003C5F94` → [sub_006E8106](../6E/Unknown_function_006E8106.md) (`tail-transfer`)
  - `0x003C5F9E` → [sub_006E8106 + 0x62](../6E/Unknown_function_006E8106.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003C5800  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
003C5805  55                              push rbp
003C5806  56                              push rsi
003C5807  57                              push rdi
003C5808  41 54                           push r12
003C580A  41 55                           push r13
003C580C  41 56                           push r14
003C580E  41 57                           push r15
003C5810  48 8D AC 24 70 FE FF FF         lea rbp, [rsp - 0x190]
003C5818  48 81 EC 90 02 00 00            sub rsp, 0x290
003C581F  48 8B 05 1A 4F A4 00            mov rax, qword ptr [rip + 0xa44f1a]
003C5826  48 33 C4                        xor rax, rsp
003C5829  48 89 85 88 01 00 00            mov qword ptr [rbp + 0x188], rax
003C5830  48 8B 85 00 02 00 00            mov rax, qword ptr [rbp + 0x200]
003C5837  4C 8B F2                        mov r14, rdx
003C583A  48 8B 9D F8 01 00 00            mov rbx, qword ptr [rbp + 0x1f8]
003C5841  44 8B E9                        mov r13d, ecx
003C5844  44 89 44 24 58                  mov dword ptr [rsp + 0x58], r8d
003C5849  33 FF                           xor edi, edi
003C584B  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
003C5850  41 B8 F8 01 00 00               mov r8d, 0x1f8
003C5856  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
003C585A  33 D2                           xor edx, edx
003C585C  48 8D 4D 88                     lea rcx, [rbp - 0x78]
003C5860  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003C5865  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
003C586A  45 0F B6 E1                     movzx r12d, r9b
003C586E  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
003C5873  E8 C8 13 30 00                  call 0x1406c6c40
003C5878  49 8B 06                        mov rax, qword ptr [r14]
003C587B  B9 01 00 00 00                  mov ecx, 1
003C5880  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
003C5884  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
003C5888  44 3B E9                        cmp r13d, ecx
003C588B  76 2F                           jbe 0x1403c58bc
003C588D  49 8D 56 08                     lea rdx, [r14 + 8]
003C5891  4C 8B 0A                        mov r9, qword ptr [rdx]
003C5894  44 8B C1                        mov r8d, ecx
003C5897  45 8D 50 FF                     lea r10d, [r8 - 1]
003C589B  4E 8B 5C D5 80                  mov r11, qword ptr [rbp + r10*8 - 0x80]
003C58A0  4D 3B D9                        cmp r11, r9
003C58A3  0F 87 A9 04 00 00               ja 0x1403c5d52
003C58A9  41 8B C0                        mov eax, r8d
003C58AC  FF C1                           inc ecx
003C58AE  48 83 C2 08                     add rdx, 8
003C58B2  4C 89 4C C5 80                  mov qword ptr [rbp + rax*8 - 0x80], r9
003C58B7  41 3B CD                        cmp ecx, r13d
003C58BA  72 D5                           jb 0x1403c5891
003C58BC  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
003C58C5  48 8D 44 24 40                  lea rax, [rsp + 0x40]
003C58CA  49 8B CF                        mov rcx, r15
003C58CD  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
003C58D2  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
003C58D7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003C58DC  45 33 C0                        xor r8d, r8d
003C58DF  48 8B D3                        mov rdx, rbx
003C58E2  E8 D9 06 00 00                  call 0x1403c5fc0
003C58E7  8B D8                           mov ebx, eax
003C58E9  41 0F B6 B7 86 01 00 00         movzx esi, byte ptr [r15 + 0x186]
003C58F1  45 33 F6                        xor r14d, r14d
003C58F4  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
003C58F9  45 8D 6E 02                     lea r13d, [r14 + 2]
003C58FD  41 83 67 74 EF                  and dword ptr [r15 + 0x74], 0xffffffef
003C5902  45 88 77 70                     mov byte ptr [r15 + 0x70], r14b
003C5906  45 88 A7 87 01 00 00            mov byte ptr [r15 + 0x187], r12b
003C590D  44 38 B5 F0 01 00 00            cmp byte ptr [rbp + 0x1f0], r14b
003C5914  74 05                           je 0x1403c591b
003C5916  41 83 4F 74 10                  or dword ptr [r15 + 0x74], 0x10
003C591B  41 8B FE                        mov edi, r14d
003C591E  66 90                           nop
003C5920  F0 49 0F BA 6F 40 00            lock bts qword ptr [r15 + 0x40], 0
003C5927  73 1B                           jae 0x1403c5944
003C5929  FF C7                           inc edi
003C592B  85 3D 7B F9 BF 00               test dword ptr [rip + 0xbff97b], edi
003C5931  0F 84 F4 03 00 00               je 0x1403c5d2b
003C5937  F3 90                           pause
003C5939  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
003C593D  48 85 C0                        test rax, rax
003C5940  74 DE                           je 0x1403c5920
003C5942  EB E5                           jmp 0x1403c5929
003C5944  45 38 B7 C1 00 00 00            cmp byte ptr [r15 + 0xc1], r14b
003C594B  0F 85 02 05 00 00               jne 0x1403c5e53
003C5951  44 38 B5 F0 01 00 00            cmp byte ptr [rbp + 0x1f0], r14b
003C5958  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
003C595D  44 8B 6C 24 34                  mov r13d, dword ptr [rsp + 0x34]
003C5962  0F 85 3C 02 00 00               jne 0x1403c5ba4
003C5968  41 F6 87 C2 00 00 00 02         test byte ptr [r15 + 0xc2], 2
003C5970  74 5D                           je 0x1403c59cf
003C5972  45 84 E4                        test r12b, r12b
003C5975  74 58                           je 0x1403c59cf
003C5977  BF C0 00 00 00                  mov edi, 0xc0
003C597C  45 33 E4                        xor r12d, r12d
003C597F  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
003C5984  41 B0 01                        mov r8b, 1
003C5987  8B D3                           mov edx, ebx
003C5989  49 8B CF                        mov rcx, r15
003C598C  E8 EF AA E5 FF                  call 0x140220480
003C5991  4D 89 67 40                     mov qword ptr [r15 + 0x40], r12
003C5995  85 C0                           test eax, eax
003C5997  0F 85 8B 05 00 00               jne 0x1403c5f28
003C599D  39 05 7D 13 C0 00               cmp dword ptr [rip + 0xc0137d], eax
003C59A3  74 0D                           je 0x1403c59b2
003C59A5  44 0F 20 C1                     mov rcx, cr8
003C59A9  40 0F B6 D6                     movzx edx, sil
003C59AD  E8 E6 FC 12 00                  call 0x1404f5698
003C59B2  44 0F 22 C6                     mov cr8, rsi
003C59B6  E9 BC 01 00 00                  jmp 0x1403c5b77
003C59BB  45 33 E4                        xor r12d, r12d
003C59BE  45 38 67 72                     cmp byte ptr [r15 + 0x72], r12b
003C59C2  0F 85 B8 05 00 00               jne 0x1403c5f80
003C59C8  41 8B FC                        mov edi, r12d
003C59CB  85 FF                           test edi, edi
003C59CD  75 B0                           jne 0x1403c597f
003C59CF  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
003C59D3  33 FF                           xor edi, edi
003C59D5  41 C6 87 84 01 00 00 05         mov byte ptr [r15 + 0x184], 5
003C59DD  41 88 87 83 02 00 00            mov byte ptr [r15 + 0x283], al
003C59E4  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
003C59EE  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
003C59F3  8B 00                           mov eax, dword ptr [rax]
003C59F5  41 89 87 B4 01 00 00            mov dword ptr [r15 + 0x1b4], eax
003C59FC  49 89 7F 40                     mov qword ptr [r15 + 0x40], rdi
003C5A00  65 4C 8B 24 25 20 00 00 00      mov r12, qword ptr gs:[0x20]
003C5A09  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
003C5A0D  48 8B CE                        mov rcx, rsi
003C5A10  E8 7B C2 E8 FF                  call 0x140251c90
003C5A15  41 83 FD 01                     cmp r13d, 1
003C5A19  0F 86 F9 02 00 00               jbe 0x1403c5d18
003C5A1F  48 8D 7D 88                     lea rdi, [rbp - 0x78]
003C5A23  45 8D 75 FF                     lea r14d, [r13 - 1]
003C5A27  48 8B 07                        mov rax, qword ptr [rdi]
003C5A2A  48 3B C6                        cmp rax, rsi
003C5A2D  74 0B                           je 0x1403c5a3a
003C5A2F  48 8B C8                        mov rcx, rax
003C5A32  48 8B F0                        mov rsi, rax
003C5A35  E8 56 C2 E8 FF                  call 0x140251c90
003C5A3A  48 83 C7 08                     add rdi, 8
003C5A3E  49 83 EE 01                     sub r14, 1
003C5A42  75 E3                           jne 0x1403c5a27
003C5A44  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
003C5A49  33 FF                           xor edi, edi
003C5A4B  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
003C5A50  4D 8B CD                        mov r9, r13
003C5A53  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
003C5A58  4C 8B C7                        mov r8, rdi
003C5A5B  49 8B D6                        mov rdx, r14
003C5A5E  49 8D 4B 11                     lea rcx, [r11 + 0x11]
003C5A62  48 8B 02                        mov rax, qword ptr [rdx]
003C5A65  C6 41 FF 00                     mov byte ptr [rcx - 1], 0
003C5A69  C6 01 04                        mov byte ptr [rcx], 4
003C5A6C  48 89 41 0F                     mov qword ptr [rcx + 0xf], rax
003C5A70  66 89 79 01                     mov word ptr [rcx + 1], di
003C5A74  4C 89 79 07                     mov qword ptr [rcx + 7], r15
003C5A78  48 8D 49 30                     lea rcx, [rcx + 0x30]
003C5A7C  4C 8B 12                        mov r10, qword ptr [rdx]
003C5A7F  41 0F B6 02                     movzx eax, byte ptr [r10]
003C5A83  24 7F                           and al, 0x7f
003C5A85  3C 02                           cmp al, 2
003C5A87  0F 84 BB 01 00 00               je 0x1403c5c48
003C5A8D  49 FF C0                        inc r8
003C5A90  48 83 C2 08                     add rdx, 8
003C5A94  49 83 E9 01                     sub r9, 1
003C5A98  75 C8                           jne 0x1403c5a62
003C5A9A  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
003C5A9F  44 8B 6C 24 34                  mov r13d, dword ptr [rsp + 0x34]
003C5AA4  49 89 BF C8 00 00 00            mov qword ptr [r15 + 0xc8], rdi
003C5AAB  8B CF                           mov ecx, edi
003C5AAD  49 89 BF D0 03 00 00            mov qword ptr [r15 + 0x3d0], rdi
003C5AB4  8B C1                           mov eax, ecx
003C5AB6  49 8B 14 C6                     mov rdx, qword ptr [r14 + rax*8]
003C5ABA  0F B6 02                        movzx eax, byte ptr [rdx]
003C5ABD  24 7F                           and al, 0x7f
003C5ABF  3C 02                           cmp al, 2
003C5AC1  0F 84 95 01 00 00               je 0x1403c5c5c
003C5AC7  83 7A 04 00                     cmp dword ptr [rdx + 4], 0
003C5ACB  7E 07                           jle 0x1403c5ad4
003C5ACD  FF C1                           inc ecx
003C5ACF  41 3B CD                        cmp ecx, r13d
003C5AD2  72 E0                           jb 0x1403c5ab4
003C5AD4  41 3B CD                        cmp ecx, r13d
003C5AD7  0F 85 05 01 00 00               jne 0x1403c5be2
003C5ADD  45 85 ED                        test r13d, r13d
003C5AE0  74 42                           je 0x1403c5b24
003C5AE2  41 8B FD                        mov edi, r13d
003C5AE5  45 33 ED                        xor r13d, r13d
003C5AE8  49 8B 36                        mov rsi, qword ptr [r14]
003C5AEB  0F B6 0E                        movzx ecx, byte ptr [rsi]
003C5AEE  0F B6 C1                        movzx eax, cl
003C5AF1  24 07                           and al, 7
003C5AF3  3C 01                           cmp al, 1
003C5AF5  0F 84 F7 03 00 00               je 0x1403c5ef2
003C5AFB  80 E1 7F                        and cl, 0x7f
003C5AFE  80 F9 05                        cmp cl, 5
003C5B01  0F 84 9C 04 00 00               je 0x1403c5fa3
003C5B07  80 F9 02                        cmp cl, 2
003C5B0A  0F 84 84 01 00 00               je 0x1403c5c94
003C5B10  49 83 C6 08                     add r14, 8
003C5B14  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
003C5B19  48 83 EF 01                     sub rdi, 1
003C5B1D  75 C9                           jne 0x1403c5ae8
003C5B1F  44 8B 6C 24 34                  mov r13d, dword ptr [rsp + 0x34]
003C5B24  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
003C5B28  F0 81 21 7F FF FF FF            lock and dword ptr [rcx], 0xffffff7f
003C5B2F  41 83 FD 01                     cmp r13d, 1
003C5B33  76 24                           jbe 0x1403c5b59
003C5B35  48 8D 55 88                     lea rdx, [rbp - 0x78]
003C5B39  45 8D 45 FF                     lea r8d, [r13 - 1]
003C5B3D  48 8B 02                        mov rax, qword ptr [rdx]
003C5B40  48 3B C1                        cmp rax, rcx
003C5B43  74 0A                           je 0x1403c5b4f
003C5B45  48 8B C8                        mov rcx, rax
003C5B48  F0 81 20 7F FF FF FF            lock and dword ptr [rax], 0xffffff7f
003C5B4F  48 83 C2 08                     add rdx, 8
003C5B53  49 83 E8 01                     sub r8, 1
003C5B57  75 E4                           jne 0x1403c5b3d
003C5B59  49 8B BF C8 00 00 00            mov rdi, qword ptr [r15 + 0xc8]
003C5B60  33 C0                           xor eax, eax
003C5B62  44 8B C3                        mov r8d, ebx
003C5B65  49 89 87 D0 03 00 00            mov qword ptr [r15 + 0x3d0], rax
003C5B6C  49 8B D7                        mov rdx, r15
003C5B6F  49 8B CC                        mov rcx, r12
003C5B72  E8 39 B0 E5 FF                  call 0x140220bb0
003C5B77  8B C7                           mov eax, edi
003C5B79  48 8B 8D 88 01 00 00            mov rcx, qword ptr [rbp + 0x188]
003C5B80  48 33 CC                        xor rcx, rsp
003C5B83  E8 B8 6A 2E 00                  call 0x1406ac640
003C5B88  48 8B 9C 24 E0 02 00 00         mov rbx, qword ptr [rsp + 0x2e0]
003C5B90  48 81 C4 90 02 00 00            add rsp, 0x290
003C5B97  41 5F                           pop r15
003C5B99  41 5E                           pop r14
003C5B9B  41 5D                           pop r13
003C5B9D  41 5C                           pop r12
003C5B9F  5F                              pop rdi
003C5BA0  5E                              pop rsi
003C5BA1  5D                              pop rbp
003C5BA2  C3                              ret
003C5BA3  CC                              int3
003C5BA4  49 0F BE C4                     movsx rax, r12b
003C5BA8  42 80 7C 38 72 00               cmp byte ptr [rax + r15 + 0x72], 0
003C5BAE  0F 85 F8 02 00 00               jne 0x1403c5eac
003C5BB4  45 84 E4                        test r12b, r12b
003C5BB7  0F 84 FE FD FF FF               je 0x1403c59bb
003C5BBD  49 8D 87 A8 00 00 00            lea rax, [r15 + 0xa8]
003C5BC4  48 39 00                        cmp qword ptr [rax], rax
003C5BC7  0F 84 EE FD FF FF               je 0x1403c59bb
003C5BCD  41 80 8F C2 00 00 00 02         or byte ptr [r15 + 0xc2], 2
003C5BD5  BF C0 00 00 00                  mov edi, 0xc0
003C5BDA  45 33 E4                        xor r12d, r12d
003C5BDD  E9 E9 FD FF FF                  jmp 0x1403c59cb
003C5BE2  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
003C5BE7  49 8B CF                        mov rcx, r15
003C5BEA  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
003C5BEE  E8 0D 08 00 00                  call 0x1403c6400
003C5BF3  85 C0                           test eax, eax
003C5BF5  0F 84 F2 00 00 00               je 0x1403c5ced
003C5BFB  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
003C5BFF  F0 81 21 7F FF FF FF            lock and dword ptr [rcx], 0xffffff7f
003C5C06  41 83 FD 01                     cmp r13d, 1
003C5C0A  76 24                           jbe 0x1403c5c30
003C5C0C  48 8D 55 88                     lea rdx, [rbp - 0x78]
003C5C10  45 8D 45 FF                     lea r8d, [r13 - 1]
003C5C14  48 8B 02                        mov rax, qword ptr [rdx]
003C5C17  48 3B C1                        cmp rax, rcx
003C5C1A  74 0A                           je 0x1403c5c26
003C5C1C  48 8B C8                        mov rcx, rax
003C5C1F  F0 81 20 7F FF FF FF            lock and dword ptr [rax], 0xffffff7f
003C5C26  48 83 C2 08                     add rdx, 8
003C5C2A  49 83 E8 01                     sub r8, 1
003C5C2E  75 E4                           jne 0x1403c5c14
003C5C30  44 8B C3                        mov r8d, ebx
003C5C33  49 8B D7                        mov rdx, r15
003C5C36  49 8B CC                        mov rcx, r12
003C5C39  E8 72 AF E5 FF                  call 0x140220bb0
003C5C3E  BF 02 01 00 00                  mov edi, 0x102
003C5C43  E9 2F FF FF FF                  jmp 0x1403c5b77
003C5C48  41 F6 42 30 02                  test byte ptr [r10 + 0x30], 2
003C5C4D  0F 84 3A FE FF FF               je 0x1403c5a8d
003C5C53  4D 0F AB C5                     bts r13, r8
003C5C57  E9 31 FE FF FF                  jmp 0x1403c5a8d
003C5C5C  45 0F B6 84 24 BA 38 00 00      movzx r8d, byte ptr [r12 + 0x38ba]
003C5C65  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
003C5C69  4C 3B F8                        cmp r15, rax
003C5C6C  0F 84 D2 02 00 00               je 0x1403c5f44
003C5C72  83 7A 04 00                     cmp dword ptr [rdx + 4], 0
003C5C76  0F 8F 51 FE FF FF               jg 0x1403c5acd
003C5C7C  4C 3B F8                        cmp r15, rax
003C5C7F  0F 85 4F FE FF FF               jne 0x1403c5ad4
003C5C85  44 38 42 02                     cmp byte ptr [rdx + 2], r8b
003C5C89  0F 85 45 FE FF FF               jne 0x1403c5ad4
003C5C8F  E9 39 FE FF FF                  jmp 0x1403c5acd
003C5C94  83 6E 04 01                     sub dword ptr [rsi + 4], 1
003C5C98  0F 85 72 FE FF FF               jne 0x1403c5b10
003C5C9E  45 8B F5                        mov r14d, r13d
003C5CA1  F0 49 0F BA 6F 40 00            lock bts qword ptr [r15 + 0x40], 0
003C5CA8  73 1D                           jae 0x1403c5cc7
003C5CAA  41 FF C6                        inc r14d
003C5CAD  44 85 35 F8 F5 BF 00            test dword ptr [rip + 0xbff5f8], r14d
003C5CB4  0F 84 05 02 00 00               je 0x1403c5ebf
003C5CBA  F3 90                           pause
003C5CBC  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
003C5CC0  48 85 C0                        test rax, rax
003C5CC3  74 DC                           je 0x1403c5ca1
003C5CC5  EB E3                           jmp 0x1403c5caa
003C5CC7  4D 8B C4                        mov r8, r12
003C5CCA  49 8B D7                        mov rdx, r15
003C5CCD  48 8B CE                        mov rcx, rsi
003C5CD0  E8 BB 07 00 00                  call 0x1403c6490
003C5CD5  4D 89 6F 40                     mov qword ptr [r15 + 0x40], r13
003C5CD9  F6 46 30 02                     test byte ptr [rsi + 0x30], 2
003C5CDD  0F 85 20 02 00 00               jne 0x1403c5f03
003C5CE3  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
003C5CE8  E9 23 FE FF FF                  jmp 0x1403c5b10
003C5CED  44 8B C7                        mov r8d, edi
003C5CF0  45 85 ED                        test r13d, r13d
003C5CF3  0F 84 90 00 00 00               je 0x1403c5d89
003C5CF9  49 8B C3                        mov rax, r11
003C5CFC  0F 1F 40 00                     nop dword ptr [rax]
003C5D00  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
003C5D04  48 83 C1 08                     add rcx, 8
003C5D08  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
003C5D0C  48 39 0A                        cmp qword ptr [rdx], rcx
003C5D0F  74 5A                           je 0x1403c5d6b
003C5D11  B9 03 00 00 00                  mov ecx, 3
003C5D16  CD 29                           int 0x29
003C5D18  45 85 ED                        test r13d, r13d
003C5D1B  0F 85 2A FD FF FF               jne 0x1403c5a4b
003C5D21  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
003C5D26  E9 79 FD FF FF                  jmp 0x1403c5aa4
003C5D2B  8B 05 87 0D C0 00               mov eax, dword ptr [rip + 0xc00d87]
003C5D31  A8 40                           test al, 0x40
003C5D33  0F 84 FE FB FF FF               je 0x1403c5937
003C5D39  E8 52 97 F4 FF                  call 0x14030f490
003C5D3E  84 C0                           test al, al
003C5D40  0F 84 F1 FB FF FF               je 0x1403c5937
003C5D46  8B CF                           mov ecx, edi
003C5D48  E8 13 97 F4 FF                  call 0x14030f460
003C5D4D  E9 E7 FB FF FF                  jmp 0x1403c5939
003C5D52  41 8B C0                        mov eax, r8d
003C5D55  45 8B C2                        mov r8d, r10d
003C5D58  4C 89 5C C5 80                  mov qword ptr [rbp + rax*8 - 0x80], r11
003C5D5D  45 85 D2                        test r10d, r10d
003C5D60  0F 84 43 FB FF FF               je 0x1403c58a9
003C5D66  E9 2C FB FF FF                  jmp 0x1403c5897
003C5D6B  48 89 08                        mov qword ptr [rax], rcx
003C5D6E  41 FF C0                        inc r8d
003C5D71  48 89 50 08                     mov qword ptr [rax + 8], rdx
003C5D75  48 89 02                        mov qword ptr [rdx], rax
003C5D78  48 89 41 08                     mov qword ptr [rcx + 8], rax
003C5D7C  48 83 C0 30                     add rax, 0x30
003C5D80  45 3B C5                        cmp r8d, r13d
003C5D83  0F 82 77 FF FF FF               jb 0x1403c5d00
003C5D89  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
003C5D8D  F0 81 21 7F FF FF FF            lock and dword ptr [rcx], 0xffffff7f
003C5D94  41 83 FD 01                     cmp r13d, 1
003C5D98  76 24                           jbe 0x1403c5dbe
003C5D9A  48 8D 55 88                     lea rdx, [rbp - 0x78]
003C5D9E  45 8D 45 FF                     lea r8d, [r13 - 1]
003C5DA2  48 8B 02                        mov rax, qword ptr [rdx]
003C5DA5  48 3B C1                        cmp rax, rcx
003C5DA8  74 0A                           je 0x1403c5db4
003C5DAA  48 8B C8                        mov rcx, rax
003C5DAD  F0 81 20 7F FF FF FF            lock and dword ptr [rax], 0xffffff7f
003C5DB4  48 83 C2 08                     add rdx, 8
003C5DB8  49 83 E8 01                     sub r8, 1
003C5DBC  75 E4                           jne 0x1403c5da2
003C5DBE  45 33 E4                        xor r12d, r12d
003C5DC1  45 88 AF 4B 02 00 00            mov byte ptr [r15 + 0x24b], r13b
003C5DC8  41 8B F4                        mov esi, r12d
003C5DCB  4C 39 64 24 48                  cmp qword ptr [rsp + 0x48], r12
003C5DD0  0F 85 B9 01 00 00               jne 0x1403c5f8f
003C5DD6  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
003C5DDB  45 33 F6                        xor r14d, r14d
003C5DDE  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
003C5DE3  49 8B D3                        mov rdx, r11
003C5DE6  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
003C5DEB  49 8B CF                        mov rcx, r15
003C5DEE  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
003C5DF2  E8 E9 81 E4 FF                  call 0x14020dfe0
003C5DF7  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003C5DFC  48 8B F8                        mov rdi, rax
003C5DFF  41 8B DE                        mov ebx, r14d
003C5E02  A9 40 FF FF FF                  test eax, 0xffffff40
003C5E07  0F 84 EE 00 00 00               je 0x1403c5efb
003C5E0D  45 32 E4                        xor r12b, r12b
003C5E10  4D 89 B7 D0 03 00 00            mov qword ptr [r15 + 0x3d0], r14
003C5E17  48 85 F6                        test rsi, rsi
003C5E1A  0F 85 79 01 00 00               jne 0x1403c5f99
003C5E20  81 FF 00 01 00 00               cmp edi, 0x100
003C5E26  0F 85 4B FD FF FF               jne 0x1403c5b77
003C5E2C  44 0F 20 C7                     mov rdi, cr8
003C5E30  B8 02 00 00 00                  mov eax, 2
003C5E35  44 0F 22 C0                     mov cr8, rax
003C5E39  39 1D E1 0E C0 00               cmp dword ptr [rip + 0xc00ee1], ebx
003C5E3F  75 5D                           jne 0x1403c5e9e
003C5E41  44 0F B6 64 24 30               movzx r12d, byte ptr [rsp + 0x30]
003C5E47  41 88 BF 86 01 00 00            mov byte ptr [r15 + 0x186], dil
003C5E4E  E9 96 FA FF FF                  jmp 0x1403c58e9
003C5E53  66 45 39 B7 E6 01 00 00         cmp word ptr [r15 + 0x1e6], r14w
003C5E5B  0F 85 F0 FA FF FF               jne 0x1403c5951
003C5E61  40 80 FE 01                     cmp sil, 1
003C5E65  0F 83 E6 FA FF FF               jae 0x1403c5951
003C5E6B  B2 01                           mov dl, 1
003C5E6D  49 8B CF                        mov rcx, r15
003C5E70  E8 5B 07 00 00                  call 0x1403c65d0
003C5E75  45 33 C0                        xor r8d, r8d
003C5E78  33 D2                           xor edx, edx
003C5E7A  33 C9                           xor ecx, ecx
003C5E7C  E8 9F B0 E8 FF                  call 0x140250f20
003C5E81  44 0F 20 C1                     mov rcx, cr8
003C5E85  45 0F 22 C5                     mov cr8, r13
003C5E89  44 39 35 90 0E C0 00            cmp dword ptr [rip + 0xc00e90], r14d
003C5E90  75 55                           jne 0x1403c5ee7
003C5E92  41 88 B7 86 01 00 00            mov byte ptr [r15 + 0x186], sil
003C5E99  E9 5F FA FF FF                  jmp 0x1403c58fd
003C5E9E  0F B6 D0                        movzx edx, al
003C5EA1  40 0F B6 CF                     movzx ecx, dil
003C5EA5  E8 52 F8 12 00                  call 0x1404f56fc
003C5EAA  EB 95                           jmp 0x1403c5e41
003C5EAC  42 C6 44 38 72 00               mov byte ptr [rax + r15 + 0x72], 0
003C5EB2  BF 01 01 00 00                  mov edi, 0x101
003C5EB7  45 33 E4                        xor r12d, r12d
003C5EBA  E9 0C FB FF FF                  jmp 0x1403c59cb
003C5EBF  8B 05 F3 0B C0 00               mov eax, dword ptr [rip + 0xc00bf3]
003C5EC5  A8 40                           test al, 0x40
003C5EC7  0F 84 ED FD FF FF               je 0x1403c5cba
003C5ECD  E8 BE 95 F4 FF                  call 0x14030f490
003C5ED2  84 C0                           test al, al
003C5ED4  0F 84 E0 FD FF FF               je 0x1403c5cba
003C5EDA  41 8B CE                        mov ecx, r14d
003C5EDD  E8 7E 95 F4 FF                  call 0x14030f460
003C5EE2  E9 D5 FD FF FF                  jmp 0x1403c5cbc
003C5EE7  41 0F B6 D5                     movzx edx, r13b
003C5EEB  E8 0C F8 12 00                  call 0x1404f56fc
003C5EF0  EB A0                           jmp 0x1403c5e92
003C5EF2  44 89 6E 04                     mov dword ptr [rsi + 4], r13d
003C5EF6  E9 15 FC FF FF                  jmp 0x1403c5b10
003C5EFB  41 B4 01                        mov r12b, 1
003C5EFE  E9 0D FF FF FF                  jmp 0x1403c5e10
003C5F03  33 D2                           xor edx, edx
003C5F05  48 8B CE                        mov rcx, rsi
003C5F08  44 8D 42 01                     lea r8d, [rdx + 1]
003C5F0C  E8 1F A3 E4 FF                  call 0x140210230
003C5F11  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
003C5F16  48 85 C0                        test rax, rax
003C5F19  0F 84 F1 FB FF FF               je 0x1403c5b10
003C5F1F  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
003C5F23  E9 E8 FB FF FF                  jmp 0x1403c5b10
003C5F28  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003C5F31  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
003C5F36  44 0F B6 C6                     movzx r8d, sil
003C5F3A  E8 C1 A8 E8 FF                  call 0x140250800
003C5F3F  E9 33 FC FF FF                  jmp 0x1403c5b77
003C5F44  44 38 42 02                     cmp byte ptr [rdx + 2], r8b
003C5F48  0F 85 24 FD FF FF               jne 0x1403c5c72
003C5F4E  81 7A 04 00 00 00 80            cmp dword ptr [rdx + 4], 0x80000000
003C5F55  0F 85 17 FD FF FF               jne 0x1403c5c72
003C5F5B  41 8B D5                        mov edx, r13d
003C5F5E  48 8D 4D 80                     lea rcx, [rbp - 0x80]
003C5F62  E8 85 B2 09 00                  call 0x1404611ec
003C5F67  44 8B C3                        mov r8d, ebx
003C5F6A  49 8B D7                        mov rdx, r15
003C5F6D  49 8B CC                        mov rcx, r12
003C5F70  E8 3B AC E5 FF                  call 0x140220bb0
003C5F75  B9 91 01 00 C0                  mov ecx, 0xc0000191
003C5F7A  E8 D1 0A F3 FF                  call 0x1402f6a50
003C5F7F  CC                              int3
003C5F80  41 C6 47 72 00                  mov byte ptr [r15 + 0x72], 0
003C5F85  BF 01 01 00 00                  mov edi, 0x101
003C5F8A  E9 3C FA FF FF                  jmp 0x1403c59cb
003C5F8F  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
003C5F94  E9 6D 21 32 00                  jmp 0x1406e8106
003C5F99  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
003C5F9E  E9 C5 21 32 00                  jmp 0x1406e8168
003C5FA3  FF 4E 04                        dec dword ptr [rsi + 4]
003C5FA6  E9 65 FB FF FF                  jmp 0x1403c5b10
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiWaitForAllObjects(int a1, __int64 a2, int a3, unsigned __int8 a4, unsigned __int8 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m294;
    unsigned __int8 v_stack_m298;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (656);
    result = (*(unsigned __int64 *)(v_rip + 10768154)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m270 = a3;
    v_rdi = 0;
    v_stack_m290 = a2;
    v_stack_m294 = a1;
    a2 = 0;
    v_stack_m260 = a7;
    v_stack_m258 = 0;
    v_stack_m298 = a4;
    result = memset(v_stack_m240, a2, 504, a4);
    v_stack_m288 = 0;
    v_stack_m248 = *(unsigned __int64 *)(a2);
    if (((unsigned int)((unsigned int)(a1))) <= 1) goto loc_003C58BC;
loc_003C5891:
loc_003C5897:
    if ((*(unsigned __int64 *)(v_stack_m1C8 + 1 - 1 * 8 - 128)) > (*(unsigned __int64 *)(a2 + 8))) goto loc_003C5D52;
loc_003C58A9:
    a1 = (unsigned int)((1) + 1);
    a2 = (a2 + 8) + (8);
    *(unsigned __int64 *)(v_stack_m1C8 + 1 * 8 - 128) = *(unsigned __int64 *)(a2 + 8);
    if (a1 < ((unsigned int)((unsigned int)(a1)))) goto loc_003C5891;
loc_003C58BC:
    v_stack_m250 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m2A8 = v_stack_m288;
    a3 = 0;
    result = KiCheckWaitNext(*(unsigned __int64 *)(gs_base + (0 + 392)), a6, a3, v_stack_m258);
loc_003C58E9:
    v_r14 = 0;
    v_stack_m278 = 0;
loc_003C58FD:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 112) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 391) = a4;
    if (a5 != 0) {
    }
loc_003C5920:
    if (a5 >= 0) goto loc_003C5944;
loc_003C5929:
    v_rdi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12581243)) & ((unsigned int)(v_rdi))) == 0) goto loc_003C5D2B;
loc_003C5937:
loc_003C5939:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_003C5920;
    goto loc_003C5929;
loc_003C5944:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 193)) != 0) goto loc_003C5E53;
loc_003C5951:
    if (a5 != 0) goto loc_003C5BA4;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (2)) == 0) goto loc_003C59CF;
    if (a4 == 0) goto loc_003C59CF;
    v_r12 = 0;
loc_003C597F:
    result = KiPerformWaitDeferredWork(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 1, v_stack_m278);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    if ((unsigned int)(result) != 0) goto loc_003C5F28;
    if ((*(unsigned int *)(v_rip + 12587901)) != ((unsigned int)(result))) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, v_stack_m278);
    }
    goto loc_003C5B77;
loc_003C59BB:
    v_r12 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 114)) != 0) goto loc_003C5F80;
loc_003C59CB:
    if (0 != 0) goto loc_003C597F;
loc_003C59CF:
    v_rdi = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 388) = 5;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = (unsigned __int8)((unsigned int)(v_stack_m270));
    v_stack_m280 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 436) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m270))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    result = KiAcquireKobjectLockSafe(v_stack_m248, a2, 1, v_stack_m278);
    if (((unsigned int)((unsigned int)(v_stack_m294))) <= 1) goto loc_003C5D18;
loc_003C5A27:
    result = *(unsigned __int64 *)(v_stack_m240);
    v_rsi = v_stack_m248;
    if ((*(unsigned __int64 *)(v_stack_m240)) != v_stack_m248) {
        a1 = *(unsigned __int64 *)(v_stack_m240);
        v_rsi = *(unsigned __int64 *)(v_stack_m240);
        result = KiAcquireKobjectLockSafe(a1, a2, 1, v_stack_m278);
    }
    v_rdi = (v_stack_m240) + (8);
    v_r14 = ((unsigned int)(v_stack_m294) - 1) - (1);
    if (condition_is_not_equal) goto loc_003C5A27;
    v_rdi = 0;
loc_003C5A4B:
loc_003C5A62:
    *(unsigned __int8 *)(v_stack_m260 + 17 - 1) = 0;
    *(unsigned __int8 *)(v_stack_m260 + 17) = 4;
    *(unsigned __int64 *)(v_stack_m260 + 17 + 15) = *(unsigned __int64 *)(v_stack_m290);
    *(unsigned __int16 *)(v_stack_m260 + 17 + 1) = 0;
    *(unsigned __int64 *)(v_stack_m260 + 17 + 7) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m290))) & (127));
    if (((unsigned __int8)(result)) == 2) goto loc_003C5C48;
loc_003C5A8D:
    a3 = (0) + 1;
    a2 = (v_stack_m290) + (8);
    a4 = ((unsigned int)(v_stack_m294)) - (1);
    if (condition_is_not_equal) goto loc_003C5A62;
    v_stack_m280 = v_stack_m280;
loc_003C5AA4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 200) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 976) = 0;
loc_003C5AB4:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m290 + 0 * 8))) & (127));
    if (((unsigned __int8)(result)) == 2) goto loc_003C5C5C;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m290 + 0 * 8) + 4)) <= 0) goto loc_003C5AD4;
loc_003C5ACD:
    a1 = (unsigned int)((0) + 1);
    if (a1 < ((unsigned int)((unsigned int)(v_stack_m294)))) goto loc_003C5AB4;
loc_003C5AD4:
    if (a1 != ((unsigned int)((unsigned int)(v_stack_m294)))) goto loc_003C5BE2;
    if ((unsigned int)((unsigned int)(v_stack_m294)) == 0) goto loc_003C5B24;
    v_r13 = 0;
loc_003C5AE8:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m290)))) & (7));
    if (((unsigned __int8)(result)) == 1) goto loc_003C5EF2;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m290))) & (127));
    if (((unsigned __int8)(a1)) == 5) goto loc_003C5FA3;
    if (((unsigned __int8)(a1)) == 2) goto loc_003C5C94;
loc_003C5B10:
    v_r14 = (v_stack_m290) + (8);
    v_stack_m290 = v_r14;
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m294)))) - (1);
    if (condition_is_not_equal) goto loc_003C5AE8;
loc_003C5B24:
    if (((unsigned int)((unsigned int)(v_stack_m294))) <= 1) goto loc_003C5B59;
loc_003C5B3D:
    if ((*(unsigned __int64 *)(v_stack_m240)) != v_stack_m248) {
        a1 = *(unsigned __int64 *)(v_stack_m240);
    }
    a2 = (v_stack_m240) + (8);
    a3 = ((unsigned int)(v_stack_m294) - 1) - (1);
    if (condition_is_not_equal) goto loc_003C5B3D;
loc_003C5B59:
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 976) = 0;
    result = KiFastExitThreadWait(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
loc_003C5B77:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    v_rsp = (v_rsp) + (656);
    return result;
loc_003C5BA4:
    if ((*(unsigned __int8 *)((__int8)((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)))) + *(unsigned __int64 *)(gs_base + (0 + 392)) * 1 + 114)) != 0) goto loc_003C5EAC;
    if ((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32))) == 0) goto loc_003C59BB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 168)) == (*(unsigned __int64 *)(gs_base + (0 + 392)) + 168)) goto loc_003C59BB;
    v_r12 = 0;
    goto loc_003C59CB;
loc_003C5BE2:
    result = KiCheckDueTimeExpired(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(v_stack_p40), v_stack_p70, a4);
    if ((unsigned int)(result) == 0) goto loc_003C5CED;
    if (((unsigned int)((unsigned int)(v_stack_m294))) <= 1) goto loc_003C5C30;
loc_003C5C14:
    if ((*(unsigned __int64 *)(v_stack_m240)) != v_stack_m248) {
        a1 = *(unsigned __int64 *)(v_stack_m240);
    }
    a2 = (v_stack_m240) + (8);
    a3 = ((unsigned int)(v_stack_m294) - 1) - (1);
    if (condition_is_not_equal) goto loc_003C5C14;
loc_003C5C30:
    result = KiFastExitThreadWait(0, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)(v_stack_p18)), a4);
    goto loc_003C5B77;
loc_003C5C48:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m290) + 48)) & (2)) == 0) goto loc_003C5A8D;
    goto loc_003C5A8D;
loc_003C5C5C:
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40))) goto loc_003C5F44;
loc_003C5C72:
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 4)) > 0) goto loc_003C5ACD;
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40))) goto loc_003C5AD4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 14522)))) goto loc_003C5AD4;
    goto loc_003C5ACD;
loc_003C5C94:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 14522)))) goto loc_003C5B10;
loc_003C5CA1:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) >= ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 14522)))) goto loc_003C5CC7;
loc_003C5CAA:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m294)))) + 1);
    if (((*(unsigned int *)(v_rip + 12580344)) & ((unsigned int)(v_r14))) == 0) goto loc_003C5EBF;
loc_003C5CBA:
loc_003C5CBC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_003C5CA1;
    goto loc_003C5CAA;
loc_003C5CC7:
    result = KiWaitSatisfyMutant(*(unsigned __int64 *)(v_stack_m290), *(unsigned __int64 *)(gs_base + (0 + 392)), 0, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = (unsigned int)(v_stack_m294);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m290) + 48)) & (2)) != 0) goto loc_003C5F03;
    goto loc_003C5B10;
loc_003C5CED:
    if ((unsigned int)((unsigned int)(v_stack_m294)) == 0) goto loc_003C5D89;
loc_003C5D00:
    a1 = (*(unsigned __int64 *)(v_stack_m260 + 32)) + (8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) == a1) goto loc_003C5D6B;
loc_003C5D18:
    if ((unsigned int)((unsigned int)(v_stack_m294)) != 0) goto loc_003C5A4B;
    goto loc_003C5AA4;
loc_003C5D2B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12586375)))) & (64)) == 0) goto loc_003C5937;
    result = KiCheckVpBackingLongSpinWaitHypercall(3, *(unsigned __int64 *)(a1 + 8), 258, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003C5937;
    result = HvlNotifyLongSpinWait(258, *(unsigned __int64 *)(a1 + 8), 258, a4);
    goto loc_003C5939;
loc_003C5D52:
    *(unsigned __int64 *)(v_stack_m1C8 + 258 * 8 - 128) = v_stack_p68;
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m290)) == 0) goto loc_003C58A9;
    goto loc_003C5897;
loc_003C5D6B:
    *(unsigned __int64 *)(258) = 258;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m290)))) + 1);
    *(unsigned __int64 *)(258 + 8) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) = 258;
    *(unsigned __int64 *)(258 + 8) = 258;
    result = (258) + (48);
    if (a3 < ((unsigned int)((unsigned int)(v_stack_m294)))) goto loc_003C5D00;
loc_003C5D89:
    if (((unsigned int)((unsigned int)(v_stack_m294))) <= 1) goto loc_003C5DBE;
loc_003C5DA2:
    if ((*(unsigned __int64 *)(v_stack_m240)) != v_stack_m248) {
        a1 = *(unsigned __int64 *)(v_stack_m240);
    }
    a2 = (v_stack_m240) + (8);
    a3 = ((unsigned int)(v_stack_m294) - 1) - (1);
    if (condition_is_not_equal) goto loc_003C5DA2;
loc_003C5DBE:
    v_r12 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 587) = (unsigned __int8)((unsigned int)(v_stack_m294));
    if (v_stack_p48 != 0) goto loc_003C5F8F;
    v_r14 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned int)(v_stack_p18);
    result = KiCommitThreadWait(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_p68, (unsigned int)(v_stack_p40), v_stack_p70);
    v_stack_p48 = result;
    if ((((unsigned int)(result)) & (0xFFFFFF40ULL)) == 0) goto loc_003C5EFB;
    v_r12 = 0;
loc_003C5E10:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 976) = 0;
    if (0 != 0) goto loc_003C5F99;
    if (((unsigned int)(result)) != 256) goto loc_003C5B77;
    if ((*(unsigned int *)(v_rip + 12586721)) != 0) goto loc_003C5E9E;
loc_003C5E41:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390));
    goto loc_003C58E9;
loc_003C5E53:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_003C5951;
    if (0 >= 1) goto loc_003C5951;
    result = KiReleaseThreadLockLowerIrql(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, (unsigned int)(v_stack_p40), v_stack_p70);
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = KiDeliverApc(a1, a2, a3, v_stack_p70);
    if ((*(unsigned int *)(v_rip + 12586640)) != 0) goto loc_003C5EE7;
loc_003C5E92:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = 0;
    goto loc_003C58FD;
loc_003C5E9E:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390)), (unsigned __int8)(result), a3, v_stack_p70);
    goto loc_003C5E41;
loc_003C5EAC:
    *(unsigned __int8 *)(result + *(unsigned __int64 *)(gs_base + (0 + 392)) * 1 + 114) = 0;
    v_r12 = 0;
    goto loc_003C59CB;
loc_003C5EBF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12585971)))) & (64)) == 0) goto loc_003C5CBA;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390)), (unsigned __int8)(result), a3, v_stack_p70);
    if ((unsigned __int8)(result) == 0) goto loc_003C5CBA;
    result = HvlNotifyLongSpinWait(0, (unsigned __int8)(result), a3, v_stack_p70);
    goto loc_003C5CBC;
loc_003C5EE7:
    result = KiRaiseIrqlProcessIrqlFlags(0, (unsigned __int8)((unsigned int)(v_stack_m294)), a3, v_stack_p70);
    goto loc_003C5E92;
loc_003C5EF2:
    *(unsigned int *)(0 + 4) = (unsigned int)((unsigned int)(v_stack_m294));
    goto loc_003C5B10;
loc_003C5EFB:
    goto loc_003C5E10;
loc_003C5F03:
    a2 = 0;
    result = KeAbPreAcquire(0, a2, a2 + 1, v_stack_p70);
    if (result == 0) goto loc_003C5B10;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_003C5B10;
loc_003C5F28:
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_p50, 0, v_stack_p70);
    goto loc_003C5B77;
loc_003C5F44:
    if ((*(unsigned __int8 *)(v_stack_p50 + 2)) != 0) goto loc_003C5C72;
    if ((*(unsigned int *)(v_stack_p50 + 4)) != 0x80000000ULL) goto loc_003C5C72;
    result = KiUnlockKobjectArray(v_stack_m248, (unsigned int)((unsigned int)((unsigned int)(v_stack_m294))), 0, v_stack_p70);
    result = KiFastExitThreadWait(1, *(unsigned __int64 *)(gs_base + (0 + 392)), 0, v_stack_p70);
    result = RtlRaiseStatus((unsigned int)(0xC0000191ULL), *(unsigned __int64 *)(gs_base + (0 + 392)), 0, v_stack_p70);
loc_003C5F80:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 114) = 0;
    goto loc_003C59CB;
loc_003C5F8F:
loc_003C5F99:
loc_003C5FA3:
    goto loc_003C5B10;
}
```

## 5. (Beta) C Style

```c
int64_t KiWaitForAllObjects(int32_t Arg1, void *Arg2, int32_t Arg3, uint8_t Arg4, uint8_t Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint32_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint32_t v_stack_m294;
    uint8_t v_stack_m298;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m40;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (656);
    result = (*(uint64_t *)(v_rip + 0xA44F1A)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m270 = Arg3;
    local_rdi = 0;
    v_stack_m290 = Arg2;
    v_stack_m294 = Arg1;
    Arg2 = 0;
    v_stack_m260 = Arg7;
    v_stack_m258 = 0;
    v_stack_m298 = Arg4;
    result = memset(v_stack_m240, Arg2, 504, Arg4);
    v_stack_m288 = 0;
    v_stack_m248 = *(uint64_t *)(arg2);
    if (((uint32_t)((uint32_t)(Arg1))) <= 1) goto loc_003C58BC;
loc_003C5891:
loc_003C5897:
    if ((*(uint64_t *)(v_stack_m1C8 + 0x1 - 0x1 * 8 - 0x80)) > (*(uint64_t *)(arg2 + 0x8))) goto loc_003C5D52;
loc_003C58A9:
    Arg1 = (uint32_t)((1) + 1);
    Arg2 = (Arg2 + 8) + (8);
    *(uint64_t *)(v_stack_m1C8 + 0x1 * 8 - 0x80) = *(uint64_t *)(arg2 + 0x8);
    if (Arg1 < ((uint32_t)((uint32_t)(Arg1)))) goto loc_003C5891;
loc_003C58BC:
    v_stack_m250 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m2A8 = v_stack_m288;
    Arg3 = 0;
    result = KiCheckWaitNext(*(uint64_t *)(gs_base + (0 + 0x188)), Arg6, Arg3, v_stack_m258);
loc_003C58E9:
    local_r14 = 0;
    v_stack_m278 = 0;
loc_003C58FD:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x70) = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x187) = Arg4;
    if (Arg5 != 0) {
    }
loc_003C5920:
    if (Arg5 >= 0) goto loc_003C5944;
loc_003C5929:
    local_rdi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xBFF97B)) & ((uint32_t)(local_rdi))) == 0) goto loc_003C5D2B;
loc_003C5937:
loc_003C5939:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_003C5920;
    goto loc_003C5929;
loc_003C5944:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC1)) != 0) goto loc_003C5E53;
loc_003C5951:
    if (Arg5 != 0) goto loc_003C5BA4;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (2)) == 0) goto loc_003C59CF;
    if (Arg4 == 0) goto loc_003C59CF;
    local_r12 = 0;
loc_003C597F:
    result = KiPerformWaitDeferredWork(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 1, v_stack_m278);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    if ((uint32_t)(result) != 0) goto loc_003C5F28;
    if ((*(uint32_t *)(v_rip + 0xC0137D)) != ((uint32_t)(result))) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, v_stack_m278);
    }
    goto loc_003C5B77;
loc_003C59BB:
    local_r12 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x72)) != 0) goto loc_003C5F80;
loc_003C59CB:
    if (0 != 0) goto loc_003C597F;
loc_003C59CF:
    local_rdi = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x184) = 5;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = (uint8_t)((uint32_t)(v_stack_m270));
    v_stack_m280 = 0;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1B4) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m270))));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    result = KiAcquireKobjectLockSafe(v_stack_m248, Arg2, 1, v_stack_m278);
    if (((uint32_t)((uint32_t)(v_stack_m294))) <= 1) goto loc_003C5D18;
loc_003C5A27:
    result = *(uint64_t *)(v_stack_m240);
    local_rsi = v_stack_m248;
    if ((*(uint64_t *)(v_stack_m240)) != v_stack_m248) {
        Arg1 = *(uint64_t *)(v_stack_m240);
        local_rsi = *(uint64_t *)(v_stack_m240);
        result = KiAcquireKobjectLockSafe(Arg1, Arg2, 1, v_stack_m278);
    }
    local_rdi = (v_stack_m240) + (8);
    local_r14 = ((uint32_t)(v_stack_m294) - 1) - (1);
    if (condition_is_not_equal) goto loc_003C5A27;
    local_rdi = 0;
loc_003C5A4B:
loc_003C5A62:
    *(uint8_t *)(v_stack_m260 + 0x11 - 0x1) = 0;
    *(uint8_t *)(v_stack_m260 + 0x11) = 4;
    *(uint64_t *)(v_stack_m260 + 0x11 + 0xF) = *(uint64_t *)(v_stack_m290);
    *(uint16_t *)(v_stack_m260 + 0x11 + 0x1) = 0;
    *(uint64_t *)(v_stack_m260 + 0x11 + 0x7) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m290))) & (127));
    if (((uint8_t)(result)) == 2) goto loc_003C5C48;
loc_003C5A8D:
    Arg3 = (0) + 1;
    Arg2 = (v_stack_m290) + (8);
    Arg4 = ((uint32_t)(v_stack_m294)) - (1);
    if (condition_is_not_equal) goto loc_003C5A62;
    v_stack_m280 = v_stack_m280;
loc_003C5AA4:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC8) = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3D0) = 0;
loc_003C5AB4:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m290 + 0x0 * 8))) & (127));
    if (((uint8_t)(result)) == 2) goto loc_003C5C5C;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m290 + 0x0 * 8) + 0x4)) <= 0) goto loc_003C5AD4;
loc_003C5ACD:
    Arg1 = (uint32_t)((0) + 1);
    if (Arg1 < ((uint32_t)((uint32_t)(v_stack_m294)))) goto loc_003C5AB4;
loc_003C5AD4:
    if (Arg1 != ((uint32_t)((uint32_t)(v_stack_m294)))) goto loc_003C5BE2;
    if ((uint32_t)((uint32_t)(v_stack_m294)) == 0) goto loc_003C5B24;
    local_r13 = 0;
loc_003C5AE8:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m290)))) & (7));
    if (((uint8_t)(result)) == 1) goto loc_003C5EF2;
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m290))) & (127));
    if (((uint8_t)(Arg1)) == 5) goto loc_003C5FA3;
    if (((uint8_t)(Arg1)) == 2) goto loc_003C5C94;
loc_003C5B10:
    local_r14 = (v_stack_m290) + (8);
    v_stack_m290 = local_r14;
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m294)))) - (1);
    if (condition_is_not_equal) goto loc_003C5AE8;
loc_003C5B24:
    if (((uint32_t)((uint32_t)(v_stack_m294))) <= 1) goto loc_003C5B59;
loc_003C5B3D:
    if ((*(uint64_t *)(v_stack_m240)) != v_stack_m248) {
        Arg1 = *(uint64_t *)(v_stack_m240);
    }
    Arg2 = (v_stack_m240) + (8);
    Arg3 = ((uint32_t)(v_stack_m294) - 1) - (1);
    if (condition_is_not_equal) goto loc_003C5B3D;
loc_003C5B59:
    result = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3D0) = 0;
    result = KiFastExitThreadWait(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
loc_003C5B77:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
    local_rsp = (local_rsp) + (656);
    return result;
loc_003C5BA4:
    if ((*(uint8_t *)((int8_t)((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)))) + *(uint64_t *)(gs_base + (0 + 0x188)) * 1 + 0x72)) != 0) goto loc_003C5EAC;
    if ((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20))) == 0) goto loc_003C59BB;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xA8)) == (*(uint64_t *)(gs_base + (0 + 0x188)) + 168)) goto loc_003C59BB;
    local_r12 = 0;
    goto loc_003C59CB;
loc_003C5BE2:
    result = KiCheckDueTimeExpired(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(v_stack_p40), v_stack_p70, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003C5CED;
    if (((uint32_t)((uint32_t)(v_stack_m294))) <= 1) goto loc_003C5C30;
loc_003C5C14:
    if ((*(uint64_t *)(v_stack_m240)) != v_stack_m248) {
        Arg1 = *(uint64_t *)(v_stack_m240);
    }
    Arg2 = (v_stack_m240) + (8);
    Arg3 = ((uint32_t)(v_stack_m294) - 1) - (1);
    if (condition_is_not_equal) goto loc_003C5C14;
loc_003C5C30:
    result = KiFastExitThreadWait(0, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)(v_stack_p18)), Arg4);
    goto loc_003C5B77;
loc_003C5C48:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m290) + 0x30)) & (2)) == 0) goto loc_003C5A8D;
    goto loc_003C5A8D;
loc_003C5C5C:
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28))) goto loc_003C5F44;
loc_003C5C72:
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x4)) > 0) goto loc_003C5ACD;
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28))) goto loc_003C5AD4;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) != ((uint8_t)(*(uint8_t *)(local_r12 + 0x38BA)))) goto loc_003C5AD4;
    goto loc_003C5ACD;
loc_003C5C94:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) != ((uint8_t)(*(uint8_t *)(local_r12 + 0x38BA)))) goto loc_003C5B10;
loc_003C5CA1:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) >= ((uint8_t)(*(uint8_t *)(local_r12 + 0x38BA)))) goto loc_003C5CC7;
loc_003C5CAA:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m294)))) + 1);
    if (((*(uint32_t *)(v_rip + 0xBFF5F8)) & ((uint32_t)(local_r14))) == 0) goto loc_003C5EBF;
loc_003C5CBA:
loc_003C5CBC:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_003C5CA1;
    goto loc_003C5CAA;
loc_003C5CC7:
    result = KiWaitSatisfyMutant(*(uint64_t *)(v_stack_m290), *(uint64_t *)(gs_base + (0 + 0x188)), 0, Arg4);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = (uint32_t)(v_stack_m294);
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m290) + 0x30)) & (2)) != 0) goto loc_003C5F03;
    goto loc_003C5B10;
loc_003C5CED:
    if ((uint32_t)((uint32_t)(v_stack_m294)) == 0) goto loc_003C5D89;
loc_003C5D00:
    Arg1 = (*(uint64_t *)(v_stack_m260 + 0x20)) + (8);
    if ((*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8))) == Arg1) goto loc_003C5D6B;
loc_003C5D18:
    if ((uint32_t)((uint32_t)(v_stack_m294)) != 0) goto loc_003C5A4B;
    goto loc_003C5AA4;
loc_003C5D2B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC00D87)))) & (64)) == 0) goto loc_003C5937;
    result = KiCheckVpBackingLongSpinWaitHypercall(3, *(uint64_t *)(Arg1 + 0x8), 258, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003C5937;
    result = HvlNotifyLongSpinWait(258, *(uint64_t *)(Arg1 + 0x8), 258, Arg4);
    goto loc_003C5939;
loc_003C5D52:
    *(uint64_t *)(v_stack_m1C8 + 0x102 * 8 - 0x80) = v_stack_p68;
    if ((uint32_t)(*(uint64_t *)(v_stack_m290)) == 0) goto loc_003C58A9;
    goto loc_003C5897;
loc_003C5D6B:
    *(uint64_t *)(258) = 258;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m290)))) + 1);
    *(uint64_t *)(258 + 0x8) = *(uint64_t *)(Arg1 + 0x8);
    *(uint64_t *)(*(uint64_t *)(Arg1 + 0x8)) = 258;
    *(uint64_t *)(258 + 0x8) = 258;
    result = (258) + (48);
    if (Arg3 < ((uint32_t)((uint32_t)(v_stack_m294)))) goto loc_003C5D00;
loc_003C5D89:
    if (((uint32_t)((uint32_t)(v_stack_m294))) <= 1) goto loc_003C5DBE;
loc_003C5DA2:
    if ((*(uint64_t *)(v_stack_m240)) != v_stack_m248) {
        Arg1 = *(uint64_t *)(v_stack_m240);
    }
    Arg2 = (v_stack_m240) + (8);
    Arg3 = ((uint32_t)(v_stack_m294) - 1) - (1);
    if (condition_is_not_equal) goto loc_003C5DA2;
loc_003C5DBE:
    local_r12 = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24B) = (uint8_t)((uint32_t)(v_stack_m294));
    if (v_stack_p48 != 0) goto loc_003C5F8F;
    local_r14 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = (uint32_t)(v_stack_p18);
    result = KiCommitThreadWait(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_p68, (uint32_t)(v_stack_p40), v_stack_p70);
    v_stack_p48 = result;
    if ((((uint32_t)(result)) & (0xFFFFFF40ULL)) == 0) goto loc_003C5EFB;
    local_r12 = 0;
loc_003C5E10:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3D0) = 0;
    if (0 != 0) goto loc_003C5F99;
    if (((uint32_t)(result)) != 256) goto loc_003C5B77;
    if ((*(uint32_t *)(v_rip + 0xC00EE1)) != 0) goto loc_003C5E9E;
loc_003C5E41:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186));
    goto loc_003C58E9;
loc_003C5E53:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_003C5951;
    if (0 >= 1) goto loc_003C5951;
    result = KiReleaseThreadLockLowerIrql(*(uint64_t *)(gs_base + (0 + 0x188)), 1, (uint32_t)(v_stack_p40), v_stack_p70);
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = KiDeliverApc(Arg1, Arg2, Arg3, v_stack_p70);
    if ((*(uint32_t *)(v_rip + 0xC00E90)) != 0) goto loc_003C5EE7;
loc_003C5E92:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = 0;
    goto loc_003C58FD;
loc_003C5E9E:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186)), (uint8_t)(result), Arg3, v_stack_p70);
    goto loc_003C5E41;
loc_003C5EAC:
    *(uint8_t *)(result + *(uint64_t *)(gs_base + (0 + 0x188)) * 1 + 0x72) = 0;
    local_r12 = 0;
    goto loc_003C59CB;
loc_003C5EBF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC00BF3)))) & (64)) == 0) goto loc_003C5CBA;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186)), (uint8_t)(result), Arg3, v_stack_p70);
    if ((uint8_t)(result) == 0) goto loc_003C5CBA;
    result = HvlNotifyLongSpinWait(0, (uint8_t)(result), Arg3, v_stack_p70);
    goto loc_003C5CBC;
loc_003C5EE7:
    result = KiRaiseIrqlProcessIrqlFlags(0, (uint8_t)((uint32_t)(v_stack_m294)), Arg3, v_stack_p70);
    goto loc_003C5E92;
loc_003C5EF2:
    *(uint32_t *)(0 + 0x4) = (uint32_t)((uint32_t)(v_stack_m294));
    goto loc_003C5B10;
loc_003C5EFB:
    goto loc_003C5E10;
loc_003C5F03:
    Arg2 = 0;
    result = KeAbPreAcquire(0, Arg2, Arg2 + 1, v_stack_p70);
    if (result == 0) goto loc_003C5B10;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_003C5B10;
loc_003C5F28:
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_p50, 0, v_stack_p70);
    goto loc_003C5B77;
loc_003C5F44:
    if ((*(uint8_t *)(v_stack_p50 + 0x2)) != 0) goto loc_003C5C72;
    if ((*(uint32_t *)(v_stack_p50 + 0x4)) != 0x80000000ULL) goto loc_003C5C72;
    result = KiUnlockKobjectArray(v_stack_m248, (uint32_t)((uint32_t)((uint32_t)(v_stack_m294))), 0, v_stack_p70);
    result = KiFastExitThreadWait(1, *(uint64_t *)(gs_base + (0 + 0x188)), 0, v_stack_p70);
    result = RtlRaiseStatus((uint32_t)(0xC0000191ULL), *(uint64_t *)(gs_base + (0 + 0x188)), 0, v_stack_p70);
loc_003C5F80:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x72) = 0;
    goto loc_003C59CB;
loc_003C5F8F:
loc_003C5F99:
loc_003C5FA3:
    goto loc_003C5B10;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C5800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
