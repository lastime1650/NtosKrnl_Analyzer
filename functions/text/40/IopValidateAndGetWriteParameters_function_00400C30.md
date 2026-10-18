# IopValidateAndGetWriteParameters

- RVA: `0x00400C30`–`0x004011EB` (길이 `1,467` bytes)
- VA: `0x0000000140400C30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A304`
- 디코드: `368`개 명령, `1,467/1,467` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00400DEF` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00400F06` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00400F2C` → [ObfReferenceObject](../20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00400FC7` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00400FE3` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x00401056` → [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x0040107F` → [IopWaitAndAcquireFileObjectLock](../../page/8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x00401119` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0040112F` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [IopPopulateCopyWriteWorkerData](IopPopulateCopyWriteWorkerData_function_00400B48.md) at `0x00400BE3`
- [IopWriteFile](../../page/8E/IopWriteFile_function_008E9790.md) at `0x008E9877`

### Static image references
- `0x00400F9C` → RVA `0x00FC6B80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00400DEF` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x00400FC7` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
  - `0x0040107F` → [IopWaitAndAcquireFileObjectLock](../../page/8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00400C30  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00400C35  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00400C3A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00400C3F  57                              push rdi
00400C40  41 56                           push r14
00400C42  41 57                           push r15
00400C44  48 83 EC 40                     sub rsp, 0x40
00400C48  4D 8B F8                        mov r15, r8
00400C4B  48 8B FA                        mov rdi, rdx
00400C4E  48 8B D9                        mov rbx, rcx
00400C51  C7 44 24 30 00 00 00 00         mov dword ptr [rsp + 0x30], 0
00400C59  48 83 79 60 00                  cmp qword ptr [rcx + 0x60], 0
00400C5E  0F 85 9B 04 00 00               jne 0x1404010ff
00400C64  48 8B 41 78                     mov rax, qword ptr [rcx + 0x78]
00400C68  48 85 C0                        test rax, rax
00400C6B  0F 85 1B 05 00 00               jne 0x14040118c
00400C71  8B 53 70                        mov edx, dword ptr [rbx + 0x70]
00400C74  F6 C2 01                        test dl, 1
00400C77  0F 85 2C 05 00 00               jne 0x1404011a9
00400C7D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00400C86  48 89 03                        mov qword ptr [rbx], rax
00400C89  0F B6 80 32 02 00 00            movzx eax, byte ptr [rax + 0x232]
00400C90  88 43 08                        mov byte ptr [rbx + 8], al
00400C93  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00400C97  41 8B 40 50                     mov eax, dword ptr [r8 + 0x50]
00400C9B  A8 02                           test al, 2
00400C9D  0F 85 39 05 00 00               jne 0x1404011dc
00400CA3  32 C0                           xor al, al
00400CA5  88 43 09                        mov byte ptr [rbx + 9], al
00400CA8  C1 EA 1E                        shr edx, 0x1e
00400CAB  F6 D2                           not dl
00400CAD  80 E2 01                        and dl, 1
00400CB0  88 53 0A                        mov byte ptr [rbx + 0xa], dl
00400CB3  49 8B 48 10                     mov rcx, qword ptr [r8 + 0x10]
00400CB7  48 85 C9                        test rcx, rcx
00400CBA  0F 85 08 02 00 00               jne 0x140400ec8
00400CC0  41 F7 40 50 00 08 00 00         test dword ptr [r8 + 0x50], 0x800
00400CC8  75 11                           jne 0x140400cdb
00400CCA  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
00400CCE  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00400CD2  48 85 C9                        test rcx, rcx
00400CD5  0F 85 4C 03 00 00               jne 0x140401027
00400CDB  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
00400CDF  48 83 79 18 00                  cmp qword ptr [rcx + 0x18], 0
00400CE4  74 36                           je 0x140400d1c
00400CE6  49 8B 80 D0 00 00 00            mov rax, qword ptr [r8 + 0xd0]
00400CED  48 85 C0                        test rax, rax
00400CF0  74 0D                           je 0x140400cff
00400CF2  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00400CF6  48 85 C0                        test rax, rax
00400CF9  0F 85 5D 02 00 00               jne 0x140400f5c
00400CFF  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00400D03  48 85 C0                        test rax, rax
00400D06  74 14                           je 0x140400d1c
00400D08  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00400D10  48 8B C8                        mov rcx, rax
00400D13  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
00400D17  48 85 C0                        test rax, rax
00400D1A  75 F4                           jne 0x140400d10
00400D1C  48 8B C1                        mov rax, rcx
00400D1F  48 8D 53 18                     lea rdx, [rbx + 0x18]
00400D23  48 89 02                        mov qword ptr [rdx], rax
00400D26  80 7B 08 00                     cmp byte ptr [rbx + 8], 0
00400D2A  0F 84 BD 02 00 00               je 0x140400fed
00400D30  48 83 7B 60 00                  cmp qword ptr [rbx + 0x60], 0
00400D35  0F 85 B2 02 00 00               jne 0x140400fed
00400D3B  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
00400D3F  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
00400D49  48 3B CA                        cmp rcx, rdx
00400D4C  48 0F 43 CA                     cmovae rcx, rdx
00400D50  8B 01                           mov eax, dword ptr [rcx]
00400D52  89 01                           mov dword ptr [rcx], eax
00400D54  44 0F B6 53 09                  movzx r10d, byte ptr [rbx + 9]
00400D59  4C 8B 5B 38                     mov r11, qword ptr [rbx + 0x38]
00400D5D  4C 8B 43 28                     mov r8, qword ptr [rbx + 0x28]
00400D61  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00400D6A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00400D6F  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00400D76  48 83 B9 10 03 00 00 00         cmp qword ptr [rcx + 0x310], 0
00400D7E  74 29                           je 0x140400da9
00400D80  0F B7 81 EC 06 00 00            movzx eax, word ptr [rcx + 0x6ec]
00400D87  B9 4C 01 00 00                  mov ecx, 0x14c
00400D8C  66 3B C1                        cmp ax, cx
00400D8F  75 76                           jne 0x140400e07
00400D91  45 84 D2                        test r10b, r10b
00400D94  75 13                           jne 0x140400da9
00400D96  49 83 C8 01                     or r8, 1
00400D9A  41 8B 0B                        mov ecx, dword ptr [r11]
00400D9D  8B 01                           mov eax, dword ptr [rcx]
00400D9F  89 01                           mov dword ptr [rcx], eax
00400DA1  48 89 4B 38                     mov qword ptr [rbx + 0x38], rcx
00400DA5  4C 89 43 28                     mov qword ptr [rbx + 0x28], r8
00400DA9  48 83 BB 80 00 00 00 00         cmp qword ptr [rbx + 0x80], 0
00400DB1  75 19                           jne 0x140400dcc
00400DB3  8B 43 48                        mov eax, dword ptr [rbx + 0x48]
00400DB6  85 C0                           test eax, eax
00400DB8  74 12                           je 0x140400dcc
00400DBA  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
00400DBE  4C 8D 04 01                     lea r8, [rcx + rax]
00400DC2  4C 3B C2                        cmp r8, rdx
00400DC5  77 4F                           ja 0x140400e16
00400DC7  4C 3B C1                        cmp r8, rcx
00400DCA  72 4A                           jb 0x140400e16
00400DCC  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00400DD0  48 83 B8 B0 00 00 00 00         cmp qword ptr [rax + 0xb0], 0
00400DD8  74 0A                           je 0x140400de4
00400DDA  48 F7 43 28 FE FF FF FF         test qword ptr [rbx + 0x28], -2
00400DE2  75 11                           jne 0x140400df5
00400DE4  4D 85 FF                        test r15, r15
00400DE7  74 32                           je 0x140400e1b
00400DE9  41 F6 C7 03                     test r15b, 3
00400DED  74 40                           je 0x140400e2f
00400DEF  E8 DC 91 49 00                  call 0x140899fd0
00400DF4  CC                              int3
00400DF5  BF 0D 00 00 C0                  mov edi, 0xc000000d
00400DFA  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00400DFE  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00400E02  E9 A2 00 00 00                  jmp 0x140400ea9
00400E07  B9 C4 01 00 00                  mov ecx, 0x1c4
00400E0C  66 3B C1                        cmp ax, cx
00400E0F  75 98                           jne 0x140400da9
00400E11  E9 7B FF FF FF                  jmp 0x140400d91
00400E16  0F B6 02                        movzx eax, byte ptr [rdx]
00400E19  EB B1                           jmp 0x140400dcc
00400E1B  4D 85 C9                        test r9, r9
00400E1E  74 26                           je 0x140400e46
00400E20  4C 3B CA                        cmp r9, rdx
00400E23  49 0F 42 D1                     cmovb rdx, r9
00400E27  90                              nop
00400E28  8B 02                           mov eax, dword ptr [rdx]
00400E2A  89 43 58                        mov dword ptr [rbx + 0x58], eax
00400E2D  EB 17                           jmp 0x140400e46
00400E2F  48 8B C2                        mov rax, rdx
00400E32  4C 3B FA                        cmp r15, rdx
00400E35  49 0F 42 C7                     cmovb rax, r15
00400E39  90                              nop
00400E3A  0F B6 00                        movzx eax, byte ptr [rax]
00400E3D  49 8B 07                        mov rax, qword ptr [r15]
00400E40  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
00400E44  EB D5                           jmp 0x140400e1b
00400E46  EB 0B                           jmp 0x140400e53
00400E48  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00400E4D  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00400E51  EB 56                           jmp 0x140400ea9
00400E53  48 8D 53 18                     lea rdx, [rbx + 0x18]
00400E57  80 7B 08 00                     cmp byte ptr [rbx + 8], 0
00400E5B  74 10                           je 0x140400e6d
00400E5D  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00400E61  8B 48 50                        mov ecx, dword ptr [rax + 0x50]
00400E64  F6 C1 08                        test cl, 8
00400E67  0F 85 1E 02 00 00               jne 0x14040108b
00400E6D  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00400E74  24 06                           and al, 6
00400E76  3C 04                           cmp al, 4
00400E78  75 08                           jne 0x140400e82
00400E7A  48 C7 43 50 FF FF FF FF         mov qword ptr [rbx + 0x50], 0xffffffffffffffff
00400E82  48 85 FF                        test rdi, rdi
00400E85  0F 85 0C 01 00 00               jne 0x140400f97
00400E8B  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00400E8F  80 7B 09 00                     cmp byte ptr [rbx + 9], 0
00400E93  75 45                           jne 0x140400eda
00400E95  4D 85 FF                        test r15, r15
00400E98  0F 84 73 01 00 00               je 0x140401011
00400E9E  8B 43 54                        mov eax, dword ptr [rbx + 0x54]
00400EA1  85 C0                           test eax, eax
00400EA3  0F 88 90 01 00 00               js 0x140401039
00400EA9  85 FF                           test edi, edi
00400EAB  0F 88 5A 02 00 00               js 0x14040110b
00400EB1  8B C7                           mov eax, edi
00400EB3  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00400EB8  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00400EBD  48 83 C4 40                     add rsp, 0x40
00400EC1  41 5F                           pop r15
00400EC3  41 5E                           pop r14
00400EC5  5F                              pop rdi
00400EC6  C3                              ret
00400EC7  CC                              int3
00400EC8  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00400ECC  48 85 C9                        test rcx, rcx
00400ECF  0F 85 0A FE FF FF               jne 0x140400cdf
00400ED5  E9 E6 FD FF FF                  jmp 0x140400cc0
00400EDA  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
00400EDE  8B 77 50                        mov esi, dword ptr [rdi + 0x50]
00400EE1  83 E6 04                        and esi, 4
00400EE4  44 0F B6 73 08                  movzx r14d, byte ptr [rbx + 8]
00400EE9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00400EF2  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00400EF9  90                              nop
00400EFA  48 8D 8F 80 00 00 00            lea rcx, [rdi + 0x80]
00400F01  45 33 C0                        xor r8d, r8d
00400F04  33 D2                           xor edx, edx
00400F06  E8 25 F3 E0 FF                  call 0x140210230
00400F0B  C6 44 24 60 00                  mov byte ptr [rsp + 0x60], 0
00400F10  BA 01 00 00 00                  mov edx, 1
00400F15  87 57 74                        xchg dword ptr [rdi + 0x74], edx
00400F18  85 D2                           test edx, edx
00400F1A  0F 85 45 01 00 00               jne 0x140401065
00400F20  48 85 C0                        test rax, rax
00400F23  74 04                           je 0x140400f29
00400F25  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
00400F29  48 8B CF                        mov rcx, rdi
00400F2C  E8 EF EA E0 FF                  call 0x14020fa20
00400F31  33 FF                           xor edi, edi
00400F33  80 7C 24 60 00                  cmp byte ptr [rsp + 0x60], 0
00400F38  0F 85 6B FF FF FF               jne 0x140400ea9
00400F3E  48 8D 53 50                     lea rdx, [rbx + 0x50]
00400F42  4D 85 FF                        test r15, r15
00400F45  75 3B                           jne 0x140400f82
00400F47  44 39 3A                        cmp dword ptr [rdx], r15d
00400F4A  75 36                           jne 0x140400f82
00400F4C  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00400F50  48 8B 48 68                     mov rcx, qword ptr [rax + 0x68]
00400F54  48 89 0A                        mov qword ptr [rdx], rcx
00400F57  E9 42 FF FF FF                  jmp 0x140400e9e
00400F5C  48 8B 00                        mov rax, qword ptr [rax]
00400F5F  48 85 C0                        test rax, rax
00400F62  0F 84 97 FD FF FF               je 0x140400cff
00400F68  48 8B D1                        mov rdx, rcx
00400F6B  48 3B D0                        cmp rdx, rax
00400F6E  0F 84 AB FD FF FF               je 0x140400d1f
00400F74  48 8B 52 18                     mov rdx, qword ptr [rdx + 0x18]
00400F78  48 85 D2                        test rdx, rdx
00400F7B  75 EE                           jne 0x140400f6b
00400F7D  E9 7D FD FF FF                  jmp 0x140400cff
00400F82  83 3A FE                        cmp dword ptr [rdx], -2
00400F85  0F 85 13 FF FF FF               jne 0x140400e9e
00400F8B  83 7B 54 FF                     cmp dword ptr [rbx + 0x54], -1
00400F8F  0F 85 09 FF FF FF               jne 0x140400e9e
00400F95  EB B5                           jmp 0x140400f4c
00400F97  44 0F B6 4B 08                  movzx r9d, byte ptr [rbx + 8]
00400F9C  4C 8B 05 DD 5B BC 00            mov r8, qword ptr [rip + 0xbc5bdd]
00400FA3  48 C7 44 24 60 00 00 00 00      mov qword ptr [rsp + 0x60], 0
00400FAC  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
00400FB5  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00400FBA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00400FBF  BA 02 00 00 00                  mov edx, 2
00400FC4  48 8B CF                        mov rcx, rdi
00400FC7  E8 E4 7D 46 00                  call 0x140868db0
00400FCC  8B F8                           mov edi, eax
00400FCE  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00400FD3  48 89 4B 20                     mov qword ptr [rbx + 0x20], rcx
00400FD7  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00400FDB  85 C0                           test eax, eax
00400FDD  0F 88 C6 FE FF FF               js 0x140400ea9
00400FE3  E8 68 73 E4 FF                  call 0x140248350
00400FE8  E9 A2 FE FF FF                  jmp 0x140400e8f
00400FED  4D 85 FF                        test r15, r15
00400FF0  74 0B                           je 0x140400ffd
00400FF2  49 8B 07                        mov rax, qword ptr [r15]
00400FF5  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
00400FF9  48 8D 53 18                     lea rdx, [rbx + 0x18]
00400FFD  4D 85 C9                        test r9, r9
00401000  0F 84 51 FE FF FF               je 0x140400e57
00401006  41 8B 01                        mov eax, dword ptr [r9]
00401009  89 43 58                        mov dword ptr [rbx + 0x58], eax
0040100C  E9 46 FE FF FF                  jmp 0x140400e57
00401011  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00401015  F7 40 50 80 02 00 00            test dword ptr [rax + 0x50], 0x280
0040101C  0F 85 7C FE FF FF               jne 0x140400e9e
00401022  E9 DF 00 00 00                  jmp 0x140401106
00401027  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0040102B  48 85 C9                        test rcx, rcx
0040102E  0F 85 AB FC FF FF               jne 0x140400cdf
00401034  E9 A2 FC FF FF                  jmp 0x140400cdb
00401039  83 F8 FF                        cmp eax, -1
0040103C  75 0A                           jne 0x140401048
0040103E  83 7B 50 FF                     cmp dword ptr [rbx + 0x50], -1
00401042  0F 84 61 FE FF FF               je 0x140400ea9
00401048  80 7B 09 00                     cmp byte ptr [rbx + 9], 0
0040104C  0F 84 B4 00 00 00               je 0x140401106
00401052  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00401056  E8 35 FA E4 FF                  call 0x140250a90
0040105B  BF 0D 00 00 C0                  mov edi, 0xc000000d
00401060  E9 A6 00 00 00                  jmp 0x14040110b
00401065  85 F6                           test esi, esi
00401067  41 0F 95 C0                     setne r8b
0040106B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00401070  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00401075  4C 8B C8                        mov r9, rax
00401078  41 0F B6 D6                     movzx edx, r14b
0040107C  48 8B CF                        mov rcx, rdi
0040107F  E8 54 D6 4A 00                  call 0x1408ae6d8
00401084  8B F8                           mov edi, eax
00401086  E9 A8 FE FF FF                  jmp 0x140400f33
0040108B  4C 8B 0A                        mov r9, qword ptr [rdx]
0040108E  41 0F B7 91 30 01 00 00         movzx edx, word ptr [r9 + 0x130]
00401096  4C 8D 43 48                     lea r8, [rbx + 0x48]
0040109A  8B CA                           mov ecx, edx
0040109C  66 85 D2                        test dx, dx
0040109F  74 0F                           je 0x1404010b0
004010A1  44 8B D2                        mov r10d, edx
004010A4  8D 42 FF                        lea eax, [rdx - 1]
004010A7  41 85 00                        test dword ptr [r8], eax
004010AA  0F 85 A9 00 00 00               jne 0x140401159
004010B0  44 8B D1                        mov r10d, ecx
004010B3  41 8B 89 98 00 00 00            mov ecx, dword ptr [r9 + 0x98]
004010BA  48 85 4B 40                     test qword ptr [rbx + 0x40], rcx
004010BE  0F 85 95 00 00 00               jne 0x140401159
004010C4  4D 85 FF                        test r15, r15
004010C7  0F 84 A0 FD FF FF               je 0x140400e6d
004010CD  8B 4B 50                        mov ecx, dword ptr [rbx + 0x50]
004010D0  83 F9 FF                        cmp ecx, -1
004010D3  0F 84 A4 00 00 00               je 0x14040117d
004010D9  83 F9 FE                        cmp ecx, -2
004010DC  0F 84 E1 00 00 00               je 0x1404011c3
004010E2  41 0F B7 81 30 01 00 00         movzx eax, word ptr [r9 + 0x130]
004010EA  66 85 C0                        test ax, ax
004010ED  0F 84 7A FD FF FF               je 0x140400e6d
004010F3  FF C8                           dec eax
004010F5  85 C1                           test ecx, eax
004010F7  0F 84 70 FD FF FF               je 0x140400e6d
004010FD  EB 07                           jmp 0x140401106
004010FF  48 83 79 30 00                  cmp qword ptr [rcx + 0x30], 0
00401104  74 3B                           je 0x140401141
00401106  BF 0D 00 00 C0                  mov edi, 0xc000000d
0040110B  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0040110F  48 85 C9                        test rcx, rcx
00401112  74 12                           je 0x140401126
00401114  BA 44 66 6C 74                  mov edx, 0x746c6644
00401119  E8 C2 67 EF FF                  call 0x1402f78e0
0040111E  48 C7 43 20 00 00 00 00         mov qword ptr [rbx + 0x20], 0
00401126  BA 44 66 6C 74                  mov edx, 0x746c6644
0040112B  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0040112F  E8 AC 67 EF FF                  call 0x1402f78e0
00401134  48 C7 43 10 00 00 00 00         mov qword ptr [rbx + 0x10], 0
0040113C  E9 70 FD FF FF                  jmp 0x140400eb1
00401141  48 85 FF                        test rdi, rdi
00401144  75 C0                           jne 0x140401106
00401146  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0040114A  48 39 B8 B0 00 00 00            cmp qword ptr [rax + 0xb0], rdi
00401151  0F 84 0D FB FF FF               je 0x140400c64
00401157  EB AD                           jmp 0x140401106
00401159  66 85 D2                        test dx, dx
0040115C  74 0C                           je 0x14040116a
0040115E  33 D2                           xor edx, edx
00401160  41 8B 00                        mov eax, dword ptr [r8]
00401163  41 F7 F2                        div r10d
00401166  85 D2                           test edx, edx
00401168  75 9C                           jne 0x140401106
0040116A  41 8B 81 98 00 00 00            mov eax, dword ptr [r9 + 0x98]
00401171  48 85 43 40                     test qword ptr [rbx + 0x40], rax
00401175  0F 84 49 FF FF FF               je 0x1404010c4
0040117B  EB 89                           jmp 0x140401106
0040117D  83 7B 54 FF                     cmp dword ptr [rbx + 0x54], -1
00401181  0F 85 52 FF FF FF               jne 0x1404010d9
00401187  E9 E1 FC FF FF                  jmp 0x140400e6d
0040118C  48 8B 08                        mov rcx, qword ptr [rax]
0040118F  48 85 C9                        test rcx, rcx
00401192  0F 84 D9 FA FF FF               je 0x140400c71
00401198  8B 43 48                        mov eax, dword ptr [rbx + 0x48]
0040119B  39 41 28                        cmp dword ptr [rcx + 0x28], eax
0040119E  0F 83 CD FA FF FF               jae 0x140400c71
004011A4  E9 5D FF FF FF                  jmp 0x140401106
004011A9  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
004011AD  8B 48 50                        mov ecx, dword ptr [rax + 0x50]
004011B0  F6 C1 08                        test cl, 8
004011B3  0F 85 C4 FA FF FF               jne 0x140400c7d
004011B9  BF D5 04 00 C0                  mov edi, 0xc00004d5
004011BE  E9 48 FF FF FF                  jmp 0x14040110b
004011C3  83 7B 54 FF                     cmp dword ptr [rbx + 0x54], -1
004011C7  0F 85 15 FF FF FF               jne 0x1404010e2
004011CD  80 7B 09 00                     cmp byte ptr [rbx + 9], 0
004011D1  0F 84 0B FF FF FF               je 0x1404010e2
004011D7  E9 91 FC FF FF                  jmp 0x140400e6d
004011DC  85 D2                           test edx, edx
004011DE  0F 88 BF FA FF FF               js 0x140400ca3
004011E4  B0 01                           mov al, 1
004011E6  E9 BA FA FF FF                  jmp 0x140400ca5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopValidateAndGetWriteParameters(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p60;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    v_stack_m28 = 0;
    if ((*(unsigned __int64 *)(a1 + 96)) != 0) goto loc_004010FF;
loc_00400C64:
    if (*(unsigned __int64 *)(a1 + 120) != 0) goto loc_0040118C;
loc_00400C71:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 112)))) & (1)) != 0) goto loc_004011A9;
loc_00400C7D:
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int8 *)(a1 + 8) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80)))) & (2)) != 0) goto loc_004011DC;
loc_00400CA3:
    result = 0;
loc_00400CA5:
    *(unsigned __int8 *)(a1 + 9) = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 112))) >> (30));
    a2 = (unsigned __int8)(~(a2));
    a2 = (unsigned __int8)((a2) & (1));
    *(unsigned __int8 *)(a1 + 10) = (unsigned __int8)(a2);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) != 0) goto loc_00400EC8;
loc_00400CC0:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80)) & (0x800ULL)) != 0) goto loc_00400CDB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 56) != 0) goto loc_00401027;
loc_00400CDB:
loc_00400CDF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 24)) == 0) goto loc_00400D1C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 208) == 0) goto loc_00400CFF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 208) + 16) != 0) goto loc_00400F5C;
loc_00400CFF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 24) == 0) goto loc_00400D1C;
loc_00400D10:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 24) + 24) != 0) goto loc_00400D10;
loc_00400D1C:
loc_00400D1F:
    *(unsigned __int64 *)(a1 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 24);
    if ((*(unsigned __int8 *)(a1 + 8)) == 0) goto loc_00400FED;
    if ((*(unsigned __int64 *)(a1 + 96)) != 0) goto loc_00400FED;
    a1 = *(unsigned __int64 *)(a1 + 56);
    if ((*(unsigned __int64 *)(a1 + 56)) >= (a1 + 24)) { a1 = a1 + 24; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m20 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_00400DA9;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) != 332) goto loc_00400E07;
loc_00400D91:
    result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 9)) == 0) {
        a3 = (*(unsigned __int64 *)(a1 + 40)) | (1);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 56));
        result = *(unsigned int *)(a1);
        *(unsigned int *)(a1) = (unsigned int)(result);
        *(unsigned __int64 *)(a1 + 56) = a1;
        *(unsigned __int64 *)(a1 + 40) = a3;
    }
    if ((*(unsigned __int64 *)(a1 + 128)) != 0) goto loc_00400DCC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72))) == 0) goto loc_00400DCC;
    if ((*(unsigned __int64 *)(a1 + 64) + (unsigned int)(*(unsigned int *)(a1 + 72)) * 1) > (a1 + 24)) goto loc_00400E16;
    if ((*(unsigned __int64 *)(a1 + 64) + (unsigned int)(*(unsigned int *)(a1 + 72)) * 1) < (*(unsigned __int64 *)(a1 + 64))) goto loc_00400E16;
loc_00400DCC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 176)) == 0) goto loc_00400DE4;
    if (((*(unsigned __int64 *)(a1 + 40)) & (-2)) != 0) goto loc_00400DF5;
loc_00400DE4:
    if (a3 == 0) goto loc_00400E1B;
    if ((((unsigned __int8)(a3)) & (3)) == 0) goto loc_00400E2F;
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(a1 + 64), a1 + 24, *(unsigned __int64 *)(a1 + 64) + (unsigned int)(*(unsigned int *)(a1 + 72)) * 1, a4);
loc_00400DF5:
    v_stack_m28 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00400EA9;
loc_00400E07:
    if (((unsigned __int16)(result)) != 452) goto loc_00400DA9;
    goto loc_00400D91;
loc_00400E16:
    goto loc_00400DCC;
loc_00400E1B:
    if (a4 == 0) goto loc_00400E46;
    a2 = a1 + 24;
    if (a4 < (a1 + 24)) { a2 = a4; }
    *(unsigned int *)(a1 + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    goto loc_00400E46;
loc_00400E2F:
    if (a3 < a2) { a2 = a3; }
    *(unsigned __int64 *)(a1 + 80) = *(unsigned __int64 *)(a3);
    goto loc_00400E1B;
loc_00400E46:
    goto loc_00400E53;
loc_00400E53:
loc_00400E57:
    if ((*(unsigned __int8 *)(a1 + 8)) == 0) goto loc_00400E6D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80)))) & (8)) != 0) goto loc_0040108B;
loc_00400E6D:
    result = (unsigned __int8)(((unsigned int)(a5)) & (6));
    if (((unsigned __int8)(result)) == 4) {
        *(unsigned __int64 *)(a1 + 80) = -1;
    }
    if ((unsigned int)(v_stack_m28) != 0) goto loc_00400F97;
loc_00400E8F:
    if ((*(unsigned __int8 *)(a1 + 9)) != 0) goto loc_00400EDA;
    if (a3 == 0) goto loc_00401011;
loc_00400E9E:
    if (sign_flag) goto loc_00401039;
loc_00400EA9:
    if (sign_flag) goto loc_0040110B;
loc_00400EB1:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)(v_stack_m28)));
loc_00400EC8:
    if (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80)) + 8) != 0) goto loc_00400CDF;
    goto loc_00400CC0;
loc_00400EDA:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 80))) & (4));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_stack_p10 + 16) + 128, a2, a3, a4);
    v_stack_p60 = 0;
    if (1 != 0) goto loc_00401065;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(*(unsigned __int64 *)(v_stack_p10 + 16), 1, a3, a4);
    v_rdi = 0;
loc_00400F33:
    if (v_stack_p60 != 0) goto loc_00400EA9;
    if (0 != 0) goto loc_00400F82;
    if ((*(unsigned int *)(v_stack_p10 + 80)) != 0) goto loc_00400F82;
loc_00400F4C:
    *(unsigned __int64 *)(v_stack_p10 + 80) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 104);
    goto loc_00400E9E;
loc_00400F5C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16)) == 0) goto loc_00400CFF;
loc_00400F6B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 104)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16)))) goto loc_00400D1F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 104) + 24) != 0) goto loc_00400F6B;
    goto loc_00400CFF;
loc_00400F82:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 104) + 24))) != -2) goto loc_00400E9E;
    if ((*(unsigned int *)(v_stack_p10 + 84)) != -1) goto loc_00400E9E;
    goto loc_00400F4C;
loc_00400F97:
    v_stack_p60 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p60;
    result = ObReferenceObjectByHandle(0, 2, *(unsigned __int64 *)(v_rip + 12344285), *(unsigned __int8 *)(v_stack_p10 + 8));
    *(unsigned __int64 *)(v_stack_p10 + 32) = v_stack_p60;
    v_stack_p30 = (unsigned int)(result);
    if (sign_flag) goto loc_00400EA9;
    result = KeResetEvent(v_stack_p60, 2, *(unsigned __int64 *)(v_rip + 12344285), *(unsigned __int8 *)(v_stack_p10 + 8));
    goto loc_00400E8F;
loc_00400FED:
    if (0 != 0) {
        result = *(unsigned __int64 *)(a3);
        *(unsigned __int64 *)(v_stack_p10 + 80) = result;
        a2 = v_stack_p10 + 24;
    }
    if (*(unsigned __int8 *)(v_stack_p10 + 8) == 0) goto loc_00400E57;
    *(unsigned int *)(v_stack_p10 + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(v_stack_p10 + 8))));
    goto loc_00400E57;
loc_00401011:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 80)) & (640)) != 0) goto loc_00400E9E;
    goto loc_00401106;
loc_00401027:
    if (*(unsigned __int64 *)(v_stack_p60 + 8) != 0) goto loc_00400CDF;
    goto loc_00400CDB;
loc_00401039:
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_p10 + 16))) != -1) goto loc_00401048;
    if ((*(unsigned int *)(v_stack_p10 + 80)) == -1) goto loc_00400EA9;
loc_00401048:
    if ((*(unsigned __int8 *)(v_stack_p10 + 9)) == 0) goto loc_00401106;
    result = IopReleaseFileObjectLock(*(unsigned __int64 *)(v_stack_p10 + 16), a2, *(unsigned __int64 *)(v_rip + 12344285), *(unsigned __int8 *)(v_stack_p10 + 8));
    goto loc_0040110B;
loc_00401065:
    a3 = ((unsigned int)(v_rsi) != 0) ? 1 : 0;
    v_stack_p20 = v_stack_p60;
    result = IopWaitAndAcquireFileObjectLock((unsigned int)(0xC000000DULL), (unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8)), a3, result);
    goto loc_00400F33;
loc_0040108B:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))) + 304)) == 0) goto loc_004010B0;
    if (((*(unsigned int *)(v_stack_p10 + 72)) & ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))) + 304) - 1))) != 0) goto loc_00401159;
loc_004010B0:
    if (((*(unsigned __int64 *)(v_stack_p10 + 64)) & ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))) + 152)))) != 0) goto loc_00401159;
loc_004010C4:
    if (a3 == 0) goto loc_00400E6D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 80)))) == -1) goto loc_0040117D;
loc_004010D9:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 80)))) == -2) goto loc_004011C3;
loc_004010E2:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))) + 304)) == 0) goto loc_00400E6D;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))) + 304)) - 1);
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 80)))) & ((unsigned int)(result))) == 0) goto loc_00400E6D;
    goto loc_00401106;
loc_004010FF:
    if ((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_p10 + 80)) + 48)) == 0) goto loc_00401141;
loc_00401106:
loc_0040110B:
    if (*(unsigned __int64 *)(v_stack_p10 + 32) != 0) {
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_p10 + 32), a2, v_stack_p10 + 72, *(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))));
        *(unsigned __int64 *)(v_stack_p10 + 32) = 0;
    }
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_p10 + 16), (unsigned int)(0x746C6644ULL), v_stack_p10 + 72, *(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))));
    *(unsigned __int64 *)(v_stack_p10 + 16) = 0;
    goto loc_00400EB1;
loc_00401141:
    if ((unsigned int)(0xC000000DULL) != 0) goto loc_00401106;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 16) + 176)) == ((unsigned int)(0xC000000DULL))) goto loc_00400C64;
    goto loc_00401106;
loc_00401159:
    if ((unsigned __int16)((unsigned int)(0x746C6644ULL)) == 0) goto loc_0040116A;
    a2 = 0;
    if (0 != 0) goto loc_00401106;
loc_0040116A:
    if (((*(unsigned __int64 *)(v_stack_p10 + 64)) & ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))) + 152)))) == 0) goto loc_004010C4;
    goto loc_00401106;
loc_0040117D:
    if ((*(unsigned int *)(v_stack_p10 + 84)) != -1) goto loc_004010D9;
    goto loc_00400E6D;
loc_0040118C:
    if (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))) + 152))) == 0) goto loc_00400C71;
    if ((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 8))) + 152))) + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 72))))) goto loc_00400C71;
    goto loc_00401106;
loc_004011A9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 80)))) & (8)) != 0) goto loc_00400C7D;
    goto loc_0040110B;
loc_004011C3:
    if ((*(unsigned int *)(v_stack_p10 + 84)) != -1) goto loc_004010E2;
    if ((*(unsigned __int8 *)(v_stack_p10 + 9)) == 0) goto loc_004010E2;
    goto loc_00400E6D;
loc_004011DC:
    if (sign_flag) goto loc_00400CA3;
    goto loc_00400CA5;
}
```

## 5. (Beta) C Style

```c
int64_t IopValidateAndGetWriteParameters(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p60;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    v_stack_m28 = 0;
    if ((*(uint64_t *)(arg1 + 0x60)) != 0) goto loc_004010FF;
loc_00400C64:
    if (*(uint64_t *)(arg1 + 0x78) != 0) goto loc_0040118C;
loc_00400C71:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) & (1)) != 0) goto loc_004011A9;
loc_00400C7D:
    *(uint64_t *)(arg1) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint8_t *)(arg1 + 0x8) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50)))) & (2)) != 0) goto loc_004011DC;
loc_00400CA3:
    result = 0;
loc_00400CA5:
    *(uint8_t *)(arg1 + 0x9) = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x70))) >> (30));
    Arg2 = (uint8_t)(~(Arg2));
    Arg2 = (uint8_t)((Arg2) & (1));
    *(uint8_t *)(arg1 + 0xA) = (uint8_t)(Arg2);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) != 0) goto loc_00400EC8;
loc_00400CC0:
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50)) & (0x800ULL)) != 0) goto loc_00400CDB;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x38) != 0) goto loc_00401027;
loc_00400CDB:
loc_00400CDF:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x18)) == 0) goto loc_00400D1C;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0xD0) == 0) goto loc_00400CFF;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0xD0) + 0x10) != 0) goto loc_00400F5C;
loc_00400CFF:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x18) == 0) goto loc_00400D1C;
loc_00400D10:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x18) + 0x18) != 0) goto loc_00400D10;
loc_00400D1C:
loc_00400D1F:
    *(uint64_t *)(arg1 + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x18);
    if ((*(uint8_t *)(arg1 + 0x8)) == 0) goto loc_00400FED;
    if ((*(uint64_t *)(arg1 + 0x60)) != 0) goto loc_00400FED;
    Arg1 = *(uint64_t *)(arg1 + 0x38);
    if ((*(uint64_t *)(arg1 + 0x38)) >= (Arg1 + 24)) { Arg1 = Arg1 + 24; }
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    v_stack_m20 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_00400DA9;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) != 332) goto loc_00400E07;
loc_00400D91:
    result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC);
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x9)) == 0) {
        Arg3 = (*(uint64_t *)(arg1 + 0x28)) | (1);
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x38));
        result = *(uint32_t *)(arg1);
        *(uint32_t *)(arg1) = (uint32_t)(result);
        *(void **)(arg1 + 0x38) = Arg1;
        *(uint64_t *)(arg1 + 0x28) = Arg3;
    }
    if ((*(uint64_t *)(arg1 + 0x80)) != 0) goto loc_00400DCC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48))) == 0) goto loc_00400DCC;
    if ((*(uint64_t *)(arg1 + 0x40) + (uint32_t)(*(uint32_t *)(arg1 + 0x48)) * 1) > (Arg1 + 24)) goto loc_00400E16;
    if ((*(uint64_t *)(arg1 + 0x40) + (uint32_t)(*(uint32_t *)(arg1 + 0x48)) * 1) < (*(uint64_t *)(arg1 + 0x40))) goto loc_00400E16;
loc_00400DCC:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0xB0)) == 0) goto loc_00400DE4;
    if (((*(uint64_t *)(arg1 + 0x28)) & (-2)) != 0) goto loc_00400DF5;
loc_00400DE4:
    if (Arg3 == 0) goto loc_00400E1B;
    if ((((uint8_t)(Arg3)) & (3)) == 0) goto loc_00400E2F;
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(arg1 + 0x40), Arg1 + 24, *(uint64_t *)(arg1 + 0x40) + (uint32_t)(*(uint32_t *)(arg1 + 0x48)) * 1, Arg4);
loc_00400DF5:
    v_stack_m28 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00400EA9;
loc_00400E07:
    if (((uint16_t)(result)) != 452) goto loc_00400DA9;
    goto loc_00400D91;
loc_00400E16:
    goto loc_00400DCC;
loc_00400E1B:
    if (Arg4 == 0) goto loc_00400E46;
    Arg2 = Arg1 + 24;
    if (Arg4 < (Arg1 + 24)) { Arg2 = Arg4; }
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2)));
    goto loc_00400E46;
loc_00400E2F:
    if (Arg3 < Arg2) { Arg2 = Arg3; }
    *(uint64_t *)(arg1 + 0x50) = *(uint64_t *)(Arg3);
    goto loc_00400E1B;
loc_00400E46:
    goto loc_00400E53;
loc_00400E53:
loc_00400E57:
    if ((*(uint8_t *)(arg1 + 0x8)) == 0) goto loc_00400E6D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50)))) & (8)) != 0) goto loc_0040108B;
loc_00400E6D:
    result = (uint8_t)(((uint32_t)(Arg5)) & (6));
    if (((uint8_t)(result)) == 4) {
        *(uint64_t *)(arg1 + 0x50) = -1;
    }
    if ((uint32_t)(v_stack_m28) != 0) goto loc_00400F97;
loc_00400E8F:
    if ((*(uint8_t *)(arg1 + 0x9)) != 0) goto loc_00400EDA;
    if (Arg3 == 0) goto loc_00401011;
loc_00400E9E:
    if (sign_flag) goto loc_00401039;
loc_00400EA9:
    if (sign_flag) goto loc_0040110B;
loc_00400EB1:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)(v_stack_m28)));
loc_00400EC8:
    if (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50)) + 0x8) != 0) goto loc_00400CDF;
    goto loc_00400CC0;
loc_00400EDA:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x50))) & (4));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_stack_p10 + 0x10) + 128, Arg2, Arg3, Arg4);
    v_stack_p60 = 0;
    if (1 != 0) goto loc_00401065;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(*(uint64_t *)(v_stack_p10 + 0x10), 1, Arg3, Arg4);
    local_rdi = 0;
loc_00400F33:
    if (v_stack_p60 != 0) goto loc_00400EA9;
    if (0 != 0) goto loc_00400F82;
    if ((*(uint32_t *)(v_stack_p10 + 0x50)) != 0) goto loc_00400F82;
loc_00400F4C:
    *(uint64_t *)(v_stack_p10 + 0x50) = *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x68);
    goto loc_00400E9E;
loc_00400F5C:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10)) == 0) goto loc_00400CFF;
loc_00400F6B:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x68)) == (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10)))) goto loc_00400D1F;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x68) + 0x18) != 0) goto loc_00400F6B;
    goto loc_00400CFF;
loc_00400F82:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x68) + 0x18))) != -2) goto loc_00400E9E;
    if ((*(uint32_t *)(v_stack_p10 + 0x54)) != -1) goto loc_00400E9E;
    goto loc_00400F4C;
loc_00400F97:
    v_stack_p60 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p60;
    result = ObReferenceObjectByHandle(0, 2, *(uint64_t *)(v_rip + 0xBC5BDD), *(uint8_t *)(v_stack_p10 + 0x8));
    *(uint64_t *)(v_stack_p10 + 0x20) = v_stack_p60;
    v_stack_p30 = (uint32_t)(result);
    if (sign_flag) goto loc_00400EA9;
    result = KeResetEvent(v_stack_p60, 2, *(uint64_t *)(v_rip + 0xBC5BDD), *(uint8_t *)(v_stack_p10 + 0x8));
    goto loc_00400E8F;
loc_00400FED:
    if (0 != 0) {
        result = *(uint64_t *)(Arg3);
        *(uint64_t *)(v_stack_p10 + 0x50) = result;
        Arg2 = v_stack_p10 + 24;
    }
    if (*(uint8_t *)(v_stack_p10 + 0x8) == 0) goto loc_00400E57;
    *(uint32_t *)(v_stack_p10 + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(v_stack_p10 + 0x8))));
    goto loc_00400E57;
loc_00401011:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x50)) & (640)) != 0) goto loc_00400E9E;
    goto loc_00401106;
loc_00401027:
    if (*(uint64_t *)(v_stack_p60 + 0x8) != 0) goto loc_00400CDF;
    goto loc_00400CDB;
loc_00401039:
    if (((uint32_t)(*(uint64_t *)(v_stack_p10 + 0x10))) != -1) goto loc_00401048;
    if ((*(uint32_t *)(v_stack_p10 + 0x50)) == -1) goto loc_00400EA9;
loc_00401048:
    if ((*(uint8_t *)(v_stack_p10 + 0x9)) == 0) goto loc_00401106;
    result = IopReleaseFileObjectLock(*(uint64_t *)(v_stack_p10 + 0x10), Arg2, *(uint64_t *)(v_rip + 0xBC5BDD), *(uint8_t *)(v_stack_p10 + 0x8));
    goto loc_0040110B;
loc_00401065:
    Arg3 = ((uint32_t)(local_rsi) != 0) ? 1 : 0;
    v_stack_p20 = v_stack_p60;
    result = IopWaitAndAcquireFileObjectLock((uint32_t)(0xC000000DULL), (uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8)), Arg3, result);
    goto loc_00400F33;
loc_0040108B:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))) + 0x130)) == 0) goto loc_004010B0;
    if (((*(uint32_t *)(v_stack_p10 + 0x48)) & ((uint32_t)(*(uint16_t *)(*(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))) + 0x130) - 1))) != 0) goto loc_00401159;
loc_004010B0:
    if (((*(uint64_t *)(v_stack_p10 + 0x40)) & ((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))) + 0x98)))) != 0) goto loc_00401159;
loc_004010C4:
    if (Arg3 == 0) goto loc_00400E6D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x50)))) == -1) goto loc_0040117D;
loc_004010D9:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x50)))) == -2) goto loc_004011C3;
loc_004010E2:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))) + 0x130)) == 0) goto loc_00400E6D;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))) + 0x130)) - 1);
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x50)))) & ((uint32_t)(result))) == 0) goto loc_00400E6D;
    goto loc_00401106;
loc_004010FF:
    if ((*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x50)) + 0x30)) == 0) goto loc_00401141;
loc_00401106:
loc_0040110B:
    if (*(uint64_t *)(v_stack_p10 + 0x20) != 0) {
        Arg2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_p10 + 0x20), Arg2, v_stack_p10 + 72, *(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))));
        *(uint64_t *)(v_stack_p10 + 0x20) = 0;
    }
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_p10 + 0x10), (uint32_t)(0x746C6644ULL), v_stack_p10 + 72, *(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))));
    *(uint64_t *)(v_stack_p10 + 0x10) = 0;
    goto loc_00400EB1;
loc_00401141:
    if ((uint32_t)(0xC000000DULL) != 0) goto loc_00401106;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x10) + 0xB0)) == ((uint32_t)(0xC000000DULL))) goto loc_00400C64;
    goto loc_00401106;
loc_00401159:
    if ((uint16_t)((uint32_t)(0x746C6644ULL)) == 0) goto loc_0040116A;
    Arg2 = 0;
    if (0 != 0) goto loc_00401106;
loc_0040116A:
    if (((*(uint64_t *)(v_stack_p10 + 0x40)) & ((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))) + 0x98)))) == 0) goto loc_004010C4;
    goto loc_00401106;
loc_0040117D:
    if ((*(uint32_t *)(v_stack_p10 + 0x54)) != -1) goto loc_004010D9;
    goto loc_00400E6D;
loc_0040118C:
    if (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))) + 0x98))) == 0) goto loc_00400C71;
    if ((*(uint32_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x8))) + 0x98))) + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x48))))) goto loc_00400C71;
    goto loc_00401106;
loc_004011A9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x50)))) & (8)) != 0) goto loc_00400C7D;
    goto loc_0040110B;
loc_004011C3:
    if ((*(uint32_t *)(v_stack_p10 + 0x54)) != -1) goto loc_004010E2;
    if ((*(uint8_t *)(v_stack_p10 + 0x9)) == 0) goto loc_004010E2;
    goto loc_00400E6D;
loc_004011DC:
    if (sign_flag) goto loc_00400CA3;
    goto loc_00400CA5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x8` | `8` | `W` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0x9` | `8` | `W` |
| `Arg1` | `+ 0xA` | `8` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `W` |
| `Arg1` | `+ 0x54` | `32` | `R` |
| `Arg1` | `+ 0x58` | `32` | `W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00400C30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
