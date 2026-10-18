# KeReleaseSemaphoreEx

- RVA: `0x003468C0`–`0x00346C52` (길이 `914` bytes)
- VA: `0x00000001403468C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077FE0`
- 디코드: `230`개 명령, `914/914` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0034690D` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x003469B0` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x003469B8` → [KiEnterDeferredReadyState](../39/KiEnterDeferredReadyState_function_00397420.md) (function, `0x00397420`)
- `0x00346A53` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00346AE9` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00346B08` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00346B3F` → [KiCompleteDirectSwitchThread](../3F/KiCompleteDirectSwitchThread_function_003FFE1C.md) (function, `0x003FFE1C`)
- `0x00346B63` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00346B72` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00346B92` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00346BAE` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00346BC7` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00346C37` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)

### Direct callers
- [AlpcpSignalAndWait](../2F/AlpcpSignalAndWait_function_002F9620.md) at `0x002F99A8`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x00395CE2`
- [sub_006E631C](../6E/Unknown_function_006E631C.md) at `0x006E6334`
- [sub_0088DAFD](../../page/88/Unknown_function_0088DAFD.md) at `0x0088DB91`
- [sub_0088EC77](../../page/88/Unknown_function_0088EC77.md) at `0x0088EF89`
- [sub_0088EC77](../../page/88/Unknown_function_0088EC77.md) at `0x0088F07B`
- [AlpcpCancelMessage](../../page/89/AlpcpCancelMessage_function_00894120.md) at `0x008944AD`
- [NtReleaseSemaphore](../../page/9C/NtReleaseSemaphore_function_009C4BC0.md) at `0x009C4C54`
- [AlpcpReplyLegacySynchronousRequest](../../page/9F/AlpcpReplyLegacySynchronousRequest_function_009F5CF0.md) at `0x009F6199`
- [sub_00B22892](../../page/B2/Unknown_function_00B22892.md) at `0x00B22AD3`
- [sub_00B22B6A](../../page/B2/Unknown_function_00B22B6A.md) at `0x00B22BB7`
- [sub_00B414D2](../../page/B4/Unknown_function_00B414D2.md) at `0x00B41514`

### Static image references
- `0x003468F5` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00346AB2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00346B55` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003468C0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
003468C5  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003468CA  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
003468CE  55                              push rbp
003468CF  56                              push rsi
003468D0  57                              push rdi
003468D1  41 54                           push r12
003468D3  41 55                           push r13
003468D5  41 56                           push r14
003468D7  41 57                           push r15
003468D9  48 83 EC 30                     sub rsp, 0x30
003468DD  41 8B F8                        mov edi, r8d
003468E0  8B F2                           mov esi, edx
003468E2  48 8B D9                        mov rbx, rcx
003468E5  45 0F 20 C6                     mov r14, cr8
003468E9  41 BC 02 00 00 00               mov r12d, 2
003468EF  45 0F 22 C4                     mov cr8, r12
003468F3  33 ED                           xor ebp, ebp
003468F5  39 2D 25 04 C8 00               cmp dword ptr [rip + 0xc80425], ebp
003468FB  0F 85 E2 01 00 00               jne 0x140346ae3
00346901  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
0034690A  48 8B CB                        mov rcx, rbx
0034690D  E8 7E B3 F0 FF                  call 0x140251c90
00346912  44 8B 7B 04                     mov r15d, dword ptr [rbx + 4]
00346916  41 8D 04 3F                     lea eax, [r15 + rdi]
0034691A  41 3B C7                        cmp eax, r15d
0034691D  0F 8C 59 02 00 00               jl 0x140346b7c
00346923  3B 43 18                        cmp eax, dword ptr [rbx + 0x18]
00346926  0F 8F 50 02 00 00               jg 0x140346b7c
0034692C  89 43 04                        mov dword ptr [rbx + 4], eax
0034692F  45 85 FF                        test r15d, r15d
00346932  0F 85 E8 00 00 00               jne 0x140346a20
00346938  48 8D 43 08                     lea rax, [rbx + 8]
0034693C  4C 8B 00                        mov r8, qword ptr [rax]
0034693F  4C 3B C0                        cmp r8, rax
00346942  0F 84 D4 00 00 00               je 0x140346a1c
00346948  49 8B 00                        mov rax, qword ptr [r8]
0034694B  49 8B F8                        mov rdi, r8
0034694E  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
00346952  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0034695A  4C 39 40 08                     cmp qword ptr [rax + 8], r8
0034695E  75 09                           jne 0x140346969
00346960  4C 39 01                        cmp qword ptr [rcx], r8
00346963  0F 84 1A 01 00 00               je 0x140346a83
00346969  B9 03 00 00 00                  mov ecx, 3
0034696E  CD 29                           int 0x29
00346970  8A 86 84 01 00 00               mov al, byte ptr [rsi + 0x184]
00346976  33 ED                           xor ebp, ebp
00346978  3C 05                           cmp al, 5
0034697A  75 6F                           jne 0x1403469eb
0034697C  0F B6 46 70                     movzx eax, byte ptr [rsi + 0x70]
00346980  44 8A E5                        mov r12b, bpl
00346983  8B C8                           mov ecx, eax
00346985  83 E1 07                        and ecx, 7
00346988  83 F9 01                        cmp ecx, 1
0034698B  0F 85 56 02 00 00               jne 0x140346be7
00346991  48 8B 96 E8 00 00 00            mov rdx, qword ptr [rsi + 0xe8]
00346998  48 85 D2                        test rdx, rdx
0034699B  74 10                           je 0x1403469ad
0034699D  8A 02                           mov al, byte ptr [rdx]
0034699F  24 7F                           and al, 0x7f
003469A1  3C 15                           cmp al, 0x15
003469A3  0F 84 73 01 00 00               je 0x140346b1c
003469A9  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
003469AD  48 8B CE                        mov rcx, rsi
003469B0  E8 1B 99 F0 FF                  call 0x1402502d0
003469B5  48 8B CE                        mov rcx, rsi
003469B8  E8 63 0A 05 00                  call 0x140397420
003469BD  49 8B 85 08 2D 00 00            mov rax, qword ptr [r13 + 0x2d08]
003469C4  48 8D 8E D8 00 00 00            lea rcx, [rsi + 0xd8]
003469CB  48 89 01                        mov qword ptr [rcx], rax
003469CE  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
003469D3  49 89 8D 08 2D 00 00            mov qword ptr [r13 + 0x2d08], rcx
003469DA  48 89 86 C8 00 00 00            mov qword ptr [rsi + 0xc8], rax
003469E1  48 89 AE D0 03 00 00            mov qword ptr [rsi + 0x3d0], rbp
003469E8  41 B4 01                        mov r12b, 1
003469EB  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
003469F3  48 89 6E 40                     mov qword ptr [rsi + 0x40], rbp
003469F7  8A 47 11                        mov al, byte ptr [rdi + 0x11]
003469FA  FE C0                           inc al
003469FC  88 47 11                        mov byte ptr [rdi + 0x11], al
003469FF  45 84 E4                        test r12b, r12b
00346A02  48 8D 43 08                     lea rax, [rbx + 8]
00346A06  41 BC 02 00 00 00               mov r12d, 2
00346A0C  0F 84 2D FF FF FF               je 0x14034693f
00346A12  83 6B 04 01                     sub dword ptr [rbx + 4], 1
00346A16  0F 85 34 02 00 00               jne 0x140346c50
00346A1C  8B 74 24 78                     mov esi, dword ptr [rsp + 0x78]
00346A20  F0 81 23 7F FF FF FF            lock and dword ptr [rbx], 0xffffff7f
00346A27  8B 9C 24 90 00 00 00            mov ebx, dword ptr [rsp + 0x90]
00346A2E  F6 C3 01                        test bl, 1
00346A31  0F 85 94 00 00 00               jne 0x140346acb
00346A37  8B D5                           mov edx, ebp
00346A39  41 84 DC                        test r12b, bl
00346A3C  0F 85 F6 00 00 00               jne 0x140346b38
00346A42  44 8B CE                        mov r9d, esi
00346A45  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00346A4A  41 B8 01 00 00 00               mov r8d, 1
00346A50  49 8B CD                        mov rcx, r13
00346A53  E8 98 B2 F0 FF                  call 0x140251cf0
00346A58  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00346A60  48 85 C0                        test rax, rax
00346A63  74 03                           je 0x140346a68
00346A65  44 89 38                        mov dword ptr [rax], r15d
00346A68  33 C0                           xor eax, eax
00346A6A  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00346A72  48 83 C4 30                     add rsp, 0x30
00346A76  41 5F                           pop r15
00346A78  41 5E                           pop r14
00346A7A  41 5D                           pop r13
00346A7C  41 5C                           pop r12
00346A7E  5F                              pop rdi
00346A7F  5E                              pop rsi
00346A80  5D                              pop rbp
00346A81  C3                              ret
00346A82  CC                              int3
00346A83  48 89 01                        mov qword ptr [rcx], rax
00346A86  48 89 48 08                     mov qword ptr [rax + 8], rcx
00346A8A  41 8A 40 10                     mov al, byte ptr [r8 + 0x10]
00346A8E  3C 01                           cmp al, 1
00346A90  75 61                           jne 0x140346af3
00346A92  41 0F B7 50 12                  movzx edx, word ptr [r8 + 0x12]
00346A97  44 8A E5                        mov r12b, bpl
00346A9A  49 8B 70 18                     mov rsi, qword ptr [r8 + 0x18]
00346A9E  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00346AA3  F0 48 0F BA 6E 40 00            lock bts qword ptr [rsi + 0x40], 0
00346AAA  0F 83 C0 FE FF FF               jae 0x140346970
00346AB0  FF C5                           inc ebp
00346AB2  85 2D F4 E7 C7 00               test dword ptr [rip + 0xc7e7f4], ebp
00346AB8  0F 84 97 00 00 00               je 0x140346b55
00346ABE  F3 90                           pause
00346AC0  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
00346AC4  48 85 C0                        test rax, rax
00346AC7  74 DA                           je 0x140346aa3
00346AC9  EB E5                           jmp 0x140346ab0
00346ACB  BA 01 00 00 00                  mov edx, 1
00346AD0  F6 C3 04                        test bl, 4
00346AD3  0F 85 69 FF FF FF               jne 0x140346a42
00346AD9  BA 03 00 00 00                  mov edx, 3
00346ADE  E9 5F FF FF FF                  jmp 0x140346a42
00346AE3  41 8A D4                        mov dl, r12b
00346AE6  41 8A CE                        mov cl, r14b
00346AE9  E8 0E EC 1A 00                  call 0x1404f56fc
00346AEE  E9 0E FE FF FF                  jmp 0x140346901
00346AF3  41 3A C4                        cmp al, r12b
00346AF6  0F 85 B8 00 00 00               jne 0x140346bb4
00346AFC  41 C6 40 11 05                  mov byte ptr [r8 + 0x11], 5
00346B01  48 8B D7                        mov rdx, rdi
00346B04  49 8B 48 18                     mov rcx, qword ptr [r8 + 0x18]
00346B08  E8 23 30 ED FF                  call 0x140219b30
00346B0D  83 6B 04 01                     sub dword ptr [rbx + 4], 1
00346B11  0F 84 05 FF FF FF               je 0x140346a1c
00346B17  E9 B0 00 00 00                  jmp 0x140346bcc
00346B1C  8B 86 1C 02 00 00               mov eax, dword ptr [rsi + 0x21c]
00346B22  0F B6 C0                        movzx eax, al
00346B25  89 86 1C 02 00 00               mov dword ptr [rsi + 0x21c], eax
00346B2B  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
00346B33  E9 75 FE FF FF                  jmp 0x1403469ad
00346B38  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
00346B3C  49 8B CD                        mov rcx, r13
00346B3F  E8 D8 92 0B 00                  call 0x1403ffe1c
00346B44  8B D3                           mov edx, ebx
00346B46  D1 EA                           shr edx, 1
00346B48  F7 D2                           not edx
00346B4A  41 23 D4                        and edx, r12d
00346B4D  83 CA 04                        or edx, 4
00346B50  E9 ED FE FF FF                  jmp 0x140346a42
00346B55  8B 05 5D FF C7 00               mov eax, dword ptr [rip + 0xc7ff5d]
00346B5B  A8 40                           test al, 0x40
00346B5D  0F 84 5B FF FF FF               je 0x140346abe
00346B63  E8 28 89 FC FF                  call 0x14030f490
00346B68  84 C0                           test al, al
00346B6A  0F 84 4E FF FF FF               je 0x140346abe
00346B70  8B CD                           mov ecx, ebp
00346B72  E8 E9 88 FC FF                  call 0x14030f460
00346B77  E9 44 FF FF FF                  jmp 0x140346ac0
00346B7C  F0 81 23 7F FF FF FF            lock and dword ptr [rbx], 0xffffff7f
00346B83  39 2D 97 01 C8 00               cmp dword ptr [rip + 0xc80197], ebp
00346B89  74 0C                           je 0x140346b97
00346B8B  44 0F 20 C1                     mov rcx, cr8
00346B8F  41 8A D6                        mov dl, r14b
00346B92  E8 01 EB 1A 00                  call 0x1404f5698
00346B97  41 0F B6 C6                     movzx eax, r14b
00346B9B  44 0F 22 C0                     mov cr8, rax
00346B9F  F6 84 24 90 00 00 00 08         test byte ptr [rsp + 0x90], 8
00346BA7  74 34                           je 0x140346bdd
00346BA9  B9 47 00 00 C0                  mov ecx, 0xc0000047
00346BAE  E8 9D FE FA FF                  call 0x1402f6a50
00346BB3  CC                              int3
00346BB4  3C 04                           cmp al, 4
00346BB6  74 70                           je 0x140346c28
00346BB8  45 33 C9                        xor r9d, r9d
00346BBB  41 B8 00 01 00 00               mov r8d, 0x100
00346BC1  48 8B D7                        mov rdx, rdi
00346BC4  49 8B CD                        mov rcx, r13
00346BC7  E8 04 9B 00 00                  call 0x1403506d0
00346BCC  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
00346BD4  48 8D 43 08                     lea rax, [rbx + 8]
00346BD8  E9 62 FD FF FF                  jmp 0x14034693f
00346BDD  B8 47 00 00 C0                  mov eax, 0xc0000047
00346BE2  E9 83 FE FF FF                  jmp 0x140346a6a
00346BE7  83 F9 04                        cmp ecx, 4
00346BEA  0F 84 A1 FD FF FF               je 0x140346991
00346BF0  85 C9                           test ecx, ecx
00346BF2  75 23                           jne 0x140346c17
00346BF4  24 FA                           and al, 0xfa
00346BF6  0C 02                           or al, 2
00346BF8  88 46 70                        mov byte ptr [rsi + 0x70], al
00346BFB  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00346C00  48 89 86 C8 00 00 00            mov qword ptr [rsi + 0xc8], rax
00346C07  48 89 AE D0 03 00 00            mov qword ptr [rsi + 0x3d0], rbp
00346C0E  40 88 6F 11                     mov byte ptr [rdi + 0x11], bpl
00346C12  E9 D1 FD FF FF                  jmp 0x1403469e8
00346C17  83 F9 05                        cmp ecx, 5
00346C1A  75 22                           jne 0x140346c3e
00346C1C  24 FE                           and al, 0xfe
00346C1E  0C 06                           or al, 6
00346C20  88 46 70                        mov byte ptr [rsi + 0x70], al
00346C23  E9 C3 FD FF FF                  jmp 0x1403469eb
00346C28  41 C6 40 11 05                  mov byte ptr [r8 + 0x11], 5
00346C2D  48 8B D3                        mov rdx, rbx
00346C30  89 6B 04                        mov dword ptr [rbx + 4], ebp
00346C33  49 8B 48 18                     mov rcx, qword ptr [r8 + 0x18]
00346C37  E8 14 10 EC FF                  call 0x140207c50
00346C3C  EB 8E                           jmp 0x140346bcc
00346C3E  83 F9 03                        cmp ecx, 3
00346C41  0F 85 A4 FD FF FF               jne 0x1403469eb
00346C47  C6 47 11 02                     mov byte ptr [rdi + 0x11], 2
00346C4B  E9 9B FD FF FF                  jmp 0x1403469eb
00346C50  EB 82                           jmp 0x140346bd4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeReleaseSemaphoreEx(__int64 a1, int a2, int a3, __int64 a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int8 v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p88;

    v_stack_p18 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (48);
    v_rbp = 0;
    if ((*(unsigned int *)(v_rip + 13108261)) != 0) goto loc_00346AE3;
loc_00346901:
    result = KiAcquireKobjectLockSafe(a1, a2, a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) + (unsigned int)(a3) * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) goto loc_00346B7C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) + (unsigned int)(a3) * 1)) > (*(unsigned int *)(a1 + 24))) goto loc_00346B7C;
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) + (unsigned int)(a3) * 1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) != 0) goto loc_00346A20;
loc_0034693F:
    if ((*(unsigned __int64 *)(a1 + 8)) == (a1 + 8)) goto loc_00346A1C;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 8))) goto loc_00346969;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8))) == (*(unsigned __int64 *)(a1 + 8))) goto loc_00346A83;
loc_00346969:
loc_00346970:
    v_rbp = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(a2) + 388))) != 5) goto loc_003469EB;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(a2) + 112)))) & (7));
    if (((unsigned int)(a1)) != 1) goto loc_00346BE7;
loc_00346991:
    if (*(unsigned __int64 *)((unsigned int)(a2) + 232) == 0) goto loc_003469AD;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(a2) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_00346B1C;
loc_003469AD:
    result = KiRemovePrcbWaitEntry((unsigned int)(a2), *(unsigned __int64 *)((unsigned int)(a2) + 232), *(unsigned __int64 *)(a1 + 8), a4);
    result = KiEnterDeferredReadyState((unsigned int)(a2), *(unsigned __int64 *)((unsigned int)(a2) + 232), *(unsigned __int64 *)(a1 + 8), a4);
    *(unsigned __int64 *)((unsigned int)(a2) + 216) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11528);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 11528) = (unsigned int)(a2) + 216;
    *(unsigned __int64 *)((unsigned int)(a2) + 200) = v_stack_p8;
    *(unsigned __int64 *)((unsigned int)(a2) + 976) = 0;
loc_003469E8:
loc_003469EB:
    *(unsigned __int64 *)((unsigned int)(a2) + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17) = (unsigned __int8)(result);
    if (1 == 0) goto loc_0034693F;
    if (1 != 0) goto loc_00346C50;
loc_00346A1C:
loc_00346A20:
    if ((((unsigned __int8)((unsigned int)(a5))) & (1)) != 0) goto loc_00346ACB;
    if (((2) & ((unsigned __int8)((unsigned int)(a5)))) != 0) goto loc_00346B38;
loc_00346A42:
    v_stack_m48 = (unsigned __int8)(v_cr8);
    result = KiExitDispatcher(*(unsigned __int64 *)(gs_base + (0 + 32)), 0, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))));
    if (a6 != 0) {
        *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    }
    result = 0;
loc_00346A6A:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00346A83:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32))) = 0;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(gs_base + (0 + 32));
    if (((unsigned __int8)(*(unsigned __int8 *)(1 + 16))) != 1) goto loc_00346AF3;
    v_stack_p70 = *(unsigned __int16 *)(1 + 18);
loc_00346AA3:
    if (((unsigned __int8)(*(unsigned __int8 *)(1 + 16))) >= 1) goto loc_00346970;
loc_00346AB0:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 13101044)) & ((unsigned int)(v_rbp))) == 0) goto loc_00346B55;
loc_00346ABE:
loc_00346AC0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 24) + 64) == 0) goto loc_00346AA3;
    goto loc_00346AB0;
loc_00346ACB:
    if ((((unsigned __int8)(v_stack_p18)) & (4)) != 0) goto loc_00346A42;
    goto loc_00346A42;
loc_00346AE3:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 0, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))));
    goto loc_00346901;
loc_00346AF3:
    if (((unsigned __int8)(result)) != 0) goto loc_00346BB4;
    *(unsigned __int8 *)(1 + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(1 + 24), *(unsigned __int64 *)(a1 + 8), 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))));
    if (((unsigned __int8)(result)) == 0) goto loc_00346A1C;
    goto loc_00346BCC;
loc_00346B1C:
    *(unsigned int *)(*(unsigned __int64 *)(1 + 24) + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24) + 540))));
    goto loc_003469AD;
loc_00346B38:
    result = KiCompleteDirectSwitchThread(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) >> (1));
    a2 = (unsigned int)(~(a2));
    a2 = (unsigned int)((a2) & (0));
    a2 = (unsigned int)((a2) | (4));
    goto loc_00346A42;
loc_00346B55:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13107037)))) & (64)) == 0) goto loc_00346ABE;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))));
    if ((unsigned __int8)(result) == 0) goto loc_00346ABE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), a2, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))));
    goto loc_00346AC0;
loc_00346B7C:
    if ((*(unsigned int *)(v_rip + 13107607)) != ((unsigned int)(v_rbp))) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))));
    }
    if (((a5) & (8)) == 0) goto loc_00346BDD;
    result = RtlRaiseStatus((unsigned int)(0xC0000047ULL), a2, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))));
loc_00346BB4:
    if (((unsigned __int8)(result)) == 4) goto loc_00346C28;
    a4 = 0;
    result = KiTryUnwaitThread(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(a1 + 8), 256, a4);
loc_00346BCC:
loc_00346BD4:
    goto loc_0034693F;
loc_00346BDD:
    goto loc_00346A6A;
loc_00346BE7:
    if (((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32)))) == 4) goto loc_00346991;
    if ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))) != 0) goto loc_00346C17;
    result = (unsigned __int8)(((unsigned int)(0xC0000047ULL)) & (250));
    result = (unsigned __int8)((result) | (2));
    *(unsigned __int8 *)(*(unsigned __int64 *)(1 + 24) + 112) = (unsigned __int8)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 24) + 200) = v_stack_p70;
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 24) + 976) = v_rbp;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17) = (unsigned __int8)(v_rbp);
    goto loc_003469E8;
loc_00346C17:
    if (((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32)))) != 5) goto loc_00346C3E;
    result = (unsigned __int8)((v_stack_p70) & (254));
    result = (unsigned __int8)((result) | (6));
    *(unsigned __int8 *)(*(unsigned __int64 *)(1 + 24) + 112) = (unsigned __int8)(result);
    goto loc_003469EB;
loc_00346C28:
    *(unsigned __int8 *)(v_stack_p88 + 17) = 5;
    *(unsigned int *)(v_stack_p18 + 4) = (unsigned int)(v_rbp);
    result = KeInsertQueueDpc(*(unsigned __int64 *)(v_stack_p88 + 24), v_stack_p18, v_stack_p88, a4);
    goto loc_00346BCC;
loc_00346C3E:
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_p88 + 24))) != 3) goto loc_003469EB;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17) = 2;
    goto loc_003469EB;
loc_00346C50:
    goto loc_00346BD4;
}
```

## 5. (Beta) C Style

```c
int64_t KeReleaseSemaphoreEx(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint8_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rsp;
    uint8_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint64_t v_stack_p88;

    v_stack_p18 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (48);
    local_rbp = 0;
    if ((*(uint32_t *)(v_rip + 0xC80425)) != 0) goto loc_00346AE3;
loc_00346901:
    result = KiAcquireKobjectLockSafe(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) + (uint32_t)(Arg3) * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) goto loc_00346B7C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) + (uint32_t)(Arg3) * 1)) > (*(uint32_t *)(arg1 + 0x18))) goto loc_00346B7C;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) + (uint32_t)(Arg3) * 1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) != 0) goto loc_00346A20;
loc_0034693F:
    if ((*(uint64_t *)(arg1 + 0x8)) == (Arg1 + 8)) goto loc_00346A1C;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x8))) goto loc_00346969;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8))) == (*(uint64_t *)(arg1 + 0x8))) goto loc_00346A83;
loc_00346969:
loc_00346970:
    local_rbp = 0;
    if (((uint8_t)(*(uint8_t *)((uint32_t)(Arg2) + 0x184))) != 5) goto loc_003469EB;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(Arg2) + 0x70)))) & (7));
    if (((uint32_t)(Arg1)) != 1) goto loc_00346BE7;
loc_00346991:
    if (*(uint64_t *)((uint32_t)(Arg2) + 0xE8) == 0) goto loc_003469AD;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)((uint32_t)(Arg2) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_00346B1C;
loc_003469AD:
    result = KiRemovePrcbWaitEntry((uint32_t)(Arg2), *(uint64_t *)((uint32_t)(Arg2) + 0xE8), *(uint64_t *)(arg1 + 0x8), Arg4);
    result = KiEnterDeferredReadyState((uint32_t)(Arg2), *(uint64_t *)((uint32_t)(Arg2) + 0xE8), *(uint64_t *)(arg1 + 0x8), Arg4);
    *(uint64_t *)((uint32_t)(Arg2) + 0xD8) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2D08);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2D08) = (uint32_t)(Arg2) + 216;
    *(uint64_t *)((uint32_t)(Arg2) + 0xC8) = v_stack_p8;
    *(uint64_t *)((uint32_t)(Arg2) + 0x3D0) = 0;
loc_003469E8:
loc_003469EB:
    *(uint64_t *)((uint32_t)(Arg2) + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11)) + 1);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11) = (uint8_t)(result);
    if (1 == 0) goto loc_0034693F;
    if (1 != 0) goto loc_00346C50;
loc_00346A1C:
loc_00346A20:
    if ((((uint8_t)((uint32_t)(Arg5))) & (1)) != 0) goto loc_00346ACB;
    if (((2) & ((uint8_t)((uint32_t)(Arg5)))) != 0) goto loc_00346B38;
loc_00346A42:
    v_stack_m48 = (uint8_t)(v_cr8);
    result = KiExitDispatcher(*(uint64_t *)(gs_base + (0 + 0x20)), 0, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))));
    if (Arg6 != 0) {
        *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    }
    result = 0;
loc_00346A6A:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00346A83:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20))) = 0;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(gs_base + (0 + 0x20));
    if (((uint8_t)(*(uint8_t *)(1 + 0x10))) != 1) goto loc_00346AF3;
    v_stack_p70 = *(uint16_t *)(1 + 0x12);
loc_00346AA3:
    if (((uint8_t)(*(uint8_t *)(1 + 0x10))) >= 1) goto loc_00346970;
loc_00346AB0:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xC7E7F4)) & ((uint32_t)(local_rbp))) == 0) goto loc_00346B55;
loc_00346ABE:
loc_00346AC0:
    if (*(uint64_t *)(*(uint64_t *)(1 + 0x18) + 0x40) == 0) goto loc_00346AA3;
    goto loc_00346AB0;
loc_00346ACB:
    if ((((uint8_t)(v_stack_p18)) & (4)) != 0) goto loc_00346A42;
    goto loc_00346A42;
loc_00346AE3:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 0, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))));
    goto loc_00346901;
loc_00346AF3:
    if (((uint8_t)(result)) != 0) goto loc_00346BB4;
    *(uint8_t *)(1 + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(1 + 0x18), *(uint64_t *)(arg1 + 0x8), 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))));
    if (((uint8_t)(result)) == 0) goto loc_00346A1C;
    goto loc_00346BCC;
loc_00346B1C:
    *(uint32_t *)(*(uint64_t *)(1 + 0x18) + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18) + 0x21C))));
    goto loc_003469AD;
loc_00346B38:
    result = KiCompleteDirectSwitchThread(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) >> (1));
    Arg2 = (uint32_t)(~(Arg2));
    Arg2 = (uint32_t)((Arg2) & (0));
    Arg2 = (uint32_t)((Arg2) | (4));
    goto loc_00346A42;
loc_00346B55:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7FF5D)))) & (64)) == 0) goto loc_00346ABE;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))));
    if ((uint8_t)(result) == 0) goto loc_00346ABE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))));
    goto loc_00346AC0;
loc_00346B7C:
    if ((*(uint32_t *)(v_rip + 0xC80197)) != ((uint32_t)(local_rbp))) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))));
    }
    if (((Arg5) & (8)) == 0) goto loc_00346BDD;
    result = RtlRaiseStatus((uint32_t)(0xC0000047ULL), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))));
loc_00346BB4:
    if (((uint8_t)(result)) == 4) goto loc_00346C28;
    Arg4 = 0;
    result = KiTryUnwaitThread(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(arg1 + 0x8), 256, Arg4);
loc_00346BCC:
loc_00346BD4:
    goto loc_0034693F;
loc_00346BDD:
    goto loc_00346A6A;
loc_00346BE7:
    if (((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20)))) == 4) goto loc_00346991;
    if ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))) != 0) goto loc_00346C17;
    result = (uint8_t)(((uint32_t)(0xC0000047ULL)) & (250));
    result = (uint8_t)((result) | (2));
    *(uint8_t *)(*(uint64_t *)(1 + 0x18) + 0x70) = (uint8_t)(result);
    *(uint64_t *)(*(uint64_t *)(1 + 0x18) + 0xC8) = v_stack_p70;
    *(uint64_t *)(*(uint64_t *)(1 + 0x18) + 0x3D0) = local_rbp;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11) = (uint8_t)(local_rbp);
    goto loc_003469E8;
loc_00346C17:
    if (((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20)))) != 5) goto loc_00346C3E;
    result = (uint8_t)((v_stack_p70) & (254));
    result = (uint8_t)((result) | (6));
    *(uint8_t *)(*(uint64_t *)(1 + 0x18) + 0x70) = (uint8_t)(result);
    goto loc_003469EB;
loc_00346C28:
    *(uint8_t *)(v_stack_p88 + 0x11) = 5;
    *(uint32_t *)(v_stack_p18 + 0x4) = (uint32_t)(local_rbp);
    result = KeInsertQueueDpc(*(uint64_t *)(v_stack_p88 + 0x18), v_stack_p18, v_stack_p88, Arg4);
    goto loc_00346BCC;
loc_00346C3E:
    if (((uint32_t)(*(uint64_t *)(v_stack_p88 + 0x18))) != 3) goto loc_003469EB;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11) = 2;
    goto loc_003469EB;
loc_00346C50:
    goto loc_00346BD4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003468C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
