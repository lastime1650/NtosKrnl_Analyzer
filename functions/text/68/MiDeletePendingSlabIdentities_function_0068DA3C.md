# MiDeletePendingSlabIdentities

- RVA: `0x0068DA3C`–`0x0068DDB0` (길이 `884` bytes)
- VA: `0x000000014068DA3C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD508`
- 디코드: `268`개 명령, `884/884` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0068DA8C` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0068DAA5` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0068DC3A` → [MiEnumerateSlabAllocatorsEx](../47/MiEnumerateSlabAllocatorsEx_function_004746F8.md) (function, `0x004746F8`)
- `0x0068DD68` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0068DD70` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0068DD92` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- [MiCreateSlabIdentity](MiCreateSlabIdentity_function_0068D2D4.md) at `0x0068D365`
- [MiDefragmentAllSlabAllocators](MiDefragmentAllSlabAllocators_function_0068D43C.md) at `0x0068D46E`
- [MiDeletePartitionSlabState](../../page/80/MiDeletePartitionSlabState_function_0080C890.md) at `0x0080C8A2`

### Static image references
- `0x0068DC30` → RVA `0x0068DE10` (`MiDeleteSlabEntriesForIdentity`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0068DA3C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0068DA41  55                              push rbp
0068DA42  56                              push rsi
0068DA43  57                              push rdi
0068DA44  41 54                           push r12
0068DA46  41 55                           push r13
0068DA48  41 56                           push r14
0068DA4A  41 57                           push r15
0068DA4C  48 8B EC                        mov rbp, rsp
0068DA4F  48 83 EC 50                     sub rsp, 0x50
0068DA53  45 33 E4                        xor r12d, r12d
0068DA56  48 83 CB FF                     or rbx, 0xffffffffffffffff
0068DA5A  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0068DA5E  44 8B EA                        mov r13d, edx
0068DA61  4C 8B F9                        mov r15, rcx
0068DA64  45 8B F4                        mov r14d, r12d
0068DA67  85 D2                           test edx, edx
0068DA69  75 48                           jne 0x14068dab3
0068DA6B  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
0068DA74  48 8D B9 78 47 00 00            lea rdi, [rcx + 0x4778]
0068DA7B  45 33 C0                        xor r8d, r8d
0068DA7E  33 D2                           xor edx, edx
0068DA80  48 8B CF                        mov rcx, rdi
0068DA83  66 41 01 9E E6 01 00 00         add word ptr [r14 + 0x1e6], bx
0068DA8B  90                              nop
0068DA8C  E8 9F 27 B8 FF                  call 0x140210230
0068DA91  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0068DA97  48 8B F0                        mov rsi, rax
0068DA9A  73 0E                           jae 0x14068daaa
0068DA9C  4C 8B C7                        mov r8, rdi
0068DA9F  48 8B D0                        mov rdx, rax
0068DAA2  48 8B CF                        mov rcx, rdi
0068DAA5  E8 E6 21 B8 FF                  call 0x14020fc90
0068DAAA  48 85 F6                        test rsi, rsi
0068DAAD  74 04                           je 0x14068dab3
0068DAAF  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0068DAB3  BE 40 00 00 00                  mov esi, 0x40
0068DAB8  45 8B D4                        mov r10d, r12d
0068DABB  89 75 E8                        mov dword ptr [rbp - 0x18], esi
0068DABE  BB 01 00 00 00                  mov ebx, 1
0068DAC3  41 8B BF 58 47 00 00            mov edi, dword ptr [r15 + 0x4758]
0068DACA  44 89 65 48                     mov dword ptr [rbp + 0x48], r12d
0068DACE  41 3B FA                        cmp edi, r10d
0068DAD1  0F 86 15 01 00 00               jbe 0x14068dbec
0068DAD7  41 8B C2                        mov eax, r10d
0068DADA  8D 57 FF                        lea edx, [rdi - 1]
0068DADD  48 C1 E8 05                     shr rax, 5
0068DAE1  41 83 E2 1F                     and r10d, 0x1f
0068DAE5  48 C1 EA 05                     shr rdx, 5
0068DAE9  45 8B DC                        mov r11d, r12d
0068DAEC  4D 8B A7 60 47 00 00            mov r12, qword ptr [r15 + 0x4760]
0068DAF3  41 8A CA                        mov cl, r10b
0068DAF6  4D 8D 0C 84                     lea r9, [r12 + rax*4]
0068DAFA  83 C8 FF                        or eax, 0xffffffff
0068DAFD  49 8D 34 94                     lea rsi, [r12 + rdx*4]
0068DB01  D3 E0                           shl eax, cl
0068DB03  41 8B 11                        mov edx, dword ptr [r9]
0068DB06  23 D0                           and edx, eax
0068DB08  49 8D 41 04                     lea rax, [r9 + 4]
0068DB0C  85 D2                           test edx, edx
0068DB0E  75 12                           jne 0x14068db22
0068DB10  48 3B C6                        cmp rax, rsi
0068DB13  77 2C                           ja 0x14068db41
0068DB15  49 83 C1 04                     add r9, 4
0068DB19  48 83 C0 04                     add rax, 4
0068DB1D  41 8B 11                        mov edx, dword ptr [r9]
0068DB20  EB EA                           jmp 0x14068db0c
0068DB22  8B C2                           mov eax, edx
0068DB24  4D 8B C1                        mov r8, r9
0068DB27  4D 2B C4                        sub r8, r12
0068DB2A  48 0F BC C8                     bsf rcx, rax
0068DB2E  49 C1 F8 02                     sar r8, 2
0068DB32  41 C1 E0 05                     shl r8d, 5
0068DB36  44 03 C1                        add r8d, ecx
0068DB39  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
0068DB3C  44 3B C7                        cmp r8d, edi
0068DB3F  76 05                           jbe 0x14068db46
0068DB41  44 8B C7                        mov r8d, edi
0068DB44  EB 49                           jmp 0x14068db8f
0068DB46  8B C3                           mov eax, ebx
0068DB48  D3 E0                           shl eax, cl
0068DB4A  2B C3                           sub eax, ebx
0068DB4C  0B D0                           or edx, eax
0068DB4E  F7 D2                           not edx
0068DB50  85 D2                           test edx, edx
0068DB52  75 17                           jne 0x14068db6b
0068DB54  49 8D 41 04                     lea rax, [r9 + 4]
0068DB58  48 3B C6                        cmp rax, rsi
0068DB5B  77 07                           ja 0x14068db64
0068DB5D  8B 10                           mov edx, dword ptr [rax]
0068DB5F  4C 8B C8                        mov r9, rax
0068DB62  EB EA                           jmp 0x14068db4e
0068DB64  B8 20 00 00 00                  mov eax, 0x20
0068DB69  EB 06                           jmp 0x14068db71
0068DB6B  8B C2                           mov eax, edx
0068DB6D  48 0F BC C0                     bsf rax, rax
0068DB71  4D 2B CC                        sub r9, r12
0068DB74  89 45 48                        mov dword ptr [rbp + 0x48], eax
0068DB77  4D 8B D9                        mov r11, r9
0068DB7A  49 C1 FB 02                     sar r11, 2
0068DB7E  41 C1 E3 05                     shl r11d, 5
0068DB82  44 03 D8                        add r11d, eax
0068DB85  44 3B DF                        cmp r11d, edi
0068DB88  44 0F 47 DF                     cmova r11d, edi
0068DB8C  45 2B D8                        sub r11d, r8d
0068DB8F  45 33 E4                        xor r12d, r12d
0068DB92  45 85 DB                        test r11d, r11d
0068DB95  74 55                           je 0x14068dbec
0068DB97  47 8D 14 03                     lea r10d, [r11 + r8]
0068DB9B  45 3A C2                        cmp r8b, r10b
0068DB9E  0F 83 1F FF FF FF               jae 0x14068dac3
0068DBA4  45 0F B6 C8                     movzx r9d, r8b
0068DBA8  41 8D 44 24 01                  lea eax, [r12 + 1]
0068DBAD  49 81 C1 AB 08 00 00            add r9, 0x8ab
0068DBB4  4F 8D 0C CF                     lea r9, [r15 + r9*8]
0068DBB8  4D 39 21                        cmp qword ptr [r9], r12
0068DBBB  75 1E                           jne 0x14068dbdb
0068DBBD  41 0F B6 C8                     movzx ecx, r8b
0068DBC1  8B D1                           mov edx, ecx
0068DBC3  83 E1 07                        and ecx, 7
0068DBC6  48 C1 EA 03                     shr rdx, 3
0068DBCA  0F BE 44 15 E0                  movsx eax, byte ptr [rbp + rdx - 0x20]
0068DBCF  0F AB C8                        bts eax, ecx
0068DBD2  88 44 15 E0                     mov byte ptr [rbp + rdx - 0x20], al
0068DBD6  B8 01 00 00 00                  mov eax, 1
0068DBDB  44 02 C0                        add r8b, al
0068DBDE  49 83 C1 08                     add r9, 8
0068DBE2  45 3A C2                        cmp r8b, r10b
0068DBE5  72 D1                           jb 0x14068dbb8
0068DBE7  E9 D2 FE FF FF                  jmp 0x14068dabe
0068DBEC  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
0068DBEF  BE 40 00 00 00                  mov esi, 0x40
0068DBF4  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
0068DBFB  3B C6                           cmp eax, esi
0068DBFD  72 22                           jb 0x14068dc21
0068DBFF  44 39 65 E0                     cmp dword ptr [rbp - 0x20], r12d
0068DC03  75 1C                           jne 0x14068dc21
0068DC05  48 8D 45 E4                     lea rax, [rbp - 0x1c]
0068DC09  48 8D 4D E4                     lea rcx, [rbp - 0x1c]
0068DC0D  48 3B C1                        cmp rax, rcx
0068DC10  0F 84 36 01 00 00               je 0x14068dd4c
0068DC16  44 39 20                        cmp dword ptr [rax], r12d
0068DC19  75 06                           jne 0x14068dc21
0068DC1B  48 83 C0 04                     add rax, 4
0068DC1F  EB E8                           jmp 0x14068dc09
0068DC21  41 83 C9 FF                     or r9d, 0xffffffff
0068DC25  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
0068DC2D  45 33 C0                        xor r8d, r8d
0068DC30  48 8D 15 D9 01 00 00            lea rdx, [rip + 0x1d9]
0068DC37  49 8B CF                        mov rcx, r15
0068DC3A  E8 B9 6A DE FF                  call 0x1404746f8
0068DC3F  45 8B D4                        mov r10d, r12d
0068DC42  44 89 65 50                     mov dword ptr [rbp + 0x50], r12d
0068DC46  44 3B D6                        cmp r10d, esi
0068DC49  0F 83 FD 00 00 00               jae 0x14068dd4c
0068DC4F  41 8B C2                        mov eax, r10d
0068DC52  4C 8D 4D E0                     lea r9, [rbp - 0x20]
0068DC56  48 C1 E8 05                     shr rax, 5
0068DC5A  41 83 E2 1F                     and r10d, 0x1f
0068DC5E  41 8A CA                        mov cl, r10b
0068DC61  45 8B DC                        mov r11d, r12d
0068DC64  4D 8D 0C 81                     lea r9, [r9 + rax*4]
0068DC68  83 C8 FF                        or eax, 0xffffffff
0068DC6B  41 8B 11                        mov edx, dword ptr [r9]
0068DC6E  D3 E0                           shl eax, cl
0068DC70  23 D0                           and edx, eax
0068DC72  49 8D 41 04                     lea rax, [r9 + 4]
0068DC76  85 D2                           test edx, edx
0068DC78  75 20                           jne 0x14068dc9a
0068DC7A  48 8D 4D E4                     lea rcx, [rbp - 0x1c]
0068DC7E  48 3B C1                        cmp rax, rcx
0068DC81  77 0D                           ja 0x14068dc90
0068DC83  49 83 C1 04                     add r9, 4
0068DC87  48 83 C0 04                     add rax, 4
0068DC8B  41 8B 11                        mov edx, dword ptr [r9]
0068DC8E  EB E6                           jmp 0x14068dc76
0068DC90  44 8B C6                        mov r8d, esi
0068DC93  BF 01 00 00 00                  mov edi, 1
0068DC98  EB 7E                           jmp 0x14068dd18
0068DC9A  8B C2                           mov eax, edx
0068DC9C  4D 8B C1                        mov r8, r9
0068DC9F  48 0F BC C8                     bsf rcx, rax
0068DCA3  48 8D 45 E0                     lea rax, [rbp - 0x20]
0068DCA7  BF 01 00 00 00                  mov edi, 1
0068DCAC  4C 2B C0                        sub r8, rax
0068DCAF  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
0068DCB2  49 C1 F8 02                     sar r8, 2
0068DCB6  41 C1 E0 05                     shl r8d, 5
0068DCBA  44 03 C1                        add r8d, ecx
0068DCBD  44 3B C6                        cmp r8d, esi
0068DCC0  76 05                           jbe 0x14068dcc7
0068DCC2  44 8B C6                        mov r8d, esi
0068DCC5  EB 51                           jmp 0x14068dd18
0068DCC7  8B C7                           mov eax, edi
0068DCC9  D3 E0                           shl eax, cl
0068DCCB  2B C7                           sub eax, edi
0068DCCD  0B D0                           or edx, eax
0068DCCF  F7 D2                           not edx
0068DCD1  85 D2                           test edx, edx
0068DCD3  75 1B                           jne 0x14068dcf0
0068DCD5  49 8D 41 04                     lea rax, [r9 + 4]
0068DCD9  48 8D 4D E4                     lea rcx, [rbp - 0x1c]
0068DCDD  48 3B C1                        cmp rax, rcx
0068DCE0  77 07                           ja 0x14068dce9
0068DCE2  8B 10                           mov edx, dword ptr [rax]
0068DCE4  4C 8B C8                        mov r9, rax
0068DCE7  EB E6                           jmp 0x14068dccf
0068DCE9  B8 20 00 00 00                  mov eax, 0x20
0068DCEE  EB 06                           jmp 0x14068dcf6
0068DCF0  8B C2                           mov eax, edx
0068DCF2  48 0F BC C0                     bsf rax, rax
0068DCF6  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0068DCFA  89 45 50                        mov dword ptr [rbp + 0x50], eax
0068DCFD  4C 2B C9                        sub r9, rcx
0068DD00  4D 8B D9                        mov r11, r9
0068DD03  49 C1 FB 02                     sar r11, 2
0068DD07  41 C1 E3 05                     shl r11d, 5
0068DD0B  44 03 D8                        add r11d, eax
0068DD0E  44 3B DE                        cmp r11d, esi
0068DD11  44 0F 47 DE                     cmova r11d, esi
0068DD15  45 2B D8                        sub r11d, r8d
0068DD18  45 85 DB                        test r11d, r11d
0068DD1B  74 2F                           je 0x14068dd4c
0068DD1D  47 8D 14 03                     lea r10d, [r11 + r8]
0068DD21  EB 1F                           jmp 0x14068dd42
0068DD23  41 0F B6 C8                     movzx ecx, r8b
0068DD27  8B D1                           mov edx, ecx
0068DD29  83 E1 07                        and ecx, 7
0068DD2C  48 C1 EA 03                     shr rdx, 3
0068DD30  49 03 97 60 47 00 00            add rdx, qword ptr [r15 + 0x4760]
0068DD37  0F BE 02                        movsx eax, byte ptr [rdx]
0068DD3A  0F B3 C8                        btr eax, ecx
0068DD3D  88 02                           mov byte ptr [rdx], al
0068DD3F  44 02 C7                        add r8b, dil
0068DD42  45 3A C2                        cmp r8b, r10b
0068DD45  72 DC                           jb 0x14068dd23
0068DD47  E9 F6 FE FF FF                  jmp 0x14068dc42
0068DD4C  45 85 ED                        test r13d, r13d
0068DD4F  75 46                           jne 0x14068dd97
0068DD51  49 8D BF 78 47 00 00            lea rdi, [r15 + 0x4778]
0068DD58  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
0068DD5D  80 E3 06                        and bl, 6
0068DD60  80 FB 02                        cmp bl, 2
0068DD63  75 08                           jne 0x14068dd6d
0068DD65  48 8B CF                        mov rcx, rdi
0068DD68  E8 63 80 BD FF                  call 0x140265dd0
0068DD6D  48 8B CF                        mov rcx, rdi
0068DD70  E8 8B 38 C5 FF                  call 0x1402e1600
0068DD75  B9 01 00 00 00                  mov ecx, 1
0068DD7A  90                              nop
0068DD7B  66 41 01 8E E6 01 00 00         add word ptr [r14 + 0x1e6], cx
0068DD83  75 12                           jne 0x14068dd97
0068DD85  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
0068DD8C  90                              nop
0068DD8D  48 39 00                        cmp qword ptr [rax], rax
0068DD90  74 05                           je 0x14068dd97
0068DD92  E8 E9 4E C5 FF                  call 0x1402e2c80
0068DD97  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0068DD9F  48 83 C4 50                     add rsp, 0x50
0068DDA3  41 5F                           pop r15
0068DDA5  41 5E                           pop r14
0068DDA7  41 5D                           pop r13
0068DDA9  41 5C                           pop r12
0068DDAB  5F                              pop rdi
0068DDAC  5E                              pop rsi
0068DDAD  5D                              pop rbp
0068DDAE  C3                              ret
0068DDAF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeletePendingSlabIdentities(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    v_r12 = 0;
    v_rbx = (v_rbx) | (-1);
    v_stack_m58 = 0;
    if (a2 != 0) goto loc_0068DAB3;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 18296, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 18296;
        a2 = result;
        a1 = a1 + 18296;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m50 = 64;
loc_0068DABE:
loc_0068DAC3:
    v_stack_p10 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264)))) <= 0) goto loc_0068DBEC;
    result = (0) >> (5);
    v_r10 = (unsigned int)((0) & (31));
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 18264)) - 1) >> (5);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) << ((unsigned __int8)((unsigned __int8)(v_r10))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 18272) + result * 4))) & ((unsigned int)(result)));
loc_0068DB0C:
    if (a2 != 0) goto loc_0068DB22;
    if ((*(unsigned __int64 *)(a1 + 18272) + result * 4 + 4) > (*(unsigned __int64 *)(a1 + 18272) + a2 * 4)) goto loc_0068DB41;
    a4 = (*(unsigned __int64 *)(a1 + 18272) + result * 4) + (4);
    result = (*(unsigned __int64 *)(a1 + 18272) + result * 4 + 4) + (4);
    goto loc_0068DB0C;
loc_0068DB22:
    a3 = (a4) - (*(unsigned __int64 *)(a1 + 18272));
    a3 = (a3) >> (2);
    a3 = (unsigned int)((a3) << (5));
    a3 = (unsigned int)((a3) + ((unsigned int)((unsigned __int8)(v_r10))));
    v_stack_p10 = (unsigned int)((unsigned __int8)(v_r10));
    if (a3 <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264))))) goto loc_0068DB46;
loc_0068DB41:
    goto loc_0068DB8F;
loc_0068DB46:
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned __int8)(v_r10))));
    result = (unsigned int)((result) - (1));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | ((unsigned int)(result)));
loc_0068DB4E:
    a2 = (unsigned int)(~(a2));
    if (a2 != 0) goto loc_0068DB6B;
    if ((a4 + 4) > (*(unsigned __int64 *)(a1 + 18272) + a2 * 4)) goto loc_0068DB64;
    goto loc_0068DB4E;
loc_0068DB64:
    goto loc_0068DB71;
loc_0068DB6B:
loc_0068DB71:
    a4 = (a4 + 4) - (*(unsigned __int64 *)(a1 + 18272));
    v_stack_p10 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))));
    v_r11 = (a4) >> (2);
    v_r11 = (unsigned int)((v_r11) << (5));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))))));
    if (((unsigned int)(v_r11)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264))))) { v_r11 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264))); }
    v_r11 = (unsigned int)((v_r11) - ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264)))))));
loc_0068DB8F:
    v_r12 = 0;
    if ((unsigned int)(v_r11) == 0) goto loc_0068DBEC;
    if (((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264)))))) >= ((unsigned __int8)(v_r11 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264)))) * 1))) goto loc_0068DAC3;
    a4 = ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264)))))) + (0x8ABULL);
loc_0068DBB8:
    result = v_r12 + 1;
    if ((*(unsigned __int64 *)(a1 + a4 * 8)) == 0) {
        a1 = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264)))));
        a2 = (unsigned int)(a1);
        a1 = (unsigned int)((a1) & (7));
        a2 = (a2) >> (3);
        result = (__int8)(*(unsigned __int8 *)(v_rsp + a2 * 1 - 32));
        *(unsigned __int8 *)(v_rsp + a2 * 1 - 32) = (unsigned __int8)(result);
        result = 1;
    }
    a3 = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264))))) + ((unsigned __int8)(result)));
    a4 = (a1 + a4 * 8) + (8);
    if (((unsigned __int8)(a3)) < ((unsigned __int8)(v_r11 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18264)))) * 1))) goto loc_0068DBB8;
    goto loc_0068DABE;
loc_0068DBEC:
    if (((unsigned int)((unsigned int)(v_stack_m50))) < 64) goto loc_0068DC21;
    if (v_stack_m58 != 0) goto loc_0068DC21;
loc_0068DC09:
    if (v_stack_m54 == v_stack_m54) goto loc_0068DD4C;
    if ((*(unsigned int *)(v_stack_m54)) != 0) goto loc_0068DC21;
    result = (v_stack_m54) + (4);
    goto loc_0068DC09;
loc_0068DC21:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    v_stack_m68 = 8;
    a3 = 0;
    result = MiEnumerateSlabAllocatorsEx(a1, v_rip + 473, a3, a4);
loc_0068DC42:
    v_stack_p18 = 0;
    if (0 >= 64) goto loc_0068DD4C;
    result = (0) >> (5);
    v_r10 = (unsigned int)((0) & (31));
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) << ((unsigned __int8)((unsigned __int8)(v_r10))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m58 + result * 4))) & ((unsigned int)(result)));
loc_0068DC76:
    if (a2 != 0) goto loc_0068DC9A;
    if ((v_stack_m58 + result * 4 + 4) > v_stack_m54) goto loc_0068DC90;
    a4 = (v_stack_m58 + result * 4) + (4);
    result = (v_stack_m58 + result * 4 + 4) + (4);
    goto loc_0068DC76;
loc_0068DC90:
    goto loc_0068DD18;
loc_0068DC9A:
    a3 = (a4) - (v_stack_m58);
    v_stack_p18 = (unsigned int)(v_stack_m54);
    a3 = (a3) >> (2);
    a3 = (unsigned int)((a3) << (5));
    a3 = (unsigned int)((a3) + ((unsigned int)(v_stack_m54)));
    if (a3 <= 64) goto loc_0068DCC7;
    goto loc_0068DD18;
loc_0068DCC7:
    result = (unsigned int)((1) << ((unsigned __int8)(v_stack_m54)));
    result = (unsigned int)((result) - (1));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | ((unsigned int)(result)));
loc_0068DCCF:
    a2 = (unsigned int)(~(a2));
    if (a2 != 0) goto loc_0068DCF0;
    if ((a4 + 4) > v_stack_m54) goto loc_0068DCE9;
    goto loc_0068DCCF;
loc_0068DCE9:
    goto loc_0068DCF6;
loc_0068DCF0:
loc_0068DCF6:
    v_stack_p18 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))));
    a4 = (a4 + 4) - (v_stack_m58);
    v_r11 = (a4) >> (2);
    v_r11 = (unsigned int)((v_r11) << (5));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))))));
    if (((unsigned int)(v_r11)) > 64) { v_r11 = 64; }
    v_r11 = (unsigned int)((v_r11) - (64));
loc_0068DD18:
    if ((unsigned int)(v_r11) == 0) goto loc_0068DD4C;
    goto loc_0068DD42;
loc_0068DD23:
    a1 = (unsigned int)((64) & (7));
    a2 = (64) >> (3);
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 18272));
    *(unsigned __int8 *)(a2) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a2)));
    a3 = (unsigned __int8)((64) + (1));
loc_0068DD42:
    if (((unsigned __int8)(a3)) < ((unsigned __int8)(v_r11 + 64 * 1))) goto loc_0068DD23;
    goto loc_0068DC42;
loc_0068DD4C:
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_0068DD97;
    v_rbx = (unsigned __int8)((-1) & (6));
    result = (__int8)(*(unsigned __int8 *)(a2));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = a1 + 18296;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 18296, a2, a3, a4);
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_0068DD97;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeletePendingSlabIdentities(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m50;
    uint64_t v_stack_m54;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    local_r12 = 0;
    local_rbx = (local_rbx) | (-1);
    v_stack_m58 = 0;
    if (Arg2 != 0) goto loc_0068DAB3;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 18296, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 18296;
        Arg2 = result;
        Arg1 = Arg1 + 18296;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m50 = 64;
loc_0068DABE:
loc_0068DAC3:
    v_stack_p10 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758)))) <= 0) goto loc_0068DBEC;
    result = (0) >> (5);
    local_r10 = (uint32_t)((0) & (31));
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x4758)) - 1) >> (5);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) << ((uint8_t)((uint8_t)(local_r10))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x4760) + result * 4))) & ((uint32_t)(result)));
loc_0068DB0C:
    if (Arg2 != 0) goto loc_0068DB22;
    if ((*(uint64_t *)(arg1 + 0x4760) + result * 4 + 4) > (*(uint64_t *)(arg1 + 0x4760) + Arg2 * 4)) goto loc_0068DB41;
    a4 = (*(uint64_t *)(arg1 + 0x4760) + result * 4) + (4);
    result = (*(uint64_t *)(arg1 + 0x4760) + result * 4 + 4) + (4);
    goto loc_0068DB0C;
loc_0068DB22:
    Arg3 = (a4) - (*(uint64_t *)(arg1 + 0x4760));
    Arg3 = (Arg3) >> (2);
    Arg3 = (uint32_t)((Arg3) << (5));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)((uint8_t)(local_r10))));
    v_stack_p10 = (uint32_t)((uint8_t)(local_r10));
    if (Arg3 <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758))))) goto loc_0068DB46;
loc_0068DB41:
    goto loc_0068DB8F;
loc_0068DB46:
    result = (uint32_t)((1) << ((uint8_t)((uint8_t)(local_r10))));
    result = (uint32_t)((result) - (1));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(a4))) | ((uint32_t)(result)));
loc_0068DB4E:
    Arg2 = (uint32_t)(~(Arg2));
    if (Arg2 != 0) goto loc_0068DB6B;
    if ((a4 + 4) > (*(uint64_t *)(arg1 + 0x4760) + Arg2 * 4)) goto loc_0068DB64;
    goto loc_0068DB4E;
loc_0068DB64:
    goto loc_0068DB71;
loc_0068DB6B:
loc_0068DB71:
    a4 = (a4 + 4) - (*(uint64_t *)(arg1 + 0x4760));
    v_stack_p10 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x4)))));
    local_r11 = (a4) >> (2);
    local_r11 = (uint32_t)((local_r11) << (5));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x4)))))));
    if (((uint32_t)(local_r11)) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758))))) { local_r11 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758))); }
    local_r11 = (uint32_t)((local_r11) - ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758)))))));
loc_0068DB8F:
    local_r12 = 0;
    if ((uint32_t)(local_r11) == 0) goto loc_0068DBEC;
    if (((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758)))))) >= ((uint8_t)(local_r11 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758)))) * 1))) goto loc_0068DAC3;
    a4 = ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758)))))) + (0x8ABULL);
loc_0068DBB8:
    result = local_r12 + 1;
    if ((*(uint64_t *)(arg1 + a4 * 8)) == 0) {
        Arg1 = (uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758)))));
        Arg2 = (uint32_t)(Arg1);
        Arg1 = (uint32_t)((Arg1) & (7));
        Arg2 = (Arg2) >> (3);
        result = (int8_t)(*(uint8_t *)(local_rsp + Arg2 * 1 - 0x20));
        *(uint8_t *)(local_rsp + Arg2 * 1 - 0x20) = (uint8_t)(result);
        result = 1;
    }
    Arg3 = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758))))) + ((uint8_t)(result)));
    a4 = (Arg1 + a4 * 8) + (8);
    if (((uint8_t)(Arg3)) < ((uint8_t)(local_r11 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4758)))) * 1))) goto loc_0068DBB8;
    goto loc_0068DABE;
loc_0068DBEC:
    if (((uint32_t)((uint32_t)(v_stack_m50))) < 64) goto loc_0068DC21;
    if (v_stack_m58 != 0) goto loc_0068DC21;
loc_0068DC09:
    if (v_stack_m54 == v_stack_m54) goto loc_0068DD4C;
    if ((*(uint32_t *)(v_stack_m54)) != 0) goto loc_0068DC21;
    result = (v_stack_m54) + (4);
    goto loc_0068DC09;
loc_0068DC21:
    a4 = (uint32_t)((a4) | (0xFFFFFFFFULL));
    v_stack_m68 = 8;
    Arg3 = 0;
    result = MiEnumerateSlabAllocatorsEx(Arg1, v_rip + 473, Arg3, a4);
loc_0068DC42:
    v_stack_p18 = 0;
    if (0 >= 64) goto loc_0068DD4C;
    result = (0) >> (5);
    local_r10 = (uint32_t)((0) & (31));
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) << ((uint8_t)((uint8_t)(local_r10))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + result * 4))) & ((uint32_t)(result)));
loc_0068DC76:
    if (Arg2 != 0) goto loc_0068DC9A;
    if ((v_stack_m58 + result * 4 + 4) > v_stack_m54) goto loc_0068DC90;
    a4 = (v_stack_m58 + result * 4) + (4);
    result = (v_stack_m58 + result * 4 + 4) + (4);
    goto loc_0068DC76;
loc_0068DC90:
    goto loc_0068DD18;
loc_0068DC9A:
    Arg3 = (a4) - (v_stack_m58);
    v_stack_p18 = (uint32_t)(v_stack_m54);
    Arg3 = (Arg3) >> (2);
    Arg3 = (uint32_t)((Arg3) << (5));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(v_stack_m54)));
    if (Arg3 <= 64) goto loc_0068DCC7;
    goto loc_0068DD18;
loc_0068DCC7:
    result = (uint32_t)((1) << ((uint8_t)(v_stack_m54)));
    result = (uint32_t)((result) - (1));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(a4))) | ((uint32_t)(result)));
loc_0068DCCF:
    Arg2 = (uint32_t)(~(Arg2));
    if (Arg2 != 0) goto loc_0068DCF0;
    if ((a4 + 4) > v_stack_m54) goto loc_0068DCE9;
    goto loc_0068DCCF;
loc_0068DCE9:
    goto loc_0068DCF6;
loc_0068DCF0:
loc_0068DCF6:
    v_stack_p18 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x4)))));
    a4 = (a4 + 4) - (v_stack_m58);
    local_r11 = (a4) >> (2);
    local_r11 = (uint32_t)((local_r11) << (5));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x4)))))));
    if (((uint32_t)(local_r11)) > 64) { local_r11 = 64; }
    local_r11 = (uint32_t)((local_r11) - (64));
loc_0068DD18:
    if ((uint32_t)(local_r11) == 0) goto loc_0068DD4C;
    goto loc_0068DD42;
loc_0068DD23:
    Arg1 = (uint32_t)((64) & (7));
    Arg2 = (64) >> (3);
    Arg2 = (Arg2) + (*(uint64_t *)(arg1 + 0x4760));
    *(uint8_t *)(Arg2) = (uint8_t)((int8_t)(*(uint8_t *)(Arg2)));
    Arg3 = (uint8_t)((64) + (1));
loc_0068DD42:
    if (((uint8_t)(Arg3)) < ((uint8_t)(local_r11 + 64 * 1))) goto loc_0068DD23;
    goto loc_0068DC42;
loc_0068DD4C:
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_0068DD97;
    local_rbx = (uint8_t)((-1) & (6));
    result = (int8_t)(*(uint8_t *)(Arg2));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = Arg1 + 18296;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(Arg1 + 18296, Arg2, Arg3, a4);
    if (((uint8_t)(local_rbx)) != 2) goto loc_0068DD97;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0 + r9*8` | `64` | `R` |
| `Arg1` | `+ 0x4758` | `32` | `R` |
| `Arg1` | `+ 0x4760` | `64` | `R` |
| `Arg1` | `+ 0x4778` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0068DA3C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
