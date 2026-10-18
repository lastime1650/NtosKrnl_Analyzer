# AlpcpReceiveMessage

- RVA: `0x00897ED0`–`0x0089850E` (길이 `1,598` bytes)
- VA: `0x0000000140897ED0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E3D4`
- 디코드: `380`개 명령, `1,598/1,598` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00897FB1` → [ExRaiseDatatypeMisalignment](ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00898158` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x008981AA` → [AlpcpReceiveMessagePort](AlpcpReceiveMessagePort_function_00896B40.md) (function, `0x00896B40`)
- `0x008982B0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008982D2` → [AlpcpExposeAttributes](AlpcpExposeAttributes_function_00897630.md) (function, `0x00897630`)
- `0x008982DF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00898301` → [AlpcpGetDataFromUserVaSafe](../92/AlpcpGetDataFromUserVaSafe_function_00922908.md) (function, `0x00922908`)
- `0x008983A6` → [AlpcpGetDataFromMessage](../92/AlpcpGetDataFromMessage_function_00922958.md) (function, `0x00922958`)
- `0x008983D6` → [AlpcpReturnMessageOnInsufficientBuffer](../A2/AlpcpReturnMessageOnInsufficientBuffer_function_00A2EF7C.md) (function, `0x00A2EF7C`)
- `0x00898408` → [AlpcpExposeCapturedContextAttribute](../A4/AlpcpExposeCapturedContextAttribute_function_00A4A72C.md) (function, `0x00A4A72C`)
- `0x00898460` → [AlpcpUnlockMessage](AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x008984A2` → [AlpcpCancelMessage](AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x00898500` → [AlpcpReceiveDirectMessagePort](AlpcpReceiveDirectMessagePort_function_008950B4.md) (function, `0x008950B4`)

### Direct callers
- [sub_00868100](../86/Unknown_function_00868100.md) at `0x00868181`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008982B0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008982DF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00897ED0  48 8B C4                        mov rax, rsp
00897ED3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00897ED7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00897EDB  48 89 48 08                     mov qword ptr [rax + 8], rcx
00897EDF  57                              push rdi
00897EE0  41 54                           push r12
00897EE2  41 55                           push r13
00897EE4  41 56                           push r14
00897EE6  41 57                           push r15
00897EE8  48 81 EC B0 00 00 00            sub rsp, 0xb0
00897EEF  4D 8B E1                        mov r12, r9
00897EF2  4D 8B F8                        mov r15, r8
00897EF5  48 8B FA                        mov rdi, rdx
00897EF8  4C 8B D1                        mov r10, rcx
00897EFB  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00897EFF  33 F6                           xor esi, esi
00897F01  48 89 70 88                     mov qword ptr [rax - 0x78], rsi
00897F05  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00897F09  48 89 70 80                     mov qword ptr [rax - 0x80], rsi
00897F0D  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
00897F16  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
00897F1E  8B 51 30                        mov edx, dword ptr [rcx + 0x30]
00897F21  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00897F25  48 8B 01                        mov rax, qword ptr [rcx]
00897F28  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00897F2D  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00897F35  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00897F3E  44 0F B6 98 32 02 00 00         movzx r11d, byte ptr [rax + 0x232]
00897F46  44 88 5C 24 30                  mov byte ptr [rsp + 0x30], r11b
00897F4B  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00897F50  49 C7 C5 FF FF FF FF            mov r13, 0xffffffffffffffff
00897F57  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
00897F5C  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00897F60  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00897F64  45 84 DB                        test r11b, r11b
00897F67  0F 84 3C 05 00 00               je 0x1408984a9
00897F6D  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00897F77  48 39 B4 24 00 01 00 00         cmp qword ptr [rsp + 0x100], rsi
00897F7F  74 20                           je 0x140897fa1
00897F81  48 8B C3                        mov rax, rbx
00897F84  4C 3B C3                        cmp r8, rbx
00897F87  49 0F 42 C0                     cmovb rax, r8
00897F8B  90                              nop
00897F8C  48 8B 00                        mov rax, qword ptr [rax]
00897F8F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00897F94  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00897F99  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00897FA1  44 8B C2                        mov r8d, edx
00897FA4  41 81 E0 00 00 00 C0            and r8d, 0xc0000000
00897FAB  40 F6 C7 03                     test dil, 3
00897FAF  74 06                           je 0x140897fb7
00897FB1  E8 1A 20 00 00                  call 0x140899fd0
00897FB6  CC                              int3
00897FB7  41 B9 00 00 00 80               mov r9d, 0x80000000
00897FBD  48 8B CB                        mov rcx, rbx
00897FC0  45 3B C1                        cmp r8d, r9d
00897FC3  0F 84 26 01 00 00               je 0x1408980ef
00897FC9  48 3B FB                        cmp rdi, rbx
00897FCC  48 0F 42 CF                     cmovb rcx, rdi
00897FD0  0F B6 01                        movzx eax, byte ptr [rcx]
00897FD3  88 01                           mov byte ptr [rcx], al
00897FD5  0F B6 41 27                     movzx eax, byte ptr [rcx + 0x27]
00897FD9  88 41 27                        mov byte ptr [rcx + 0x27], al
00897FDC  44 8B F2                        mov r14d, edx
00897FDF  41 81 E6 00 00 00 01            and r14d, 0x1000000
00897FE6  0F 85 EC 00 00 00               jne 0x1408980d8
00897FEC  4D 85 E4                        test r12, r12
00897FEF  0F 84 7B 01 00 00               je 0x140898170
00897FF5  C6 44 24 48 01                  mov byte ptr [rsp + 0x48], 1
00897FFA  48 8B C3                        mov rax, rbx
00897FFD  4C 3B E3                        cmp r12, rbx
00898000  49 0F 42 C4                     cmovb rax, r12
00898004  90                              nop
00898005  44 8B 28                        mov r13d, dword ptr [rax]
00898008  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
0089800D  41 8B CD                        mov ecx, r13d
00898010  C1 F9 1F                        sar ecx, 0x1f
00898013  45 3B C1                        cmp r8d, r9d
00898016  0F 84 EB 00 00 00               je 0x140898107
0089801C  83 E1 18                        and ecx, 0x18
0089801F  83 C1 08                        add ecx, 8
00898022  41 0F BA E5 1E                  bt r13d, 0x1e
00898027  8D 41 20                        lea eax, [rcx + 0x20]
0089802A  0F 43 C1                        cmovae eax, ecx
0089802D  41 0F BA E5 1D                  bt r13d, 0x1d
00898032  8D 48 20                        lea ecx, [rax + 0x20]
00898035  0F 43 C8                        cmovae ecx, eax
00898038  41 0F BA E5 1C                  bt r13d, 0x1c
0089803D  8D 51 18                        lea edx, [rcx + 0x18]
00898040  0F 43 D1                        cmovae edx, ecx
00898043  41 0F BA E5 1B                  bt r13d, 0x1b
00898048  8D 42 18                        lea eax, [rdx + 0x18]
0089804B  0F 43 C2                        cmovae eax, edx
0089804E  41 F7 C5 00 00 00 04            test r13d, 0x4000000
00898055  8D 48 08                        lea ecx, [rax + 8]
00898058  41 B8 08 00 00 00               mov r8d, 8
0089805E  0F 44 C8                        cmove ecx, eax
00898061  8D 41 08                        lea eax, [rcx + 8]
00898064  41 0F BA E5 19                  bt r13d, 0x19
00898069  0F 43 C1                        cmovae eax, ecx
0089806C  8B D0                           mov edx, eax
0089806E  48 81 FA 00 10 00 00            cmp rdx, 0x1000
00898075  0F 83 DA 00 00 00               jae 0x140898155
0089807B  41 8D 48 FF                     lea ecx, [r8 - 1]
0089807F  49 85 CC                        test r12, rcx
00898082  0F 85 29 FF FF FF               jne 0x140897fb1
00898088  48 8B CB                        mov rcx, rbx
0089808B  4C 3B E3                        cmp r12, rbx
0089808E  49 0F 42 CC                     cmovb rcx, r12
00898092  0F B6 01                        movzx eax, byte ptr [rcx]
00898095  88 01                           mov byte ptr [rcx], al
00898097  0F B6 44 11 FF                  movzx eax, byte ptr [rcx + rdx - 1]
0089809C  88 44 11 FF                     mov byte ptr [rcx + rdx - 1], al
008980A0  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
008980A5  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
008980A9  4D 85 FF                        test r15, r15
008980AC  74 25                           je 0x1408980d3
008980AE  48 8B C3                        mov rax, rbx
008980B1  4C 3B FB                        cmp r15, rbx
008980B4  49 0F 42 C7                     cmovb rax, r15
008980B8  90                              nop
008980B9  48 8B 00                        mov rax, qword ptr [rax]
008980BC  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008980C1  49 0F 42 DF                     cmovb rbx, r15
008980C5  48 8B 03                        mov rax, qword ptr [rbx]
008980C8  48 89 03                        mov qword ptr [rbx], rax
008980CB  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
008980CF  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
008980D3  E9 AC 00 00 00                  jmp 0x140898184
008980D8  85 D2                           test edx, edx
008980DA  78 67                           js 0x140898143
008980DC  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008980DF  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008980E3  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
008980E6  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
008980EA  E9 FD FE FF FF                  jmp 0x140897fec
008980EF  48 3B FB                        cmp rdi, rbx
008980F2  48 0F 42 CF                     cmovb rcx, rdi
008980F6  0F B6 01                        movzx eax, byte ptr [rcx]
008980F9  88 01                           mov byte ptr [rcx], al
008980FB  0F B6 41 17                     movzx eax, byte ptr [rcx + 0x17]
008980FF  88 41 17                        mov byte ptr [rcx + 0x17], al
00898102  E9 D5 FE FF FF                  jmp 0x140897fdc
00898107  83 E1 0C                        and ecx, 0xc
0089810A  83 C1 08                        add ecx, 8
0089810D  41 0F BA E5 1E                  bt r13d, 0x1e
00898112  8D 41 10                        lea eax, [rcx + 0x10]
00898115  0F 43 C1                        cmovae eax, ecx
00898118  41 0F BA E5 1D                  bt r13d, 0x1d
0089811D  8D 48 14                        lea ecx, [rax + 0x14]
00898120  0F 43 C8                        cmovae ecx, eax
00898123  41 0F BA E5 1C                  bt r13d, 0x1c
00898128  8D 41 10                        lea eax, [rcx + 0x10]
0089812B  0F 43 C1                        cmovae eax, ecx
0089812E  41 F7 C5 00 00 00 08            test r13d, 0x8000000
00898135  8D 48 18                        lea ecx, [rax + 0x18]
00898138  41 B8 04 00 00 00               mov r8d, 4
0089813E  E9 1B FF FF FF                  jmp 0x14089805e
00898143  0F BA E2 1E                     bt edx, 0x1e
00898147  72 93                           jb 0x1408980dc
00898149  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0089814C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00898150  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
00898153  EB 91                           jmp 0x1408980e6
00898155  49 8B CC                        mov rcx, r12
00898158  E8 63 10 05 00                  call 0x1408e91c0
0089815D  4C 8B 94 24 E0 00 00 00         mov r10, qword ptr [rsp + 0xe0]
00898165  44 0F B6 5C 24 30               movzx r11d, byte ptr [rsp + 0x30]
0089816B  E9 30 FF FF FF                  jmp 0x1408980a0
00898170  8B CE                           mov ecx, esi
00898172  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00898176  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0089817A  E9 2A FF FF FF                  jmp 0x1408980a9
0089817F  E9 E4 02 00 00                  jmp 0x140898468
00898184  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00898189  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0089818D  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00898192  49 8B CA                        mov rcx, r10
00898195  45 85 F6                        test r14d, r14d
00898198  0F 85 59 03 00 00               jne 0x1408984f7
0089819E  4C 8B 84 24 00 01 00 00         mov r8, qword ptr [rsp + 0x100]
008981A6  41 0F B6 D3                     movzx edx, r11b
008981AA  E8 91 E9 FF FF                  call 0x140896b40
008981AF  44 8B F0                        mov r14d, eax
008981B2  85 C0                           test eax, eax
008981B4  0F 85 AB 02 00 00               jne 0x140898465
008981BA  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
008981BE  81 E1 00 00 00 C0               and ecx, 0xc0000000
008981C4  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
008981C9  B8 18 00 00 00                  mov eax, 0x18
008981CE  BA 00 00 00 80                  mov edx, 0x80000000
008981D3  41 B8 28 00 00 00               mov r8d, 0x28
008981D9  3B CA                           cmp ecx, edx
008981DB  66 41 0F 45 C0                  cmovne ax, r8w
008981E0  66 03 83 F0 00 00 00            add ax, word ptr [rbx + 0xf0]
008981E7  4D 85 FF                        test r15, r15
008981EA  74 14                           je 0x140898200
008981EC  0F B7 C0                        movzx eax, ax
008981EF  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
008981F7  49 3B C5                        cmp rax, r13
008981FA  0F 87 B0 01 00 00               ja 0x1408983b0
00898200  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00898208  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
0089820F  89 B4 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], esi
00898216  3B CA                           cmp ecx, edx
00898218  0F 84 F3 00 00 00               je 0x140898311
0089821E  0F 10 83 F0 00 00 00            movups xmm0, xmmword ptr [rbx + 0xf0]
00898225  0F 11 07                        movups xmmword ptr [rdi], xmm0
00898228  0F 10 8B 00 01 00 00            movups xmm1, xmmword ptr [rbx + 0x100]
0089822F  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00898233  F2 0F 10 83 10 01 00 00         movsd xmm0, qword ptr [rbx + 0x110]
0089823B  F2 0F 11 47 20                  movsd qword ptr [rdi + 0x20], xmm0
00898240  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00898245  41 F7 85 00 01 00 00 00 10 00 00  test dword ptr [r13 + 0x100], 0x1000
00898250  74 13                           je 0x140898265
00898252  0F B7 83 F4 00 00 00            movzx eax, word ptr [rbx + 0xf4]
00898259  B9 0F C0 FF FF                  mov ecx, 0xffffc00f
0089825E  66 23 C1                        and ax, cx
00898261  66 89 47 04                     mov word ptr [rdi + 4], ax
00898265  0F B7 83 F2 00 00 00            movzx eax, word ptr [rbx + 0xf2]
0089826C  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00898273  48 8D 4F 28                     lea rcx, [rdi + 0x28]
00898277  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
0089827F  48 83 BB B0 00 00 00 00         cmp qword ptr [rbx + 0xb0], 0
00898287  75 72                           jne 0x1408982fb
00898289  4C 8B 7B 60                     mov r15, qword ptr [rbx + 0x60]
0089828D  4D 85 FF                        test r15, r15
00898290  75 76                           jne 0x140898308
00898292  41 BF 00 02 00 00               mov r15d, 0x200
00898298  0F B7 83 F0 00 00 00            movzx eax, word ptr [rbx + 0xf0]
0089829F  8B F8                           mov edi, eax
008982A1  48 8D 93 18 01 00 00            lea rdx, [rbx + 0x118]
008982A8  49 3B C7                        cmp rax, r15
008982AB  77 2F                           ja 0x1408982dc
008982AD  4C 8B C7                        mov r8, rdi
008982B0  E8 8B E5 E2 FF                  call 0x1406c6840
008982B5  4D 85 E4                        test r12, r12
008982B8  0F 84 5E 01 00 00               je 0x14089841c
008982BE  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008982C3  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
008982C8  4C 8B C3                        mov r8, rbx
008982CB  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
008982CF  49 8B CD                        mov rcx, r13
008982D2  E8 59 F3 FF FF                  call 0x140897630
008982D7  E9 40 01 00 00                  jmp 0x14089841c
008982DC  4D 8B C7                        mov r8, r15
008982DF  E8 5C E5 E2 FF                  call 0x1406c6840
008982E4  49 2B FF                        sub rdi, r15
008982E7  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
008982EF  49 03 CF                        add rcx, r15
008982F2  48 8B 93 E0 00 00 00            mov rdx, qword ptr [rbx + 0xe0]
008982F9  EB B2                           jmp 0x1408982ad
008982FB  48 8B D1                        mov rdx, rcx
008982FE  48 8B CB                        mov rcx, rbx
00898301  E8 02 A6 08 00                  call 0x140922908
00898306  EB AD                           jmp 0x1408982b5
00898308  4D 8B 7F 20                     mov r15, qword ptr [r15 + 0x20]
0089830C  4D 2B F8                        sub r15, r8
0089830F  EB 87                           jmp 0x140898298
00898311  0F B7 83 F0 00 00 00            movzx eax, word ptr [rbx + 0xf0]
00898318  66 89 07                        mov word ptr [rdi], ax
0089831B  0F B7 83 F0 00 00 00            movzx eax, word ptr [rbx + 0xf0]
00898322  83 C0 18                        add eax, 0x18
00898325  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
0089832C  66 89 47 02                     mov word ptr [rdi + 2], ax
00898330  0F B7 83 F6 00 00 00            movzx eax, word ptr [rbx + 0xf6]
00898337  66 85 C0                        test ax, ax
0089833A  0F 85 CF 00 00 00               jne 0x14089840f
00898340  66 89 77 06                     mov word ptr [rdi + 6], si
00898344  BA 00 10 00 00                  mov edx, 0x1000
00898349  66 0B 93 F4 00 00 00            or dx, word ptr [rbx + 0xf4]
00898350  66 89 57 04                     mov word ptr [rdi + 4], dx
00898354  8B 83 F8 00 00 00               mov eax, dword ptr [rbx + 0xf8]
0089835A  89 47 08                        mov dword ptr [rdi + 8], eax
0089835D  8B 83 00 01 00 00               mov eax, dword ptr [rbx + 0x100]
00898363  89 47 0C                        mov dword ptr [rdi + 0xc], eax
00898366  8B 83 08 01 00 00               mov eax, dword ptr [rbx + 0x108]
0089836C  89 47 10                        mov dword ptr [rdi + 0x10], eax
0089836F  8B 83 10 01 00 00               mov eax, dword ptr [rbx + 0x110]
00898375  89 47 14                        mov dword ptr [rdi + 0x14], eax
00898378  8B 83 10 01 00 00               mov eax, dword ptr [rbx + 0x110]
0089837E  89 47 14                        mov dword ptr [rdi + 0x14], eax
00898381  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00898386  41 F7 85 00 01 00 00 00 10 00 00  test dword ptr [r13 + 0x100], 0x1000
00898391  74 0C                           je 0x14089839f
00898393  B9 0F C0 FF FF                  mov ecx, 0xffffc00f
00898398  66 23 D1                        and dx, cx
0089839B  66 89 57 04                     mov word ptr [rdi + 4], dx
0089839F  48 8D 57 18                     lea rdx, [rdi + 0x18]
008983A3  48 8B CB                        mov rcx, rbx
008983A6  E8 AD A5 08 00                  call 0x140922958
008983AB  E9 05 FF FF FF                  jmp 0x1408982b5
008983B0  0F 57 C0                        xorps xmm0, xmm0
008983B3  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
008983BB  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
008983C3  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
008983CB  48 8B D3                        mov rdx, rbx
008983CE  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
008983D3  49 8B CD                        mov rcx, r13
008983D6  E8 A1 6B 19 00                  call 0x140a2ef7c
008983DB  44 8B F0                        mov r14d, eax
008983DE  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
008983E2  3D 23 00 00 C0                  cmp eax, 0xc0000023
008983E7  75 33                           jne 0x14089841c
008983E9  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
008983F1  49 89 07                        mov qword ptr [r15], rax
008983F4  4D 8B CC                        mov r9, r12
008983F7  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
008983FC  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00898404  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
00898408  E8 1F 23 1B 00                  call 0x140a4a72c
0089840D  EB 0D                           jmp 0x14089841c
0089840F  66 83 E8 10                     sub ax, 0x10
00898413  66 89 47 06                     mov word ptr [rdi + 6], ax
00898417  E9 28 FF FF FF                  jmp 0x140898344
0089841C  B9 00 00 00 80                  mov ecx, 0x80000000
00898421  EB 1B                           jmp 0x14089843e
00898423  44 8B F0                        mov r14d, eax
00898426  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0089842A  33 F6                           xor esi, esi
0089842C  B9 00 00 00 80                  mov ecx, 0x80000000
00898431  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00898436  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
0089843E  41 81 FE 23 00 00 C0            cmp r14d, 0xc0000023
00898445  74 0E                           je 0x140898455
00898447  4C 39 6B 40                     cmp qword ptr [rbx + 0x40], r13
0089844B  75 08                           jne 0x140898455
0089844D  48 89 73 40                     mov qword ptr [rbx + 0x40], rsi
00898451  48 89 73 38                     mov qword ptr [rbx + 0x38], rsi
00898455  41 8D 04 0E                     lea eax, [r14 + rcx]
00898459  85 C1                           test ecx, eax
0089845B  74 29                           je 0x140898486
0089845D  48 8B CB                        mov rcx, rbx
00898460  E8 7B F6 FF FF                  call 0x140897ae0
00898465  41 8B C6                        mov eax, r14d
00898468  4C 8D 9C 24 B0 00 00 00         lea r11, [rsp + 0xb0]
00898470  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00898474  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00898478  49 8B E3                        mov rsp, r11
0089847B  41 5F                           pop r15
0089847D  41 5E                           pop r14
0089847F  41 5D                           pop r13
00898481  41 5C                           pop r12
00898483  5F                              pop rdi
00898484  C3                              ret
00898485  CC                              int3
00898486  41 81 FE 23 00 00 C0            cmp r14d, 0xc0000023
0089848D  74 CE                           je 0x14089845d
0089848F  48 89 B3 C8 00 00 00            mov qword ptr [rbx + 0xc8], rsi
00898496  41 B8 00 00 01 00               mov r8d, 0x10000
0089849C  48 8B D3                        mov rdx, rbx
0089849F  49 8B CD                        mov rcx, r13
008984A2  E8 79 BC FF FF                  call 0x140894120
008984A7  EB BC                           jmp 0x140898465
008984A9  44 8B F2                        mov r14d, edx
008984AC  41 81 E6 00 00 00 01            and r14d, 0x1000000
008984B3  74 0E                           je 0x1408984c3
008984B5  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008984B8  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008984BC  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
008984BF  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
008984C3  4D 85 E4                        test r12, r12
008984C6  74 42                           je 0x14089850a
008984C8  41 8B 0C 24                     mov ecx, dword ptr [r12]
008984CC  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
008984D0  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
008984D4  4D 85 FF                        test r15, r15
008984D7  74 08                           je 0x1408984e1
008984D9  4D 8B 2F                        mov r13, qword ptr [r15]
008984DC  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
008984E1  41 F7 41 74 00 04 00 00         test dword ptr [r9 + 0x74], 0x400
008984E9  0F 84 9A FC FF FF               je 0x140898189
008984EF  41 B3 01                        mov r11b, 1
008984F2  E9 92 FC FF FF                  jmp 0x140898189
008984F7  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
008984FC  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
00898500  E8 AF CB FF FF                  call 0x1408950b4
00898505  E9 A5 FC FF FF                  jmp 0x1408981af
0089850A  8B CE                           mov ecx, esi
0089850C  EB BE                           jmp 0x1408984cc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpReceiveMessage(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int8 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA8;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    v_stack_mA0 = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    v_stack_m68 = *(unsigned __int64 *)(a1);
    v_stack_m50 = *(unsigned __int64 *)(a1);
    v_stack_mA8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m60 = 0;
    v_stack_m80 = -1;
    v_stack_m98 = 0;
    v_stack_m9C = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008984A9;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (a5 != 0) {
        result = v_rbx;
        if ((*(unsigned __int64 *)(v_rsp + 40)) < v_rbx) { result = *(unsigned __int64 *)(v_rsp + 40); }
        result = *(unsigned __int64 *)(result);
        v_stack_m60 = result;
        result = v_stack_m60;
        v_stack_p28 = result;
    }
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (0xC0000000ULL));
    if ((((unsigned __int8)(a2)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, (unsigned int)(*(unsigned int *)(a1 + 48)), a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    }
    if (((unsigned int)(a3)) == ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_008980EF;
    a1 = v_rbx;
    if (a2 < v_rbx) { a1 = a2; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 39) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 39));
loc_00897FDC:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (0x1000000ULL));
    if (condition_is_not_equal) goto loc_008980D8;
loc_00897FEC:
    if (a4 == 0) goto loc_00898170;
    v_stack_m90 = 1;
    result = v_rbx;
    if (a4 < v_rbx) { result = a4; }
    v_stack_mA4 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) >> (31));
    if (((unsigned int)(a3)) == ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_00898107;
    a1 = (unsigned int)((a1) & (24));
    a1 = (unsigned int)((a1) + (8));
    result = a1 + 32;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    a1 = result + 32;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(result); }
    a2 = a1 + 24;
    if (condition_is_above_or_equal) { a2 = (unsigned int)(a1); }
    result = a2 + 24;
    if (condition_is_above_or_equal) { result = (unsigned int)(a2); }
loc_0089805E:
    a1 = result + 8;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result)))) & (0x4000000ULL)) == 0) { a1 = (unsigned int)(result); }
    result = a1 + 8;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    if (((unsigned int)((unsigned int)(result))) >= 0x1000ULL) goto loc_00898155;
    if (((a4) & (8 - 1)) != 0) goto loc_00897FB1;
    a1 = v_rbx;
    if (a4 < v_rbx) { a1 = a4; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + (unsigned int)((unsigned int)(result)) * 1 - 1) = (unsigned __int8)(*(unsigned __int8 *)(a1 + (unsigned int)((unsigned int)(result)) * 1 - 1));
loc_008980A0:
    v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
loc_008980A9:
    result = *(unsigned __int8 *)(a1 + (unsigned int)((unsigned int)(result)) * 1 - 1);
    if (a3 != 0) {
        result = v_rbx;
        if (a3 < v_rbx) { result = a3; }
        result = *(unsigned __int64 *)(result);
        v_stack_m80 = result;
        if (a3 < v_rbx) { v_rbx = a3; }
        result = *(unsigned __int64 *)(v_rbx);
        *(unsigned __int64 *)(v_rbx) = result;
        a1 = v_stack_mA0;
        v_stack_mA4 = (unsigned int)(a1);
    }
    goto loc_00898184;
loc_008980D8:
    if (sign_flag) goto loc_00898143;
loc_008980DC:
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 24)));
loc_008980E6:
    v_stack_m9C = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)));
    goto loc_00897FEC;
loc_008980EF:
    if (a2 < v_rbx) { a1 = a2; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 23) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 23));
    goto loc_00897FDC;
loc_00898107:
    a1 = (unsigned int)((a1) & (12));
    a1 = (unsigned int)((a1) + (8));
    result = a1 + 16;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    a1 = result + 20;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(result); }
    result = a1 + 16;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    goto loc_0089805E;
loc_00898143:
    if (condition_is_below) goto loc_008980DC;
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)));
    goto loc_008980E6;
loc_00898155:
    result = ProbeForWrite(a4, (unsigned int)((unsigned int)(result)), 4, (unsigned int)(0x80000000ULL));
    goto loc_008980A0;
loc_00898170:
    v_stack_mA4 = 0;
    v_stack_mA0 = 0;
    goto loc_008980A9;
loc_00898184:
loc_00898189:
    v_stack_mB8 = 0;
    if ((unsigned int)(v_r14) != 0) goto loc_008984F7;
    result = AlpcpReceiveMessagePort(v_stack_p8, (unsigned __int8)(v_stack_mA8), a5, v_stack_m78);
loc_008981AF:
    if ((unsigned int)(result) != 0) goto loc_00898465;
    a1 = (unsigned int)(((unsigned int)(v_stack_m88)) & (0xC0000000ULL));
    result = 24;
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(0x80000000ULL)))) { result = 40; }
    result = (unsigned __int16)((result) + (*(unsigned __int16 *)(v_stack_m78 + 240)));
    if (a3 == 0) goto loc_00898200;
    v_stack_p8 = (unsigned __int16)(result);
    if (((unsigned __int16)(result)) > v_stack_m80) goto loc_008983B0;
loc_00898200:
    *(unsigned __int64 *)(v_stack_m78 + 200) = v_stack_m58;
    v_stack_p8 = 0;
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_00898311;
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int64 *)(a2 + 16) = v_xmm1;
    *(unsigned __int64 *)(a2 + 32) = v_xmm0;
    result = v_stack_m58;
    if (((*(unsigned int *)(v_stack_m68 + 256)) & (0x1000ULL)) != 0) {
        result = *(unsigned __int16 *)(v_stack_m78 + 244);
        a1 = 0xFFFFC00FULL;
        result = (unsigned __int16)((result) & ((unsigned __int16)(a1)));
        *(unsigned __int16 *)(a2 + 4) = (unsigned __int16)(result);
    }
    v_stack_p8 = (unsigned int)(*(unsigned __int16 *)(v_stack_m78 + 242));
    v_stack_p8 = a2 + 40;
    if ((*(unsigned __int64 *)(v_stack_m78 + 176)) != 0) goto loc_008982FB;
    if (*(unsigned __int64 *)(v_stack_m78 + 96) != 0) goto loc_00898308;
loc_00898298:
    if ((*(unsigned __int16 *)(v_stack_m78 + 240)) > 512) goto loc_008982DC;
loc_008982AD:
    result = memcpy(a2 + 40, v_stack_m78 + 280, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m78 + 240))), v_stack_m78);
loc_008982B5:
    if (a4 == 0) goto loc_0089841C;
    v_stack_mB8 = a4;
    result = AlpcpExposeAttributes(v_stack_m68, (unsigned int)(v_stack_m88), v_stack_m78, (unsigned int)(v_stack_mA4));
    goto loc_0089841C;
loc_008982DC:
    result = memcpy(v_stack_m68, (unsigned int)(v_stack_m88), 512, (unsigned int)(v_stack_mA4));
    v_rdi = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m78 + 240)))) - (512);
    a1 = (v_stack_p8) + (512);
    goto loc_008982AD;
loc_008982FB:
    result = AlpcpGetDataFromUserVaSafe(v_stack_m78, a1, 512, (unsigned int)(v_stack_mA4));
    goto loc_008982B5;
loc_00898308:
    v_r15 = (*(unsigned __int64 *)(512 + 32)) - (512);
    goto loc_00898298;
loc_00898311:
    *(unsigned __int16 *)(v_rdi) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m78 + 240));
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m78 + 240)) + (24));
    v_stack_p8 = (unsigned int)(result);
    *(unsigned __int16 *)(v_rdi + 2) = (unsigned __int16)(result);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m78 + 246)) != 0) goto loc_0089840F;
    *(unsigned __int16 *)(v_rdi + 6) = 0;
loc_00898344:
    a2 = (unsigned __int16)(((unsigned int)(0x1000ULL)) | (*(unsigned __int16 *)(v_stack_m78 + 244)));
    *(unsigned __int16 *)(v_rdi + 4) = (unsigned __int16)(a2);
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m78 + 248)));
    *(unsigned int *)(v_rdi + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m78 + 256)));
    *(unsigned int *)(v_rdi + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m78 + 264)));
    *(unsigned int *)(v_rdi + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m78 + 272)));
    *(unsigned int *)(v_rdi + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m78 + 272)));
    if (((*(unsigned int *)(v_stack_m68 + 256)) & (0x1000ULL)) != 0) {
        a1 = 0xFFFFC00FULL;
        a2 = (unsigned __int16)((a2) & ((unsigned __int16)(a1)));
        *(unsigned __int16 *)(v_rdi + 4) = (unsigned __int16)(a2);
    }
    result = AlpcpGetDataFromMessage(v_stack_m78, v_rdi + 24, 512, (unsigned int)(v_stack_mA4));
    goto loc_008982B5;
loc_008983B0:
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = AlpcpReturnMessageOnInsufficientBuffer(v_stack_m68, v_stack_m78, v_stack_m48, (unsigned int)(v_stack_mA4));
    v_stack_m70 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_0089841C;
    *(unsigned __int64 *)(v_r15) = v_stack_p8;
    result = AlpcpExposeCapturedContextAttribute((unsigned int)(v_stack_m88), v_stack_m48, (unsigned int)(v_stack_mA4), a4);
    goto loc_0089841C;
loc_0089840F:
    result = (unsigned __int16)((result) - (16));
    *(unsigned __int16 *)(v_rdi + 6) = (unsigned __int16)(result);
    goto loc_00898344;
loc_0089841C:
    goto loc_0089843E;
loc_0089843E:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000023ULL) goto loc_00898455;
    if ((*(unsigned __int64 *)(v_stack_m78 + 64)) == v_stack_m68) {
        *(unsigned __int64 *)(v_stack_m78 + 64) = 0;
        *(unsigned __int64 *)(v_stack_m78 + 56) = 0;
    }
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) == 0) goto loc_00898486;
loc_0089845D:
    result = AlpcpUnlockMessage(v_stack_m78, v_stack_m48, (unsigned int)(v_stack_mA4), a4);
loc_00898465:
loc_00898468:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00898486:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000023ULL) goto loc_0089845D;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 200) = *(unsigned __int64 *)(v_stack_m28 + 64);
    result = AlpcpCancelMessage(v_stack_m68, *(unsigned __int64 *)(v_stack_m28 + 56), (unsigned int)(0x10000ULL), a4);
    goto loc_00898465;
loc_008984A9:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) & (0x1000000ULL));
    if (!(condition_is_equal)) {
        result = *(unsigned int *)(v_rdi + 24);
        v_stack_m70 = (unsigned int)(result);
        result = *(unsigned int *)(v_rdi + 32);
        v_stack_m74 = (unsigned int)(result);
    }
    if (a4 == 0) goto loc_0089850A;
loc_008984CC:
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    v_stack_m7C = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    v_r13 = v_stack_m68;
    if (v_r15 != 0) {
        v_r13 = *(unsigned __int64 *)(v_r15);
        v_stack_m58 = v_r13;
    }
    if (((*(unsigned int *)(a4 + 116)) & (0x400ULL)) == 0) goto loc_00898189;
    goto loc_00898189;
loc_008984F7:
    result = AlpcpReceiveDirectMessagePort((unsigned int)(*(unsigned int *)(a4)), (unsigned int)(v_stack_m70), (unsigned int)(v_stack_m74), a4);
    goto loc_008981AF;
loc_0089850A:
    goto loc_008984CC;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpReceiveMessage(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint8_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA8;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    v_stack_mA0 = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    v_stack_m68 = *(uint64_t *)(arg1);
    v_stack_m50 = *(uint64_t *)(arg1);
    v_stack_mA8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m60 = 0;
    v_stack_m80 = -1;
    v_stack_m98 = 0;
    v_stack_m9C = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008984A9;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (Arg5 != 0) {
        result = local_rbx;
        if ((*(uint64_t *)(local_rsp + 0x28)) < local_rbx) { result = *(uint64_t *)(local_rsp + 0x28); }
        result = *(uint64_t *)(result);
        v_stack_m60 = result;
        result = v_stack_m60;
        v_stack_p28 = result;
    }
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (0xC0000000ULL));
    if ((((uint8_t)(Arg2)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    }
    if (((uint32_t)(Arg3)) == ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_008980EF;
    Arg1 = local_rbx;
    if (Arg2 < local_rbx) { Arg1 = Arg2; }
    *(uint8_t *)(arg1) = (uint8_t)(*(uint8_t *)(arg1));
    *(uint8_t *)(arg1 + 0x27) = (uint8_t)(*(uint8_t *)(arg1 + 0x27));
loc_00897FDC:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (0x1000000ULL));
    if (condition_is_not_equal) goto loc_008980D8;
loc_00897FEC:
    if (Arg4 == 0) goto loc_00898170;
    v_stack_m90 = 1;
    result = local_rbx;
    if (Arg4 < local_rbx) { result = Arg4; }
    v_stack_mA4 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) >> (31));
    if (((uint32_t)(Arg3)) == ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_00898107;
    Arg1 = (uint32_t)((Arg1) & (24));
    Arg1 = (uint32_t)((Arg1) + (8));
    result = Arg1 + 32;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    Arg1 = result + 32;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(result); }
    Arg2 = Arg1 + 24;
    if (condition_is_above_or_equal) { Arg2 = (uint32_t)(Arg1); }
    result = Arg2 + 24;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg2); }
loc_0089805E:
    Arg1 = result + 8;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result)))) & (0x4000000ULL)) == 0) { Arg1 = (uint32_t)(result); }
    result = Arg1 + 8;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    if (((uint32_t)((uint32_t)(result))) >= 0x1000ULL) goto loc_00898155;
    if (((Arg4) & (8 - 1)) != 0) goto loc_00897FB1;
    Arg1 = local_rbx;
    if (Arg4 < local_rbx) { Arg1 = Arg4; }
    *(uint8_t *)(arg1) = (uint8_t)(*(uint8_t *)(arg1));
    *(uint8_t *)(arg1 + (uint32_t)((uint32_t)(result)) * 1 - 0x1) = (uint8_t)(*(uint8_t *)(arg1 + (uint32_t)((uint32_t)(result)) * 1 - 0x1));
loc_008980A0:
    v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
loc_008980A9:
    result = *(uint8_t *)(arg1 + (uint32_t)((uint32_t)(result)) * 1 - 0x1);
    if (Arg3 != 0) {
        result = local_rbx;
        if (Arg3 < local_rbx) { result = Arg3; }
        result = *(uint64_t *)(result);
        v_stack_m80 = result;
        if (Arg3 < local_rbx) { local_rbx = Arg3; }
        result = *(uint64_t *)(local_rbx);
        *(uint64_t *)(local_rbx) = result;
        Arg1 = v_stack_mA0;
        v_stack_mA4 = (uint32_t)(Arg1);
    }
    goto loc_00898184;
loc_008980D8:
    if (sign_flag) goto loc_00898143;
loc_008980DC:
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x18)));
loc_008980E6:
    v_stack_m9C = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)));
    goto loc_00897FEC;
loc_008980EF:
    if (Arg2 < local_rbx) { Arg1 = Arg2; }
    *(uint8_t *)(arg1) = (uint8_t)(*(uint8_t *)(arg1));
    *(uint8_t *)(arg1 + 0x17) = (uint8_t)(*(uint8_t *)(arg1 + 0x17));
    goto loc_00897FDC;
loc_00898107:
    Arg1 = (uint32_t)((Arg1) & (12));
    Arg1 = (uint32_t)((Arg1) + (8));
    result = Arg1 + 16;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    Arg1 = result + 20;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(result); }
    result = Arg1 + 16;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    goto loc_0089805E;
loc_00898143:
    if (condition_is_below) goto loc_008980DC;
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)));
    goto loc_008980E6;
loc_00898155:
    result = ProbeForWrite(Arg4, (uint32_t)((uint32_t)(result)), 4, (uint32_t)(0x80000000ULL));
    goto loc_008980A0;
loc_00898170:
    v_stack_mA4 = 0;
    v_stack_mA0 = 0;
    goto loc_008980A9;
loc_00898184:
loc_00898189:
    v_stack_mB8 = 0;
    if ((uint32_t)(local_r14) != 0) goto loc_008984F7;
    result = AlpcpReceiveMessagePort(v_stack_p8, (uint8_t)(v_stack_mA8), Arg5, v_stack_m78);
loc_008981AF:
    if ((uint32_t)(result) != 0) goto loc_00898465;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m88)) & (0xC0000000ULL));
    result = 24;
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(0x80000000ULL)))) { result = 40; }
    result = (uint16_t)((result) + (*(uint16_t *)(v_stack_m78 + 0xF0)));
    if (Arg3 == 0) goto loc_00898200;
    v_stack_p8 = (uint16_t)(result);
    if (((uint16_t)(result)) > v_stack_m80) goto loc_008983B0;
loc_00898200:
    *(uint64_t *)(v_stack_m78 + 0xC8) = v_stack_m58;
    v_stack_p8 = 0;
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_00898311;
    *(uint64_t *)(arg2) = v_xmm0;
    *(uint64_t *)(arg2 + 0x10) = v_xmm1;
    *(uint64_t *)(arg2 + 0x20) = v_xmm0;
    result = v_stack_m58;
    if (((*(uint32_t *)(v_stack_m68 + 0x100)) & (0x1000ULL)) != 0) {
        result = *(uint16_t *)(v_stack_m78 + 0xF4);
        Arg1 = 0xFFFFC00FULL;
        result = (uint16_t)((result) & ((uint16_t)(Arg1)));
        *(uint16_t *)(arg2 + 0x4) = (uint16_t)(result);
    }
    v_stack_p8 = (uint32_t)(*(uint16_t *)(v_stack_m78 + 0xF2));
    v_stack_p8 = Arg2 + 40;
    if ((*(uint64_t *)(v_stack_m78 + 0xB0)) != 0) goto loc_008982FB;
    if (*(uint64_t *)(v_stack_m78 + 0x60) != 0) goto loc_00898308;
loc_00898298:
    if ((*(uint16_t *)(v_stack_m78 + 0xF0)) > 512) goto loc_008982DC;
loc_008982AD:
    result = memcpy(Arg2 + 40, v_stack_m78 + 280, (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m78 + 0xF0))), v_stack_m78);
loc_008982B5:
    if (Arg4 == 0) goto loc_0089841C;
    v_stack_mB8 = Arg4;
    result = AlpcpExposeAttributes(v_stack_m68, (uint32_t)(v_stack_m88), v_stack_m78, (uint32_t)(v_stack_mA4));
    goto loc_0089841C;
loc_008982DC:
    result = memcpy(v_stack_m68, (uint32_t)(v_stack_m88), 512, (uint32_t)(v_stack_mA4));
    local_rdi = ((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m78 + 0xF0)))) - (512);
    Arg1 = (v_stack_p8) + (512);
    goto loc_008982AD;
loc_008982FB:
    result = AlpcpGetDataFromUserVaSafe(v_stack_m78, Arg1, 512, (uint32_t)(v_stack_mA4));
    goto loc_008982B5;
loc_00898308:
    local_r15 = (*(uint64_t *)(512 + 0x20)) - (512);
    goto loc_00898298;
loc_00898311:
    *(uint16_t *)(local_rdi) = (uint16_t)(*(uint16_t *)(v_stack_m78 + 0xF0));
    result = (uint32_t)((*(uint16_t *)(v_stack_m78 + 0xF0)) + (24));
    v_stack_p8 = (uint32_t)(result);
    *(uint16_t *)(local_rdi + 0x2) = (uint16_t)(result);
    if ((uint16_t)(*(uint16_t *)(v_stack_m78 + 0xF6)) != 0) goto loc_0089840F;
    *(uint16_t *)(local_rdi + 0x6) = 0;
loc_00898344:
    Arg2 = (uint16_t)(((uint32_t)(0x1000ULL)) | (*(uint16_t *)(v_stack_m78 + 0xF4)));
    *(uint16_t *)(local_rdi + 0x4) = (uint16_t)(Arg2);
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m78 + 0xF8)));
    *(uint32_t *)(local_rdi + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m78 + 0x100)));
    *(uint32_t *)(local_rdi + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m78 + 0x108)));
    *(uint32_t *)(local_rdi + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m78 + 0x110)));
    *(uint32_t *)(local_rdi + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m78 + 0x110)));
    if (((*(uint32_t *)(v_stack_m68 + 0x100)) & (0x1000ULL)) != 0) {
        Arg1 = 0xFFFFC00FULL;
        Arg2 = (uint16_t)((Arg2) & ((uint16_t)(Arg1)));
        *(uint16_t *)(local_rdi + 0x4) = (uint16_t)(Arg2);
    }
    result = AlpcpGetDataFromMessage(v_stack_m78, local_rdi + 24, 512, (uint32_t)(v_stack_mA4));
    goto loc_008982B5;
loc_008983B0:
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = AlpcpReturnMessageOnInsufficientBuffer(v_stack_m68, v_stack_m78, v_stack_m48, (uint32_t)(v_stack_mA4));
    v_stack_m70 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_0089841C;
    *(uint64_t *)(local_r15) = v_stack_p8;
    result = AlpcpExposeCapturedContextAttribute((uint32_t)(v_stack_m88), v_stack_m48, (uint32_t)(v_stack_mA4), Arg4);
    goto loc_0089841C;
loc_0089840F:
    result = (uint16_t)((result) - (16));
    *(uint16_t *)(local_rdi + 0x6) = (uint16_t)(result);
    goto loc_00898344;
loc_0089841C:
    goto loc_0089843E;
loc_0089843E:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000023ULL) goto loc_00898455;
    if ((*(uint64_t *)(v_stack_m78 + 0x40)) == v_stack_m68) {
        *(uint64_t *)(v_stack_m78 + 0x40) = 0;
        *(uint64_t *)(v_stack_m78 + 0x38) = 0;
    }
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) == 0) goto loc_00898486;
loc_0089845D:
    result = AlpcpUnlockMessage(v_stack_m78, v_stack_m48, (uint32_t)(v_stack_mA4), Arg4);
loc_00898465:
loc_00898468:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00898486:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000023ULL) goto loc_0089845D;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xC8) = *(uint64_t *)(v_stack_m28 + 0x40);
    result = AlpcpCancelMessage(v_stack_m68, *(uint64_t *)(v_stack_m28 + 0x38), (uint32_t)(0x10000ULL), Arg4);
    goto loc_00898465;
loc_008984A9:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) & (0x1000000ULL));
    if (!(condition_is_equal)) {
        result = *(uint32_t *)(local_rdi + 0x18);
        v_stack_m70 = (uint32_t)(result);
        result = *(uint32_t *)(local_rdi + 0x20);
        v_stack_m74 = (uint32_t)(result);
    }
    if (Arg4 == 0) goto loc_0089850A;
loc_008984CC:
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4)));
    v_stack_m7C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4)));
    local_r13 = v_stack_m68;
    if (local_r15 != 0) {
        local_r13 = *(uint64_t *)(local_r15);
        v_stack_m58 = local_r13;
    }
    if (((*(uint32_t *)(Arg4 + 0x74)) & (0x400ULL)) == 0) goto loc_00898189;
    goto loc_00898189;
loc_008984F7:
    result = AlpcpReceiveDirectMessagePort((uint32_t)(*(uint32_t *)(Arg4)), (uint32_t)(v_stack_m70), (uint32_t)(v_stack_m74), Arg4);
    goto loc_008981AF;
loc_0089850A:
    goto loc_008984CC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x18` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00897ED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
