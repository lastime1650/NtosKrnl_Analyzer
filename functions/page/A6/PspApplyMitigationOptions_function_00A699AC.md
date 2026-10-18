# PspApplyMitigationOptions

- RVA: `0x00A699AC`–`0x00A6A860` (길이 `3,764` bytes)
- VA: `0x0000000140A699AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B41F4`
- 디코드: `789`개 명령, `3,764/3,764` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A69FAE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A6A136` → [PspSetNoChildProcessRestrictedPolicy](../AB/PspSetNoChildProcessRestrictedPolicy_function_00AB1BE0.md) (function, `0x00AB1BE0`)
- `0x00A6A3EA` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x00A6A40A` → [ExpLockHandleTableExclusive](../../text/45/ExpLockHandleTableExclusive_function_00458B08.md) (function, `0x00458B08`)
- `0x00A6A430` → [ExpUnlockHandleTableExclusive](../../text/46/ExpUnlockHandleTableExclusive_function_004608A8.md) (function, `0x004608A8`)
- `0x00A6A43C` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00A6A47F` → [PspSetRedirectionTrustPolicy](../A7/PspSetRedirectionTrustPolicy_function_00A7C2D4.md) (function, `0x00A7C2D4`)
- `0x00A6A508` → [PspDecodeMitigationExecuteOptions](../A7/PspDecodeMitigationExecuteOptions_function_00A7EAC4.md) (function, `0x00A7EAC4`)
- `0x00A6A849` → [PspSetRedirectionTrustPolicy](../A7/PspSetRedirectionTrustPolicy_function_00A7C2D4.md) (function, `0x00A7C2D4`)

### Direct callers
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A159FA`

### Static image references
- `0x00A699C6` → RVA `0x00E0A740` (`.data`; read)
- `0x00A6A204` → RVA `0x00FC6E34` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00A69FAE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A6A40A` → [ExpLockHandleTableExclusive](../../text/45/ExpLockHandleTableExclusive_function_00458B08.md) (`PAGE` → `.text`)
  - `0x00A6A430` → [ExpUnlockHandleTableExclusive](../../text/46/ExpUnlockHandleTableExclusive_function_004608A8.md) (`PAGE` → `.text`)
  - `0x00A6A43C` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00A6A396` → [sub_00B3F098](../B3/Unknown_function_00B3F098.md) (`tail-transfer`)
  - `0x00A6A610` → [sub_00B3F098](../B3/Unknown_function_00B3F098.md) (`tail-transfer`)
  - `0x00A6A661` → [sub_00B3F098 + 0x9](../B3/Unknown_function_00B3F098.md) (`tail-transfer`)
  - `0x00A6A671` → [sub_00B3F098 + 0x9](../B3/Unknown_function_00B3F098.md) (`tail-transfer`)
  - `0x00A6A71B` → [sub_00B3F098 + 0x12](../B3/Unknown_function_00B3F098.md) (`tail-transfer`)
  - `0x00A6A729` → [sub_00B3F098 + 0x12](../B3/Unknown_function_00B3F098.md) (`tail-transfer`)
  - `0x00A6A733` → [sub_00B3F098 + 0x86](../B3/Unknown_function_00B3F098.md) (`tail-transfer`)
  - `0x00A6A73D` → [sub_00B3F098 + 0x86](../B3/Unknown_function_00B3F098.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A699AC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00A699B1  55                              push rbp
00A699B2  56                              push rsi
00A699B3  57                              push rdi
00A699B4  41 54                           push r12
00A699B6  41 55                           push r13
00A699B8  41 56                           push r14
00A699BA  41 57                           push r15
00A699BC  48 8B EC                        mov rbp, rsp
00A699BF  48 81 EC 80 00 00 00            sub rsp, 0x80
00A699C6  48 8B 05 73 0D 3A 00            mov rax, qword ptr [rip + 0x3a0d73]
00A699CD  48 33 C4                        xor rax, rsp
00A699D0  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00A699D4  41 0F 10 10                     movups xmm2, xmmword ptr [r8]
00A699D8  B8 4C 01 00 00                  mov eax, 0x14c
00A699DD  4D 8B E0                        mov r12, r8
00A699E0  4C 8B FA                        mov r15, rdx
00A699E3  F2 41 0F 10 58 10               movsd xmm3, qword ptr [r8 + 0x10]
00A699E9  48 8B F9                        mov rdi, rcx
00A699EC  F2 41 0F 10 49 10               movsd xmm1, qword ptr [r9 + 0x10]
00A699F2  41 0F 10 01                     movups xmm0, xmmword ptr [r9]
00A699F6  0F 11 55 C0                     movups xmmword ptr [rbp - 0x40], xmm2
00A699FA  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00A699FE  F2 0F 11 5D D0                  movsd qword ptr [rbp - 0x30], xmm3
00A69A03  F2 0F 11 4D E8                  movsd qword ptr [rbp - 0x18], xmm1
00A69A08  66 39 81 EC 06 00 00            cmp word ptr [rcx + 0x6ec], ax
00A69A0F  0F 84 E6 0A 00 00               je 0x140a6a4fb
00A69A15  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A69A19  41 BD 03 00 00 00               mov r13d, 3
00A69A1F  48 8B CE                        mov rcx, rsi
00A69A22  48 C1 E9 08                     shr rcx, 8
00A69A26  41 23 CD                        and ecx, r13d
00A69A29  83 E9 01                        sub ecx, 1
00A69A2C  0F 84 71 09 00 00               je 0x140a6a3a3
00A69A32  83 F9 02                        cmp ecx, 2
00A69A35  0F 84 60 09 00 00               je 0x140a6a39b
00A69A3B  8B 5D 60                        mov ebx, dword ptr [rbp + 0x60]
00A69A3E  48 8B C6                        mov rax, rsi
00A69A41  48 C1 E8 10                     shr rax, 0x10
00A69A45  41 22 C5                        and al, r13b
00A69A48  0F 84 7E 06 00 00               je 0x140a6a0cc
00A69A4E  3C 02                           cmp al, 2
00A69A50  75 0C                           jne 0x140a69a5e
00A69A52  F0 83 8F 50 07 00 00 40         lock or dword ptr [rdi + 0x750], 0x40
00A69A5A  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A69A5E  8B 87 50 07 00 00               mov eax, dword ptr [rdi + 0x750]
00A69A64  A8 40                           test al, 0x40
00A69A66  75 21                           jne 0x140a69a89
00A69A68  48 8B CE                        mov rcx, rsi
00A69A6B  48 C1 E9 14                     shr rcx, 0x14
00A69A6F  41 23 CD                        and ecx, r13d
00A69A72  0F 85 E8 08 00 00               jne 0x140a6a360
00A69A78  F6 C3 02                        test bl, 2
00A69A7B  74 0C                           je 0x140a69a89
00A69A7D  F0 83 8F 50 07 00 00 20         lock or dword ptr [rdi + 0x750], 0x20
00A69A85  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A69A89  4D 85 FF                        test r15, r15
00A69A8C  0F 85 33 07 00 00               jne 0x140a6a1c5
00A69A92  48 8B CE                        mov rcx, rsi
00A69A95  48 C1 E9 1C                     shr rcx, 0x1c
00A69A99  41 23 CD                        and ecx, r13d
00A69A9C  83 F9 01                        cmp ecx, 1
00A69A9F  0F 84 04 08 00 00               je 0x140a6a2a9
00A69AA5  F7 87 50 07 00 00 00 10 00 00   test dword ptr [rdi + 0x750], 0x1000
00A69AAF  41 BB 00 20 00 00               mov r11d, 0x2000
00A69AB5  0F 84 80 08 00 00               je 0x140a6a33b
00A69ABB  4D 85 FF                        test r15, r15
00A69ABE  74 0F                           je 0x140a69acf
00A69AC0  41 8B 87 D8 07 00 00            mov eax, dword ptr [r15 + 0x7d8]
00A69AC7  A8 02                           test al, 2
00A69AC9  0F 85 5F 0A 00 00               jne 0x140a6a52e
00A69ACF  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00A69AD3  48 C1 E9 1C                     shr rcx, 0x1c
00A69AD7  41 23 CD                        and ecx, r13d
00A69ADA  83 F9 01                        cmp ecx, 1
00A69ADD  0F 84 63 0A 00 00               je 0x140a6a546
00A69AE3  8B 87 D8 07 00 00               mov eax, dword ptr [rdi + 0x7d8]
00A69AE9  A8 02                           test al, 2
00A69AEB  0F 84 D8 07 00 00               je 0x140a6a2c9
00A69AF1  48 8B CE                        mov rcx, rsi
00A69AF4  48 C1 E9 24                     shr rcx, 0x24
00A69AF8  41 23 CD                        and ecx, r13d
00A69AFB  83 E9 01                        sub ecx, 1
00A69AFE  0F 84 5E 0A 00 00               je 0x140a6a562
00A69B04  83 F9 02                        cmp ecx, 2
00A69B07  0F 84 4A 0A 00 00               je 0x140a6a557
00A69B0D  F3 0F 6F 45 C0                  movdqu xmm0, xmmword ptr [rbp - 0x40]
00A69B12  41 B9 00 04 00 00               mov r9d, 0x400
00A69B18  66 0F 73 D8 08                  psrldq xmm0, 8
00A69B1D  66 48 0F 7E C1                  movq rcx, xmm0
00A69B22  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
00A69B26  48 C1 E9 38                     shr rcx, 0x38
00A69B2A  41 23 CD                        and ecx, r13d
00A69B2D  83 F9 01                        cmp ecx, 1
00A69B30  0F 84 40 0A 00 00               je 0x140a6a576
00A69B36  F7 87 50 07 00 00 00 01 00 00   test dword ptr [rdi + 0x750], 0x100
00A69B40  41 BA 00 08 00 00               mov r10d, 0x800
00A69B46  0F 84 A2 07 00 00               je 0x140a6a2ee
00A69B4C  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00A69B50  48 C7 C2 FF FF EE FE            mov rdx, 0xfffffffffeeeffff
00A69B57  48 23 C2                        and rax, rdx
00A69B5A  B9 00 00 22 02                  mov ecx, 0x2220000
00A69B5F  48 0B C1                        or rax, rcx
00A69B62  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00A69B66  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00A69B6A  48 23 C2                        and rax, rdx
00A69B6D  48 0B C1                        or rax, rcx
00A69B70  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00A69B74  48 8B CE                        mov rcx, rsi
00A69B77  48 C1 E9 20                     shr rcx, 0x20
00A69B7B  41 23 CD                        and ecx, r13d
00A69B7E  83 F9 01                        cmp ecx, 1
00A69B81  0F 84 00 0A 00 00               je 0x140a6a587
00A69B87  48 8B CE                        mov rcx, rsi
00A69B8A  48 C1 E9 28                     shr rcx, 0x28
00A69B8E  41 23 CD                        and ecx, r13d
00A69B91  0F 84 7E 04 00 00               je 0x140a6a015
00A69B97  83 E9 01                        sub ecx, 1
00A69B9A  0F 84 9D 04 00 00               je 0x140a6a03d
00A69BA0  83 F9 02                        cmp ecx, 2
00A69BA3  0F 84 5B 06 00 00               je 0x140a6a204
00A69BA9  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69BAD  48 C1 E9 08                     shr rcx, 8
00A69BB1  41 23 CD                        and ecx, r13d
00A69BB4  83 F9 01                        cmp ecx, 1
00A69BB7  0F 84 05 0A 00 00               je 0x140a6a5c2
00A69BBD  48 8B CE                        mov rcx, rsi
00A69BC0  BA 00 00 80 00                  mov edx, 0x800000
00A69BC5  48 C1 E9 2C                     shr rcx, 0x2c
00A69BC9  41 23 CD                        and ecx, r13d
00A69BCC  83 E9 01                        sub ecx, 1
00A69BCF  0F 84 B4 08 00 00               je 0x140a6a489
00A69BD5  83 F9 02                        cmp ecx, 2
00A69BD8  0F 84 D5 08 00 00               je 0x140a6a4b3
00A69BDE  85 97 50 07 00 00               test dword ptr [rdi + 0x750], edx
00A69BE4  0F 84 84 07 00 00               je 0x140a6a36e
00A69BEA  8B 4D C0                        mov ecx, dword ptr [rbp - 0x40]
00A69BED  8A C1                           mov al, cl
00A69BEF  C0 E8 04                        shr al, 4
00A69BF2  41 84 C5                        test r13b, al
00A69BF5  0F 84 A7 05 00 00               je 0x140a6a1a2
00A69BFB  C0 E9 04                        shr cl, 4
00A69BFE  41 22 CD                        and cl, r13b
00A69C01  80 F9 01                        cmp cl, 1
00A69C04  0F 85 0B 0A 00 00               jne 0x140a6a615
00A69C0A  8B C3                           mov eax, ebx
00A69C0C  B9 00 C0 00 00                  mov ecx, 0xc000
00A69C11  23 C1                           and eax, ecx
00A69C13  3D 00 40 00 00                  cmp eax, 0x4000
00A69C18  0F 84 C2 08 00 00               je 0x140a6a4e0
00A69C1E  3B C1                           cmp eax, ecx
00A69C20  0F 84 10 0A 00 00               je 0x140a6a636
00A69C26  48 8B CE                        mov rcx, rsi
00A69C29  BA 00 00 02 00                  mov edx, 0x20000
00A69C2E  48 C1 E9 30                     shr rcx, 0x30
00A69C32  41 23 CD                        and ecx, r13d
00A69C35  83 E9 01                        sub ecx, 1
00A69C38  0F 84 28 0A 00 00               je 0x140a6a666
00A69C3E  83 F9 02                        cmp ecx, 2
00A69C41  0F 84 13 0A 00 00               je 0x140a6a65a
00A69C47  F7 87 50 07 00 00 00 00 03 00   test dword ptr [rdi + 0x750], 0x30000
00A69C51  75 14                           jne 0x140a69c67
00A69C53  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A69C57  48 C1 E9 30                     shr rcx, 0x30
00A69C5B  41 23 CD                        and ecx, r13d
00A69C5E  83 F9 01                        cmp ecx, 1
00A69C61  0F 84 0F 0A 00 00               je 0x140a6a676
00A69C67  BA 00 00 08 00                  mov edx, 0x80000
00A69C6C  4D 85 FF                        test r15, r15
00A69C6F  0F 85 B7 05 00 00               jne 0x140a6a22c
00A69C75  48 8B CE                        mov rcx, rsi
00A69C78  48 C1 E9 34                     shr rcx, 0x34
00A69C7C  41 23 CD                        and ecx, r13d
00A69C7F  83 F9 01                        cmp ecx, 1
00A69C82  0F 84 0A 05 00 00               je 0x140a6a192
00A69C88  85 97 50 07 00 00               test dword ptr [rdi + 0x750], edx
00A69C8E  0F 84 7F 06 00 00               je 0x140a6a313
00A69C94  BA 00 00 20 00                  mov edx, 0x200000
00A69C99  4D 85 FF                        test r15, r15
00A69C9C  0F 85 4B 03 00 00               jne 0x140a69fed
00A69CA2  48 8B CE                        mov rcx, rsi
00A69CA5  48 C1 E9 38                     shr rcx, 0x38
00A69CA9  41 23 CD                        and ecx, r13d
00A69CAC  83 F9 01                        cmp ecx, 1
00A69CAF  0F 84 8B 04 00 00               je 0x140a6a140
00A69CB5  85 97 50 07 00 00               test dword ptr [rdi + 0x750], edx
00A69CBB  0F 84 AA 03 00 00               je 0x140a6a06b
00A69CC1  BA 00 00 04 00                  mov edx, 0x40000
00A69CC6  48 B9 FF FF FF FF FF FF FF CF   movabs rcx, 0xcfffffffffffffff
00A69CD0  4D 85 FF                        test r15, r15
00A69CD3  0F 85 F6 02 00 00               jne 0x140a69fcf
00A69CD9  48 C1 EE 3C                     shr rsi, 0x3c
00A69CDD  41 23 F5                        and esi, r13d
00A69CE0  83 FE 01                        cmp esi, 1
00A69CE3  0F 84 D4 05 00 00               je 0x140a6a2bd
00A69CE9  41 B8 00 00 00 08               mov r8d, 0x8000000
00A69CEF  4D 85 FF                        test r15, r15
00A69CF2  74 1A                           je 0x140a69d0e
00A69CF4  41 8B 87 50 07 00 00            mov eax, dword ptr [r15 + 0x750]
00A69CFB  0F BA E0 1A                     bt eax, 0x1a
00A69CFF  0F 82 81 09 00 00               jb 0x140a6a686
00A69D05  41 85 C0                        test r8d, eax
00A69D08  0F 85 8E 09 00 00               jne 0x140a6a69c
00A69D0E  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69D12  BA 00 00 00 0C                  mov edx, 0xc000000
00A69D17  48 C1 E9 04                     shr rcx, 4
00A69D1B  41 23 CD                        and ecx, r13d
00A69D1E  83 E9 01                        sub ecx, 1
00A69D21  0F 84 8C 09 00 00               je 0x140a6a6b3
00A69D27  83 F9 02                        cmp ecx, 2
00A69D2A  0F 84 76 09 00 00               je 0x140a6a6a6
00A69D30  85 97 50 07 00 00               test dword ptr [rdi + 0x750], edx
00A69D36  75 14                           jne 0x140a69d4c
00A69D38  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A69D3C  48 C1 E9 04                     shr rcx, 4
00A69D40  41 23 CD                        and ecx, r13d
00A69D43  83 F9 01                        cmp ecx, 1
00A69D46  0F 84 73 09 00 00               je 0x140a6a6bf
00A69D4C  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69D50  48 C1 E9 1C                     shr rcx, 0x1c
00A69D54  41 23 CD                        and ecx, r13d
00A69D57  83 F9 01                        cmp ecx, 1
00A69D5A  0F 84 6C 09 00 00               je 0x140a6a6cc
00A69D60  8B 87 54 07 00 00               mov eax, dword ptr [rdi + 0x754]
00A69D66  A8 01                           test al, 1
00A69D68  0F 84 E2 03 00 00               je 0x140a6a150
00A69D6E  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69D72  48 C1 E9 20                     shr rcx, 0x20
00A69D76  41 23 CD                        and ecx, r13d
00A69D79  83 F9 01                        cmp ecx, 1
00A69D7C  0F 84 57 09 00 00               je 0x140a6a6d9
00A69D82  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69D86  41 BE 00 00 00 40               mov r14d, 0x40000000
00A69D8C  48 C1 E9 30                     shr rcx, 0x30
00A69D90  41 23 CD                        and ecx, r13d
00A69D93  83 F9 01                        cmp ecx, 1
00A69D96  75 08                           jne 0x140a69da0
00A69D98  F0 44 09 B7 50 07 00 00         lock or dword ptr [rdi + 0x750], r14d
00A69DA0  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69DA4  48 C1 E9 34                     shr rcx, 0x34
00A69DA8  41 23 CD                        and ecx, r13d
00A69DAB  83 F9 01                        cmp ecx, 1
00A69DAE  0F 84 32 09 00 00               je 0x140a6a6e6
00A69DB4  8B 87 54 07 00 00               mov eax, dword ptr [rdi + 0x754]
00A69DBA  A8 04                           test al, 4
00A69DBC  0F 84 AF 03 00 00               je 0x140a6a171
00A69DC2  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69DC6  48 C1 E9 28                     shr rcx, 0x28
00A69DCA  41 23 CD                        and ecx, r13d
00A69DCD  83 F9 01                        cmp ecx, 1
00A69DD0  0F 84 1D 09 00 00               je 0x140a6a6f3
00A69DD6  44 85 8F 54 07 00 00            test dword ptr [rdi + 0x754], r9d
00A69DDD  0F 84 F7 02 00 00               je 0x140a6a0da
00A69DE3  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69DE7  48 C1 E9 10                     shr rcx, 0x10
00A69DEB  41 23 CD                        and ecx, r13d
00A69DEE  83 F9 01                        cmp ecx, 1
00A69DF1  0F 84 09 09 00 00               je 0x140a6a700
00A69DF7  8B 87 54 07 00 00               mov eax, dword ptr [rdi + 0x754]
00A69DFD  A8 10                           test al, 0x10
00A69DFF  0F 84 F6 02 00 00               je 0x140a6a0fb
00A69E05  B8 4C 01 00 00                  mov eax, 0x14c
00A69E0A  66 39 87 EC 06 00 00            cmp word ptr [rdi + 0x6ec], ax
00A69E11  0F 84 F6 08 00 00               je 0x140a6a70d
00A69E17  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00A69E1B  48 C1 E8 24                     shr rax, 0x24
00A69E1F  0F B6 F0                        movzx esi, al
00A69E22  8B CE                           mov ecx, esi
00A69E24  41 23 CD                        and ecx, r13d
00A69E27  83 E9 01                        sub ecx, 1
00A69E2A  0F 84 08 09 00 00               je 0x140a6a738
00A69E30  83 F9 02                        cmp ecx, 2
00A69E33  0F 84 F5 08 00 00               je 0x140a6a72e
00A69E39  41 22 F5                        and sil, r13b
00A69E3C  40 80 FE 01                     cmp sil, 1
00A69E40  0F 85 D6 02 00 00               jne 0x140a6a11c
00A69E46  41 B8 00 00 00 10               mov r8d, 0x10000000
00A69E4C  4D 85 FF                        test r15, r15
00A69E4F  0F 85 3E 02 00 00               jne 0x140a6a093
00A69E55  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69E59  48 C1 E9 2C                     shr rcx, 0x2c
00A69E5D  41 23 CD                        and ecx, r13d
00A69E60  83 E9 01                        sub ecx, 1
00A69E63  0F 84 E9 08 00 00               je 0x140a6a752
00A69E69  83 F9 02                        cmp ecx, 2
00A69E6C  0F 84 D0 08 00 00               je 0x140a6a742
00A69E72  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A69E76  48 8B D1                        mov rdx, rcx
00A69E79  48 C1 EA 3C                     shr rdx, 0x3c
00A69E7D  41 23 D5                        and edx, r13d
00A69E80  0F 84 CE 03 00 00               je 0x140a6a254
00A69E86  83 EA 01                        sub edx, 1
00A69E89  0F 84 0A 04 00 00               je 0x140a6a299
00A69E8F  83 FA 02                        cmp edx, 2
00A69E92  0F 84 C7 08 00 00               je 0x140a6a75f
00A69E98  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A69E9C  48 C1 E9 3C                     shr rcx, 0x3c
00A69EA0  41 23 CD                        and ecx, r13d
00A69EA3  83 F9 01                        cmp ecx, 1
00A69EA6  0F 84 F1 08 00 00               je 0x140a6a79d
00A69EAC  F7 87 54 07 00 00 00 40 00 00   test dword ptr [rdi + 0x754], 0x4000
00A69EB6  0F 85 F8 04 00 00               jne 0x140a6a3b4
00A69EBC  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00A69EC0  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00A69EC4  48 83 C8 02                     or rax, 2
00A69EC8  0F B6 4D E8                     movzx ecx, byte ptr [rbp - 0x18]
00A69ECC  41 23 CD                        and ecx, r13d
00A69ECF  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00A69ED3  83 F9 01                        cmp ecx, 1
00A69ED6  0F 84 EA 08 00 00               je 0x140a6a7c6
00A69EDC  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00A69EE0  48 C1 E9 04                     shr rcx, 4
00A69EE4  41 23 CD                        and ecx, r13d
00A69EE7  83 E9 01                        sub ecx, 1
00A69EEA  0F 84 01 09 00 00               je 0x140a6a7f1
00A69EF0  83 F9 02                        cmp ecx, 2
00A69EF3  0F 84 DD 08 00 00               je 0x140a6a7d6
00A69EF9  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00A69EFD  48 C1 E9 04                     shr rcx, 4
00A69F01  41 23 CD                        and ecx, r13d
00A69F04  83 F9 01                        cmp ecx, 1
00A69F07  0F 84 F4 08 00 00               je 0x140a6a801
00A69F0D  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00A69F11  48 C1 E9 0C                     shr rcx, 0xc
00A69F15  41 23 CD                        and ecx, r13d
00A69F18  0F 84 F3 08 00 00               je 0x140a6a811
00A69F1E  83 F9 01                        cmp ecx, 1
00A69F21  0F 84 FD 08 00 00               je 0x140a6a824
00A69F27  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00A69F2B  48 C1 E9 0C                     shr rcx, 0xc
00A69F2F  41 23 CD                        and ecx, r13d
00A69F32  83 F9 01                        cmp ecx, 1
00A69F35  0F 84 F9 08 00 00               je 0x140a6a834
00A69F3B  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00A69F3F  48 C1 E9 10                     shr rcx, 0x10
00A69F43  41 23 CD                        and ecx, r13d
00A69F46  0F 84 10 01 00 00               je 0x140a6a05c
00A69F4C  83 F9 01                        cmp ecx, 1
00A69F4F  75 08                           jne 0x140a69f59
00A69F51  F0 44 09 B7 54 07 00 00         lock or dword ptr [rdi + 0x754], r14d
00A69F59  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00A69F5D  48 C1 E8 14                     shr rax, 0x14
00A69F61  0F B6 D8                        movzx ebx, al
00A69F64  8B CB                           mov ecx, ebx
00A69F66  41 23 CD                        and ecx, r13d
00A69F69  83 F9 01                        cmp ecx, 1
00A69F6C  0F 84 CF 08 00 00               je 0x140a6a841
00A69F72  41 22 DD                        and bl, r13b
00A69F75  80 FB 01                        cmp bl, 1
00A69F78  0F 85 E7 04 00 00               jne 0x140a6a465
00A69F7E  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00A69F82  48 C1 E9 18                     shr rcx, 0x18
00A69F86  41 23 CD                        and ecx, r13d
00A69F89  83 F9 01                        cmp ecx, 1
00A69F8C  0F 84 C1 08 00 00               je 0x140a6a853
00A69F92  0F 10 45 C0                     movups xmm0, xmmword ptr [rbp - 0x40]
00A69F96  F2 0F 10 4D D0                  movsd xmm1, qword ptr [rbp - 0x30]
00A69F9B  41 0F 11 04 24                  movups xmmword ptr [r12], xmm0
00A69FA0  F2 41 0F 11 4C 24 10            movsd qword ptr [r12 + 0x10], xmm1
00A69FA7  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00A69FAB  48 33 CC                        xor rcx, rsp
00A69FAE  E8 8D 26 C4 FF                  call 0x1406ac640
00A69FB3  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
00A69FBB  48 81 C4 80 00 00 00            add rsp, 0x80
00A69FC2  41 5F                           pop r15
00A69FC4  41 5E                           pop r14
00A69FC6  41 5D                           pop r13
00A69FC8  41 5C                           pop r12
00A69FCA  5F                              pop rdi
00A69FCB  5E                              pop rsi
00A69FCC  5D                              pop rbp
00A69FCD  C3                              ret
00A69FCE  CC                              int3
00A69FCF  41 85 97 50 07 00 00            test dword ptr [r15 + 0x750], edx
00A69FD6  0F 84 FD FC FF FF               je 0x140a69cd9
00A69FDC  48 23 F1                        and rsi, rcx
00A69FDF  48 0F BA EE 3C                  bts rsi, 0x3c
00A69FE4  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A69FE8  E9 EC FC FF FF                  jmp 0x140a69cd9
00A69FED  41 85 97 50 07 00 00            test dword ptr [r15 + 0x750], edx
00A69FF4  0F 84 A8 FC FF FF               je 0x140a69ca2
00A69FFA  48 B8 FF FF FF FF FF FF FF FC   movabs rax, 0xfcffffffffffffff
00A6A004  48 23 F0                        and rsi, rax
00A6A007  48 0F BA EE 38                  bts rsi, 0x38
00A6A00C  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A6A010  E9 8D FC FF FF                  jmp 0x140a69ca2
00A6A015  F6 C3 08                        test bl, 8
00A6A018  0F 84 8B FB FF FF               je 0x140a69ba9
00A6A01E  48 B8 FF FF FF FF FF FC FF FF   movabs rax, 0xfffffcffffffffff
00A6A028  48 23 F0                        and rsi, rax
00A6A02B  48 0F BA EE 28                  bts rsi, 0x28
00A6A030  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A6A034  F6 C3 20                        test bl, 0x20
00A6A037  0F 85 5E 05 00 00               jne 0x140a6a59b
00A6A03D  F0 83 8F 50 07 00 00 01         lock or dword ptr [rdi + 0x750], 1
00A6A045  F6 C3 10                        test bl, 0x10
00A6A048  75 09                           jne 0x140a6a053
00A6A04A  F0 0F BA AF 88 00 00 00 05      lock bts dword ptr [rdi + 0x88], 5
00A6A053  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A057  E9 4D FB FF FF                  jmp 0x140a69ba9
00A6A05C  0F BA E3 13                     bt ebx, 0x13
00A6A060  0F 83 EB FE FF FF               jae 0x140a69f51
00A6A066  E9 EE FE FF FF                  jmp 0x140a69f59
00A6A06B  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A6A06F  48 C1 E9 38                     shr rcx, 0x38
00A6A073  41 23 CD                        and ecx, r13d
00A6A076  83 F9 01                        cmp ecx, 1
00A6A079  0F 85 42 FC FF FF               jne 0x140a69cc1
00A6A07F  F0 81 8F 50 07 00 00 00 00 40 00  lock or dword ptr [rdi + 0x750], 0x400000
00A6A08A  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A08E  E9 2E FC FF FF                  jmp 0x140a69cc1
00A6A093  41 8B 87 50 07 00 00            mov eax, dword ptr [r15 + 0x750]
00A6A09A  41 85 C0                        test r8d, eax
00A6A09D  0F 84 B2 FD FF FF               je 0x140a69e55
00A6A0A3  0F BA E0 1D                     bt eax, 0x1d
00A6A0A7  0F 82 A8 FD FF FF               jb 0x140a69e55
00A6A0AD  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00A6A0B1  48 B9 FF FF FF FF FF CF FF FF   movabs rcx, 0xffffcfffffffffff
00A6A0BB  48 23 C1                        and rax, rcx
00A6A0BE  48 0F BA E8 2C                  bts rax, 0x2c
00A6A0C3  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00A6A0C7  E9 89 FD FF FF                  jmp 0x140a69e55
00A6A0CC  F6 C3 01                        test bl, 1
00A6A0CF  0F 85 89 F9 FF FF               jne 0x140a69a5e
00A6A0D5  E9 78 F9 FF FF                  jmp 0x140a69a52
00A6A0DA  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A6A0DE  48 C1 E9 28                     shr rcx, 0x28
00A6A0E2  41 23 CD                        and ecx, r13d
00A6A0E5  83 F9 01                        cmp ecx, 1
00A6A0E8  0F 85 F5 FC FF FF               jne 0x140a69de3
00A6A0EE  F0 44 09 97 54 07 00 00         lock or dword ptr [rdi + 0x754], r10d
00A6A0F6  E9 E8 FC FF FF                  jmp 0x140a69de3
00A6A0FB  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A6A0FF  48 C1 E9 10                     shr rcx, 0x10
00A6A103  41 23 CD                        and ecx, r13d
00A6A106  83 F9 01                        cmp ecx, 1
00A6A109  0F 85 F6 FC FF FF               jne 0x140a69e05
00A6A10F  F0 83 8F 54 07 00 00 20         lock or dword ptr [rdi + 0x754], 0x20
00A6A117  E9 E9 FC FF FF                  jmp 0x140a69e05
00A6A11C  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A6A120  48 C1 E9 24                     shr rcx, 0x24
00A6A124  41 23 CD                        and ecx, r13d
00A6A127  83 F9 01                        cmp ecx, 1
00A6A12A  0F 85 16 FD FF FF               jne 0x140a69e46
00A6A130  41 8B D5                        mov edx, r13d
00A6A133  48 8B CF                        mov rcx, rdi
00A6A136  E8 A5 7A 04 00                  call 0x140ab1be0
00A6A13B  E9 06 FD FF FF                  jmp 0x140a69e46
00A6A140  F0 09 97 50 07 00 00            lock or dword ptr [rdi + 0x750], edx
00A6A147  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A14B  E9 65 FB FF FF                  jmp 0x140a69cb5
00A6A150  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A6A154  48 C1 E9 1C                     shr rcx, 0x1c
00A6A158  41 23 CD                        and ecx, r13d
00A6A15B  83 F9 01                        cmp ecx, 1
00A6A15E  0F 85 0A FC FF FF               jne 0x140a69d6e
00A6A164  F0 83 8F 54 07 00 00 02         lock or dword ptr [rdi + 0x754], 2
00A6A16C  E9 FD FB FF FF                  jmp 0x140a69d6e
00A6A171  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A6A175  48 C1 E9 20                     shr rcx, 0x20
00A6A179  41 23 CD                        and ecx, r13d
00A6A17C  83 F9 01                        cmp ecx, 1
00A6A17F  0F 85 3D FC FF FF               jne 0x140a69dc2
00A6A185  F0 83 8F 54 07 00 00 08         lock or dword ptr [rdi + 0x754], 8
00A6A18D  E9 30 FC FF FF                  jmp 0x140a69dc2
00A6A192  F0 09 97 50 07 00 00            lock or dword ptr [rdi + 0x750], edx
00A6A199  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A19D  E9 E6 FA FF FF                  jmp 0x140a69c88
00A6A1A2  8B 87 50 07 00 00               mov eax, dword ptr [rdi + 0x750]
00A6A1A8  A8 01                           test al, 1
00A6A1AA  0F 84 4B FA FF FF               je 0x140a69bfb
00A6A1B0  48 83 E6 CF                     and rsi, 0xffffffffffffffcf
00A6A1B4  48 0F BA EE 04                  bts rsi, 4
00A6A1B9  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A6A1BD  40 8A CE                        mov cl, sil
00A6A1C0  E9 36 FA FF FF                  jmp 0x140a69bfb
00A6A1C5  48 8B CE                        mov rcx, rsi
00A6A1C8  48 C1 E9 18                     shr rcx, 0x18
00A6A1CC  41 23 CD                        and ecx, r13d
00A6A1CF  0F 85 FD 02 00 00               jne 0x140a6a4d2
00A6A1D5  F6 C3 04                        test bl, 4
00A6A1D8  0F 85 09 02 00 00               jne 0x140a6a3e7
00A6A1DE  41 F7 87 50 07 00 00 00 10 00 00  test dword ptr [r15 + 0x750], 0x1000
00A6A1E9  0F 84 A3 F8 FF FF               je 0x140a69a92
00A6A1EF  48 81 E6 FF FF FF CF            and rsi, 0xffffffffcfffffff
00A6A1F6  48 0F BA EE 1C                  bts rsi, 0x1c
00A6A1FB  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A6A1FF  E9 8E F8 FF FF                  jmp 0x140a69a92
00A6A204  83 3D 29 CC 55 00 00            cmp dword ptr [rip + 0x55cc29], 0
00A6A20B  0F 85 39 02 00 00               jne 0x140a6a44a
00A6A211  F0 83 8F 50 07 00 00 02         lock or dword ptr [rdi + 0x750], 2
00A6A219  48 B8 00 00 00 00 00 03 00 00   movabs rax, 0x30000000000
00A6A223  48 09 45 C0                     or qword ptr [rbp - 0x40], rax
00A6A227  E9 11 FE FF FF                  jmp 0x140a6a03d
00A6A22C  41 85 97 50 07 00 00            test dword ptr [r15 + 0x750], edx
00A6A233  0F 84 3C FA FF FF               je 0x140a69c75
00A6A239  48 B8 FF FF FF FF FF FF CF FF   movabs rax, 0xffcfffffffffffff
00A6A243  48 23 F0                        and rsi, rax
00A6A246  48 0F BA EE 34                  bts rsi, 0x34
00A6A24B  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A6A24F  E9 21 FA FF FF                  jmp 0x140a69c75
00A6A254  0F BA E3 10                     bt ebx, 0x10
00A6A258  0F 83 3A FC FF FF               jae 0x140a69e98
00A6A25E  B8 00 00 10 00                  mov eax, 0x100000
00A6A263  85 D8                           test eax, ebx
00A6A265  0F 85 2D FC FF FF               jne 0x140a69e98
00A6A26B  0F BA E3 15                     bt ebx, 0x15
00A6A26F  0F 82 23 FC FF FF               jb 0x140a69e98
00A6A275  0F BA E3 11                     bt ebx, 0x11
00A6A279  0F 82 12 05 00 00               jb 0x140a6a791
00A6A27F  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00A6A283  48 BA FF FF FF FF FF FF FF CF   movabs rdx, 0xcfffffffffffffff
00A6A28D  48 23 C2                        and rax, rdx
00A6A290  48 0F BA E8 3C                  bts rax, 0x3c
00A6A295  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00A6A299  F0 81 8F 54 07 00 00 00 40 00 00  lock or dword ptr [rdi + 0x754], 0x4000
00A6A2A4  E9 EF FB FF FF                  jmp 0x140a69e98
00A6A2A9  F0 81 8F 50 07 00 00 00 30 00 00  lock or dword ptr [rdi + 0x750], 0x3000
00A6A2B4  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A2B8  E9 E8 F7 FF FF                  jmp 0x140a69aa5
00A6A2BD  F0 09 97 50 07 00 00            lock or dword ptr [rdi + 0x750], edx
00A6A2C4  E9 20 FA FF FF                  jmp 0x140a69ce9
00A6A2C9  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00A6A2CD  48 C1 E9 1C                     shr rcx, 0x1c
00A6A2D1  41 23 CD                        and ecx, r13d
00A6A2D4  83 F9 01                        cmp ecx, 1
00A6A2D7  0F 85 14 F8 FF FF               jne 0x140a69af1
00A6A2DD  F0 83 8F D8 07 00 00 04         lock or dword ptr [rdi + 0x7d8], 4
00A6A2E5  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A2E9  E9 03 F8 FF FF                  jmp 0x140a69af1
00A6A2EE  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A6A2F2  48 C1 E9 24                     shr rcx, 0x24
00A6A2F6  41 23 CD                        and ecx, r13d
00A6A2F9  83 F9 01                        cmp ecx, 1
00A6A2FC  0F 85 72 F8 FF FF               jne 0x140a69b74
00A6A302  F0 44 09 97 50 07 00 00         lock or dword ptr [rdi + 0x750], r10d
00A6A30A  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A30E  E9 61 F8 FF FF                  jmp 0x140a69b74
00A6A313  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A6A317  48 C1 E9 34                     shr rcx, 0x34
00A6A31B  41 23 CD                        and ecx, r13d
00A6A31E  83 F9 01                        cmp ecx, 1
00A6A321  0F 85 6D F9 FF FF               jne 0x140a69c94
00A6A327  F0 81 8F 50 07 00 00 00 00 10 00  lock or dword ptr [rdi + 0x750], 0x100000
00A6A332  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A336  E9 59 F9 FF FF                  jmp 0x140a69c94
00A6A33B  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A6A33F  48 C1 E9 1C                     shr rcx, 0x1c
00A6A343  41 23 CD                        and ecx, r13d
00A6A346  83 F9 01                        cmp ecx, 1
00A6A349  0F 85 6C F7 FF FF               jne 0x140a69abb
00A6A34F  F0 44 09 9F 50 07 00 00         lock or dword ptr [rdi + 0x750], r11d
00A6A357  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A35B  E9 5B F7 FF FF                  jmp 0x140a69abb
00A6A360  83 F9 01                        cmp ecx, 1
00A6A363  0F 84 14 F7 FF FF               je 0x140a69a7d
00A6A369  E9 1B F7 FF FF                  jmp 0x140a69a89
00A6A36E  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A6A372  48 C1 E9 2C                     shr rcx, 0x2c
00A6A376  41 23 CD                        and ecx, r13d
00A6A379  83 E9 01                        sub ecx, 1
00A6A37C  0F 84 83 02 00 00               je 0x140a6a605
00A6A382  83 F9 02                        cmp ecx, 2
00A6A385  0F 85 5F F8 FF FF               jne 0x140a69bea
00A6A38B  F0 81 8F 50 07 00 00 00 00 00 02  lock or dword ptr [rdi + 0x750], 0x2000000
00A6A396  E9 FD 4C 0D 00                  jmp 0x140b3f098
00A6A39B  F0 83 8F 50 07 00 00 08         lock or dword ptr [rdi + 0x750], 8
00A6A3A3  F0 83 8F 50 07 00 00 10         lock or dword ptr [rdi + 0x750], 0x10
00A6A3AB  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A3AF  E9 87 F6 FF FF                  jmp 0x140a69a3b
00A6A3B4  F0 81 8F 54 07 00 00 00 00 02 00  lock or dword ptr [rdi + 0x754], 0x20000
00A6A3BF  8A 45 D0                        mov al, byte ptr [rbp - 0x30]
00A6A3C2  41 22 C5                        and al, r13b
00A6A3C5  0F 85 E2 03 00 00               jne 0x140a6a7ad
00A6A3CB  0F BA E3 12                     bt ebx, 0x12
00A6A3CF  0F 82 E1 03 00 00               jb 0x140a6a7b6
00A6A3D5  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00A6A3D9  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00A6A3DD  48 0F BA E8 00                  bts rax, 0
00A6A3E2  E9 E1 FA FF FF                  jmp 0x140a69ec8
00A6A3E7  48 8B CF                        mov rcx, rdi
00A6A3EA  E8 81 97 E2 FF                  call 0x140893b70
00A6A3EF  4C 8B F0                        mov r14, rax
00A6A3F2  48 85 C0                        test rax, rax
00A6A3F5  0F 84 E3 FD FF FF               je 0x140a6a1de
00A6A3FB  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
00A6A404  48 8B C8                        mov rcx, rax
00A6A407  48 8B D6                        mov rdx, rsi
00A6A40A  E8 F9 E6 9E FF                  call 0x140458b08
00A6A40F  49 8B 4E 60                     mov rcx, qword ptr [r14 + 0x60]
00A6A413  48 85 C9                        test rcx, rcx
00A6A416  0F 85 FC 00 00 00               jne 0x140a6a518
00A6A41C  41 8A 46 2C                     mov al, byte ptr [r14 + 0x2c]
00A6A420  A8 02                           test al, 2
00A6A422  75 06                           jne 0x140a6a42a
00A6A424  0C 02                           or al, 2
00A6A426  41 88 46 2C                     mov byte ptr [r14 + 0x2c], al
00A6A42A  48 8B D6                        mov rdx, rsi
00A6A42D  49 8B CE                        mov rcx, r14
00A6A430  E8 73 64 9F FF                  call 0x1404608a8
00A6A435  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
00A6A43C  E8 3F FA 8D FF                  call 0x140349e80
00A6A441  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A445  E9 94 FD FF FF                  jmp 0x140a6a1de
00A6A44A  48 B8 FF FF FF FF FF FC FF FF   movabs rax, 0xfffffcffffffffff
00A6A454  48 23 F0                        and rsi, rax
00A6A457  48 0F BA EE 28                  bts rsi, 0x28
00A6A45C  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A6A460  E9 D8 FB FF FF                  jmp 0x140a6a03d
00A6A465  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00A6A469  48 C1 E9 14                     shr rcx, 0x14
00A6A46D  41 23 CD                        and ecx, r13d
00A6A470  83 F9 01                        cmp ecx, 1
00A6A473  0F 85 05 FB FF FF               jne 0x140a69f7e
00A6A479  8D 51 01                        lea edx, [rcx + 1]
00A6A47C  48 8B CF                        mov rcx, rdi
00A6A47F  E8 50 1E 01 00                  call 0x140a7c2d4
00A6A484  E9 F5 FA FF FF                  jmp 0x140a69f7e
00A6A489  80 BF F8 05 00 00 08            cmp byte ptr [rdi + 0x5f8], 8
00A6A490  0F 82 57 01 00 00               jb 0x140a6a5ed
00A6A496  80 BF F9 05 00 00 08            cmp byte ptr [rdi + 0x5f9], 8
00A6A49D  0F 82 56 01 00 00               jb 0x140a6a5f9
00A6A4A3  F0 09 97 50 07 00 00            lock or dword ptr [rdi + 0x750], edx
00A6A4AA  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A4AE  E9 2B F7 FF FF                  jmp 0x140a69bde
00A6A4B3  80 BF F8 05 00 00 06            cmp byte ptr [rdi + 0x5f8], 6
00A6A4BA  0F 82 21 01 00 00               jb 0x140a6a5e1
00A6A4C0  80 BF F9 05 00 00 06            cmp byte ptr [rdi + 0x5f9], 6
00A6A4C7  73 DA                           jae 0x140a6a4a3
00A6A4C9  C6 87 F9 05 00 00 06            mov byte ptr [rdi + 0x5f9], 6
00A6A4D0  EB D1                           jmp 0x140a6a4a3
00A6A4D2  83 F9 01                        cmp ecx, 1
00A6A4D5  0F 85 03 FD FF FF               jne 0x140a6a1de
00A6A4DB  E9 07 FF FF FF                  jmp 0x140a6a3e7
00A6A4E0  48 B8 FF FF FF FF FF FF FC FF   movabs rax, 0xfffcffffffffffff
00A6A4EA  48 23 F0                        and rsi, rax
00A6A4ED  48 0F BA EE 30                  bts rsi, 0x30
00A6A4F2  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A6A4F6  E9 2B F7 FF FF                  jmp 0x140a69c26
00A6A4FB  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00A6A4FF  0F 29 55 A0                     movaps xmmword ptr [rbp - 0x60], xmm2
00A6A503  F2 0F 11 5D B0                  movsd qword ptr [rbp - 0x50], xmm3
00A6A508  E8 B7 45 01 00                  call 0x140a7eac4
00A6A50D  88 87 93 00 00 00               mov byte ptr [rdi + 0x93], al
00A6A513  E9 FD F4 FF FF                  jmp 0x140a69a15
00A6A518  8B 41 08                        mov eax, dword ptr [rcx + 8]
00A6A51B  A8 08                           test al, 8
00A6A51D  0F 85 07 FF FF FF               jne 0x140a6a42a
00A6A523  83 C8 08                        or eax, 8
00A6A526  89 41 08                        mov dword ptr [rcx + 8], eax
00A6A529  E9 FC FE FF FF                  jmp 0x140a6a42a
00A6A52E  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00A6A532  48 25 FF FF FF CF               and rax, 0xffffffffcfffffff
00A6A538  48 0F BA E8 1C                  bts rax, 0x1c
00A6A53D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00A6A541  E9 89 F5 FF FF                  jmp 0x140a69acf
00A6A546  F0 83 8F D8 07 00 00 06         lock or dword ptr [rdi + 0x7d8], 6
00A6A54E  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A552  E9 8C F5 FF FF                  jmp 0x140a69ae3
00A6A557  F0 81 8F 50 07 00 00 00 02 00 00  lock or dword ptr [rdi + 0x750], 0x200
00A6A562  F0 81 8F 50 07 00 00 00 09 00 00  lock or dword ptr [rdi + 0x750], 0x900
00A6A56D  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A571  E9 97 F5 FF FF                  jmp 0x140a69b0d
00A6A576  F0 44 09 8F 50 07 00 00         lock or dword ptr [rdi + 0x750], r9d
00A6A57E  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A582  E9 AF F5 FF FF                  jmp 0x140a69b36
00A6A587  F0 81 8F 50 07 00 00 80 00 00 00  lock or dword ptr [rdi + 0x750], 0x80
00A6A592  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A596  E9 EC F5 FF FF                  jmp 0x140a69b87
00A6A59B  83 3D 92 C8 55 00 00            cmp dword ptr [rip + 0x55c892], 0
00A6A5A2  0F 85 95 FA FF FF               jne 0x140a6a03d
00A6A5A8  F0 83 8F 50 07 00 00 02         lock or dword ptr [rdi + 0x750], 2
00A6A5B0  48 B8 00 00 00 00 00 03 00 00   movabs rax, 0x30000000000
00A6A5BA  48 0B F0                        or rsi, rax
00A6A5BD  E9 9A FE FF FF                  jmp 0x140a6a45c
00A6A5C2  8B 87 50 07 00 00               mov eax, dword ptr [rdi + 0x750]
00A6A5C8  A8 01                           test al, 1
00A6A5CA  0F 84 ED F5 FF FF               je 0x140a69bbd
00A6A5D0  F0 83 8F 50 07 00 00 04         lock or dword ptr [rdi + 0x750], 4
00A6A5D8  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A5DC  E9 DC F5 FF FF                  jmp 0x140a69bbd
00A6A5E1  C6 87 F8 05 00 00 06            mov byte ptr [rdi + 0x5f8], 6
00A6A5E8  E9 D3 FE FF FF                  jmp 0x140a6a4c0
00A6A5ED  C6 87 F8 05 00 00 08            mov byte ptr [rdi + 0x5f8], 8
00A6A5F4  E9 9D FE FF FF                  jmp 0x140a6a496
00A6A5F9  C6 87 F9 05 00 00 08            mov byte ptr [rdi + 0x5f9], 8
00A6A600  E9 9E FE FF FF                  jmp 0x140a6a4a3
00A6A605  F0 81 8F 50 07 00 00 00 00 00 01  lock or dword ptr [rdi + 0x750], 0x1000000
00A6A610  E9 83 4A 0D 00                  jmp 0x140b3f098
00A6A615  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00A6A619  48 C1 E9 04                     shr rcx, 4
00A6A61D  41 23 CD                        and ecx, r13d
00A6A620  83 F9 01                        cmp ecx, 1
00A6A623  0F 85 E1 F5 FF FF               jne 0x140a69c0a
00A6A629  48 83 CE 30                     or rsi, 0x30
00A6A62D  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
00A6A631  E9 D4 F5 FF FF                  jmp 0x140a69c0a
00A6A636  48 8B C6                        mov rax, rsi
00A6A639  48 C1 E8 30                     shr rax, 0x30
00A6A63D  41 22 C5                        and al, r13b
00A6A640  3C 01                           cmp al, 1
00A6A642  0F 84 DE F5 FF FF               je 0x140a69c26
00A6A648  48 B8 00 00 00 00 00 00 03 00   movabs rax, 0x3000000000000
00A6A652  48 0B F0                        or rsi, rax
00A6A655  E9 98 FE FF FF                  jmp 0x140a6a4f2
00A6A65A  F0 09 97 50 07 00 00            lock or dword ptr [rdi + 0x750], edx
00A6A661  E9 3B 4A 0D 00                  jmp 0x140b3f0a1
00A6A666  F0 81 8F 50 07 00 00 00 00 01 00  lock or dword ptr [rdi + 0x750], 0x10000
00A6A671  E9 2B 4A 0D 00                  jmp 0x140b3f0a1
00A6A676  F0 09 97 50 07 00 00            lock or dword ptr [rdi + 0x750], edx
00A6A67D  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00A6A681  E9 E1 F5 FF FF                  jmp 0x140a69c67
00A6A686  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00A6A68A  48 83 E0 CF                     and rax, 0xffffffffffffffcf
00A6A68E  48 0F BA E8 04                  bts rax, 4
00A6A693  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00A6A697  E9 72 F6 FF FF                  jmp 0x140a69d0e
00A6A69C  48 83 4D C8 30                  or qword ptr [rbp - 0x38], 0x30
00A6A6A1  E9 68 F6 FF FF                  jmp 0x140a69d0e
00A6A6A6  F0 44 09 87 50 07 00 00         lock or dword ptr [rdi + 0x750], r8d
00A6A6AE  E9 7D F6 FF FF                  jmp 0x140a69d30
00A6A6B3  F0 09 97 50 07 00 00            lock or dword ptr [rdi + 0x750], edx
00A6A6BA  E9 71 F6 FF FF                  jmp 0x140a69d30
00A6A6BF  F0 44 09 87 50 07 00 00         lock or dword ptr [rdi + 0x750], r8d
00A6A6C7  E9 80 F6 FF FF                  jmp 0x140a69d4c
00A6A6CC  F0 83 8F 54 07 00 00 01         lock or dword ptr [rdi + 0x754], 1
00A6A6D4  E9 87 F6 FF FF                  jmp 0x140a69d60
00A6A6D9  F0 83 8F 54 07 00 00 04         lock or dword ptr [rdi + 0x754], 4
00A6A6E1  E9 9C F6 FF FF                  jmp 0x140a69d82
00A6A6E6  F0 44 09 9F 54 07 00 00         lock or dword ptr [rdi + 0x754], r11d
00A6A6EE  E9 C1 F6 FF FF                  jmp 0x140a69db4
00A6A6F3  F0 44 09 8F 54 07 00 00         lock or dword ptr [rdi + 0x754], r9d
00A6A6FB  E9 D6 F6 FF FF                  jmp 0x140a69dd6
00A6A700  F0 83 8F 54 07 00 00 10         lock or dword ptr [rdi + 0x754], 0x10
00A6A708  E9 EA F6 FF FF                  jmp 0x140a69df7
00A6A70D  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00A6A711  48 C1 E9 14                     shr rcx, 0x14
00A6A715  41 23 CD                        and ecx, r13d
00A6A718  83 F9 01                        cmp ecx, 1
00A6A71B  0F 85 89 49 0D 00               jne 0x140b3f0aa
00A6A721  F0 83 8F 54 07 00 00 40         lock or dword ptr [rdi + 0x754], 0x40
00A6A729  E9 7C 49 0D 00                  jmp 0x140b3f0aa
00A6A72E  BA 02 00 00 00                  mov edx, 2
00A6A733  E9 E6 49 0D 00                  jmp 0x140b3f11e
00A6A738  BA 01 00 00 00                  mov edx, 1
00A6A73D  E9 DC 49 0D 00                  jmp 0x140b3f11e
00A6A742  F0 81 8F 50 07 00 00 00 00 00 30  lock or dword ptr [rdi + 0x750], 0x30000000
00A6A74D  E9 20 F7 FF FF                  jmp 0x140a69e72
00A6A752  F0 44 09 87 50 07 00 00         lock or dword ptr [rdi + 0x750], r8d
00A6A75A  E9 13 F7 FF FF                  jmp 0x140a69e72
00A6A75F  48 BA FF FF FF FF FF FF FF CF   movabs rdx, 0xcfffffffffffffff
00A6A769  48 23 CA                        and rcx, rdx
00A6A76C  48 0F BA E9 3C                  bts rcx, 0x3c
00A6A771  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
00A6A775  F0 81 8F 54 07 00 00 00 40 00 00  lock or dword ptr [rdi + 0x754], 0x4000
00A6A780  B8 00 00 10 00                  mov eax, 0x100000
00A6A785  F0 09 87 54 07 00 00            lock or dword ptr [rdi + 0x754], eax
00A6A78C  E9 07 F7 FF FF                  jmp 0x140a69e98
00A6A791  F0 09 87 54 07 00 00            lock or dword ptr [rdi + 0x754], eax
00A6A798  E9 E2 FA FF FF                  jmp 0x140a6a27f
00A6A79D  F0 81 8F 54 07 00 00 00 80 00 00  lock or dword ptr [rdi + 0x754], 0x8000
00A6A7A8  E9 FF F6 FF FF                  jmp 0x140a69eac
00A6A7AD  41 3A C5                        cmp al, r13b
00A6A7B0  0F 85 1F FC FF FF               jne 0x140a6a3d5
00A6A7B6  F0 81 8F 54 07 00 00 00 00 00 80  lock or dword ptr [rdi + 0x754], 0x80000000
00A6A7C1  E9 0F FC FF FF                  jmp 0x140a6a3d5
00A6A7C6  F0 81 8F 54 07 00 00 00 00 04 00  lock or dword ptr [rdi + 0x754], 0x40000
00A6A7D1  E9 06 F7 FF FF                  jmp 0x140a69edc
00A6A7D6  F0 81 8F 54 07 00 00 00 00 20 00  lock or dword ptr [rdi + 0x754], 0x200000
00A6A7E1  F0 81 8F 54 07 00 00 00 00 40 00  lock or dword ptr [rdi + 0x754], 0x400000
00A6A7EC  E9 08 F7 FF FF                  jmp 0x140a69ef9
00A6A7F1  F0 81 8F 54 07 00 00 00 00 20 00  lock or dword ptr [rdi + 0x754], 0x200000
00A6A7FC  E9 F8 F6 FF FF                  jmp 0x140a69ef9
00A6A801  F0 81 8F 54 07 00 00 00 00 80 00  lock or dword ptr [rdi + 0x754], 0x800000
00A6A80C  E9 FC F6 FF FF                  jmp 0x140a69f0d
00A6A811  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00A6A815  48 25 FF CF FF FF               and rax, 0xffffffffffffcfff
00A6A81B  48 0F BA E8 0C                  bts rax, 0xc
00A6A820  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00A6A824  F0 81 8F 54 07 00 00 00 00 00 08  lock or dword ptr [rdi + 0x754], 0x8000000
00A6A82F  E9 F3 F6 FF FF                  jmp 0x140a69f27
00A6A834  F0 44 09 87 54 07 00 00         lock or dword ptr [rdi + 0x754], r8d
00A6A83C  E9 FA F6 FF FF                  jmp 0x140a69f3b
00A6A841  BA 01 00 00 00                  mov edx, 1
00A6A846  48 8B CF                        mov rcx, rdi
00A6A849  E8 86 1A 01 00                  call 0x140a7c2d4
00A6A84E  E9 1F F7 FF FF                  jmp 0x140a69f72
00A6A853  F0 83 8F D8 07 00 00 01         lock or dword ptr [rdi + 0x7d8], 1
00A6A85B  E9 32 F7 FF FF                  jmp 0x140a69f92
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspApplyMitigationOptions(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 3804531)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m78 = v_xmm2;
    v_stack_m60 = v_xmm0;
    v_stack_m68 = v_xmm3;
    v_stack_m50 = v_xmm1;
    if ((*(unsigned __int16 *)(a1 + 1772)) == 332) goto loc_00A6A4FB;
loc_00A69A15:
    a1 = (v_stack_m78) >> (8);
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A3A3;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A39B;
loc_00A69A3B:
    result = (v_stack_m78) >> (16);
    result = (unsigned __int8)((result) & (3));
    if (condition_is_equal) goto loc_00A6A0CC;
    v_rsi = v_stack_m78;
    if (((unsigned __int8)(result)) == 2) {
        v_rsi = v_stack_m78;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1872)))) & (64)) != 0) goto loc_00A69A89;
    a1 = (v_rsi) >> (20);
    a1 = (unsigned int)((a1) & (3));
    if (condition_is_not_equal) goto loc_00A6A360;
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) != 0) {
        v_rsi = v_stack_m78;
    }
    if (a2 != 0) goto loc_00A6A1C5;
loc_00A69A92:
    a1 = (v_rsi) >> (28);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A2A9;
loc_00A69AA5:
    if (((*(unsigned int *)(a1 + 1872)) & (0x1000ULL)) == 0) goto loc_00A6A33B;
loc_00A69ABB:
    if (a2 == 0) goto loc_00A69ACF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 2008)))) & (2)) != 0) goto loc_00A6A52E;
loc_00A69ACF:
    a1 = (v_stack_m68) >> (28);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A546;
loc_00A69AE3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 2008)))) & (2)) == 0) goto loc_00A6A2C9;
loc_00A69AF1:
    a1 = (v_rsi) >> (36);
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A562;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A557;
loc_00A69B0D:
    v_stack_m70 = a1;
    a1 = (a1) >> (56);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A576;
loc_00A69B36:
    if (((*(unsigned int *)(a1 + 1872)) & (256)) == 0) goto loc_00A6A2EE;
    result = (v_stack_m70) & (0xFFFFFFFFFEEEFFFFULL);
    result = (result) | ((unsigned int)(0x2220000ULL));
    v_stack_m70 = result;
    result = (v_stack_m58) & (0xFFFFFFFFFEEEFFFFULL);
    result = (result) | ((unsigned int)(0x2220000ULL));
    v_stack_m58 = result;
loc_00A69B74:
    a1 = (v_rsi) >> (32);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A587;
loc_00A69B87:
    a1 = (v_rsi) >> (40);
    a1 = (unsigned int)((a1) & (3));
    if (condition_is_equal) goto loc_00A6A015;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A03D;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A204;
loc_00A69BA9:
    a1 = (v_stack_m70) >> (8);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A5C2;
loc_00A69BBD:
    a1 = (v_rsi) >> (44);
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A489;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A4B3;
loc_00A69BDE:
    if (((*(unsigned int *)(a1 + 1872)) & ((unsigned int)((unsigned int)(0x800000ULL)))) == 0) goto loc_00A6A36E;
loc_00A69BEA:
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_m78))) >> (4));
    if (((3) & ((unsigned __int8)(result))) == 0) goto loc_00A6A1A2;
loc_00A69BFB:
    a1 = (unsigned __int8)(((unsigned int)(v_stack_m78)) >> (4));
    a1 = (unsigned __int8)((a1) & (3));
    if (((unsigned __int8)(a1)) != 1) goto loc_00A6A615;
loc_00A69C0A:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & ((unsigned int)((unsigned int)(0xC000ULL))));
    if (((unsigned int)(result)) == 0x4000ULL) goto loc_00A6A4E0;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000ULL)))) goto loc_00A6A636;
loc_00A69C26:
    a1 = (v_rsi) >> (48);
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A666;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A65A;
    if (((*(unsigned int *)(a1 + 1872)) & (0x30000ULL)) != 0) goto loc_00A69C67;
    a1 = (v_stack_m60) >> (48);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A676;
loc_00A69C67:
    if (a2 != 0) goto loc_00A6A22C;
loc_00A69C75:
    a1 = (v_rsi) >> (52);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A192;
loc_00A69C88:
    if (((*(unsigned int *)(a1 + 1872)) & ((unsigned int)((unsigned int)(0x80000ULL)))) == 0) goto loc_00A6A313;
loc_00A69C94:
    if (a2 != 0) goto loc_00A69FED;
loc_00A69CA2:
    a1 = (v_rsi) >> (56);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A140;
loc_00A69CB5:
    if (((*(unsigned int *)(a1 + 1872)) & ((unsigned int)((unsigned int)(0x200000ULL)))) == 0) goto loc_00A6A06B;
loc_00A69CC1:
    if (a2 != 0) goto loc_00A69FCF;
loc_00A69CD9:
    v_rsi = (v_rsi) >> (60);
    v_rsi = (unsigned int)((v_rsi) & (3));
    if (((unsigned int)(v_rsi)) == 1) goto loc_00A6A2BD;
loc_00A69CE9:
    if (a2 == 0) goto loc_00A69D0E;
    if (condition_is_below) goto loc_00A6A686;
    if ((((unsigned int)((unsigned int)(0x8000000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 1872))))) != 0) goto loc_00A6A69C;
loc_00A69D0E:
    a1 = (v_stack_m70) >> (4);
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A6B3;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A6A6;
loc_00A69D30:
    if (((*(unsigned int *)(a1 + 1872)) & ((unsigned int)((unsigned int)(0xC000000ULL)))) != 0) goto loc_00A69D4C;
    a1 = (v_stack_m58) >> (4);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A6BF;
loc_00A69D4C:
    a1 = (v_stack_m70) >> (28);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A6CC;
loc_00A69D60:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1876)))) & (1)) == 0) goto loc_00A6A150;
loc_00A69D6E:
    a1 = (v_stack_m70) >> (32);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A6D9;
loc_00A69D82:
    a1 = (v_stack_m70) >> (48);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) {
    }
    a1 = (v_stack_m70) >> (52);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A6E6;
loc_00A69DB4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1876)))) & (4)) == 0) goto loc_00A6A171;
loc_00A69DC2:
    a1 = (v_stack_m70) >> (40);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A6F3;
loc_00A69DD6:
    if (((*(unsigned int *)(a1 + 1876)) & ((unsigned int)((unsigned int)(0x400ULL)))) == 0) goto loc_00A6A0DA;
loc_00A69DE3:
    a1 = (v_stack_m70) >> (16);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A700;
loc_00A69DF7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1876)))) & (16)) == 0) goto loc_00A6A0FB;
loc_00A69E05:
    if ((*(unsigned __int16 *)(a1 + 1772)) == 332) goto loc_00A6A70D;
    result = (v_stack_m70) >> (36);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(result)))) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A738;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A72E;
    v_rsi = (unsigned __int8)(((unsigned __int8)(result)) & (3));
    if (((unsigned __int8)(v_rsi)) != 1) goto loc_00A6A11C;
loc_00A69E46:
    if (a2 != 0) goto loc_00A6A093;
loc_00A69E55:
    a1 = (v_stack_m70) >> (44);
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A752;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A742;
loc_00A69E72:
    a2 = (v_stack_m70) >> (60);
    a2 = (unsigned int)((a2) & (3));
    if (condition_is_equal) goto loc_00A6A254;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A6A299;
    if (((unsigned int)(a2)) == 2) goto loc_00A6A75F;
loc_00A69E98:
    a1 = (v_stack_m58) >> (60);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A79D;
loc_00A69EAC:
    if (((*(unsigned int *)(a1 + 1876)) & (0x4000ULL)) != 0) goto loc_00A6A3B4;
    result = (v_stack_m68) & (-2);
    result = (result) | (2);
loc_00A69EC8:
    a1 = (unsigned int)((v_stack_m50) & (3));
    v_stack_m68 = result;
    if (((unsigned int)(a1)) == 1) goto loc_00A6A7C6;
loc_00A69EDC:
    a1 = (v_stack_m68) >> (4);
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A7F1;
    if (((unsigned int)(a1)) == 2) goto loc_00A6A7D6;
loc_00A69EF9:
    a1 = (v_stack_m50) >> (4);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A801;
loc_00A69F0D:
    a1 = (v_stack_m68) >> (12);
    a1 = (unsigned int)((a1) & (3));
    if (condition_is_equal) goto loc_00A6A811;
    if (((unsigned int)(a1)) == 1) goto loc_00A6A824;
loc_00A69F27:
    a1 = (v_stack_m50) >> (12);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A834;
loc_00A69F3B:
    a1 = (v_stack_m68) >> (16);
    a1 = (unsigned int)((a1) & (3));
    if (condition_is_equal) goto loc_00A6A05C;
    if (((unsigned int)(a1)) == 1) {
    }
    result = (v_stack_m68) >> (20);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(result)))) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A841;
loc_00A69F72:
    v_rbx = (unsigned __int8)(((unsigned __int8)(result)) & (3));
    if (((unsigned __int8)(v_rbx)) != 1) goto loc_00A6A465;
loc_00A69F7E:
    a1 = (v_stack_m68) >> (24);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) == 1) goto loc_00A6A853;
loc_00A69F92:
    *(unsigned __int64 *)(a3) = v_xmm0;
    *(unsigned __int64 *)(a3 + 16) = v_xmm1;
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    v_rsp = (v_rsp) + (128);
    return result;
loc_00A69FCF:
    if (((*(unsigned int *)(a2 + 1872)) & ((unsigned int)(a2))) == 0) goto loc_00A69CD9;
    v_rsi = (v_rsi) & (a1);
    v_stack_m78 = v_rsi;
    goto loc_00A69CD9;
loc_00A69FED:
    if (((*(unsigned int *)(a2 + 1872)) & ((unsigned int)(a2))) == 0) goto loc_00A69CA2;
    v_rsi = (v_rsi) & (result);
    v_stack_m78 = v_rsi;
    goto loc_00A69CA2;
loc_00A6A015:
    if ((((unsigned __int8)(v_stack_p10)) & (8)) == 0) goto loc_00A69BA9;
    v_rsi = (v_rsi) & (result);
    v_stack_m78 = v_rsi;
    if ((((unsigned __int8)(v_stack_p10)) & (32)) != 0) goto loc_00A6A59B;
loc_00A6A03D:
    if ((((unsigned __int8)(v_stack_p10)) & (16)) == 0) {
    }
    goto loc_00A69BA9;
loc_00A6A05C:
    if (condition_is_above_or_equal) goto loc_00A69F51;
    goto loc_00A69F59;
loc_00A6A06B:
    a1 = (v_stack_m60) >> (56);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69CC1;
    goto loc_00A69CC1;
loc_00A6A093:
    if ((((unsigned int)((unsigned int)(0x10000000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 1872))))) == 0) goto loc_00A69E55;
    if (condition_is_below) goto loc_00A69E55;
    result = (v_stack_m70) & (a1);
    v_stack_m70 = result;
    goto loc_00A69E55;
loc_00A6A0CC:
    if ((((unsigned __int8)(v_stack_p10)) & (1)) != 0) goto loc_00A69A5E;
    goto loc_00A69A52;
loc_00A6A0DA:
    a1 = (v_stack_m58) >> (40);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69DE3;
    goto loc_00A69DE3;
loc_00A6A0FB:
    a1 = (v_stack_m58) >> (16);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69E05;
    goto loc_00A69E05;
loc_00A6A11C:
    a1 = (v_stack_m58) >> (36);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69E46;
    result = PspSetNoChildProcessRestrictedPolicy(a1, 3, (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    goto loc_00A69E46;
loc_00A6A140:
    goto loc_00A69CB5;
loc_00A6A150:
    a1 = (v_stack_m58) >> (28);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69D6E;
    goto loc_00A69D6E;
loc_00A6A171:
    a1 = (v_stack_m58) >> (32);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69DC2;
    goto loc_00A69DC2;
loc_00A6A192:
    goto loc_00A69C88;
loc_00A6A1A2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1872)))) & (1)) == 0) goto loc_00A69BFB;
    v_rsi = (v_stack_m78) & (-49);
    v_stack_m78 = v_rsi;
    goto loc_00A69BFB;
loc_00A6A1C5:
    a1 = (v_rsi) >> (24);
    a1 = (unsigned int)((a1) & (3));
    if (condition_is_not_equal) goto loc_00A6A4D2;
    if ((((unsigned __int8)(v_stack_p10)) & (4)) != 0) goto loc_00A6A3E7;
loc_00A6A1DE:
    if (((*(unsigned int *)(a2 + 1872)) & (0x1000ULL)) == 0) goto loc_00A69A92;
    v_rsi = (v_rsi) & (0xFFFFFFFFCFFFFFFFULL);
    v_stack_m78 = v_rsi;
    goto loc_00A69A92;
loc_00A6A204:
    if ((*(unsigned int *)(v_rip + 5622825)) != 0) goto loc_00A6A44A;
    goto loc_00A6A03D;
loc_00A6A22C:
    if (((*(unsigned int *)(a2 + 1872)) & (3)) == 0) goto loc_00A69C75;
    v_rsi = (v_rsi) & ((unsigned int)(*(unsigned int *)(a1 + 1872)));
    v_stack_m78 = v_rsi;
    goto loc_00A69C75;
loc_00A6A254:
    if (condition_is_above_or_equal) goto loc_00A69E98;
    if ((((unsigned int)((unsigned int)(0x100000ULL))) & ((unsigned int)(v_stack_p10))) != 0) goto loc_00A69E98;
    if (condition_is_below) goto loc_00A69E98;
    if (condition_is_below) goto loc_00A6A791;
loc_00A6A27F:
    result = (v_stack_m70) & (3);
    v_stack_m70 = result;
loc_00A6A299:
    goto loc_00A69E98;
loc_00A6A2A9:
    goto loc_00A69AA5;
loc_00A6A2BD:
    goto loc_00A69CE9;
loc_00A6A2C9:
    a1 = (v_stack_m50) >> (28);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69AF1;
    goto loc_00A69AF1;
loc_00A6A2EE:
    a1 = (v_stack_m60) >> (36);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69B74;
    goto loc_00A69B74;
loc_00A6A313:
    a1 = (v_stack_m60) >> (52);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69C94;
    goto loc_00A69C94;
loc_00A6A33B:
    a1 = (v_stack_m60) >> (28);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69ABB;
    goto loc_00A69ABB;
loc_00A6A360:
    if (((unsigned int)(a1)) == 1) goto loc_00A69A7D;
    goto loc_00A69A89;
loc_00A6A36E:
    a1 = (v_stack_m60) >> (44);
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A6A605;
    if (((unsigned int)(a1)) != 2) goto loc_00A69BEA;
loc_00A6A39B:
loc_00A6A3A3:
    goto loc_00A69A3B;
loc_00A6A3B4:
    result = (unsigned __int8)((v_stack_m68) & (3));
    if (condition_is_not_equal) goto loc_00A6A7AD;
    if (condition_is_below) goto loc_00A6A7B6;
loc_00A6A3D5:
    result = (v_stack_m68) & (-4);
    goto loc_00A69EC8;
loc_00A6A3E7:
    result = ObReferenceProcessHandleTable(a1, 3, (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    if (result == 0) goto loc_00A6A1DE;
    result = ExpLockHandleTableExclusive(result, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    if (*(unsigned __int64 *)(result + 96) != 0) goto loc_00A6A518;
    result = *(unsigned __int8 *)(result + 44);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 44))) & (2)) == 0) {
        result = (unsigned __int8)((*(unsigned __int8 *)(result + 44)) | (2));
        *(unsigned __int8 *)(result + 44) = (unsigned __int8)(result);
    }
    result = ExpUnlockHandleTableExclusive(result, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    result = ExReleaseRundownProtection(a1 + 488, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    goto loc_00A6A1DE;
loc_00A6A44A:
    v_rsi = (v_stack_m78) & (result);
loc_00A6A45C:
    v_stack_m78 = v_rsi;
    goto loc_00A6A03D;
loc_00A6A465:
    a1 = (v_stack_m50) >> (20);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69F7E;
    result = PspSetRedirectionTrustPolicy(a1, a1 + 1, (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    goto loc_00A69F7E;
loc_00A6A489:
    if ((*(unsigned __int8 *)(a1 + 1528)) < 8) goto loc_00A6A5ED;
loc_00A6A496:
    if ((*(unsigned __int8 *)(a1 + 1529)) < 8) goto loc_00A6A5F9;
loc_00A6A4A3:
    goto loc_00A69BDE;
loc_00A6A4B3:
    if ((*(unsigned __int8 *)(a1 + 1528)) < 6) goto loc_00A6A5E1;
loc_00A6A4C0:
    if ((*(unsigned __int8 *)(a1 + 1529)) >= 6) goto loc_00A6A4A3;
    *(unsigned __int8 *)(a1 + 1529) = 6;
    goto loc_00A6A4A3;
loc_00A6A4D2:
    if (((unsigned int)(a1)) != 1) goto loc_00A6A1DE;
    goto loc_00A6A3E7;
loc_00A6A4E0:
    v_rsi = (v_stack_m78) & (result);
loc_00A6A4F2:
    v_stack_m78 = v_rsi;
    goto loc_00A69C26;
loc_00A6A4FB:
    v_stack_m98 = v_xmm2;
    v_stack_m88 = v_xmm3;
    result = PspDecodeMitigationExecuteOptions(v_stack_m98, a1 + 1, (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    *(unsigned __int8 *)(a1 + 147) = (unsigned __int8)(result);
    goto loc_00A69A15;
loc_00A6A518:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m98 + 8)))) & (8)) != 0) goto loc_00A6A42A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m98 + 8))) | (8));
    *(unsigned int *)(v_stack_m98 + 8) = (unsigned int)(result);
    goto loc_00A6A42A;
loc_00A6A52E:
    result = (v_stack_m68) & (0xFFFFFFFFCFFFFFFFULL);
    v_stack_m68 = result;
    goto loc_00A69ACF;
loc_00A6A546:
    goto loc_00A69AE3;
loc_00A6A557:
loc_00A6A562:
    goto loc_00A69B0D;
loc_00A6A576:
    goto loc_00A69B36;
loc_00A6A587:
    goto loc_00A69B87;
loc_00A6A59B:
    if ((*(unsigned int *)(v_rip + 5621906)) != 0) goto loc_00A6A03D;
    v_rsi = (v_stack_m78) | (result);
    goto loc_00A6A45C;
loc_00A6A5C2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1872)))) & (1)) == 0) goto loc_00A69BBD;
    goto loc_00A69BBD;
loc_00A6A5E1:
    *(unsigned __int8 *)(a1 + 1528) = 6;
    goto loc_00A6A4C0;
loc_00A6A5ED:
    *(unsigned __int8 *)(a1 + 1528) = 8;
    goto loc_00A6A496;
loc_00A6A5F9:
    *(unsigned __int8 *)(a1 + 1529) = 8;
    goto loc_00A6A4A3;
loc_00A6A605:
loc_00A6A615:
    a1 = (v_stack_m60) >> (4);
    a1 = (unsigned int)((a1) & (3));
    if (((unsigned int)(a1)) != 1) goto loc_00A69C0A;
    v_rsi = (v_stack_m78) | (48);
    v_stack_m78 = v_rsi;
    goto loc_00A69C0A;
loc_00A6A636:
    result = (v_rsi) >> (48);
    result = (unsigned __int8)((result) & (3));
    if (((unsigned __int8)(result)) == 1) goto loc_00A69C26;
    v_rsi = (v_rsi) | (result);
    goto loc_00A6A4F2;
loc_00A6A65A:
loc_00A6A666:
loc_00A6A676:
    goto loc_00A69C67;
loc_00A6A686:
    result = (v_stack_m70) & (-49);
    v_stack_m70 = result;
    goto loc_00A69D0E;
loc_00A6A69C:
    goto loc_00A69D0E;
loc_00A6A6A6:
    goto loc_00A69D30;
loc_00A6A6B3:
    goto loc_00A69D30;
loc_00A6A6BF:
    goto loc_00A69D4C;
loc_00A6A6CC:
    goto loc_00A69D60;
loc_00A6A6D9:
    goto loc_00A69D82;
loc_00A6A6E6:
    goto loc_00A69DB4;
loc_00A6A6F3:
    goto loc_00A69DD6;
loc_00A6A700:
    goto loc_00A69DF7;
loc_00A6A70D:
    a1 = (v_stack_m70) >> (20);
    a1 = (unsigned int)((a1) & (3));
loc_00A6A72E:
loc_00A6A738:
loc_00A6A742:
    goto loc_00A69E72;
loc_00A6A752:
    goto loc_00A69E72;
loc_00A6A75F:
    a1 = (a1) & (1);
    v_stack_m70 = a1;
    goto loc_00A69E98;
loc_00A6A791:
    goto loc_00A6A27F;
loc_00A6A79D:
    goto loc_00A69EAC;
loc_00A6A7AD:
    if (((unsigned __int8)((unsigned int)(0x100000ULL))) != 3) goto loc_00A6A3D5;
loc_00A6A7B6:
    goto loc_00A6A3D5;
loc_00A6A7C6:
    goto loc_00A69EDC;
loc_00A6A7D6:
    goto loc_00A69EF9;
loc_00A6A7F1:
    goto loc_00A69EF9;
loc_00A6A801:
    goto loc_00A69F0D;
loc_00A6A811:
    result = (v_stack_m68) & (0xFFFFFFFFFFFFCFFFULL);
    v_stack_m68 = result;
loc_00A6A824:
    goto loc_00A69F27;
loc_00A6A834:
    goto loc_00A69F3B;
loc_00A6A841:
    result = PspSetRedirectionTrustPolicy(a1, 1, (unsigned int)(0x10000000ULL), (unsigned int)(0x400ULL));
    goto loc_00A69F72;
loc_00A6A853:
    goto loc_00A69F92;
}
```

## 5. (Beta) C Style

```c
int64_t PspApplyMitigationOptions(void *Arg1, int64_t Arg2, void *Arg3, void *Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x3A0D73)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m78 = v_xmm2;
    v_stack_m60 = v_xmm0;
    v_stack_m68 = v_xmm3;
    v_stack_m50 = v_xmm1;
    if ((*(uint16_t *)(arg1 + 0x6EC)) == 332) goto loc_00A6A4FB;
loc_00A69A15:
    Arg1 = (v_stack_m78) >> (8);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A3A3;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A39B;
loc_00A69A3B:
    result = (v_stack_m78) >> (16);
    result = (uint8_t)((result) & (3));
    if (condition_is_equal) goto loc_00A6A0CC;
    local_rsi = v_stack_m78;
    if (((uint8_t)(result)) == 2) {
        local_rsi = v_stack_m78;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x750)))) & (64)) != 0) goto loc_00A69A89;
    Arg1 = (local_rsi) >> (20);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (condition_is_not_equal) goto loc_00A6A360;
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) != 0) {
        local_rsi = v_stack_m78;
    }
    if (Arg2 != 0) goto loc_00A6A1C5;
loc_00A69A92:
    Arg1 = (local_rsi) >> (28);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A2A9;
loc_00A69AA5:
    if (((*(uint32_t *)(arg1 + 0x750)) & (0x1000ULL)) == 0) goto loc_00A6A33B;
loc_00A69ABB:
    if (Arg2 == 0) goto loc_00A69ACF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x7D8)))) & (2)) != 0) goto loc_00A6A52E;
loc_00A69ACF:
    Arg1 = (v_stack_m68) >> (28);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A546;
loc_00A69AE3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7D8)))) & (2)) == 0) goto loc_00A6A2C9;
loc_00A69AF1:
    Arg1 = (local_rsi) >> (36);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A562;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A557;
loc_00A69B0D:
    v_stack_m70 = Arg1;
    Arg1 = (Arg1) >> (56);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A576;
loc_00A69B36:
    if (((*(uint32_t *)(arg1 + 0x750)) & (256)) == 0) goto loc_00A6A2EE;
    result = (v_stack_m70) & (0xFFFFFFFFFEEEFFFFULL);
    result = (result) | ((uint32_t)(0x2220000ULL));
    v_stack_m70 = result;
    result = (v_stack_m58) & (0xFFFFFFFFFEEEFFFFULL);
    result = (result) | ((uint32_t)(0x2220000ULL));
    v_stack_m58 = result;
loc_00A69B74:
    Arg1 = (local_rsi) >> (32);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A587;
loc_00A69B87:
    Arg1 = (local_rsi) >> (40);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (condition_is_equal) goto loc_00A6A015;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A03D;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A204;
loc_00A69BA9:
    Arg1 = (v_stack_m70) >> (8);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A5C2;
loc_00A69BBD:
    Arg1 = (local_rsi) >> (44);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A489;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A4B3;
loc_00A69BDE:
    if (((*(uint32_t *)(arg1 + 0x750)) & ((uint32_t)((uint32_t)(0x800000ULL)))) == 0) goto loc_00A6A36E;
loc_00A69BEA:
    result = (uint8_t)(((uint8_t)((uint32_t)(v_stack_m78))) >> (4));
    if (((3) & ((uint8_t)(result))) == 0) goto loc_00A6A1A2;
loc_00A69BFB:
    Arg1 = (uint8_t)(((uint32_t)(v_stack_m78)) >> (4));
    Arg1 = (uint8_t)((Arg1) & (3));
    if (((uint8_t)(Arg1)) != 1) goto loc_00A6A615;
loc_00A69C0A:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & ((uint32_t)((uint32_t)(0xC000ULL))));
    if (((uint32_t)(result)) == 0x4000ULL) goto loc_00A6A4E0;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000ULL)))) goto loc_00A6A636;
loc_00A69C26:
    Arg1 = (local_rsi) >> (48);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A666;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A65A;
    if (((*(uint32_t *)(arg1 + 0x750)) & (0x30000ULL)) != 0) goto loc_00A69C67;
    Arg1 = (v_stack_m60) >> (48);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A676;
loc_00A69C67:
    if (Arg2 != 0) goto loc_00A6A22C;
loc_00A69C75:
    Arg1 = (local_rsi) >> (52);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A192;
loc_00A69C88:
    if (((*(uint32_t *)(arg1 + 0x750)) & ((uint32_t)((uint32_t)(0x80000ULL)))) == 0) goto loc_00A6A313;
loc_00A69C94:
    if (Arg2 != 0) goto loc_00A69FED;
loc_00A69CA2:
    Arg1 = (local_rsi) >> (56);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A140;
loc_00A69CB5:
    if (((*(uint32_t *)(arg1 + 0x750)) & ((uint32_t)((uint32_t)(0x200000ULL)))) == 0) goto loc_00A6A06B;
loc_00A69CC1:
    if (Arg2 != 0) goto loc_00A69FCF;
loc_00A69CD9:
    local_rsi = (local_rsi) >> (60);
    local_rsi = (uint32_t)((local_rsi) & (3));
    if (((uint32_t)(local_rsi)) == 1) goto loc_00A6A2BD;
loc_00A69CE9:
    if (Arg2 == 0) goto loc_00A69D0E;
    if (condition_is_below) goto loc_00A6A686;
    if ((((uint32_t)((uint32_t)(0x8000000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x750))))) != 0) goto loc_00A6A69C;
loc_00A69D0E:
    Arg1 = (v_stack_m70) >> (4);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A6B3;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A6A6;
loc_00A69D30:
    if (((*(uint32_t *)(arg1 + 0x750)) & ((uint32_t)((uint32_t)(0xC000000ULL)))) != 0) goto loc_00A69D4C;
    Arg1 = (v_stack_m58) >> (4);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A6BF;
loc_00A69D4C:
    Arg1 = (v_stack_m70) >> (28);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A6CC;
loc_00A69D60:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x754)))) & (1)) == 0) goto loc_00A6A150;
loc_00A69D6E:
    Arg1 = (v_stack_m70) >> (32);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A6D9;
loc_00A69D82:
    Arg1 = (v_stack_m70) >> (48);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) {
    }
    Arg1 = (v_stack_m70) >> (52);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A6E6;
loc_00A69DB4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x754)))) & (4)) == 0) goto loc_00A6A171;
loc_00A69DC2:
    Arg1 = (v_stack_m70) >> (40);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A6F3;
loc_00A69DD6:
    if (((*(uint32_t *)(arg1 + 0x754)) & ((uint32_t)((uint32_t)(0x400ULL)))) == 0) goto loc_00A6A0DA;
loc_00A69DE3:
    Arg1 = (v_stack_m70) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A700;
loc_00A69DF7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x754)))) & (16)) == 0) goto loc_00A6A0FB;
loc_00A69E05:
    if ((*(uint16_t *)(arg1 + 0x6EC)) == 332) goto loc_00A6A70D;
    result = (v_stack_m70) >> (36);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(result)))) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A738;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A72E;
    local_rsi = (uint8_t)(((uint8_t)(result)) & (3));
    if (((uint8_t)(local_rsi)) != 1) goto loc_00A6A11C;
loc_00A69E46:
    if (Arg2 != 0) goto loc_00A6A093;
loc_00A69E55:
    Arg1 = (v_stack_m70) >> (44);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A752;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A742;
loc_00A69E72:
    Arg2 = (v_stack_m70) >> (60);
    Arg2 = (uint32_t)((Arg2) & (3));
    if (condition_is_equal) goto loc_00A6A254;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A6A299;
    if (((uint32_t)(Arg2)) == 2) goto loc_00A6A75F;
loc_00A69E98:
    Arg1 = (v_stack_m58) >> (60);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A79D;
loc_00A69EAC:
    if (((*(uint32_t *)(arg1 + 0x754)) & (0x4000ULL)) != 0) goto loc_00A6A3B4;
    result = (v_stack_m68) & (-2);
    result = (result) | (2);
loc_00A69EC8:
    Arg1 = (uint32_t)((v_stack_m50) & (3));
    v_stack_m68 = result;
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A7C6;
loc_00A69EDC:
    Arg1 = (v_stack_m68) >> (4);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A7F1;
    if (((uint32_t)(Arg1)) == 2) goto loc_00A6A7D6;
loc_00A69EF9:
    Arg1 = (v_stack_m50) >> (4);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A801;
loc_00A69F0D:
    Arg1 = (v_stack_m68) >> (12);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (condition_is_equal) goto loc_00A6A811;
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A824;
loc_00A69F27:
    Arg1 = (v_stack_m50) >> (12);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A834;
loc_00A69F3B:
    Arg1 = (v_stack_m68) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (condition_is_equal) goto loc_00A6A05C;
    if (((uint32_t)(Arg1)) == 1) {
    }
    result = (v_stack_m68) >> (20);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(result)))) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A841;
loc_00A69F72:
    local_rbx = (uint8_t)(((uint8_t)(result)) & (3));
    if (((uint8_t)(local_rbx)) != 1) goto loc_00A6A465;
loc_00A69F7E:
    Arg1 = (v_stack_m68) >> (24);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) == 1) goto loc_00A6A853;
loc_00A69F92:
    *(uint64_t *)(arg3) = v_xmm0;
    *(uint64_t *)(arg3 + 0x10) = v_xmm1;
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    local_rsp = (local_rsp) + (128);
    return result;
loc_00A69FCF:
    if (((*(uint32_t *)(Arg2 + 0x750)) & ((uint32_t)(Arg2))) == 0) goto loc_00A69CD9;
    local_rsi = (local_rsi) & (Arg1);
    v_stack_m78 = local_rsi;
    goto loc_00A69CD9;
loc_00A69FED:
    if (((*(uint32_t *)(Arg2 + 0x750)) & ((uint32_t)(Arg2))) == 0) goto loc_00A69CA2;
    local_rsi = (local_rsi) & (result);
    v_stack_m78 = local_rsi;
    goto loc_00A69CA2;
loc_00A6A015:
    if ((((uint8_t)(v_stack_p10)) & (8)) == 0) goto loc_00A69BA9;
    local_rsi = (local_rsi) & (result);
    v_stack_m78 = local_rsi;
    if ((((uint8_t)(v_stack_p10)) & (32)) != 0) goto loc_00A6A59B;
loc_00A6A03D:
    if ((((uint8_t)(v_stack_p10)) & (16)) == 0) {
    }
    goto loc_00A69BA9;
loc_00A6A05C:
    if (condition_is_above_or_equal) goto loc_00A69F51;
    goto loc_00A69F59;
loc_00A6A06B:
    Arg1 = (v_stack_m60) >> (56);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69CC1;
    goto loc_00A69CC1;
loc_00A6A093:
    if ((((uint32_t)((uint32_t)(0x10000000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x750))))) == 0) goto loc_00A69E55;
    if (condition_is_below) goto loc_00A69E55;
    result = (v_stack_m70) & (Arg1);
    v_stack_m70 = result;
    goto loc_00A69E55;
loc_00A6A0CC:
    if ((((uint8_t)(v_stack_p10)) & (1)) != 0) goto loc_00A69A5E;
    goto loc_00A69A52;
loc_00A6A0DA:
    Arg1 = (v_stack_m58) >> (40);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69DE3;
    goto loc_00A69DE3;
loc_00A6A0FB:
    Arg1 = (v_stack_m58) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69E05;
    goto loc_00A69E05;
loc_00A6A11C:
    Arg1 = (v_stack_m58) >> (36);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69E46;
    result = PspSetNoChildProcessRestrictedPolicy(Arg1, 3, (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    goto loc_00A69E46;
loc_00A6A140:
    goto loc_00A69CB5;
loc_00A6A150:
    Arg1 = (v_stack_m58) >> (28);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69D6E;
    goto loc_00A69D6E;
loc_00A6A171:
    Arg1 = (v_stack_m58) >> (32);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69DC2;
    goto loc_00A69DC2;
loc_00A6A192:
    goto loc_00A69C88;
loc_00A6A1A2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x750)))) & (1)) == 0) goto loc_00A69BFB;
    local_rsi = (v_stack_m78) & (-49);
    v_stack_m78 = local_rsi;
    goto loc_00A69BFB;
loc_00A6A1C5:
    Arg1 = (local_rsi) >> (24);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (condition_is_not_equal) goto loc_00A6A4D2;
    if ((((uint8_t)(v_stack_p10)) & (4)) != 0) goto loc_00A6A3E7;
loc_00A6A1DE:
    if (((*(uint32_t *)(Arg2 + 0x750)) & (0x1000ULL)) == 0) goto loc_00A69A92;
    local_rsi = (local_rsi) & (0xFFFFFFFFCFFFFFFFULL);
    v_stack_m78 = local_rsi;
    goto loc_00A69A92;
loc_00A6A204:
    if ((*(uint32_t *)(v_rip + 0x55CC29)) != 0) goto loc_00A6A44A;
    goto loc_00A6A03D;
loc_00A6A22C:
    if (((*(uint32_t *)(Arg2 + 0x750)) & (3)) == 0) goto loc_00A69C75;
    local_rsi = (local_rsi) & ((uint32_t)(*(uint32_t *)(arg1 + 0x750)));
    v_stack_m78 = local_rsi;
    goto loc_00A69C75;
loc_00A6A254:
    if (condition_is_above_or_equal) goto loc_00A69E98;
    if ((((uint32_t)((uint32_t)(0x100000ULL))) & ((uint32_t)(v_stack_p10))) != 0) goto loc_00A69E98;
    if (condition_is_below) goto loc_00A69E98;
    if (condition_is_below) goto loc_00A6A791;
loc_00A6A27F:
    result = (v_stack_m70) & (3);
    v_stack_m70 = result;
loc_00A6A299:
    goto loc_00A69E98;
loc_00A6A2A9:
    goto loc_00A69AA5;
loc_00A6A2BD:
    goto loc_00A69CE9;
loc_00A6A2C9:
    Arg1 = (v_stack_m50) >> (28);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69AF1;
    goto loc_00A69AF1;
loc_00A6A2EE:
    Arg1 = (v_stack_m60) >> (36);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69B74;
    goto loc_00A69B74;
loc_00A6A313:
    Arg1 = (v_stack_m60) >> (52);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69C94;
    goto loc_00A69C94;
loc_00A6A33B:
    Arg1 = (v_stack_m60) >> (28);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69ABB;
    goto loc_00A69ABB;
loc_00A6A360:
    if (((uint32_t)(Arg1)) == 1) goto loc_00A69A7D;
    goto loc_00A69A89;
loc_00A6A36E:
    Arg1 = (v_stack_m60) >> (44);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A6A605;
    if (((uint32_t)(Arg1)) != 2) goto loc_00A69BEA;
loc_00A6A39B:
loc_00A6A3A3:
    goto loc_00A69A3B;
loc_00A6A3B4:
    result = (uint8_t)((v_stack_m68) & (3));
    if (condition_is_not_equal) goto loc_00A6A7AD;
    if (condition_is_below) goto loc_00A6A7B6;
loc_00A6A3D5:
    result = (v_stack_m68) & (-4);
    goto loc_00A69EC8;
loc_00A6A3E7:
    result = ObReferenceProcessHandleTable(Arg1, 3, (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    if (result == 0) goto loc_00A6A1DE;
    result = ExpLockHandleTableExclusive(result, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    if (*(uint64_t *)(result + 0x60) != 0) goto loc_00A6A518;
    result = *(uint8_t *)(result + 0x2C);
    if ((((uint8_t)(*(uint8_t *)(result + 0x2C))) & (2)) == 0) {
        result = (uint8_t)((*(uint8_t *)(result + 0x2C)) | (2));
        *(uint8_t *)(result + 0x2C) = (uint8_t)(result);
    }
    result = ExpUnlockHandleTableExclusive(result, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    result = ExReleaseRundownProtection(Arg1 + 488, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    goto loc_00A6A1DE;
loc_00A6A44A:
    local_rsi = (v_stack_m78) & (result);
loc_00A6A45C:
    v_stack_m78 = local_rsi;
    goto loc_00A6A03D;
loc_00A6A465:
    Arg1 = (v_stack_m50) >> (20);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69F7E;
    result = PspSetRedirectionTrustPolicy(Arg1, Arg1 + 1, (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    goto loc_00A69F7E;
loc_00A6A489:
    if ((*(uint8_t *)(arg1 + 0x5F8)) < 8) goto loc_00A6A5ED;
loc_00A6A496:
    if ((*(uint8_t *)(arg1 + 0x5F9)) < 8) goto loc_00A6A5F9;
loc_00A6A4A3:
    goto loc_00A69BDE;
loc_00A6A4B3:
    if ((*(uint8_t *)(arg1 + 0x5F8)) < 6) goto loc_00A6A5E1;
loc_00A6A4C0:
    if ((*(uint8_t *)(arg1 + 0x5F9)) >= 6) goto loc_00A6A4A3;
    *(uint8_t *)(arg1 + 0x5F9) = 6;
    goto loc_00A6A4A3;
loc_00A6A4D2:
    if (((uint32_t)(Arg1)) != 1) goto loc_00A6A1DE;
    goto loc_00A6A3E7;
loc_00A6A4E0:
    local_rsi = (v_stack_m78) & (result);
loc_00A6A4F2:
    v_stack_m78 = local_rsi;
    goto loc_00A69C26;
loc_00A6A4FB:
    v_stack_m98 = v_xmm2;
    v_stack_m88 = v_xmm3;
    result = PspDecodeMitigationExecuteOptions(v_stack_m98, Arg1 + 1, (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    *(uint8_t *)(arg1 + 0x93) = (uint8_t)(result);
    goto loc_00A69A15;
loc_00A6A518:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x8)))) & (8)) != 0) goto loc_00A6A42A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x8))) | (8));
    *(uint32_t *)(v_stack_m98 + 0x8) = (uint32_t)(result);
    goto loc_00A6A42A;
loc_00A6A52E:
    result = (v_stack_m68) & (0xFFFFFFFFCFFFFFFFULL);
    v_stack_m68 = result;
    goto loc_00A69ACF;
loc_00A6A546:
    goto loc_00A69AE3;
loc_00A6A557:
loc_00A6A562:
    goto loc_00A69B0D;
loc_00A6A576:
    goto loc_00A69B36;
loc_00A6A587:
    goto loc_00A69B87;
loc_00A6A59B:
    if ((*(uint32_t *)(v_rip + 0x55C892)) != 0) goto loc_00A6A03D;
    local_rsi = (v_stack_m78) | (result);
    goto loc_00A6A45C;
loc_00A6A5C2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x750)))) & (1)) == 0) goto loc_00A69BBD;
    goto loc_00A69BBD;
loc_00A6A5E1:
    *(uint8_t *)(arg1 + 0x5F8) = 6;
    goto loc_00A6A4C0;
loc_00A6A5ED:
    *(uint8_t *)(arg1 + 0x5F8) = 8;
    goto loc_00A6A496;
loc_00A6A5F9:
    *(uint8_t *)(arg1 + 0x5F9) = 8;
    goto loc_00A6A4A3;
loc_00A6A605:
loc_00A6A615:
    Arg1 = (v_stack_m60) >> (4);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (((uint32_t)(Arg1)) != 1) goto loc_00A69C0A;
    local_rsi = (v_stack_m78) | (48);
    v_stack_m78 = local_rsi;
    goto loc_00A69C0A;
loc_00A6A636:
    result = (local_rsi) >> (48);
    result = (uint8_t)((result) & (3));
    if (((uint8_t)(result)) == 1) goto loc_00A69C26;
    local_rsi = (local_rsi) | (result);
    goto loc_00A6A4F2;
loc_00A6A65A:
loc_00A6A666:
loc_00A6A676:
    goto loc_00A69C67;
loc_00A6A686:
    result = (v_stack_m70) & (-49);
    v_stack_m70 = result;
    goto loc_00A69D0E;
loc_00A6A69C:
    goto loc_00A69D0E;
loc_00A6A6A6:
    goto loc_00A69D30;
loc_00A6A6B3:
    goto loc_00A69D30;
loc_00A6A6BF:
    goto loc_00A69D4C;
loc_00A6A6CC:
    goto loc_00A69D60;
loc_00A6A6D9:
    goto loc_00A69D82;
loc_00A6A6E6:
    goto loc_00A69DB4;
loc_00A6A6F3:
    goto loc_00A69DD6;
loc_00A6A700:
    goto loc_00A69DF7;
loc_00A6A70D:
    Arg1 = (v_stack_m70) >> (20);
    Arg1 = (uint32_t)((Arg1) & (3));
loc_00A6A72E:
loc_00A6A738:
loc_00A6A742:
    goto loc_00A69E72;
loc_00A6A752:
    goto loc_00A69E72;
loc_00A6A75F:
    Arg1 = (Arg1) & (1);
    v_stack_m70 = Arg1;
    goto loc_00A69E98;
loc_00A6A791:
    goto loc_00A6A27F;
loc_00A6A79D:
    goto loc_00A69EAC;
loc_00A6A7AD:
    if (((uint8_t)((uint32_t)(0x100000ULL))) != 3) goto loc_00A6A3D5;
loc_00A6A7B6:
    goto loc_00A6A3D5;
loc_00A6A7C6:
    goto loc_00A69EDC;
loc_00A6A7D6:
    goto loc_00A69EF9;
loc_00A6A7F1:
    goto loc_00A69EF9;
loc_00A6A801:
    goto loc_00A69F0D;
loc_00A6A811:
    result = (v_stack_m68) & (0xFFFFFFFFFFFFCFFFULL);
    v_stack_m68 = result;
loc_00A6A824:
    goto loc_00A69F27;
loc_00A6A834:
    goto loc_00A69F3B;
loc_00A6A841:
    result = PspSetRedirectionTrustPolicy(Arg1, 1, (uint32_t)(0x10000000ULL), (uint32_t)(0x400ULL));
    goto loc_00A69F72;
loc_00A6A853:
    goto loc_00A69F92;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x88` | `32` | `R/W` |
| `Arg1` | `+ 0x93` | `8` | `W` |
| `Arg1` | `+ 0x1E8` | `64` | `R` |
| `Arg1` | `+ 0x5F8` | `8` | `R` |
| `Arg1` | `+ 0x5F8` | `8` | `W` |
| `Arg1` | `+ 0x5F9` | `8` | `R` |
| `Arg1` | `+ 0x5F9` | `8` | `W` |
| `Arg1` | `+ 0x6EC` | `16` | `R` |
| `Arg1` | `+ 0x750` | `32` | `R` |
| `Arg1` | `+ 0x750` | `32` | `R/W` |
| `Arg1` | `+ 0x754` | `32` | `R` |
| `Arg1` | `+ 0x754` | `32` | `R/W` |
| `Arg1` | `+ 0x7D8` | `32` | `R` |
| `Arg1` | `+ 0x7D8` | `32` | `R/W` |
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x0` | `128` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A699AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
