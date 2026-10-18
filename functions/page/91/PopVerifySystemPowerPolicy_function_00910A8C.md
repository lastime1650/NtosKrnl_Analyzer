# PopVerifySystemPowerPolicy

- RVA: `0x00910A8C`–`0x00911145` (길이 `1,721` bytes)
- VA: `0x0000000140910A8C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008A15C`
- 디코드: `410`개 명령, `1,721/1,721` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00910BF4` → [PopVerifyPowerActionPolicy](PopVerifyPowerActionPolicy_function_0091114C.md) (function, `0x0091114C`)
- `0x00910BFD` → [PopVerifyPowerActionPolicy](PopVerifyPowerActionPolicy_function_0091114C.md) (function, `0x0091114C`)
- `0x00910C06` → [PopVerifyPowerActionPolicy](PopVerifyPowerActionPolicy_function_0091114C.md) (function, `0x0091114C`)
- `0x00910C0F` → [PopVerifyPowerActionPolicy](PopVerifyPowerActionPolicy_function_0091114C.md) (function, `0x0091114C`)
- `0x00910D1D` → [PopVerifyPowerActionPolicy](PopVerifyPowerActionPolicy_function_0091114C.md) (function, `0x0091114C`)
- `0x00910DB0` → [PopVerifyPowerActionPolicy](PopVerifyPowerActionPolicy_function_0091114C.md) (function, `0x0091114C`)
- `0x00910F5A` → [PopIsHiberbootSupported](../70/PopIsHiberbootSupported_function_00702F8C.md) (function, `0x00702F8C`)
- `0x00910F67` → [PopIsHibernateSupported](../AA/PopIsHibernateSupported_function_00AA3DFC.md) (function, `0x00AA3DFC`)
- `0x00910F9D` → [PopIsHiberbootSupported](../70/PopIsHiberbootSupported_function_00702F8C.md) (function, `0x00702F8C`)
- `0x00910FAA` → [PopIsHibernateSupported](../AA/PopIsHibernateSupported_function_00AA3DFC.md) (function, `0x00AA3DFC`)
- `0x00910FE0` → [PopIsHiberbootSupported](../70/PopIsHiberbootSupported_function_00702F8C.md) (function, `0x00702F8C`)
- `0x00910FED` → [PopIsHibernateSupported](../AA/PopIsHibernateSupported_function_00AA3DFC.md) (function, `0x00AA3DFC`)
- `0x00911023` → [PopIsHiberbootSupported](../70/PopIsHiberbootSupported_function_00702F8C.md) (function, `0x00702F8C`)
- `0x00911030` → [PopIsHibernateSupported](../AA/PopIsHibernateSupported_function_00AA3DFC.md) (function, `0x00AA3DFC`)
- `0x00911075` → [PopVerifyPowerActionPolicy](PopVerifyPowerActionPolicy_function_0091114C.md) (function, `0x0091114C`)
- `0x00911086` → [PopIsHiberbootSupported](../70/PopIsHiberbootSupported_function_00702F8C.md) (function, `0x00702F8C`)
- `0x0091109A` → [PopIsHibernateSupported](../AA/PopIsHibernateSupported_function_00AA3DFC.md) (function, `0x00AA3DFC`)
- `0x009110E4` → [PopVerifySystemPowerState](../A9/PopVerifySystemPowerState_function_00A9537C.md) (function, `0x00A9537C`)

### Direct callers
- [PopApplyPolicy](PopApplyPolicy_function_009107B0.md) at `0x009108B1`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x0095637B`

### Static image references
- `0x00910B42` → RVA `0x00F0CEC5` (`.data`; read)
- `0x00910B90` → RVA `0x00F0CD00` (`.data`; read)
- `0x00910B9E` → RVA `0x00F0CD04` (`.data`; read)
- `0x00910BB2` → RVA `0x00F0CD08` (`.data`; read)
- `0x00910BC0` → RVA `0x00F0CD0C` (`.data`; read)
- `0x00910BD4` → RVA `0x00F0CD10` (`.data`; read)
- `0x00910BE2` → RVA `0x00F0CD14` (`.data`; read)
- `0x00910C18` → RVA `0x00F0CEC0` (`.data`; read)
- `0x00910EC3` → RVA `0x00F0CEC4` (`.data`; read)
- `0x00911106` → RVA `0x00F0CEC7` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **16**
  - `0x00910ECA` → [sub_00B214D8](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x00910F7F` → [sub_00B214D8 + 0x16](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x00910F86` → [sub_00B214D8 + 0x16](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x00910F95` → [sub_00B214D8 + 0x26](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x00910FC2` → [sub_00B214D8 + 0x5A](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x00910FC9` → [sub_00B214D8 + 0x5A](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x00910FD8` → [sub_00B214D8 + 0x6A](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x00911005` → [sub_00B214D8 + 0x9E](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x0091100C` → [sub_00B214D8 + 0x9E](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x0091101B` → [sub_00B214D8 + 0xAE](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x00911048` → [sub_00B214D8 + 0xE2](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x0091104F` → [sub_00B214D8 + 0xE2](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x0091105E` → [sub_00B214D8 + 0xF2](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x009110B5` → [sub_00B214D8 + 0x126](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x009110BD` → [sub_00B214D8 + 0x126](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)
  - `0x009110CC` → [sub_00B214D8 + 0x136](../B2/Unknown_function_00B214D8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00910A8C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00910A91  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00910A96  55                              push rbp
00910A97  56                              push rsi
00910A98  57                              push rdi
00910A99  41 54                           push r12
00910A9B  41 55                           push r13
00910A9D  41 56                           push r14
00910A9F  41 57                           push r15
00910AA1  48 83 EC 20                     sub rsp, 0x20
00910AA5  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00910AA8  B8 80 00 00 00                  mov eax, 0x80
00910AAD  BD 01 00 00 00                  mov ebp, 1
00910AB2  48 8B FA                        mov rdi, rdx
00910AB5  0F 11 02                        movups xmmword ptr [rdx], xmm0
00910AB8  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00910ABC  4C 8D 04 10                     lea r8, [rax + rdx]
00910AC0  0F 11 4A 10                     movups xmmword ptr [rdx + 0x10], xmm1
00910AC4  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00910AC8  0F 11 42 20                     movups xmmword ptr [rdx + 0x20], xmm0
00910ACC  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
00910AD0  0F 11 4A 30                     movups xmmword ptr [rdx + 0x30], xmm1
00910AD4  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
00910AD8  0F 11 42 40                     movups xmmword ptr [rdx + 0x40], xmm0
00910ADC  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
00910AE0  0F 11 4A 50                     movups xmmword ptr [rdx + 0x50], xmm1
00910AE4  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
00910AE8  0F 11 42 60                     movups xmmword ptr [rdx + 0x60], xmm0
00910AEC  0F 10 41 70                     movups xmm0, xmmword ptr [rcx + 0x70]
00910AF0  48 03 C8                        add rcx, rax
00910AF3  41 0F 11 40 F0                  movups xmmword ptr [r8 - 0x10], xmm0
00910AF8  0F 10 09                        movups xmm1, xmmword ptr [rcx]
00910AFB  41 0F 11 08                     movups xmmword ptr [r8], xmm1
00910AFF  0F 10 41 10                     movups xmm0, xmmword ptr [rcx + 0x10]
00910B03  41 0F 11 40 10                  movups xmmword ptr [r8 + 0x10], xmm0
00910B08  0F 10 49 20                     movups xmm1, xmmword ptr [rcx + 0x20]
00910B0C  41 0F 11 48 20                  movups xmmword ptr [r8 + 0x20], xmm1
00910B11  0F 10 41 30                     movups xmm0, xmmword ptr [rcx + 0x30]
00910B15  41 0F 11 40 30                  movups xmmword ptr [r8 + 0x30], xmm0
00910B1A  0F 10 49 40                     movups xmm1, xmmword ptr [rcx + 0x40]
00910B1E  41 0F 11 48 40                  movups xmmword ptr [r8 + 0x40], xmm1
00910B23  0F 10 41 50                     movups xmm0, xmmword ptr [rcx + 0x50]
00910B27  41 0F 11 40 50                  movups xmmword ptr [r8 + 0x50], xmm0
00910B2C  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
00910B30  49 89 40 60                     mov qword ptr [r8 + 0x60], rax
00910B34  39 2A                           cmp dword ptr [rdx], ebp
00910B36  0F 85 7D 03 00 00               jne 0x140910eb9
00910B3C  45 33 FF                        xor r15d, r15d
00910B3F  8D 75 02                        lea esi, [rbp + 2]
00910B42  44 38 3D 7C C3 5F 00            cmp byte ptr [rip + 0x5fc37c], r15b
00910B49  44 8D 65 03                     lea r12d, [rbp + 3]
00910B4D  44 8D 6D 01                     lea r13d, [rbp + 1]
00910B51  0F 84 6C 03 00 00               je 0x140910ec3
00910B57  44 89 62 48                     mov dword ptr [rdx + 0x48], r12d
00910B5B  48 8D 5A 44                     lea rbx, [rdx + 0x44]
00910B5F  8B 03                           mov eax, dword ptr [rbx]
00910B61  41 3B C5                        cmp eax, r13d
00910B64  0F 8C 6E 03 00 00               jl 0x140910ed8
00910B6A  41 3B C4                        cmp eax, r12d
00910B6D  0F 8F 70 03 00 00               jg 0x140910ee3
00910B73  8B 4A 48                        mov ecx, dword ptr [rdx + 0x48]
00910B76  41 3B CD                        cmp ecx, r13d
00910B79  0F 8C 6F 03 00 00               jl 0x140910eee
00910B7F  41 3B CC                        cmp ecx, r12d
00910B82  0F 8F 72 03 00 00               jg 0x140910efa
00910B88  3B C8                           cmp ecx, eax
00910B8A  0F 8C 76 03 00 00               jl 0x140910f06
00910B90  8B 15 6A C1 5F 00               mov edx, dword ptr [rip + 0x5fc16a]
00910B96  3B C2                           cmp eax, edx
00910B98  0F 8C 72 03 00 00               jl 0x140910f10
00910B9E  8B 05 60 C1 5F 00               mov eax, dword ptr [rip + 0x5fc160]
00910BA4  3B C8                           cmp ecx, eax
00910BA6  0F 8F 6B 03 00 00               jg 0x140910f17
00910BAC  8B 87 C0 00 00 00               mov eax, dword ptr [rdi + 0xc0]
00910BB2  8B 0D 50 C1 5F 00               mov ecx, dword ptr [rip + 0x5fc150]
00910BB8  3B C1                           cmp eax, ecx
00910BBA  0F 82 5F 03 00 00               jb 0x140910f1f
00910BC0  8B 0D 46 C1 5F 00               mov ecx, dword ptr [rip + 0x5fc146]
00910BC6  3B C1                           cmp eax, ecx
00910BC8  0F 87 62 03 00 00               ja 0x140910f30
00910BCE  8B 87 D4 00 00 00               mov eax, dword ptr [rdi + 0xd4]
00910BD4  8B 0D 36 C1 5F 00               mov ecx, dword ptr [rip + 0x5fc136]
00910BDA  3B C1                           cmp eax, ecx
00910BDC  0F 82 59 03 00 00               jb 0x140910f3b
00910BE2  8B 0D 2C C1 5F 00               mov ecx, dword ptr [rip + 0x5fc12c]
00910BE8  3B C1                           cmp eax, ecx
00910BEA  0F 87 5C 03 00 00               ja 0x140910f4c
00910BF0  48 8D 4F 04                     lea rcx, [rdi + 4]
00910BF4  E8 53 05 00 00                  call 0x14091114c
00910BF9  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00910BFD  E8 4A 05 00 00                  call 0x14091114c
00910C02  48 8D 4F 1C                     lea rcx, [rdi + 0x1c]
00910C06  E8 41 05 00 00                  call 0x14091114c
00910C0B  48 8D 4F 30                     lea rcx, [rdi + 0x30]
00910C0F  E8 38 05 00 00                  call 0x14091114c
00910C14  4C 8D 57 28                     lea r10, [rdi + 0x28]
00910C18  4C 8D 1D A1 C2 5F 00            lea r11, [rip + 0x5fc2a1]
00910C1F  4D 85 D2                        test r10, r10
00910C22  74 33                           je 0x140910c57
00910C24  45 8B 0A                        mov r9d, dword ptr [r10]
00910C27  41 8B C9                        mov ecx, r9d
00910C2A  41 83 F9 FF                     cmp r9d, -1
00910C2E  0F 8F FE 01 00 00               jg 0x140910e32
00910C34  41 83 F9 05                     cmp r9d, 5
00910C38  0F 84 19 03 00 00               je 0x140910f57
00910C3E  41 3B CC                        cmp ecx, r12d
00910C41  0F 85 3D 03 00 00               jne 0x140910f84
00910C47  44 38 3D 77 C2 5F 00            cmp byte ptr [rip + 0x5fc277], r15b
00910C4E  0F 84 28 03 00 00               je 0x140910f7c
00910C54  45 89 0A                        mov dword ptr [r10], r9d
00910C57  48 85 DB                        test rbx, rbx
00910C5A  74 33                           je 0x140910c8f
00910C5C  44 8B 0B                        mov r9d, dword ptr [rbx]
00910C5F  41 8B C9                        mov ecx, r9d
00910C62  41 83 F9 FF                     cmp r9d, -1
00910C66  0F 8F D7 01 00 00               jg 0x140910e43
00910C6C  41 83 F9 05                     cmp r9d, 5
00910C70  0F 84 24 03 00 00               je 0x140910f9a
00910C76  41 3B CC                        cmp ecx, r12d
00910C79  0F 85 48 03 00 00               jne 0x140910fc7
00910C7F  44 38 3D 3F C2 5F 00            cmp byte ptr [rip + 0x5fc23f], r15b
00910C86  0F 84 33 03 00 00               je 0x140910fbf
00910C8C  44 89 0B                        mov dword ptr [rbx], r9d
00910C8F  4C 8D 57 48                     lea r10, [rdi + 0x48]
00910C93  4D 85 D2                        test r10, r10
00910C96  74 33                           je 0x140910ccb
00910C98  45 8B 0A                        mov r9d, dword ptr [r10]
00910C9B  41 8B C9                        mov ecx, r9d
00910C9E  41 83 F9 FF                     cmp r9d, -1
00910CA2  0F 8F AC 01 00 00               jg 0x140910e54
00910CA8  41 83 F9 05                     cmp r9d, 5
00910CAC  0F 84 2B 03 00 00               je 0x140910fdd
00910CB2  41 3B CC                        cmp ecx, r12d
00910CB5  0F 85 4F 03 00 00               jne 0x14091100a
00910CBB  44 38 3D 03 C2 5F 00            cmp byte ptr [rip + 0x5fc203], r15b
00910CC2  0F 84 3A 03 00 00               je 0x140911002
00910CC8  45 89 0A                        mov dword ptr [r10], r9d
00910CCB  4C 8D 57 4C                     lea r10, [rdi + 0x4c]
00910CCF  4D 85 D2                        test r10, r10
00910CD2  74 33                           je 0x140910d07
00910CD4  45 8B 0A                        mov r9d, dword ptr [r10]
00910CD7  41 8B C9                        mov ecx, r9d
00910CDA  41 83 F9 FF                     cmp r9d, -1
00910CDE  0F 8F 81 01 00 00               jg 0x140910e65
00910CE4  41 83 F9 05                     cmp r9d, 5
00910CE8  0F 84 32 03 00 00               je 0x140911020
00910CEE  41 3B CC                        cmp ecx, r12d
00910CF1  0F 85 56 03 00 00               jne 0x14091104d
00910CF7  44 38 3D C7 C1 5F 00            cmp byte ptr [rip + 0x5fc1c7], r15b
00910CFE  0F 84 41 03 00 00               je 0x140911045
00910D04  45 89 0A                        mov dword ptr [r10], r9d
00910D07  4C 8D 77 74                     lea r14, [rdi + 0x74]
00910D0B  41 8B EF                        mov ebp, r15d
00910D0E  48 8D 77 68                     lea rsi, [rdi + 0x68]
00910D12  BF 01 00 00 00                  mov edi, 1
00910D17  8B 1E                           mov ebx, dword ptr [rsi]
00910D19  49 8D 4E F4                     lea rcx, [r14 - 0xc]
00910D1D  E8 2A 04 00 00                  call 0x14091114c
00910D22  83 FB 03                        cmp ebx, 3
00910D25  0F 84 38 03 00 00               je 0x140911063
00910D2B  4C 8D 4E 0C                     lea r9, [rsi + 0xc]
00910D2F  4D 85 C9                        test r9, r9
00910D32  74 34                           je 0x140910d68
00910D34  45 8B 09                        mov r9d, dword ptr [r9]
00910D37  41 8B C9                        mov ecx, r9d
00910D3A  41 83 F9 FF                     cmp r9d, -1
00910D3E  0F 8F 32 01 00 00               jg 0x140910e76
00910D44  41 83 F9 05                     cmp r9d, 5
00910D48  0F 84 31 03 00 00               je 0x14091107f
00910D4E  41 3B CC                        cmp ecx, r12d
00910D51  0F 85 63 03 00 00               jne 0x1409110ba
00910D57  44 38 3D 67 C1 5F 00            cmp byte ptr [rip + 0x5fc167], r15b
00910D5E  0F 84 4B 03 00 00               je 0x1409110af
00910D64  44 89 4E 0C                     mov dword ptr [rsi + 0xc], r9d
00910D68  44 39 2E                        cmp dword ptr [rsi], r13d
00910D6B  0F 84 60 03 00 00               je 0x1409110d1
00910D71  3B EF                           cmp ebp, edi
00910D73  72 12                           jb 0x140910d87
00910D75  83 3E 06                        cmp dword ptr [rsi], 6
00910D78  8B 46 04                        mov eax, dword ptr [rsi + 4]
00910D7B  0F 84 30 01 00 00               je 0x140910eb1
00910D81  83 E0 EF                        and eax, 0xffffffef
00910D84  89 46 04                        mov dword ptr [rsi + 4], eax
00910D87  83 7E FC 64                     cmp dword ptr [rsi - 4], 0x64
00910D8B  0F 87 5D 03 00 00               ja 0x1409110ee
00910D91  03 EF                           add ebp, edi
00910D93  49 83 C6 18                     add r14, 0x18
00910D97  48 83 C6 18                     add rsi, 0x18
00910D9B  41 3B EC                        cmp ebp, r12d
00910D9E  0F 82 73 FF FF FF               jb 0x140910d17
00910DA4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00910DA9  48 8D 8F DC 00 00 00            lea rcx, [rdi + 0xdc]
00910DB0  E8 97 03 00 00                  call 0x14091114c
00910DB5  44 39 7F 5C                     cmp dword ptr [rdi + 0x5c], r15d
00910DB9  0F 84 3B 03 00 00               je 0x1409110fa
00910DBF  48 8D 4F 58                     lea rcx, [rdi + 0x58]
00910DC3  8B 01                           mov eax, dword ptr [rcx]
00910DC5  48 8B D1                        mov rdx, rcx
00910DC8  85 C0                           test eax, eax
00910DCA  0F 85 36 03 00 00               jne 0x140911106
00910DD0  44 8B 47 3C                     mov r8d, dword ptr [rdi + 0x3c]
00910DD4  41 BA 3C 00 00 00               mov r10d, 0x3c
00910DDA  45 8B C8                        mov r9d, r8d
00910DDD  45 85 C0                        test r8d, r8d
00910DE0  0F 85 A2 00 00 00               jne 0x140910e88
00910DE6  FF C8                           dec eax
00910DE8  83 F8 3A                        cmp eax, 0x3a
00910DEB  0F 86 31 03 00 00               jbe 0x140911122
00910DF1  8A 47 40                        mov al, byte ptr [rdi + 0x40]
00910DF4  3C 5A                           cmp al, 0x5a
00910DF6  0F 87 2E 03 00 00               ja 0x14091112a
00910DFC  45 85 C9                        test r9d, r9d
00910DFF  0F 85 9B 00 00 00               jne 0x140910ea0
00910E05  8B 47 44                        mov eax, dword ptr [rdi + 0x44]
00910E08  39 47 48                        cmp dword ptr [rdi + 0x48], eax
00910E0B  0F 8C 24 03 00 00               jl 0x140911135
00910E11  39 47 4C                        cmp dword ptr [rdi + 0x4c], eax
00910E14  0F 8F 23 03 00 00               jg 0x14091113d
00910E1A  33 C0                           xor eax, eax
00910E1C  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00910E21  48 83 C4 20                     add rsp, 0x20
00910E25  41 5F                           pop r15
00910E27  41 5E                           pop r14
00910E29  41 5D                           pop r13
00910E2B  41 5C                           pop r12
00910E2D  5F                              pop rdi
00910E2E  5E                              pop rsi
00910E2F  5D                              pop rbp
00910E30  C3                              ret
00910E31  CC                              int3
00910E32  41 8D 41 FE                     lea eax, [r9 - 2]
00910E36  3B C6                           cmp eax, esi
00910E38  0F 86 F6 FD FF FF               jbe 0x140910c34
00910E3E  E9 14 FE FF FF                  jmp 0x140910c57
00910E43  41 8D 41 FE                     lea eax, [r9 - 2]
00910E47  3B C6                           cmp eax, esi
00910E49  0F 86 1D FE FF FF               jbe 0x140910c6c
00910E4F  E9 3B FE FF FF                  jmp 0x140910c8f
00910E54  41 8D 41 FE                     lea eax, [r9 - 2]
00910E58  3B C6                           cmp eax, esi
00910E5A  0F 86 48 FE FF FF               jbe 0x140910ca8
00910E60  E9 66 FE FF FF                  jmp 0x140910ccb
00910E65  41 8D 41 FE                     lea eax, [r9 - 2]
00910E69  3B C6                           cmp eax, esi
00910E6B  0F 86 73 FE FF FF               jbe 0x140910ce4
00910E71  E9 91 FE FF FF                  jmp 0x140910d07
00910E76  41 8D 41 FE                     lea eax, [r9 - 2]
00910E7A  83 F8 03                        cmp eax, 3
00910E7D  0F 86 C1 FE FF FF               jbe 0x140910d44
00910E83  E9 E0 FE FF FF                  jmp 0x140910d68
00910E88  48 8B CA                        mov rcx, rdx
00910E8B  45 3B C2                        cmp r8d, r10d
00910E8E  0F 83 52 FF FF FF               jae 0x140910de6
00910E94  44 89 57 3C                     mov dword ptr [rdi + 0x3c], r10d
00910E98  45 8B CA                        mov r9d, r10d
00910E9B  E9 46 FF FF FF                  jmp 0x140910de6
00910EA0  84 C0                           test al, al
00910EA2  0F 85 5D FF FF FF               jne 0x140910e05
00910EA8  C6 47 40 5A                     mov byte ptr [rdi + 0x40], 0x5a
00910EAC  E9 54 FF FF FF                  jmp 0x140910e05
00910EB1  83 C8 10                        or eax, 0x10
00910EB4  E9 CB FE FF FF                  jmp 0x140910d84
00910EB9  B8 0D 00 00 C0                  mov eax, 0xc000000d
00910EBE  E9 59 FF FF FF                  jmp 0x140910e1c
00910EC3  44 38 3D FA BF 5F 00            cmp byte ptr [rip + 0x5fbffa], r15b
00910ECA  0F 84 08 06 21 00               je 0x140b214d8
00910ED0  89 72 48                        mov dword ptr [rdx + 0x48], esi
00910ED3  E9 83 FC FF FF                  jmp 0x140910b5b
00910ED8  44 89 2B                        mov dword ptr [rbx], r13d
00910EDB  41 8B C5                        mov eax, r13d
00910EDE  E9 90 FC FF FF                  jmp 0x140910b73
00910EE3  44 89 23                        mov dword ptr [rbx], r12d
00910EE6  41 8B C4                        mov eax, r12d
00910EE9  E9 85 FC FF FF                  jmp 0x140910b73
00910EEE  44 89 6A 48                     mov dword ptr [rdx + 0x48], r13d
00910EF2  41 8B CD                        mov ecx, r13d
00910EF5  E9 8E FC FF FF                  jmp 0x140910b88
00910EFA  44 89 62 48                     mov dword ptr [rdx + 0x48], r12d
00910EFE  41 8B CC                        mov ecx, r12d
00910F01  E9 82 FC FF FF                  jmp 0x140910b88
00910F06  89 42 48                        mov dword ptr [rdx + 0x48], eax
00910F09  8B C8                           mov ecx, eax
00910F0B  E9 80 FC FF FF                  jmp 0x140910b90
00910F10  89 13                           mov dword ptr [rbx], edx
00910F12  E9 87 FC FF FF                  jmp 0x140910b9e
00910F17  89 47 48                        mov dword ptr [rdi + 0x48], eax
00910F1A  E9 8D FC FF FF                  jmp 0x140910bac
00910F1F  89 8F C0 00 00 00               mov dword ptr [rdi + 0xc0], ecx
00910F25  8B 05 DD BD 5F 00               mov eax, dword ptr [rip + 0x5fbddd]
00910F2B  E9 90 FC FF FF                  jmp 0x140910bc0
00910F30  89 8F C0 00 00 00               mov dword ptr [rdi + 0xc0], ecx
00910F36  E9 93 FC FF FF                  jmp 0x140910bce
00910F3B  89 8F D4 00 00 00               mov dword ptr [rdi + 0xd4], ecx
00910F41  8B 05 C9 BD 5F 00               mov eax, dword ptr [rip + 0x5fbdc9]
00910F47  E9 96 FC FF FF                  jmp 0x140910be2
00910F4C  89 8F D4 00 00 00               mov dword ptr [rdi + 0xd4], ecx
00910F52  E9 99 FC FF FF                  jmp 0x140910bf0
00910F57  49 8B CB                        mov rcx, r11
00910F5A  E8 2D 20 DF FF                  call 0x140702f8c
00910F5F  84 C0                           test al, al
00910F61  0F 85 ED FC FF FF               jne 0x140910c54
00910F67  E8 90 2E 19 00                  call 0x140aa3dfc
00910F6C  84 C0                           test al, al
00910F6E  0F 85 E0 FC FF FF               jne 0x140910c54
00910F74  45 8B CC                        mov r9d, r12d
00910F77  E9 CB FC FF FF                  jmp 0x140910c47
00910F7C  44 8B CE                        mov r9d, esi
00910F7F  E9 6A 05 21 00                  jmp 0x140b214ee
00910F84  3B CE                           cmp ecx, esi
00910F86  0F 84 62 05 21 00               je 0x140b214ee
00910F8C  41 3B CD                        cmp ecx, r13d
00910F8F  0F 85 BF FC FF FF               jne 0x140910c54
00910F95  E9 64 05 21 00                  jmp 0x140b214fe
00910F9A  49 8B CB                        mov rcx, r11
00910F9D  E8 EA 1F DF FF                  call 0x140702f8c
00910FA2  84 C0                           test al, al
00910FA4  0F 85 E2 FC FF FF               jne 0x140910c8c
00910FAA  E8 4D 2E 19 00                  call 0x140aa3dfc
00910FAF  84 C0                           test al, al
00910FB1  0F 85 D5 FC FF FF               jne 0x140910c8c
00910FB7  45 8B CC                        mov r9d, r12d
00910FBA  E9 C0 FC FF FF                  jmp 0x140910c7f
00910FBF  44 8B CE                        mov r9d, esi
00910FC2  E9 6B 05 21 00                  jmp 0x140b21532
00910FC7  3B CE                           cmp ecx, esi
00910FC9  0F 84 63 05 21 00               je 0x140b21532
00910FCF  41 3B CD                        cmp ecx, r13d
00910FD2  0F 85 B4 FC FF FF               jne 0x140910c8c
00910FD8  E9 65 05 21 00                  jmp 0x140b21542
00910FDD  49 8B CB                        mov rcx, r11
00910FE0  E8 A7 1F DF FF                  call 0x140702f8c
00910FE5  84 C0                           test al, al
00910FE7  0F 85 DB FC FF FF               jne 0x140910cc8
00910FED  E8 0A 2E 19 00                  call 0x140aa3dfc
00910FF2  84 C0                           test al, al
00910FF4  0F 85 CE FC FF FF               jne 0x140910cc8
00910FFA  45 8B CC                        mov r9d, r12d
00910FFD  E9 B9 FC FF FF                  jmp 0x140910cbb
00911002  44 8B CE                        mov r9d, esi
00911005  E9 6C 05 21 00                  jmp 0x140b21576
0091100A  3B CE                           cmp ecx, esi
0091100C  0F 84 64 05 21 00               je 0x140b21576
00911012  41 3B CD                        cmp ecx, r13d
00911015  0F 85 AD FC FF FF               jne 0x140910cc8
0091101B  E9 66 05 21 00                  jmp 0x140b21586
00911020  49 8B CB                        mov rcx, r11
00911023  E8 64 1F DF FF                  call 0x140702f8c
00911028  84 C0                           test al, al
0091102A  0F 85 D4 FC FF FF               jne 0x140910d04
00911030  E8 C7 2D 19 00                  call 0x140aa3dfc
00911035  84 C0                           test al, al
00911037  0F 85 C7 FC FF FF               jne 0x140910d04
0091103D  45 8B CC                        mov r9d, r12d
00911040  E9 B2 FC FF FF                  jmp 0x140910cf7
00911045  44 8B CE                        mov r9d, esi
00911048  E9 6D 05 21 00                  jmp 0x140b215ba
0091104D  3B CE                           cmp ecx, esi
0091104F  0F 84 65 05 21 00               je 0x140b215ba
00911055  41 3B CD                        cmp ecx, r13d
00911058  0F 85 A6 FC FF FF               jne 0x140910d04
0091105E  E9 67 05 21 00                  jmp 0x140b215ca
00911063  83 3E 03                        cmp dword ptr [rsi], 3
00911066  0F 8D BF FC FF FF               jge 0x140910d2b
0091106C  48 8B CE                        mov rcx, rsi
0091106F  C7 06 06 00 00 00               mov dword ptr [rsi], 6
00911075  E8 D2 00 00 00                  call 0x14091114c
0091107A  E9 AC FC FF FF                  jmp 0x140910d2b
0091107F  48 8D 0D 3A BE 5F 00            lea rcx, [rip + 0x5fbe3a]
00911086  E8 01 1F DF FF                  call 0x140702f8c
0091108B  84 C0                           test al, al
0091108D  0F 85 D1 FC FF FF               jne 0x140910d64
00911093  48 8D 0D 26 BE 5F 00            lea rcx, [rip + 0x5fbe26]
0091109A  E8 5D 2D 19 00                  call 0x140aa3dfc
0091109F  84 C0                           test al, al
009110A1  0F 85 BD FC FF FF               jne 0x140910d64
009110A7  45 8B CC                        mov r9d, r12d
009110AA  E9 A8 FC FF FF                  jmp 0x140910d57
009110AF  41 B9 03 00 00 00               mov r9d, 3
009110B5  E9 44 05 21 00                  jmp 0x140b215fe
009110BA  83 F9 03                        cmp ecx, 3
009110BD  0F 84 3B 05 21 00               je 0x140b215fe
009110C3  41 3B CD                        cmp ecx, r13d
009110C6  0F 85 98 FC FF FF               jne 0x140910d64
009110CC  E9 3D 05 21 00                  jmp 0x140b2160e
009110D1  44 39 66 0C                     cmp dword ptr [rsi + 0xc], r12d
009110D5  0F 8E 96 FC FF FF               jle 0x140910d71
009110DB  8B D7                           mov edx, edi
009110DD  44 89 66 0C                     mov dword ptr [rsi + 0xc], r12d
009110E1  49 8B CE                        mov rcx, r14
009110E4  E8 93 42 18 00                  call 0x140a9537c
009110E9  E9 83 FC FF FF                  jmp 0x140910d71
009110EE  C7 46 FC 64 00 00 00            mov dword ptr [rsi - 4], 0x64
009110F5  E9 97 FC FF FF                  jmp 0x140910d91
009110FA  C7 47 5C 01 00 00 00            mov dword ptr [rdi + 0x5c], 1
00911101  E9 B9 FC FF FF                  jmp 0x140910dbf
00911106  44 38 3D BA BD 5F 00            cmp byte ptr [rip + 0x5fbdba], r15b
0091110D  0F 85 BD FC FF FF               jne 0x140910dd0
00911113  44 89 39                        mov dword ptr [rcx], r15d
00911116  48 8D 57 58                     lea rdx, [rdi + 0x58]
0091111A  41 8B C7                        mov eax, r15d
0091111D  E9 AE FC FF FF                  jmp 0x140910dd0
00911122  44 89 11                        mov dword ptr [rcx], r10d
00911125  E9 C7 FC FF FF                  jmp 0x140910df1
0091112A  C6 47 40 5A                     mov byte ptr [rdi + 0x40], 0x5a
0091112E  B0 5A                           mov al, 0x5a
00911130  E9 C7 FC FF FF                  jmp 0x140910dfc
00911135  89 47 48                        mov dword ptr [rdi + 0x48], eax
00911138  E9 D4 FC FF FF                  jmp 0x140910e11
0091113D  89 47 4C                        mov dword ptr [rdi + 0x4c], eax
00911140  E9 D5 FC FF FF                  jmp 0x140910e1a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopVerifySystemPowerPolicy(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (32);
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int64 *)(a2 + 16) = v_xmm1;
    *(unsigned __int64 *)(a2 + 32) = v_xmm0;
    *(unsigned __int64 *)(a2 + 48) = v_xmm1;
    *(unsigned __int64 *)(a2 + 64) = v_xmm0;
    *(unsigned __int64 *)(a2 + 80) = v_xmm1;
    *(unsigned __int64 *)(a2 + 96) = v_xmm0;
    a1 = (a1) + (128);
    *(unsigned __int64 *)(128 + a2 * 1 - 16) = v_xmm0;
    *(unsigned __int64 *)(128 + a2 * 1) = v_xmm1;
    *(unsigned __int64 *)(128 + a2 * 1 + 16) = v_xmm0;
    *(unsigned __int64 *)(128 + a2 * 1 + 32) = v_xmm1;
    *(unsigned __int64 *)(128 + a2 * 1 + 48) = v_xmm0;
    *(unsigned __int64 *)(128 + a2 * 1 + 64) = v_xmm1;
    *(unsigned __int64 *)(128 + a2 * 1 + 80) = v_xmm0;
    *(unsigned __int64 *)(128 + a2 * 1 + 96) = *(unsigned __int64 *)(a1 + 96);
    if ((*(unsigned int *)(a2)) != 1) goto loc_00910EB9;
    v_r15 = 0;
    if ((*(unsigned __int8 *)(v_rip + 6275964)) == 0) goto loc_00910EC3;
    *(unsigned int *)(a2 + 72) = (unsigned int)(1 + 3);
loc_00910B5B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)))) < ((unsigned int)(1 + 1))) goto loc_00910ED8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)))) > ((unsigned int)(1 + 3))) goto loc_00910EE3;
loc_00910B73:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) < ((unsigned int)(1 + 1))) goto loc_00910EEE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) > ((unsigned int)(1 + 3))) goto loc_00910EFA;
loc_00910B88:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68))))) goto loc_00910F06;
loc_00910B90:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6275434))))) goto loc_00910F10;
loc_00910B9E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6275424))))) goto loc_00910F17;
loc_00910BAC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 192)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6275408))))) goto loc_00910F1F;
loc_00910BC0:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 192)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6275398))))) goto loc_00910F30;
loc_00910BCE:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 212)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6275382))))) goto loc_00910F3B;
loc_00910BE2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 212)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6275372))))) goto loc_00910F4C;
loc_00910BF0:
    result = PopVerifyPowerActionPolicy(a2 + 4, (unsigned int)(*(unsigned int *)(v_rip + 6275434)), 128 + a2 * 1, a4);
    result = PopVerifyPowerActionPolicy(a2 + 16, (unsigned int)(*(unsigned int *)(v_rip + 6275434)), 128 + a2 * 1, a4);
    result = PopVerifyPowerActionPolicy(a2 + 28, (unsigned int)(*(unsigned int *)(v_rip + 6275434)), 128 + a2 * 1, a4);
    result = PopVerifyPowerActionPolicy(a2 + 48, (unsigned int)(*(unsigned int *)(v_rip + 6275434)), 128 + a2 * 1, a4);
    if (a2 + 40 == 0) goto loc_00910C57;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)))) > -1) goto loc_00910E32;
loc_00910C34:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)))) == 5) goto loc_00910F57;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)))))) != ((unsigned int)(1 + 3))) goto loc_00910F84;
loc_00910C47:
    if ((*(unsigned __int8 *)(v_rip + 6275703)) == 0) goto loc_00910F7C;
loc_00910C54:
    *(unsigned int *)(a2 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)));
loc_00910C57:
    if (a2 + 68 == 0) goto loc_00910C8F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)))) > -1) goto loc_00910E43;
loc_00910C6C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)))) == 5) goto loc_00910F9A;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)))))) != ((unsigned int)(1 + 3))) goto loc_00910FC7;
loc_00910C7F:
    if ((*(unsigned __int8 *)(v_rip + 6275647)) == 0) goto loc_00910FBF;
loc_00910C8C:
    *(unsigned int *)(a2 + 68) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)));
loc_00910C8F:
    if (a2 + 72 == 0) goto loc_00910CCB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) > -1) goto loc_00910E54;
loc_00910CA8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))) == 5) goto loc_00910FDD;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)))))) != ((unsigned int)(1 + 3))) goto loc_0091100A;
loc_00910CBB:
    if ((*(unsigned __int8 *)(v_rip + 6275587)) == 0) goto loc_00911002;
loc_00910CC8:
    *(unsigned int *)(a2 + 72) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 72)));
loc_00910CCB:
    if (a2 + 76 == 0) goto loc_00910D07;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 76)))) > -1) goto loc_00910E65;
loc_00910CE4:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 76)))) == 5) goto loc_00911020;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 76)))))) != ((unsigned int)(1 + 3))) goto loc_0091104D;
loc_00910CF7:
    if ((*(unsigned __int8 *)(v_rip + 6275527)) == 0) goto loc_00911045;
loc_00910D04:
    *(unsigned int *)(a2 + 76) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 76)));
loc_00910D07:
loc_00910D17:
    result = PopVerifyPowerActionPolicy(a2 + 116 - 12, (unsigned int)(*(unsigned int *)(v_rip + 6275434)), 128 + a2 * 1, (unsigned int)(*(unsigned int *)(a2 + 76)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 104)))) == 3) goto loc_00911063;
loc_00910D2B:
    if (a2 + 104 + 12 == 0) goto loc_00910D68;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 104 + 12)))) > -1) goto loc_00910E76;
loc_00910D44:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 104 + 12)))) == 5) goto loc_0091107F;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 104 + 12)))))) != ((unsigned int)(1 + 3))) goto loc_009110BA;
loc_00910D57:
    if ((*(unsigned __int8 *)(v_rip + 6275431)) == 0) goto loc_009110AF;
loc_00910D64:
    *(unsigned int *)(a2 + 104 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 104 + 12)));
loc_00910D68:
    if ((*(unsigned int *)(a2 + 104)) == ((unsigned int)(1 + 1))) goto loc_009110D1;
loc_00910D71:
    if (0 < 1) goto loc_00910D87;
    if ((*(unsigned int *)(a2 + 104)) == 6) goto loc_00910EB1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 104 + 4))) & (0xFFFFFFEFULL));
loc_00910D84:
    *(unsigned int *)(a2 + 104 + 4) = (unsigned int)(result);
loc_00910D87:
    if ((*(unsigned int *)(a2 + 104 - 4)) > 100) goto loc_009110EE;
loc_00910D91:
    v_rbp = (unsigned int)((0) + (1));
    v_r14 = (a2 + 116) + (24);
    v_rsi = (a2 + 104) + (24);
    if (((unsigned int)(v_rbp)) < ((unsigned int)(1 + 3))) goto loc_00910D17;
    result = PopVerifyPowerActionPolicy(v_stack_p10 + 220, (unsigned int)(*(unsigned int *)(v_rip + 6275434)), 128 + a2 * 1, (unsigned int)(*(unsigned int *)(a2 + 104 + 12)));
    if ((*(unsigned int *)(v_stack_p10 + 92)) == 0) goto loc_009110FA;
loc_00910DBF:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 88))) != 0) goto loc_00911106;
loc_00910DD0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60))) != 0) goto loc_00910E88;
loc_00910DE6:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 88))) - 1);
    if (((unsigned int)(result)) <= 58) goto loc_00911122;
loc_00910DF1:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 64))) > 90) goto loc_0091112A;
loc_00910DFC:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60))))) != 0) goto loc_00910EA0;
loc_00910E05:
    if ((*(unsigned int *)(v_stack_p10 + 72)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 68))))) goto loc_00911135;
loc_00910E11:
    if ((*(unsigned int *)(v_stack_p10 + 76)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 68))))) goto loc_0091113D;
loc_00910E1A:
    result = 0;
loc_00910E1C:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00910E32:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60)))) - 2)) <= ((unsigned int)(v_rsi))) goto loc_00910C34;
    goto loc_00910C57;
loc_00910E43:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60)))) - 2)) <= ((unsigned int)(v_rsi))) goto loc_00910C6C;
    goto loc_00910C8F;
loc_00910E54:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60)))) - 2)) <= ((unsigned int)(v_rsi))) goto loc_00910CA8;
    goto loc_00910CCB;
loc_00910E65:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60)))) - 2)) <= ((unsigned int)(v_rsi))) goto loc_00910CE4;
    goto loc_00910D07;
loc_00910E76:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60)))) - 2)) <= 3) goto loc_00910D44;
    goto loc_00910D68;
loc_00910E88:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60)))) >= 60) goto loc_00910DE6;
    *(unsigned int *)(v_stack_p10 + 60) = 60;
    goto loc_00910DE6;
loc_00910EA0:
    if ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60)))) - 2) != 0) goto loc_00910E05;
    *(unsigned __int8 *)(v_stack_p10 + 64) = 90;
    goto loc_00910E05;
loc_00910EB1:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 60)))) - 2) | (16));
    goto loc_00910D84;
loc_00910EB9:
    goto loc_00910E1C;
loc_00910EC3:
    *(unsigned int *)(v_stack_p10 + 88 + 72) = (unsigned int)(v_rsi);
    goto loc_00910B5B;
loc_00910ED8:
    *(unsigned int *)(v_stack_p18) = (unsigned int)(1 + 1);
    goto loc_00910B73;
loc_00910EE3:
    *(unsigned int *)(v_stack_p18) = (unsigned int)(1 + 3);
    goto loc_00910B73;
loc_00910EEE:
    *(unsigned int *)(v_stack_p10 + 88 + 72) = (unsigned int)(1 + 1);
    goto loc_00910B88;
loc_00910EFA:
    *(unsigned int *)(v_stack_p10 + 88 + 72) = (unsigned int)(1 + 3);
    goto loc_00910B88;
loc_00910F06:
    *(unsigned int *)(v_stack_p10 + 88 + 72) = (unsigned int)((unsigned int)((unsigned int)(1 + 3)));
    goto loc_00910B90;
loc_00910F10:
    *(unsigned int *)(v_stack_p18) = (unsigned int)(v_stack_p10 + 88);
    goto loc_00910B9E;
loc_00910F17:
    *(unsigned int *)(v_stack_p10 + 72) = (unsigned int)((unsigned int)((unsigned int)(1 + 3)));
    goto loc_00910BAC;
loc_00910F1F:
    *(unsigned int *)(v_stack_p10 + 192) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(1 + 3)))));
    goto loc_00910BC0;
loc_00910F30:
    *(unsigned int *)(v_stack_p10 + 192) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(1 + 3)))));
    goto loc_00910BCE;
loc_00910F3B:
    *(unsigned int *)(v_stack_p10 + 212) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(1 + 3)))));
    goto loc_00910BE2;
loc_00910F4C:
    *(unsigned int *)(v_stack_p10 + 212) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(1 + 3)))));
    goto loc_00910BF0;
loc_00910F57:
    result = PopIsHiberbootSupported(v_rip + 6275745, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), 60);
    if ((unsigned __int8)(result) != 0) goto loc_00910C54;
    result = PopIsHibernateSupported(v_rip + 6275745, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), 60);
    if ((unsigned __int8)(result) != 0) goto loc_00910C54;
    goto loc_00910C47;
loc_00910F7C:
loc_00910F84:
    if (((unsigned int)(v_rip + 6275745)) != ((unsigned int)(1 + 1))) goto loc_00910C54;
loc_00910F9A:
    result = PopIsHiberbootSupported(v_rip + 6275745, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_00910C8C;
    result = PopIsHibernateSupported(v_rip + 6275745, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_00910C8C;
    goto loc_00910C7F;
loc_00910FBF:
loc_00910FC7:
    if (((unsigned int)(v_rip + 6275745)) != ((unsigned int)(1 + 1))) goto loc_00910C8C;
loc_00910FDD:
    result = PopIsHiberbootSupported(v_rip + 6275745, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_00910CC8;
    result = PopIsHibernateSupported(v_rip + 6275745, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_00910CC8;
    goto loc_00910CBB;
loc_00911002:
loc_0091100A:
    if (((unsigned int)(v_rip + 6275745)) != ((unsigned int)(1 + 1))) goto loc_00910CC8;
loc_00911020:
    result = PopIsHiberbootSupported(v_rip + 6275745, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_00910D04;
    result = PopIsHibernateSupported(v_rip + 6275745, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_00910D04;
    goto loc_00910CF7;
loc_00911045:
loc_0091104D:
    if (((unsigned int)(v_rip + 6275745)) != ((unsigned int)(1 + 1))) goto loc_00910D04;
loc_00911063:
    if ((*(unsigned int *)(v_rsi)) >= 3) goto loc_00910D2B;
    *(unsigned int *)(v_rsi) = 6;
    result = PopVerifyPowerActionPolicy(v_rsi, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    goto loc_00910D2B;
loc_0091107F:
    result = PopIsHiberbootSupported(v_rip + 6274618, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_00910D64;
    result = PopIsHibernateSupported(v_rip + 6274598, v_stack_p10 + 88, (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), (unsigned int)((unsigned int)(v_rsi)));
    if ((unsigned __int8)(result) != 0) goto loc_00910D64;
    goto loc_00910D57;
loc_009110AF:
loc_009110BA:
    if (((unsigned int)(v_rip + 6274598)) != ((unsigned int)(1 + 1))) goto loc_00910D64;
loc_009110D1:
    if ((*(unsigned int *)(v_rsi + 12)) <= ((unsigned int)(1 + 3))) goto loc_00910D71;
    *(unsigned int *)(v_rsi + 12) = (unsigned int)(1 + 3);
    result = PopVerifySystemPowerState(v_r14, (unsigned int)((unsigned int)(v_stack_p10)), (unsigned int)(*(unsigned int *)(v_stack_p10 + 60)), 3);
    goto loc_00910D71;
loc_009110EE:
    *(unsigned int *)(v_rsi - 4) = 100;
    goto loc_00910D91;
loc_009110FA:
    *(unsigned int *)(v_stack_p10 + 92) = 1;
    goto loc_00910DBF;
loc_00911106:
    if ((*(unsigned __int8 *)(v_rip + 6274490)) != 0) goto loc_00910DD0;
    *(unsigned int *)(v_r14) = 0;
    goto loc_00910DD0;
loc_00911122:
    *(unsigned int *)(v_r14) = 60;
    goto loc_00910DF1;
loc_0091112A:
    *(unsigned __int8 *)(v_stack_p10 + 64) = 90;
    goto loc_00910DFC;
loc_00911135:
    *(unsigned int *)(v_stack_p10 + 72) = 90;
    goto loc_00910E11;
loc_0091113D:
    *(unsigned int *)(v_stack_p10 + 76) = 90;
    goto loc_00910E1A;
}
```

## 5. (Beta) C Style

```c
int64_t PopVerifySystemPowerPolicy(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (32);
    *(uint64_t *)(arg2) = v_xmm0;
    *(uint64_t *)(arg2 + 0x10) = v_xmm1;
    *(uint64_t *)(arg2 + 0x20) = v_xmm0;
    *(uint64_t *)(arg2 + 0x30) = v_xmm1;
    *(uint64_t *)(arg2 + 0x40) = v_xmm0;
    *(uint64_t *)(arg2 + 0x50) = v_xmm1;
    *(uint64_t *)(arg2 + 0x60) = v_xmm0;
    Arg1 = (Arg1) + (128);
    *(uint64_t *)(128 + arg2 * 1 - 0x10) = v_xmm0;
    *(uint64_t *)(128 + arg2 * 1) = v_xmm1;
    *(uint64_t *)(128 + arg2 * 1 + 0x10) = v_xmm0;
    *(uint64_t *)(128 + arg2 * 1 + 0x20) = v_xmm1;
    *(uint64_t *)(128 + arg2 * 1 + 0x30) = v_xmm0;
    *(uint64_t *)(128 + arg2 * 1 + 0x40) = v_xmm1;
    *(uint64_t *)(128 + arg2 * 1 + 0x50) = v_xmm0;
    *(uint64_t *)(128 + arg2 * 1 + 0x60) = *(uint64_t *)(arg1 + 0x60);
    if ((*(uint32_t *)(arg2)) != 1) goto loc_00910EB9;
    local_r15 = 0;
    if ((*(uint8_t *)(v_rip + 0x5FC37C)) == 0) goto loc_00910EC3;
    *(uint32_t *)(arg2 + 0x48) = (uint32_t)(1 + 3);
loc_00910B5B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)))) < ((uint32_t)(1 + 1))) goto loc_00910ED8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)))) > ((uint32_t)(1 + 3))) goto loc_00910EE3;
loc_00910B73:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) < ((uint32_t)(1 + 1))) goto loc_00910EEE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) > ((uint32_t)(1 + 3))) goto loc_00910EFA;
loc_00910B88:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44))))) goto loc_00910F06;
loc_00910B90:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5FC16A))))) goto loc_00910F10;
loc_00910B9E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5FC160))))) goto loc_00910F17;
loc_00910BAC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC0)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5FC150))))) goto loc_00910F1F;
loc_00910BC0:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC0)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5FC146))))) goto loc_00910F30;
loc_00910BCE:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xD4)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5FC136))))) goto loc_00910F3B;
loc_00910BE2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xD4)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5FC12C))))) goto loc_00910F4C;
loc_00910BF0:
    result = PopVerifyPowerActionPolicy(Arg2 + 4, (uint32_t)(*(uint32_t *)(v_rip + 0x5FC16A)), 128 + Arg2 * 1, a4);
    result = PopVerifyPowerActionPolicy(Arg2 + 16, (uint32_t)(*(uint32_t *)(v_rip + 0x5FC16A)), 128 + Arg2 * 1, a4);
    result = PopVerifyPowerActionPolicy(Arg2 + 28, (uint32_t)(*(uint32_t *)(v_rip + 0x5FC16A)), 128 + Arg2 * 1, a4);
    result = PopVerifyPowerActionPolicy(Arg2 + 48, (uint32_t)(*(uint32_t *)(v_rip + 0x5FC16A)), 128 + Arg2 * 1, a4);
    if (Arg2 + 40 == 0) goto loc_00910C57;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)))) > -1) goto loc_00910E32;
loc_00910C34:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)))) == 5) goto loc_00910F57;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)))))) != ((uint32_t)(1 + 3))) goto loc_00910F84;
loc_00910C47:
    if ((*(uint8_t *)(v_rip + 0x5FC277)) == 0) goto loc_00910F7C;
loc_00910C54:
    *(uint32_t *)(arg2 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)));
loc_00910C57:
    if (Arg2 + 68 == 0) goto loc_00910C8F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)))) > -1) goto loc_00910E43;
loc_00910C6C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)))) == 5) goto loc_00910F9A;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)))))) != ((uint32_t)(1 + 3))) goto loc_00910FC7;
loc_00910C7F:
    if ((*(uint8_t *)(v_rip + 0x5FC23F)) == 0) goto loc_00910FBF;
loc_00910C8C:
    *(uint32_t *)(arg2 + 0x44) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)));
loc_00910C8F:
    if (Arg2 + 72 == 0) goto loc_00910CCB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) > -1) goto loc_00910E54;
loc_00910CA8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) == 5) goto loc_00910FDD;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))))) != ((uint32_t)(1 + 3))) goto loc_0091100A;
loc_00910CBB:
    if ((*(uint8_t *)(v_rip + 0x5FC203)) == 0) goto loc_00911002;
loc_00910CC8:
    *(uint32_t *)(arg2 + 0x48) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)));
loc_00910CCB:
    if (Arg2 + 76 == 0) goto loc_00910D07;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4C)))) > -1) goto loc_00910E65;
loc_00910CE4:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4C)))) == 5) goto loc_00911020;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4C)))))) != ((uint32_t)(1 + 3))) goto loc_0091104D;
loc_00910CF7:
    if ((*(uint8_t *)(v_rip + 0x5FC1C7)) == 0) goto loc_00911045;
loc_00910D04:
    *(uint32_t *)(arg2 + 0x4C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4C)));
loc_00910D07:
loc_00910D17:
    result = PopVerifyPowerActionPolicy(Arg2 + 116 - 12, (uint32_t)(*(uint32_t *)(v_rip + 0x5FC16A)), 128 + Arg2 * 1, (uint32_t)(*(uint32_t *)(arg2 + 0x4C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x68)))) == 3) goto loc_00911063;
loc_00910D2B:
    if (Arg2 + 104 + 12 == 0) goto loc_00910D68;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x68 + 0xC)))) > -1) goto loc_00910E76;
loc_00910D44:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x68 + 0xC)))) == 5) goto loc_0091107F;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x68 + 0xC)))))) != ((uint32_t)(1 + 3))) goto loc_009110BA;
loc_00910D57:
    if ((*(uint8_t *)(v_rip + 0x5FC167)) == 0) goto loc_009110AF;
loc_00910D64:
    *(uint32_t *)(arg2 + 0x68 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x68 + 0xC)));
loc_00910D68:
    if ((*(uint32_t *)(arg2 + 0x68)) == ((uint32_t)(1 + 1))) goto loc_009110D1;
loc_00910D71:
    if (0 < 1) goto loc_00910D87;
    if ((*(uint32_t *)(arg2 + 0x68)) == 6) goto loc_00910EB1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x68 + 0x4))) & (0xFFFFFFEFULL));
loc_00910D84:
    *(uint32_t *)(arg2 + 0x68 + 0x4) = (uint32_t)(result);
loc_00910D87:
    if ((*(uint32_t *)(arg2 + 0x68 - 0x4)) > 100) goto loc_009110EE;
loc_00910D91:
    local_rbp = (uint32_t)((0) + (1));
    local_r14 = (Arg2 + 116) + (24);
    local_rsi = (Arg2 + 104) + (24);
    if (((uint32_t)(local_rbp)) < ((uint32_t)(1 + 3))) goto loc_00910D17;
    result = PopVerifyPowerActionPolicy(v_stack_p10 + 220, (uint32_t)(*(uint32_t *)(v_rip + 0x5FC16A)), 128 + Arg2 * 1, (uint32_t)(*(uint32_t *)(arg2 + 0x68 + 0xC)));
    if ((*(uint32_t *)(v_stack_p10 + 0x5C)) == 0) goto loc_009110FA;
loc_00910DBF:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x58))) != 0) goto loc_00911106;
loc_00910DD0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C))) != 0) goto loc_00910E88;
loc_00910DE6:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x58))) - 1);
    if (((uint32_t)(result)) <= 58) goto loc_00911122;
loc_00910DF1:
    if (((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x40))) > 90) goto loc_0091112A;
loc_00910DFC:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C))))) != 0) goto loc_00910EA0;
loc_00910E05:
    if ((*(uint32_t *)(v_stack_p10 + 0x48)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44))))) goto loc_00911135;
loc_00910E11:
    if ((*(uint32_t *)(v_stack_p10 + 0x4C)) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44))))) goto loc_0091113D;
loc_00910E1A:
    result = 0;
loc_00910E1C:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00910E32:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)))) - 2)) <= ((uint32_t)(local_rsi))) goto loc_00910C34;
    goto loc_00910C57;
loc_00910E43:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)))) - 2)) <= ((uint32_t)(local_rsi))) goto loc_00910C6C;
    goto loc_00910C8F;
loc_00910E54:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)))) - 2)) <= ((uint32_t)(local_rsi))) goto loc_00910CA8;
    goto loc_00910CCB;
loc_00910E65:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)))) - 2)) <= ((uint32_t)(local_rsi))) goto loc_00910CE4;
    goto loc_00910D07;
loc_00910E76:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)))) - 2)) <= 3) goto loc_00910D44;
    goto loc_00910D68;
loc_00910E88:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)))) >= 60) goto loc_00910DE6;
    *(uint32_t *)(v_stack_p10 + 0x3C) = 60;
    goto loc_00910DE6;
loc_00910EA0:
    if ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)))) - 2) != 0) goto loc_00910E05;
    *(uint8_t *)(v_stack_p10 + 0x40) = 90;
    goto loc_00910E05;
loc_00910EB1:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)))) - 2) | (16));
    goto loc_00910D84;
loc_00910EB9:
    goto loc_00910E1C;
loc_00910EC3:
    *(uint32_t *)(v_stack_p10 + 0x58 + 0x48) = (uint32_t)(local_rsi);
    goto loc_00910B5B;
loc_00910ED8:
    *(uint32_t *)(v_stack_p18) = (uint32_t)(1 + 1);
    goto loc_00910B73;
loc_00910EE3:
    *(uint32_t *)(v_stack_p18) = (uint32_t)(1 + 3);
    goto loc_00910B73;
loc_00910EEE:
    *(uint32_t *)(v_stack_p10 + 0x58 + 0x48) = (uint32_t)(1 + 1);
    goto loc_00910B88;
loc_00910EFA:
    *(uint32_t *)(v_stack_p10 + 0x58 + 0x48) = (uint32_t)(1 + 3);
    goto loc_00910B88;
loc_00910F06:
    *(uint32_t *)(v_stack_p10 + 0x58 + 0x48) = (uint32_t)((uint32_t)((uint32_t)(1 + 3)));
    goto loc_00910B90;
loc_00910F10:
    *(uint32_t *)(v_stack_p18) = (uint32_t)(v_stack_p10 + 88);
    goto loc_00910B9E;
loc_00910F17:
    *(uint32_t *)(v_stack_p10 + 0x48) = (uint32_t)((uint32_t)((uint32_t)(1 + 3)));
    goto loc_00910BAC;
loc_00910F1F:
    *(uint32_t *)(v_stack_p10 + 0xC0) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(1 + 3)))));
    goto loc_00910BC0;
loc_00910F30:
    *(uint32_t *)(v_stack_p10 + 0xC0) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(1 + 3)))));
    goto loc_00910BCE;
loc_00910F3B:
    *(uint32_t *)(v_stack_p10 + 0xD4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(1 + 3)))));
    goto loc_00910BE2;
loc_00910F4C:
    *(uint32_t *)(v_stack_p10 + 0xD4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(1 + 3)))));
    goto loc_00910BF0;
loc_00910F57:
    result = PopIsHiberbootSupported(v_rip + 6275745, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), 60);
    if ((uint8_t)(result) != 0) goto loc_00910C54;
    result = PopIsHibernateSupported(v_rip + 6275745, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), 60);
    if ((uint8_t)(result) != 0) goto loc_00910C54;
    goto loc_00910C47;
loc_00910F7C:
loc_00910F84:
    if (((uint32_t)(v_rip + 6275745)) != ((uint32_t)(1 + 1))) goto loc_00910C54;
loc_00910F9A:
    result = PopIsHiberbootSupported(v_rip + 6275745, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_00910C8C;
    result = PopIsHibernateSupported(v_rip + 6275745, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_00910C8C;
    goto loc_00910C7F;
loc_00910FBF:
loc_00910FC7:
    if (((uint32_t)(v_rip + 6275745)) != ((uint32_t)(1 + 1))) goto loc_00910C8C;
loc_00910FDD:
    result = PopIsHiberbootSupported(v_rip + 6275745, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_00910CC8;
    result = PopIsHibernateSupported(v_rip + 6275745, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_00910CC8;
    goto loc_00910CBB;
loc_00911002:
loc_0091100A:
    if (((uint32_t)(v_rip + 6275745)) != ((uint32_t)(1 + 1))) goto loc_00910CC8;
loc_00911020:
    result = PopIsHiberbootSupported(v_rip + 6275745, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_00910D04;
    result = PopIsHibernateSupported(v_rip + 6275745, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_00910D04;
    goto loc_00910CF7;
loc_00911045:
loc_0091104D:
    if (((uint32_t)(v_rip + 6275745)) != ((uint32_t)(1 + 1))) goto loc_00910D04;
loc_00911063:
    if ((*(uint32_t *)(local_rsi)) >= 3) goto loc_00910D2B;
    *(uint32_t *)(local_rsi) = 6;
    result = PopVerifyPowerActionPolicy(local_rsi, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    goto loc_00910D2B;
loc_0091107F:
    result = PopIsHiberbootSupported(v_rip + 6274618, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_00910D64;
    result = PopIsHibernateSupported(v_rip + 6274598, v_stack_p10 + 88, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), (uint32_t)((uint32_t)(local_rsi)));
    if ((uint8_t)(result) != 0) goto loc_00910D64;
    goto loc_00910D57;
loc_009110AF:
loc_009110BA:
    if (((uint32_t)(v_rip + 6274598)) != ((uint32_t)(1 + 1))) goto loc_00910D64;
loc_009110D1:
    if ((*(uint32_t *)(local_rsi + 0xC)) <= ((uint32_t)(1 + 3))) goto loc_00910D71;
    *(uint32_t *)(local_rsi + 0xC) = (uint32_t)(1 + 3);
    result = PopVerifySystemPowerState(local_r14, (uint32_t)((uint32_t)(v_stack_p10)), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x3C)), 3);
    goto loc_00910D71;
loc_009110EE:
    *(uint32_t *)(local_rsi - 0x4) = 100;
    goto loc_00910D91;
loc_009110FA:
    *(uint32_t *)(v_stack_p10 + 0x5C) = 1;
    goto loc_00910DBF;
loc_00911106:
    if ((*(uint8_t *)(v_rip + 0x5FBDBA)) != 0) goto loc_00910DD0;
    *(uint32_t *)(local_r14) = 0;
    goto loc_00910DD0;
loc_00911122:
    *(uint32_t *)(local_r14) = 60;
    goto loc_00910DF1;
loc_0091112A:
    *(uint8_t *)(v_stack_p10 + 0x40) = 90;
    goto loc_00910DFC;
loc_00911135:
    *(uint32_t *)(v_stack_p10 + 0x48) = 90;
    goto loc_00910E11;
loc_0091113D:
    *(uint32_t *)(v_stack_p10 + 0x4C) = 90;
    goto loc_00910E1A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x30` | `128` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x50` | `128` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x60` | `128` | `R` |
| `Arg1` | `+ 0x70` | `128` | `R` |
| `Arg2` | `- 0xC` | `64` | `R` |
| `Arg2` | `- 0x4` | `32` | `R` |
| `Arg2` | `- 0x4` | `32` | `W` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x4` | `64` | `R` |
| `Arg2` | `+ 0xC` | `32` | `R` |
| `Arg2` | `+ 0xC` | `32` | `W` |
| `Arg2` | `+ 0xC` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x10` | `128` | `R` |
| `Arg2` | `+ 0x1C` | `64` | `R` |
| `Arg2` | `+ 0x20` | `128` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x30` | `128` | `R` |
| `Arg2` | `+ 0x40` | `128` | `R` |
| `Arg2` | `+ 0x44` | `64` | `R` |
| `Arg2` | `+ 0x48` | `32` | `R` |
| `Arg2` | `+ 0x48` | `32` | `W` |

추가 오프셋 10개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00910A8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
