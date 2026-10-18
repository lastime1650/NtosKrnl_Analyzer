# RtlpHpLfhSubsegmentDelayFreeListProcess

- RVA: `0x00323CE0`–`0x0032421F` (길이 `1,343` bytes)
- VA: `0x0000000140323CE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000759D4`
- 디코드: `339`개 명령, `1,343/1,343` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00323F70` → [RtlpHpEnvCompactionSchedule](RtlpHpEnvCompactionSchedule_function_003264A0.md) (function, `0x003264A0`)
- `0x00323FBF` → [RtlpHpLfhSubsegmentFindEmptyUnits](RtlpHpLfhSubsegmentFindEmptyUnits_function_00324600.md) (function, `0x00324600`)
- `0x00323FF0` → [RtlpHpAcquireLockExclusive](RtlpHpAcquireLockExclusive_function_003246B0.md) (function, `0x003246B0`)
- `0x0032401C` → [RtlpHpReleaseLockExclusive](RtlpHpReleaseLockExclusive_function_00324230.md) (function, `0x00324230`)
- `0x0032403C` → [RtlpHpReleaseLockShared](RtlpHpReleaseLockShared_function_003245B0.md) (function, `0x003245B0`)
- `0x00324063` → [RtlpHpLfhContextUpdateFreeCommitCount](../49/RtlpHpLfhContextUpdateFreeCommitCount_function_00497E98.md) (function, `0x00497E98`)
- `0x003240C6` → [RtlpHpSegLfhVsDecommit](RtlpHpSegLfhVsDecommit_function_003243F0.md) (function, `0x003243F0`)
- `0x003240D7` → [RtlpHpLfhSubsegmentDecBlockCounts](RtlpHpLfhSubsegmentDecBlockCounts_function_003244D0.md) (function, `0x003244D0`)
- `0x0032411D` → [RtlpHpLfhSubsegmentDelayFreeListBatch](../47/RtlpHpLfhSubsegmentDelayFreeListBatch_function_004792F4.md) (function, `0x004792F4`)
- `0x00324146` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x00324167` → [RtlpHpLfhBlockBitmapInitialize](../2E/RtlpHpLfhBlockBitmapInitialize_function_002E8418.md) (function, `0x002E8418`)
- `0x0032419F` → [RtlpHpLfhSubsegmentSetWitheldBlocks](../48/RtlpHpLfhSubsegmentSetWitheldBlocks_function_0048478C.md) (function, `0x0048478C`)
- `0x003241EC` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x0032420B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [RtlpHpLfhOwnerRunMaintenance](../2E/RtlpHpLfhOwnerRunMaintenance_function_002E8980.md) at `0x002E8AC6`
- [RtlpHpLfhOwnerFreeListProcess](../2E/RtlpHpLfhOwnerFreeListProcess_function_002E8BA0.md) at `0x002E8C88`
- [RtlpHpLfhOwnerGetSubsegment](../2E/RtlpHpLfhOwnerGetSubsegment_function_002E8E0C.md) at `0x002E8E9A`

### Static image references
- `0x00323D16` → RVA `0x00E28308` (`.data`; read)
- `0x00324088` → RVA `0x003243F0` (`RtlpHpSegLfhVsDecommit`; read)
- `0x00324096` → RVA `0x00E28300` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00323CE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00323CE5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00323CEA  55                              push rbp
00323CEB  56                              push rsi
00323CEC  57                              push rdi
00323CED  41 54                           push r12
00323CEF  41 55                           push r13
00323CF1  41 56                           push r14
00323CF3  41 57                           push r15
00323CF5  48 83 EC 70                     sub rsp, 0x70
00323CF9  44 0F B6 72 33                  movzx r14d, byte ptr [rdx + 0x33]
00323CFE  48 8B FA                        mov rdi, rdx
00323D01  4C 8B FA                        mov r15, rdx
00323D04  41 80 E6 01                     and r14b, 1
00323D08  49 C1 EF 0C                     shr r15, 0xc
00323D0C  4D 8B E0                        mov r12, r8
00323D0F  49 C1 EC 10                     shr r12, 0x10
00323D13  41 8B C7                        mov eax, r15d
00323D16  33 05 EC 45 B0 00               xor eax, dword ptr [rip + 0xb045ec]
00323D1C  4C 8D 6F 27                     lea r13, [rdi + 0x27]
00323D20  33 42 28                        xor eax, dword ptr [rdx + 0x28]
00323D23  48 8B D9                        mov rbx, rcx
00323D26  0F B7 4F 22                     movzx ecx, word ptr [rdi + 0x22]
00323D2A  44 8B C8                        mov r9d, eax
00323D2D  44 0F B7 D0                     movzx r10d, ax
00323D31  49 C1 E9 10                     shr r9, 0x10
00323D35  4C 03 CA                        add r9, rdx
00323D38  8B E8                           mov ebp, eax
00323D3A  0F B7 47 20                     movzx eax, word ptr [rdi + 0x20]
00323D3E  41 0F B7 D4                     movzx edx, r12w
00323D42  03 C2                           add eax, edx
00323D44  44 88 B4 24 B8 00 00 00         mov byte ptr [rsp + 0xb8], r14b
00323D4C  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00323D51  44 89 54 24 38                  mov dword ptr [rsp + 0x38], r10d
00323D56  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
00323D5B  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
00323D60  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00323D65  3B C8                           cmp ecx, eax
00323D67  0F 84 E5 03 00 00               je 0x140324152
00323D6D  41 80 7D 00 01                  cmp byte ptr [r13], 1
00323D72  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00323D77  0F 84 7D 03 00 00               je 0x1403240fa
00323D7D  0F B7 AC 24 C0 00 00 00         movzx ebp, word ptr [rsp + 0xc0]
00323D85  66 85 ED                        test bp, bp
00323D88  0F 84 5B 01 00 00               je 0x140323ee9
00323D8E  66 90                           nop
00323D90  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
00323D94  44 0F B7 C5                     movzx r8d, bp
00323D98  8B D0                           mov edx, eax
00323D9A  41 FF C8                        dec r8d
00323D9D  48 C1 E8 20                     shr rax, 0x20
00323DA1  41 8B F0                        mov esi, r8d
00323DA4  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
00323DA9  41 0F AF F2                     imul esi, r10d
00323DAD  49 03 F1                        add rsi, r9
00323DB0  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
00323DB5  33 16                           xor edx, dword ptr [rsi]
00323DB7  0F B7 2E                        movzx ebp, word ptr [rsi]
00323DBA  40 0F B6 CD                     movzx ecx, bpl
00323DBE  D3 C2                           rol edx, cl
00323DC0  33 D0                           xor edx, eax
00323DC2  66 89 AC 24 C0 00 00 00         mov word ptr [rsp + 0xc0], bp
00323DCA  33 D6                           xor edx, esi
00323DCC  39 56 08                        cmp dword ptr [rsi + 8], edx
00323DCF  0F 85 52 03 00 00               jne 0x140324127
00323DD5  44 8B DE                        mov r11d, esi
00323DD8  45 84 F6                        test r14b, r14b
00323DDB  0F 85 9E 00 00 00               jne 0x140323e7f
00323DE1  41 80 7D 00 01                  cmp byte ptr [r13], 1
00323DE6  0F 86 93 00 00 00               jbe 0x140323e7f
00323DEC  0F B6 4F 26                     movzx ecx, byte ptr [rdi + 0x26]
00323DF0  44 2B DF                        sub r11d, edi
00323DF3  0F B6 47 18                     movzx eax, byte ptr [rdi + 0x18]
00323DF7  45 8B C3                        mov r8d, r11d
00323DFA  41 C1 E8 0C                     shr r8d, 0xc
00323DFE  41 D3 E8                        shr r8d, cl
00323E01  4C 8D 0C C7                     lea r9, [rdi + rax*8]
00323E05  4F 8D 14 00                     lea r10, [r8 + r8]
00323E09  4D 03 CA                        add r9, r10
00323E0C  41 0F 0D 09                     prefetchw byte ptr [r9]
00323E10  0F B7 57 28                     movzx edx, word ptr [rdi + 0x28]
00323E14  41 BC FF FF FF FF               mov r12d, 0xffffffff
00323E1A  41 0F B7 C7                     movzx eax, r15w
00323E1E  33 D0                           xor edx, eax
00323E20  0F B7 05 E1 44 B0 00            movzx eax, word ptr [rip + 0xb044e1]
00323E27  33 C2                           xor eax, edx
00323E29  33 D2                           xor edx, edx
00323E2B  FF C8                           dec eax
00323E2D  41 03 C3                        add eax, r11d
00323E30  C1 E8 0C                        shr eax, 0xc
00323E33  D3 E8                           shr eax, cl
00323E35  41 2B C0                        sub eax, r8d
00323E38  FF C0                           inc eax
00323E3A  49 8D 0C 41                     lea rcx, [r9 + rax*2]
00323E3E  4C 3B C9                        cmp r9, rcx
00323E41  73 3C                           jae 0x140323e7f
00323E43  B8 FF FF FF FF                  mov eax, 0xffffffff
00323E48  66 F0 41 0F C1 01               lock xadd word ptr [r9], ax
00323E4E  66 83 E8 01                     sub ax, 1
00323E52  0F 84 15 02 00 00               je 0x14032406d
00323E58  66 83 F8 FF                     cmp ax, -1
00323E5C  75 02                           jne 0x140323e60
00323E5E  FF CA                           dec edx
00323E60  49 83 C1 02                     add r9, 2
00323E64  49 83 C2 02                     add r10, 2
00323E68  4C 3B C9                        cmp r9, rcx
00323E6B  72 D6                           jb 0x140323e43
00323E6D  85 D2                           test edx, edx
00323E6F  0F 85 CE 01 00 00               jne 0x140324043
00323E75  41 83 FC FF                     cmp r12d, -1
00323E79  0F 85 88 00 00 00               jne 0x140323f07
00323E7F  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00323E83  48 C7 C2 FE FF FF FF            mov rdx, 0xfffffffffffffffe
00323E8A  8B C8                           mov ecx, eax
00323E8C  44 8B C8                        mov r9d, eax
00323E8F  83 E1 3F                        and ecx, 0x3f
00323E92  48 C1 E8 06                     shr rax, 6
00323E96  48 D3 C2                        rol rdx, cl
00323E99  4C 8D 04 C7                     lea r8, [rdi + rax*8]
00323E9D  45 84 F6                        test r14b, r14b
00323EA0  0F 85 11 03 00 00               jne 0x1403241b7
00323EA6  41 0F 0D 48 40                  prefetchw byte ptr [r8 + 0x40]
00323EAB  49 8B 40 40                     mov rax, qword ptr [r8 + 0x40]
00323EAF  48 8B C8                        mov rcx, rax
00323EB2  48 23 CA                        and rcx, rdx
00323EB5  F0 49 0F B1 48 40               lock cmpxchg qword ptr [r8 + 0x40], rcx
00323EBB  75 F2                           jne 0x140323eaf
00323EBD  48 F7 D2                        not rdx
00323EC0  48 23 D0                        and rdx, rax
00323EC3  48 85 D2                        test rdx, rdx
00323EC6  0F 84 04 03 00 00               je 0x1403241d0
00323ECC  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00323ED1  44 8B 54 24 38                  mov r10d, dword ptr [rsp + 0x38]
00323ED6  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00323EDB  66 85 ED                        test bp, bp
00323EDE  0F 85 AC FE FF FF               jne 0x140323d90
00323EE4  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
00323EE9  66 44 01 67 20                  add word ptr [rdi + 0x20], r12w
00323EEE  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00323EF6  48 83 C4 70                     add rsp, 0x70
00323EFA  41 5F                           pop r15
00323EFC  41 5E                           pop r14
00323EFE  41 5D                           pop r13
00323F00  41 5C                           pop r12
00323F02  5F                              pop rdi
00323F03  5E                              pop rsi
00323F04  5D                              pop rbp
00323F05  C3                              ret
00323F06  CC                              int3
00323F07  33 F6                           xor esi, esi
00323F09  C7 44 24 30 00 00 00 00         mov dword ptr [rsp + 0x30], 0
00323F11  40 B5 FF                        mov bpl, 0xff
00323F14  45 85 E4                        test r12d, r12d
00323F17  78 78                           js 0x140323f91
00323F19  48 8B 13                        mov rdx, qword ptr [rbx]
00323F1C  89 B4 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], esi
00323F23  F6 42 0D 08                     test byte ptr [rdx + 0xd], 8
00323F27  75 79                           jne 0x140323fa2
00323F29  48 0F BF 42 16                  movsx rax, word ptr [rdx + 0x16]
00323F2E  41 B8 08 00 00 00               mov r8d, 8
00323F34  0F B6 4A 0B                     movzx ecx, byte ptr [rdx + 0xb]
00323F38  4C 8B 7C 10 18                  mov r15, qword ptr [rax + rdx + 0x18]
00323F3D  4C 03 7C 10 10                  add r15, qword ptr [rax + rdx + 0x10]
00323F42  4C 8B 74 10 08                  mov r14, qword ptr [rax + rdx + 8]
00323F47  49 8B C6                        mov rax, r14
00323F4A  48 D3 E8                        shr rax, cl
00323F4D  0F B6 4A 0C                     movzx ecx, byte ptr [rdx + 0xc]
00323F51  48 83 F8 08                     cmp rax, 8
00323F55  49 0F 46 C0                     cmovbe rax, r8
00323F59  49 D3 EE                        shr r14, cl
00323F5C  4D 3B F0                        cmp r14, r8
00323F5F  4D 0F 46 F0                     cmovbe r14, r8
00323F63  4C 3B F8                        cmp r15, rax
00323F66  0F 86 B5 00 00 00               jbe 0x140324021
00323F6C  48 8B 4A 38                     mov rcx, qword ptr [rdx + 0x38]
00323F70  E8 2B 25 00 00                  call 0x1403264a0
00323F75  85 C0                           test eax, eax
00323F77  0F 88 2C 02 00 00               js 0x1403241a9
00323F7D  4D 3B FE                        cmp r15, r14
00323F80  44 0F B6 B4 24 B8 00 00 00      movzx r14d, byte ptr [rsp + 0xb8]
00323F89  0F 86 9B 00 00 00               jbe 0x14032402a
00323F8F  EB 11                           jmp 0x140323fa2
00323F91  C7 84 24 C8 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xc8], 1
00323F9C  41 BC 01 00 00 00               mov r12d, 1
00323FA2  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00323FA7  44 3B E0                        cmp r12d, eax
00323FAA  73 7E                           jae 0x14032402a
00323FAC  44 8B B4 24 C8 00 00 00         mov r14d, dword ptr [rsp + 0xc8]
00323FB4  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00323FB9  41 8B D4                        mov edx, r12d
00323FBC  48 8B CF                        mov rcx, rdi
00323FBF  E8 3C 06 00 00                  call 0x140324600
00323FC4  44 8B E0                        mov r12d, eax
00323FC7  83 F8 FF                        cmp eax, -1
00323FCA  74 3B                           je 0x140324007
00323FCC  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
00323FD1  41 83 FD 02                     cmp r13d, 2
00323FD5  0F 82 1D 02 00 00               jb 0x1403241f8
00323FDB  85 F6                           test esi, esi
00323FDD  0F 85 A1 00 00 00               jne 0x140324084
00323FE3  0F B6 53 41                     movzx edx, byte ptr [rbx + 0x41]
00323FE7  48 8D 4F 38                     lea rcx, [rdi + 0x38]
00323FEB  BE 02 00 00 00                  mov esi, 2
00323FF0  E8 BB 06 00 00                  call 0x1403246b0
00323FF5  0F B6 E8                        movzx ebp, al
00323FF8  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
00323FFD  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00324002  44 3B E0                        cmp r12d, eax
00324005  72 AD                           jb 0x140323fb4
00324007  85 F6                           test esi, esi
00324009  74 16                           je 0x140324021
0032400B  0F B6 53 41                     movzx edx, byte ptr [rbx + 0x41]
0032400F  48 8D 4F 38                     lea rcx, [rdi + 0x38]
00324013  44 0F B6 C5                     movzx r8d, bpl
00324017  83 FE 02                        cmp esi, 2
0032401A  75 20                           jne 0x14032403c
0032401C  E8 0F 02 00 00                  call 0x140324230
00324021  44 0F B6 B4 24 B8 00 00 00      movzx r14d, byte ptr [rsp + 0xb8]
0032402A  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0032402F  0F B7 AC 24 C0 00 00 00         movzx ebp, word ptr [rsp + 0xc0]
00324037  E9 43 FE FF FF                  jmp 0x140323e7f
0032403C  E8 6F 05 00 00                  call 0x1403245b0
00324041  EB DE                           jmp 0x140324021
00324043  0F B6 4F 26                     movzx ecx, byte ptr [rdi + 0x26]
00324047  C1 E2 0C                        shl edx, 0xc
0032404A  D3 E2                           shl edx, cl
0032404C  48 8B CB                        mov rcx, rbx
0032404F  8B C2                           mov eax, edx
00324051  99                              cdq
00324052  81 E2 FF 0F 00 00               and edx, 0xfff
00324058  03 C2                           add eax, edx
0032405A  48 8B D7                        mov rdx, rdi
0032405D  C1 F8 0C                        sar eax, 0xc
00324060  4C 63 C0                        movsxd r8, eax
00324063  E8 30 3E 17 00                  call 0x140497e98
00324068  E9 08 FE FF FF                  jmp 0x140323e75
0032406D  FF C2                           inc edx
0032406F  41 83 FC FF                     cmp r12d, -1
00324073  0F 85 E7 FD FF FF               jne 0x140323e60
00324079  4D 8B E2                        mov r12, r10
0032407C  49 D1 FC                        sar r12, 1
0032407F  E9 DC FD FF FF                  jmp 0x140323e60
00324084  0F B6 4F 26                     movzx ecx, byte ptr [rdi + 0x26]
00324088  4C 8D 05 61 03 00 00            lea r8, [rip + 0x361]
0032408F  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00324093  45 8B FC                        mov r15d, r12d
00324096  48 33 05 63 42 B0 00            xor rax, qword ptr [rip + 0xb04263]
0032409D  45 8B F5                        mov r14d, r13d
003240A0  41 C1 E7 0C                     shl r15d, 0xc
003240A4  48 33 C3                        xor rax, rbx
003240A7  41 D3 E7                        shl r15d, cl
003240AA  41 C1 E6 0C                     shl r14d, 0xc
003240AE  41 D3 E6                        shl r14d, cl
003240B1  48 8B 0B                        mov rcx, qword ptr [rbx]
003240B4  41 8B D7                        mov edx, r15d
003240B7  48 03 D7                        add rdx, rdi
003240BA  49 3B C0                        cmp rax, r8
003240BD  45 8B C6                        mov r8d, r14d
003240C0  0F 85 45 01 00 00               jne 0x14032420b
003240C6  E8 25 03 00 00                  call 0x1403243f0
003240CB  45 8B CE                        mov r9d, r14d
003240CE  45 8B C7                        mov r8d, r15d
003240D1  48 8B D7                        mov rdx, rdi
003240D4  48 8B CB                        mov rcx, rbx
003240D7  E8 F4 03 00 00                  call 0x1403244d0
003240DC  83 BC 24 C8 00 00 00 00         cmp dword ptr [rsp + 0xc8], 0
003240E4  0F 84 2B 01 00 00               je 0x140324215
003240EA  44 8B B4 24 C8 00 00 00         mov r14d, dword ptr [rsp + 0xc8]
003240F2  45 03 E5                        add r12d, r13d
003240F5  E9 FE FE FF FF                  jmp 0x140323ff8
003240FA  45 84 F6                        test r14b, r14b
003240FD  0F 85 7A FC FF FF               jne 0x140323d7d
00324103  0F B6 47 18                     movzx eax, byte ptr [rdi + 0x18]
00324107  83 E8 08                        sub eax, 8
0032410A  3B D0                           cmp edx, eax
0032410C  0F 86 6B FC FF FF               jbe 0x140323d7d
00324112  48 8B D7                        mov rdx, rdi
00324115  44 89 54 24 20                  mov dword ptr [rsp + 0x20], r10d
0032411A  48 8B CB                        mov rcx, rbx
0032411D  E8 D2 51 15 00                  call 0x1404792f4
00324122  E9 C2 FD FF FF                  jmp 0x140323ee9
00324127  41 8B C0                        mov eax, r8d
0032412A  4C 8B CF                        mov r9, rdi
0032412D  4C 8B C6                        mov r8, rsi
00324130  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
00324139  48 8B D3                        mov rdx, rbx
0032413C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00324141  B9 17 00 00 00                  mov ecx, 0x17
00324146  E8 71 76 03 00                  call 0x14035b7bc
0032414B  CD 2C                           int 0x2c
0032414D  E9 83 FC FF FF                  jmp 0x140323dd5
00324152  41 80 7D 00 01                  cmp byte ptr [r13], 1
00324157  0F 85 20 FC FF FF               jne 0x140323d7d
0032415D  0F B6 57 25                     movzx edx, byte ptr [rdi + 0x25]
00324161  03 D1                           add edx, ecx
00324163  48 8D 4F 40                     lea rcx, [rdi + 0x40]
00324167  E8 AC 42 FC FF                  call 0x1402e8418
0032416C  80 7F 25 00                     cmp byte ptr [rdi + 0x25], 0
00324170  C6 47 24 00                     mov byte ptr [rdi + 0x24], 0
00324174  0F 86 6F FD FF FF               jbe 0x140323ee9
0032417A  0F B7 4F 26                     movzx ecx, word ptr [rdi + 0x26]
0032417E  44 8B CD                        mov r9d, ebp
00324181  44 0F B7 47 2C                  movzx r8d, word ptr [rdi + 0x2c]
00324186  8B C1                           mov eax, ecx
00324188  C1 E8 08                        shr eax, 8
0032418B  C1 E0 0C                        shl eax, 0xc
0032418E  D3 E0                           shl eax, cl
00324190  48 8D 4F 40                     lea rcx, [rdi + 0x40]
00324194  49 C1 E0 06                     shl r8, 6
00324198  4C 03 C3                        add r8, rbx
0032419B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0032419F  E8 E8 05 16 00                  call 0x14048478c
003241A4  E9 40 FD FF FF                  jmp 0x140323ee9
003241A9  44 0F B6 B4 24 B8 00 00 00      movzx r14d, byte ptr [rsp + 0xb8]
003241B2  E9 EB FD FF FF                  jmp 0x140323fa2
003241B7  49 8B 48 40                     mov rcx, qword ptr [r8 + 0x40]
003241BB  48 8B C2                        mov rax, rdx
003241BE  48 23 C1                        and rax, rcx
003241C1  48 F7 D2                        not rdx
003241C4  49 89 40 40                     mov qword ptr [r8 + 0x40], rax
003241C8  48 23 D1                        and rdx, rcx
003241CB  E9 F3 FC FF FF                  jmp 0x140323ec3
003241D0  48 8B 13                        mov rdx, qword ptr [rbx]
003241D3  4C 8B C6                        mov r8, rsi
003241D6  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
003241DF  B9 11 00 00 00                  mov ecx, 0x11
003241E4  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003241E9  4C 8B CF                        mov r9, rdi
003241EC  E8 CB 75 03 00                  call 0x14035b7bc
003241F1  CD 2C                           int 0x2c
003241F3  E9 D4 FC FF FF                  jmp 0x140323ecc
003241F8  45 85 F6                        test r14d, r14d
003241FB  0F 85 F1 FE FF FF               jne 0x1403240f2
00324201  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
00324206  E9 FC FD FF FF                  jmp 0x140324007
0032420B  E8 C0 68 39 00                  call 0x1406baad0
00324210  E9 B6 FE FF FF                  jmp 0x1403240cb
00324215  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0032421A  E9 EC FD FF FF                  jmp 0x14032400b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpLfhSubsegmentDelayFreeListProcess(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_pB8;
    unsigned __int16 v_stack_pC0;
    unsigned int v_stack_pC8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (112);
    v_r14 = (unsigned __int8)((*(unsigned __int8 *)(a2 + 51)) & (1));
    v_r15 = (a2) >> (12);
    v_r12 = (a3) >> (16);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) ^ (*(unsigned int *)(v_rip + 11552236)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(a2 + 40)));
    a4 = ((unsigned int)((unsigned int)(result))) >> (16);
    a4 = (a4) + (a2);
    result = (unsigned int)((*(unsigned __int16 *)(a2 + 32)) + ((unsigned int)((unsigned __int16)(v_r12))));
    v_stack_p10 = (unsigned __int8)(v_r14);
    v_stack_m50 = v_r15;
    v_stack_m70 = (unsigned int)((unsigned __int16)(result));
    v_stack_m58 = a4;
    v_stack_m48 = v_r12;
    v_stack_m60 = a2 + 39;
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 34))) == ((unsigned int)(result))) goto loc_00324152;
    v_stack_m60 = a2 + 39;
    if ((*(unsigned __int8 *)(a2 + 39)) == 1) goto loc_003240FA;
loc_00323D7D:
    if ((unsigned __int16)(v_stack_p18) == 0) goto loc_00323EE9;
loc_00323D90:
    a3 = (unsigned int)(((unsigned __int16)(v_stack_p18)) - 1);
    result = (*(unsigned __int64 *)(a1 + 80)) >> (32);
    v_stack_m74 = (unsigned int)(a3);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a3))) * ((unsigned int)((unsigned __int16)(result))));
    v_rsi = (v_rsi) + (a4);
    v_stack_m68 = v_rsi;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 80)))) ^ (*(unsigned int *)(v_rsi)));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
    v_stack_p18 = (unsigned __int16)(*(unsigned __int16 *)(v_rsi));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(v_rsi)));
    if ((*(unsigned int *)(v_rsi + 8)) != ((unsigned int)(a2))) goto loc_00324127;
loc_00323DD5:
    if ((unsigned __int8)(v_r14) != 0) goto loc_00323E7F;
    if ((*(unsigned __int8 *)(a2 + 39)) <= 1) goto loc_00323E7F;
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - ((unsigned int)(a2)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) >> (12));
    a3 = (unsigned int)((a3) >> ((unsigned __int8)(*(unsigned __int8 *)(a2 + 38))));
    a4 = (a2 + *(unsigned __int8 *)(a2 + 24) * 8) + (a3 + a3 * 1);
    a2 = (unsigned int)((*(unsigned __int16 *)(a2 + 40)) ^ ((unsigned int)((unsigned __int16)(v_r15))));
    result = (unsigned int)((*(unsigned __int16 *)(v_rip + 11551969)) ^ ((unsigned int)(a2)));
    a2 = 0;
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) + ((unsigned int)(v_r11)));
    result = (unsigned int)((result) >> (12));
    result = (unsigned int)((result) >> ((unsigned __int8)(*(unsigned __int8 *)(a2 + 38))));
    result = (unsigned int)((result) - ((unsigned int)(a3)));
    result = (unsigned int)((result) + 1);
    if (a4 >= (a4 + result * 2)) goto loc_00323E7F;
loc_00323E43:
    result = (unsigned __int16)(((unsigned int)(0xFFFFFFFFULL)) - (1));
    if (condition_is_equal) goto loc_0032406D;
    if (((unsigned __int16)(result)) == -1) {
        a2 = (unsigned int)((a2) - 1);
    }
    a4 = (a4) + (2);
    v_r10 = (a3 + a3 * 1) + (2);
    if (a4 < (a4 + result * 2)) goto loc_00323E43;
    if ((unsigned int)(a2) != 0) goto loc_00324043;
loc_00323E75:
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) != -1) goto loc_00323F07;
loc_00323E7F:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))) & (63));
    result = ((unsigned int)(v_stack_m74)) >> (6);
    if ((unsigned __int8)(v_r14) != 0) goto loc_003241B7;
loc_00323EAF:
    a1 = (*(unsigned __int64 *)(a2 + result * 8 + 64)) & (-2);
    if (condition_is_not_equal) goto loc_00323EAF;
    a2 = ~(-2);
    a2 = (a2) & (*(unsigned __int64 *)(a2 + result * 8 + 64));
loc_00323EC3:
    if (a2 == 0) goto loc_003241D0;
loc_00323ECC:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) != 0) goto loc_00323D90;
loc_00323EE9:
    v_rsp = (v_rsp) + (112);
    return *(unsigned __int64 *)(a2 + result * 8 + 64);
loc_00323F07:
    v_rsi = 0;
    v_stack_p30 = 0;
    if (sign_flag) goto loc_00323F91;
    v_stack_pC8 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8) + 13)) & (8)) != 0) goto loc_00323FA2;
    v_r15 = (*(unsigned __int64 *)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8) + 22)) + *(unsigned __int64 *)(v_stack_p8) * 1 + 24)) + (*(unsigned __int64 *)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8) + 22)) + *(unsigned __int64 *)(v_stack_p8) * 1 + 16));
    result = (*(unsigned __int64 *)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8) + 22)) + *(unsigned __int64 *)(v_stack_p8) * 1 + 8)) >> ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8) + 11)));
    if (result <= 8) { result = 8; }
    v_r14 = (*(unsigned __int64 *)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8) + 22)) + *(unsigned __int64 *)(v_stack_p8) * 1 + 8)) >> ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8) + 12)));
    if (v_r14 <= 8) { v_r14 = 8; }
    if (v_r15 <= result) goto loc_00324021;
    result = RtlpHpEnvCompactionSchedule(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8) + 56), *(unsigned __int64 *)(v_stack_p8), 8, v_stack_m58);
    if (sign_flag) goto loc_003241A9;
    if (v_r15 <= v_r14) goto loc_0032402A;
    goto loc_00323FA2;
loc_00323F91:
    v_stack_pC8 = 1;
loc_00323FA2:
    if (1 >= ((unsigned int)(*(unsigned __int8 *)(a2 + 39)))) goto loc_0032402A;
loc_00323FB4:
    result = RtlpHpLfhSubsegmentFindEmptyUnits(a2, 1, v_stack_p30, v_stack_m58);
    if (((unsigned int)(result)) == -1) goto loc_00324007;
    if (((unsigned int)((unsigned int)(v_stack_p30))) < 2) goto loc_003241F8;
    if (0 != 0) goto loc_00324084;
    result = RtlpHpAcquireLockExclusive(a2 + 56, *(unsigned __int8 *)(v_stack_p8 + 65), v_stack_p30, v_stack_m58);
loc_00323FF8:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < ((unsigned int)(*(unsigned __int8 *)(v_stack_p48)))) goto loc_00323FB4;
loc_00324007:
    if (2 == 0) goto loc_00324021;
loc_0032400B:
    if (2 != 2) goto loc_0032403C;
    result = RtlpHpReleaseLockExclusive(a2 + 56, *(unsigned __int8 *)(v_stack_p8 + 65), (unsigned __int8)((unsigned __int8)(result)), v_stack_m58);
loc_00324021:
loc_0032402A:
    goto loc_00323E7F;
loc_0032403C:
    result = RtlpHpReleaseLockShared(a2 + 56, *(unsigned __int8 *)(v_stack_p8 + 65), (unsigned __int8)((unsigned __int8)(result)), v_stack_m58);
    goto loc_00324021;
loc_00324043:
    a2 = (unsigned int)((*(unsigned __int8 *)(v_stack_p8 + 65)) << (12));
    a2 = (unsigned int)((a2) << ((unsigned __int8)(*(unsigned __int8 *)(a2 + 38))));
    a2 = (unsigned int)((a2) & (0xFFFULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) + ((unsigned int)(a2)));
    result = (unsigned int)((result) >> (12));
    result = RtlpHpLfhContextUpdateFreeCommitCount(v_stack_p8, a2, (int)((unsigned int)(result)), v_stack_m58);
    goto loc_00323E75;
loc_0032406D:
    a2 = (unsigned int)((a2) + 1);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != -1) goto loc_00323E60;
    v_r12 = ((unsigned int)(v_stack_m70)) >> (1);
    goto loc_00323E60;
loc_00324084:
    result = (*(unsigned __int64 *)(v_stack_p8 + 32)) ^ (*(unsigned __int64 *)(v_rip + 11551331));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) << (12));
    result = (result) ^ (v_stack_p8);
    v_r15 = (unsigned int)((v_r15) << ((unsigned __int8)(*(unsigned __int8 *)(a2 + 38))));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p48))) << (12));
    v_r14 = (unsigned int)((v_r14) << ((unsigned __int8)(*(unsigned __int8 *)(a2 + 38))));
    a2 = ((unsigned int)((unsigned int)(v_r15))) + (a2);
    if (result != (v_rip + 865)) goto loc_0032420B;
    result = RtlpHpSegLfhVsDecommit(*(unsigned __int64 *)(v_stack_p8), a2, (unsigned int)((unsigned int)(v_r14)), v_stack_m58);
loc_003240CB:
    result = RtlpHpLfhSubsegmentDecBlockCounts(v_stack_p8, a2, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_r14)));
    if (v_stack_pC8 == 0) goto loc_00324215;
loc_003240F2:
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(v_stack_p48)));
    goto loc_00323FF8;
loc_003240FA:
    if ((unsigned __int8)((unsigned int)(v_stack_pC8)) != 0) goto loc_00323D7D;
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 24)) - (8));
    if (((unsigned int)(a2)) <= ((unsigned int)(result))) goto loc_00323D7D;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m70));
    result = RtlpHpLfhSubsegmentDelayFreeListBatch(v_stack_p8, a2, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_r14)));
    goto loc_00323EE9;
loc_00324127:
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15))));
    result = RtlpLogHeapFailure(23, v_stack_p8, v_stack_p40, a2);
    goto loc_00323DD5;
loc_00324152:
    if ((*(unsigned __int8 *)(v_stack_p48)) != 1) goto loc_00323D7D;
    a2 = (unsigned int)((*(unsigned __int8 *)(a2 + 37)) + (23));
    result = RtlpHpLfhBlockBitmapInitialize(a2 + 64, a2, v_stack_p40, a2);
    *(unsigned __int8 *)(a2 + 36) = 0;
    if ((*(unsigned __int8 *)(a2 + 37)) <= 0) goto loc_00323EE9;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a2 + 38)))) >> (8));
    result = (unsigned int)((result) << (12));
    result = (unsigned int)((result) << ((unsigned __int8)(*(unsigned __int16 *)(a2 + 38))));
    a3 = (*(unsigned __int16 *)(a2 + 44)) << (6);
    a3 = (a3) + (v_stack_p8);
    v_stack_p20 = (unsigned int)(result);
    result = RtlpHpLfhSubsegmentSetWitheldBlocks(a2 + 64, a2, a3, (unsigned int)((unsigned int)(v_stack_pC0)));
    goto loc_00323EE9;
loc_003241A9:
    goto loc_00323FA2;
loc_003241B7:
    result = (a2) & (*(unsigned __int64 *)(a3 + 64));
    a2 = ~(a2);
    *(unsigned __int64 *)(a3 + 64) = result;
    a2 = (a2) & (*(unsigned __int64 *)(a3 + 64));
    goto loc_00323EC3;
loc_003241D0:
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_pC0));
    result = RtlpLogHeapFailure(17, *(unsigned __int64 *)(v_stack_p8), v_stack_p40, a2);
    goto loc_00323ECC;
loc_003241F8:
    if ((unsigned int)(v_stack_pB8) != 0) goto loc_003240F2;
    goto loc_00324007;
loc_0032420B:
    result = guard_dispatch_icall(17, *(unsigned __int64 *)(v_stack_p8), v_stack_p40, a2);
    goto loc_003240CB;
loc_00324215:
    goto loc_0032400B;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpLfhSubsegmentDelayFreeListProcess(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;
    uint8_t v_stack_pB8;
    uint16_t v_stack_pC0;
    uint32_t v_stack_pC8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (112);
    local_r14 = (uint8_t)((*(uint8_t *)(arg2 + 0x33)) & (1));
    local_r15 = (Arg2) >> (12);
    local_r12 = (Arg3) >> (16);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) ^ (*(uint32_t *)(v_rip + 0xB045EC)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(arg2 + 0x28)));
    a4 = ((uint32_t)((uint32_t)(result))) >> (16);
    a4 = (a4) + (Arg2);
    result = (uint32_t)((*(uint16_t *)(arg2 + 0x20)) + ((uint32_t)((uint16_t)(local_r12))));
    v_stack_p10 = (uint8_t)(local_r14);
    v_stack_m50 = local_r15;
    v_stack_m70 = (uint32_t)((uint16_t)(result));
    v_stack_m58 = a4;
    v_stack_m48 = local_r12;
    v_stack_m60 = Arg2 + 39;
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x22))) == ((uint32_t)(result))) goto loc_00324152;
    v_stack_m60 = Arg2 + 39;
    if ((*(uint8_t *)(arg2 + 0x27)) == 1) goto loc_003240FA;
loc_00323D7D:
    if ((uint16_t)(v_stack_p18) == 0) goto loc_00323EE9;
loc_00323D90:
    Arg3 = (uint32_t)(((uint16_t)(v_stack_p18)) - 1);
    result = (*(uint64_t *)(arg1 + 0x50)) >> (32);
    v_stack_m74 = (uint32_t)(Arg3);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) * ((uint32_t)((uint16_t)(result))));
    local_rsi = (local_rsi) + (a4);
    v_stack_m68 = local_rsi;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x50)))) ^ (*(uint32_t *)(local_rsi)));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
    v_stack_p18 = (uint16_t)(*(uint16_t *)(local_rsi));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(local_rsi)));
    if ((*(uint32_t *)(local_rsi + 0x8)) != ((uint32_t)(Arg2))) goto loc_00324127;
loc_00323DD5:
    if ((uint8_t)(local_r14) != 0) goto loc_00323E7F;
    if ((*(uint8_t *)(arg2 + 0x27)) <= 1) goto loc_00323E7F;
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) >> (12));
    Arg3 = (uint32_t)((Arg3) >> ((uint8_t)(*(uint8_t *)(arg2 + 0x26))));
    a4 = (Arg2 + *(uint8_t *)(arg2 + 0x18) * 8) + (Arg3 + Arg3 * 1);
    Arg2 = (uint32_t)((*(uint16_t *)(arg2 + 0x28)) ^ ((uint32_t)((uint16_t)(local_r15))));
    result = (uint32_t)((*(uint16_t *)(v_rip + 0xB044E1)) ^ ((uint32_t)(Arg2)));
    Arg2 = 0;
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) + ((uint32_t)(local_r11)));
    result = (uint32_t)((result) >> (12));
    result = (uint32_t)((result) >> ((uint8_t)(*(uint8_t *)(arg2 + 0x26))));
    result = (uint32_t)((result) - ((uint32_t)(Arg3)));
    result = (uint32_t)((result) + 1);
    if (a4 >= (a4 + result * 2)) goto loc_00323E7F;
loc_00323E43:
    result = (uint16_t)(((uint32_t)(0xFFFFFFFFULL)) - (1));
    if (condition_is_equal) goto loc_0032406D;
    if (((uint16_t)(result)) == -1) {
        Arg2 = (uint32_t)((Arg2) - 1);
    }
    a4 = (a4) + (2);
    local_r10 = (Arg3 + Arg3 * 1) + (2);
    if (a4 < (a4 + result * 2)) goto loc_00323E43;
    if ((uint32_t)(Arg2) != 0) goto loc_00324043;
loc_00323E75:
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) != -1) goto loc_00323F07;
loc_00323E7F:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))) & (63));
    result = ((uint32_t)(v_stack_m74)) >> (6);
    if ((uint8_t)(local_r14) != 0) goto loc_003241B7;
loc_00323EAF:
    Arg1 = (*(uint64_t *)(arg2 + result * 8 + 0x40)) & (-2);
    if (condition_is_not_equal) goto loc_00323EAF;
    Arg2 = ~(-2);
    Arg2 = (Arg2) & (*(uint64_t *)(arg2 + result * 8 + 0x40));
loc_00323EC3:
    if (Arg2 == NULL) goto loc_003241D0;
loc_00323ECC:
    if ((uint16_t)(*(uint16_t *)(local_rsi)) != 0) goto loc_00323D90;
loc_00323EE9:
    local_rsp = (local_rsp) + (112);
    return *(uint64_t *)(arg2 + result * 8 + 0x40);
loc_00323F07:
    local_rsi = 0;
    v_stack_p30 = 0;
    if (sign_flag) goto loc_00323F91;
    v_stack_pC8 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p8) + 0xD)) & (8)) != 0) goto loc_00323FA2;
    local_r15 = (*(uint64_t *)((int16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8) + 0x16)) + *(uint64_t *)(v_stack_p8) * 1 + 0x18)) + (*(uint64_t *)((int16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8) + 0x16)) + *(uint64_t *)(v_stack_p8) * 1 + 0x10));
    result = (*(uint64_t *)((int16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8) + 0x16)) + *(uint64_t *)(v_stack_p8) * 1 + 0x8)) >> ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p8) + 0xB)));
    if (result <= 8) { result = 8; }
    local_r14 = (*(uint64_t *)((int16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8) + 0x16)) + *(uint64_t *)(v_stack_p8) * 1 + 0x8)) >> ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p8) + 0xC)));
    if (local_r14 <= 8) { local_r14 = 8; }
    if (local_r15 <= result) goto loc_00324021;
    result = RtlpHpEnvCompactionSchedule(*(uint64_t *)(*(uint64_t *)(v_stack_p8) + 0x38), *(uint64_t *)(v_stack_p8), 8, v_stack_m58);
    if (sign_flag) goto loc_003241A9;
    if (local_r15 <= local_r14) goto loc_0032402A;
    goto loc_00323FA2;
loc_00323F91:
    v_stack_pC8 = 1;
loc_00323FA2:
    if (1 >= ((uint32_t)(*(uint8_t *)(arg2 + 0x27)))) goto loc_0032402A;
loc_00323FB4:
    result = RtlpHpLfhSubsegmentFindEmptyUnits(Arg2, 1, v_stack_p30, v_stack_m58);
    if (((uint32_t)(result)) == -1) goto loc_00324007;
    if (((uint32_t)((uint32_t)(v_stack_p30))) < 2) goto loc_003241F8;
    if (0 != 0) goto loc_00324084;
    result = RtlpHpAcquireLockExclusive(Arg2 + 56, *(uint8_t *)(v_stack_p8 + 0x41), v_stack_p30, v_stack_m58);
loc_00323FF8:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < ((uint32_t)(*(uint8_t *)(v_stack_p48)))) goto loc_00323FB4;
loc_00324007:
    if (2 == 0) goto loc_00324021;
loc_0032400B:
    if (2 != 2) goto loc_0032403C;
    result = RtlpHpReleaseLockExclusive(Arg2 + 56, *(uint8_t *)(v_stack_p8 + 0x41), (uint8_t)((uint8_t)(result)), v_stack_m58);
loc_00324021:
loc_0032402A:
    goto loc_00323E7F;
loc_0032403C:
    result = RtlpHpReleaseLockShared(Arg2 + 56, *(uint8_t *)(v_stack_p8 + 0x41), (uint8_t)((uint8_t)(result)), v_stack_m58);
    goto loc_00324021;
loc_00324043:
    Arg2 = (uint32_t)((*(uint8_t *)(v_stack_p8 + 0x41)) << (12));
    Arg2 = (uint32_t)((Arg2) << ((uint8_t)(*(uint8_t *)(arg2 + 0x26))));
    Arg2 = (uint32_t)((Arg2) & (0xFFFULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)(Arg2)));
    result = (uint32_t)((result) >> (12));
    result = RtlpHpLfhContextUpdateFreeCommitCount(v_stack_p8, Arg2, (int32_t)((uint32_t)(result)), v_stack_m58);
    goto loc_00323E75;
loc_0032406D:
    Arg2 = (uint32_t)((Arg2) + 1);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != -1) goto loc_00323E60;
    local_r12 = ((uint32_t)(v_stack_m70)) >> (1);
    goto loc_00323E60;
loc_00324084:
    result = (*(uint64_t *)(v_stack_p8 + 0x20)) ^ (*(uint64_t *)(v_rip + 0xB04263));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) << (12));
    result = (result) ^ (v_stack_p8);
    local_r15 = (uint32_t)((local_r15) << ((uint8_t)(*(uint8_t *)(arg2 + 0x26))));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p48))) << (12));
    local_r14 = (uint32_t)((local_r14) << ((uint8_t)(*(uint8_t *)(arg2 + 0x26))));
    Arg2 = ((uint32_t)((uint32_t)(local_r15))) + (Arg2);
    if (result != (v_rip + 865)) goto loc_0032420B;
    result = RtlpHpSegLfhVsDecommit(*(uint64_t *)(v_stack_p8), Arg2, (uint32_t)((uint32_t)(local_r14)), v_stack_m58);
loc_003240CB:
    result = RtlpHpLfhSubsegmentDecBlockCounts(v_stack_p8, Arg2, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_r14)));
    if (v_stack_pC8 == 0) goto loc_00324215;
loc_003240F2:
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(v_stack_p48)));
    goto loc_00323FF8;
loc_003240FA:
    if ((uint8_t)((uint32_t)(v_stack_pC8)) != 0) goto loc_00323D7D;
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x18)) - (8));
    if (((uint32_t)(Arg2)) <= ((uint32_t)(result))) goto loc_00323D7D;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m70));
    result = RtlpHpLfhSubsegmentDelayFreeListBatch(v_stack_p8, Arg2, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_r14)));
    goto loc_00323EE9;
loc_00324127:
    v_stack_p28 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15))));
    result = RtlpLogHeapFailure(23, v_stack_p8, v_stack_p40, Arg2);
    goto loc_00323DD5;
loc_00324152:
    if ((*(uint8_t *)(v_stack_p48)) != 1) goto loc_00323D7D;
    Arg2 = (uint32_t)((*(uint8_t *)(arg2 + 0x25)) + (23));
    result = RtlpHpLfhBlockBitmapInitialize(Arg2 + 64, Arg2, v_stack_p40, Arg2);
    *(uint8_t *)(arg2 + 0x24) = 0;
    if ((*(uint8_t *)(arg2 + 0x25)) <= 0) goto loc_00323EE9;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg2 + 0x26)))) >> (8));
    result = (uint32_t)((result) << (12));
    result = (uint32_t)((result) << ((uint8_t)(*(uint16_t *)(arg2 + 0x26))));
    Arg3 = (*(uint16_t *)(arg2 + 0x2C)) << (6);
    Arg3 = (Arg3) + (v_stack_p8);
    v_stack_p20 = (uint32_t)(result);
    result = RtlpHpLfhSubsegmentSetWitheldBlocks(Arg2 + 64, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_pC0)));
    goto loc_00323EE9;
loc_003241A9:
    goto loc_00323FA2;
loc_003241B7:
    result = (Arg2) & (*(uint64_t *)(Arg3 + 0x40));
    Arg2 = ~(Arg2);
    *(uint64_t *)(Arg3 + 0x40) = result;
    Arg2 = (Arg2) & (*(uint64_t *)(Arg3 + 0x40));
    goto loc_00323EC3;
loc_003241D0:
    v_stack_p28 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_pC0));
    result = RtlpLogHeapFailure(17, *(uint64_t *)(v_stack_p8), v_stack_p40, Arg2);
    goto loc_00323ECC;
loc_003241F8:
    if ((uint32_t)(v_stack_pB8) != 0) goto loc_003240F2;
    goto loc_00324007;
loc_0032420B:
    result = guard_dispatch_icall(17, *(uint64_t *)(v_stack_p8), v_stack_p40, Arg2);
    goto loc_003240CB;
loc_00324215:
    goto loc_0032400B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x41` | `8` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg2` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg2` | `+ 0x18` | `8` | `R` |
| `Arg2` | `+ 0x20` | `16` | `R` |
| `Arg2` | `+ 0x20` | `16` | `R/W` |
| `Arg2` | `+ 0x22` | `16` | `R` |
| `Arg2` | `+ 0x24` | `8` | `W` |
| `Arg2` | `+ 0x25` | `8` | `R` |
| `Arg2` | `+ 0x26` | `8` | `R` |
| `Arg2` | `+ 0x26` | `16` | `R` |
| `Arg2` | `+ 0x27` | `64` | `R` |
| `Arg2` | `+ 0x28` | `16` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x2C` | `16` | `R` |
| `Arg2` | `+ 0x33` | `8` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x40` | `8` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x40` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00323CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
