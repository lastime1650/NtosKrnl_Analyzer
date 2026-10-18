# PpForEachDeviceInstanceDriver

- RVA: `0x00A07D2C`–`0x00A08270` (길이 `1,348` bytes)
- VA: `0x0000000140A07D2C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A8690`
- 디코드: `326`개 명령, `1,348/1,348` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00A07DF1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A07E0D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A07E4D` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x00A07E97` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00A07ED8` → [CmOpenCommonClassRegKey](../8E/CmOpenCommonClassRegKey_function_008EFF5C.md) (function, `0x008EFF5C`)
- `0x00A07F03` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A07F24` → [PnpUnicodeStringToWstrFree](../8F/PnpUnicodeStringToWstrFree_function_008F59F0.md) (function, `0x008F59F0`)
- `0x00A07F33` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A07F41` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A07F4F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A07F5D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A07F94` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0802E` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A08088` → [PiForEachDriverQueryRoutine](PiForEachDriverQueryRoutine_function_00A08278.md) (function, `0x00A08278`)
- `0x00A080C6` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00A08112` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0812A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A081A2` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A081DC` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00A0820D` → [CmGetInstallerClassRegProp](../99/CmGetInstallerClassRegProp_function_00994940.md) (function, `0x00994940`)

### Direct callers
- [PiDeviceRegistration](PiDeviceRegistration_function_00A07A60.md) at `0x00A07C2D`
- [PiDeviceRegistration](PiDeviceRegistration_function_00A07A60.md) at `0x00A07CF5`

### Static image references
- `0x00A07D48` → RVA `0x00E0A740` (`.data`; read)
- `0x00A07E1E` → RVA `0x00E66398` (`.data`; read)
- `0x00A07EE8` → RVA `0x00998530` (`PiProcessDriverInstance`; read)
- `0x00A07FAF` → RVA `0x00002DF0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00A07DF1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A07E0D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A07F03` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A07F33` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A07F41` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A07F4F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A07F5D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A07F94` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A08112` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0812A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00A08257` → [sub_00B346F2](../B3/Unknown_function_00B346F2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A07D2C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00A07D31  55                              push rbp
00A07D32  56                              push rsi
00A07D33  57                              push rdi
00A07D34  41 54                           push r12
00A07D36  41 55                           push r13
00A07D38  41 56                           push r14
00A07D3A  41 57                           push r15
00A07D3C  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00A07D41  48 81 EC 00 01 00 00            sub rsp, 0x100
00A07D48  48 8B 05 F1 29 40 00            mov rax, qword ptr [rip + 0x4029f1]
00A07D4F  48 33 C4                        xor rax, rsp
00A07D52  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00A07D56  45 33 ED                        xor r13d, r13d
00A07D59  4D 8B F8                        mov r15, r8
00A07D5C  4C 89 6D 97                     mov qword ptr [rbp - 0x69], r13
00A07D60  4C 8B F1                        mov r14, rcx
00A07D63  4C 89 6D 9F                     mov qword ptr [rbp - 0x61], r13
00A07D67  41 8B F5                        mov esi, r13d
00A07D6A  44 89 6D 8B                     mov dword ptr [rbp - 0x75], r13d
00A07D6E  44 89 6D 8F                     mov dword ptr [rbp - 0x71], r13d
00A07D72  44 89 6D 87                     mov dword ptr [rbp - 0x79], r13d
00A07D76  44 89 6D 93                     mov dword ptr [rbp - 0x6d], r13d
00A07D7A  48 85 C9                        test rcx, rcx
00A07D7D  0F 84 B6 04 00 00               je 0x140a08239
00A07D83  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00A07D87  45 8D 4D 02                     lea r9d, [r13 + 2]
00A07D8B  41 BA 00 01 00 00               mov r10d, 0x100
00A07D91  66 41 3B D1                     cmp dx, r9w
00A07D95  0F 82 B1 04 00 00               jb 0x140a0824c
00A07D9B  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
00A07D9F  48 85 FF                        test rdi, rdi
00A07DA2  0F 84 A4 04 00 00               je 0x140a0824c
00A07DA8  0F B7 09                        movzx ecx, word ptr [rcx]
00A07DAB  66 3B CA                        cmp cx, dx
00A07DAE  0F 87 85 04 00 00               ja 0x140a08239
00A07DB4  66 85 C9                        test cx, cx
00A07DB7  0F 84 C1 01 00 00               je 0x140a07f7e
00A07DBD  66 44 39 2F                     cmp word ptr [rdi], r13w
00A07DC1  74 5B                           je 0x140a07e1e
00A07DC3  66 3B CA                        cmp cx, dx
00A07DC6  75 0D                           jne 0x140a07dd5
00A07DC8  8B C1                           mov eax, ecx
00A07DCA  48 D1 E8                        shr rax, 1
00A07DCD  66 44 39 6C 47 FE               cmp word ptr [rdi + rax*2 - 2], r13w
00A07DD3  74 49                           je 0x140a07e1e
00A07DD5  48 8B C2                        mov rax, rdx
00A07DD8  49 2B C1                        sub rax, r9
00A07DDB  48 3B C8                        cmp rcx, rax
00A07DDE  0F 86 33 04 00 00               jbe 0x140a08217
00A07DE4  48 8D 51 02                     lea rdx, [rcx + 2]
00A07DE8  41 B8 50 70 73 75               mov r8d, 0x75737050
00A07DEE  49 8B CA                        mov rcx, r10
00A07DF1  E8 FA A2 17 00                  call 0x140b820f0
00A07DF6  48 8B F8                        mov rdi, rax
00A07DF9  48 85 C0                        test rax, rax
00A07DFC  0F 84 A3 01 00 00               je 0x140a07fa5
00A07E02  45 0F B7 06                     movzx r8d, word ptr [r14]
00A07E06  48 8B C8                        mov rcx, rax
00A07E09  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00A07E0D  E8 2E EA CB FF                  call 0x1406c6840
00A07E12  41 0F B7 06                     movzx eax, word ptr [r14]
00A07E16  48 D1 E8                        shr rax, 1
00A07E19  66 44 89 2C 47                  mov word ptr [rdi + rax*2], r13w
00A07E1E  48 8B 0D 73 E5 45 00            mov rcx, qword ptr [rip + 0x45e573]
00A07E25  48 8D 45 9F                     lea rax, [rbp - 0x61]
00A07E29  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00A07E2E  45 33 C9                        xor r9d, r9d
00A07E31  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A07E36  41 BC 19 00 02 00               mov r12d, 0x20019
00A07E3C  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
00A07E41  48 8B D7                        mov rdx, rdi
00A07E44  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00A07E49  45 8D 41 10                     lea r8d, [r9 + 0x10]
00A07E4D  E8 EE 66 EE FF                  call 0x1408ee540
00A07E52  8B D8                           mov ebx, eax
00A07E54  85 C0                           test eax, eax
00A07E56  0F 88 BD 00 00 00               js 0x140a07f19
00A07E5C  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
00A07E60  48 8D 45 8B                     lea rax, [rbp - 0x75]
00A07E64  48 8B 0D 2D E5 45 00            mov rcx, qword ptr [rip + 0x45e52d]
00A07E6B  41 B9 09 00 00 00               mov r9d, 9
00A07E71  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
00A07E76  48 8B D7                        mov rdx, rdi
00A07E79  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A07E7E  48 8D 45 C7                     lea rax, [rbp - 0x39]
00A07E82  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A07E87  48 8D 45 8F                     lea rax, [rbp - 0x71]
00A07E8B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A07E90  C7 45 8B 4E 00 00 00            mov dword ptr [rbp - 0x75], 0x4e
00A07E97  E8 D4 59 EE FF                  call 0x1408ed870
00A07E9C  8B D8                           mov ebx, eax
00A07E9E  85 C0                           test eax, eax
00A07EA0  78 3D                           js 0x140a07edf
00A07EA2  83 7D 8F 01                     cmp dword ptr [rbp - 0x71], 1
00A07EA6  75 37                           jne 0x140a07edf
00A07EA8  44 39 6D 8B                     cmp dword ptr [rbp - 0x75], r13d
00A07EAC  74 31                           je 0x140a07edf
00A07EAE  48 8B 0D E3 E4 45 00            mov rcx, qword ptr [rip + 0x45e4e3]
00A07EB5  48 8D 45 97                     lea rax, [rbp - 0x69]
00A07EB9  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00A07EBE  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00A07EC2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A07EC7  45 33 C9                        xor r9d, r9d
00A07ECA  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
00A07ECF  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00A07ED4  45 8D 41 20                     lea r8d, [r9 + 0x20]
00A07ED8  E8 7F 80 EE FF                  call 0x1408eff5c
00A07EDD  8B D8                           mov ebx, eax
00A07EDF  BA AA 00 00 00                  mov edx, 0xaa
00A07EE4  4C 89 7D B7                     mov qword ptr [rbp - 0x49], r15
00A07EE8  48 8D 05 41 06 F9 FF            lea rax, [rip - 0x6f9bf]
00A07EEF  4C 89 75 A7                     mov qword ptr [rbp - 0x59], r14
00A07EF3  41 B8 50 70 20 20               mov r8d, 0x20207050
00A07EF9  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00A07EFD  89 55 8B                        mov dword ptr [rbp - 0x75], edx
00A07F00  8D 4A 56                        lea ecx, [rdx + 0x56]
00A07F03  E8 E8 A1 17 00                  call 0x140b820f0
00A07F08  48 8B F0                        mov rsi, rax
00A07F0B  48 85 C0                        test rax, rax
00A07F0E  0F 85 98 00 00 00               jne 0x140a07fac
00A07F14  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A07F19  48 85 FF                        test rdi, rdi
00A07F1C  74 0B                           je 0x140a07f29
00A07F1E  49 8B D6                        mov rdx, r14
00A07F21  48 8B CF                        mov rcx, rdi
00A07F24  E8 C7 DA EE FF                  call 0x1408f59f0
00A07F29  48 85 F6                        test rsi, rsi
00A07F2C  74 0A                           je 0x140a07f38
00A07F2E  33 D2                           xor edx, edx
00A07F30  48 8B CE                        mov rcx, rsi
00A07F33  E8 38 A9 17 00                  call 0x140b82870
00A07F38  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00A07F3C  48 85 C9                        test rcx, rcx
00A07F3F  74 05                           je 0x140a07f46
00A07F41  E8 6A 53 CA FF                  call 0x1406ad2b0
00A07F46  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00A07F4A  48 85 C9                        test rcx, rcx
00A07F4D  74 05                           je 0x140a07f54
00A07F4F  E8 5C 53 CA FF                  call 0x1406ad2b0
00A07F54  8B C3                           mov eax, ebx
00A07F56  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00A07F5A  48 33 CC                        xor rcx, rsp
00A07F5D  E8 DE 46 CA FF                  call 0x1406ac640
00A07F62  48 8B 9C 24 48 01 00 00         mov rbx, qword ptr [rsp + 0x148]
00A07F6A  48 81 C4 00 01 00 00            add rsp, 0x100
00A07F71  41 5F                           pop r15
00A07F73  41 5E                           pop r14
00A07F75  41 5D                           pop r13
00A07F77  41 5C                           pop r12
00A07F79  5F                              pop rdi
00A07F7A  5E                              pop rsi
00A07F7B  5D                              pop rbp
00A07F7C  C3                              ret
00A07F7D  CC                              int3
00A07F7E  66 44 39 2F                     cmp word ptr [rdi], r13w
00A07F82  0F 84 96 FE FF FF               je 0x140a07e1e
00A07F88  41 B8 50 70 73 75               mov r8d, 0x75737050
00A07F8E  49 8B D1                        mov rdx, r9
00A07F91  49 8B CA                        mov rcx, r10
00A07F94  E8 57 A1 17 00                  call 0x140b820f0
00A07F99  48 8B F8                        mov rdi, rax
00A07F9C  48 85 C0                        test rax, rax
00A07F9F  0F 85 9E 02 00 00               jne 0x140a08243
00A07FA5  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A07FAA  EB A8                           jmp 0x140a07f54
00A07FAC  45 8B FD                        mov r15d, r13d
00A07FAF  4C 8D 05 3A AE 5F FF            lea r8, [rip - 0xa051c6]
00A07FB6  41 83 FF 05                     cmp r15d, 5
00A07FBA  0F 83 59 FF FF FF               jae 0x140a07f19
00A07FC0  45 8B E7                        mov r12d, r15d
00A07FC3  49 C1 E4 05                     shl r12, 5
00A07FC7  43 8A 4C 04 10                  mov cl, byte ptr [r12 + r8 + 0x10]
00A07FCC  84 C9                           test cl, cl
00A07FCE  0F 85 FC 00 00 00               jne 0x140a080d0
00A07FD4  8B 55 8B                        mov edx, dword ptr [rbp - 0x75]
00A07FD7  4B 8B 44 04 08                  mov rax, qword ptr [r12 + r8 + 8]
00A07FDC  89 55 87                        mov dword ptr [rbp - 0x79], edx
00A07FDF  84 C9                           test cl, cl
00A07FE1  0F 85 F8 00 00 00               jne 0x140a080df
00A07FE7  48 85 C0                        test rax, rax
00A07FEA  0F 84 A8 00 00 00               je 0x140a08098
00A07FF0  4C 8B 4D 9F                     mov r9, qword ptr [rbp - 0x61]
00A07FF4  48 8D 4D 87                     lea rcx, [rbp - 0x79]
00A07FF8  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
00A07FFD  41 B8 01 00 00 00               mov r8d, 1
00A08003  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00A08008  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00A0800C  48 8B D7                        mov rdx, rdi
00A0800F  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00A08014  48 8D 4D 93                     lea rcx, [rbp - 0x6d]
00A08018  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A0801D  48 8B 0D 74 E3 45 00            mov rcx, qword ptr [rip + 0x45e374]
00A08024  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A08029  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A0802E  E8 4D A1 ED FF                  call 0x1408e2180
00A08033  8B D8                           mov ebx, eax
00A08035  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A0803A  0F 84 CD 00 00 00               je 0x140a0810d
00A08040  81 FB 25 02 00 C0               cmp ebx, 0xc0000225
00A08046  75 12                           jne 0x140a0805a
00A08048  41 8B DD                        mov ebx, r13d
00A0804B  4C 8D 05 9E AD 5F FF            lea r8, [rip - 0xa05262]
00A08052  41 FF C7                        inc r15d
00A08055  E9 5C FF FF FF                  jmp 0x140a07fb6
00A0805A  85 DB                           test ebx, ebx
00A0805C  0F 88 B7 FE FF FF               js 0x140a07f19
00A08062  44 8B 45 87                     mov r8d, dword ptr [rbp - 0x79]
00A08066  48 8D 45 A7                     lea rax, [rbp - 0x59]
00A0806A  8B 4D 8F                        mov ecx, dword ptr [rbp - 0x71]
00A0806D  48 8B D6                        mov rdx, rsi
00A08070  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A08075  48 8D 05 74 AD 5F FF            lea rax, [rip - 0xa0528c]
00A0807C  45 8B CF                        mov r9d, r15d
00A0807F  49 C1 E1 05                     shl r9, 5
00A08083  4D 8B 4C 01 18                  mov r9, qword ptr [r9 + rax + 0x18]
00A08088  E8 EB 01 00 00                  call 0x140a08278
00A0808D  8B D8                           mov ebx, eax
00A0808F  85 C0                           test eax, eax
00A08091  79 B8                           jns 0x140a0804b
00A08093  E9 81 FE FF FF                  jmp 0x140a07f19
00A08098  47 8B 0C 04                     mov r9d, dword ptr [r12 + r8]
00A0809C  48 8D 45 87                     lea rax, [rbp - 0x79]
00A080A0  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
00A080A4  48 8B D7                        mov rdx, rdi
00A080A7  48 8B 0D EA E2 45 00            mov rcx, qword ptr [rip + 0x45e2ea]
00A080AE  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
00A080B3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A080B8  48 8D 45 8F                     lea rax, [rbp - 0x71]
00A080BC  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A080C1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A080C6  E8 A5 57 EE FF                  call 0x1408ed870
00A080CB  E9 63 FF FF FF                  jmp 0x140a08033
00A080D0  4C 39 6D 97                     cmp qword ptr [rbp - 0x69], r13
00A080D4  0F 85 FA FE FF FF               jne 0x140a07fd4
00A080DA  E9 73 FF FF FF                  jmp 0x140a08052
00A080DF  48 85 C0                        test rax, rax
00A080E2  0F 84 FB 00 00 00               je 0x140a081e3
00A080E8  4C 8B 4D 97                     mov r9, qword ptr [rbp - 0x69]
00A080EC  48 8D 4D 87                     lea rcx, [rbp - 0x79]
00A080F0  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
00A080F5  41 B8 02 00 00 00               mov r8d, 2
00A080FB  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00A08100  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00A08104  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00A08108  E9 02 FF FF FF                  jmp 0x140a0800f
00A0810D  33 D2                           xor edx, edx
00A0810F  48 8B CE                        mov rcx, rsi
00A08112  E8 59 A7 17 00                  call 0x140b82870
00A08117  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
00A0811A  B9 00 01 00 00                  mov ecx, 0x100
00A0811F  8B D0                           mov edx, eax
00A08121  89 45 8B                        mov dword ptr [rbp - 0x75], eax
00A08124  41 B8 50 70 20 20               mov r8d, 0x20207050
00A0812A  E8 C1 9F 17 00                  call 0x140b820f0
00A0812F  48 8B F0                        mov rsi, rax
00A08132  48 85 C0                        test rax, rax
00A08135  0F 84 D9 FD FF FF               je 0x140a07f14
00A0813B  48 8D 15 AE AC 5F FF            lea rdx, [rip - 0xa05352]
00A08142  41 8B C7                        mov eax, r15d
00A08145  49 8B 4C 14 08                  mov rcx, qword ptr [r12 + rdx + 8]
00A0814A  48 C1 E0 05                     shl rax, 5
00A0814E  45 8B CF                        mov r9d, r15d
00A08151  44 38 6C 10 10                  cmp byte ptr [rax + rdx + 0x10], r13b
00A08156  48 8D 45 87                     lea rax, [rbp - 0x79]
00A0815A  0F 85 F4 00 00 00               jne 0x140a08254
00A08160  48 85 C9                        test rcx, rcx
00A08163  74 49                           je 0x140a081ae
00A08165  4C 8B 4D 9F                     mov r9, qword ptr [rbp - 0x61]
00A08169  41 B8 01 00 00 00               mov r8d, 1
00A0816F  48 8B D7                        mov rdx, rdi
00A08172  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
00A08177  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A0817C  8B 45 8B                        mov eax, dword ptr [rbp - 0x75]
00A0817F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A08183  48 8D 45 93                     lea rax, [rbp - 0x6d]
00A08187  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00A0818C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A08191  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A08196  48 8B 0D FB E1 45 00            mov rcx, qword ptr [rip + 0x45e1fb]
00A0819D  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A081A2  E8 D9 9F ED FF                  call 0x1408e2180
00A081A7  8B D8                           mov ebx, eax
00A081A9  E9 92 FE FF FF                  jmp 0x140a08040
00A081AE  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
00A081B2  48 8B 0D DF E1 45 00            mov rcx, qword ptr [rip + 0x45e1df]
00A081B9  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
00A081BE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A081C3  48 8D 45 8F                     lea rax, [rbp - 0x71]
00A081C7  49 C1 E1 05                     shl r9, 5
00A081CB  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A081D0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A081D5  45 8B 0C 11                     mov r9d, dword ptr [r9 + rdx]
00A081D9  48 8B D7                        mov rdx, rdi
00A081DC  E8 8F 56 EE FF                  call 0x1408ed870
00A081E1  EB C4                           jmp 0x140a081a7
00A081E3  47 8B 0C 04                     mov r9d, dword ptr [r12 + r8]
00A081E7  48 8D 45 87                     lea rax, [rbp - 0x79]
00A081EB  4C 8B 45 97                     mov r8, qword ptr [rbp - 0x69]
00A081EF  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00A081F3  48 8B 0D 9E E1 45 00            mov rcx, qword ptr [rip + 0x45e19e]
00A081FA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A081FF  48 8D 45 8F                     lea rax, [rbp - 0x71]
00A08203  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A08208  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0820D  E8 2E C7 F8 FF                  call 0x140994940
00A08212  E9 1C FE FF FF                  jmp 0x140a08033
00A08217  48 8B C1                        mov rax, rcx
00A0821A  48 D1 E8                        shr rax, 1
00A0821D  66 44 39 6C 47 FE               cmp word ptr [rdi + rax*2 - 2], r13w
00A08223  0F 84 F5 FB FF FF               je 0x140a07e1e
00A08229  66 44 39 2C 47                  cmp word ptr [rdi + rax*2], r13w
00A0822E  0F 85 B0 FB FF FF               jne 0x140a07de4
00A08234  E9 E5 FB FF FF                  jmp 0x140a07e1e
00A08239  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A0823E  E9 11 FD FF FF                  jmp 0x140a07f54
00A08243  66 44 89 28                     mov word ptr [rax], r13w
00A08247  E9 D2 FB FF FF                  jmp 0x140a07e1e
00A0824C  49 8B FD                        mov rdi, r13
00A0824F  E9 CA FB FF FF                  jmp 0x140a07e1e
00A08254  48 85 C9                        test rcx, rcx
00A08257  0F 84 95 C4 12 00               je 0x140b346f2
00A0825D  4C 8B 4D 97                     mov r9, qword ptr [rbp - 0x69]
00A08261  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00A08265  41 B8 02 00 00 00               mov r8d, 2
00A0826B  E9 02 FF FF FF                  jmp 0x140a08172
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpForEachDeviceInstanceDriver(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int8 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 4205041)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r13 = 0;
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_mD4 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mCC = 0;
    if (a1 == 0) goto loc_00A08239;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) < ((unsigned __int16)(v_r13 + 2))) goto loc_00A0824C;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A0824C;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) > ((unsigned __int16)(*(unsigned __int16 *)(a1 + 2)))) goto loc_00A08239;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) == 0) goto loc_00A07F7E;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8))) == 0) goto loc_00A07E1E;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) != ((unsigned __int16)(*(unsigned __int16 *)(a1 + 2)))) goto loc_00A07DD5;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1)))) >> (1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + result * 2 - 2)) == 0) goto loc_00A07E1E;
loc_00A07DD5:
    result = (*(unsigned __int16 *)(a1 + 2)) - (v_r13 + 2);
    if ((*(unsigned __int16 *)(a1)) <= result) goto loc_00A08217;
loc_00A07DE4:
    result = ExAllocatePool2(256, *(unsigned __int16 *)(a1) + 2, (unsigned int)(0x75737050ULL), v_r13 + 2);
    if (result == 0) goto loc_00A07FA5;
    result = memcpy(result, *(unsigned __int64 *)(a1 + 8), *(unsigned __int16 *)(a1), v_r13 + 2);
    result = (*(unsigned __int16 *)(a1)) >> (1);
    *(unsigned __int16 *)(result + result * 2) = 0;
loc_00A07E1E:
    v_stack_m100 = 0;
    a4 = 0;
    v_stack_m108 = v_stack_mC0;
    v_stack_m110 = 0;
    v_stack_m118 = (unsigned int)((unsigned int)(0x20019ULL));
    result = _CmOpenDeviceRegKey(*(unsigned __int64 *)(v_rip + 4580723), result, a4 + 16, a4);
    if (sign_flag) goto loc_00A07F19;
    v_stack_m100 = 0;
    v_stack_m108 = v_stack_mD4;
    v_stack_m110 = v_stack_m98;
    v_stack_m118 = v_stack_mD0;
    v_stack_mD4 = 78;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4580653), result, v_stack_mC0, 9);
    if (sign_flag) goto loc_00A07EDF;
    if (v_stack_mD0 != 1) goto loc_00A07EDF;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (v_stack_mD4 != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 4580579);
        result = v_stack_mC8;
        v_stack_m100 = 0;
        a2 = v_stack_m98;
        v_stack_m108 = result;
        a4 = 0;
        v_stack_m110 = 0;
        v_stack_m118 = (unsigned int)((unsigned int)(0x20019ULL));
        a3 = a4 + 32;
        result = CmOpenCommonClassRegKey(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    v_stack_mA8 = a3;
    v_stack_mB8 = a1;
    v_stack_mB0 = v_rip - 457151;
    v_stack_mD4 = 170;
    result = ExAllocatePool2(170 + 86, 170, (unsigned int)(0x20207050ULL), a4);
    if (result != 0) goto loc_00A07FAC;
loc_00A07F14:
loc_00A07F19:
    if (result != 0) {
        a2 = a1;
        a1 = result;
        result = PnpUnicodeStringToWstrFree(a1, a2, (unsigned int)(0x20207050ULL), a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x20207050ULL), a4);
    }
    if (v_stack_mC8 != 0) {
        result = ZwClose(v_stack_mC8, a2, (unsigned int)(0x20207050ULL), a4);
    }
    if (v_stack_mC0 != 0) {
        result = ZwClose(v_stack_mC0, a2, (unsigned int)(0x20207050ULL), a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x20207050ULL), a4);
    v_rsp = (v_rsp) + (256);
    return result;
loc_00A07F7E:
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_00A07E1E;
    result = ExAllocatePool2(256, 0, (unsigned int)(0x75737050ULL), a4);
    if (result != 0) goto loc_00A08243;
loc_00A07FA5:
    goto loc_00A07F54;
loc_00A07FAC:
loc_00A07FB6:
    if (0 >= 5) goto loc_00A07F19;
    v_r12 = (0) << (5);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + v_rip - 10506694 * 1 + 16)) != 0) goto loc_00A080D0;
loc_00A07FD4:
    v_stack_mD8 = (unsigned int)((unsigned int)(v_stack_mD4));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r12 + v_rip - 10506694 * 1 + 16)) != 0) goto loc_00A080DF;
    if (*(unsigned __int64 *)(v_r12 + v_rip - 10506694 * 1 + 8) == 0) goto loc_00A08098;
    v_stack_p50 = 0;
    v_stack_p48 = v_stack_mD8;
    v_stack_p40 = (unsigned int)((unsigned int)(v_stack_mD4));
loc_00A0800F:
    v_stack_p38 = result;
    v_stack_p30 = v_stack_mCC;
    v_stack_p28 = *(unsigned __int64 *)(v_r12 + v_rip - 10506694 * 1 + 8);
    v_stack_p20 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4580212), result, 1, v_stack_mC0);
loc_00A08033:
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00A0810D;
loc_00A08040:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000225ULL) goto loc_00A0805A;
loc_00A0804B:
loc_00A08052:
    v_r15 = (unsigned int)((0) + 1);
    goto loc_00A07FB6;
loc_00A0805A:
    if (sign_flag) goto loc_00A07F19;
    v_stack_p20 = v_stack_mB8;
    a4 = ((unsigned int)((unsigned int)(v_r15))) << (5);
    result = PiForEachDriverQueryRoutine((unsigned int)(v_stack_mD0), result, (unsigned int)(v_stack_mD8), *(unsigned __int64 *)(a4 + v_rip - 10506892 * 1 + 24));
    if (!sign_flag) goto loc_00A0804B;
    goto loc_00A07F19;
loc_00A08098:
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_mD8;
    v_stack_p28 = result;
    v_stack_p20 = v_stack_mD0;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4580074), result, v_stack_mC0, (unsigned int)(*(unsigned int *)(v_r12 + (unsigned int)(v_stack_mD8) * 1)));
    goto loc_00A08033;
loc_00A080D0:
    if (v_stack_mC8 != 0) goto loc_00A07FD4;
    goto loc_00A08052;
loc_00A080DF:
    if (result == 0) goto loc_00A081E3;
    v_stack_p50 = 0;
    v_stack_p48 = v_stack_mD8;
    v_stack_p40 = (unsigned int)(result);
    goto loc_00A0800F;
loc_00A0810D:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 2, v_stack_mC8);
    v_stack_mD4 = (unsigned int)((unsigned int)(v_stack_mD8));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD8))), (unsigned int)(0x20207050ULL), v_stack_mC8);
    if (result == 0) goto loc_00A07F14;
    result = ((unsigned int)((unsigned int)(v_r15))) << (5);
    if ((*(unsigned __int8 *)(result + v_rip - 10507090 * 1 + 16)) != 0) goto loc_00A08254;
    if (*(unsigned __int64 *)(v_r12 + v_rip - 10507090 * 1 + 8) == 0) goto loc_00A081AE;
loc_00A08172:
    v_stack_p50 = 0;
    v_stack_p48 = v_stack_mD8;
    v_stack_p40 = (unsigned int)((unsigned int)(v_stack_mD4));
    v_stack_p38 = result;
    v_stack_p30 = v_stack_mCC;
    v_stack_p28 = *(unsigned __int64 *)(v_r12 + v_rip - 10507090 * 1 + 8);
    v_stack_p20 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4579835), result, 1, v_stack_mC0);
loc_00A081A7:
    goto loc_00A08040;
loc_00A081AE:
    v_stack_p38 = 0;
    v_stack_p30 = result;
    a4 = (v_stack_mC0) << (5);
    v_stack_p28 = result;
    v_stack_p20 = v_stack_mD0;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4579807), result, v_stack_mC0, (unsigned int)(*(unsigned int *)(a4 + result * 1)));
    goto loc_00A081A7;
loc_00A081E3:
    v_stack_p30 = v_stack_mD8;
    v_stack_p28 = result;
    v_stack_p20 = v_stack_mD0;
    result = CmGetInstallerClassRegProp(*(unsigned __int64 *)(v_rip + 4579742), v_stack_m98, v_stack_mC8, (unsigned int)(*(unsigned int *)(v_r12 + v_stack_mC0 * 1)));
    goto loc_00A08033;
loc_00A08217:
    result = (*(unsigned __int64 *)(v_rip + 4579742)) >> (1);
    if ((*(unsigned __int16 *)(result + result * 2 - 2)) == 0) goto loc_00A07E1E;
    if ((*(unsigned __int16 *)(result + result * 2)) != 0) goto loc_00A07DE4;
    goto loc_00A07E1E;
loc_00A08239:
    goto loc_00A07F54;
loc_00A08243:
    *(unsigned __int16 *)(result) = 0;
    goto loc_00A07E1E;
loc_00A0824C:
    goto loc_00A07E1E;
loc_00A08254:
    goto loc_00A08172;
}
```

## 5. (Beta) C Style

```c
int64_t PpForEachDeviceInstanceDriver(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint8_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m48;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x4029F1)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r13 = 0;
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_mD4 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mCC = 0;
    if (Arg1 == NULL) goto loc_00A08239;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x2))) < ((uint16_t)(local_r13 + 2))) goto loc_00A0824C;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A0824C;
    if (((uint16_t)(*(uint16_t *)(arg1))) > ((uint16_t)(*(uint16_t *)(arg1 + 0x2)))) goto loc_00A08239;
    if ((uint16_t)(*(uint16_t *)(arg1)) == 0) goto loc_00A07F7E;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8))) == 0) goto loc_00A07E1E;
    if (((uint16_t)(*(uint16_t *)(arg1))) != ((uint16_t)(*(uint16_t *)(arg1 + 0x2)))) goto loc_00A07DD5;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1)))) >> (1);
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + result * 2 - 0x2)) == 0) goto loc_00A07E1E;
loc_00A07DD5:
    result = (*(uint16_t *)(arg1 + 0x2)) - (local_r13 + 2);
    if ((*(uint16_t *)(arg1)) <= result) goto loc_00A08217;
loc_00A07DE4:
    result = ExAllocatePool2(256, *(uint16_t *)(arg1) + 2, (uint32_t)(0x75737050ULL), local_r13 + 2);
    if (result == 0) goto loc_00A07FA5;
    result = memcpy(result, *(uint64_t *)(arg1 + 0x8), *(uint16_t *)(arg1), local_r13 + 2);
    result = (*(uint16_t *)(arg1)) >> (1);
    *(uint16_t *)(result + result * 2) = 0;
loc_00A07E1E:
    v_stack_m100 = 0;
    a4 = 0;
    v_stack_m108 = v_stack_mC0;
    v_stack_m110 = 0;
    v_stack_m118 = (uint32_t)((uint32_t)(0x20019ULL));
    result = _CmOpenDeviceRegKey(*(uint64_t *)(v_rip + 0x45E573), result, a4 + 16, a4);
    if (sign_flag) goto loc_00A07F19;
    v_stack_m100 = 0;
    v_stack_m108 = v_stack_mD4;
    v_stack_m110 = v_stack_m98;
    v_stack_m118 = v_stack_mD0;
    v_stack_mD4 = 78;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x45E52D), result, v_stack_mC0, 9);
    if (sign_flag) goto loc_00A07EDF;
    if (v_stack_mD0 != 1) goto loc_00A07EDF;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (v_stack_mD4 != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x45E4E3);
        result = v_stack_mC8;
        v_stack_m100 = 0;
        Arg2 = v_stack_m98;
        v_stack_m108 = result;
        a4 = 0;
        v_stack_m110 = 0;
        v_stack_m118 = (uint32_t)((uint32_t)(0x20019ULL));
        Arg3 = a4 + 32;
        result = CmOpenCommonClassRegKey(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    v_stack_mA8 = Arg3;
    v_stack_mB8 = Arg1;
    v_stack_mB0 = v_rip - 457151;
    v_stack_mD4 = 170;
    result = ExAllocatePool2(170 + 86, 170, (uint32_t)(0x20207050ULL), a4);
    if (result != 0) goto loc_00A07FAC;
loc_00A07F14:
loc_00A07F19:
    if (result != 0) {
        Arg2 = Arg1;
        Arg1 = result;
        result = PnpUnicodeStringToWstrFree(Arg1, Arg2, (uint32_t)(0x20207050ULL), a4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x20207050ULL), a4);
    }
    if (v_stack_mC8 != 0) {
        result = ZwClose(v_stack_mC8, Arg2, (uint32_t)(0x20207050ULL), a4);
    }
    if (v_stack_mC0 != 0) {
        result = ZwClose(v_stack_mC0, Arg2, (uint32_t)(0x20207050ULL), a4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x20207050ULL), a4);
    local_rsp = (local_rsp) + (256);
    return result;
loc_00A07F7E:
    if ((*(uint16_t *)(result)) == 0) goto loc_00A07E1E;
    result = ExAllocatePool2(256, 0, (uint32_t)(0x75737050ULL), a4);
    if (result != 0) goto loc_00A08243;
loc_00A07FA5:
    goto loc_00A07F54;
loc_00A07FAC:
loc_00A07FB6:
    if (0 >= 5) goto loc_00A07F19;
    local_r12 = (0) << (5);
    if ((uint8_t)(*(uint8_t *)(local_r12 + v_rip - 0xA051C6 * 1 + 0x10)) != 0) goto loc_00A080D0;
loc_00A07FD4:
    v_stack_mD8 = (uint32_t)((uint32_t)(v_stack_mD4));
    if ((uint8_t)(*(uint8_t *)(local_r12 + v_rip - 0xA051C6 * 1 + 0x10)) != 0) goto loc_00A080DF;
    if (*(uint64_t *)(local_r12 + v_rip - 0xA051C6 * 1 + 0x8) == 0) goto loc_00A08098;
    v_stack_p50 = 0;
    v_stack_p48 = v_stack_mD8;
    v_stack_p40 = (uint32_t)((uint32_t)(v_stack_mD4));
loc_00A0800F:
    v_stack_p38 = result;
    v_stack_p30 = v_stack_mCC;
    v_stack_p28 = *(uint64_t *)(local_r12 + v_rip - 0xA051C6 * 1 + 0x8);
    v_stack_p20 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x45E374), result, 1, v_stack_mC0);
loc_00A08033:
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00A0810D;
loc_00A08040:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000225ULL) goto loc_00A0805A;
loc_00A0804B:
loc_00A08052:
    local_r15 = (uint32_t)((0) + 1);
    goto loc_00A07FB6;
loc_00A0805A:
    if (sign_flag) goto loc_00A07F19;
    v_stack_p20 = v_stack_mB8;
    a4 = ((uint32_t)((uint32_t)(local_r15))) << (5);
    result = PiForEachDriverQueryRoutine((uint32_t)(v_stack_mD0), result, (uint32_t)(v_stack_mD8), *(uint64_t *)(a4 + v_rip - 0xA0528C * 1 + 0x18));
    if (!sign_flag) goto loc_00A0804B;
    goto loc_00A07F19;
loc_00A08098:
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_mD8;
    v_stack_p28 = result;
    v_stack_p20 = v_stack_mD0;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x45E2EA), result, v_stack_mC0, (uint32_t)(*(uint32_t *)(local_r12 + (uint32_t)(v_stack_mD8) * 1)));
    goto loc_00A08033;
loc_00A080D0:
    if (v_stack_mC8 != 0) goto loc_00A07FD4;
    goto loc_00A08052;
loc_00A080DF:
    if (result == 0) goto loc_00A081E3;
    v_stack_p50 = 0;
    v_stack_p48 = v_stack_mD8;
    v_stack_p40 = (uint32_t)(result);
    goto loc_00A0800F;
loc_00A0810D:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 2, v_stack_mC8);
    v_stack_mD4 = (uint32_t)((uint32_t)(v_stack_mD8));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD8))), (uint32_t)(0x20207050ULL), v_stack_mC8);
    if (result == 0) goto loc_00A07F14;
    result = ((uint32_t)((uint32_t)(local_r15))) << (5);
    if ((*(uint8_t *)(result + v_rip - 0xA05352 * 1 + 0x10)) != 0) goto loc_00A08254;
    if (*(uint64_t *)(local_r12 + v_rip - 0xA05352 * 1 + 0x8) == 0) goto loc_00A081AE;
loc_00A08172:
    v_stack_p50 = 0;
    v_stack_p48 = v_stack_mD8;
    v_stack_p40 = (uint32_t)((uint32_t)(v_stack_mD4));
    v_stack_p38 = result;
    v_stack_p30 = v_stack_mCC;
    v_stack_p28 = *(uint64_t *)(local_r12 + v_rip - 0xA05352 * 1 + 0x8);
    v_stack_p20 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x45E1FB), result, 1, v_stack_mC0);
loc_00A081A7:
    goto loc_00A08040;
loc_00A081AE:
    v_stack_p38 = 0;
    v_stack_p30 = result;
    a4 = (v_stack_mC0) << (5);
    v_stack_p28 = result;
    v_stack_p20 = v_stack_mD0;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x45E1DF), result, v_stack_mC0, (uint32_t)(*(uint32_t *)(a4 + result * 1)));
    goto loc_00A081A7;
loc_00A081E3:
    v_stack_p30 = v_stack_mD8;
    v_stack_p28 = result;
    v_stack_p20 = v_stack_mD0;
    result = CmGetInstallerClassRegProp(*(uint64_t *)(v_rip + 0x45E19E), v_stack_m98, v_stack_mC8, (uint32_t)(*(uint32_t *)(local_r12 + v_stack_mC0 * 1)));
    goto loc_00A08033;
loc_00A08217:
    result = (*(uint64_t *)(v_rip + 0x45E19E)) >> (1);
    if ((*(uint16_t *)(result + result * 2 - 0x2)) == 0) goto loc_00A07E1E;
    if ((*(uint16_t *)(result + result * 2)) != 0) goto loc_00A07DE4;
    goto loc_00A07E1E;
loc_00A08239:
    goto loc_00A07F54;
loc_00A08243:
    *(uint16_t *)(result) = 0;
    goto loc_00A07E1E;
loc_00A0824C:
    goto loc_00A07E1E;
loc_00A08254:
    goto loc_00A08172;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A07D2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
