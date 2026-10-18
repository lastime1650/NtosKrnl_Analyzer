# MiMapViewOfSection

- RVA: `0x00898F10`–`0x00899595` (길이 `1,669` bytes)
- VA: `0x0000000140898F10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007E4E4`
- 디코드: `395`개 명령, `1,669/1,669` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00898F77` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x00898FFB` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x0089915E` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x00899190` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x0089919E` → [MiValidateVadMetadataFlags](../88/MiValidateVadMetadataFlags_function_008843D0.md) (function, `0x008843D0`)
- `0x008991E9` → [MiMapViewOfDataSection](../88/MiMapViewOfDataSection_function_00884E20.md) (function, `0x00884E20`)
- `0x008991FC` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0089920E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00899319` → [MiMapViewOfPhysicalSection](../97/MiMapViewOfPhysicalSection_function_0097F984.md) (function, `0x0097F984`)
- `0x00899356` → [MiMapViewOfImageSection](../97/MiMapViewOfImageSection_function_0097E92C.md) (function, `0x0097E92C`)
- `0x008993BC` → [MiArbitraryCodeBlocked](../97/MiArbitraryCodeBlocked_function_0097D7CC.md) (function, `0x0097D7CC`)
- `0x00899448` → [MiFinalizeLagePageImageMapping](../7F/MiFinalizeLagePageImageMapping_function_007FE454.md) (function, `0x007FE454`)

### Direct callers
- [AlpcpCreateView](../88/AlpcpCreateView_function_0088A9B8.md) at `0x0088AB91`
- [AlpcpCreateView](../88/AlpcpCreateView_function_0088A9B8.md) at `0x0088AE9D`
- [NtMapViewOfSection](NtMapViewOfSection_function_008986E0.md) at `0x00898928`
- [MmMapViewOfSection](../98/MmMapViewOfSection_function_00981680.md) at `0x009817C1`
- [MiMapViewOfSectionExCommon](../9A/MiMapViewOfSectionExCommon_function_009A1C60.md) at `0x009A1E28`
- [NtGetNlsSectionPtr](../A1/NtGetNlsSectionPtr_function_00A195B0.md) at `0x00A19896`

### Static image references
- `0x00898F24` → RVA `0x00E0A740` (`.data`; read)
- `0x00899003` → RVA `0x00014710` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00898F77` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x00898FFB` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (`PAGE` → `.text`)
  - `0x0089915E` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (`PAGE` → `.text`)
  - `0x00899190` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x008991FC` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0089920E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x008992A9` → [sub_00B19B64](../B1/Unknown_function_00B19B64.md) (`tail-transfer`)
  - `0x00899420` → [sub_00B19B64 + 0x51](../B1/Unknown_function_00B19B64.md) (`tail-transfer`)
  - `0x0089944F` → [sub_00B19B64 + 0x51](../B1/Unknown_function_00B19B64.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00898F10  40 53                           push rbx
00898F12  55                              push rbp
00898F13  56                              push rsi
00898F14  57                              push rdi
00898F15  41 54                           push r12
00898F17  41 55                           push r13
00898F19  41 56                           push r14
00898F1B  41 57                           push r15
00898F1D  48 81 EC A8 00 00 00            sub rsp, 0xa8
00898F24  48 8B 05 15 18 57 00            mov rax, qword ptr [rip + 0x571815]
00898F2B  48 33 C4                        xor rax, rsp
00898F2E  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00898F36  4C 8B 5A 58                     mov r11, qword ptr [rdx + 0x58]
00898F3A  0F 57 C0                        xorps xmm0, xmm0
00898F3D  4C 8B BC 24 10 01 00 00         mov r15, qword ptr [rsp + 0x110]
00898F45  33 C0                           xor eax, eax
00898F47  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00898F4C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00898F51  44 8B E8                        mov r13d, eax
00898F54  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00898F59  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
00898F5E  49 8B F1                        mov rsi, r9
00898F61  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
00898F69  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00898F6E  4D 8B E0                        mov r12, r8
00898F71  48 8B DA                        mov rbx, rdx
00898F74  48 8B E9                        mov rbp, rcx
00898F77  E8 34 BD 9F FF                  call 0x140294cb0
00898F7C  8B 94 24 20 01 00 00            mov edx, dword ptr [rsp + 0x120]
00898F83  4C 8B F0                        mov r14, rax
00898F86  41 BA 00 00 01 00               mov r10d, 0x10000
00898F8C  48 8B 38                        mov rdi, qword ptr [rax]
00898F8F  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00898F93  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00898F98  85 D2                           test edx, edx
00898F9A  0F 84 88 02 00 00               je 0x140899228
00898FA0  F7 43 28 00 00 00 40            test dword ptr [rbx + 0x28], 0x40000000
00898FA7  0F 85 E6 04 00 00               jne 0x140899493
00898FAD  44 8B 43 2C                     mov r8d, dword ptr [rbx + 0x2c]
00898FB1  41 8B C8                        mov ecx, r8d
00898FB4  81 E1 F0 00 00 00               and ecx, 0xf0
00898FBA  0F 85 03 03 00 00               jne 0x1408992c3
00898FC0  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
00898FC3  A8 20                           test al, 0x20
00898FC5  0F 85 F8 02 00 00               jne 0x1408992c3
00898FCB  41 0F BA E0 1E                  bt r8d, 0x1e
00898FD0  0F 82 D7 04 00 00               jb 0x1408994ad
00898FD6  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
00898FD9  41 B9 00 20 00 00               mov r9d, 0x2000
00898FDF  A8 08                           test al, 8
00898FE1  0F 85 EB 04 00 00               jne 0x1408994d2
00898FE7  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
00898FEA  A8 20                           test al, 0x20
00898FEC  0F 85 9F 02 00 00               jne 0x140899291
00898FF2  8B 4D 3C                        mov ecx, dword ptr [rbp + 0x3c]
00898FF5  81 E1 FF 0F 00 00               and ecx, 0xfff
00898FFB  E8 80 04 A9 FF                  call 0x140329480
00899000  83 E0 07                        and eax, 7
00899003  48 8D 0D 06 B7 77 FF            lea rcx, [rip - 0x8848fa]
0089900A  8B 0C 81                        mov ecx, dword ptr [rcx + rax*4]
0089900D  81 C9 00 07 00 00               or ecx, 0x700
00899013  44 0B C1                        or r8d, ecx
00899016  44 3B C1                        cmp r8d, ecx
00899019  0F 85 4B 04 00 00               jne 0x14089946a
0089901F  8B 4B 28                        mov ecx, dword ptr [rbx + 0x28]
00899022  F7 C1 00 00 84 00               test ecx, 0x840000
00899028  0F 85 31 02 00 00               jne 0x14089925f
0089902E  66 44 39 6B 3A                  cmp word ptr [rbx + 0x3a], r13w
00899033  0F 85 26 02 00 00               jne 0x14089925f
00899039  41 F7 46 38 00 04 00 00         test dword ptr [r14 + 0x38], 0x400
00899041  0F 85 A5 04 00 00               jne 0x1408994ec
00899047  49 8B 17                        mov rdx, qword ptr [r15]
0089904A  4C 8B 43 18                     mov r8, qword ptr [rbx + 0x18]
0089904E  49 8D 04 10                     lea rax, [r8 + rdx]
00899052  48 3B C2                        cmp rax, rdx
00899055  0F 82 23 04 00 00               jb 0x14089947e
0089905B  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0089905F  48 3B C1                        cmp rax, rcx
00899062  0F 87 0C 04 00 00               ja 0x140899474
00899068  4D 85 C0                        test r8, r8
0089906B  75 07                           jne 0x140899074
0089906D  48 2B CA                        sub rcx, rdx
00899070  48 89 4B 18                     mov qword ptr [rbx + 0x18], rcx
00899074  41 F7 46 38 00 04 00 00         test dword ptr [r14 + 0x38], 0x400
0089907C  0F 85 EB 01 00 00               jne 0x14089926d
00899082  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00899086  49 3B CA                        cmp rcx, r10
00899089  0F 87 6E 04 00 00               ja 0x1408994fd
0089908F  45 8B 07                        mov r8d, dword ptr [r15]
00899092  48 8D 51 FF                     lea rdx, [rcx - 1]
00899096  49 23 D0                        and rdx, r8
00899099  0F 85 27 03 00 00               jne 0x1408993c6
0089909F  4C 39 6B 18                     cmp qword ptr [rbx + 0x18], r13
008990A3  0F 8E D5 03 00 00               jle 0x14089947e
008990A9  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
008990AD  49 8B 14 24                     mov rdx, qword ptr [r12]
008990B1  48 8D 41 FF                     lea rax, [rcx - 1]
008990B5  48 85 C2                        test rdx, rax
008990B8  0F 85 F0 01 00 00               jne 0x1408992ae
008990BE  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
008990C2  B8 00 10 00 00                  mov eax, 0x1000
008990C7  48 8B D1                        mov rdx, rcx
008990CA  48 89 4B 20                     mov qword ptr [rbx + 0x20], rcx
008990CE  4C 8B C9                        mov r9, rcx
008990D1  81 E2 FF 0F 00 00               and edx, 0xfff
008990D7  0F 85 FF 01 00 00               jne 0x1408992dc
008990DD  44 8B 53 3C                     mov r10d, dword ptr [rbx + 0x3c]
008990E1  49 8B C4                        mov rax, r12
008990E4  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
008990E8  41 83 E2 01                     and r10d, 1
008990EC  48 0F 44 C3                     cmove rax, rbx
008990F0  4C 8B 00                        mov r8, qword ptr [rax]
008990F3  4C 3B C2                        cmp r8, rdx
008990F6  0F 87 63 01 00 00               ja 0x14089925f
008990FC  49 2B D0                        sub rdx, r8
008990FF  48 FF C2                        inc rdx
00899102  49 3B D1                        cmp rdx, r9
00899105  0F 82 0E 04 00 00               jb 0x140899519
0089910B  BA 00 20 00 00                  mov edx, 0x2000
00899110  48 3B F1                        cmp rsi, rcx
00899113  0F 87 13 04 00 00               ja 0x14089952c
00899119  48 3B 4D 30                     cmp rcx, qword ptr [rbp + 0x30]
0089911D  0F 87 65 03 00 00               ja 0x140899488
00899123  8B 4B 28                        mov ecx, dword ptr [rbx + 0x28]
00899126  85 CA                           test edx, ecx
00899128  0F 85 31 03 00 00               jne 0x14089945f
0089912E  0F BA E1 17                     bt ecx, 0x17
00899132  0F 82 BE 01 00 00               jb 0x1408992f6
00899138  F7 43 40 00 00 00 04            test dword ptr [rbx + 0x40], 0x4000000
0089913F  0F 85 F5 03 00 00               jne 0x14089953a
00899145  8B 4B 2C                        mov ecx, dword ptr [rbx + 0x2c]
00899148  66 85 57 0C                     test word ptr [rdi + 0xc], dx
0089914C  0F 85 33 04 00 00               jne 0x140899585
00899152  66 0F BA 67 0C 0C               bt word ptr [rdi + 0xc], 0xc
00899158  0F 82 6E 01 00 00               jb 0x1408992cc
0089915E  E8 1D 03 A9 FF                  call 0x140329480
00899163  8B F0                           mov esi, eax
00899165  83 F8 FF                        cmp eax, -1
00899168  0F 84 F8 00 00 00               je 0x140899266
0089916E  4C 8B 43 60                     mov r8, qword ptr [rbx + 0x60]
00899172  41 F7 80 50 07 00 00 00 01 00 00  test dword ptr [r8 + 0x750], 0x100
0089917D  0F 85 FD 01 00 00               jne 0x140899380
00899183  4D 3B C3                        cmp r8, r11
00899186  74 13                           je 0x14089919b
00899188  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
0089918D  49 8B CB                        mov rcx, r11
00899190  E8 6B D6 97 FF                  call 0x140216800
00899195  41 BD 01 00 00 00               mov r13d, 1
0089919B  48 8B CB                        mov rcx, rbx
0089919E  E8 2D B2 FE FF                  call 0x1408843d0
008991A3  8B F8                           mov edi, eax
008991A5  85 C0                           test eax, eax
008991A7  78 47                           js 0x1408991f0
008991A9  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
008991AD  0F BA E0 0A                     bt eax, 0xa
008991B1  0F 82 59 01 00 00               jb 0x140899310
008991B7  A8 20                           test al, 0x20
008991B9  0F 85 64 01 00 00               jne 0x140899323
008991BF  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008991C4  4D 8B CF                        mov r9, r15
008991C7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008991CC  4D 8B C4                        mov r8, r12
008991CF  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
008991D6  48 8B D3                        mov rdx, rbx
008991D9  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
008991DD  49 8B CE                        mov rcx, r14
008991E0  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008991E4  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
008991E9  E8 32 BC FE FF                  call 0x140884e20
008991EE  8B F8                           mov edi, eax
008991F0  45 85 ED                        test r13d, r13d
008991F3  74 0C                           je 0x140899201
008991F5  33 D2                           xor edx, edx
008991F7  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
008991FC  E8 2F EB 97 FF                  call 0x140217d30
00899201  8B C7                           mov eax, edi
00899203  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0089920B  48 33 CC                        xor rcx, rsp
0089920E  E8 2D 34 E1 FF                  call 0x1406ac640
00899213  48 81 C4 A8 00 00 00            add rsp, 0xa8
0089921A  41 5F                           pop r15
0089921C  41 5E                           pop r14
0089921E  41 5D                           pop r13
00899220  41 5C                           pop r12
00899222  5F                              pop rdi
00899223  5E                              pop rsi
00899224  5D                              pop rbp
00899225  5B                              pop rbx
00899226  C3                              ret
00899227  CC                              int3
00899228  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
0089922F  FF C8                           dec eax
00899231  83 F8 01                        cmp eax, 1
00899234  77 29                           ja 0x14089925f
00899236  41 F7 46 38 00 04 00 00         test dword ptr [r14 + 0x38], 0x400
0089923E  75 12                           jne 0x140899252
00899240  4C 39 53 10                     cmp qword ptr [rbx + 0x10], r10
00899244  72 0C                           jb 0x140899252
00899246  66 45 39 28                     cmp word ptr [r8], r13w
0089924A  75 6D                           jne 0x1408992b9
0089924C  66 45 39 2F                     cmp word ptr [r15], r13w
00899250  75 67                           jne 0x1408992b9
00899252  F7 43 28 FF DF 2B 9F            test dword ptr [rbx + 0x28], 0x9f2bdfff
00899259  0F 84 41 FD FF FF               je 0x140898fa0
0089925F  B8 0D 00 00 C0                  mov eax, 0xc000000d
00899264  EB 9D                           jmp 0x140899203
00899266  B8 45 00 00 C0                  mov eax, 0xc0000045
0089926B  EB 96                           jmp 0x140899203
0089926D  41 8B 0F                        mov ecx, dword ptr [r15]
00899270  F7 C1 FF 0F 00 00               test ecx, 0xfff
00899276  0F 84 23 FE FF FF               je 0x14089909f
0089927C  8B 43 3C                        mov eax, dword ptr [rbx + 0x3c]
0089927F  A8 02                           test al, 2
00899281  75 36                           jne 0x1408992b9
00899283  81 E1 00 F0 FF FF               and ecx, 0xfffff000
00899289  41 89 0F                        mov dword ptr [r15], ecx
0089928C  E9 0E FE FF FF                  jmp 0x14089909f
00899291  4C 39 6B 48                     cmp qword ptr [rbx + 0x48], r13
00899295  75 C8                           jne 0x14089925f
00899297  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
0089929A  41 85 C1                        test r9d, eax
0089929D  75 C0                           jne 0x14089925f
0089929F  0F BA E0 1D                     bt eax, 0x1d
008992A3  0F 83 9E FD FF FF               jae 0x140899047
008992A9  E9 B6 08 28 00                  jmp 0x140b19b64
008992AE  8B 43 3C                        mov eax, dword ptr [rbx + 0x3c]
008992B1  A8 02                           test al, 2
008992B3  0F 84 51 02 00 00               je 0x14089950a
008992B9  B8 20 02 00 C0                  mov eax, 0xc0000220
008992BE  E9 40 FF FF FF                  jmp 0x140899203
008992C3  83 4B 3C 08                     or dword ptr [rbx + 0x3c], 8
008992C7  E9 FF FC FF FF                  jmp 0x140898fcb
008992CC  0F BA E9 0A                     bts ecx, 0xa
008992D0  0F BA F1 09                     btr ecx, 9
008992D4  89 4B 2C                        mov dword ptr [rbx + 0x2c], ecx
008992D7  E9 82 FE FF FF                  jmp 0x14089915e
008992DC  2B C2                           sub eax, edx
008992DE  44 8B C8                        mov r9d, eax
008992E1  4C 03 C9                        add r9, rcx
008992E4  4C 3B C9                        cmp r9, rcx
008992E7  0F 82 91 01 00 00               jb 0x14089947e
008992ED  4C 89 4B 18                     mov qword ptr [rbx + 0x18], r9
008992F1  E9 E7 FD FF FF                  jmp 0x1408990dd
008992F6  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
008992F9  A8 20                           test al, 0x20
008992FB  0F 84 5E FF FF FF               je 0x14089925f
00899301  0F BA E1 1D                     bt ecx, 0x1d
00899305  0F 83 2D FE FF FF               jae 0x140899138
0089930B  E9 4F FF FF FF                  jmp 0x14089925f
00899310  44 8B CE                        mov r9d, esi
00899313  4D 8B C7                        mov r8, r15
00899316  49 8B D4                        mov rdx, r12
00899319  E8 66 66 0E 00                  call 0x14097f984
0089931E  E9 CB FE FF FF                  jmp 0x1408991ee
00899323  49 8B 04 24                     mov rax, qword ptr [r12]
00899327  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
0089932C  C7 44 24 38 00 00 00 00         mov dword ptr [rsp + 0x38], 0
00899334  4D 8B CF                        mov r9, r15
00899337  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089933C  48 8B D3                        mov rdx, rbx
0089933F  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
00899346  49 8B CE                        mov rcx, r14
00899349  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
0089934D  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00899351  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
00899356  E8 D1 55 0E 00                  call 0x14097e92c
0089935B  8B F8                           mov edi, eax
0089935D  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
00899360  0F BA E0 1D                     bt eax, 0x1d
00899364  0F 82 A1 00 00 00               jb 0x14089940b
0089936A  85 FF                           test edi, edi
0089936C  0F 88 7E FE FF FF               js 0x1408991f0
00899372  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00899377  49 89 04 24                     mov qword ptr [r12], rax
0089937B  E9 70 FE FF FF                  jmp 0x1408991f0
00899380  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00899389  F7 80 A0 05 00 00 00 00 04 00   test dword ptr [rax + 0x5a0], 0x40000
00899393  0F 85 EA FD FF FF               jne 0x140899183
00899399  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
0089939C  A8 20                           test al, 0x20
0089939E  75 5F                           jne 0x1408993ff
008993A0  F7 43 40 00 00 00 20            test dword ptr [rbx + 0x40], 0x20000000
008993A7  0F 94 C2                        sete dl
008993AA  40 F6 C6 02                     test sil, 2
008993AE  0F 95 C0                        setne al
008993B1  84 D0                           test al, dl
008993B3  0F 84 CA FD FF FF               je 0x140899183
008993B9  49 8B C8                        mov rcx, r8
008993BC  E8 0B 44 0E 00                  call 0x14097d7cc
008993C1  E9 3D FE FF FF                  jmp 0x140899203
008993C6  8B 43 3C                        mov eax, dword ptr [rbx + 0x3c]
008993C9  A8 02                           test al, 2
008993CB  0F 85 E8 FE FF FF               jne 0x1408992b9
008993D1  F7 D9                           neg ecx
008993D3  41 23 C8                        and ecx, r8d
008993D6  41 89 0F                        mov dword ptr [r15], ecx
008993D9  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
008993DD  A8 20                           test al, 0x20
008993DF  0F 85 BA FC FF FF               jne 0x14089909f
008993E5  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
008993E9  48 8D 0C 10                     lea rcx, [rax + rdx]
008993ED  48 3B C8                        cmp rcx, rax
008993F0  0F 82 88 00 00 00               jb 0x14089947e
008993F6  48 89 4B 18                     mov qword ptr [rbx + 0x18], rcx
008993FA  E9 A0 FC FF FF                  jmp 0x14089909f
008993FF  81 63 28 FF FF FF DF            and dword ptr [rbx + 0x28], 0xdfffffff
00899406  E9 78 FD FF FF                  jmp 0x140899183
0089940B  0F BA F0 1D                     btr eax, 0x1d
0089940F  89 43 28                        mov dword ptr [rbx + 0x28], eax
00899412  85 FF                           test edi, edi
00899414  0F 88 09 FF FF FF               js 0x140899323
0089941A  81 FF 0E 00 00 40               cmp edi, 0x4000000e
00899420  0F 84 8F 07 28 00               je 0x140b19bb5
00899426  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
0089942D  4D 8B CF                        mov r9, r15
00899430  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00899435  48 8B D3                        mov rdx, rbx
00899438  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
0089943C  49 8B CE                        mov rcx, r14
0089943F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00899443  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
00899448  E8 07 50 F6 FF                  call 0x1407fe454
0089944D  85 C0                           test eax, eax
0089944F  0F 88 60 07 28 00               js 0x140b19bb5
00899455  BF 03 00 00 40                  mov edi, 0x40000003
0089945A  E9 13 FF FF FF                  jmp 0x140899372
0089945F  8B 45 3C                        mov eax, dword ptr [rbp + 0x3c]
00899462  A8 44                           test al, 0x44
00899464  0F 85 C4 FC FF FF               jne 0x14089912e
0089946A  B8 4E 00 00 C0                  mov eax, 0xc000004e
0089946F  E9 8F FD FF FF                  jmp 0x140899203
00899474  44 85 4B 28                     test dword ptr [rbx + 0x28], r9d
00899478  0F 85 EA FB FF FF               jne 0x140899068
0089947E  B8 1F 00 00 C0                  mov eax, 0xc000001f
00899483  E9 7B FD FF FF                  jmp 0x140899203
00899488  85 53 28                        test dword ptr [rbx + 0x28], edx
0089948B  0F 85 92 FC FF FF               jne 0x140899123
00899491  EB EB                           jmp 0x14089947e
00899493  85 D2                           test edx, edx
00899495  0F 85 12 FB FF FF               jne 0x140898fad
0089949B  4D 39 AB 40 06 00 00            cmp qword ptr [r11 + 0x640], r13
008994A2  0F 84 B7 FD FF FF               je 0x14089925f
008994A8  E9 00 FB FF FF                  jmp 0x140898fad
008994AD  85 C9                           test ecx, ecx
008994AF  0F 84 AA FD FF FF               je 0x14089925f
008994B5  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
008994B8  A8 20                           test al, 0x20
008994BA  0F 85 9F FD FF FF               jne 0x14089925f
008994C0  41 0F BA F0 1E                  btr r8d, 0x1e
008994C5  83 4B 78 02                     or dword ptr [rbx + 0x78], 2
008994C9  44 89 43 2C                     mov dword ptr [rbx + 0x2c], r8d
008994CD  E9 04 FB FF FF                  jmp 0x140898fd6
008994D2  41 F6 C0 F0                     test r8b, 0xf0
008994D6  0F 84 83 FD FF FF               je 0x14089925f
008994DC  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
008994DF  A8 20                           test al, 0x20
008994E1  0F 85 78 FD FF FF               jne 0x14089925f
008994E7  E9 06 FB FF FF                  jmp 0x140898ff2
008994EC  F7 C1 00 20 00 20               test ecx, 0x20002000
008994F2  0F 85 67 FD FF FF               jne 0x14089925f
008994F8  E9 4A FB FF FF                  jmp 0x140899047
008994FD  4D 39 6E 40                     cmp qword ptr [r14 + 0x40], r13
00899501  49 0F 45 CA                     cmovne rcx, r10
00899505  E9 85 FB FF FF                  jmp 0x14089908f
0089950A  48 F7 D9                        neg rcx
0089950D  48 23 CA                        and rcx, rdx
00899510  49 89 0C 24                     mov qword ptr [r12], rcx
00899514  E9 A5 FB FF FF                  jmp 0x1408990be
00899519  45 85 D2                        test r10d, r10d
0089951C  49 8B C5                        mov rax, r13
0089951F  0F 95 C0                        setne al
00899522  05 17 00 00 C0                  add eax, 0xc0000017
00899527  E9 D7 FC FF FF                  jmp 0x140899203
0089952C  85 53 28                        test dword ptr [rbx + 0x28], edx
0089952F  0F 84 2A FD FF FF               je 0x14089925f
00899535  E9 DF FB FF FF                  jmp 0x140899119
0089953A  41 F7 46 38 20 04 00 00         test dword ptr [r14 + 0x38], 0x420
00899542  0F 85 17 FD FF FF               jne 0x14089925f
00899548  F7 C1 FF DF FF FF               test ecx, 0xffffdfff
0089954E  0F 85 0B FD FF FF               jne 0x14089925f
00899554  8B 43 3C                        mov eax, dword ptr [rbx + 0x3c]
00899557  A8 01                           test al, 1
00899559  0F 84 00 FD FF FF               je 0x14089925f
0089955F  49 8B 0C 24                     mov rcx, qword ptr [r12]
00899563  48 8B C1                        mov rax, rcx
00899566  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0089956C  48 3B C8                        cmp rcx, rax
0089956F  0F 85 EA FC FF FF               jne 0x14089925f
00899575  4C 39 6C 24 50                  cmp qword ptr [rsp + 0x50], r13
0089957A  0F 84 DF FC FF FF               je 0x14089925f
00899580  E9 C0 FB FF FF                  jmp 0x140899145
00899585  0F BA E9 09                     bts ecx, 9
00899589  0F BA F1 0A                     btr ecx, 0xa
0089958D  89 4B 2C                        mov dword ptr [rbx + 0x2c], ecx
00899590  E9 BD FB FF FF                  jmp 0x140899152
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMapViewOfSection(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;

    v_rsp = (v_rsp) - (168);
    result = (*(unsigned __int64 *)(v_rip + 5707797)) ^ (v_rsp);
    v_stack_m58 = result;
    result = 0;
    v_stack_m88 = v_xmm0;
    v_stack_mA8 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_mA0 = *(unsigned __int64 *)(a2 + 88);
    v_stack_m68 = v_xmm0;
    v_stack_m90 = a4;
    result = MiSectionControlArea(a1, a2, a3, a4);
    v_stack_m98 = *(unsigned __int64 *)(a2 + 24);
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_00899228;
loc_00898FA0:
    if (((*(unsigned int *)(a2 + 40)) & (0x40000000ULL)) != 0) goto loc_00899493;
loc_00898FAD:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 44))))) & (240));
    if (condition_is_not_equal) goto loc_008992C3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) != 0) goto loc_008992C3;
loc_00898FCB:
    if (condition_is_below) goto loc_008994AD;
loc_00898FD6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 120)))) & (8)) != 0) goto loc_008994D2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) != 0) goto loc_00899291;
loc_00898FF2:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 60))) & (0xFFFULL));
    result = MiMakeProtectionMask(a1, (unsigned int)(a7), (unsigned int)(*(unsigned int *)(a2 + 44)), (unsigned int)(0x2000ULL));
    result = (unsigned int)((result) & (7));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 8931578 + result * 4))) | (0x700ULL));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 44))) | ((unsigned int)(a1)));
    if (((unsigned int)(a3)) != ((unsigned int)(a1))) goto loc_0089946A;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)))) & (0x840000ULL)) != 0) goto loc_0089925F;
    if ((*(unsigned __int16 *)(a2 + 58)) != 0) goto loc_0089925F;
    if (((*(unsigned int *)(result + 56)) & (0x400ULL)) != 0) goto loc_008994EC;
loc_00899047:
    if ((*(unsigned __int64 *)(a2 + 24) + *(unsigned __int64 *)(a5) * 1) < (*(unsigned __int64 *)(a5))) goto loc_0089947E;
    if ((*(unsigned __int64 *)(a2 + 24) + *(unsigned __int64 *)(a5) * 1) > (*(unsigned __int64 *)(a1 + 48))) goto loc_00899474;
loc_00899068:
    if (*(unsigned __int64 *)(a2 + 24) == 0) {
        a1 = (*(unsigned __int64 *)(a1 + 48)) - (*(unsigned __int64 *)(a5));
        *(unsigned __int64 *)(a2 + 24) = a1;
    }
    if (((*(unsigned int *)(result + 56)) & (0x400ULL)) != 0) goto loc_0089926D;
    if ((*(unsigned __int64 *)(a2 + 16)) > ((unsigned int)(0x10000ULL))) goto loc_008994FD;
loc_0089908F:
    a2 = (*(unsigned __int64 *)(a2 + 16) - 1) & ((unsigned int)(*(unsigned int *)(a5)));
    if (condition_is_not_equal) goto loc_008993C6;
loc_0089909F:
    if ((*(unsigned __int64 *)(a2 + 24)) <= 0) goto loc_0089947E;
    if (((*(unsigned __int64 *)(a3)) & (*(unsigned __int64 *)(a2 + 16) - 1)) != 0) goto loc_008992AE;
loc_008990BE:
    *(unsigned __int64 *)(a2 + 32) = *(unsigned __int64 *)(a2 + 24);
    a2 = (unsigned int)((*(unsigned __int64 *)(a2 + 24)) & (0xFFFULL));
    if (condition_is_not_equal) goto loc_008992DC;
loc_008990DD:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 60))) & (1));
    if (condition_is_equal) { a3 = a2; }
    if ((*(unsigned __int64 *)(a3)) > (*(unsigned __int64 *)(a2 + 8))) goto loc_0089925F;
    a2 = (*(unsigned __int64 *)(a2 + 8)) - (*(unsigned __int64 *)(a3));
    a2 = (a2) + 1;
    if (a2 < (*(unsigned __int64 *)(a2 + 24))) goto loc_00899519;
    if (a4 > (*(unsigned __int64 *)(a2 + 24))) goto loc_0089952C;
loc_00899119:
    if ((*(unsigned __int64 *)(a2 + 24)) > (*(unsigned __int64 *)(a1 + 48))) goto loc_00899488;
loc_00899123:
    if ((((unsigned int)((unsigned int)(0x2000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40))))) != 0) goto loc_0089945F;
loc_0089912E:
    if (condition_is_below) goto loc_008992F6;
loc_00899138:
    if (((*(unsigned int *)(a2 + 64)) & (0x4000000ULL)) != 0) goto loc_0089953A;
loc_00899145:
    if (((*(unsigned __int16 *)(*(unsigned __int64 *)(result) + 12)) & ((unsigned __int16)((unsigned int)(0x2000ULL)))) != 0) goto loc_00899585;
loc_00899152:
    if (condition_is_below) goto loc_008992CC;
loc_0089915E:
    result = MiMakeProtectionMask((unsigned int)(*(unsigned int *)(a2 + 44)), (unsigned int)(0x2000ULL), *(unsigned __int64 *)(a3), *(unsigned __int64 *)(a2 + 24));
    if (((unsigned int)(result)) == -1) goto loc_00899266;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a2 + 96) + 1872)) & (256)) != 0) goto loc_00899380;
loc_00899183:
    v_r13 = 0;
    if ((*(unsigned __int64 *)(a2 + 96)) != (*(unsigned __int64 *)(a2 + 88))) {
        a2 = v_stack_m88;
        a1 = *(unsigned __int64 *)(a2 + 88);
        result = KeStackAttachProcess(a1, a2, *(unsigned __int64 *)(a2 + 96), *(unsigned __int64 *)(a2 + 24));
        v_r13 = 1;
    }
    result = MiValidateVadMetadataFlags(a2, a2, *(unsigned __int64 *)(a2 + 96), *(unsigned __int64 *)(a2 + 24));
    if (sign_flag) goto loc_008991F0;
    if (condition_is_below) goto loc_00899310;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56)))) & (32)) != 0) goto loc_00899323;
    v_stack_mB0 = v_stack_m90;
    v_stack_mB8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_mC0 = (unsigned int)((unsigned int)(a6));
    v_stack_mC8 = a1;
    result = MiMapViewOfDataSection(result, a2, a3, a5);
loc_008991EE:
loc_008991F0:
    if ((unsigned int)(v_r13) != 0) {
        a2 = 0;
        a1 = v_stack_m88;
        result = KiUnstackDetachProcess(a1, a2, a3, a5);
    }
loc_00899203:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a5);
    v_rsp = (v_rsp) + (168);
    return result;
loc_00899228:
    result = (unsigned int)(((unsigned int)(a6)) - 1);
    if (((unsigned int)(result)) > 1) goto loc_0089925F;
    if (((*(unsigned int *)(result + 56)) & (0x400ULL)) != 0) goto loc_00899252;
    if ((*(unsigned __int64 *)(a2 + 16)) < v_r10) goto loc_00899252;
    if ((*(unsigned __int16 *)(a3)) != ((unsigned __int16)(v_r13))) goto loc_008992B9;
    if ((*(unsigned __int16 *)(a5)) != ((unsigned __int16)(v_r13))) goto loc_008992B9;
loc_00899252:
    if (((*(unsigned int *)(a2 + 40)) & (0x9F2BDFFFULL)) == 0) goto loc_00898FA0;
loc_0089925F:
    goto loc_00899203;
loc_00899266:
    goto loc_00899203;
loc_0089926D:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a5)))) & (0xFFFULL)) == 0) goto loc_0089909F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 60)))) & (2)) != 0) goto loc_008992B9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a5))) & (0xFFFFF000ULL));
    *(unsigned int *)(a5) = (unsigned int)(a1);
    goto loc_0089909F;
loc_00899291:
    if ((*(unsigned __int64 *)(a2 + 72)) != v_r13) goto loc_0089925F;
    if ((((unsigned int)(a5)) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40))))) != 0) goto loc_0089925F;
    if (condition_is_above_or_equal) goto loc_00899047;
loc_008992AE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 60)))) & (2)) == 0) goto loc_0089950A;
loc_008992B9:
    goto loc_00899203;
loc_008992C3:
    goto loc_00898FCB;
loc_008992CC:
    *(unsigned int *)(a2 + 44) = (unsigned int)(a1);
    goto loc_0089915E;
loc_008992DC:
    result = (unsigned int)(((unsigned int)(0xC0000220ULL)) - (0));
    a4 = ((unsigned int)((unsigned int)(result))) + (a1);
    if (a4 < a1) goto loc_0089947E;
    *(unsigned __int64 *)(a2 + 24) = a4;
    goto loc_008990DD;
loc_008992F6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) == 0) goto loc_0089925F;
    if (condition_is_above_or_equal) goto loc_00899138;
    goto loc_0089925F;
loc_00899310:
    result = MiMapViewOfPhysicalSection(a1, a3, a5, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_008991EE;
loc_00899323:
    v_stack_p38 = 0;
    v_stack_p40 = *(unsigned __int64 *)(a3);
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_p28 = (unsigned int)((unsigned int)(a6));
    v_stack_p20 = a1;
    result = MiMapViewOfImageSection(result, 0, v_stack_p40, a5);
    if (condition_is_below) goto loc_0089940B;
    if (sign_flag) goto loc_008991F0;
loc_00899372:
    *(unsigned __int64 *)(a3) = v_stack_p40;
    goto loc_008991F0;
loc_00899380:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)) & (0x40000ULL)) != 0) goto loc_00899183;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) != 0) goto loc_008993FF;
    a2 = (((*(unsigned int *)(a2 + 64)) & (0x20000000ULL)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (2)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a2))) == 0) goto loc_00899183;
    result = MiArbitraryCodeBlocked(v_stack_p40, a2, v_stack_p40, a5);
    goto loc_00899203;
loc_008993C6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 60)))) & (2)) != 0) goto loc_008992B9;
    a1 = (unsigned int)(-(v_stack_p40));
    a1 = (unsigned int)((a1) & ((unsigned int)(v_stack_p40)));
    *(unsigned int *)(a5) = (unsigned int)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56)))) & (32)) != 0) goto loc_0089909F;
    if ((*(unsigned __int64 *)(a2 + 24) + a2 * 1) < (*(unsigned __int64 *)(a2 + 24))) goto loc_0089947E;
    *(unsigned __int64 *)(a2 + 24) = *(unsigned __int64 *)(a2 + 24) + a2 * 1;
    goto loc_0089909F;
loc_008993FF:
    goto loc_00899183;
loc_0089940B:
    *(unsigned int *)(a2 + 40) = (unsigned int)(*(unsigned __int64 *)(a2 + 24));
    if (sign_flag) goto loc_00899323;
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_p28 = (unsigned int)((unsigned int)(a6));
    v_stack_p20 = a1;
    result = MiFinalizeLagePageImageMapping(result, a2, v_stack_p40, a5);
    goto loc_00899372;
loc_0089945F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 60)))) & (68)) != 0) goto loc_0089912E;
loc_0089946A:
    goto loc_00899203;
loc_00899474:
    if (((*(unsigned int *)(a2 + 40)) & ((unsigned int)(a5))) != 0) goto loc_00899068;
loc_0089947E:
    goto loc_00899203;
loc_00899488:
    if (((*(unsigned int *)(a2 + 40)) & ((unsigned int)(a2))) != 0) goto loc_00899123;
    goto loc_0089947E;
loc_00899493:
    if ((unsigned int)(a2) != 0) goto loc_00898FAD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 88) + 1600)) == v_r13) goto loc_0089925F;
    goto loc_00898FAD;
loc_008994AD:
    if ((unsigned int)(result) == 0) goto loc_0089925F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) != 0) goto loc_0089925F;
    *(unsigned int *)(a2 + 44) = (unsigned int)(v_stack_p40);
    goto loc_00898FD6;
loc_008994D2:
    if ((((unsigned __int8)(v_stack_p40)) & (240)) == 0) goto loc_0089925F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) != 0) goto loc_0089925F;
    goto loc_00898FF2;
loc_008994EC:
    if ((((unsigned int)(result)) & (0x20002000ULL)) != 0) goto loc_0089925F;
    goto loc_00899047;
loc_008994FD:
    a1 = result;
    if ((*(unsigned __int64 *)(result + 64)) != v_r13) { a1 = v_r10; }
    goto loc_0089908F;
loc_0089950A:
    a1 = -(a1);
    a1 = (a1) & (a2);
    *(unsigned __int64 *)(a3) = a1;
    goto loc_008990BE;
loc_00899519:
    result = ((unsigned int)(v_r10) != 0) ? 1 : 0;
    result = (unsigned int)((result) + (0xC0000017ULL));
    goto loc_00899203;
loc_0089952C:
    if (((*(unsigned int *)(a2 + 40)) & ((unsigned int)(a2))) == 0) goto loc_0089925F;
    goto loc_00899119;
loc_0089953A:
    if (((*(unsigned int *)(result + 56)) & (0x420ULL)) != 0) goto loc_0089925F;
    if ((((unsigned int)(a1)) & (0xFFFFDFFFULL)) != 0) goto loc_0089925F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 60)))) & (1)) == 0) goto loc_0089925F;
    result = (*(unsigned __int64 *)(a3)) & (0xFFFFFFFFFFFFF000ULL);
    if ((*(unsigned __int64 *)(a3)) != result) goto loc_0089925F;
    if (v_stack_p50 == v_r13) goto loc_0089925F;
    goto loc_00899145;
loc_00899585:
    *(unsigned int *)(a2 + 44) = (unsigned int)(*(unsigned __int64 *)(a3));
    goto loc_00899152;
}
```

## 5. (Beta) C Style

```c
int64_t MiMapViewOfSection(void *Arg1, void *Arg2, void *Arg3, int64_t Arg4, void *Arg5, uint32_t Arg6, uint32_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;

    local_rsp = (local_rsp) - (168);
    result = (*(uint64_t *)(v_rip + 0x571815)) ^ (local_rsp);
    v_stack_m58 = result;
    result = 0;
    v_stack_m88 = v_xmm0;
    v_stack_mA8 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_mA0 = *(uint64_t *)(arg2 + 0x58);
    v_stack_m68 = v_xmm0;
    v_stack_m90 = Arg4;
    result = MiSectionControlArea(Arg1, Arg2, Arg3, Arg4);
    v_stack_m98 = *(uint64_t *)(arg2 + 0x18);
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_00899228;
loc_00898FA0:
    if (((*(uint32_t *)(arg2 + 0x28)) & (0x40000000ULL)) != 0) goto loc_00899493;
loc_00898FAD:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x2C))))) & (240));
    if (condition_is_not_equal) goto loc_008992C3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) != 0) goto loc_008992C3;
loc_00898FCB:
    if (condition_is_below) goto loc_008994AD;
loc_00898FD6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x78)))) & (8)) != 0) goto loc_008994D2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) != 0) goto loc_00899291;
loc_00898FF2:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x3C))) & (0xFFFULL));
    result = MiMakeProtectionMask(Arg1, (uint32_t)(Arg7), (uint32_t)(*(uint32_t *)(arg2 + 0x2C)), (uint32_t)(0x2000ULL));
    result = (uint32_t)((result) & (7));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x8848FA + result * 4))) | (0x700ULL));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x2C))) | ((uint32_t)(Arg1)));
    if (((uint32_t)(Arg3)) != ((uint32_t)(Arg1))) goto loc_0089946A;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)))) & (0x840000ULL)) != 0) goto loc_0089925F;
    if ((*(uint16_t *)(arg2 + 0x3A)) != 0) goto loc_0089925F;
    if (((*(uint32_t *)(result + 0x38)) & (0x400ULL)) != 0) goto loc_008994EC;
loc_00899047:
    if ((*(uint64_t *)(arg2 + 0x18) + *(uint64_t *)(arg5) * 1) < (*(uint64_t *)(arg5))) goto loc_0089947E;
    if ((*(uint64_t *)(arg2 + 0x18) + *(uint64_t *)(arg5) * 1) > (*(uint64_t *)(arg1 + 0x30))) goto loc_00899474;
loc_00899068:
    if (*(uint64_t *)(arg2 + 0x18) == 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x30)) - (*(uint64_t *)(arg5));
        *(void **)(arg2 + 0x18) = Arg1;
    }
    if (((*(uint32_t *)(result + 0x38)) & (0x400ULL)) != 0) goto loc_0089926D;
    if ((*(uint64_t *)(arg2 + 0x10)) > ((uint32_t)(0x10000ULL))) goto loc_008994FD;
loc_0089908F:
    Arg2 = (*(uint64_t *)(arg2 + 0x10) - 1) & ((uint32_t)(*(uint32_t *)(arg5)));
    if (condition_is_not_equal) goto loc_008993C6;
loc_0089909F:
    if ((*(uint64_t *)(arg2 + 0x18)) <= 0) goto loc_0089947E;
    if (((*(uint64_t *)(arg3)) & (*(uint64_t *)(arg2 + 0x10) - 1)) != 0) goto loc_008992AE;
loc_008990BE:
    *(uint64_t *)(arg2 + 0x20) = *(uint64_t *)(arg2 + 0x18);
    Arg2 = (uint32_t)((*(uint64_t *)(arg2 + 0x18)) & (0xFFFULL));
    if (condition_is_not_equal) goto loc_008992DC;
loc_008990DD:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x3C))) & (1));
    if (condition_is_equal) { Arg3 = Arg2; }
    if ((*(uint64_t *)(arg3)) > (*(uint64_t *)(arg2 + 0x8))) goto loc_0089925F;
    Arg2 = (*(uint64_t *)(arg2 + 0x8)) - (*(uint64_t *)(arg3));
    Arg2 = (Arg2) + 1;
    if (Arg2 < (*(uint64_t *)(arg2 + 0x18))) goto loc_00899519;
    if (Arg4 > (*(uint64_t *)(arg2 + 0x18))) goto loc_0089952C;
loc_00899119:
    if ((*(uint64_t *)(arg2 + 0x18)) > (*(uint64_t *)(arg1 + 0x30))) goto loc_00899488;
loc_00899123:
    if ((((uint32_t)((uint32_t)(0x2000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28))))) != 0) goto loc_0089945F;
loc_0089912E:
    if (condition_is_below) goto loc_008992F6;
loc_00899138:
    if (((*(uint32_t *)(arg2 + 0x40)) & (0x4000000ULL)) != 0) goto loc_0089953A;
loc_00899145:
    if (((*(uint16_t *)(*(uint64_t *)(result) + 0xC)) & ((uint16_t)((uint32_t)(0x2000ULL)))) != 0) goto loc_00899585;
loc_00899152:
    if (condition_is_below) goto loc_008992CC;
loc_0089915E:
    result = MiMakeProtectionMask((uint32_t)(*(uint32_t *)(arg2 + 0x2C)), (uint32_t)(0x2000ULL), *(uint64_t *)(arg3), *(uint64_t *)(arg2 + 0x18));
    if (((uint32_t)(result)) == -1) goto loc_00899266;
    if (((*(uint32_t *)(*(uint64_t *)(arg2 + 0x60) + 0x750)) & (256)) != 0) goto loc_00899380;
loc_00899183:
    local_r13 = 0;
    if ((*(uint64_t *)(arg2 + 0x60)) != (*(uint64_t *)(arg2 + 0x58))) {
        Arg2 = v_stack_m88;
        Arg1 = *(uint64_t *)(arg2 + 0x58);
        result = KeStackAttachProcess(Arg1, Arg2, *(uint64_t *)(arg2 + 0x60), *(uint64_t *)(arg2 + 0x18));
        local_r13 = 1;
    }
    result = MiValidateVadMetadataFlags(Arg2, Arg2, *(uint64_t *)(arg2 + 0x60), *(uint64_t *)(arg2 + 0x18));
    if (sign_flag) goto loc_008991F0;
    if (condition_is_below) goto loc_00899310;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38)))) & (32)) != 0) goto loc_00899323;
    v_stack_mB0 = v_stack_m90;
    v_stack_mB8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_mC0 = (uint32_t)((uint32_t)(Arg6));
    v_stack_mC8 = Arg1;
    result = MiMapViewOfDataSection(result, Arg2, Arg3, Arg5);
loc_008991EE:
loc_008991F0:
    if ((uint32_t)(local_r13) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m88;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, Arg5);
    }
loc_00899203:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg5);
    local_rsp = (local_rsp) + (168);
    return result;
loc_00899228:
    result = (uint32_t)(((uint32_t)(Arg6)) - 1);
    if (((uint32_t)(result)) > 1) goto loc_0089925F;
    if (((*(uint32_t *)(result + 0x38)) & (0x400ULL)) != 0) goto loc_00899252;
    if ((*(uint64_t *)(arg2 + 0x10)) < local_r10) goto loc_00899252;
    if ((*(uint16_t *)(arg3)) != ((uint16_t)(local_r13))) goto loc_008992B9;
    if ((*(uint16_t *)(arg5)) != ((uint16_t)(local_r13))) goto loc_008992B9;
loc_00899252:
    if (((*(uint32_t *)(arg2 + 0x28)) & (0x9F2BDFFFULL)) == 0) goto loc_00898FA0;
loc_0089925F:
    goto loc_00899203;
loc_00899266:
    goto loc_00899203;
loc_0089926D:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg5)))) & (0xFFFULL)) == 0) goto loc_0089909F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x3C)))) & (2)) != 0) goto loc_008992B9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5))) & (0xFFFFF000ULL));
    *(uint32_t *)(arg5) = (uint32_t)(Arg1);
    goto loc_0089909F;
loc_00899291:
    if ((*(uint64_t *)(arg2 + 0x48)) != local_r13) goto loc_0089925F;
    if ((((uint32_t)(Arg5)) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28))))) != 0) goto loc_0089925F;
    if (condition_is_above_or_equal) goto loc_00899047;
loc_008992AE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x3C)))) & (2)) == 0) goto loc_0089950A;
loc_008992B9:
    goto loc_00899203;
loc_008992C3:
    goto loc_00898FCB;
loc_008992CC:
    *(uint32_t *)(arg2 + 0x2C) = (uint32_t)(Arg1);
    goto loc_0089915E;
loc_008992DC:
    result = (uint32_t)(((uint32_t)(0xC0000220ULL)) - (0));
    Arg4 = ((uint32_t)((uint32_t)(result))) + (Arg1);
    if (Arg4 < Arg1) goto loc_0089947E;
    *(uint64_t *)(arg2 + 0x18) = Arg4;
    goto loc_008990DD;
loc_008992F6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) == 0) goto loc_0089925F;
    if (condition_is_above_or_equal) goto loc_00899138;
    goto loc_0089925F;
loc_00899310:
    result = MiMapViewOfPhysicalSection(Arg1, Arg3, Arg5, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_008991EE;
loc_00899323:
    v_stack_p38 = 0;
    v_stack_p40 = *(uint64_t *)(arg3);
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_p28 = (uint32_t)((uint32_t)(Arg6));
    v_stack_p20 = Arg1;
    result = MiMapViewOfImageSection(result, 0, v_stack_p40, Arg5);
    if (condition_is_below) goto loc_0089940B;
    if (sign_flag) goto loc_008991F0;
loc_00899372:
    *(uint64_t *)(arg3) = v_stack_p40;
    goto loc_008991F0;
loc_00899380:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)) & (0x40000ULL)) != 0) goto loc_00899183;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) != 0) goto loc_008993FF;
    Arg2 = (((*(uint32_t *)(arg2 + 0x40)) & (0x20000000ULL)) == 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (2)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg2))) == 0) goto loc_00899183;
    result = MiArbitraryCodeBlocked(v_stack_p40, Arg2, v_stack_p40, Arg5);
    goto loc_00899203;
loc_008993C6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x3C)))) & (2)) != 0) goto loc_008992B9;
    Arg1 = (uint32_t)(-(v_stack_p40));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(v_stack_p40)));
    *(uint32_t *)(arg5) = (uint32_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38)))) & (32)) != 0) goto loc_0089909F;
    if ((*(uint64_t *)(arg2 + 0x18) + Arg2 * 1) < (*(uint64_t *)(arg2 + 0x18))) goto loc_0089947E;
    *(uint64_t *)(arg2 + 0x18) = *(uint64_t *)(arg2 + 0x18) + Arg2 * 1;
    goto loc_0089909F;
loc_008993FF:
    goto loc_00899183;
loc_0089940B:
    *(uint32_t *)(arg2 + 0x28) = (uint32_t)(*(uint64_t *)(arg2 + 0x18));
    if (sign_flag) goto loc_00899323;
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_p28 = (uint32_t)((uint32_t)(Arg6));
    v_stack_p20 = Arg1;
    result = MiFinalizeLagePageImageMapping(result, Arg2, v_stack_p40, Arg5);
    goto loc_00899372;
loc_0089945F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)))) & (68)) != 0) goto loc_0089912E;
loc_0089946A:
    goto loc_00899203;
loc_00899474:
    if (((*(uint32_t *)(arg2 + 0x28)) & ((uint32_t)(Arg5))) != 0) goto loc_00899068;
loc_0089947E:
    goto loc_00899203;
loc_00899488:
    if (((*(uint32_t *)(arg2 + 0x28)) & ((uint32_t)(Arg2))) != 0) goto loc_00899123;
    goto loc_0089947E;
loc_00899493:
    if ((uint32_t)(Arg2) != 0) goto loc_00898FAD;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x58) + 0x640)) == local_r13) goto loc_0089925F;
    goto loc_00898FAD;
loc_008994AD:
    if ((uint32_t)(result) == 0) goto loc_0089925F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) != 0) goto loc_0089925F;
    *(uint32_t *)(arg2 + 0x2C) = (uint32_t)(v_stack_p40);
    goto loc_00898FD6;
loc_008994D2:
    if ((((uint8_t)(v_stack_p40)) & (240)) == 0) goto loc_0089925F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) != 0) goto loc_0089925F;
    goto loc_00898FF2;
loc_008994EC:
    if ((((uint32_t)(result)) & (0x20002000ULL)) != 0) goto loc_0089925F;
    goto loc_00899047;
loc_008994FD:
    Arg1 = result;
    if ((*(uint64_t *)(result + 0x40)) != local_r13) { Arg1 = local_r10; }
    goto loc_0089908F;
loc_0089950A:
    Arg1 = -(Arg1);
    Arg1 = (Arg1) & (Arg2);
    *(void **)(arg3) = Arg1;
    goto loc_008990BE;
loc_00899519:
    result = ((uint32_t)(local_r10) != 0) ? 1 : 0;
    result = (uint32_t)((result) + (0xC0000017ULL));
    goto loc_00899203;
loc_0089952C:
    if (((*(uint32_t *)(arg2 + 0x28)) & ((uint32_t)(Arg2))) == 0) goto loc_0089925F;
    goto loc_00899119;
loc_0089953A:
    if (((*(uint32_t *)(result + 0x38)) & (0x420ULL)) != 0) goto loc_0089925F;
    if ((((uint32_t)(Arg1)) & (0xFFFFDFFFULL)) != 0) goto loc_0089925F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x3C)))) & (1)) == 0) goto loc_0089925F;
    result = (*(uint64_t *)(arg3)) & (0xFFFFFFFFFFFFF000ULL);
    if ((*(uint64_t *)(arg3)) != result) goto loc_0089925F;
    if (v_stack_p50 == local_r13) goto loc_0089925F;
    goto loc_00899145;
loc_00899585:
    *(uint32_t *)(arg2 + 0x2C) = (uint32_t)(*(uint64_t *)(arg3));
    goto loc_00899152;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x3C` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x20` | `64` | `W` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R/W` |
| `Arg2` | `+ 0x28` | `32` | `W` |
| `Arg2` | `+ 0x2C` | `32` | `R` |
| `Arg2` | `+ 0x2C` | `32` | `W` |
| `Arg2` | `+ 0x3A` | `16` | `R` |
| `Arg2` | `+ 0x3C` | `32` | `R` |
| `Arg2` | `+ 0x3C` | `32` | `R/W` |
| `Arg2` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x78` | `32` | `R` |
| `Arg2` | `+ 0x78` | `32` | `R/W` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg5` | `+ 0x0` | `16` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg5` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00898F10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
