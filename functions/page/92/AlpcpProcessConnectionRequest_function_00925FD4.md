# AlpcpProcessConnectionRequest

- RVA: `0x00925FD4`–`0x009264E7` (길이 `1,299` bytes)
- VA: `0x0000000140925FD4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008D4B0`
- 디코드: `295`개 명령, `1,299/1,299` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00926010` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00926069` → [AlpcpProbeForWriteMessageHeader](../89/AlpcpProbeForWriteMessageHeader_function_00898660.md) (function, `0x00898660`)
- `0x00926079` → [AlpcpProbeAndCaptureMessageHeader](../9C/AlpcpProbeAndCaptureMessageHeader_function_009C5BB0.md) (function, `0x009C5BB0`)
- `0x009260C5` → [AlpcpProbeMessageAttributes](../89/AlpcpProbeMessageAttributes_function_008995A0.md) (function, `0x008995A0`)
- `0x00926142` → [AlpcpFormatConnectionRequest](AlpcpFormatConnectionRequest_function_00922A40.md) (function, `0x00922A40`)
- `0x0092618F` → [AlpcpDispatchConnectionRequest](AlpcpDispatchConnectionRequest_function_0092353C.md) (function, `0x0092353C`)
- `0x009261EA` → [AlpcpReceiveSynchronousReply](AlpcpReceiveSynchronousReply_function_009224F0.md) (function, `0x009224F0`)
- `0x0092625F` → [AlpcpExposeAttributes](../89/AlpcpExposeAttributes_function_00897630.md) (function, `0x00897630`)
- `0x009262DC` → [AlpcpGetDataFromMessage](AlpcpGetDataFromMessage_function_00922958.md) (function, `0x00922958`)
- `0x0092638F` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00926429` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00926484` → [AlpcpLogConnectRequest](../74/AlpcpLogConnectRequest_function_0074D14C.md) (function, `0x0074D14C`)
- `0x009264A3` → [AlpcpLogConnectFail](../74/AlpcpLogConnectFail_function_0074D0D8.md) (function, `0x0074D0D8`)
- `0x009264B8` → [AlpcpLogConnectFail](../74/AlpcpLogConnectFail_function_0074D0D8.md) (function, `0x0074D0D8`)
- `0x009264C9` → [AlpcpLogConnectSuccess](../74/AlpcpLogConnectSuccess_function_0074D1BC.md) (function, `0x0074D1BC`)

### Direct callers
- [AlpcpConnectPort](AlpcpConnectPort_function_00926C8C.md) at `0x00926F79`

### Static image references
- `0x00926164` → RVA `0x00E66D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00926010` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00926494` → [sub_00B22BEA](../B2/Unknown_function_00B22BEA.md) (`tail-transfer`)
  - `0x009264A9` → [sub_00B22BEA](../B2/Unknown_function_00B22BEA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00925FD4  48 8B C4                        mov rax, rsp
00925FD7  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
00925FDB  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
00925FDF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00925FE3  57                              push rdi
00925FE4  41 54                           push r12
00925FE6  41 55                           push r13
00925FE8  41 56                           push r14
00925FEA  41 57                           push r15
00925FEC  48 81 EC E0 00 00 00            sub rsp, 0xe0
00925FF3  4D 8B F9                        mov r15, r9
00925FF6  49 8B D8                        mov rbx, r8
00925FF9  8B F2                           mov esi, edx
00925FFB  48 8B F9                        mov rdi, rcx
00925FFE  45 33 F6                        xor r14d, r14d
00926001  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00926006  33 D2                           xor edx, edx
00926008  45 8D 46 40                     lea r8d, [r14 + 0x40]
0092600C  48 8D 48 98                     lea rcx, [rax - 0x68]
00926010  E8 2B 0C DA FF                  call 0x1406c6c40
00926015  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0092601A  0F 57 C0                        xorps xmm0, xmm0
0092601D  33 C0                           xor eax, eax
0092601F  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00926024  0F 11 84 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm0
0092602C  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00926034  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
00926039  0F BA E6 10                     bt esi, 0x10
0092603D  0F 82 00 04 00 00               jb 0x140926443
00926043  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00926048  48 83 4C 24 68 FF               or qword ptr [rsp + 0x68], 0xffffffffffffffff
0092604E  44 8A AC 24 48 01 00 00         mov r13b, byte ptr [rsp + 0x148]
00926056  45 84 ED                        test r13b, r13b
00926059  0F 84 56 03 00 00               je 0x1409263b5
0092605F  48 85 DB                        test rbx, rbx
00926062  74 1A                           je 0x14092607e
00926064  8B D6                           mov edx, esi
00926066  48 8B CB                        mov rcx, rbx
00926069  E8 F2 25 F7 FF                  call 0x140898660
0092606E  44 8B C6                        mov r8d, esi
00926071  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00926076  48 8B CB                        mov rcx, rbx
00926079  E8 32 FB 09 00                  call 0x1409c5bb0
0092607E  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
00926088  4D 85 FF                        test r15, r15
0092608B  74 20                           je 0x1409260ad
0092608D  48 8B C7                        mov rax, rdi
00926090  4C 3B FF                        cmp r15, rdi
00926093  49 0F 42 C7                     cmovb rax, r15
00926097  90                              nop
00926098  48 8B 00                        mov rax, qword ptr [rax]
0092609B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
009260A0  48 8B CF                        mov rcx, rdi
009260A3  49 0F 42 CF                     cmovb rcx, r15
009260A7  48 8B 01                        mov rax, qword ptr [rcx]
009260AA  48 89 01                        mov qword ptr [rcx], rax
009260AD  4C 8B A4 24 38 01 00 00         mov r12, qword ptr [rsp + 0x138]
009260B5  41 B6 01                        mov r14b, 1
009260B8  4D 85 E4                        test r12, r12
009260BB  74 11                           je 0x1409260ce
009260BD  45 8A C6                        mov r8b, r14b
009260C0  49 8B D4                        mov rdx, r12
009260C3  8B CE                           mov ecx, esi
009260C5  E8 D6 34 F7 FF                  call 0x1408995a0
009260CA  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009260CE  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
009260D6  48 85 C0                        test rax, rax
009260D9  74 1D                           je 0x1409260f8
009260DB  48 3B C7                        cmp rax, rdi
009260DE  48 0F 42 F8                     cmovb rdi, rax
009260E2  90                              nop
009260E3  48 8B 07                        mov rax, qword ptr [rdi]
009260E6  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009260EB  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009260F0  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009260F8  EB 05                           jmp 0x1409260ff
009260FA  E9 98 02 00 00                  jmp 0x140926397
009260FF  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
00926107  44 88 6C 24 48                  mov byte ptr [rsp + 0x48], r13b
0092610C  45 33 ED                        xor r13d, r13d
0092610F  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
00926114  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00926119  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
0092611E  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
00926126  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092612B  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00926130  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00926135  4C 8B CB                        mov r9, rbx
00926138  4C 8B C7                        mov r8, rdi
0092613B  8B D6                           mov edx, esi
0092613D  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00926142  E8 F9 C8 FF FF                  call 0x140922a40
00926147  85 C0                           test eax, eax
00926149  0F 88 48 02 00 00               js 0x140926397
0092614F  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00926154  41 8B 85 08 01 00 00            mov eax, dword ptr [r13 + 0x108]
0092615B  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
00926162  33 C9                           xor ecx, ecx
00926164  38 0D 96 0B 54 00               cmp byte ptr [rip + 0x540b96], cl
0092616A  0F 85 11 03 00 00               jne 0x140926481
00926170  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
00926178  4C 89 AC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r13
00926180  89 B4 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], esi
00926187  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
0092618F  E8 A8 D3 FF FF                  call 0x14092353c
00926194  8B F8                           mov edi, eax
00926196  33 C0                           xor eax, eax
00926198  85 FF                           test edi, edi
0092619A  0F 88 EE 02 00 00               js 0x14092648e
009261A0  0F BA E6 11                     bt esi, 0x11
009261A4  0F 83 3E 02 00 00               jae 0x1409263e8
009261AA  0F BA E6 14                     bt esi, 0x14
009261AE  72 10                           jb 0x1409261c0
009261B0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009261B9  44 8A B0 32 02 00 00            mov r14b, byte ptr [rax + 0x232]
009261C0  45 33 ED                        xor r13d, r13d
009261C3  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009261C8  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
009261D0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009261D5  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
009261DA  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
009261DF  41 8A D6                        mov dl, r14b
009261E2  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
009261EA  E8 01 C3 FF FF                  call 0x1409224f0
009261EF  44 8B F0                        mov r14d, eax
009261F2  85 C0                           test eax, eax
009261F4  0F 85 F2 01 00 00               jne 0x1409263ec
009261FA  44 38 2D FF 0A 54 00            cmp byte ptr [rip + 0x540aff], r13b
00926201  0F 85 BB 02 00 00               jne 0x1409264c2
00926207  85 F6                           test esi, esi
00926209  0F 88 C4 02 00 00               js 0x1409264d3
0092620F  B8 28 00 00 00                  mov eax, 0x28
00926214  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00926219  0F B7 8F F0 00 00 00            movzx ecx, word ptr [rdi + 0xf0]
00926220  03 C1                           add eax, ecx
00926222  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00926226  4D 85 FF                        test r15, r15
00926229  0F 85 E5 01 00 00               jne 0x140926414
0092622F  48 85 DB                        test rbx, rbx
00926232  75 35                           jne 0x140926269
00926234  4C 8B AC 24 10 01 00 00         mov r13, qword ptr [rsp + 0x110]
0092623C  4D 85 FF                        test r15, r15
0092623F  74 03                           je 0x140926244
00926241  49 89 07                        mov qword ptr [r15], rax
00926244  4D 85 E4                        test r12, r12
00926247  0F 84 35 01 00 00               je 0x140926382
0092624D  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00926252  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
00926257  4C 8B C7                        mov r8, rdi
0092625A  8B D6                           mov edx, esi
0092625C  49 8B CD                        mov rcx, r13
0092625F  E8 CC 13 F7 FF                  call 0x140897630
00926264  E9 19 01 00 00                  jmp 0x140926382
00926269  44 89 AC 24 18 01 00 00         mov dword ptr [rsp + 0x118], r13d
00926271  8B C6                           mov eax, esi
00926273  25 00 00 00 C0                  and eax, 0xc0000000
00926278  3D 00 00 00 80                  cmp eax, 0x80000000
0092627D  74 6B                           je 0x1409262ea
0092627F  0F 10 87 F0 00 00 00            movups xmm0, xmmword ptr [rdi + 0xf0]
00926286  0F 11 03                        movups xmmword ptr [rbx], xmm0
00926289  0F 10 8F 00 01 00 00            movups xmm1, xmmword ptr [rdi + 0x100]
00926290  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
00926294  F2 0F 10 87 10 01 00 00         movsd xmm0, qword ptr [rdi + 0x110]
0092629C  F2 0F 11 43 20                  movsd qword ptr [rbx + 0x20], xmm0
009262A1  4C 8B AC 24 10 01 00 00         mov r13, qword ptr [rsp + 0x110]
009262A9  41 0F BA A5 00 01 00 00 0C      bt dword ptr [r13 + 0x100], 0xc
009262B2  73 13                           jae 0x1409262c7
009262B4  0F B7 87 F4 00 00 00            movzx eax, word ptr [rdi + 0xf4]
009262BB  B9 0F C0 FF FF                  mov ecx, 0xffffc00f
009262C0  66 23 C1                        and ax, cx
009262C3  66 89 43 04                     mov word ptr [rbx + 4], ax
009262C7  0F B7 87 F2 00 00 00            movzx eax, word ptr [rdi + 0xf2]
009262CE  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
009262D5  48 8D 53 28                     lea rdx, [rbx + 0x28]
009262D9  48 8B CF                        mov rcx, rdi
009262DC  E8 77 C6 FF FF                  call 0x140922958
009262E1  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
009262E5  E9 52 FF FF FF                  jmp 0x14092623c
009262EA  66 89 0B                        mov word ptr [rbx], cx
009262ED  0F B7 87 F0 00 00 00            movzx eax, word ptr [rdi + 0xf0]
009262F4  83 C0 18                        add eax, 0x18
009262F7  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
009262FE  66 89 43 02                     mov word ptr [rbx + 2], ax
00926302  0F B7 87 F6 00 00 00            movzx eax, word ptr [rdi + 0xf6]
00926309  66 85 C0                        test ax, ax
0092630C  75 6A                           jne 0x140926378
0092630E  66 44 89 6B 06                  mov word ptr [rbx + 6], r13w
00926313  B9 00 10 00 00                  mov ecx, 0x1000
00926318  8B D1                           mov edx, ecx
0092631A  66 0B 97 F4 00 00 00            or dx, word ptr [rdi + 0xf4]
00926321  66 89 53 04                     mov word ptr [rbx + 4], dx
00926325  8B 87 F8 00 00 00               mov eax, dword ptr [rdi + 0xf8]
0092632B  89 43 08                        mov dword ptr [rbx + 8], eax
0092632E  8B 87 00 01 00 00               mov eax, dword ptr [rdi + 0x100]
00926334  89 43 0C                        mov dword ptr [rbx + 0xc], eax
00926337  8B 87 08 01 00 00               mov eax, dword ptr [rdi + 0x108]
0092633D  89 43 10                        mov dword ptr [rbx + 0x10], eax
00926340  8B 87 10 01 00 00               mov eax, dword ptr [rdi + 0x110]
00926346  89 43 14                        mov dword ptr [rbx + 0x14], eax
00926349  8B 87 10 01 00 00               mov eax, dword ptr [rdi + 0x110]
0092634F  89 43 14                        mov dword ptr [rbx + 0x14], eax
00926352  4C 8B AC 24 10 01 00 00         mov r13, qword ptr [rsp + 0x110]
0092635A  41 85 8D 00 01 00 00            test dword ptr [r13 + 0x100], ecx
00926361  74 0C                           je 0x14092636f
00926363  B9 0F C0 FF FF                  mov ecx, 0xffffc00f
00926368  66 23 D1                        and dx, cx
0092636B  66 89 53 04                     mov word ptr [rbx + 4], dx
0092636F  48 8D 53 18                     lea rdx, [rbx + 0x18]
00926373  E9 61 FF FF FF                  jmp 0x1409262d9
00926378  66 83 E8 10                     sub ax, 0x10
0092637C  66 89 43 06                     mov word ptr [rbx + 6], ax
00926380  EB 91                           jmp 0x140926313
00926382  EB 08                           jmp 0x14092638c
00926384  44 8B F0                        mov r14d, eax
00926387  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0092638C  48 8B CF                        mov rcx, rdi
0092638F  E8 4C 17 F7 FF                  call 0x140897ae0
00926394  41 8B C6                        mov eax, r14d
00926397  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
0092639F  49 8B 5B 40                     mov rbx, qword ptr [r11 + 0x40]
009263A3  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
009263A7  49 8B E3                        mov rsp, r11
009263AA  41 5F                           pop r15
009263AC  41 5E                           pop r14
009263AE  41 5D                           pop r13
009263B0  41 5C                           pop r12
009263B2  5F                              pop rdi
009263B3  C3                              ret
009263B4  CC                              int3
009263B5  48 85 DB                        test rbx, rbx
009263B8  0F 85 8F 00 00 00               jne 0x14092644d
009263BE  4D 85 FF                        test r15, r15
009263C1  0F 85 AD 00 00 00               jne 0x140926474
009263C7  4C 8B A4 24 38 01 00 00         mov r12, qword ptr [rsp + 0x138]
009263CF  41 B6 01                        mov r14b, 1
009263D2  4D 85 E4                        test r12, r12
009263D5  0F 84 2C FD FF FF               je 0x140926107
009263DB  41 8B 04 24                     mov eax, dword ptr [r12]
009263DF  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009263E3  E9 1F FD FF FF                  jmp 0x140926107
009263E8  8B C7                           mov eax, edi
009263EA  EB AB                           jmp 0x140926397
009263EC  44 38 2D 0D 09 54 00            cmp byte ptr [rip + 0x54090d], r13b
009263F3  0F 85 B5 00 00 00               jne 0x1409264ae
009263F9  4C 8B AC 24 10 01 00 00         mov r13, qword ptr [rsp + 0x110]
00926401  41 F6 85 A0 01 00 00 10         test byte ptr [r13 + 0x1a0], 0x10
00926409  B8 41 00 00 C0                  mov eax, 0xc0000041
0092640E  44 0F 45 F0                     cmovne r14d, eax
00926412  EB 80                           jmp 0x140926394
00926414  44 8B E8                        mov r13d, eax
00926417  4C 3B 6C 24 68                  cmp r13, qword ptr [rsp + 0x68]
0092641C  77 08                           ja 0x140926426
0092641E  45 33 ED                        xor r13d, r13d
00926421  E9 09 FE FF FF                  jmp 0x14092622f
00926426  48 8B CF                        mov rcx, rdi
00926429  E8 B2 16 F7 FF                  call 0x140897ae0
0092642E  90                              nop
0092642F  4D 89 2F                        mov qword ptr [r15], r13
00926432  EB 05                           jmp 0x140926439
00926434  E9 5E FF FF FF                  jmp 0x140926397
00926439  B8 23 00 00 C0                  mov eax, 0xc0000023
0092643E  E9 54 FF FF FF                  jmp 0x140926397
00926443  B8 0D 00 00 C0                  mov eax, 0xc000000d
00926448  E9 4A FF FF FF                  jmp 0x140926397
0092644D  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00926450  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00926455  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00926459  0F 11 8C 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm1
00926461  F2 0F 10 43 20                  movsd xmm0, qword ptr [rbx + 0x20]
00926466  F2 0F 11 84 24 98 00 00 00      movsd qword ptr [rsp + 0x98], xmm0
0092646F  E9 4A FF FF FF                  jmp 0x1409263be
00926474  49 8B 07                        mov rax, qword ptr [r15]
00926477  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0092647C  E9 46 FF FF FF                  jmp 0x1409263c7
00926481  49 8B CD                        mov rcx, r13
00926484  E8 C3 6C E2 FF                  call 0x14074d14c
00926489  E9 E2 FC FF FF                  jmp 0x140926170
0092648E  38 05 6C 08 54 00               cmp byte ptr [rip + 0x54086c], al
00926494  0F 84 50 C7 1F 00               je 0x140b22bea
0092649A  8B D7                           mov edx, edi
0092649C  8B 8C 24 18 01 00 00            mov ecx, dword ptr [rsp + 0x118]
009264A3  E8 30 6C E2 FF                  call 0x14074d0d8
009264A8  90                              nop
009264A9  E9 3C C7 1F 00                  jmp 0x140b22bea
009264AE  41 8B D6                        mov edx, r14d
009264B1  8B 8C 24 18 01 00 00            mov ecx, dword ptr [rsp + 0x118]
009264B8  E8 1B 6C E2 FF                  call 0x14074d0d8
009264BD  E9 37 FF FF FF                  jmp 0x1409263f9
009264C2  8B 8C 24 18 01 00 00            mov ecx, dword ptr [rsp + 0x118]
009264C9  E8 EE 6C E2 FF                  call 0x14074d1bc
009264CE  E9 34 FD FF FF                  jmp 0x140926207
009264D3  0F BA E6 1E                     bt esi, 0x1e
009264D7  B8 18 00 00 00                  mov eax, 0x18
009264DC  0F 83 32 FD FF FF               jae 0x140926214
009264E2  E9 28 FD FF FF                  jmp 0x14092620f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpProcessConnectionRequest(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int8 v_stack_mC0;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (224);
    v_r14 = 0;
    v_stack_mB8 = 0;
    a2 = 0;
    result = memset(v_rsp - 104, a2, v_r14 + 64, a4);
    v_stack_mB0 = 0;
    result = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = 0;
    v_stack_m98 = 0;
    if (condition_is_below) goto loc_00926443;
    v_stack_mB8 = 0;
    if (a8 == 0) goto loc_009263B5;
    if (a3 != 0) {
        a2 = (unsigned int)((unsigned int)(a2));
        a1 = a3;
        result = AlpcpProbeForWriteMessageHeader(a1, a2, v_r14 + 64, a4);
        a3 = (unsigned int)((unsigned int)(a2));
        a2 = v_stack_m90;
        a1 = a3;
        result = AlpcpProbeAndCaptureMessageHeader(a1, a2, a3, a4);
    }
    if (a4 != 0) {
        result = a1;
        if (a4 < a1) { result = a4; }
        result = *(unsigned __int64 *)(result);
        v_stack_mA0 = result;
        a1 = a1;
        if (a4 < a1) { a1 = a4; }
        result = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(a1) = result;
    }
    if (a6 != 0) {
        a3 = 1;
        a2 = a6;
        a1 = (unsigned int)((unsigned int)(a2));
        result = AlpcpProbeMessageAttributes(a1, a2, a3, a4);
        v_stack_mB8 = (unsigned int)(result);
    }
    result = a7;
    if (a7 != 0) {
        if (a7 < a1) { a1 = a7; }
        result = *(unsigned __int64 *)(a1);
        v_stack_m98 = result;
        result = v_stack_m98;
        v_stack_p38 = result;
    }
    goto loc_009260FF;
loc_009260FF:
loc_00926107:
    v_stack_mC0 = a8;
    v_r13 = 0;
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = a5;
    v_stack_mE8 = v_stack_m90;
    result = AlpcpFormatConnectionRequest(v_stack_mB0, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_p8, a3);
    if (sign_flag) goto loc_00926397;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 264)));
    a1 = 0;
    if ((*(unsigned __int8 *)(v_rip + 5507990)) != 0) goto loc_00926481;
loc_00926170:
    v_stack_m68 = v_stack_p8;
    v_stack_m60 = v_stack_mB0;
    v_stack_m38 = (unsigned int)((unsigned int)(a2));
    result = AlpcpDispatchConnectionRequest(v_stack_m68, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_p8, a3);
    result = 0;
    if (sign_flag) goto loc_0092648E;
    if (condition_is_above_or_equal) goto loc_009263E8;
    v_r14 = 1;
    if (!(condition_is_below)) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        v_r14 = *(unsigned __int8 *)(result + 562);
    }
    v_r13 = 0;
    v_stack_mB0 = 0;
    v_stack_mE8 = a7;
    result = AlpcpReceiveSynchronousReply(v_stack_m68, (unsigned __int8)(v_r14), v_stack_mB0, (unsigned int)(v_stack_mB8));
    if ((unsigned int)(result) != 0) goto loc_009263EC;
    if ((*(unsigned __int8 *)(v_rip + 5507839)) != 0) goto loc_009264C2;
loc_00926207:
    if (sign_flag) goto loc_009264D3;
loc_0092620F:
loc_00926214:
    result = (unsigned int)((40) + ((unsigned int)(*(unsigned __int16 *)(v_stack_mB0 + 240))));
    v_stack_mA8 = (unsigned int)(result);
    if (a4 != 0) goto loc_00926414;
loc_0092622F:
    if (a3 != 0) goto loc_00926269;
loc_0092623C:
    if (a4 != 0) {
        *(unsigned __int64 *)(a4) = result;
    }
    if (a6 == 0) goto loc_00926382;
    v_stack_mE8 = a6;
    result = AlpcpExposeAttributes(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_mB0, (unsigned int)(v_stack_mB8));
    goto loc_00926382;
loc_00926269:
    v_stack_p10 = (unsigned int)(v_stack_p8);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0x80000000ULL) goto loc_009262EA;
    *(unsigned __int64 *)(a3) = v_xmm0;
    *(unsigned __int64 *)(a3 + 16) = v_xmm1;
    *(unsigned __int64 *)(a3 + 32) = v_xmm0;
    if (((unsigned int)(result)) < 0x80000000ULL) {
        result = *(unsigned __int16 *)(v_stack_mB0 + 244);
        a1 = 0xFFFFC00FULL;
        result = (unsigned __int16)((result) & ((unsigned __int16)(a1)));
        *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(result);
    }
    v_stack_p10 = (unsigned int)(*(unsigned __int16 *)(v_stack_mB0 + 242));
loc_009262D9:
    result = AlpcpGetDataFromMessage(v_stack_mB0, a3 + 40, v_stack_mB0, (unsigned int)(v_stack_mB8));
    goto loc_0092623C;
loc_009262EA:
    *(unsigned __int16 *)(a3) = (unsigned __int16)(v_stack_mB0);
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_mB0 + 240)) + (24));
    v_stack_p10 = (unsigned int)(result);
    *(unsigned __int16 *)(a3 + 2) = (unsigned __int16)(result);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_mB0 + 246)) != 0) goto loc_00926378;
    *(unsigned __int16 *)(a3 + 6) = (unsigned __int16)(v_stack_p8);
loc_00926313:
    a2 = (unsigned __int16)(((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))) | (*(unsigned __int16 *)(v_stack_mB0 + 244)));
    *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(a2);
    *(unsigned int *)(a3 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 248)));
    *(unsigned int *)(a3 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 256)));
    *(unsigned int *)(a3 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 264)));
    *(unsigned int *)(a3 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 272)));
    *(unsigned int *)(a3 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 272)));
    if (((*(unsigned int *)(v_stack_p8 + 256)) & ((unsigned int)((unsigned int)(0x1000ULL)))) != 0) {
        a1 = 0xFFFFC00FULL;
        a2 = (unsigned __int16)((a2) & ((unsigned __int16)(a1)));
        *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(a2);
    }
    goto loc_009262D9;
loc_00926378:
    result = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_stack_mB0 + 272))) - (16));
    *(unsigned __int16 *)(a3 + 6) = (unsigned __int16)(result);
    goto loc_00926313;
loc_00926382:
    goto loc_0092638C;
loc_0092638C:
    result = AlpcpUnlockMessage(v_stack_mB0, a3 + 24, v_stack_mB0, (unsigned int)(v_stack_mB8));
loc_00926394:
loc_00926397:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_009263B5:
    if (*(unsigned __int64 *)(v_stack_m28 + 64) != 0) goto loc_0092644D;
loc_009263BE:
    if (a4 != 0) goto loc_00926474;
loc_009263C7:
    if (a6 == 0) goto loc_00926107;
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(a6)));
    goto loc_00926107;
loc_009263E8:
    goto loc_00926397;
loc_009263EC:
    if ((*(unsigned __int8 *)(v_rip + 5507341)) != ((unsigned __int8)(v_stack_p8))) goto loc_009264AE;
loc_009263F9:
    v_r14 = 1;
    if (((*(unsigned __int8 *)(v_stack_p30 + 416)) & (16)) != 0) { v_r14 = (unsigned int)((unsigned int)(0xC0000041ULL)); }
    goto loc_00926394;
loc_00926414:
    if (((unsigned int)((unsigned int)((unsigned int)(0xC0000041ULL)))) > v_stack_m78) goto loc_00926426;
    v_r13 = 0;
    goto loc_0092622F;
loc_00926426:
    result = AlpcpUnlockMessage(v_stack_mB0, a3 + 24, v_stack_mB0, (unsigned int)(v_stack_mB8));
    *(unsigned __int64 *)(a4) = 0;
    goto loc_00926439;
loc_00926439:
    goto loc_00926397;
loc_00926443:
    goto loc_00926397;
loc_0092644D:
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm1;
    v_stack_m48 = v_xmm0;
    goto loc_009263BE;
loc_00926474:
    v_stack_m78 = *(unsigned __int64 *)(a4);
    goto loc_009263C7;
loc_00926481:
    result = AlpcpLogConnectRequest(0, a3 + 24, v_stack_mB0, (unsigned int)(v_stack_mB8));
    goto loc_00926170;
loc_0092648E:
    result = AlpcpLogConnectFail((unsigned int)(v_stack_p38), (unsigned int)((unsigned int)(v_stack_mB0)), v_stack_mB0, (unsigned int)(v_stack_mB8));
loc_009264AE:
    result = AlpcpLogConnectFail((unsigned int)(v_stack_p38), (unsigned int)((unsigned int)(v_r14)), v_stack_mB0, (unsigned int)(v_stack_mB8));
    goto loc_009263F9;
loc_009264C2:
    result = AlpcpLogConnectSuccess((unsigned int)(v_stack_p38), (unsigned int)((unsigned int)(v_r14)), v_stack_mB0, (unsigned int)(v_stack_mB8));
    goto loc_00926207;
loc_009264D3:
    if ((*(unsigned __int8 *)(v_rip + 5507180)) >= ((unsigned __int8)(result))) goto loc_00926214;
    goto loc_0092620F;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpProcessConnectionRequest(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, uint8_t Arg8)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint8_t v_stack_mC0;
    uint8_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (224);
    local_r14 = 0;
    v_stack_mB8 = 0;
    Arg2 = 0;
    result = memset(local_rsp - 104, Arg2, local_r14 + 64, Arg4);
    v_stack_mB0 = 0;
    result = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = 0;
    v_stack_m98 = 0;
    if (condition_is_below) goto loc_00926443;
    v_stack_mB8 = 0;
    if (Arg8 == 0) goto loc_009263B5;
    if (Arg3 != 0) {
        Arg2 = (uint32_t)((uint32_t)(Arg2));
        Arg1 = Arg3;
        result = AlpcpProbeForWriteMessageHeader(Arg1, Arg2, local_r14 + 64, Arg4);
        Arg3 = (uint32_t)((uint32_t)(Arg2));
        Arg2 = v_stack_m90;
        Arg1 = Arg3;
        result = AlpcpProbeAndCaptureMessageHeader(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg4 != 0) {
        result = Arg1;
        if (Arg4 < Arg1) { result = Arg4; }
        result = *(uint64_t *)(result);
        v_stack_mA0 = result;
        Arg1 = Arg1;
        if (Arg4 < Arg1) { Arg1 = Arg4; }
        result = *(uint64_t *)(Arg1);
        *(uint64_t *)(Arg1) = result;
    }
    if (Arg6 != 0) {
        Arg3 = 1;
        Arg2 = Arg6;
        Arg1 = (uint32_t)((uint32_t)(Arg2));
        result = AlpcpProbeMessageAttributes(Arg1, Arg2, Arg3, Arg4);
        v_stack_mB8 = (uint32_t)(result);
    }
    result = Arg7;
    if (Arg7 != 0) {
        if (Arg7 < Arg1) { Arg1 = Arg7; }
        result = *(uint64_t *)(Arg1);
        v_stack_m98 = result;
        result = v_stack_m98;
        v_stack_p38 = result;
    }
    goto loc_009260FF;
loc_009260FF:
loc_00926107:
    v_stack_mC0 = Arg8;
    local_r13 = 0;
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = Arg5;
    v_stack_mE8 = v_stack_m90;
    result = AlpcpFormatConnectionRequest(v_stack_mB0, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_p8, Arg3);
    if (sign_flag) goto loc_00926397;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x108)));
    Arg1 = 0;
    if ((*(uint8_t *)(v_rip + 0x540B96)) != 0) goto loc_00926481;
loc_00926170:
    v_stack_m68 = v_stack_p8;
    v_stack_m60 = v_stack_mB0;
    v_stack_m38 = (uint32_t)((uint32_t)(Arg2));
    result = AlpcpDispatchConnectionRequest(v_stack_m68, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_p8, Arg3);
    result = 0;
    if (sign_flag) goto loc_0092648E;
    if (condition_is_above_or_equal) goto loc_009263E8;
    local_r14 = 1;
    if (!(condition_is_below)) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        local_r14 = *(uint8_t *)(result + 0x232);
    }
    local_r13 = 0;
    v_stack_mB0 = 0;
    v_stack_mE8 = Arg7;
    result = AlpcpReceiveSynchronousReply(v_stack_m68, (uint8_t)(local_r14), v_stack_mB0, (uint32_t)(v_stack_mB8));
    if ((uint32_t)(result) != 0) goto loc_009263EC;
    if ((*(uint8_t *)(v_rip + 0x540AFF)) != 0) goto loc_009264C2;
loc_00926207:
    if (sign_flag) goto loc_009264D3;
loc_0092620F:
loc_00926214:
    result = (uint32_t)((40) + ((uint32_t)(*(uint16_t *)(v_stack_mB0 + 0xF0))));
    v_stack_mA8 = (uint32_t)(result);
    if (Arg4 != 0) goto loc_00926414;
loc_0092622F:
    if (Arg3 != 0) goto loc_00926269;
loc_0092623C:
    if (Arg4 != 0) {
        *(uint64_t *)(Arg4) = result;
    }
    if (Arg6 == 0) goto loc_00926382;
    v_stack_mE8 = Arg6;
    result = AlpcpExposeAttributes(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_mB0, (uint32_t)(v_stack_mB8));
    goto loc_00926382;
loc_00926269:
    v_stack_p10 = (uint32_t)(v_stack_p8);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0x80000000ULL) goto loc_009262EA;
    *(uint64_t *)(Arg3) = v_xmm0;
    *(uint64_t *)(Arg3 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg3 + 0x20) = v_xmm0;
    if (((uint32_t)(result)) < 0x80000000ULL) {
        result = *(uint16_t *)(v_stack_mB0 + 0xF4);
        Arg1 = 0xFFFFC00FULL;
        result = (uint16_t)((result) & ((uint16_t)(Arg1)));
        *(uint16_t *)(Arg3 + 0x4) = (uint16_t)(result);
    }
    v_stack_p10 = (uint32_t)(*(uint16_t *)(v_stack_mB0 + 0xF2));
loc_009262D9:
    result = AlpcpGetDataFromMessage(v_stack_mB0, Arg3 + 40, v_stack_mB0, (uint32_t)(v_stack_mB8));
    goto loc_0092623C;
loc_009262EA:
    *(uint16_t *)(Arg3) = (uint16_t)(v_stack_mB0);
    result = (uint32_t)((*(uint16_t *)(v_stack_mB0 + 0xF0)) + (24));
    v_stack_p10 = (uint32_t)(result);
    *(uint16_t *)(Arg3 + 0x2) = (uint16_t)(result);
    if ((uint16_t)(*(uint16_t *)(v_stack_mB0 + 0xF6)) != 0) goto loc_00926378;
    *(uint16_t *)(Arg3 + 0x6) = (uint16_t)(v_stack_p8);
loc_00926313:
    Arg2 = (uint16_t)(((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))) | (*(uint16_t *)(v_stack_mB0 + 0xF4)));
    *(uint16_t *)(Arg3 + 0x4) = (uint16_t)(Arg2);
    *(uint32_t *)(Arg3 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0xF8)));
    *(uint32_t *)(Arg3 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x100)));
    *(uint32_t *)(Arg3 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x108)));
    *(uint32_t *)(Arg3 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x110)));
    *(uint32_t *)(Arg3 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x110)));
    if (((*(uint32_t *)(v_stack_p8 + 0x100)) & ((uint32_t)((uint32_t)(0x1000ULL)))) != 0) {
        Arg1 = 0xFFFFC00FULL;
        Arg2 = (uint16_t)((Arg2) & ((uint16_t)(Arg1)));
        *(uint16_t *)(Arg3 + 0x4) = (uint16_t)(Arg2);
    }
    goto loc_009262D9;
loc_00926378:
    result = (uint16_t)(((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x110))) - (16));
    *(uint16_t *)(Arg3 + 0x6) = (uint16_t)(result);
    goto loc_00926313;
loc_00926382:
    goto loc_0092638C;
loc_0092638C:
    result = AlpcpUnlockMessage(v_stack_mB0, Arg3 + 24, v_stack_mB0, (uint32_t)(v_stack_mB8));
loc_00926394:
loc_00926397:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_009263B5:
    if (*(uint64_t *)(v_stack_m28 + 0x40) != 0) goto loc_0092644D;
loc_009263BE:
    if (Arg4 != 0) goto loc_00926474;
loc_009263C7:
    if (Arg6 == 0) goto loc_00926107;
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg6)));
    goto loc_00926107;
loc_009263E8:
    goto loc_00926397;
loc_009263EC:
    if ((*(uint8_t *)(v_rip + 0x54090D)) != ((uint8_t)(v_stack_p8))) goto loc_009264AE;
loc_009263F9:
    local_r14 = 1;
    if (((*(uint8_t *)(v_stack_p30 + 0x1A0)) & (16)) != 0) { local_r14 = (uint32_t)((uint32_t)(0xC0000041ULL)); }
    goto loc_00926394;
loc_00926414:
    if (((uint32_t)((uint32_t)((uint32_t)(0xC0000041ULL)))) > v_stack_m78) goto loc_00926426;
    local_r13 = 0;
    goto loc_0092622F;
loc_00926426:
    result = AlpcpUnlockMessage(v_stack_mB0, Arg3 + 24, v_stack_mB0, (uint32_t)(v_stack_mB8));
    *(uint64_t *)(Arg4) = 0;
    goto loc_00926439;
loc_00926439:
    goto loc_00926397;
loc_00926443:
    goto loc_00926397;
loc_0092644D:
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm1;
    v_stack_m48 = v_xmm0;
    goto loc_009263BE;
loc_00926474:
    v_stack_m78 = *(uint64_t *)(Arg4);
    goto loc_009263C7;
loc_00926481:
    result = AlpcpLogConnectRequest(0, Arg3 + 24, v_stack_mB0, (uint32_t)(v_stack_mB8));
    goto loc_00926170;
loc_0092648E:
    result = AlpcpLogConnectFail((uint32_t)(v_stack_p38), (uint32_t)((uint32_t)(v_stack_mB0)), v_stack_mB0, (uint32_t)(v_stack_mB8));
loc_009264AE:
    result = AlpcpLogConnectFail((uint32_t)(v_stack_p38), (uint32_t)((uint32_t)(local_r14)), v_stack_mB0, (uint32_t)(v_stack_mB8));
    goto loc_009263F9;
loc_009264C2:
    result = AlpcpLogConnectSuccess((uint32_t)(v_stack_p38), (uint32_t)((uint32_t)(local_r14)), v_stack_mB0, (uint32_t)(v_stack_mB8));
    goto loc_00926207;
loc_009264D3:
    if ((*(uint8_t *)(v_rip + 0x54086C)) >= ((uint8_t)(result))) goto loc_00926214;
    goto loc_0092620F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00925FD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
