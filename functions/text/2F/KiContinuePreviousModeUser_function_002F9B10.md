# KiContinuePreviousModeUser

- RVA: `0x002F9B10`–`0x002F9FE0` (길이 `1,232` bytes)
- VA: `0x00000001402F9B10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000728C8`
- 디코드: `280`개 명령, `1,232/1,232` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002F9BDF` → [RtlpValidateContextFlags2](../4E/RtlpValidateContextFlags2_function_004EF138.md) (function, `0x004EF138`)
- `0x002F9C16` → [RtlpValidateContextFlags2](../4E/RtlpValidateContextFlags2_function_004EF138.md) (function, `0x004EF138`)
- `0x002F9C43` → [RtlGetExtendedContextLength3](../4E/RtlGetExtendedContextLength3_function_004EF028.md) (function, `0x004EF028`)
- `0x002F9C6B` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x002F9C7D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002F9C96` → [RtlpValidateContextFlags2](../4E/RtlpValidateContextFlags2_function_004EF138.md) (function, `0x004EF138`)
- `0x002F9CB9` → [RtlInitializeExtendedContext2](RtlInitializeExtendedContext2_function_002F5D40.md) (function, `0x002F5D40`)
- `0x002F9CD9` → [RtlpReadExtendedContext](../../page/8D/RtlpReadExtendedContext_function_008D61D0.md) (function, `0x008D61D0`)
- `0x002F9D11` → [RtlLocateExtendedFeature2](RtlLocateExtendedFeature2_function_002F82F0.md) (function, `0x002F82F0`)
- `0x002F9D5A` → [RtlGuardIsValidStackPointer](../../page/9E/RtlGuardIsValidStackPointer_function_009EB860.md) (function, `0x009EB860`)
- `0x002F9D8A` → [PsWow64GetProcessMachine](../../page/8D/PsWow64GetProcessMachine_function_008D2130.md) (function, `0x008D2130`)
- `0x002F9DD5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002F9E65` → [KiVerifyContextXStateCetUEnabled](../3D/KiVerifyContextXStateCetUEnabled_function_003D75C0.md) (function, `0x003D75C0`)
- `0x002F9EA9` → [KiVerifyContextIpForUserCet](../40/KiVerifyContextIpForUserCet_function_0040C028.md) (function, `0x0040C028`)
- `0x002F9EE5` → [KiLogUserCetSetContextIpValidationFailure](../5C/KiLogUserCetSetContextIpValidationFailure_function_005C830C.md) (function, `0x005C830C`)
- `0x002F9F32` → [KeContextToKframes](../4F/KeContextToKframes_function_004FD790.md) (function, `0x004FD790`)

### Direct callers
- [KiContinueEx](../41/KiContinueEx_function_0041C370.md) at `0x0041C45B`

### Static image references
- `0x002F9B3B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x002F9CD9` → [RtlpReadExtendedContext](../../page/8D/RtlpReadExtendedContext_function_008D61D0.md) (`.text` → `PAGE`)
  - `0x002F9D5A` → [RtlGuardIsValidStackPointer](../../page/9E/RtlGuardIsValidStackPointer_function_009EB860.md) (`.text` → `PAGE`)
  - `0x002F9D8A` → [PsWow64GetProcessMachine](../../page/8D/PsWow64GetProcessMachine_function_008D2130.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002F9EDA` → [sub_006DF3D6 + 0x27](../6D/Unknown_function_006DF3D6.md) (`tail-transfer`)
  - `0x002F9FB7` → [sub_006DF3D6](../6D/Unknown_function_006DF3D6.md) (`tail-transfer`)
  - `0x002F9FCB` → [sub_006DF3D6](../6D/Unknown_function_006DF3D6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F9B10  40 55                           push rbp
002F9B12  41 54                           push r12
002F9B14  41 55                           push r13
002F9B16  41 56                           push r14
002F9B18  41 57                           push r15
002F9B1A  48 81 EC 80 00 00 00            sub rsp, 0x80
002F9B21  48 8D 6C 24 30                  lea rbp, [rsp + 0x30]
002F9B26  48 89 9D 80 00 00 00            mov qword ptr [rbp + 0x80], rbx
002F9B2D  48 89 B5 88 00 00 00            mov qword ptr [rbp + 0x88], rsi
002F9B34  48 89 BD 90 00 00 00            mov qword ptr [rbp + 0x90], rdi
002F9B3B  48 8B 05 FE 0B B1 00            mov rax, qword ptr [rip + 0xb10bfe]
002F9B42  48 33 C5                        xor rax, rbp
002F9B45  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
002F9B49  4C 89 45 40                     mov qword ptr [rbp + 0x40], r8
002F9B4D  48 89 55 38                     mov qword ptr [rbp + 0x38], rdx
002F9B51  4C 8B E9                        mov r13, rcx
002F9B54  45 33 E4                        xor r12d, r12d
002F9B57  4C 89 65 08                     mov qword ptr [rbp + 8], r12
002F9B5B  44 89 65 10                     mov dword ptr [rbp + 0x10], r12d
002F9B5F  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
002F9B68  8B 79 30                        mov edi, dword ptr [rcx + 0x30]
002F9B6B  89 7D 30                        mov dword ptr [rbp + 0x30], edi
002F9B6E  49 81 F9 FF 00 00 00            cmp r9, 0xff
002F9B75  77 0F                           ja 0x1402f9b86
002F9B77  0F 57 C0                        xorps xmm0, xmm0
002F9B7A  33 C0                           xor eax, eax
002F9B7C  0F 11 45 18                     movups xmmword ptr [rbp + 0x18], xmm0
002F9B80  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
002F9B84  EB 41                           jmp 0x1402f9bc7
002F9B86  41 0F 10 09                     movups xmm1, xmmword ptr [r9]
002F9B8A  0F 11 4D 18                     movups xmmword ptr [rbp + 0x18], xmm1
002F9B8E  F2 41 0F 10 41 10               movsd xmm0, qword ptr [r9 + 0x10]
002F9B94  F2 0F 11 45 28                  movsd qword ptr [rbp + 0x28], xmm0
002F9B99  66 48 0F 7E C8                  movq rax, xmm1
002F9B9E  48 C1 E8 20                     shr rax, 0x20
002F9BA2  A9 FC FF FF FF                  test eax, 0xfffffffc
002F9BA7  75 14                           jne 0x1402f9bbd
002F9BA9  48 83 7D 20 00                  cmp qword ptr [rbp + 0x20], 0
002F9BAE  75 0D                           jne 0x1402f9bbd
002F9BB0  83 7D 18 04                     cmp dword ptr [rbp + 0x18], 4
002F9BB4  73 07                           jae 0x1402f9bbd
002F9BB6  48 83 7D 28 00                  cmp qword ptr [rbp + 0x28], 0
002F9BBB  74 0A                           je 0x1402f9bc7
002F9BBD  B8 0D 00 00 C0                  mov eax, 0xc000000d
002F9BC2  E9 07 02 00 00                  jmp 0x1402f9dce
002F9BC7  EB 05                           jmp 0x1402f9bce
002F9BC9  E9 00 02 00 00                  jmp 0x1402f9dce
002F9BCE  48 BB D8 03 00 00 80 F7 FF FF   movabs rbx, 0xfffff780000003d8
002F9BD8  4C 8B C3                        mov r8, rbx
002F9BDB  33 D2                           xor edx, edx
002F9BDD  8B CF                           mov ecx, edi
002F9BDF  E8 54 55 1F 00                  call 0x1404ef138
002F9BE4  85 C0                           test eax, eax
002F9BE6  78 0A                           js 0x1402f9bf2
002F9BE8  0F BA E7 14                     bt edi, 0x14
002F9BEC  0F 83 71 03 00 00               jae 0x1402f9f63
002F9BF2  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
002F9BF8  41 3B C7                        cmp eax, r15d
002F9BFB  0F 84 68 03 00 00               je 0x1402f9f69
002F9C01  85 C0                           test eax, eax
002F9C03  0F 88 C5 01 00 00               js 0x1402f9dce
002F9C09  44 89 65 00                     mov dword ptr [rbp], r12d
002F9C0D  4C 8B C3                        mov r8, rbx
002F9C10  48 8D 55 00                     lea rdx, [rbp]
002F9C14  8B CF                           mov ecx, edi
002F9C16  E8 1D 55 1F 00                  call 0x1404ef138
002F9C1B  48 BE 08 07 00 00 80 F7 FF FF   movabs rsi, 0xfffff78000000708
002F9C25  85 C0                           test eax, eax
002F9C27  0F 88 A1 01 00 00               js 0x1402f9dce
002F9C2D  4D 8B C4                        mov r8, r12
002F9C30  F6 45 00 02                     test byte ptr [rbp], 2
002F9C34  0F 85 D9 01 00 00               jne 0x1402f9e13
002F9C3A  4C 8B CB                        mov r9, rbx
002F9C3D  48 8D 55 10                     lea rdx, [rbp + 0x10]
002F9C41  8B CF                           mov ecx, edi
002F9C43  E8 E0 53 1F 00                  call 0x1404ef028
002F9C48  85 C0                           test eax, eax
002F9C4A  0F 88 7E 01 00 00               js 0x1402f9dce
002F9C50  44 8B 45 10                     mov r8d, dword ptr [rbp + 0x10]
002F9C54  49 8D 40 0F                     lea rax, [r8 + 0xf]
002F9C58  49 3B C0                        cmp rax, r8
002F9C5B  77 0A                           ja 0x1402f9c67
002F9C5D  48 B8 F0 FF FF FF FF FF FF 0F   movabs rax, 0xffffffffffffff0
002F9C67  48 83 E0 F0                     and rax, 0xfffffffffffffff0
002F9C6B  E8 F0 0C 3C 00                  call 0x1406ba960
002F9C70  48 2B E0                        sub rsp, rax
002F9C73  48 8D 5C 24 30                  lea rbx, [rsp + 0x30]
002F9C78  33 D2                           xor edx, edx
002F9C7A  48 8B CB                        mov rcx, rbx
002F9C7D  E8 BE CF 3C 00                  call 0x1406c6c40
002F9C82  44 89 65 04                     mov dword ptr [rbp + 4], r12d
002F9C86  49 B8 D8 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003d8
002F9C90  48 8D 55 04                     lea rdx, [rbp + 4]
002F9C94  8B CF                           mov ecx, edi
002F9C96  E8 9D 54 1F 00                  call 0x1404ef138
002F9C9B  85 C0                           test eax, eax
002F9C9D  0F 88 2B 01 00 00               js 0x1402f9dce
002F9CA3  4D 8B CC                        mov r9, r12
002F9CA6  F6 45 04 02                     test byte ptr [rbp + 4], 2
002F9CAA  0F 85 4E 01 00 00               jne 0x1402f9dfe
002F9CB0  4C 8D 45 08                     lea r8, [rbp + 8]
002F9CB4  8B D7                           mov edx, edi
002F9CB6  48 8B CB                        mov rcx, rbx
002F9CB9  E8 82 C0 FF FF                  call 0x1402f5d40
002F9CBE  85 C0                           test eax, eax
002F9CC0  0F 88 08 01 00 00               js 0x1402f9dce
002F9CC6  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
002F9CCB  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
002F9CD0  44 8B CF                        mov r9d, edi
002F9CD3  4C 8B 45 08                     mov r8, qword ptr [rbp + 8]
002F9CD7  B2 01                           mov dl, 1
002F9CD9  E8 F2 C4 5D 00                  call 0x1408d61d0
002F9CDE  85 C0                           test eax, eax
002F9CE0  0F 88 E8 00 00 00               js 0x1402f9dce
002F9CE6  4C 89 65 08                     mov qword ptr [rbp + 8], r12
002F9CEA  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
002F9CED  25 40 00 10 00                  and eax, 0x100040
002F9CF2  3D 40 00 10 00                  cmp eax, 0x100040
002F9CF7  75 29                           jne 0x1402f9d22
002F9CF9  48 8D 8B D0 04 00 00            lea rcx, [rbx + 0x4d0]
002F9D00  45 33 C9                        xor r9d, r9d
002F9D03  41 8D 51 0B                     lea edx, [r9 + 0xb]
002F9D07  49 B8 D8 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003d8
002F9D11  E8 DA E5 FF FF                  call 0x1402f82f0
002F9D16  4C 8B C0                        mov r8, rax
002F9D19  48 85 C0                        test rax, rax
002F9D1C  0F 85 FC 00 00 00               jne 0x1402f9e1e
002F9D22  49 8B B6 20 02 00 00            mov rsi, qword ptr [r14 + 0x220]
002F9D29  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
002F9D2F  A8 20                           test al, 0x20
002F9D31  74 34                           je 0x1402f9d67
002F9D33  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
002F9D36  25 01 00 10 00                  and eax, 0x100001
002F9D3B  3D 01 00 10 00                  cmp eax, 0x100001
002F9D40  75 25                           jne 0x1402f9d67
002F9D42  4C 8B AB 98 00 00 00            mov r13, qword ptr [rbx + 0x98]
002F9D49  49 8B 86 F0 00 00 00            mov rax, qword ptr [r14 + 0xf0]
002F9D50  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
002F9D54  48 8B D0                        mov rdx, rax
002F9D57  49 8B CD                        mov rcx, r13
002F9D5A  E8 01 1B 6F 00                  call 0x1409eb860
002F9D5F  85 C0                           test eax, eax
002F9D61  0F 84 31 02 00 00               je 0x1402f9f98
002F9D67  41 BC 4C 01 00 00               mov r12d, 0x14c
002F9D6D  49 8B B6 20 02 00 00            mov rsi, qword ptr [r14 + 0x220]
002F9D74  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
002F9D77  25 01 00 10 00                  and eax, 0x100001
002F9D7C  3D 01 00 10 00                  cmp eax, 0x100001
002F9D81  0F 85 8C 01 00 00               jne 0x1402f9f13
002F9D87  48 8B CE                        mov rcx, rsi
002F9D8A  E8 A1 83 5D 00                  call 0x1408d2130
002F9D8F  66 41 3B C4                     cmp ax, r12w
002F9D93  74 14                           je 0x1402f9da9
002F9D95  48 83 BE 40 06 00 00 00         cmp qword ptr [rsi + 0x640], 0
002F9D9D  0F 85 2D 02 00 00               jne 0x1402f9fd0
002F9DA3  66 C7 43 38 33 00               mov word ptr [rbx + 0x38], 0x33
002F9DA9  4D 8B AE B8 00 00 00            mov r13, qword ptr [r14 + 0xb8]
002F9DB0  41 F7 46 74 00 00 10 00         test dword ptr [r14 + 0x74], 0x100000
002F9DB8  0F 85 B9 00 00 00               jne 0x1402f9e77
002F9DBE  33 F6                           xor esi, esi
002F9DC0  85 F6                           test esi, esi
002F9DC2  0F 89 4B 01 00 00               jns 0x1402f9f13
002F9DC8  44 8B FE                        mov r15d, esi
002F9DCB  41 8B C7                        mov eax, r15d
002F9DCE  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
002F9DD2  48 33 CD                        xor rcx, rbp
002F9DD5  E8 66 28 3B 00                  call 0x1406ac640
002F9DDA  48 8B 9D 80 00 00 00            mov rbx, qword ptr [rbp + 0x80]
002F9DE1  48 8B B5 88 00 00 00            mov rsi, qword ptr [rbp + 0x88]
002F9DE8  48 8B BD 90 00 00 00            mov rdi, qword ptr [rbp + 0x90]
002F9DEF  48 8D 65 50                     lea rsp, [rbp + 0x50]
002F9DF3  41 5F                           pop r15
002F9DF5  41 5E                           pop r14
002F9DF7  41 5D                           pop r13
002F9DF9  41 5C                           pop r12
002F9DFB  5D                              pop rbp
002F9DFC  C3                              ret
002F9DFD  CC                              int3
002F9DFE  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
002F9E08  4C 8B 0E                        mov r9, qword ptr [rsi]
002F9E0B  4C 0B 08                        or r9, qword ptr [rax]
002F9E0E  E9 9D FE FF FF                  jmp 0x1402f9cb0
002F9E13  4C 8B 06                        mov r8, qword ptr [rsi]
002F9E16  4C 0B 03                        or r8, qword ptr [rbx]
002F9E19  E9 1C FE FF FF                  jmp 0x1402f9c3a
002F9E1E  4C 63 93 E0 04 00 00            movsxd r10, dword ptr [rbx + 0x4e0]
002F9E25  B9 A7 06 00 00                  mov ecx, 0x6a7
002F9E2A  0F 32                           rdmsr
002F9E2C  48 C1 E2 20                     shl rdx, 0x20
002F9E30  48 0B C2                        or rax, rdx
002F9E33  48 89 45 08                     mov qword ptr [rbp + 8], rax
002F9E37  4D 8B 8C 1A D0 04 00 00         mov r9, qword ptr [r10 + rbx + 0x4d0]
002F9E3F  49 8B D1                        mov rdx, r9
002F9E42  81 E2 00 08 00 00               and edx, 0x800
002F9E48  41 F7 46 74 00 00 10 00         test dword ptr [r14 + 0x74], 0x100000
002F9E50  0F 84 99 00 00 00               je 0x1402f9eef
002F9E56  48 85 D2                        test rdx, rdx
002F9E59  0F 84 1C 01 00 00               je 0x1402f9f7b
002F9E5F  48 8B D0                        mov rdx, rax
002F9E62  49 8B C8                        mov rcx, r8
002F9E65  E8 56 D7 0D 00                  call 0x1403d75c0
002F9E6A  85 C0                           test eax, eax
002F9E6C  0F 89 B0 FE FF FF               jns 0x1402f9d22
002F9E72  E9 57 FF FF FF                  jmp 0x1402f9dce
002F9E77  45 8B A5 54 07 00 00            mov r12d, dword ptr [r13 + 0x754]
002F9E7E  41 0F BA E4 11                  bt r12d, 0x11
002F9E83  0F 92 C0                        setb al
002F9E86  A8 01                           test al, 1
002F9E88  0F 84 30 FF FF FF               je 0x1402f9dbe
002F9E8E  41 C1 EC 1F                     shr r12d, 0x1f
002F9E92  48 8D 45 08                     lea rax, [rbp + 8]
002F9E96  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002F9E9B  45 0F B6 CC                     movzx r9d, r12b
002F9E9F  4C 8D 45 18                     lea r8, [rbp + 0x18]
002F9EA3  48 8B D3                        mov rdx, rbx
002F9EA6  49 8B CE                        mov rcx, r14
002F9EA9  E8 7A 21 11 00                  call 0x14040c028
002F9EAE  8B F0                           mov esi, eax
002F9EB0  B8 0A 06 00 C0                  mov eax, 0xc000060a
002F9EB5  3B F0                           cmp esi, eax
002F9EB7  0F 85 03 FF FF FF               jne 0x1402f9dc0
002F9EBD  41 80 F4 01                     xor r12b, 1
002F9EC1  45 0F B6 CC                     movzx r9d, r12b
002F9EC5  4C 8B 83 F8 00 00 00            mov r8, qword ptr [rbx + 0xf8]
002F9ECC  8B 55 18                        mov edx, dword ptr [rbp + 0x18]
002F9ECF  41 F7 85 54 07 00 00 00 00 04 00  test dword ptr [r13 + 0x754], 0x40000
002F9EDA  0F 84 1D 55 3E 00               je 0x1406df3fd
002F9EE0  B9 01 00 00 00                  mov ecx, 1
002F9EE5  E8 22 E4 2C 00                  call 0x1405c830c
002F9EEA  E9 CF FE FF FF                  jmp 0x1402f9dbe
002F9EEF  48 85 D2                        test rdx, rdx
002F9EF2  0F 84 2A FE FF FF               je 0x1402f9d22
002F9EF8  49 83 38 00                     cmp qword ptr [r8], 0
002F9EFC  75 0B                           jne 0x1402f9f09
002F9EFE  49 83 78 08 00                  cmp qword ptr [r8 + 8], 0
002F9F03  0F 84 19 FE FF FF               je 0x1402f9d22
002F9F09  B8 0A 06 00 C0                  mov eax, 0xc000060a
002F9F0E  E9 BB FE FF FF                  jmp 0x1402f9dce
002F9F13  49 8B 96 28 04 00 00            mov rdx, qword ptr [r14 + 0x428]
002F9F1A  48 85 D2                        test rdx, rdx
002F9F1D  75 1F                           jne 0x1402f9f3e
002F9F1F  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
002F9F24  44 8B CF                        mov r9d, edi
002F9F27  4C 8B C3                        mov r8, rbx
002F9F2A  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
002F9F2E  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
002F9F32  E8 59 38 20 00                  call 0x1404fd790
002F9F37  33 C0                           xor eax, eax
002F9F39  E9 90 FE FF FF                  jmp 0x1402f9dce
002F9F3E  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
002F9F41  25 40 00 10 00                  and eax, 0x100040
002F9F46  3D 40 00 10 00                  cmp eax, 0x100040
002F9F4B  75 D2                           jne 0x1402f9f1f
002F9F4D  48 63 83 E0 04 00 00            movsxd rax, dword ptr [rbx + 0x4e0]
002F9F54  48 85 94 18 D0 04 00 00         test qword ptr [rax + rbx + 0x4d0], rdx
002F9F5C  74 C1                           je 0x1402f9f1f
002F9F5E  E9 68 FE FF FF                  jmp 0x1402f9dcb
002F9F63  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
002F9F69  81 E7 1F 00 10 F8               and edi, 0xf810001f
002F9F6F  0F BA EF 14                     bts edi, 0x14
002F9F73  41 8B C4                        mov eax, r12d
002F9F76  E9 86 FC FF FF                  jmp 0x1402f9c01
002F9F7B  49 0F BA E9 0B                  bts r9, 0xb
002F9F80  4D 89 8C 1A D0 04 00 00         mov qword ptr [r10 + rbx + 0x4d0], r9
002F9F88  49 C7 00 01 00 00 00            mov qword ptr [r8], 1
002F9F8F  49 89 40 08                     mov qword ptr [r8 + 8], rax
002F9F93  E9 8A FD FF FF                  jmp 0x1402f9d22
002F9F98  48 83 BE 10 03 00 00 00         cmp qword ptr [rsi + 0x310], 0
002F9FA0  0F 84 25 FE FF FF               je 0x1402f9dcb
002F9FA6  0F B7 86 EC 06 00 00            movzx eax, word ptr [rsi + 0x6ec]
002F9FAD  41 BC 4C 01 00 00               mov r12d, 0x14c
002F9FB3  66 41 3B C4                     cmp ax, r12w
002F9FB7  0F 84 19 54 3E 00               je 0x1406df3d6
002F9FBD  B9 C4 01 00 00                  mov ecx, 0x1c4
002F9FC2  66 3B C1                        cmp ax, cx
002F9FC5  0F 85 00 FE FF FF               jne 0x1402f9dcb
002F9FCB  E9 06 54 3E 00                  jmp 0x1406df3d6
002F9FD0  66 83 7B 38 23                  cmp word ptr [rbx + 0x38], 0x23
002F9FD5  0F 84 CE FD FF FF               je 0x1402f9da9
002F9FDB  E9 C3 FD FF FF                  jmp 0x1402f9da3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiContinuePreviousModeUser(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (128);
    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    result = (*(unsigned __int64 *)(v_rip + 11602942)) ^ (v_stack_m78);
    v_stack_m30 = result;
    v_stack_m38 = a3;
    v_stack_m40 = a2;
    v_r12 = 0;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    if (a4 > 255) goto loc_002F9B86;
    result = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = 0;
    goto loc_002F9BC7;
loc_002F9B86:
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm0;
    result = (result) >> (32);
    if ((((unsigned int)(result)) & (0xFFFFFFFCULL)) != 0) goto loc_002F9BBD;
    if (v_stack_m58 != 0) goto loc_002F9BBD;
    if (v_stack_m60 >= 4) goto loc_002F9BBD;
    if (v_stack_m50 == 0) goto loc_002F9BC7;
loc_002F9BBD:
    goto loc_002F9DCE;
loc_002F9BC7:
    goto loc_002F9BCE;
loc_002F9BCE:
    a2 = 0;
    result = RtlpValidateContextFlags2((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))), a2, v_rbx, a4);
    if (sign_flag) goto loc_002F9BF2;
    if (condition_is_above_or_equal) goto loc_002F9F63;
loc_002F9BF2:
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000000DULL)))) goto loc_002F9F69;
loc_002F9C01:
    if (sign_flag) goto loc_002F9DCE;
    v_stack_m78 = 0;
    result = RtlpValidateContextFlags2((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))), v_stack_m78, v_rbx, a4);
    if (sign_flag) goto loc_002F9DCE;
    if (((v_stack_m78) & (2)) != 0) goto loc_002F9E13;
loc_002F9C3A:
    result = RtlGetExtendedContextLength3((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))), v_stack_m68, 0, v_rbx);
    if (sign_flag) goto loc_002F9DCE;
    if (((unsigned int)(v_stack_m68) + 15) <= ((unsigned int)(v_stack_m68))) {
    }
    result = ((unsigned int)(v_stack_m68) + 15) & (-16);
    result = _chkstk((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))), v_stack_m68, (unsigned int)(v_stack_m68), v_rbx);
    v_rsp = (v_rsp) - (result);
    a2 = 0;
    result = memset(v_stack_m78, a2, (unsigned int)(v_stack_m68), v_rbx);
    v_stack_m74 = 0;
    result = RtlpValidateContextFlags2((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))), v_stack_m74, (unsigned int)(v_stack_m68), v_rbx);
    if (sign_flag) goto loc_002F9DCE;
    if (((v_stack_m74) & (2)) != 0) goto loc_002F9DFE;
loc_002F9CB0:
    result = RtlInitializeExtendedContext2(v_stack_m78, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))), v_stack_m70, 0);
    if (sign_flag) goto loc_002F9DCE;
    v_stack_m80 = 0;
    v_stack_m88 = a1;
    result = RtlpReadExtendedContext(v_stack_m78, 1, v_stack_m70, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    if (sign_flag) goto loc_002F9DCE;
    v_stack_m70 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m78 + 48))) & (0x100040ULL));
    if (((unsigned int)(result)) != 0x100040ULL) goto loc_002F9D22;
    a4 = 0;
    result = RtlLocateExtendedFeature2(v_stack_m78 + 1232, a4 + 11, v_stack_m70, a4);
    if (result != 0) goto loc_002F9E1E;
loc_002F9D22:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 136)))) & (32)) == 0) goto loc_002F9D67;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m78 + 48))) & (0x100001ULL));
    if (((unsigned int)(result)) != 0x100001ULL) goto loc_002F9D67;
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240);
    result = RtlGuardIsValidStackPointer(*(unsigned __int64 *)(v_stack_m78 + 152), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240), result, a4);
    if ((unsigned int)(result) == 0) goto loc_002F9F98;
loc_002F9D67:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m78 + 48))) & (0x100001ULL));
    if (((unsigned int)(result)) != 0x100001ULL) goto loc_002F9F13;
    result = PsWow64GetProcessMachine(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240), result, a4);
    if (((unsigned __int16)(result)) == 332) goto loc_002F9DA9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1600)) != 0) goto loc_002F9FD0;
loc_002F9DA3:
    *(unsigned __int16 *)(v_stack_m78 + 56) = 51;
loc_002F9DA9:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x100000ULL)) != 0) goto loc_002F9E77;
loc_002F9DBE:
    v_rsi = 0;
loc_002F9DC0:
    if (!sign_flag) goto loc_002F9F13;
loc_002F9DCB:
loc_002F9DCE:
    a1 = (v_stack_m30) ^ (v_stack_m78);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240), result, a4);
    return result;
loc_002F9DFE:
    a4 = (*(unsigned __int64 *)(v_stack_p10)) | (*(unsigned __int64 *)(result));
    goto loc_002F9CB0;
loc_002F9E13:
    a3 = (*(unsigned __int64 *)(v_stack_p10)) | (*(unsigned __int64 *)(v_stack_p8));
    goto loc_002F9C3A;
loc_002F9E1E:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240)) << (32);
    result = (result) | (a2);
    v_stack_m70 = result;
    a2 = (unsigned int)((*(unsigned __int64 *)((int)(*(unsigned int *)(v_stack_p8 + 1248)) + v_stack_p8 * 1 + 1232)) & (0x800ULL));
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x100000ULL)) == 0) goto loc_002F9EEF;
    if (a2 == 0) goto loc_002F9F7B;
    result = KiVerifyContextXStateCetUEnabled(a3, result, a3, *(unsigned __int64 *)((int)(*(unsigned int *)(v_stack_p8 + 1248)) + v_stack_p8 * 1 + 1232));
    if (!sign_flag) goto loc_002F9D22;
    goto loc_002F9DCE;
loc_002F9E77:
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_002F9DBE;
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1876))) >> (31));
    v_stack_p20 = v_stack_m70;
    result = KiVerifyContextIpForUserCet(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_p8, v_stack_m60, (unsigned __int8)(v_r12));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC000060AULL)))) goto loc_002F9DC0;
    v_r12 = (unsigned __int8)((v_r12) ^ (1));
    result = KiLogUserCetSetContextIpValidationFailure(1, (unsigned int)(v_stack_m60), *(unsigned __int64 *)(v_stack_p8 + 248), (unsigned __int8)(v_r12));
    goto loc_002F9DBE;
loc_002F9EEF:
    if ((unsigned int)(v_stack_m60) == 0) goto loc_002F9D22;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 248))) != 0) goto loc_002F9F09;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 248) + 8)) == 0) goto loc_002F9D22;
loc_002F9F09:
    goto loc_002F9DCE;
loc_002F9F13:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1064) != 0) goto loc_002F9F3E;
loc_002F9F1F:
    v_stack_p20 = 1;
    result = KeContextToKframes(v_stack_m38, v_stack_m40, v_stack_p8, (unsigned int)((unsigned int)(v_stack_p18)));
    result = 0;
    goto loc_002F9DCE;
loc_002F9F3E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 48))) & (0x100040ULL));
    if (((unsigned int)(result)) != 0x100040ULL) goto loc_002F9F1F;
    if (((*(unsigned __int64 *)((int)(*(unsigned int *)(v_stack_p8 + 1248)) + v_stack_p8 * 1 + 1232)) & (v_stack_m40)) == 0) goto loc_002F9F1F;
    goto loc_002F9DCB;
loc_002F9F63:
loc_002F9F69:
    v_rdi = (unsigned int)((v_stack_p18) & (0xF810001FULL));
    goto loc_002F9C01;
loc_002F9F7B:
    *(unsigned __int64 *)((int)(*(unsigned int *)(v_stack_p8 + 1248)) + v_stack_p8 * 1 + 1232) = (unsigned int)((unsigned int)(v_stack_p18));
    *(unsigned __int64 *)(v_stack_p8) = 1;
    *(unsigned __int64 *)(v_stack_p8 + 8) = (unsigned int)((unsigned int)(v_r12));
    goto loc_002F9D22;
loc_002F9F98:
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 784)) == 0) goto loc_002F9DCB;
    if (((unsigned __int16)(*(unsigned __int16 *)((unsigned int)((unsigned int)(result)) + 1772))) != 452) goto loc_002F9DCB;
loc_002F9FD0:
    if ((*(unsigned __int16 *)(v_stack_p8 + 56)) == 35) goto loc_002F9DA9;
    goto loc_002F9DA3;
}
```

## 5. (Beta) C Style

```c
int64_t KiContinuePreviousModeUser(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (128);
    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    result = (*(uint64_t *)(v_rip + 0xB10BFE)) ^ (v_stack_m78);
    v_stack_m30 = result;
    v_stack_m38 = Arg3;
    v_stack_m40 = Arg2;
    local_r12 = 0;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    if (Arg4 > 255) goto loc_002F9B86;
    result = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = 0;
    goto loc_002F9BC7;
loc_002F9B86:
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm0;
    result = (result) >> (32);
    if ((((uint32_t)(result)) & (0xFFFFFFFCULL)) != 0) goto loc_002F9BBD;
    if (v_stack_m58 != 0) goto loc_002F9BBD;
    if (v_stack_m60 >= 4) goto loc_002F9BBD;
    if (v_stack_m50 == 0) goto loc_002F9BC7;
loc_002F9BBD:
    goto loc_002F9DCE;
loc_002F9BC7:
    goto loc_002F9BCE;
loc_002F9BCE:
    Arg2 = 0;
    result = RtlpValidateContextFlags2((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))), Arg2, local_rbx, Arg4);
    if (sign_flag) goto loc_002F9BF2;
    if (condition_is_above_or_equal) goto loc_002F9F63;
loc_002F9BF2:
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000000DULL)))) goto loc_002F9F69;
loc_002F9C01:
    if (sign_flag) goto loc_002F9DCE;
    v_stack_m78 = 0;
    result = RtlpValidateContextFlags2((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))), v_stack_m78, local_rbx, Arg4);
    if (sign_flag) goto loc_002F9DCE;
    if (((v_stack_m78) & (2)) != 0) goto loc_002F9E13;
loc_002F9C3A:
    result = RtlGetExtendedContextLength3((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))), v_stack_m68, 0, local_rbx);
    if (sign_flag) goto loc_002F9DCE;
    if (((uint32_t)(v_stack_m68) + 15) <= ((uint32_t)(v_stack_m68))) {
    }
    result = ((uint32_t)(v_stack_m68) + 15) & (-16);
    result = _chkstk((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))), v_stack_m68, (uint32_t)(v_stack_m68), local_rbx);
    local_rsp = (local_rsp) - (result);
    Arg2 = 0;
    result = memset(v_stack_m78, Arg2, (uint32_t)(v_stack_m68), local_rbx);
    v_stack_m74 = 0;
    result = RtlpValidateContextFlags2((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))), v_stack_m74, (uint32_t)(v_stack_m68), local_rbx);
    if (sign_flag) goto loc_002F9DCE;
    if (((v_stack_m74) & (2)) != 0) goto loc_002F9DFE;
loc_002F9CB0:
    result = RtlInitializeExtendedContext2(v_stack_m78, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))), v_stack_m70, 0);
    if (sign_flag) goto loc_002F9DCE;
    v_stack_m80 = 0;
    v_stack_m88 = Arg1;
    result = RtlpReadExtendedContext(v_stack_m78, 1, v_stack_m70, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    if (sign_flag) goto loc_002F9DCE;
    v_stack_m70 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m78 + 0x30))) & (0x100040ULL));
    if (((uint32_t)(result)) != 0x100040ULL) goto loc_002F9D22;
    Arg4 = 0;
    result = RtlLocateExtendedFeature2(v_stack_m78 + 1232, Arg4 + 11, v_stack_m70, Arg4);
    if (result != 0) goto loc_002F9E1E;
loc_002F9D22:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x88)))) & (32)) == 0) goto loc_002F9D67;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m78 + 0x30))) & (0x100001ULL));
    if (((uint32_t)(result)) != 0x100001ULL) goto loc_002F9D67;
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0);
    result = RtlGuardIsValidStackPointer(*(uint64_t *)(v_stack_m78 + 0x98), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0), result, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002F9F98;
loc_002F9D67:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m78 + 0x30))) & (0x100001ULL));
    if (((uint32_t)(result)) != 0x100001ULL) goto loc_002F9F13;
    result = PsWow64GetProcessMachine(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0), result, Arg4);
    if (((uint16_t)(result)) == 332) goto loc_002F9DA9;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x640)) != 0) goto loc_002F9FD0;
loc_002F9DA3:
    *(uint16_t *)(v_stack_m78 + 0x38) = 51;
loc_002F9DA9:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x100000ULL)) != 0) goto loc_002F9E77;
loc_002F9DBE:
    local_rsi = 0;
loc_002F9DC0:
    if (!sign_flag) goto loc_002F9F13;
loc_002F9DCB:
loc_002F9DCE:
    Arg1 = (v_stack_m30) ^ (v_stack_m78);
    result = _security_check_cookie(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0), result, Arg4);
    return result;
loc_002F9DFE:
    Arg4 = (*(uint64_t *)(v_stack_p10)) | (*(uint64_t *)(result));
    goto loc_002F9CB0;
loc_002F9E13:
    Arg3 = (*(uint64_t *)(v_stack_p10)) | (*(uint64_t *)(v_stack_p8));
    goto loc_002F9C3A;
loc_002F9E1E:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0)) << (32);
    result = (result) | (Arg2);
    v_stack_m70 = result;
    Arg2 = (uint32_t)((*(uint64_t *)((int32_t)(*(uint32_t *)(v_stack_p8 + 0x4E0)) + v_stack_p8 * 1 + 0x4D0)) & (0x800ULL));
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x100000ULL)) == 0) goto loc_002F9EEF;
    if (Arg2 == 0) goto loc_002F9F7B;
    result = KiVerifyContextXStateCetUEnabled(Arg3, result, Arg3, *(uint64_t *)((int32_t)(*(uint32_t *)(v_stack_p8 + 0x4E0)) + v_stack_p8 * 1 + 0x4D0));
    if (!sign_flag) goto loc_002F9D22;
    goto loc_002F9DCE;
loc_002F9E77:
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_002F9DBE;
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x754))) >> (31));
    v_stack_p20 = v_stack_m70;
    result = KiVerifyContextIpForUserCet(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_p8, v_stack_m60, (uint8_t)(local_r12));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC000060AULL)))) goto loc_002F9DC0;
    local_r12 = (uint8_t)((local_r12) ^ (1));
    result = KiLogUserCetSetContextIpValidationFailure(1, (uint32_t)(v_stack_m60), *(uint64_t *)(v_stack_p8 + 0xF8), (uint8_t)(local_r12));
    goto loc_002F9DBE;
loc_002F9EEF:
    if ((uint32_t)(v_stack_m60) == 0) goto loc_002F9D22;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF8))) != 0) goto loc_002F9F09;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xF8) + 0x8)) == 0) goto loc_002F9D22;
loc_002F9F09:
    goto loc_002F9DCE;
loc_002F9F13:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x428) != 0) goto loc_002F9F3E;
loc_002F9F1F:
    v_stack_p20 = 1;
    result = KeContextToKframes(v_stack_m38, v_stack_m40, v_stack_p8, (uint32_t)((uint32_t)(v_stack_p18)));
    result = 0;
    goto loc_002F9DCE;
loc_002F9F3E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x30))) & (0x100040ULL));
    if (((uint32_t)(result)) != 0x100040ULL) goto loc_002F9F1F;
    if (((*(uint64_t *)((int32_t)(*(uint32_t *)(v_stack_p8 + 0x4E0)) + v_stack_p8 * 1 + 0x4D0)) & (v_stack_m40)) == 0) goto loc_002F9F1F;
    goto loc_002F9DCB;
loc_002F9F63:
loc_002F9F69:
    local_rdi = (uint32_t)((v_stack_p18) & (0xF810001FULL));
    goto loc_002F9C01;
loc_002F9F7B:
    *(uint64_t *)((int32_t)(*(uint32_t *)(v_stack_p8 + 0x4E0)) + v_stack_p8 * 1 + 0x4D0) = (uint32_t)((uint32_t)(v_stack_p18));
    *(uint64_t *)(v_stack_p8) = 1;
    *(uint64_t *)(v_stack_p8 + 0x8) = (uint32_t)((uint32_t)(local_r12));
    goto loc_002F9D22;
loc_002F9F98:
    if ((*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x310)) == 0) goto loc_002F9DCB;
    if (((uint16_t)(*(uint16_t *)((uint32_t)((uint32_t)(result)) + 0x6EC))) != 452) goto loc_002F9DCB;
loc_002F9FD0:
    if ((*(uint16_t *)(v_stack_p8 + 0x38)) == 35) goto loc_002F9DA9;
    goto loc_002F9DA3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F9B10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
