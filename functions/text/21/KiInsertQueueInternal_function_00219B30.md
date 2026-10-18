# KiInsertQueueInternal

- RVA: `0x00219B30`–`0x00219E73` (길이 `835` bytes)
- VA: `0x0000000140219B30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005EC18`
- 디코드: `209`개 명령, `835/835` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **33**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00219C2E` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x00219CDF` → [KiWakeOtherQueueWaiters](../39/KiWakeOtherQueueWaiters_function_003964D0.md) (function, `0x003964D0`)
- `0x00219D57` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00219D74` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00219D80` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00219D8A` → [KeIsThreadRunning](../39/KeIsThreadRunning_function_00396720.md) (function, `0x00396720`)
- `0x00219D98` → [EtwTraceEnqueueWork](../39/EtwTraceEnqueueWork_function_0039674C.md) (function, `0x0039674C`)
- `0x00219E10` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00219E1B` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [KiResumeThread](../20/KiResumeThread_function_00203644.md) at `0x00203880`
- [sub_0021A01D](Unknown_function_0021A01D.md) at `0x0021A03D`
- [KiRetireDpcList](KiRetireDpcList_function_0021A0B0.md) at `0x0021ABCC`
- [KiTimerWaitTest](../23/KiTimerWaitTest_function_002337D0.md) at `0x00233A46`
- [KiTimerWaitTest](../23/KiTimerWaitTest_function_002337D0.md) at `0x00233AB9`
- [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) at `0x00250579`
- [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) at `0x00250C68`
- [FsRtlReleaseHeaderMutex](../25/FsRtlReleaseHeaderMutex_function_002516C0.md) at `0x002518DE`
- [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) at `0x00251BB7`
- [sub_0025E5F6](../25/Unknown_function_0025E5F6.md) at `0x0025E905`
- [sub_0025E5F6](../25/Unknown_function_0025E5F6.md) at `0x0025EA5A`
- [sub_00260366](../26/Unknown_function_00260366.md) at `0x00260B23`
- [sub_00260366](../26/Unknown_function_00260366.md) at `0x00260C8E`
- [ExReleaseFastResource](../26/ExReleaseFastResource_function_002613D0.md) at `0x00261A11`
- [sub_00261DFE](../26/Unknown_function_00261DFE.md) at `0x0026219B`
- [sub_002630C6](../26/Unknown_function_002630C6.md) at `0x002630FD`
- [sub_0027475D](../27/Unknown_function_0027475D.md) at `0x00274F7B`
- [sub_0027475D](../27/Unknown_function_0027475D.md) at `0x0027510D`
- [sub_00286720](../28/Unknown_function_00286720.md) at `0x00286742`
- [KeSignalGate](../2C/KeSignalGate_function_002C748C.md) at `0x002C759B`
- [sub_0033F84B](../33/Unknown_function_0033F84B.md) at `0x0033F85E`
- [sub_0033F84B](../33/Unknown_function_0033F84B.md) at `0x0033F8AB`
- [KeReleaseSemaphoreEx](../34/KeReleaseSemaphoreEx_function_003468C0.md) at `0x00346B08`
- [KeWakeWaitChain](../34/KeWakeWaitChain_function_0034F8C0.md) at `0x0034FA90`
- [KeSetEventBoostPriorityEx](../35/KeSetEventBoostPriorityEx_function_00350148.md) at `0x003502AF`
- [MiReturnWsToExpansionList](../35/MiReturnWsToExpansionList_function_003504E0.md) at `0x00350626`
- [KeRundownQueueCommon](../35/KeRundownQueueCommon_function_003515F4.md) at `0x003516C7`
- [KeDeleteMutant](../35/KeDeleteMutant_function_00351788.md) at `0x00351962`
- [KePulseEvent](../35/KePulseEvent_function_00351EF0.md) at `0x00352005`
- [KePulseEvent](../35/KePulseEvent_function_00351EF0.md) at `0x00352085`
- [KeSetProcess](../35/KeSetProcess_function_003520E8.md) at `0x003521D5`
- [KeTerminateThread](../35/KeTerminateThread_function_00355138.md) at `0x003553FC`
- [KeRegisterObjectNotification](../39/KeRegisterObjectNotification_function_00393454.md) at `0x003934D4`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x00395F35`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x00395F8A`
- [KiWakeOtherQueueWaiters](../39/KiWakeOtherQueueWaiters_function_003964D0.md) at `0x003966BD`
- [KeReleaseMutantEx](../39/KeReleaseMutantEx_function_00396850.md) at `0x00396BCC`
- [sub_00397299](../39/Unknown_function_00397299.md) at `0x003972AC`
- [KiExpireTimer2](../3A/KiExpireTimer2_function_003A24E0.md) at `0x003A2888`
- [KiExpireTimer2](../3A/KiExpireTimer2_function_003A24E0.md) at `0x003A2BE2`
- [sub_006F59B4](../6F/Unknown_function_006F59B4.md) at `0x006F5B3A`

### Static image references
- `0x00219B5F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00219B75` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00219D23` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00219D6A` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00219B30  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00219B35  55                              push rbp
00219B36  56                              push rsi
00219B37  57                              push rdi
00219B38  41 54                           push r12
00219B3A  41 55                           push r13
00219B3C  41 56                           push r14
00219B3E  41 57                           push r15
00219B40  48 83 EC 20                     sub rsp, 0x20
00219B44  48 83 22 00                     and qword ptr [rdx], 0
00219B48  4C 8D 79 08                     lea r15, [rcx + 8]
00219B4C  48 8B F2                        mov rsi, rdx
00219B4F  48 8B F9                        mov rdi, rcx
00219B52  44 0F 20 C1                     mov rcx, cr8
00219B56  B8 02 00 00 00                  mov eax, 2
00219B5B  44 0F 22 C0                     mov cr8, rax
00219B5F  83 3D BA D1 DA 00 00            cmp dword ptr [rip + 0xdad1ba], 0
00219B66  0F 85 E9 01 00 00               jne 0x140219d55
00219B6C  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
00219B75  F7 05 85 CF DA 00 00 00 00 01   test dword ptr [rip + 0xdacf85], 0x1000000
00219B7F  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
00219B84  49 8B 6E 08                     mov rbp, qword ptr [r14 + 8]
00219B88  0F 85 F9 01 00 00               jne 0x140219d87
00219B8E  33 DB                           xor ebx, ebx
00219B90  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
00219B95  0F 82 19 02 00 00               jb 0x140219db4
00219B9B  4D 39 3F                        cmp qword ptr [r15], r15
00219B9E  0F 84 01 01 00 00               je 0x140219ca5
00219BA4  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
00219BA7  3B 47 2C                        cmp eax, dword ptr [rdi + 0x2c]
00219BAA  0F 83 F5 00 00 00               jae 0x140219ca5
00219BB0  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
00219BB7  48 3B C7                        cmp rax, rdi
00219BBA  0F 84 E2 01 00 00               je 0x140219da2
00219BC0  4D 8B 27                        mov r12, qword ptr [r15]
00219BC3  49 8B EC                        mov rbp, r12
00219BC6  4D 8B 24 24                     mov r12, qword ptr [r12]
00219BCA  80 7D 10 03                     cmp byte ptr [rbp + 0x10], 3
00219BCE  0F 85 CC 00 00 00               jne 0x140219ca0
00219BD4  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00219BD8  49 39 6C 24 08                  cmp qword ptr [r12 + 8], rbp
00219BDD  75 09                           jne 0x140219be8
00219BDF  48 39 28                        cmp qword ptr [rax], rbp
00219BE2  0F 84 19 01 00 00               je 0x140219d01
00219BE8  B9 03 00 00 00                  mov ecx, 3
00219BED  CD 29                           int 0x29
00219BEF  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
00219BF5  3C 05                           cmp al, 5
00219BF7  0F 85 81 00 00 00               jne 0x140219c7e
00219BFD  0F B6 43 70                     movzx eax, byte ptr [rbx + 0x70]
00219C01  8B C8                           mov ecx, eax
00219C03  83 E1 07                        and ecx, 7
00219C06  83 F9 01                        cmp ecx, 1
00219C09  0F 85 13 02 00 00               jne 0x140219e22
00219C0F  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
00219C16  48 85 D2                        test rdx, rdx
00219C19  74 10                           je 0x140219c2b
00219C1B  8A 02                           mov al, byte ptr [rdx]
00219C1D  24 7F                           and al, 0x7f
00219C1F  3C 15                           cmp al, 0x15
00219C21  0F 84 12 01 00 00               je 0x140219d39
00219C27  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
00219C2B  48 8B CB                        mov rcx, rbx
00219C2E  E8 9D 66 03 00                  call 0x1402502d0
00219C33  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
00219C39  3C 01                           cmp al, 1
00219C3B  0F 85 8A 01 00 00               jne 0x140219dcb
00219C41  83 4B 74 02                     or dword ptr [rbx + 0x74], 2
00219C45  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00219C4A  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
00219C51  C6 83 84 01 00 00 07            mov byte ptr [rbx + 0x184], 7
00219C58  48 8B 82 08 2D 00 00            mov rax, qword ptr [rdx + 0x2d08]
00219C5F  48 89 01                        mov qword ptr [rcx], rax
00219C62  48 89 8A 08 2D 00 00            mov qword ptr [rdx + 0x2d08], rcx
00219C69  48 89 B3 C8 00 00 00            mov qword ptr [rbx + 0xc8], rsi
00219C70  48 C7 83 D0 03 00 00 00 00 00 00  mov qword ptr [rbx + 0x3d0], 0
00219C7B  41 B5 01                        mov r13b, 1
00219C7E  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
00219C86  8A 45 11                        mov al, byte ptr [rbp + 0x11]
00219C89  FE C0                           inc al
00219C8B  88 45 11                        mov byte ptr [rbp + 0x11], al
00219C8E  45 84 ED                        test r13b, r13b
00219C91  0F 85 CA 00 00 00               jne 0x140219d61
00219C97  4D 3B E7                        cmp r12, r15
00219C9A  0F 85 23 FF FF FF               jne 0x140219bc3
00219CA0  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00219CA5  44 8B 47 04                     mov r8d, dword ptr [rdi + 4]
00219CA9  41 8D 40 01                     lea eax, [r8 + 1]
00219CAD  89 47 04                        mov dword ptr [rdi + 4], eax
00219CB0  48 8D 47 18                     lea rax, [rdi + 0x18]
00219CB4  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00219CB8  48 39 02                        cmp qword ptr [rdx], rax
00219CBB  0F 85 27 FF FF FF               jne 0x140219be8
00219CC1  48 89 06                        mov qword ptr [rsi], rax
00219CC4  48 89 56 08                     mov qword ptr [rsi + 8], rdx
00219CC8  48 89 32                        mov qword ptr [rdx], rsi
00219CCB  48 89 70 08                     mov qword ptr [rax + 8], rsi
00219CCF  45 85 C0                        test r8d, r8d
00219CD2  75 10                           jne 0x140219ce4
00219CD4  4D 39 3F                        cmp qword ptr [r15], r15
00219CD7  74 0B                           je 0x140219ce4
00219CD9  48 8B D7                        mov rdx, rdi
00219CDC  49 8B CE                        mov rcx, r14
00219CDF  E8 EC C7 17 00                  call 0x1403964d0
00219CE4  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
00219CEB  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00219CF0  48 83 C4 20                     add rsp, 0x20
00219CF4  41 5F                           pop r15
00219CF6  41 5E                           pop r14
00219CF8  41 5D                           pop r13
00219CFA  41 5C                           pop r12
00219CFC  5F                              pop rdi
00219CFD  5E                              pop rsi
00219CFE  5D                              pop rbp
00219CFF  C3                              ret
00219D00  CC                              int3
00219D01  4C 89 20                        mov qword ptr [rax], r12
00219D04  45 32 ED                        xor r13b, r13b
00219D07  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
00219D0C  45 33 F6                        xor r14d, r14d
00219D0F  48 8B 5D 18                     mov rbx, qword ptr [rbp + 0x18]
00219D13  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
00219D1A  0F 83 CF FE FF FF               jae 0x140219bef
00219D20  41 FF C6                        inc r14d
00219D23  44 85 35 82 B5 DA 00            test dword ptr [rip + 0xdab582], r14d
00219D2A  74 3E                           je 0x140219d6a
00219D2C  F3 90                           pause
00219D2E  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00219D32  48 85 C0                        test rax, rax
00219D35  74 DC                           je 0x140219d13
00219D37  EB E7                           jmp 0x140219d20
00219D39  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
00219D3F  0F B6 C0                        movzx eax, al
00219D42  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
00219D48  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
00219D50  E9 D6 FE FF FF                  jmp 0x140219c2b
00219D55  8A D0                           mov dl, al
00219D57  E8 A0 B9 2D 00                  call 0x1404f56fc
00219D5C  E9 0B FE FF FF                  jmp 0x140219b6c
00219D61  48 83 26 00                     and qword ptr [rsi], 0
00219D65  E9 7A FF FF FF                  jmp 0x140219ce4
00219D6A  8B 05 48 CD DA 00               mov eax, dword ptr [rip + 0xdacd48]
00219D70  A8 40                           test al, 0x40
00219D72  74 B8                           je 0x140219d2c
00219D74  E8 17 57 0F 00                  call 0x14030f490
00219D79  84 C0                           test al, al
00219D7B  74 AF                           je 0x140219d2c
00219D7D  41 8B CE                        mov ecx, r14d
00219D80  E8 DB 56 0F 00                  call 0x14030f460
00219D85  EB A7                           jmp 0x140219d2e
00219D87  48 8B CD                        mov rcx, rbp
00219D8A  E8 91 C9 17 00                  call 0x140396720
00219D8F  44 8A C0                        mov r8b, al
00219D92  48 8B CD                        mov rcx, rbp
00219D95  48 8B D6                        mov rdx, rsi
00219D98  E8 AF C9 17 00                  call 0x14039674c
00219D9D  E9 EC FD FF FF                  jmp 0x140219b8e
00219DA2  80 BD 83 02 00 00 0F            cmp byte ptr [rbp + 0x283], 0xf
00219DA9  0F 85 11 FE FF FF               jne 0x140219bc0
00219DAF  E9 F1 FE FF FF                  jmp 0x140219ca5
00219DB4  FF C3                           inc ebx
00219DB6  85 1D F0 B4 DA 00               test dword ptr [rip + 0xdab4f0], ebx
00219DBC  74 48                           je 0x140219e06
00219DBE  F3 90                           pause
00219DC0  8B 07                           mov eax, dword ptr [rdi]
00219DC2  84 C0                           test al, al
00219DC4  78 EE                           js 0x140219db4
00219DC6  E9 C5 FD FF FF                  jmp 0x140219b90
00219DCB  3C 05                           cmp al, 5
00219DCD  0F 85 72 FE FF FF               jne 0x140219c45
00219DD3  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00219DDD  8B 08                           mov ecx, dword ptr [rax]
00219DDF  2B 8B B4 01 00 00               sub ecx, dword ptr [rbx + 0x1b4]
00219DE5  44 38 AB 87 01 00 00            cmp byte ptr [rbx + 0x187], r13b
00219DEC  74 0C                           je 0x140219dfa
00219DEE  48 01 8B E8 03 00 00            add qword ptr [rbx + 0x3e8], rcx
00219DF5  E9 4B FE FF FF                  jmp 0x140219c45
00219DFA  48 01 8B E0 03 00 00            add qword ptr [rbx + 0x3e0], rcx
00219E01  E9 3F FE FF FF                  jmp 0x140219c45
00219E06  8B 05 AC CC DA 00               mov eax, dword ptr [rip + 0xdaccac]
00219E0C  A8 40                           test al, 0x40
00219E0E  74 AE                           je 0x140219dbe
00219E10  E8 7B 56 0F 00                  call 0x14030f490
00219E15  84 C0                           test al, al
00219E17  74 A5                           je 0x140219dbe
00219E19  8B CB                           mov ecx, ebx
00219E1B  E8 40 56 0F 00                  call 0x14030f460
00219E20  EB 9E                           jmp 0x140219dc0
00219E22  83 F9 04                        cmp ecx, 4
00219E25  0F 84 E4 FD FF FF               je 0x140219c0f
00219E2B  85 C9                           test ecx, ecx
00219E2D  75 21                           jne 0x140219e50
00219E2F  24 FA                           and al, 0xfa
00219E31  0C 02                           or al, 2
00219E33  88 43 70                        mov byte ptr [rbx + 0x70], al
00219E36  48 89 B3 C8 00 00 00            mov qword ptr [rbx + 0xc8], rsi
00219E3D  48 C7 83 D0 03 00 00 00 00 00 00  mov qword ptr [rbx + 0x3d0], 0
00219E48  88 4D 11                        mov byte ptr [rbp + 0x11], cl
00219E4B  E9 2B FE FF FF                  jmp 0x140219c7b
00219E50  83 F9 05                        cmp ecx, 5
00219E53  75 0C                           jne 0x140219e61
00219E55  24 FE                           and al, 0xfe
00219E57  0C 06                           or al, 6
00219E59  88 43 70                        mov byte ptr [rbx + 0x70], al
00219E5C  E9 1D FE FF FF                  jmp 0x140219c7e
00219E61  83 F9 03                        cmp ecx, 3
00219E64  0F 85 14 FE FF FF               jne 0x140219c7e
00219E6A  C6 45 11 02                     mov byte ptr [rbp + 0x11], 2
00219E6E  E9 0B FE FF FF                  jmp 0x140219c7e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiInsertQueueInternal(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 14340538)) != 0) goto loc_00219D55;
loc_00219B6C:
    v_stack_p10 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if (((*(unsigned int *)(v_rip + 14339973)) & (0x1000000ULL)) != 0) goto loc_00219D87;
loc_00219B8E:
    v_rbx = 0;
loc_00219B90:
    if (condition_is_below) goto loc_00219DB4;
    if ((*(unsigned __int64 *)(a1 + 8)) == (a1 + 8)) goto loc_00219CA5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) >= (*(unsigned int *)(a1 + 44))) goto loc_00219CA5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232)) == a1) goto loc_00219DA2;
loc_00219BC0:
loc_00219BC3:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 16)) != 3) goto loc_00219CA0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 8))) goto loc_00219BE8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8))) == (*(unsigned __int64 *)(a1 + 8))) goto loc_00219D01;
loc_00219BE8:
loc_00219BEF:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 388))) != 5) goto loc_00219C7E;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rbx + 112)))) & (7));
    if (((unsigned int)(a1)) != 1) goto loc_00219E22;
loc_00219C0F:
    if (*(unsigned __int64 *)(v_rbx + 232) == 0) goto loc_00219C2B;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_00219D39;
loc_00219C2B:
    result = KiRemovePrcbWaitEntry(0, *(unsigned __int64 *)(v_rbx + 232), a3, a4);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 388))) != 1) goto loc_00219DCB;
loc_00219C45:
    *(unsigned __int8 *)(v_rbx + 388) = 7;
    *(unsigned __int64 *)(v_rbx + 216) = *(unsigned __int64 *)(v_stack_p10 + 11528);
    *(unsigned __int64 *)(v_stack_p10 + 11528) = v_rbx + 216;
    *(unsigned __int64 *)(v_rbx + 200) = a2;
    *(unsigned __int64 *)(v_rbx + 976) = 0;
loc_00219C7B:
loc_00219C7E:
    *(unsigned __int64 *)(v_rbx + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17) = (unsigned __int8)(result);
    if (1 != 0) goto loc_00219D61;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != (a1 + 8)) goto loc_00219BC3;
loc_00219CA0:
loc_00219CA5:
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8))) != (a1 + 24)) goto loc_00219BE8;
    *(unsigned __int64 *)(a2) = a1 + 24;
    *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(a1 + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8)) = a2;
    *(unsigned __int64 *)(a1 + 24 + 8) = a2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) != 0) goto loc_00219CE4;
    result = a1 + 24;
    if ((*(unsigned __int64 *)(a1 + 8)) != (a1 + 8)) {
        a2 = a1;
        a1 = v_stack_p10;
        result = KiWakeOtherQueueWaiters(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 4)), a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
loc_00219D01:
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8));
    v_r13 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 8) = result;
    v_r14 = 0;
loc_00219D13:
    if (condition_is_above_or_equal) goto loc_00219BEF;
loc_00219D20:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14333314)) & ((unsigned int)(v_r14))) == 0) goto loc_00219D6A;
loc_00219D2C:
loc_00219D2E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 64) == 0) goto loc_00219D13;
    goto loc_00219D20;
loc_00219D39:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 540))));
    goto loc_00219C2B;
loc_00219D55:
    result = KiRaiseIrqlProcessIrqlFlags(a1, (unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 540)))), (unsigned int)(*(unsigned int *)(a1 + 4)), a4);
    goto loc_00219B6C;
loc_00219D61:
    goto loc_00219CE4;
loc_00219D6A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14339400)))) & (64)) == 0) goto loc_00219D2C;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 540)))), (unsigned int)(*(unsigned int *)(a1 + 4)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00219D2C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), (unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 540)))), (unsigned int)(*(unsigned int *)(a1 + 4)), a4);
    goto loc_00219D2E;
loc_00219D87:
    result = KeIsThreadRunning(*(unsigned __int64 *)(a1 + 8), (unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 540)))), (unsigned int)(*(unsigned int *)(a1 + 4)), a4);
    result = EtwTraceEnqueueWork(*(unsigned __int64 *)(a1 + 8), a2, (unsigned __int8)(result), a4);
    goto loc_00219B8E;
loc_00219DA2:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 643)) != 15) goto loc_00219BC0;
    goto loc_00219CA5;
loc_00219DB4:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24)) + 1);
    if (((*(unsigned int *)(v_rip + 14333168)) & ((unsigned int)(v_rbx))) == 0) goto loc_00219E06;
loc_00219DBE:
loc_00219DC0:
    if (sign_flag) goto loc_00219DB4;
    goto loc_00219B90;
loc_00219DCB:
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) != 5) goto loc_00219C45;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1))))) - (*(unsigned int *)(v_rbx + 436)));
    if ((*(unsigned __int8 *)(v_rbx + 391)) == 0) goto loc_00219DFA;
    goto loc_00219C45;
loc_00219DFA:
    goto loc_00219C45;
loc_00219E06:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14339244)))) & (64)) == 0) goto loc_00219DBE;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, (unsigned __int8)(result), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00219DBE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned __int8)(result), a4);
    goto loc_00219DC0;
loc_00219E22:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) == 4) goto loc_00219C0F;
    if ((unsigned int)((unsigned int)((unsigned int)(v_rbx))) != 0) goto loc_00219E50;
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    *(unsigned __int8 *)(v_rbx + 112) = (unsigned __int8)(result);
    *(unsigned __int64 *)(v_rbx + 200) = a2;
    *(unsigned __int64 *)(v_rbx + 976) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17) = (unsigned __int8)((unsigned int)((unsigned int)(v_rbx)));
    goto loc_00219C7B;
loc_00219E50:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) != 5) goto loc_00219E61;
    result = (unsigned __int8)((result) & (254));
    result = (unsigned __int8)((result) | (6));
    *(unsigned __int8 *)(v_rbx + 112) = (unsigned __int8)(result);
    goto loc_00219C7E;
loc_00219E61:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) != 3) goto loc_00219C7E;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17) = 2;
    goto loc_00219C7E;
}
```

## 5. (Beta) C Style

```c
int64_t KiInsertQueueInternal(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xDAD1BA)) != 0) goto loc_00219D55;
loc_00219B6C:
    v_stack_p10 = *(uint64_t *)(gs_base + (0 + 0x20));
    if (((*(uint32_t *)(v_rip + 0xDACF85)) & (0x1000000ULL)) != 0) goto loc_00219D87;
loc_00219B8E:
    local_rbx = 0;
loc_00219B90:
    if (condition_is_below) goto loc_00219DB4;
    if ((*(uint64_t *)(arg1 + 0x8)) == (Arg1 + 8)) goto loc_00219CA5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) >= (*(uint32_t *)(arg1 + 0x2C))) goto loc_00219CA5;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8)) == Arg1) goto loc_00219DA2;
loc_00219BC0:
loc_00219BC3:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)) != 3) goto loc_00219CA0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x8))) goto loc_00219BE8;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8))) == (*(uint64_t *)(arg1 + 0x8))) goto loc_00219D01;
loc_00219BE8:
loc_00219BEF:
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x184))) != 5) goto loc_00219C7E;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_rbx + 0x70)))) & (7));
    if (((uint32_t)(Arg1)) != 1) goto loc_00219E22;
loc_00219C0F:
    if (*(uint64_t *)(local_rbx + 0xE8) == 0) goto loc_00219C2B;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_rbx + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_00219D39;
loc_00219C2B:
    result = KiRemovePrcbWaitEntry(0, *(uint64_t *)(local_rbx + 0xE8), a3, a4);
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x184))) != 1) goto loc_00219DCB;
loc_00219C45:
    *(uint8_t *)(local_rbx + 0x184) = 7;
    *(uint64_t *)(local_rbx + 0xD8) = *(uint64_t *)(v_stack_p10 + 0x2D08);
    *(uint64_t *)(v_stack_p10 + 0x2D08) = local_rbx + 216;
    *(void **)(local_rbx + 0xC8) = Arg2;
    *(uint64_t *)(local_rbx + 0x3D0) = 0;
loc_00219C7B:
loc_00219C7E:
    *(uint64_t *)(local_rbx + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11)) + 1);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11) = (uint8_t)(result);
    if (1 != 0) goto loc_00219D61;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != (Arg1 + 8)) goto loc_00219BC3;
loc_00219CA0:
loc_00219CA5:
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8))) != (Arg1 + 24)) goto loc_00219BE8;
    *(void **)(arg2) = Arg1 + 24;
    *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(arg1 + 0x18 + 0x8);
    *(void **)(*(uint64_t *)(arg1 + 0x18 + 0x8)) = Arg2;
    *(void **)(arg1 + 0x18 + 0x8) = Arg2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) != 0) goto loc_00219CE4;
    result = Arg1 + 24;
    if ((*(uint64_t *)(arg1 + 0x8)) != (Arg1 + 8)) {
        Arg2 = Arg1;
        Arg1 = v_stack_p10;
        result = KiWakeOtherQueueWaiters(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x4)), a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
loc_00219D01:
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8));
    local_r13 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x8) = result;
    local_r14 = 0;
loc_00219D13:
    if (condition_is_above_or_equal) goto loc_00219BEF;
loc_00219D20:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xDAB582)) & ((uint32_t)(local_r14))) == 0) goto loc_00219D6A;
loc_00219D2C:
loc_00219D2E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x40) == 0) goto loc_00219D13;
    goto loc_00219D20;
loc_00219D39:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x21C))));
    goto loc_00219C2B;
loc_00219D55:
    result = KiRaiseIrqlProcessIrqlFlags(Arg1, (uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x21C)))), (uint32_t)(*(uint32_t *)(arg1 + 0x4)), a4);
    goto loc_00219B6C;
loc_00219D61:
    goto loc_00219CE4;
loc_00219D6A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDACD48)))) & (64)) == 0) goto loc_00219D2C;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x21C)))), (uint32_t)(*(uint32_t *)(arg1 + 0x4)), a4);
    if ((uint8_t)(result) == 0) goto loc_00219D2C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), (uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x21C)))), (uint32_t)(*(uint32_t *)(arg1 + 0x4)), a4);
    goto loc_00219D2E;
loc_00219D87:
    result = KeIsThreadRunning(*(uint64_t *)(arg1 + 0x8), (uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x21C)))), (uint32_t)(*(uint32_t *)(arg1 + 0x4)), a4);
    result = EtwTraceEnqueueWork(*(uint64_t *)(arg1 + 0x8), Arg2, (uint8_t)(result), a4);
    goto loc_00219B8E;
loc_00219DA2:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x283)) != 15) goto loc_00219BC0;
    goto loc_00219CA5;
loc_00219DB4:
    local_rbx = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18)) + 1);
    if (((*(uint32_t *)(v_rip + 0xDAB4F0)) & ((uint32_t)(local_rbx))) == 0) goto loc_00219E06;
loc_00219DBE:
loc_00219DC0:
    if (sign_flag) goto loc_00219DB4;
    goto loc_00219B90;
loc_00219DCB:
    if (((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) != 5) goto loc_00219C45;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1))))) - (*(uint32_t *)(local_rbx + 0x1B4)));
    if ((*(uint8_t *)(local_rbx + 0x187)) == 0) goto loc_00219DFA;
    goto loc_00219C45;
loc_00219DFA:
    goto loc_00219C45;
loc_00219E06:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDACCAC)))) & (64)) == 0) goto loc_00219DBE;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, (uint8_t)(result), a4);
    if ((uint8_t)(result) == 0) goto loc_00219DBE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint8_t)(result), a4);
    goto loc_00219DC0;
loc_00219E22:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) == 4) goto loc_00219C0F;
    if ((uint32_t)((uint32_t)((uint32_t)(local_rbx))) != 0) goto loc_00219E50;
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    *(uint8_t *)(local_rbx + 0x70) = (uint8_t)(result);
    *(void **)(local_rbx + 0xC8) = Arg2;
    *(uint64_t *)(local_rbx + 0x3D0) = 0;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11) = (uint8_t)((uint32_t)((uint32_t)(local_rbx)));
    goto loc_00219C7B;
loc_00219E50:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) != 5) goto loc_00219E61;
    result = (uint8_t)((result) & (254));
    result = (uint8_t)((result) | (6));
    *(uint8_t *)(local_rbx + 0x70) = (uint8_t)(result);
    goto loc_00219C7E;
loc_00219E61:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) != 3) goto loc_00219C7E;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11) = 2;
    goto loc_00219C7E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00219B30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
