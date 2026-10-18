# MiManageUltraSpacePageTable

- RVA: `0x002DCAF0`–`0x002DCF9E` (길이 `1,198` bytes)
- VA: `0x00000001402DCAF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000707A8`
- 디코드: `307`개 명령, `1,198/1,198` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x002DCB60` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002DCC26` → [KeFlushTb](../31/KeFlushTb_function_00314140.md) (function, `0x00314140`)
- `0x002DCC48` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002DCD01` → [KiFlushAddressSpaceTb](../30/KiFlushAddressSpaceTb_function_00308F50.md) (function, `0x00308F50`)
- `0x002DCD80` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x002DCE51` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x002DCE69` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x002DCE78` → [KxFlushEntireTb](../30/KxFlushEntireTb_function_00309094.md) (function, `0x00309094`)
- `0x002DCE96` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x002DCED3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002DCEEB` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002DCF03` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002DCF5A` → [MiArePageContentsZero](../4D/MiArePageContentsZero_function_004D4278.md) (function, `0x004D4278`)
- `0x002DCF94` → [MiArePageContentsZero](../4D/MiArePageContentsZero_function_004D4278.md) (function, `0x004D4278`)

### Direct callers
- [MiDeleteUltraMapContext](MiDeleteUltraMapContext_function_002DC9A4.md) at `0x002DCAAD`
- [sub_00322E07](../32/Unknown_function_00322E07.md) at `0x00322E14`
- [sub_00322E07](../32/Unknown_function_00322E07.md) at `0x00322E2B`
- [MiReuseUltraPageTable](../47/MiReuseUltraPageTable_function_00472298.md) at `0x004722D3`

### Static image references
- `0x002DCB04` → RVA `0x00E38E30` (`.data`; read)
- `0x002DCB29` → RVA `0x00E2DBF8` (`.data`; read)
- `0x002DCB71` → RVA `0x00FCF080` (`CACHEALI`; read)
- `0x002DCCCC` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002DCCE8` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x002DCD09` → RVA `0x00E685D4` (`.data`; read)
- `0x002DCE3D` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x002DCE62` → RVA `0x00E38D00` (`.data`; read)
- `0x002DCEB3` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002DCEBC` → RVA `0x00E06D28` (`.data`; read)
- `0x002DCEC6` → RVA `0x00EFA8E0` (`.data`; read)
- `0x002DCF0A` → RVA `0x00FC6A87` (`ALMOSTRO`; read)
- `0x002DCF2A` → RVA `0x00E30270` (`.data`; read)
- `0x002DCF32` → RVA `0x00FC5054` (`ALMOSTRO`; reference)
- `0x002DCF38` → RVA `0x00E30270` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002DCAF0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002DCAF5  55                              push rbp
002DCAF6  56                              push rsi
002DCAF7  57                              push rdi
002DCAF8  41 54                           push r12
002DCAFA  41 55                           push r13
002DCAFC  41 56                           push r14
002DCAFE  41 57                           push r15
002DCB00  48 83 EC 30                     sub rsp, 0x30
002DCB04  48 8B 05 25 C3 B5 00            mov rax, qword ptr [rip + 0xb5c325]
002DCB0B  48 8B F1                        mov rsi, rcx
002DCB0E  C1 EA 09                        shr edx, 9
002DCB11  45 8B E0                        mov r12d, r8d
002DCB14  83 E2 3F                        and edx, 0x3f
002DCB17  8B 40 04                        mov eax, dword ptr [rax + 4]
002DCB1A  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
002DCB21  48 8D 14 52                     lea rdx, [rdx + rdx*2]
002DCB25  48 C1 E2 07                     shl rdx, 7
002DCB29  48 03 15 C8 10 B5 00            add rdx, qword ptr [rip + 0xb510c8]
002DCB30  45 33 ED                        xor r13d, r13d
002DCB33  48 8B 8A 78 01 00 00            mov rcx, qword ptr [rdx + 0x178]
002DCB3A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002DCB3F  48 8D B9 88 02 00 00            lea rdi, [rcx + 0x288]
002DCB46  48 8D 99 08 03 00 00            lea rbx, [rcx + 0x308]
002DCB4D  44 0F 20 C0                     mov rax, cr8
002DCB51  48 81 C1 28 03 00 00            add rcx, 0x328
002DCB58  3C 02                           cmp al, 2
002DCB5A  0F 84 E3 00 00 00               je 0x1402dcc43
002DCB60  E8 2B BB F6 FF                  call 0x140248690
002DCB65  88 44 24 78                     mov byte ptr [rsp + 0x78], al
002DCB69  45 33 D2                        xor r10d, r10d
002DCB6C  F0 44 09 14 24                  lock or dword ptr [rsp], r10d
002DCB71  44 8B 3D 08 25 CF 00            mov r15d, dword ptr [rip + 0xcf2508]
002DCB78  45 8D 42 08                     lea r8d, [r10 + 8]
002DCB7C  45 8B F7                        mov r14d, r15d
002DCB7F  41 8B EA                        mov ebp, r10d
002DCB82  41 83 E6 03                     and r14d, 3
002DCB86  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
002DCB8A  48 85 D2                        test rdx, rdx
002DCB8D  75 5D                           jne 0x1402dcbec
002DCB8F  FF C5                           inc ebp
002DCB91  48 83 C7 20                     add rdi, 0x20
002DCB95  83 FD 04                        cmp ebp, 4
002DCB98  72 EC                           jb 0x1402dcb86
002DCB9A  45 85 E4                        test r12d, r12d
002DCB9D  74 22                           je 0x1402dcbc1
002DCB9F  41 F6 C4 02                     test r12b, 2
002DCBA3  74 26                           je 0x1402dcbcb
002DCBA5  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
002DCBAA  48 8B C3                        mov rax, rbx
002DCBAD  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002DCBB1  48 39 01                        cmp qword ptr [rcx], rax
002DCBB4  0F 84 63 01 00 00               je 0x1402dcd1d
002DCBBA  B9 03 00 00 00                  mov ecx, 3
002DCBBF  CD 29                           int 0x29
002DCBC1  4C 39 53 10                     cmp qword ptr [rbx + 0x10], r10
002DCBC5  0F 84 01 01 00 00               je 0x1402dcccc
002DCBCB  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
002DCBD0  41 8B C6                        mov eax, r14d
002DCBD3  48 C1 E0 05                     shl rax, 5
002DCBD7  48 05 88 02 00 00               add rax, 0x288
002DCBDD  49 03 C1                        add rax, r9
002DCBE0  4C 39 50 10                     cmp qword ptr [rax + 0x10], r10
002DCBE4  75 C7                           jne 0x1402dcbad
002DCBE6  44 89 78 18                     mov dword ptr [rax + 0x18], r15d
002DCBEA  EB C1                           jmp 0x1402dcbad
002DCBEC  8B 4F 18                        mov ecx, dword ptr [rdi + 0x18]
002DCBEF  41 8B C7                        mov eax, r15d
002DCBF2  2B C1                           sub eax, ecx
002DCBF4  83 F8 02                        cmp eax, 2
002DCBF7  77 59                           ja 0x1402dcc52
002DCBF9  F6 C1 01                        test cl, 1
002DCBFC  75 05                           jne 0x1402dcc03
002DCBFE  83 F8 02                        cmp eax, 2
002DCC01  73 4F                           jae 0x1402dcc52
002DCC03  44 39 94 24 88 00 00 00         cmp dword ptr [rsp + 0x88], r10d
002DCC0B  74 82                           je 0x1402dcb8f
002DCC0D  45 85 ED                        test r13d, r13d
002DCC10  0F 85 79 FF FF FF               jne 0x1402dcb8f
002DCC16  49 3B D0                        cmp rdx, r8
002DCC19  0F 82 70 FF FF FF               jb 0x1402dcb8f
002DCC1F  41 8D 55 01                     lea edx, [r13 + 1]
002DCC23  8D 4A 01                        lea ecx, [rdx + 1]
002DCC26  E8 15 75 03 00                  call 0x140314140
002DCC2B  41 BD 01 00 00 00               mov r13d, 1
002DCC31  FF CD                           dec ebp
002DCC33  48 83 EF 20                     sub rdi, 0x20
002DCC37  45 33 D2                        xor r10d, r10d
002DCC3A  45 8D 45 07                     lea r8d, [r13 + 7]
002DCC3E  E9 4C FF FF FF                  jmp 0x1402dcb8f
002DCC43  C6 44 24 78 11                  mov byte ptr [rsp + 0x78], 0x11
002DCC48  E8 33 C2 F6 FF                  call 0x140248e80
002DCC4D  E9 17 FF FF FF                  jmp 0x1402dcb69
002DCC52  48 8B 0F                        mov rcx, qword ptr [rdi]
002DCC55  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
002DCC59  48 89 41 08                     mov qword ptr [rcx + 8], rax
002DCC5D  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
002DCC61  48 8B 07                        mov rax, qword ptr [rdi]
002DCC64  48 89 01                        mov qword ptr [rcx], rax
002DCC67  48 8B 03                        mov rax, qword ptr [rbx]
002DCC6A  48 8B 0F                        mov rcx, qword ptr [rdi]
002DCC6D  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
002DCC71  48 39 58 08                     cmp qword ptr [rax + 8], rbx
002DCC75  0F 85 3F FF FF FF               jne 0x1402dcbba
002DCC7B  48 39 1A                        cmp qword ptr [rdx], rbx
002DCC7E  0F 85 36 FF FF FF               jne 0x1402dcbba
002DCC84  48 8B 01                        mov rax, qword ptr [rcx]
002DCC87  48 39 48 08                     cmp qword ptr [rax + 8], rcx
002DCC8B  0F 85 29 FF FF FF               jne 0x1402dcbba
002DCC91  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002DCC95  48 39 08                        cmp qword ptr [rax], rcx
002DCC98  0F 85 1C FF FF FF               jne 0x1402dcbba
002DCC9E  48 89 0A                        mov qword ptr [rdx], rcx
002DCCA1  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002DCCA5  48 89 43 08                     mov qword ptr [rbx + 8], rax
002DCCA9  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002DCCAD  48 89 18                        mov qword ptr [rax], rbx
002DCCB0  48 89 51 08                     mov qword ptr [rcx + 8], rdx
002DCCB4  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
002DCCB8  48 01 43 10                     add qword ptr [rbx + 0x10], rax
002DCCBC  48 89 7F 08                     mov qword ptr [rdi + 8], rdi
002DCCC0  48 89 3F                        mov qword ptr [rdi], rdi
002DCCC3  4C 89 57 10                     mov qword ptr [rdi + 0x10], r10
002DCCC7  E9 C3 FE FF FF                  jmp 0x1402dcb8f
002DCCCC  8B 05 E6 9D CE 00               mov eax, dword ptr [rip + 0xce9de6]
002DCCD2  A8 04                           test al, 4
002DCCD4  0F 84 99 01 00 00               je 0x1402dce73
002DCCDA  A8 02                           test al, 2
002DCCDC  75 19                           jne 0x1402dccf7
002DCCDE  0F BA E0 17                     bt eax, 0x17
002DCCE2  0F 82 22 02 00 00               jb 0x1402dcf0a
002DCCE8  8B 05 92 9D CE 00               mov eax, dword ptr [rip + 0xce9d92]
002DCCEE  83 F8 01                        cmp eax, 1
002DCCF1  0F 84 7C 01 00 00               je 0x1402dce73
002DCCF7  41 B1 01                        mov r9b, 1
002DCCFA  33 D2                           xor edx, edx
002DCCFC  45 8A C1                        mov r8b, r9b
002DCCFF  33 C9                           xor ecx, ecx
002DCD01  E8 4A C2 02 00                  call 0x140308f50
002DCD06  45 33 D2                        xor r10d, r10d
002DCD09  44 39 15 C4 B8 B8 00            cmp dword ptr [rip + 0xb8b8c4], r10d
002DCD10  0F 85 90 01 00 00               jne 0x1402dcea6
002DCD16  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
002DCD1B  EB 45                           jmp 0x1402dcd62
002DCD1D  48 89 06                        mov qword ptr [rsi], rax
002DCD20  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
002DCD24  48 89 31                        mov qword ptr [rcx], rsi
002DCD27  48 89 70 08                     mov qword ptr [rax + 8], rsi
002DCD2B  49 8B F2                        mov rsi, r10
002DCD2E  48 FF 40 10                     inc qword ptr [rax + 0x10]
002DCD32  45 85 E4                        test r12d, r12d
002DCD35  75 2B                           jne 0x1402dcd62
002DCD37  4C 39 53 10                     cmp qword ptr [rbx + 0x10], r10
002DCD3B  74 25                           je 0x1402dcd62
002DCD3D  48 8B 33                        mov rsi, qword ptr [rbx]
002DCD40  48 8B 06                        mov rax, qword ptr [rsi]
002DCD43  48 39 5E 08                     cmp qword ptr [rsi + 8], rbx
002DCD47  0F 85 6D FE FF FF               jne 0x1402dcbba
002DCD4D  48 39 70 08                     cmp qword ptr [rax + 8], rsi
002DCD51  0F 85 63 FE FF FF               jne 0x1402dcbba
002DCD57  48 89 03                        mov qword ptr [rbx], rax
002DCD5A  48 89 58 08                     mov qword ptr [rax + 8], rbx
002DCD5E  48 FF 4B 10                     dec qword ptr [rbx + 0x10]
002DCD62  B9 00 01 00 00                  mov ecx, 0x100
002DCD67  48 39 4B 10                     cmp qword ptr [rbx + 0x10], rcx
002DCD6B  77 67                           ja 0x1402dcdd4
002DCD6D  49 8B EA                        mov rbp, r10
002DCD70  49 8B FA                        mov rdi, r10
002DCD73  8A 5C 24 78                     mov bl, byte ptr [rsp + 0x78]
002DCD77  49 8D 89 28 03 00 00            lea rcx, [r9 + 0x328]
002DCD7E  8A D3                           mov dl, bl
002DCD80  E8 3B B5 F6 FF                  call 0x1402482c0
002DCD85  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
002DCD8F  49 BC AB AA AA AA AA AA AA AA   movabs r12, 0xaaaaaaaaaaaaaaab
002DCD99  48 85 FF                        test rdi, rdi
002DCD9C  0F 85 8E 00 00 00               jne 0x1402dce30
002DCDA2  48 85 F6                        test rsi, rsi
002DCDA5  74 27                           je 0x1402dcdce
002DCDA7  49 8B C7                        mov rax, r15
002DCDAA  48 2B F0                        sub rsi, rax
002DCDAD  48 C1 FE 04                     sar rsi, 4
002DCDB1  49 0F AF F4                     imul rsi, r12
002DCDB5  48 8B C6                        mov rax, rsi
002DCDB8  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
002DCDBD  48 83 C4 30                     add rsp, 0x30
002DCDC1  41 5F                           pop r15
002DCDC3  41 5E                           pop r14
002DCDC5  41 5D                           pop r13
002DCDC7  41 5C                           pop r12
002DCDC9  5F                              pop rdi
002DCDCA  5E                              pop rsi
002DCDCB  5D                              pop rbp
002DCDCC  C3                              ret
002DCDCD  CC                              int3
002DCDCE  48 83 C8 FF                     or rax, 0xffffffffffffffff
002DCDD2  EB E4                           jmp 0x1402dcdb8
002DCDD4  45 85 E4                        test r12d, r12d
002DCDD7  74 94                           je 0x1402dcd6d
002DCDD9  48 8B 3B                        mov rdi, qword ptr [rbx]
002DCDDC  44 39 94 24 88 00 00 00         cmp dword ptr [rsp + 0x88], r10d
002DCDE4  0F 85 32 01 00 00               jne 0x1402dcf1c
002DCDEA  48 8B C1                        mov rax, rcx
002DCDED  48 8B 3F                        mov rdi, qword ptr [rdi]
002DCDF0  48 83 E8 01                     sub rax, 1
002DCDF4  75 F7                           jne 0x1402dcded
002DCDF6  48 8B 07                        mov rax, qword ptr [rdi]
002DCDF9  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
002DCDFD  48 39 78 08                     cmp qword ptr [rax + 8], rdi
002DCE01  0F 85 B3 FD FF FF               jne 0x1402dcbba
002DCE07  48 39 3A                        cmp qword ptr [rdx], rdi
002DCE0A  0F 85 AA FD FF FF               jne 0x1402dcbba
002DCE10  48 89 1A                        mov qword ptr [rdx], rbx
002DCE13  41 B8 08 00 00 00               mov r8d, 8
002DCE19  48 8B C3                        mov rax, rbx
002DCE1C  4A 89 14 03                     mov qword ptr [rbx + r8], rdx
002DCE20  48 8B 6B 10                     mov rbp, qword ptr [rbx + 0x10]
002DCE24  48 2B E9                        sub rbp, rcx
002DCE27  48 89 4B 10                     mov qword ptr [rbx + 0x10], rcx
002DCE2B  E9 43 FF FF FF                  jmp 0x1402dcd73
002DCE30  48 85 ED                        test rbp, rbp
002DCE33  74 2A                           je 0x1402dce5f
002DCE35  4C 8B F5                        mov r14, rbp
002DCE38  80 FB 02                        cmp bl, 2
002DCE3B  74 45                           je 0x1402dce82
002DCE3D  8A 05 45 9C CE 00               mov al, byte ptr [rip + 0xce9c45]
002DCE43  84 C0                           test al, al
002DCE45  0F 88 19 01 00 00               js 0x1402dcf64
002DCE4B  48 8B 1F                        mov rbx, qword ptr [rdi]
002DCE4E  48 8B CF                        mov rcx, rdi
002DCE51  E8 8A 7C 05 00                  call 0x140334ae0
002DCE56  48 8B FB                        mov rdi, rbx
002DCE59  49 83 EE 01                     sub r14, 1
002DCE5D  75 DE                           jne 0x1402dce3d
002DCE5F  48 8B D5                        mov rdx, rbp
002DCE62  48 8D 0D 97 BE B5 00            lea rcx, [rip + 0xb5be97]
002DCE69  E8 2E 5B 04 00                  call 0x14032299c
002DCE6E  E9 2F FF FF FF                  jmp 0x1402dcda2
002DCE73  B9 01 00 00 00                  mov ecx, 1
002DCE78  E8 17 C2 02 00                  call 0x140309094
002DCE7D  E9 84 FE FF FF                  jmp 0x1402dcd06
002DCE82  8A 05 00 9C CE 00               mov al, byte ptr [rip + 0xce9c00]
002DCE88  84 C0                           test al, al
002DCE8A  0F 88 9A 00 00 00               js 0x1402dcf2a
002DCE90  48 8B 1F                        mov rbx, qword ptr [rdi]
002DCE93  48 8B CF                        mov rcx, rdi
002DCE96  E8 B5 7C 05 00                  call 0x140334b50
002DCE9B  48 8B FB                        mov rdi, rbx
002DCE9E  49 83 EE 01                     sub r14, 1
002DCEA2  75 DE                           jne 0x1402dce82
002DCEA4  EB B9                           jmp 0x1402dce5f
002DCEA6  44 0F 20 C7                     mov rdi, cr8
002DCEAA  BA 0F 00 00 00                  mov edx, 0xf
002DCEAF  44 0F 22 C2                     mov cr8, rdx
002DCEB3  44 39 15 66 9E CE 00            cmp dword ptr [rip + 0xce9e66], r10d
002DCEBA  75 44                           jne 0x1402dcf00
002DCEBC  48 8B 05 65 9E B2 00            mov rax, qword ptr [rip + 0xb29e65]
002DCEC3  45 33 C0                        xor r8d, r8d
002DCEC6  48 8B 0D 13 DA C1 00            mov rcx, qword ptr [rip + 0xc1da13]
002DCECD  33 D2                           xor edx, edx
002DCECF  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
002DCED3  E8 F8 DB 3D 00                  call 0x1406baad0
002DCED8  45 33 D2                        xor r10d, r10d
002DCEDB  44 39 15 3E 9E CE 00            cmp dword ptr [rip + 0xce9e3e], r10d
002DCEE2  74 0F                           je 0x1402dcef3
002DCEE4  44 0F 20 C1                     mov rcx, cr8
002DCEE8  40 8A D7                        mov dl, dil
002DCEEB  E8 A8 87 21 00                  call 0x1404f5698
002DCEF0  45 33 D2                        xor r10d, r10d
002DCEF3  40 0F B6 C7                     movzx eax, dil
002DCEF7  44 0F 22 C0                     mov cr8, rax
002DCEFB  E9 16 FE FF FF                  jmp 0x1402dcd16
002DCF00  40 8A CF                        mov cl, dil
002DCF03  E8 F4 87 21 00                  call 0x1404f56fc
002DCF08  EB B2                           jmp 0x1402dcebc
002DCF0A  44 38 15 76 9B CE 00            cmp byte ptr [rip + 0xce9b76], r10b
002DCF11  0F 84 E0 FD FF FF               je 0x1402dccf7
002DCF17  E9 CC FD FF FF                  jmp 0x1402dcce8
002DCF1C  48 89 1B                        mov qword ptr [rbx], rbx
002DCF1F  48 8B D3                        mov rdx, rbx
002DCF22  49 8B CA                        mov rcx, r10
002DCF25  E9 E9 FE FF FF                  jmp 0x1402dce13
002DCF2A  8B 05 40 33 B5 00               mov eax, dword ptr [rip + 0xb53340]
002DCF30  FF C0                           inc eax
002DCF32  85 05 1C 81 CE 00               test dword ptr [rip + 0xce811c], eax
002DCF38  89 05 32 33 B5 00               mov dword ptr [rip + 0xb53332], eax
002DCF3E  0F 85 4C FF FF FF               jne 0x1402dce90
002DCF44  49 8B C7                        mov rax, r15
002DCF47  48 8B CF                        mov rcx, rdi
002DCF4A  BA 01 00 00 00                  mov edx, 1
002DCF4F  48 2B C8                        sub rcx, rax
002DCF52  48 C1 F9 04                     sar rcx, 4
002DCF56  49 0F AF CC                     imul rcx, r12
002DCF5A  E8 19 73 1F 00                  call 0x1404d4278
002DCF5F  E9 2C FF FF FF                  jmp 0x1402dce90
002DCF64  8B 05 06 33 B5 00               mov eax, dword ptr [rip + 0xb53306]
002DCF6A  FF C0                           inc eax
002DCF6C  85 05 E2 80 CE 00               test dword ptr [rip + 0xce80e2], eax
002DCF72  89 05 F8 32 B5 00               mov dword ptr [rip + 0xb532f8], eax
002DCF78  0F 85 CD FE FF FF               jne 0x1402dce4b
002DCF7E  49 8B C7                        mov rax, r15
002DCF81  48 8B CF                        mov rcx, rdi
002DCF84  BA 01 00 00 00                  mov edx, 1
002DCF89  48 2B C8                        sub rcx, rax
002DCF8C  48 C1 F9 04                     sar rcx, 4
002DCF90  49 0F AF CC                     imul rcx, r12
002DCF94  E8 DF 72 1F 00                  call 0x1404d4278
002DCF99  E9 AD FE FF FF                  jmp 0x1402dce4b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiManageUltraSpacePageTable(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m68;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p88;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    a2 = (unsigned int)((a2) >> (9));
    a2 = (unsigned int)((a2) & (63));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11911973) + 4)));
    a2 = (a2 + a2 * 2) << (7);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 11866312));
    v_r13 = 0;
    v_stack_m48 = *(unsigned __int64 *)(a2 + 376);
    a1 = (*(unsigned __int64 *)(a2 + 376)) + (808);
    if (((unsigned __int8)(v_cr8)) == 2) goto loc_002DCC43;
    result = ExAcquireSpinLockExclusive(a1, a2, a3, a4);
    v_stack_p10 = (unsigned __int8)(result);
loc_002DCB69:
    v_r10 = 0;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13575432))))) & (3));
loc_002DCB86:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 648 + 16) != 0) goto loc_002DCBEC;
loc_002DCB8F:
    v_rbp = (unsigned int)((0) + 1);
    v_rdi = (*(unsigned __int64 *)(a2 + 376) + 648) + (32);
    if (((unsigned int)(v_rbp)) < 4) goto loc_002DCB86;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_002DCBC1;
    if ((((unsigned __int8)((unsigned int)(a3))) & (2)) == 0) goto loc_002DCBCB;
loc_002DCBAD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776 + 8))) == (*(unsigned __int64 *)(a2 + 376) + 776)) goto loc_002DCD1D;
loc_002DCBBA:
loc_002DCBC1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776 + 16)) == 0) goto loc_002DCCCC;
loc_002DCBCB:
    result = ((unsigned int)((unsigned int)(v_r14))) << (5);
    result = (result) + (648);
    result = (result) + (v_stack_m48);
    if ((*(unsigned __int64 *)(result + 16)) != 0) goto loc_002DCBAD;
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13575432)));
    goto loc_002DCBAD;
loc_002DCBEC:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13575432))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 24)))));
    if (((unsigned int)(result)) > 2) goto loc_002DCC52;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 24)))) & (1)) != 0) goto loc_002DCC03;
    if (((unsigned int)(result)) >= 2) goto loc_002DCC52;
loc_002DCC03:
    if (v_stack_p20 == 0) goto loc_002DCB8F;
    if (0 != 0) goto loc_002DCB8F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 648 + 16)) < (v_r10 + 8)) goto loc_002DCB8F;
    result = KeFlushTb(v_r13 + 1 + 1, v_r13 + 1, v_r10 + 8, v_stack_m48);
    v_rbp = (unsigned int)((v_rbp) - 1);
    v_rdi = (v_rdi) - (32);
    v_r10 = 0;
    goto loc_002DCB8F;
loc_002DCC43:
    v_stack_p10 = 17;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_r13 + 1 + 1, v_r13 + 1, 1 + 7, v_stack_m48);
    goto loc_002DCB69;
loc_002DCC52:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8) = *(unsigned __int64 *)(v_rdi + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8)) = *(unsigned __int64 *)(v_rdi);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776) + 8)) != (*(unsigned __int64 *)(a2 + 376) + 776)) goto loc_002DCBBA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776 + 8))) != (*(unsigned __int64 *)(a2 + 376) + 776)) goto loc_002DCBBA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi)) + 8)) != (*(unsigned __int64 *)(v_rdi))) goto loc_002DCBBA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8))) != (*(unsigned __int64 *)(v_rdi))) goto loc_002DCBBA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776 + 8)) = *(unsigned __int64 *)(v_rdi);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8)) = *(unsigned __int64 *)(a2 + 376) + 776;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776 + 8);
    *(unsigned __int64 *)(v_rdi + 8) = v_rdi;
    *(unsigned __int64 *)(v_rdi) = v_rdi;
    *(unsigned __int64 *)(v_rdi + 16) = 0;
    goto loc_002DCB8F;
loc_002DCCCC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13540838)))) & (4)) == 0) goto loc_002DCE73;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13540838)))) & (2)) != 0) goto loc_002DCCF7;
    if (condition_is_below) goto loc_002DCF0A;
loc_002DCCE8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13540754)))) == 1) goto loc_002DCE73;
loc_002DCCF7:
    a2 = 0;
    a1 = 0;
    result = KiFlushAddressSpaceTb(a1, a2, 1, 1);
loc_002DCD06:
    v_r10 = 0;
    if ((*(unsigned int *)(v_rip + 12105924)) != 0) goto loc_002DCEA6;
loc_002DCD16:
    goto loc_002DCD62;
loc_002DCD1D:
    *(unsigned __int64 *)(a1) = result;
    *(unsigned __int64 *)(a1 + 8) = 0;
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_002DCD62;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776 + 16)) == 0) goto loc_002DCD62;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776) + 8)) != (*(unsigned __int64 *)(a2 + 376) + 776)) goto loc_002DCBBA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776))) goto loc_002DCBBA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776)) + 8) = *(unsigned __int64 *)(a2 + 376) + 776;
loc_002DCD62:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776 + 16)) > 256) goto loc_002DCDD4;
loc_002DCD6D:
loc_002DCD73:
    result = MiReleaseSpinLockExclusive(v_stack_m48 + 808, (unsigned __int8)(v_stack_p10), 1, v_stack_m48);
    if (0 != 0) goto loc_002DCE30;
loc_002DCDA2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776) == 0) goto loc_002DCDCE;
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 376) + 776)) - ((unsigned int)(*(unsigned int *)(v_rip + 13575432)));
    v_rsi = (v_rsi) >> (4);
    v_rsi = (v_rsi) * ((unsigned int)(a3));
loc_002DCDB8:
    v_rsp = (v_rsp) + (48);
    return v_rsi;
loc_002DCDCE:
    result = (v_rsi) | (-1);
    goto loc_002DCDB8;
loc_002DCDD4:
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_002DCD6D;
    if (v_stack_p88 != 0) goto loc_002DCF1C;
loc_002DCDED:
    result = (v_stack_m48 + 808) - (1);
    if (condition_is_not_equal) goto loc_002DCDED;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8))) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8)))) goto loc_002DCBBA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8)))) goto loc_002DCBBA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8)) + 8)) = v_stack_p8;
loc_002DCE13:
    *(unsigned __int64 *)(v_stack_p8 + 8 * 1) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8)) + 8);
    v_rbp = (*(unsigned __int64 *)(v_stack_p8 + 16)) - (v_stack_m48 + 808);
    *(unsigned __int64 *)(v_stack_p8 + 16) = v_stack_m48 + 808;
    goto loc_002DCD73;
loc_002DCE30:
    if (v_rbp == 0) goto loc_002DCE5F;
    if (((unsigned __int8)(v_stack_p8)) == 2) goto loc_002DCE82;
loc_002DCE3D:
    if (sign_flag) goto loc_002DCF64;
loc_002DCE4B:
    result = MiReleaseFreshPage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8)) + 8), 8, v_stack_m48);
    v_r14 = (v_rbp) - (1);
    if (condition_is_not_equal) goto loc_002DCE3D;
loc_002DCE5F:
    result = MiReleaseNonPagedResources(v_rip + 11910807, v_rbp, 8, v_stack_m48);
    goto loc_002DCDA2;
loc_002DCE73:
    result = KxFlushEntireTb(1, v_rbp, 8, v_stack_m48);
    goto loc_002DCD06;
loc_002DCE82:
    if (sign_flag) goto loc_002DCF2A;
loc_002DCE90:
    result = MiReleaseFreshPageAtDpc(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8))), v_rbp, 8, v_stack_m48);
    v_r14 = (v_r14) - (1);
    if (condition_is_not_equal) goto loc_002DCE82;
    goto loc_002DCE5F;
loc_002DCEA6:
    if ((*(unsigned int *)(v_rip + 13540966)) != 0) goto loc_002DCF00;
loc_002DCEBC:
    a3 = 0;
    a2 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 12704275), a2, a3, v_stack_m48);
    v_r10 = 0;
    if ((*(unsigned int *)(v_rip + 13540926)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, v_stack_m48);
        v_r10 = 0;
    }
    goto loc_002DCD16;
loc_002DCF00:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), a2, a3, v_stack_m48);
    goto loc_002DCEBC;
loc_002DCF0A:
    if ((*(unsigned __int8 *)(v_rip + 13540214)) == 0) goto loc_002DCCF7;
    goto loc_002DCCE8;
loc_002DCF1C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8))))) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8))));
    goto loc_002DCE13;
loc_002DCF2A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11875136))) + 1);
    *(unsigned int *)(v_rip + 11875122) = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 13533468)) & ((unsigned int)(result))) != 0) goto loc_002DCE90;
    a1 = (v_cr8) - ((unsigned int)(*(unsigned int *)(v_rip + 13575432)));
    a1 = (a1) >> (4);
    a1 = (a1) * ((unsigned int)(a3));
    result = MiArePageContentsZero(a1, 1, a3, v_stack_m48);
    goto loc_002DCE90;
loc_002DCF64:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11875078))) + 1);
    *(unsigned int *)(v_rip + 11875064) = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 13533410)) & ((unsigned int)(result))) != 0) goto loc_002DCE4B;
    a1 = (v_cr8) - ((unsigned int)(*(unsigned int *)(v_rip + 13575432)));
    a1 = (a1) >> (4);
    a1 = (a1) * ((unsigned int)(a3));
    result = MiArePageContentsZero(a1, 1, a3, v_stack_m48);
    goto loc_002DCE4B;
}
```

## 5. (Beta) C Style

```c
int64_t MiManageUltraSpacePageTable(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m68;
    uint8_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;
    uint32_t v_stack_p88;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    Arg2 = (uint32_t)((Arg2) >> (9));
    Arg2 = (uint32_t)((Arg2) & (63));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB5C325) + 0x4)));
    Arg2 = (Arg2 + Arg2 * 2) << (7);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xB510C8));
    local_r13 = 0;
    v_stack_m48 = *(uint64_t *)(Arg2 + 0x178);
    Arg1 = (*(uint64_t *)(Arg2 + 0x178)) + (808);
    if (((uint8_t)(v_cr8)) == 2) goto loc_002DCC43;
    result = ExAcquireSpinLockExclusive(Arg1, Arg2, Arg3, a4);
    v_stack_p10 = (uint8_t)(result);
loc_002DCB69:
    local_r10 = 0;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF2508))))) & (3));
loc_002DCB86:
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x288 + 0x10) != 0) goto loc_002DCBEC;
loc_002DCB8F:
    local_rbp = (uint32_t)((0) + 1);
    local_rdi = (*(uint64_t *)(Arg2 + 0x178) + 648) + (32);
    if (((uint32_t)(local_rbp)) < 4) goto loc_002DCB86;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_002DCBC1;
    if ((((uint8_t)((uint32_t)(Arg3))) & (2)) == 0) goto loc_002DCBCB;
loc_002DCBAD:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308 + 0x8))) == (*(uint64_t *)(Arg2 + 0x178) + 776)) goto loc_002DCD1D;
loc_002DCBBA:
loc_002DCBC1:
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308 + 0x10)) == 0) goto loc_002DCCCC;
loc_002DCBCB:
    result = ((uint32_t)((uint32_t)(local_r14))) << (5);
    result = (result) + (648);
    result = (result) + (v_stack_m48);
    if ((*(uint64_t *)(result + 0x10)) != 0) goto loc_002DCBAD;
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF2508)));
    goto loc_002DCBAD;
loc_002DCBEC:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCF2508))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x18)))));
    if (((uint32_t)(result)) > 2) goto loc_002DCC52;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x18)))) & (1)) != 0) goto loc_002DCC03;
    if (((uint32_t)(result)) >= 2) goto loc_002DCC52;
loc_002DCC03:
    if (v_stack_p20 == 0) goto loc_002DCB8F;
    if (0 != 0) goto loc_002DCB8F;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x288 + 0x10)) < (local_r10 + 8)) goto loc_002DCB8F;
    result = KeFlushTb(local_r13 + 1 + 1, local_r13 + 1, local_r10 + 8, v_stack_m48);
    local_rbp = (uint32_t)((local_rbp) - 1);
    local_rdi = (local_rdi) - (32);
    local_r10 = 0;
    goto loc_002DCB8F;
loc_002DCC43:
    v_stack_p10 = 17;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(local_r13 + 1 + 1, local_r13 + 1, 1 + 7, v_stack_m48);
    goto loc_002DCB69;
loc_002DCC52:
    *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8) = *(uint64_t *)(local_rdi + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x8)) = *(uint64_t *)(local_rdi);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308) + 0x8)) != (*(uint64_t *)(Arg2 + 0x178) + 776)) goto loc_002DCBBA;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308 + 0x8))) != (*(uint64_t *)(Arg2 + 0x178) + 776)) goto loc_002DCBBA;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi)) + 0x8)) != (*(uint64_t *)(local_rdi))) goto loc_002DCBBA;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8))) != (*(uint64_t *)(local_rdi))) goto loc_002DCBBA;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308 + 0x8)) = *(uint64_t *)(local_rdi);
    *(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308 + 0x8) = *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8)) = *(uint64_t *)(Arg2 + 0x178) + 776;
    *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8) = *(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308 + 0x8);
    *(uint64_t *)(local_rdi + 0x8) = local_rdi;
    *(uint64_t *)(local_rdi) = local_rdi;
    *(uint64_t *)(local_rdi + 0x10) = 0;
    goto loc_002DCB8F;
loc_002DCCCC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCE9DE6)))) & (4)) == 0) goto loc_002DCE73;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCE9DE6)))) & (2)) != 0) goto loc_002DCCF7;
    if (condition_is_below) goto loc_002DCF0A;
loc_002DCCE8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCE9D92)))) == 1) goto loc_002DCE73;
loc_002DCCF7:
    Arg2 = 0;
    Arg1 = 0;
    result = KiFlushAddressSpaceTb(Arg1, Arg2, 1, 1);
loc_002DCD06:
    local_r10 = 0;
    if ((*(uint32_t *)(v_rip + 0xB8B8C4)) != 0) goto loc_002DCEA6;
loc_002DCD16:
    goto loc_002DCD62;
loc_002DCD1D:
    *(uint64_t *)(Arg1) = result;
    *(uint64_t *)(Arg1 + 0x8) = 0;
    *(uint64_t *)(Arg1) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_002DCD62;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308 + 0x10)) == 0) goto loc_002DCD62;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308) + 0x8)) != (*(uint64_t *)(Arg2 + 0x178) + 776)) goto loc_002DCBBA;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308))) goto loc_002DCBBA;
    *(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308)) + 0x8) = *(uint64_t *)(Arg2 + 0x178) + 776;
loc_002DCD62:
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308 + 0x10)) > 256) goto loc_002DCDD4;
loc_002DCD6D:
loc_002DCD73:
    result = MiReleaseSpinLockExclusive(v_stack_m48 + 808, (uint8_t)(v_stack_p10), 1, v_stack_m48);
    if (0 != 0) goto loc_002DCE30;
loc_002DCDA2:
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308) == 0) goto loc_002DCDCE;
    local_rsi = (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x178) + 0x308)) - ((uint32_t)(*(uint32_t *)(v_rip + 0xCF2508)));
    local_rsi = (local_rsi) >> (4);
    local_rsi = (local_rsi) * ((uint32_t)(Arg3));
loc_002DCDB8:
    local_rsp = (local_rsp) + (48);
    return local_rsi;
loc_002DCDCE:
    result = (local_rsi) | (-1);
    goto loc_002DCDB8;
loc_002DCDD4:
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_002DCD6D;
    if (v_stack_p88 != 0) goto loc_002DCF1C;
loc_002DCDED:
    result = (v_stack_m48 + 808) - (1);
    if (condition_is_not_equal) goto loc_002DCDED;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8))) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_stack_p8)))) goto loc_002DCBBA;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(v_stack_p8)))) goto loc_002DCBBA;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8)) + 0x8)) = v_stack_p8;
loc_002DCE13:
    *(uint64_t *)(v_stack_p8 + 0x8 * 1) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8)) + 0x8);
    local_rbp = (*(uint64_t *)(v_stack_p8 + 0x10)) - (v_stack_m48 + 808);
    *(uint64_t *)(v_stack_p8 + 0x10) = v_stack_m48 + 808;
    goto loc_002DCD73;
loc_002DCE30:
    if (local_rbp == 0) goto loc_002DCE5F;
    if (((uint8_t)(v_stack_p8)) == 2) goto loc_002DCE82;
loc_002DCE3D:
    if (sign_flag) goto loc_002DCF64;
loc_002DCE4B:
    result = MiReleaseFreshPage(*(uint64_t *)(*(uint64_t *)(v_stack_p8)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8)) + 0x8), 8, v_stack_m48);
    local_r14 = (local_rbp) - (1);
    if (condition_is_not_equal) goto loc_002DCE3D;
loc_002DCE5F:
    result = MiReleaseNonPagedResources(v_rip + 11910807, local_rbp, 8, v_stack_m48);
    goto loc_002DCDA2;
loc_002DCE73:
    result = KxFlushEntireTb(1, local_rbp, 8, v_stack_m48);
    goto loc_002DCD06;
loc_002DCE82:
    if (sign_flag) goto loc_002DCF2A;
loc_002DCE90:
    result = MiReleaseFreshPageAtDpc(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8))), local_rbp, 8, v_stack_m48);
    local_r14 = (local_r14) - (1);
    if (condition_is_not_equal) goto loc_002DCE82;
    goto loc_002DCE5F;
loc_002DCEA6:
    if ((*(uint32_t *)(v_rip + 0xCE9E66)) != 0) goto loc_002DCF00;
loc_002DCEBC:
    Arg3 = 0;
    Arg2 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0xC1DA13), Arg2, Arg3, v_stack_m48);
    local_r10 = 0;
    if ((*(uint32_t *)(v_rip + 0xCE9E3E)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, v_stack_m48);
        local_r10 = 0;
    }
    goto loc_002DCD16;
loc_002DCF00:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), Arg2, Arg3, v_stack_m48);
    goto loc_002DCEBC;
loc_002DCF0A:
    if ((*(uint8_t *)(v_rip + 0xCE9B76)) == 0) goto loc_002DCCF7;
    goto loc_002DCCE8;
loc_002DCF1C:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8))))) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8))));
    goto loc_002DCE13;
loc_002DCF2A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB53340))) + 1);
    *(uint32_t *)(v_rip + 0xB53332) = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xCE811C)) & ((uint32_t)(result))) != 0) goto loc_002DCE90;
    Arg1 = (v_cr8) - ((uint32_t)(*(uint32_t *)(v_rip + 0xCF2508)));
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * ((uint32_t)(Arg3));
    result = MiArePageContentsZero(Arg1, 1, Arg3, v_stack_m48);
    goto loc_002DCE90;
loc_002DCF64:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB53306))) + 1);
    *(uint32_t *)(v_rip + 0xB532F8) = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xCE80E2)) & ((uint32_t)(result))) != 0) goto loc_002DCE4B;
    Arg1 = (v_cr8) - ((uint32_t)(*(uint32_t *)(v_rip + 0xCF2508)));
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * ((uint32_t)(Arg3));
    result = MiArePageContentsZero(Arg1, 1, Arg3, v_stack_m48);
    goto loc_002DCE4B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DCAF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
