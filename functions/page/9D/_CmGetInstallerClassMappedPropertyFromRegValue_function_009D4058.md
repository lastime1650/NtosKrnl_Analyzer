# _CmGetInstallerClassMappedPropertyFromRegValue

- RVA: `0x009D4058`–`0x009D446B` (길이 `1,043` bytes)
- VA: `0x00000001409D4058`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A1628`
- 디코드: `252`개 명령, `1,043/1,043` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x009D4144` → [CmOpenCommonClassRegKey](../8E/CmOpenCommonClassRegKey_function_008EFF5C.md) (function, `0x008EFF5C`)
- `0x009D41D5` → [PnpRegQueryValueIndirect](../8E/PnpRegQueryValueIndirect_function_008EE210.md) (function, `0x008EE210`)
- `0x009D4287` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x009D42B2` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009D42C0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009D4360` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009D440B` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x009D4461` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [CmGetInstallerClassMappedPropertyKeys](../83/CmGetInstallerClassMappedPropertyKeys_function_00830704.md) at `0x00830865`
- [CmGetInstallerClassMappedProperty](CmGetInstallerClassMappedProperty_function_009D3764.md) at `0x009D3898`

### Static image references
- `0x009D4074` → RVA `0x00E0A740` (`.data`; read)
- `0x009D40A0` → RVA `0x00B4D320` (`PAGE`; read)
- `0x009D423E` → RVA `0x00014350` (`.rdata`; read)
- `0x009D424B` → RVA `0x00014358` (`.rdata`; read)
- `0x009D4304` → RVA `0x00014398` (`.rdata`; read)
- `0x009D4311` → RVA `0x000143A0` (`.rdata`; read)
- `0x009D4335` → RVA `0x008EE210` (`PnpRegQueryValueIndirect`; read)
- `0x009D436D` → RVA `0x00027DA0` (`.rdata`; read)
- `0x009D437E` → RVA `0x00027DA8` (`.rdata`; read)
- `0x009D438D` → RVA `0x00027D10` (`.rdata`; read)
- `0x009D439E` → RVA `0x00027D18` (`.rdata`; read)
- `0x009D43AD` → RVA `0x00021EF0` (`.rdata`; read)
- `0x009D43BE` → RVA `0x00021EF8` (`.rdata`; read)
- `0x009D4404` → RVA `0x00B06E20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009D4419` → RVA `0x00014380` (`.rdata`; read)
- `0x009D442A` → RVA `0x00014388` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x009D42B2` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009D42C0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009D4360` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009D440B` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x009D4461` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x009D4374` → [sub_00B2F7FC](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D4385` → [sub_00B2F7FC](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D4394` → [sub_00B2F7FC + 0xE](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D43A5` → [sub_00B2F7FC + 0xE](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D43B4` → [sub_00B2F7FC + 0x1C](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D43C5` → [sub_00B2F7FC + 0x1C](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D43DA` → [sub_00B2F7FC + 0x2A](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D43F5` → [sub_00B2F7FC + 0x31](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D4411` → [sub_00B2F7FC + 0x3E](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D4420` → [sub_00B2F7FC + 0x4B](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)
  - `0x009D4431` → [sub_00B2F7FC + 0x4B](../B2/Unknown_function_00B2F7FC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009D4058  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009D405D  55                              push rbp
009D405E  56                              push rsi
009D405F  57                              push rdi
009D4060  41 54                           push r12
009D4062  41 55                           push r13
009D4064  41 56                           push r14
009D4066  41 57                           push r15
009D4068  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
009D406D  48 81 EC B0 00 00 00            sub rsp, 0xb0
009D4074  48 8B 05 C5 66 43 00            mov rax, qword ptr [rip + 0x4366c5]
009D407B  48 33 C4                        xor rax, rsp
009D407E  48 89 45 F7                     mov qword ptr [rbp - 9], rax
009D4082  4C 8B 75 7F                     mov r14, qword ptr [rbp + 0x7f]
009D4086  33 C0                           xor eax, eax
009D4088  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
009D408C  49 8B F9                        mov rdi, r9
009D408F  4C 8B 6D 6F                     mov r13, qword ptr [rbp + 0x6f]
009D4093  4D 8B D0                        mov r10, r8
009D4096  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
009D409A  8B D8                           mov ebx, eax
009D409C  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
009D40A0  48 8D 15 79 92 17 00            lea rdx, [rip + 0x179279]
009D40A7  44 8B 5F 10                     mov r11d, dword ptr [rdi + 0x10]
009D40AB  44 8B F8                        mov r15d, eax
009D40AE  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
009D40B2  44 8B C8                        mov r9d, eax
009D40B5  4C 89 75 BF                     mov qword ptr [rbp - 0x41], r14
009D40B9  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
009D40BD  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
009D40C1  89 45 9F                        mov dword ptr [rbp - 0x61], eax
009D40C4  89 45 9B                        mov dword ptr [rbp - 0x65], eax
009D40C7  88 45 97                        mov byte ptr [rbp - 0x69], al
009D40CA  89 45 AF                        mov dword ptr [rbp - 0x51], eax
009D40CD  4C 8B 02                        mov r8, qword ptr [rdx]
009D40D0  48 8B F2                        mov rsi, rdx
009D40D3  45 3B 58 10                     cmp r11d, dword ptr [r8 + 0x10]
009D40D7  0F 84 04 02 00 00               je 0x1409d42e1
009D40DD  41 FF C1                        inc r9d
009D40E0  48 83 C2 20                     add rdx, 0x20
009D40E4  48 8B F0                        mov rsi, rax
009D40E7  41 83 F9 0D                     cmp r9d, 0xd
009D40EB  72 E0                           jb 0x1409d40cd
009D40ED  45 33 C9                        xor r9d, r9d
009D40F0  48 85 F6                        test rsi, rsi
009D40F3  0F 84 35 02 00 00               je 0x1409d432e
009D40F9  45 89 0C 24                     mov dword ptr [r12], r9d
009D40FD  45 89 0E                        mov dword ptr [r14], r9d
009D4100  4D 85 ED                        test r13, r13
009D4103  0F 84 1D 02 00 00               je 0x1409d4326
009D4109  44 8B 75 77                     mov r14d, dword ptr [rbp + 0x77]
009D410D  41 8B C6                        mov eax, r14d
009D4110  F7 D8                           neg eax
009D4112  48 1B C9                        sbb rcx, rcx
009D4115  4C 23 E9                        and r13, rcx
009D4118  4D 85 D2                        test r10, r10
009D411B  75 3D                           jne 0x1409d415a
009D411D  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
009D4121  48 8D 45 A7                     lea rax, [rbp - 0x59]
009D4125  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
009D4129  45 8D 42 20                     lea r8d, [r10 + 0x20]
009D412D  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
009D4132  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D4137  44 88 4C 24 28                  mov byte ptr [rsp + 0x28], r9b
009D413C  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
009D4144  E8 13 BE F1 FF                  call 0x1408eff5c
009D4149  8B D8                           mov ebx, eax
009D414B  45 33 C9                        xor r9d, r9d
009D414E  85 C0                           test eax, eax
009D4150  0F 88 46 01 00 00               js 0x1409d429c
009D4156  4C 8B 55 CF                     mov r10, qword ptr [rbp - 0x31]
009D415A  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
009D415D  83 F9 07                        cmp ecx, 7
009D4160  0F 84 D5 00 00 00               je 0x1409d423b
009D4166  83 F9 08                        cmp ecx, 8
009D4169  0F 84 FB 01 00 00               je 0x1409d436a
009D416F  83 F9 09                        cmp ecx, 9
009D4172  0F 84 12 02 00 00               je 0x1409d438a
009D4178  83 F9 0A                        cmp ecx, 0xa
009D417B  0F 84 80 01 00 00               je 0x1409d4301
009D4181  83 F9 0F                        cmp ecx, 0xf
009D4184  0F 84 20 02 00 00               je 0x1409d43aa
009D418A  83 F9 02                        cmp ecx, 2
009D418D  0F 84 83 02 00 00               je 0x1409d4416
009D4193  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
009D4197  4D 85 D2                        test r10, r10
009D419A  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
009D419E  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
009D41A2  49 0F 45 D2                     cmovne rdx, r10
009D41A6  44 89 75 9B                     mov dword ptr [rbp - 0x65], r14d
009D41AA  48 8B 81 08 02 00 00            mov rax, qword ptr [rcx + 0x208]
009D41B1  48 85 C0                        test rax, rax
009D41B4  0F 85 7B 01 00 00               jne 0x1409d4335
009D41BA  48 8D 45 97                     lea rax, [rbp - 0x69]
009D41BE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D41C3  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
009D41C7  48 8D 45 9B                     lea rax, [rbp - 0x65]
009D41CB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D41D0  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
009D41D5  E8 36 A0 F1 FF                  call 0x1408ee210
009D41DA  8B C8                           mov ecx, eax
009D41DC  3D 34 00 00 C0                  cmp eax, 0xc0000034
009D41E1  0F 84 B0 00 00 00               je 0x1409d4297
009D41E7  3D 7C 01 00 C0                  cmp eax, 0xc000017c
009D41EC  0F 84 A5 00 00 00               je 0x1409d4297
009D41F2  45 33 C9                        xor r9d, r9d
009D41F5  85 C0                           test eax, eax
009D41F7  0F 85 47 02 00 00               jne 0x1409d4444
009D41FD  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
009D4200  39 45 9F                        cmp dword ptr [rbp - 0x61], eax
009D4203  0F 85 4E 02 00 00               jne 0x1409d4457
009D4209  85 C9                           test ecx, ecx
009D420B  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
009D420E  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
009D4212  89 02                           mov dword ptr [rdx], eax
009D4214  8B 46 08                        mov eax, dword ptr [rsi + 8]
009D4217  41 89 04 24                     mov dword ptr [r12], eax
009D421B  0F 84 15 02 00 00               je 0x1409d4436
009D4221  BB 23 00 00 C0                  mov ebx, 0xc0000023
009D4226  83 F8 12                        cmp eax, 0x12
009D4229  75 71                           jne 0x1409d429c
009D422B  44 38 4D 97                     cmp byte ptr [rbp - 0x69], r9b
009D422F  74 6B                           je 0x1409d429c
009D4231  41 C7 04 24 19 00 00 00         mov dword ptr [r12], 0x19
009D4239  EB 61                           jmp 0x1409d429c
009D423B  48 8B 07                        mov rax, qword ptr [rdi]
009D423E  48 2B 05 0B 01 64 FF            sub rax, qword ptr [rip - 0x9bfef5]
009D4245  75 0B                           jne 0x1409d4252
009D4247  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D424B  48 2B 05 06 01 64 FF            sub rax, qword ptr [rip - 0x9bfefa]
009D4252  48 85 C0                        test rax, rax
009D4255  0F 85 0B FF FF FF               jne 0x1409d4166
009D425B  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
009D425F  48 8D 45 9B                     lea rax, [rbp - 0x65]
009D4263  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
009D4267  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
009D426B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009D4270  4D 85 D2                        test r10, r10
009D4273  48 8D 45 DF                     lea rax, [rbp - 0x21]
009D4277  C7 45 9B 16 00 00 00            mov dword ptr [rbp - 0x65], 0x16
009D427E  49 0F 45 D2                     cmovne rdx, r10
009D4282  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009D4287  E8 70 FE FB FF                  call 0x1409940fc
009D428C  3D 34 00 00 C0                  cmp eax, 0xc0000034
009D4291  0F 85 33 01 00 00               jne 0x1409d43ca
009D4297  BB 25 02 00 C0                  mov ebx, 0xc0000225
009D429C  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
009D42A0  48 85 C9                        test rcx, rcx
009D42A3  0F 85 B8 01 00 00               jne 0x1409d4461
009D42A9  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
009D42AD  48 85 C9                        test rcx, rcx
009D42B0  74 05                           je 0x1409d42b7
009D42B2  E8 F9 8F CD FF                  call 0x1406ad2b0
009D42B7  8B C3                           mov eax, ebx
009D42B9  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
009D42BD  48 33 CC                        xor rcx, rsp
009D42C0  E8 7B 83 CD FF                  call 0x1406ac640
009D42C5  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
009D42CD  48 81 C4 B0 00 00 00            add rsp, 0xb0
009D42D4  41 5F                           pop r15
009D42D6  41 5E                           pop r14
009D42D8  41 5D                           pop r13
009D42DA  41 5C                           pop r12
009D42DC  5F                              pop rdi
009D42DD  5E                              pop rsi
009D42DE  5D                              pop rbp
009D42DF  C3                              ret
009D42E0  CC                              int3
009D42E1  48 8B 0F                        mov rcx, qword ptr [rdi]
009D42E4  49 2B 08                        sub rcx, qword ptr [r8]
009D42E7  75 08                           jne 0x1409d42f1
009D42E9  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009D42ED  49 2B 48 08                     sub rcx, qword ptr [r8 + 8]
009D42F1  33 C0                           xor eax, eax
009D42F3  48 85 C9                        test rcx, rcx
009D42F6  0F 84 F1 FD FF FF               je 0x1409d40ed
009D42FC  E9 DC FD FF FF                  jmp 0x1409d40dd
009D4301  48 8B 07                        mov rax, qword ptr [rdi]
009D4304  48 2B 05 8D 00 64 FF            sub rax, qword ptr [rip - 0x9bff73]
009D430B  75 0B                           jne 0x1409d4318
009D430D  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D4311  48 2B 05 88 00 64 FF            sub rax, qword ptr [rip - 0x9bff78]
009D4318  48 85 C0                        test rax, rax
009D431B  0F 85 60 FE FF FF               jne 0x1409d4181
009D4321  E9 35 FF FF FF                  jmp 0x1409d425b
009D4326  45 8B F1                        mov r14d, r9d
009D4329  E9 EA FD FF FF                  jmp 0x1409d4118
009D432E  BB 16 00 00 C0                  mov ebx, 0xc0000016
009D4333  EB 82                           jmp 0x1409d42b7
009D4335  4C 8D 0D D4 9E F1 FF            lea r9, [rip - 0xe612c]
009D433C  49 3B C1                        cmp rax, r9
009D433F  0F 84 75 FE FF FF               je 0x1409d41ba
009D4345  4C 8D 4D 97                     lea r9, [rbp - 0x69]
009D4349  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
009D434E  4C 8D 4D 9B                     lea r9, [rbp - 0x65]
009D4352  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
009D4357  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
009D435B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
009D4360  E8 6B 67 CE FF                  call 0x1406baad0
009D4365  E9 70 FE FF FF                  jmp 0x1409d41da
009D436A  48 8B 07                        mov rax, qword ptr [rdi]
009D436D  48 2B 05 2C 3A 65 FF            sub rax, qword ptr [rip - 0x9ac5d4]
009D4374  0F 85 82 B4 15 00               jne 0x140b2f7fc
009D437A  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D437E  48 2B 05 23 3A 65 FF            sub rax, qword ptr [rip - 0x9ac5dd]
009D4385  E9 72 B4 15 00                  jmp 0x140b2f7fc
009D438A  48 8B 07                        mov rax, qword ptr [rdi]
009D438D  48 2B 05 7C 39 65 FF            sub rax, qword ptr [rip - 0x9ac684]
009D4394  0F 85 70 B4 15 00               jne 0x140b2f80a
009D439A  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D439E  48 2B 05 73 39 65 FF            sub rax, qword ptr [rip - 0x9ac68d]
009D43A5  E9 60 B4 15 00                  jmp 0x140b2f80a
009D43AA  48 8B 07                        mov rax, qword ptr [rdi]
009D43AD  48 2B 05 3C DB 64 FF            sub rax, qword ptr [rip - 0x9b24c4]
009D43B4  0F 85 5E B4 15 00               jne 0x140b2f818
009D43BA  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D43BE  48 2B 05 33 DB 64 FF            sub rax, qword ptr [rip - 0x9b24cd]
009D43C5  E9 4E B4 15 00                  jmp 0x140b2f818
009D43CA  3D 7C 01 00 C0                  cmp eax, 0xc000017c
009D43CF  0F 84 C2 FE FF FF               je 0x1409d4297
009D43D5  45 33 C9                        xor r9d, r9d
009D43D8  85 C0                           test eax, eax
009D43DA  0F 88 46 B4 15 00               js 0x140b2f826
009D43E0  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
009D43E4  C7 02 01 00 00 00               mov dword ptr [rdx], 1
009D43EA  8B 46 08                        mov eax, dword ptr [rsi + 8]
009D43ED  41 89 04 24                     mov dword ptr [r12], eax
009D43F1  41 83 FE 01                     cmp r14d, 1
009D43F5  0F 82 32 B4 15 00               jb 0x140b2f82d
009D43FB  48 8D 55 DF                     lea rdx, [rbp - 0x21]
009D43FF  66 44 89 4D F3                  mov word ptr [rbp - 0xd], r9w
009D4404  48 8D 0D 15 2A 13 00            lea rcx, [rip + 0x132a15]
009D440B  E8 70 BC B2 FF                  call 0x140500080
009D4410  90                              nop
009D4411  E9 24 B4 15 00                  jmp 0x140b2f83a
009D4416  48 8B 07                        mov rax, qword ptr [rdi]
009D4419  48 2B 05 60 FF 63 FF            sub rax, qword ptr [rip - 0x9c00a0]
009D4420  0F 85 21 B4 15 00               jne 0x140b2f847
009D4426  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009D442A  48 2B 05 57 FF 63 FF            sub rax, qword ptr [rip - 0x9c00a9]
009D4431  E9 11 B4 15 00                  jmp 0x140b2f847
009D4436  45 85 F6                        test r14d, r14d
009D4439  0F 85 E7 FD FF FF               jne 0x1409d4226
009D443F  E9 DD FD FF FF                  jmp 0x1409d4221
009D4444  81 F9 23 00 00 C0               cmp ecx, 0xc0000023
009D444A  0F 84 AD FD FF FF               je 0x1409d41fd
009D4450  8B D9                           mov ebx, ecx
009D4452  E9 45 FE FF FF                  jmp 0x1409d429c
009D4457  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009D445C  E9 3B FE FF FF                  jmp 0x1409d429c
009D4461  E8 4A 8E CD FF                  call 0x1406ad2b0
009D4466  E9 3E FE FF FF                  jmp 0x1409d42a9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _CmGetInstallerClassMappedPropertyFromRegValue(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m48;
    unsigned __int16 v_stack_m4C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int8 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 4417221)) ^ (v_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m68 = a2;
    v_stack_m70 = a3;
    v_stack_m88 = a1;
    v_stack_m80 = a8;
    v_stack_m98 = 0;
    v_stack_m78 = 0;
    v_stack_mA0 = 0;
    v_stack_mA4 = 0;
    v_stack_mA8 = 0;
    v_stack_m90 = 0;
loc_009D40CD:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 1544825) + 16))) goto loc_009D42E1;
loc_009D40DD:
    a4 = (unsigned int)((0) + 1);
    a2 = (v_rip + 1544825) + (32);
    if (((unsigned int)(a4)) < 13) goto loc_009D40CD;
loc_009D40ED:
    a4 = 0;
    if (0 == 0) goto loc_009D432E;
    *(unsigned int *)(a5) = 0;
    *(unsigned int *)(a8) = 0;
    if (a6 == 0) goto loc_009D4326;
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(a7)))));
    v_r13 = (a6) & (a1);
loc_009D4118:
    if (a3 != 0) goto loc_009D415A;
    v_stack_mB0 = 0;
    v_stack_mB8 = v_stack_m98;
    v_stack_mC0 = 0;
    v_stack_mC8 = 1;
    result = CmOpenCommonClassRegKey(v_stack_m88, v_stack_m68, a3 + 32, a4);
    a4 = 0;
    if (sign_flag) goto loc_009D429C;
loc_009D415A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 7) goto loc_009D423B;
loc_009D4166:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 8) goto loc_009D436A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 9) goto loc_009D438A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 10) goto loc_009D4301;
loc_009D4181:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 15) goto loc_009D43AA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 2) goto loc_009D4416;
    a2 = v_stack_m98;
    if (v_stack_m70 != 0) { a2 = v_stack_m70; }
    v_stack_mA4 = (unsigned int)((unsigned int)(a7));
    if (*(unsigned __int64 *)(v_stack_m88 + 520) != 0) goto loc_009D4335;
loc_009D41BA:
    v_stack_mB8 = v_stack_mA8;
    v_stack_mC0 = v_stack_mA4;
    v_stack_mC8 = v_r13;
    result = PnpRegQueryValueIndirect(v_stack_m88, a2, *(unsigned __int64 *)(0 + 16), v_stack_mA0);
loc_009D41DA:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_009D4297;
    if (((unsigned int)(result)) == 0xC000017CULL) goto loc_009D4297;
    a4 = 0;
    if ((unsigned int)(result) != 0) goto loc_009D4444;
loc_009D41FD:
    if (v_stack_mA0 != ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 24))))) goto loc_009D4457;
    *(unsigned int *)(v_stack_m80) = (unsigned int)((unsigned int)(v_stack_mA4));
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_009D4436;
loc_009D4221:
loc_009D4226:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))) != 18) goto loc_009D429C;
    if (v_stack_mA8 == 0) goto loc_009D429C;
    *(unsigned int *)(a5) = 25;
    goto loc_009D429C;
loc_009D423B:
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 10223349));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10223354));
    }
    if (result != 0) goto loc_009D4166;
loc_009D425B:
    v_stack_mC0 = v_stack_mA4;
    v_stack_mA4 = 22;
    a2 = v_stack_m98;
    if (v_stack_m70 != 0) { a2 = v_stack_m70; }
    v_stack_mC8 = v_stack_m60;
    result = PnpCtxRegQueryValue((unsigned int)((unsigned int)(result)), a2, *(unsigned __int64 *)(0 + 16), v_stack_mA0);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_009D43CA;
loc_009D4297:
loc_009D429C:
    if (v_stack_m78 != 0) goto loc_009D4461;
loc_009D42A9:
    if (v_stack_m98 != 0) {
        result = ZwClose(v_stack_m98, a2, *(unsigned __int64 *)(0 + 16), v_stack_mA0);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(0 + 16), v_stack_mA0);
    v_rsp = (v_rsp) + (176);
    return result;
loc_009D42E1:
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 16)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 16) + 8));
    }
    result = 0;
    if (a1 == 0) goto loc_009D40ED;
    goto loc_009D40DD;
loc_009D4301:
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 10223475));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10223480));
    }
    if (result != 0) goto loc_009D4181;
    goto loc_009D425B;
loc_009D4326:
    goto loc_009D4118;
loc_009D432E:
    goto loc_009D42B7;
loc_009D4335:
    if (result == (v_rip - 942380)) goto loc_009D41BA;
    v_stack_p30 = v_stack_mA8;
    v_stack_p28 = v_stack_mA4;
    v_stack_p20 = v_r13;
    result = guard_dispatch_icall(a1, a2, *(unsigned __int64 *)(0 + 16), v_stack_mA0);
    goto loc_009D41DA;
loc_009D436A:
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 10143188));
    result = (*(unsigned __int64 *)(a4 + 8)) - (*(unsigned __int64 *)(v_rip - 10143197));
loc_009D438A:
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 10143364));
    result = (*(unsigned __int64 *)(a4 + 8)) - (*(unsigned __int64 *)(v_rip - 10143373));
loc_009D43AA:
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 10167492));
    result = (*(unsigned __int64 *)(a4 + 8)) - (*(unsigned __int64 *)(v_rip - 10167501));
loc_009D43CA:
    if (((unsigned int)(result)) == 0xC000017CULL) goto loc_009D4297;
    a4 = 0;
    *(unsigned int *)(v_stack_m80) = 1;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)));
    v_stack_m4C = 0;
    result = wcsicmp(v_rip + 1255957, v_stack_m60, *(unsigned __int64 *)(0 + 16), a4);
loc_009D4416:
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 10223776));
    result = (*(unsigned __int64 *)(a4 + 8)) - (*(unsigned __int64 *)(v_rip - 10223785));
loc_009D4436:
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_mA0))) != 0) goto loc_009D4226;
    goto loc_009D4221;
loc_009D4444:
    if (((unsigned int)(v_rip + 1255957)) == 0xC0000023ULL) goto loc_009D41FD;
    goto loc_009D429C;
loc_009D4457:
    goto loc_009D429C;
loc_009D4461:
    result = ZwClose(v_rip + 1255957, v_stack_m60, *(unsigned __int64 *)(0 + 16), a4);
    goto loc_009D42A9;
}
```

## 5. (Beta) C Style

```c
int64_t _CmGetInstallerClassMappedPropertyFromRegValue(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, void *Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m48;
    uint16_t v_stack_m4C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint8_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x4366C5)) ^ (local_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m68 = Arg2;
    v_stack_m70 = Arg3;
    v_stack_m88 = Arg1;
    v_stack_m80 = Arg8;
    v_stack_m98 = 0;
    v_stack_m78 = 0;
    v_stack_mA0 = 0;
    v_stack_mA4 = 0;
    v_stack_mA8 = 0;
    v_stack_m90 = 0;
loc_009D40CD:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == (*(uint32_t *)(*(uint64_t *)(v_rip + 0x179279) + 0x10))) goto loc_009D42E1;
loc_009D40DD:
    Arg4 = (uint32_t)((0) + 1);
    Arg2 = (v_rip + 1544825) + (32);
    if (((uint32_t)(Arg4)) < 13) goto loc_009D40CD;
loc_009D40ED:
    Arg4 = 0;
    if (0 == 0) goto loc_009D432E;
    *(uint32_t *)(arg5) = 0;
    *(uint32_t *)(arg8) = 0;
    if (Arg6 == 0) goto loc_009D4326;
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(Arg7)))));
    local_r13 = (Arg6) & (Arg1);
loc_009D4118:
    if (Arg3 != 0) goto loc_009D415A;
    v_stack_mB0 = 0;
    v_stack_mB8 = v_stack_m98;
    v_stack_mC0 = 0;
    v_stack_mC8 = 1;
    result = CmOpenCommonClassRegKey(v_stack_m88, v_stack_m68, Arg3 + 32, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_009D429C;
loc_009D415A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 7) goto loc_009D423B;
loc_009D4166:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 8) goto loc_009D436A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 9) goto loc_009D438A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 10) goto loc_009D4301;
loc_009D4181:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 15) goto loc_009D43AA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 2) goto loc_009D4416;
    Arg2 = v_stack_m98;
    if (v_stack_m70 != 0) { Arg2 = v_stack_m70; }
    v_stack_mA4 = (uint32_t)((uint32_t)(Arg7));
    if (*(uint64_t *)(v_stack_m88 + 0x208) != 0) goto loc_009D4335;
loc_009D41BA:
    v_stack_mB8 = v_stack_mA8;
    v_stack_mC0 = v_stack_mA4;
    v_stack_mC8 = local_r13;
    result = PnpRegQueryValueIndirect(v_stack_m88, Arg2, *(uint64_t *)(0 + 0x10), v_stack_mA0);
loc_009D41DA:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_009D4297;
    if (((uint32_t)(result)) == 0xC000017CULL) goto loc_009D4297;
    Arg4 = 0;
    if ((uint32_t)(result) != 0) goto loc_009D4444;
loc_009D41FD:
    if (v_stack_mA0 != ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x18))))) goto loc_009D4457;
    *(uint32_t *)(v_stack_m80) = (uint32_t)((uint32_t)(v_stack_mA4));
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_009D4436;
loc_009D4221:
loc_009D4226:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))) != 18) goto loc_009D429C;
    if (v_stack_mA8 == 0) goto loc_009D429C;
    *(uint32_t *)(arg5) = 25;
    goto loc_009D429C;
loc_009D423B:
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x9BFEF5));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BFEFA));
    }
    if (result != 0) goto loc_009D4166;
loc_009D425B:
    v_stack_mC0 = v_stack_mA4;
    v_stack_mA4 = 22;
    Arg2 = v_stack_m98;
    if (v_stack_m70 != 0) { Arg2 = v_stack_m70; }
    v_stack_mC8 = v_stack_m60;
    result = PnpCtxRegQueryValue((uint32_t)((uint32_t)(result)), Arg2, *(uint64_t *)(0 + 0x10), v_stack_mA0);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_009D43CA;
loc_009D4297:
loc_009D429C:
    if (v_stack_m78 != 0) goto loc_009D4461;
loc_009D42A9:
    if (v_stack_m98 != 0) {
        result = ZwClose(v_stack_m98, Arg2, *(uint64_t *)(0 + 0x10), v_stack_mA0);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(0 + 0x10), v_stack_mA0);
    local_rsp = (local_rsp) + (176);
    return result;
loc_009D42E1:
    Arg1 = (*(uint64_t *)(arg4)) - (*(uint64_t *)(*(uint64_t *)(0 + 0x10)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg4 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(0 + 0x10) + 0x8));
    }
    result = 0;
    if (Arg1 == 0) goto loc_009D40ED;
    goto loc_009D40DD;
loc_009D4301:
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x9BFF73));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x9BFF78));
    }
    if (result != 0) goto loc_009D4181;
    goto loc_009D425B;
loc_009D4326:
    goto loc_009D4118;
loc_009D432E:
    goto loc_009D42B7;
loc_009D4335:
    if (result == (v_rip - 942380)) goto loc_009D41BA;
    v_stack_p30 = v_stack_mA8;
    v_stack_p28 = v_stack_mA4;
    v_stack_p20 = local_r13;
    result = guard_dispatch_icall(Arg1, Arg2, *(uint64_t *)(0 + 0x10), v_stack_mA0);
    goto loc_009D41DA;
loc_009D436A:
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x9AC5D4));
    result = (*(uint64_t *)(arg4 + 0x8)) - (*(uint64_t *)(v_rip - 0x9AC5DD));
loc_009D438A:
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x9AC684));
    result = (*(uint64_t *)(arg4 + 0x8)) - (*(uint64_t *)(v_rip - 0x9AC68D));
loc_009D43AA:
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x9B24C4));
    result = (*(uint64_t *)(arg4 + 0x8)) - (*(uint64_t *)(v_rip - 0x9B24CD));
loc_009D43CA:
    if (((uint32_t)(result)) == 0xC000017CULL) goto loc_009D4297;
    Arg4 = 0;
    *(uint32_t *)(v_stack_m80) = 1;
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)));
    v_stack_m4C = 0;
    result = wcsicmp(v_rip + 1255957, v_stack_m60, *(uint64_t *)(0 + 0x10), Arg4);
loc_009D4416:
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x9C00A0));
    result = (*(uint64_t *)(arg4 + 0x8)) - (*(uint64_t *)(v_rip - 0x9C00A9));
loc_009D4436:
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_mA0))) != 0) goto loc_009D4226;
    goto loc_009D4221;
loc_009D4444:
    if (((uint32_t)(v_rip + 1255957)) == 0xC0000023ULL) goto loc_009D41FD;
    goto loc_009D429C;
loc_009D4457:
    goto loc_009D429C;
loc_009D4461:
    result = ZwClose(v_rip + 1255957, v_stack_m60, *(uint64_t *)(0 + 0x10), Arg4);
    goto loc_009D42A9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D4058&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
