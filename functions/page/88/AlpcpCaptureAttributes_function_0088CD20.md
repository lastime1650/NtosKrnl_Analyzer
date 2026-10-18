# AlpcpCaptureAttributes

- RVA: `0x0088CD20`–`0x0088D28F` (길이 `1,391` bytes)
- VA: `0x000000014088CD20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D428`
- 디코드: `362`개 명령, `1,391/1,391` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0088CDFE` → [AlpcpCaptureContextAttribute](AlpcpCaptureContextAttribute_function_0088DCC0.md) (function, `0x0088DCC0`)
- `0x0088CE32` → [AlpcpReleaseAttributes](AlpcpReleaseAttributes_function_0088D750.md) (function, `0x0088D750`)
- `0x0088CF06` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0088CFB8` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x0088CFE9` → [AlpcpCaptureSecurityAttribute](../89/AlpcpCaptureSecurityAttribute_function_00890540.md) (function, `0x00890540`)
- `0x0088D04B` → [AlpcpCaptureContextAttribute32](../A1/AlpcpCaptureContextAttribute32_function_00A1DD08.md) (function, `0x00A1DD08`)
- `0x0088D07C` → [AlpcpCaptureWorkOnBehalfAttribute](../9D/AlpcpCaptureWorkOnBehalfAttribute_function_009D6D10.md) (function, `0x009D6D10`)
- `0x0088D0AA` → [AlpcpCaptureViewAttribute](AlpcpCaptureViewAttribute_function_0088957C.md) (function, `0x0088957C`)
- `0x0088D115` → [AlpcpCaptureDirectAttribute](../A1/AlpcpCaptureDirectAttribute_function_00A126AC.md) (function, `0x00A126AC`)
- `0x0088D134` → [AlpcpCaptureSecurityAttribute32](../A2/AlpcpCaptureSecurityAttribute32_function_00A20924.md) (function, `0x00A20924`)
- `0x0088D184` → [AlpcpCaptureHandleAttribute](../89/AlpcpCaptureHandleAttribute_function_0089335C.md) (function, `0x0089335C`)
- `0x0088D1EF` → [AlpcpCaptureDirectAttribute32](../A2/AlpcpCaptureDirectAttribute32_function_00A27044.md) (function, `0x00A27044`)
- `0x0088D225` → [AlpcpCaptureViewAttribute32](../A6/AlpcpCaptureViewAttribute32_function_00A61E68.md) (function, `0x00A61E68`)
- `0x0088D27A` → [AlpcpCaptureHandleAttribute32](../AB/AlpcpCaptureHandleAttribute32_function_00AB8238.md) (function, `0x00AB8238`)

### Direct callers
- [AlpcpSendMessage](AlpcpSendMessage_function_0088BD40.md) at `0x0088C3E8`
- [AlpcpFormatConnectionRequest](../92/AlpcpFormatConnectionRequest_function_00922A40.md) at `0x00922AC9`
- [AlpcpAcceptConnectPort](../A3/AlpcpAcceptConnectPort_function_00A34290.md) at `0x00A34B2B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0088CD20  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0088CD25  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0088CD2A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0088CD2F  57                              push rdi
0088CD30  41 54                           push r12
0088CD32  41 55                           push r13
0088CD34  41 56                           push r14
0088CD36  41 57                           push r15
0088CD38  48 83 EC 40                     sub rsp, 0x40
0088CD3C  4D 8B E9                        mov r13, r9
0088CD3F  49 8B F0                        mov rsi, r8
0088CD42  44 8B E2                        mov r12d, edx
0088CD45  4C 8B D1                        mov r10, rcx
0088CD48  0F 57 C0                        xorps xmm0, xmm0
0088CD4B  33 C0                           xor eax, eax
0088CD4D  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0088CD55  0F 11 03                        movups xmmword ptr [rbx], xmm0
0088CD58  0F 11 43 10                     movups xmmword ptr [rbx + 0x10], xmm0
0088CD5C  0F 11 43 20                     movups xmmword ptr [rbx + 0x20], xmm0
0088CD60  0F 11 43 30                     movups xmmword ptr [rbx + 0x30], xmm0
0088CD64  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
0088CD68  49 8B 41 68                     mov rax, qword ptr [r9 + 0x68]
0088CD6C  48 89 03                        mov qword ptr [rbx], rax
0088CD6F  49 8B 41 70                     mov rax, qword ptr [r9 + 0x70]
0088CD73  48 89 43 08                     mov qword ptr [rbx + 8], rax
0088CD77  4D 85 C0                        test r8, r8
0088CD7A  0F 84 58 02 00 00               je 0x14088cfd8
0088CD80  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088CD89  80 B8 32 02 00 00 00            cmp byte ptr [rax + 0x232], 0
0088CD90  0F 85 C0 00 00 00               jne 0x14088ce56
0088CD96  45 8B 38                        mov r15d, dword ptr [r8]
0088CD99  41 8B 78 04                     mov edi, dword ptr [r8 + 4]
0088CD9D  41 8B C7                        mov eax, r15d
0088CDA0  F7 D0                           not eax
0088CDA2  85 C7                           test edi, eax
0088CDA4  0F 85 90 04 00 00               jne 0x14088d23a
0088CDAA  45 33 F6                        xor r14d, r14d
0088CDAD  45 85 E4                        test r12d, r12d
0088CDB0  0F 88 4D 02 00 00               js 0x14088d003
0088CDB6  85 FF                           test edi, edi
0088CDB8  0F 88 21 02 00 00               js 0x14088cfdf
0088CDBE  0F BA E7 1E                     bt edi, 0x1e
0088CDC2  0F 82 C1 02 00 00               jb 0x14088d089
0088CDC8  0F BA E7 1D                     bt edi, 0x1d
0088CDCC  73 3C                           jae 0x14088ce0a
0088CDCE  41 8B C7                        mov eax, r15d
0088CDD1  25 00 00 00 C0                  and eax, 0xc0000000
0088CDD6  48 63 C8                        movsxd rcx, eax
0088CDD9  48 C1 F9 3F                     sar rcx, 0x3f
0088CDDD  83 E1 18                        and ecx, 0x18
0088CDE0  48 83 C1 08                     add rcx, 8
0088CDE4  0F BA E0 1E                     bt eax, 0x1e
0088CDE8  48 8D 51 20                     lea rdx, [rcx + 0x20]
0088CDEC  48 0F 43 D1                     cmovae rdx, rcx
0088CDF0  48 03 D6                        add rdx, rsi
0088CDF3  4C 8B CB                        mov r9, rbx
0088CDF6  4D 8B C5                        mov r8, r13
0088CDF9  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0088CDFE  E8 BD 0E 00 00                  call 0x14088dcc0
0088CE03  44 8B F0                        mov r14d, eax
0088CE06  85 C0                           test eax, eax
0088CE08  78 1E                           js 0x14088ce28
0088CE0A  0F BA E7 1C                     bt edi, 0x1c
0088CE0E  0F 82 3A 03 00 00               jb 0x14088d14e
0088CE14  0F BA E7 1A                     bt edi, 0x1a
0088CE18  0F 82 A1 02 00 00               jb 0x14088d0bf
0088CE1E  0F BA E7 19                     bt edi, 0x19
0088CE22  0F 82 51 02 00 00               jb 0x14088d079
0088CE28  45 85 F6                        test r14d, r14d
0088CE2B  79 0A                           jns 0x14088ce37
0088CE2D  48 8B D3                        mov rdx, rbx
0088CE30  33 C9                           xor ecx, ecx
0088CE32  E8 19 09 00 00                  call 0x14088d750
0088CE37  41 8B C6                        mov eax, r14d
0088CE3A  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
0088CE3F  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0088CE47  48 83 C4 40                     add rsp, 0x40
0088CE4B  41 5F                           pop r15
0088CE4D  41 5E                           pop r14
0088CE4F  41 5D                           pop r13
0088CE51  41 5C                           pop r12
0088CE53  5F                              pop rdi
0088CE54  C3                              ret
0088CE55  CC                              int3
0088CE56  45 32 C0                        xor r8b, r8b
0088CE59  44 88 44 24 30                  mov byte ptr [rsp + 0x30], r8b
0088CE5E  49 B9 00 00 FF FF FF 7F 00 00   movabs r9, 0x7fffffff0000
0088CE68  49 8B C1                        mov rax, r9
0088CE6B  49 3B F1                        cmp rsi, r9
0088CE6E  48 0F 42 C6                     cmovb rax, rsi
0088CE72  90                              nop
0088CE73  44 8B 38                        mov r15d, dword ptr [rax]
0088CE76  41 8B C4                        mov eax, r12d
0088CE79  25 00 00 00 C0                  and eax, 0xc0000000
0088CE7E  41 8B CF                        mov ecx, r15d
0088CE81  C1 F9 1F                        sar ecx, 0x1f
0088CE84  3D 00 00 00 80                  cmp eax, 0x80000000
0088CE89  0F 84 DC 00 00 00               je 0x14088cf6b
0088CE8F  83 E1 18                        and ecx, 0x18
0088CE92  83 C1 08                        add ecx, 8
0088CE95  41 0F BA E7 1E                  bt r15d, 0x1e
0088CE9A  8D 41 20                        lea eax, [rcx + 0x20]
0088CE9D  0F 43 C1                        cmovae eax, ecx
0088CEA0  41 0F BA E7 1D                  bt r15d, 0x1d
0088CEA5  8D 48 20                        lea ecx, [rax + 0x20]
0088CEA8  0F 43 C8                        cmovae ecx, eax
0088CEAB  41 0F BA E7 1C                  bt r15d, 0x1c
0088CEB0  8D 41 18                        lea eax, [rcx + 0x18]
0088CEB3  0F 43 C1                        cmovae eax, ecx
0088CEB6  41 0F BA E7 1B                  bt r15d, 0x1b
0088CEBB  8D 48 18                        lea ecx, [rax + 0x18]
0088CEBE  0F 43 C8                        cmovae ecx, eax
0088CEC1  41 0F BA E7 1A                  bt r15d, 0x1a
0088CEC6  8D 41 08                        lea eax, [rcx + 8]
0088CEC9  0F 43 C1                        cmovae eax, ecx
0088CECC  41 0F BA E7 19                  bt r15d, 0x19
0088CED1  8D 50 08                        lea edx, [rax + 8]
0088CED4  0F 43 D0                        cmovae edx, eax
0088CED7  B9 08 00 00 00                  mov ecx, 8
0088CEDC  41 F7 C7 00 00 00 A0            test r15d, 0xa0000000
0088CEE3  74 08                           je 0x14088ceed
0088CEE5  41 B0 01                        mov r8b, 1
0088CEE8  44 88 44 24 30                  mov byte ptr [rsp + 0x30], r8b
0088CEED  45 84 C0                        test r8b, r8b
0088CEF0  74 38                           je 0x14088cf2a
0088CEF2  48 81 FA 00 10 00 00            cmp rdx, 0x1000
0088CEF9  0F 83 B3 00 00 00               jae 0x14088cfb2
0088CEFF  FF C9                           dec ecx
0088CF01  48 85 CE                        test rsi, rcx
0088CF04  74 06                           je 0x14088cf0c
0088CF06  E8 C5 D0 00 00                  call 0x140899fd0
0088CF0B  CC                              int3
0088CF0C  49 3B F1                        cmp rsi, r9
0088CF0F  4C 0F 42 CE                     cmovb r9, rsi
0088CF13  41 0F B6 01                     movzx eax, byte ptr [r9]
0088CF17  41 88 01                        mov byte ptr [r9], al
0088CF1A  41 0F B6 44 11 FF               movzx eax, byte ptr [r9 + rdx - 1]
0088CF20  41 88 44 11 FF                  mov byte ptr [r9 + rdx - 1], al
0088CF25  E9 98 00 00 00                  jmp 0x14088cfc2
0088CF2A  48 8D 42 FF                     lea rax, [rdx - 1]
0088CF2E  48 3D FE FF 00 00               cmp rax, 0xfffe
0088CF34  76 20                           jbe 0x14088cf56
0088CF36  48 85 D2                        test rdx, rdx
0088CF39  0F 84 83 00 00 00               je 0x14088cfc2
0088CF3F  FF C9                           dec ecx
0088CF41  48 85 CE                        test rsi, rcx
0088CF44  75 C0                           jne 0x14088cf06
0088CF46  48 8D 04 32                     lea rax, [rdx + rsi]
0088CF4A  49 3B C1                        cmp rax, r9
0088CF4D  77 16                           ja 0x14088cf65
0088CF4F  48 3B C6                        cmp rax, rsi
0088CF52  72 11                           jb 0x14088cf65
0088CF54  EB 6C                           jmp 0x14088cfc2
0088CF56  FF C9                           dec ecx
0088CF58  48 85 CE                        test rsi, rcx
0088CF5B  75 A9                           jne 0x14088cf06
0088CF5D  49 3B F1                        cmp rsi, r9
0088CF60  4C 0F 42 CE                     cmovb r9, rsi
0088CF64  90                              nop
0088CF65  41 0F B6 01                     movzx eax, byte ptr [r9]
0088CF69  EB 57                           jmp 0x14088cfc2
0088CF6B  83 E1 0C                        and ecx, 0xc
0088CF6E  83 C1 08                        add ecx, 8
0088CF71  41 0F BA E7 1E                  bt r15d, 0x1e
0088CF76  8D 41 10                        lea eax, [rcx + 0x10]
0088CF79  0F 43 C1                        cmovae eax, ecx
0088CF7C  41 0F BA E7 1D                  bt r15d, 0x1d
0088CF81  8D 48 14                        lea ecx, [rax + 0x14]
0088CF84  0F 43 C8                        cmovae ecx, eax
0088CF87  41 0F BA E7 1C                  bt r15d, 0x1c
0088CF8C  8D 41 10                        lea eax, [rcx + 0x10]
0088CF8F  0F 43 C1                        cmovae eax, ecx
0088CF92  41 0F BA E7 1B                  bt r15d, 0x1b
0088CF97  8D 48 18                        lea ecx, [rax + 0x18]
0088CF9A  0F 43 C8                        cmovae ecx, eax
0088CF9D  41 0F BA E7 19                  bt r15d, 0x19
0088CFA2  8D 51 08                        lea edx, [rcx + 8]
0088CFA5  0F 43 D1                        cmovae edx, ecx
0088CFA8  B9 04 00 00 00                  mov ecx, 4
0088CFAD  E9 2A FF FF FF                  jmp 0x14088cedc
0088CFB2  44 8B C1                        mov r8d, ecx
0088CFB5  48 8B CE                        mov rcx, rsi
0088CFB8  E8 03 C2 05 00                  call 0x1408e91c0
0088CFBD  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
0088CFC2  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
0088CFC7  8B 7E 04                        mov edi, dword ptr [rsi + 4]
0088CFCA  89 7C 24 3C                     mov dword ptr [rsp + 0x3c], edi
0088CFCE  E9 CA FD FF FF                  jmp 0x14088cd9d
0088CFD3  E9 62 FE FF FF                  jmp 0x14088ce3a
0088CFD8  33 C0                           xor eax, eax
0088CFDA  E9 5B FE FF FF                  jmp 0x14088ce3a
0088CFDF  48 8D 56 08                     lea rdx, [rsi + 8]
0088CFE3  4C 8B C3                        mov r8, rbx
0088CFE6  49 8B CA                        mov rcx, r10
0088CFE9  E8 52 35 00 00                  call 0x140890540
0088CFEE  44 8B F0                        mov r14d, eax
0088CFF1  85 C0                           test eax, eax
0088CFF3  0F 88 2F FE FF FF               js 0x14088ce28
0088CFF9  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
0088CFFE  E9 BB FD FF FF                  jmp 0x14088cdbe
0088D003  85 FF                           test edi, edi
0088D005  0F 88 1F 01 00 00               js 0x14088d12a
0088D00B  0F BA E7 1E                     bt edi, 0x1e
0088D00F  0F 82 EF 01 00 00               jb 0x14088d204
0088D015  0F BA E7 1D                     bt edi, 0x1d
0088D019  73 40                           jae 0x14088d05b
0088D01B  41 8B C7                        mov eax, r15d
0088D01E  25 00 00 00 C0                  and eax, 0xc0000000
0088D023  48 63 C8                        movsxd rcx, eax
0088D026  48 C1 F9 3F                     sar rcx, 0x3f
0088D02A  83 E1 0C                        and ecx, 0xc
0088D02D  48 83 C1 08                     add rcx, 8
0088D031  0F BA E0 1E                     bt eax, 0x1e
0088D035  48 8D 51 10                     lea rdx, [rcx + 0x10]
0088D039  48 0F 43 D1                     cmovae rdx, rcx
0088D03D  48 03 D6                        add rdx, rsi
0088D040  4C 8B CB                        mov r9, rbx
0088D043  4D 8B C5                        mov r8, r13
0088D046  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0088D04B  E8 B8 0C 19 00                  call 0x140a1dd08
0088D050  44 8B F0                        mov r14d, eax
0088D053  85 C0                           test eax, eax
0088D055  0F 88 CD FD FF FF               js 0x14088ce28
0088D05B  0F BA E7 1C                     bt edi, 0x1c
0088D05F  0F 82 DF 01 00 00               jb 0x14088d244
0088D065  0F BA E7 1A                     bt edi, 0x1a
0088D069  0F 82 2A 01 00 00               jb 0x14088d199
0088D06F  0F BA E7 19                     bt edi, 0x19
0088D073  0F 83 AF FD FF FF               jae 0x14088ce28
0088D079  48 8B CB                        mov rcx, rbx
0088D07C  E8 8F 9C 14 00                  call 0x1409d6d10
0088D081  44 8B F0                        mov r14d, eax
0088D084  E9 9F FD FF FF                  jmp 0x14088ce28
0088D089  49 63 D7                        movsxd rdx, r15d
0088D08C  48 81 E2 00 00 00 80            and rdx, 0xffffffff80000000
0088D093  48 C1 FA 3F                     sar rdx, 0x3f
0088D097  83 E2 18                        and edx, 0x18
0088D09A  48 83 C2 08                     add rdx, 8
0088D09E  48 03 D6                        add rdx, rsi
0088D0A1  4C 8B CB                        mov r9, rbx
0088D0A4  4D 8B C5                        mov r8, r13
0088D0A7  49 8B CA                        mov rcx, r10
0088D0AA  E8 CD C4 FF FF                  call 0x14088957c
0088D0AF  44 8B F0                        mov r14d, eax
0088D0B2  85 C0                           test eax, eax
0088D0B4  0F 89 0E FD FF FF               jns 0x14088cdc8
0088D0BA  E9 69 FD FF FF                  jmp 0x14088ce28
0088D0BF  41 81 E7 00 00 00 F8            and r15d, 0xf8000000
0088D0C6  49 63 CF                        movsxd rcx, r15d
0088D0C9  48 C1 F9 3F                     sar rcx, 0x3f
0088D0CD  83 E1 18                        and ecx, 0x18
0088D0D0  48 83 C1 08                     add rcx, 8
0088D0D4  41 0F BA E7 1E                  bt r15d, 0x1e
0088D0D9  48 8D 41 20                     lea rax, [rcx + 0x20]
0088D0DD  48 0F 43 C1                     cmovae rax, rcx
0088D0E1  41 0F BA E7 1D                  bt r15d, 0x1d
0088D0E6  48 8D 48 20                     lea rcx, [rax + 0x20]
0088D0EA  48 0F 43 C8                     cmovae rcx, rax
0088D0EE  41 0F BA E7 1C                  bt r15d, 0x1c
0088D0F3  48 8D 41 18                     lea rax, [rcx + 0x18]
0088D0F7  48 0F 43 C1                     cmovae rax, rcx
0088D0FB  41 0F BA E7 1B                  bt r15d, 0x1b
0088D100  48 8D 48 18                     lea rcx, [rax + 0x18]
0088D104  48 0F 43 C8                     cmovae rcx, rax
0088D108  48 03 CE                        add rcx, rsi
0088D10B  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
0088D10F  45 8B CC                        mov r9d, r12d
0088D112  4C 8B C3                        mov r8, rbx
0088D115  E8 92 55 18 00                  call 0x140a126ac
0088D11A  44 8B F0                        mov r14d, eax
0088D11D  85 C0                           test eax, eax
0088D11F  0F 88 03 FD FF FF               js 0x14088ce28
0088D125  E9 F4 FC FF FF                  jmp 0x14088ce1e
0088D12A  48 8D 56 08                     lea rdx, [rsi + 8]
0088D12E  4C 8B C3                        mov r8, rbx
0088D131  49 8B CA                        mov rcx, r10
0088D134  E8 EB 37 19 00                  call 0x140a20924
0088D139  44 8B F0                        mov r14d, eax
0088D13C  85 C0                           test eax, eax
0088D13E  0F 88 E4 FC FF FF               js 0x14088ce28
0088D144  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
0088D149  E9 BD FE FF FF                  jmp 0x14088d00b
0088D14E  41 8B D7                        mov edx, r15d
0088D151  81 E2 00 00 00 E0               and edx, 0xe0000000
0088D157  48 63 C2                        movsxd rax, edx
0088D15A  48 C1 F8 3F                     sar rax, 0x3f
0088D15E  83 E0 18                        and eax, 0x18
0088D161  48 83 C0 08                     add rax, 8
0088D165  0F BA E2 1E                     bt edx, 0x1e
0088D169  48 8D 48 20                     lea rcx, [rax + 0x20]
0088D16D  48 0F 43 C8                     cmovae rcx, rax
0088D171  0F BA E2 1D                     bt edx, 0x1d
0088D175  48 8D 41 20                     lea rax, [rcx + 0x20]
0088D179  48 0F 43 C1                     cmovae rax, rcx
0088D17D  48 8D 0C 30                     lea rcx, [rax + rsi]
0088D181  48 8B D3                        mov rdx, rbx
0088D184  E8 D3 61 00 00                  call 0x14089335c
0088D189  44 8B F0                        mov r14d, eax
0088D18C  85 C0                           test eax, eax
0088D18E  0F 88 94 FC FF FF               js 0x14088ce28
0088D194  E9 7B FC FF FF                  jmp 0x14088ce14
0088D199  41 81 E7 00 00 00 F8            and r15d, 0xf8000000
0088D1A0  49 63 CF                        movsxd rcx, r15d
0088D1A3  48 C1 F9 3F                     sar rcx, 0x3f
0088D1A7  83 E1 0C                        and ecx, 0xc
0088D1AA  48 83 C1 08                     add rcx, 8
0088D1AE  41 0F BA E7 1E                  bt r15d, 0x1e
0088D1B3  48 8D 41 10                     lea rax, [rcx + 0x10]
0088D1B7  48 0F 43 C1                     cmovae rax, rcx
0088D1BB  41 0F BA E7 1D                  bt r15d, 0x1d
0088D1C0  48 8D 48 14                     lea rcx, [rax + 0x14]
0088D1C4  48 0F 43 C8                     cmovae rcx, rax
0088D1C8  41 0F BA E7 1C                  bt r15d, 0x1c
0088D1CD  48 8D 41 10                     lea rax, [rcx + 0x10]
0088D1D1  48 0F 43 C1                     cmovae rax, rcx
0088D1D5  41 0F BA E7 1B                  bt r15d, 0x1b
0088D1DA  48 8D 48 18                     lea rcx, [rax + 0x18]
0088D1DE  48 0F 43 C8                     cmovae rcx, rax
0088D1E2  48 03 CE                        add rcx, rsi
0088D1E5  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
0088D1E9  45 8B CC                        mov r9d, r12d
0088D1EC  4C 8B C3                        mov r8, rbx
0088D1EF  E8 50 9E 19 00                  call 0x140a27044
0088D1F4  44 8B F0                        mov r14d, eax
0088D1F7  85 C0                           test eax, eax
0088D1F9  0F 88 29 FC FF FF               js 0x14088ce28
0088D1FF  E9 6B FE FF FF                  jmp 0x14088d06f
0088D204  49 63 D7                        movsxd rdx, r15d
0088D207  48 81 E2 00 00 00 80            and rdx, 0xffffffff80000000
0088D20E  48 C1 FA 3F                     sar rdx, 0x3f
0088D212  83 E2 0C                        and edx, 0xc
0088D215  48 83 C2 08                     add rdx, 8
0088D219  48 03 D6                        add rdx, rsi
0088D21C  4C 8B CB                        mov r9, rbx
0088D21F  4D 8B C5                        mov r8, r13
0088D222  49 8B CA                        mov rcx, r10
0088D225  E8 3E 4C 1D 00                  call 0x140a61e68
0088D22A  44 8B F0                        mov r14d, eax
0088D22D  85 C0                           test eax, eax
0088D22F  0F 89 E0 FD FF FF               jns 0x14088d015
0088D235  E9 EE FB FF FF                  jmp 0x14088ce28
0088D23A  B8 0D 00 00 C0                  mov eax, 0xc000000d
0088D23F  E9 F6 FB FF FF                  jmp 0x14088ce3a
0088D244  41 8B D7                        mov edx, r15d
0088D247  81 E2 00 00 00 E0               and edx, 0xe0000000
0088D24D  48 63 C2                        movsxd rax, edx
0088D250  48 C1 F8 3F                     sar rax, 0x3f
0088D254  83 E0 0C                        and eax, 0xc
0088D257  48 83 C0 08                     add rax, 8
0088D25B  0F BA E2 1E                     bt edx, 0x1e
0088D25F  48 8D 48 10                     lea rcx, [rax + 0x10]
0088D263  48 0F 43 C8                     cmovae rcx, rax
0088D267  0F BA E2 1D                     bt edx, 0x1d
0088D26B  48 8D 41 14                     lea rax, [rcx + 0x14]
0088D26F  48 0F 43 C1                     cmovae rax, rcx
0088D273  48 8D 0C 30                     lea rcx, [rax + rsi]
0088D277  48 8B D3                        mov rdx, rbx
0088D27A  E8 B9 AF 22 00                  call 0x140ab8238
0088D27F  44 8B F0                        mov r14d, eax
0088D282  85 C0                           test eax, eax
0088D284  0F 88 9E FB FF FF               js 0x14088ce28
0088D28A  E9 D6 FD FF FF                  jmp 0x14088d065
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpCaptureAttributes(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    result = 0;
    *(unsigned __int64 *)(a5) = v_xmm0;
    *(unsigned __int64 *)(a5 + 16) = v_xmm0;
    *(unsigned __int64 *)(a5 + 32) = v_xmm0;
    *(unsigned __int64 *)(a5 + 48) = v_xmm0;
    *(unsigned __int64 *)(a5 + 64) = 0;
    *(unsigned __int64 *)(a5) = *(unsigned __int64 *)(a4 + 104);
    *(unsigned __int64 *)(a5 + 8) = *(unsigned __int64 *)(a4 + 112);
    if (a3 == 0) goto loc_0088CFD8;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0088CE56;
loc_0088CD9D:
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3))))));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))) & ((unsigned int)(result))) != 0) goto loc_0088D23A;
    v_r14 = 0;
    if (sign_flag) goto loc_0088D003;
    if (sign_flag) goto loc_0088CFDF;
loc_0088CDBE:
    if (condition_is_below) goto loc_0088D089;
loc_0088CDC8:
    if (condition_is_above_or_equal) goto loc_0088CE0A;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) & (0xC0000000ULL));
    a1 = ((int)((unsigned int)(result))) >> (63);
    a1 = (unsigned int)((a1) & (24));
    a1 = (a1) + (8);
    a2 = a1 + 32;
    if (condition_is_above_or_equal) { a2 = a1; }
    a2 = (a2) + (a3);
    result = AlpcpCaptureContextAttribute(v_stack_p8, a2, a4, a5);
    if (sign_flag) goto loc_0088CE28;
loc_0088CE0A:
    if (condition_is_below) goto loc_0088D14E;
loc_0088CE14:
    if (condition_is_below) goto loc_0088D0BF;
loc_0088CE1E:
    if (condition_is_below) goto loc_0088D079;
loc_0088CE28:
    if (sign_flag) {
        a2 = a5;
        a1 = 0;
        result = AlpcpReleaseAttributes(a1, a2, a4, a5);
    }
loc_0088CE3A:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0088CE56:
    a3 = 0;
    v_stack_p30 = 0;
    if (v_stack_p18 < a5) { a5 = v_stack_p18; }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (0xC0000000ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5))))) >> (31));
    if (((unsigned int)(result)) == 0x80000000ULL) goto loc_0088CF6B;
    a1 = (unsigned int)((a1) & (24));
    a1 = (unsigned int)((a1) + (8));
    result = a1 + 32;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    a1 = result + 32;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(result); }
    result = a1 + 24;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    a1 = result + 24;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(result); }
    result = a1 + 8;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    a2 = result + 8;
    if (condition_is_above_or_equal) { a2 = (unsigned int)(result); }
loc_0088CEDC:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a5)))) & (0xA0000000ULL)) != 0) {
        a3 = 1;
        v_stack_p30 = (unsigned __int8)(a3);
    }
    if ((unsigned __int8)(a3) == 0) goto loc_0088CF2A;
    if (a2 >= 0x1000ULL) goto loc_0088CFB2;
    a1 = (unsigned int)((8) - 1);
    if (((v_stack_p18) & (a1)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a5);
    }
    if (v_stack_p18 < a5) { a5 = v_stack_p18; }
    *(unsigned __int8 *)(a5) = (unsigned __int8)(*(unsigned __int8 *)(a5));
    *(unsigned __int8 *)(a5 + a2 * 1 - 1) = (unsigned __int8)(*(unsigned __int8 *)(a5 + a2 * 1 - 1));
    goto loc_0088CFC2;
loc_0088CF2A:
    if ((a2 - 1) <= 0xFFFEULL) goto loc_0088CF56;
    if (a2 == 0) goto loc_0088CFC2;
    a1 = (unsigned int)((a1) - 1);
    if (((v_stack_p18) & (a1)) != 0) goto loc_0088CF06;
    if ((a2 + v_stack_p18 * 1) > a5) goto loc_0088CF65;
    if ((a2 + v_stack_p18 * 1) < v_stack_p18) goto loc_0088CF65;
    goto loc_0088CFC2;
loc_0088CF56:
    a1 = (unsigned int)((a1) - 1);
    if (((v_stack_p18) & (a1)) != 0) goto loc_0088CF06;
    if (v_stack_p18 < a5) { a5 = v_stack_p18; }
loc_0088CF65:
    goto loc_0088CFC2;
loc_0088CF6B:
    a1 = (unsigned int)((a1) & (12));
    a1 = (unsigned int)((a1) + (8));
    result = a1 + 16;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    a1 = result + 20;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(result); }
    result = a1 + 16;
    if (condition_is_above_or_equal) { result = (unsigned int)(a1); }
    a1 = result + 24;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(result); }
    a2 = a1 + 8;
    if (condition_is_above_or_equal) { a2 = (unsigned int)(a1); }
    goto loc_0088CEDC;
loc_0088CFB2:
    result = ProbeForWrite(v_stack_p18, a2, 4, a5);
loc_0088CFC2:
    v_stack_p38 = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
    v_stack_p3C = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    goto loc_0088CD9D;
loc_0088CFD8:
    result = 0;
    goto loc_0088CE3A;
loc_0088CFDF:
    result = AlpcpCaptureSecurityAttribute(v_stack_p70, v_stack_p18 + 8, v_stack_p10, a5);
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088CDBE;
loc_0088D003:
    if (sign_flag) goto loc_0088D12A;
loc_0088D00B:
    if (condition_is_below) goto loc_0088D204;
loc_0088D015:
    if (condition_is_above_or_equal) goto loc_0088D05B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5))))) & (0xC0000000ULL));
    a1 = ((int)((unsigned int)(result))) >> (63);
    a1 = (unsigned int)((a1) & (12));
    a1 = (a1) + (8);
    a2 = a1 + 16;
    if (condition_is_above_or_equal) { a2 = a1; }
    a2 = (a2) + (v_stack_p18);
    result = AlpcpCaptureContextAttribute32(v_stack_p70, a2, a4, v_stack_p10);
    if (sign_flag) goto loc_0088CE28;
loc_0088D05B:
    if (condition_is_below) goto loc_0088D244;
loc_0088D065:
    if (condition_is_below) goto loc_0088D199;
loc_0088D06F:
    if (condition_is_above_or_equal) goto loc_0088CE28;
loc_0088D079:
    result = AlpcpCaptureWorkOnBehalfAttribute(v_stack_p10, a2, a4, v_stack_p10);
    goto loc_0088CE28;
loc_0088D089:
    a2 = ((int)((unsigned int)((unsigned int)(*(unsigned int *)(a5))))) & (0xFFFFFFFF80000000ULL);
    a2 = (a2) >> (63);
    a2 = (unsigned int)((a2) & (24));
    a2 = (a2) + (8);
    a2 = (a2) + (v_stack_p18);
    result = AlpcpCaptureViewAttribute(v_stack_p70, a2, a4, v_stack_p10);
    if (!sign_flag) goto loc_0088CDC8;
    goto loc_0088CE28;
loc_0088D0BF:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a5))) & (0xF8000000ULL));
    a1 = ((int)((unsigned int)(v_r15))) >> (63);
    a1 = (unsigned int)((a1) & (24));
    a1 = (a1) + (8);
    result = a1 + 32;
    if (condition_is_above_or_equal) { result = a1; }
    a1 = result + 32;
    if (condition_is_above_or_equal) { a1 = result; }
    result = a1 + 24;
    if (condition_is_above_or_equal) { result = a1; }
    a1 = result + 24;
    if (condition_is_above_or_equal) { a1 = result; }
    a1 = (a1) + (v_stack_p18);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    result = AlpcpCaptureDirectAttribute(a1, a2, v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(a2))));
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088CE1E;
loc_0088D12A:
    result = AlpcpCaptureSecurityAttribute32(v_stack_p70, v_stack_p18 + 8, v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(a2))));
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088D00B;
loc_0088D14E:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (0xE0000000ULL));
    result = ((int)(a2)) >> (63);
    result = (unsigned int)((result) & (24));
    result = (result) + (8);
    a1 = result + 32;
    if (condition_is_above_or_equal) { a1 = result; }
    result = a1 + 32;
    if (condition_is_above_or_equal) { result = a1; }
    result = AlpcpCaptureHandleAttribute(result + v_stack_p18 * 1, v_stack_p10, v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(a2))));
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088CE14;
loc_0088D199:
    v_r15 = (unsigned int)((v_r15) & (0xF8000000ULL));
    a1 = ((int)((unsigned int)(v_r15))) >> (63);
    a1 = (unsigned int)((a1) & (12));
    a1 = (a1) + (8);
    result = a1 + 16;
    if (condition_is_above_or_equal) { result = a1; }
    a1 = result + 20;
    if (condition_is_above_or_equal) { a1 = result; }
    result = a1 + 16;
    if (condition_is_above_or_equal) { result = a1; }
    a1 = result + 24;
    if (condition_is_above_or_equal) { a1 = result; }
    a1 = (a1) + (v_stack_p18);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 4)));
    result = AlpcpCaptureDirectAttribute32(a1, v_stack_p10, v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(a2))));
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088D06F;
loc_0088D204:
    a2 = ((int)((unsigned int)(v_r15))) & (0xFFFFFFFF80000000ULL);
    a2 = (a2) >> (63);
    a2 = (unsigned int)((a2) & (12));
    a2 = (a2) + (8);
    a2 = (a2) + (v_stack_p18);
    result = AlpcpCaptureViewAttribute32(v_stack_p70, a2, a4, v_stack_p10);
    if (!sign_flag) goto loc_0088D015;
    goto loc_0088CE28;
loc_0088D23A:
    goto loc_0088CE3A;
loc_0088D244:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (0xE0000000ULL));
    result = ((int)(a2)) >> (63);
    result = (unsigned int)((result) & (12));
    result = (result) + (8);
    a1 = result + 16;
    if (condition_is_above_or_equal) { a1 = result; }
    result = a1 + 20;
    if (condition_is_above_or_equal) { result = a1; }
    result = AlpcpCaptureHandleAttribute32(result + v_stack_p18 * 1, v_stack_p10, a4, v_stack_p10);
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088D065;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpCaptureAttributes(int64_t Arg1, int32_t Arg2, int64_t Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    result = 0;
    *(uint64_t *)(arg5) = v_xmm0;
    *(uint64_t *)(arg5 + 0x10) = v_xmm0;
    *(uint64_t *)(arg5 + 0x20) = v_xmm0;
    *(uint64_t *)(arg5 + 0x30) = v_xmm0;
    *(uint64_t *)(arg5 + 0x40) = 0;
    *(uint64_t *)(arg5) = *(uint64_t *)(arg4 + 0x68);
    *(uint64_t *)(arg5 + 0x8) = *(uint64_t *)(arg4 + 0x70);
    if (Arg3 == 0) goto loc_0088CFD8;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0088CE56;
loc_0088CD9D:
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3))))));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)))) & ((uint32_t)(result))) != 0) goto loc_0088D23A;
    local_r14 = 0;
    if (sign_flag) goto loc_0088D003;
    if (sign_flag) goto loc_0088CFDF;
loc_0088CDBE:
    if (condition_is_below) goto loc_0088D089;
loc_0088CDC8:
    if (condition_is_above_or_equal) goto loc_0088CE0A;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3))))) & (0xC0000000ULL));
    Arg1 = ((int32_t)((uint32_t)(result))) >> (63);
    Arg1 = (uint32_t)((Arg1) & (24));
    Arg1 = (Arg1) + (8);
    Arg2 = Arg1 + 32;
    if (condition_is_above_or_equal) { Arg2 = Arg1; }
    Arg2 = (Arg2) + (Arg3);
    result = AlpcpCaptureContextAttribute(v_stack_p8, Arg2, Arg4, Arg5);
    if (sign_flag) goto loc_0088CE28;
loc_0088CE0A:
    if (condition_is_below) goto loc_0088D14E;
loc_0088CE14:
    if (condition_is_below) goto loc_0088D0BF;
loc_0088CE1E:
    if (condition_is_below) goto loc_0088D079;
loc_0088CE28:
    if (sign_flag) {
        Arg2 = Arg5;
        Arg1 = 0;
        result = AlpcpReleaseAttributes(Arg1, Arg2, Arg4, Arg5);
    }
loc_0088CE3A:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0088CE56:
    Arg3 = 0;
    v_stack_p30 = 0;
    if (v_stack_p18 < Arg5) { Arg5 = v_stack_p18; }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (0xC0000000ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5))))) >> (31));
    if (((uint32_t)(result)) == 0x80000000ULL) goto loc_0088CF6B;
    Arg1 = (uint32_t)((Arg1) & (24));
    Arg1 = (uint32_t)((Arg1) + (8));
    result = Arg1 + 32;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    Arg1 = result + 32;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(result); }
    result = Arg1 + 24;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    Arg1 = result + 24;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(result); }
    result = Arg1 + 8;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    Arg2 = result + 8;
    if (condition_is_above_or_equal) { Arg2 = (uint32_t)(result); }
loc_0088CEDC:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg5)))) & (0xA0000000ULL)) != 0) {
        Arg3 = 1;
        v_stack_p30 = (uint8_t)(Arg3);
    }
    if ((uint8_t)(Arg3) == 0) goto loc_0088CF2A;
    if (Arg2 >= 0x1000ULL) goto loc_0088CFB2;
    Arg1 = (uint32_t)((8) - 1);
    if (((v_stack_p18) & (Arg1)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg5);
    }
    if (v_stack_p18 < Arg5) { Arg5 = v_stack_p18; }
    *(uint8_t *)(arg5) = (uint8_t)(*(uint8_t *)(arg5));
    *(uint8_t *)(arg5 + Arg2 * 1 - 0x1) = (uint8_t)(*(uint8_t *)(arg5 + Arg2 * 1 - 0x1));
    goto loc_0088CFC2;
loc_0088CF2A:
    if ((Arg2 - 1) <= 0xFFFEULL) goto loc_0088CF56;
    if (Arg2 == 0) goto loc_0088CFC2;
    Arg1 = (uint32_t)((Arg1) - 1);
    if (((v_stack_p18) & (Arg1)) != 0) goto loc_0088CF06;
    if ((Arg2 + v_stack_p18 * 1) > Arg5) goto loc_0088CF65;
    if ((Arg2 + v_stack_p18 * 1) < v_stack_p18) goto loc_0088CF65;
    goto loc_0088CFC2;
loc_0088CF56:
    Arg1 = (uint32_t)((Arg1) - 1);
    if (((v_stack_p18) & (Arg1)) != 0) goto loc_0088CF06;
    if (v_stack_p18 < Arg5) { Arg5 = v_stack_p18; }
loc_0088CF65:
    goto loc_0088CFC2;
loc_0088CF6B:
    Arg1 = (uint32_t)((Arg1) & (12));
    Arg1 = (uint32_t)((Arg1) + (8));
    result = Arg1 + 16;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    Arg1 = result + 20;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(result); }
    result = Arg1 + 16;
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg1); }
    Arg1 = result + 24;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(result); }
    Arg2 = Arg1 + 8;
    if (condition_is_above_or_equal) { Arg2 = (uint32_t)(Arg1); }
    goto loc_0088CEDC;
loc_0088CFB2:
    result = ProbeForWrite(v_stack_p18, Arg2, 4, Arg5);
loc_0088CFC2:
    v_stack_p38 = (uint32_t)((uint32_t)(*(uint32_t *)(arg5)));
    v_stack_p3C = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    goto loc_0088CD9D;
loc_0088CFD8:
    result = 0;
    goto loc_0088CE3A;
loc_0088CFDF:
    result = AlpcpCaptureSecurityAttribute(v_stack_p70, v_stack_p18 + 8, v_stack_p10, Arg5);
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088CDBE;
loc_0088D003:
    if (sign_flag) goto loc_0088D12A;
loc_0088D00B:
    if (condition_is_below) goto loc_0088D204;
loc_0088D015:
    if (condition_is_above_or_equal) goto loc_0088D05B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5))))) & (0xC0000000ULL));
    Arg1 = ((int32_t)((uint32_t)(result))) >> (63);
    Arg1 = (uint32_t)((Arg1) & (12));
    Arg1 = (Arg1) + (8);
    Arg2 = Arg1 + 16;
    if (condition_is_above_or_equal) { Arg2 = Arg1; }
    Arg2 = (Arg2) + (v_stack_p18);
    result = AlpcpCaptureContextAttribute32(v_stack_p70, Arg2, Arg4, v_stack_p10);
    if (sign_flag) goto loc_0088CE28;
loc_0088D05B:
    if (condition_is_below) goto loc_0088D244;
loc_0088D065:
    if (condition_is_below) goto loc_0088D199;
loc_0088D06F:
    if (condition_is_above_or_equal) goto loc_0088CE28;
loc_0088D079:
    result = AlpcpCaptureWorkOnBehalfAttribute(v_stack_p10, Arg2, Arg4, v_stack_p10);
    goto loc_0088CE28;
loc_0088D089:
    Arg2 = ((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5))))) & (0xFFFFFFFF80000000ULL);
    Arg2 = (Arg2) >> (63);
    Arg2 = (uint32_t)((Arg2) & (24));
    Arg2 = (Arg2) + (8);
    Arg2 = (Arg2) + (v_stack_p18);
    result = AlpcpCaptureViewAttribute(v_stack_p70, Arg2, Arg4, v_stack_p10);
    if (!sign_flag) goto loc_0088CDC8;
    goto loc_0088CE28;
loc_0088D0BF:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5))) & (0xF8000000ULL));
    Arg1 = ((int32_t)((uint32_t)(local_r15))) >> (63);
    Arg1 = (uint32_t)((Arg1) & (24));
    Arg1 = (Arg1) + (8);
    result = Arg1 + 32;
    if (condition_is_above_or_equal) { result = Arg1; }
    Arg1 = result + 32;
    if (condition_is_above_or_equal) { Arg1 = result; }
    result = Arg1 + 24;
    if (condition_is_above_or_equal) { result = Arg1; }
    Arg1 = result + 24;
    if (condition_is_above_or_equal) { Arg1 = result; }
    Arg1 = (Arg1) + (v_stack_p18);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    result = AlpcpCaptureDirectAttribute(Arg1, Arg2, v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(Arg2))));
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088CE1E;
loc_0088D12A:
    result = AlpcpCaptureSecurityAttribute32(v_stack_p70, v_stack_p18 + 8, v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(Arg2))));
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088D00B;
loc_0088D14E:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (0xE0000000ULL));
    result = ((int32_t)(Arg2)) >> (63);
    result = (uint32_t)((result) & (24));
    result = (result) + (8);
    Arg1 = result + 32;
    if (condition_is_above_or_equal) { Arg1 = result; }
    result = Arg1 + 32;
    if (condition_is_above_or_equal) { result = Arg1; }
    result = AlpcpCaptureHandleAttribute(result + v_stack_p18 * 1, v_stack_p10, v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(Arg2))));
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088CE14;
loc_0088D199:
    local_r15 = (uint32_t)((local_r15) & (0xF8000000ULL));
    Arg1 = ((int32_t)((uint32_t)(local_r15))) >> (63);
    Arg1 = (uint32_t)((Arg1) & (12));
    Arg1 = (Arg1) + (8);
    result = Arg1 + 16;
    if (condition_is_above_or_equal) { result = Arg1; }
    Arg1 = result + 20;
    if (condition_is_above_or_equal) { Arg1 = result; }
    result = Arg1 + 16;
    if (condition_is_above_or_equal) { result = Arg1; }
    Arg1 = result + 24;
    if (condition_is_above_or_equal) { Arg1 = result; }
    Arg1 = (Arg1) + (v_stack_p18);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x4)));
    result = AlpcpCaptureDirectAttribute32(Arg1, v_stack_p10, v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(Arg2))));
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088D06F;
loc_0088D204:
    Arg2 = ((int32_t)((uint32_t)(local_r15))) & (0xFFFFFFFF80000000ULL);
    Arg2 = (Arg2) >> (63);
    Arg2 = (uint32_t)((Arg2) & (12));
    Arg2 = (Arg2) + (8);
    Arg2 = (Arg2) + (v_stack_p18);
    result = AlpcpCaptureViewAttribute32(v_stack_p70, Arg2, Arg4, v_stack_p10);
    if (!sign_flag) goto loc_0088D015;
    goto loc_0088CE28;
loc_0088D23A:
    goto loc_0088CE3A;
loc_0088D244:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (0xE0000000ULL));
    result = ((int32_t)(Arg2)) >> (63);
    result = (uint32_t)((result) & (12));
    result = (result) + (8);
    Arg1 = result + 16;
    if (condition_is_above_or_equal) { Arg1 = result; }
    result = Arg1 + 20;
    if (condition_is_above_or_equal) { result = Arg1; }
    result = AlpcpCaptureHandleAttribute32(result + v_stack_p18 * 1, v_stack_p10, Arg4, v_stack_p10);
    if (sign_flag) goto loc_0088CE28;
    goto loc_0088D065;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x68` | `64` | `R` |
| `Arg4` | `+ 0x70` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x8` | `64` | `W` |
| `Arg5` | `+ 0x10` | `128` | `R` |
| `Arg5` | `+ 0x20` | `128` | `R` |
| `Arg5` | `+ 0x30` | `128` | `R` |
| `Arg5` | `+ 0x40` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088CD20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
