# CmGetDeviceInterfaceMappedPropertyFromRegValue

- RVA: `0x008F40BC`–`0x008F4556` (길이 `1,178` bytes)
- VA: `0x00000001408F40BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000876CC`
- 디코드: `290`개 명령, `1,178/1,178` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x008F41D0` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x008F41F9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F4219` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008F42CF` → [_RegRtlOpenKeyTransacted](../8E/_RegRtlOpenKeyTransacted_function_008EF810.md) (function, `0x008EF810`)
- `0x008F4335` → [PnpRegQueryValueIndirect](../8E/PnpRegQueryValueIndirect_function_008EE210.md) (function, `0x008EE210`)
- `0x008F4340` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008F43C2` → [_CmOpenDeviceInterfaceRegKey](_CmOpenDeviceInterfaceRegKey_function_008F31F4.md) (function, `0x008F31F4`)
- `0x008F442C` → [_CmOpenDeviceInterfaceRegKey](_CmOpenDeviceInterfaceRegKey_function_008F31F4.md) (function, `0x008F31F4`)
- `0x008F445C` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x008F4467` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008F452D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [_PnpDispatchDeviceInterface](../8E/_PnpDispatchDeviceInterface_function_008E0DB0.md) at `0x008E0FA3`
- [CmGetDeviceInterfaceMappedPropertyKeys](CmGetDeviceInterfaceMappedPropertyKeys_function_008F50AC.md) at `0x008F514B`

### Static image references
- `0x008F412C` → RVA `0x00B4B1E0` (`PAGE`; read)
- `0x008F418A` → RVA `0x000114D0` (`.rdata`; read)
- `0x008F4197` → RVA `0x000114D8` (`.rdata`; read)
- `0x008F426C` → RVA `0x000114F8` (`.rdata`; read)
- `0x008F4279` → RVA `0x00011500` (`.rdata`; read)
- `0x008F42BA` → RVA `0x00B0D340` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008F4329` → RVA `0x00B09360` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008F43E8` → RVA `0x00011490` (`.rdata`; read)
- `0x008F43F5` → RVA `0x00011498` (`.rdata`; read)
- `0x008F444C` → RVA `0x00B0D7F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008F44F4` → RVA `0x008EE210` (`PnpRegQueryValueIndirect`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x008F41D0` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x008F41F9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F4219` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008F4340` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008F4467` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008F452D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F40BC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008F40C1  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008F40C6  55                              push rbp
008F40C7  56                              push rsi
008F40C8  57                              push rdi
008F40C9  41 54                           push r12
008F40CB  41 55                           push r13
008F40CD  41 56                           push r14
008F40CF  41 57                           push r15
008F40D1  48 8B EC                        mov rbp, rsp
008F40D4  48 81 EC 80 00 00 00            sub rsp, 0x80
008F40DB  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
008F40DF  33 DB                           xor ebx, ebx
008F40E1  48 21 5D E0                     and qword ptr [rbp - 0x20], rbx
008F40E5  49 8B F0                        mov rsi, r8
008F40E8  4C 8B 45 60                     mov r8, qword ptr [rbp + 0x60]
008F40EC  49 8B F9                        mov rdi, r9
008F40EF  48 21 5D D8                     and qword ptr [rbp - 0x28], rbx
008F40F3  4C 8B F1                        mov r14, rcx
008F40F6  48 21 5D D0                     and qword ptr [rbp - 0x30], rbx
008F40FA  21 5D C8                        and dword ptr [rbp - 0x38], ebx
008F40FD  41 21 18                        and dword ptr [r8], ebx
008F4100  21 18                           and dword ptr [rax], ebx
008F4102  21 5D C4                        and dword ptr [rbp - 0x3c], ebx
008F4105  4C 8B 6D 68                     mov r13, qword ptr [rbp + 0x68]
008F4109  88 5D 58                        mov byte ptr [rbp + 0x58], bl
008F410C  88 5D C0                        mov byte ptr [rbp - 0x40], bl
008F410F  4D 85 ED                        test r13, r13
008F4112  0F 85 3D 01 00 00               jne 0x1408f4255
008F4118  45 33 FF                        xor r15d, r15d
008F411B  45 8B 61 10                     mov r12d, dword ptr [r9 + 0x10]
008F411F  41 83 FC 02                     cmp r12d, 2
008F4123  0F 82 C1 03 00 00               jb 0x1408f44ea
008F4129  45 33 D2                        xor r10d, r10d
008F412C  48 8D 15 AD 70 25 00            lea rdx, [rip + 0x2570ad]
008F4133  4C 8B 0A                        mov r9, qword ptr [rdx]
008F4136  4C 8B DA                        mov r11, rdx
008F4139  45 3B 61 10                     cmp r12d, dword ptr [r9 + 0x10]
008F413D  0F 85 F9 00 00 00               jne 0x1408f423c
008F4143  48 8B 0F                        mov rcx, qword ptr [rdi]
008F4146  49 2B 09                        sub rcx, qword ptr [r9]
008F4149  75 08                           jne 0x1408f4153
008F414B  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008F414F  49 2B 49 08                     sub rcx, qword ptr [r9 + 8]
008F4153  48 85 C9                        test rcx, rcx
008F4156  0F 85 E0 00 00 00               jne 0x1408f423c
008F415C  4D 85 DB                        test r11, r11
008F415F  0F 84 85 03 00 00               je 0x1408f44ea
008F4165  4C 8B 65 48                     mov r12, qword ptr [rbp + 0x48]
008F4169  48 85 F6                        test rsi, rsi
008F416C  0F 84 2A 02 00 00               je 0x1408f439c
008F4172  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008F4175  83 F8 02                        cmp eax, 2
008F4178  0F 84 EB 00 00 00               je 0x1408f4269
008F417E  83 F8 03                        cmp eax, 3
008F4181  0F 85 53 02 00 00               jne 0x1408f43da
008F4187  48 8B 07                        mov rax, qword ptr [rdi]
008F418A  48 2B 05 3F D3 71 FF            sub rax, qword ptr [rip - 0x8e2cc1]
008F4191  75 0B                           jne 0x1408f419e
008F4193  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F4197  48 2B 05 3A D3 71 FF            sub rax, qword ptr [rip - 0x8e2cc6]
008F419E  48 85 C0                        test rax, rax
008F41A1  0F 85 39 03 00 00               jne 0x1408f44e0
008F41A7  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
008F41AB  C7 00 01 00 00 00               mov dword ptr [rax], 1
008F41B1  41 C7 00 11 00 00 00            mov dword ptr [r8], 0x11
008F41B8  41 83 FF 01                     cmp r15d, 1
008F41BC  0F 82 ED 02 00 00               jb 0x1408f44af
008F41C2  0F 57 C0                        xorps xmm0, xmm0
008F41C5  48 8D 4D E8                     lea rcx, [rbp - 0x18]
008F41C9  49 8B D4                        mov rdx, r12
008F41CC  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
008F41D0  E8 8B F7 B6 FF                  call 0x140463960
008F41D5  8B D8                           mov ebx, eax
008F41D7  85 C0                           test eax, eax
008F41D9  78 26                           js 0x1408f4201
008F41DB  49 8B 86 20 01 00 00            mov rax, qword ptr [r14 + 0x120]
008F41E2  48 85 C0                        test rax, rax
008F41E5  0F 84 53 03 00 00               je 0x1408f453e
008F41EB  45 33 C9                        xor r9d, r9d
008F41EE  4C 8D 45 C0                     lea r8, [rbp - 0x40]
008F41F2  48 8D 55 E8                     lea rdx, [rbp - 0x18]
008F41F6  49 8B CE                        mov rcx, r14
008F41F9  E8 D2 68 DC FF                  call 0x1406baad0
008F41FE  48 8B D8                        mov rbx, rax
008F4201  85 DB                           test ebx, ebx
008F4203  78 0B                           js 0x1408f4210
008F4205  8A 4D C0                        mov cl, byte ptr [rbp - 0x40]
008F4208  F6 D9                           neg cl
008F420A  1A D2                           sbb dl, dl
008F420C  41 88 55 00                     mov byte ptr [r13], dl
008F4210  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
008F4214  48 85 C9                        test rcx, rcx
008F4217  74 05                           je 0x1408f421e
008F4219  E8 92 90 DB FF                  call 0x1406ad2b0
008F421E  8B C3                           mov eax, ebx
008F4220  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
008F4228  48 81 C4 80 00 00 00            add rsp, 0x80
008F422F  41 5F                           pop r15
008F4231  41 5E                           pop r14
008F4233  41 5D                           pop r13
008F4235  41 5C                           pop r12
008F4237  5F                              pop rdi
008F4238  5E                              pop rsi
008F4239  5D                              pop rbp
008F423A  C3                              ret
008F423B  CC                              int3
008F423C  45 33 DB                        xor r11d, r11d
008F423F  41 FF C2                        inc r10d
008F4242  48 83 C2 10                     add rdx, 0x10
008F4246  41 83 FA 03                     cmp r10d, 3
008F424A  0F 83 0C FF FF FF               jae 0x1408f415c
008F4250  E9 DE FE FF FF                  jmp 0x1408f4133
008F4255  44 8B 7D 70                     mov r15d, dword ptr [rbp + 0x70]
008F4259  41 8B C7                        mov eax, r15d
008F425C  F7 D8                           neg eax
008F425E  48 1B C9                        sbb rcx, rcx
008F4261  4C 23 E9                        and r13, rcx
008F4264  E9 B2 FE FF FF                  jmp 0x1408f411b
008F4269  48 8B 07                        mov rax, qword ptr [rdi]
008F426C  48 2B 05 85 D2 71 FF            sub rax, qword ptr [rip - 0x8e2d7b]
008F4273  75 0B                           jne 0x1408f4280
008F4275  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F4279  48 2B 05 80 D2 71 FF            sub rax, qword ptr [rip - 0x8e2d80]
008F4280  48 85 C0                        test rax, rax
008F4283  0F 85 57 02 00 00               jne 0x1408f44e0
008F4289  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
008F428D  48 85 F6                        test rsi, rsi
008F4290  48 0F 45 CE                     cmovne rcx, rsi
008F4294  4D 85 F6                        test r14, r14
008F4297  0F 84 3C 02 00 00               je 0x1408f44d9
008F429D  49 8B 86 E0 00 00 00            mov rax, qword ptr [r14 + 0xe0]
008F42A4  48 85 C0                        test rax, rax
008F42A7  0F 84 2C 02 00 00               je 0x1408f44d9
008F42AD  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
008F42B1  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
008F42B6  48 8D 45 D0                     lea rax, [rbp - 0x30]
008F42BA  48 8D 15 7F 90 21 00            lea rdx, [rip + 0x21907f]
008F42C1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F42C6  41 B9 01 00 00 00               mov r9d, 1
008F42CC  45 33 C0                        xor r8d, r8d
008F42CF  E8 3C B5 FF FF                  call 0x1408ef810
008F42D4  41 BC 34 00 00 C0               mov r12d, 0xc0000034
008F42DA  41 3B C4                        cmp eax, r12d
008F42DD  0F 84 DD 01 00 00               je 0x1408f44c0
008F42E3  BE 7C 01 00 C0                  mov esi, 0xc000017c
008F42E8  3B C6                           cmp eax, esi
008F42EA  0F 84 D0 01 00 00               je 0x1408f44c0
008F42F0  85 C0                           test eax, eax
008F42F2  0F 88 3F 02 00 00               js 0x1408f4537
008F42F8  49 8B 86 08 02 00 00            mov rax, qword ptr [r14 + 0x208]
008F42FF  44 89 7D C4                     mov dword ptr [rbp - 0x3c], r15d
008F4303  48 85 C0                        test rax, rax
008F4306  0F 85 E8 01 00 00               jne 0x1408f44f4
008F430C  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008F4310  48 8D 45 58                     lea rax, [rbp + 0x58]
008F4314  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F4319  4C 8D 4D C8                     lea r9, [rbp - 0x38]
008F431D  48 8D 45 C4                     lea rax, [rbp - 0x3c]
008F4321  49 8B CE                        mov rcx, r14
008F4324  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F4329  4C 8D 05 30 50 21 00            lea r8, [rip + 0x215030]
008F4330  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008F4335  E8 D6 9E FF FF                  call 0x1408ee210
008F433A  8B F8                           mov edi, eax
008F433C  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
008F4340  E8 6B 8F DB FF                  call 0x1406ad2b0
008F4345  41 3B FC                        cmp edi, r12d
008F4348  0F 84 72 01 00 00               je 0x1408f44c0
008F434E  3B FE                           cmp edi, esi
008F4350  0F 84 6A 01 00 00               je 0x1408f44c0
008F4356  B9 23 00 00 C0                  mov ecx, 0xc0000023
008F435B  85 FF                           test edi, edi
008F435D  0F 85 67 01 00 00               jne 0x1408f44ca
008F4363  8B 45 C4                        mov eax, dword ptr [rbp - 0x3c]
008F4366  48 8B 55 78                     mov rdx, qword ptr [rbp + 0x78]
008F436A  89 02                           mov dword ptr [rdx], eax
008F436C  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
008F4370  C7 00 12 00 00 00               mov dword ptr [rax], 0x12
008F4376  85 FF                           test edi, edi
008F4378  0F 85 3B 01 00 00               jne 0x1408f44b9
008F437E  45 85 FF                        test r15d, r15d
008F4381  0F 84 32 01 00 00               je 0x1408f44b9
008F4387  80 7D 58 00                     cmp byte ptr [rbp + 0x58], 0
008F438B  0F 84 7F FE FF FF               je 0x1408f4210
008F4391  C7 00 19 00 00 00               mov dword ptr [rax], 0x19
008F4397  E9 74 FE FF FF                  jmp 0x1408f4210
008F439C  48 21 5C 24 38                  and qword ptr [rsp + 0x38], rbx
008F43A1  48 8D 45 E0                     lea rax, [rbp - 0x20]
008F43A5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F43AA  41 B8 30 00 00 00               mov r8d, 0x30
008F43B0  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
008F43B4  49 8B D4                        mov rdx, r12
008F43B7  49 8B CE                        mov rcx, r14
008F43BA  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008F43C2  E8 2D EE FF FF                  call 0x1408f31f4
008F43C7  8B D8                           mov ebx, eax
008F43C9  85 C0                           test eax, eax
008F43CB  0F 88 3F FE FF FF               js 0x1408f4210
008F43D1  4C 8B 45 60                     mov r8, qword ptr [rbp + 0x60]
008F43D5  E9 98 FD FF FF                  jmp 0x1408f4172
008F43DA  3D 00 01 00 00                  cmp eax, 0x100
008F43DF  0F 85 FB 00 00 00               jne 0x1408f44e0
008F43E5  48 8B 07                        mov rax, qword ptr [rdi]
008F43E8  48 2B 05 A1 D0 71 FF            sub rax, qword ptr [rip - 0x8e2f5f]
008F43EF  75 0B                           jne 0x1408f43fc
008F43F1  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F43F5  48 2B 05 9C D0 71 FF            sub rax, qword ptr [rip - 0x8e2f64]
008F43FC  48 85 C0                        test rax, rax
008F43FF  0F 85 DB 00 00 00               jne 0x1408f44e0
008F4405  48 21 44 24 38                  and qword ptr [rsp + 0x38], rax
008F440A  41 B8 31 00 00 00               mov r8d, 0x31
008F4410  48 8D 45 D8                     lea rax, [rbp - 0x28]
008F4414  49 8B D4                        mov rdx, r12
008F4417  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F441C  49 8B CE                        mov rcx, r14
008F441F  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
008F4424  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008F442C  E8 C3 ED FF FF                  call 0x1408f31f4
008F4431  8B D8                           mov ebx, eax
008F4433  85 C0                           test eax, eax
008F4435  0F 88 D5 FD FF FF               js 0x1408f4210
008F443B  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
008F443F  48 8D 45 C4                     lea rax, [rbp - 0x3c]
008F4443  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F4448  4C 8D 4D C8                     lea r9, [rbp - 0x38]
008F444C  4C 8D 05 9D 93 21 00            lea r8, [rip + 0x21939d]
008F4453  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008F4458  44 89 7D C4                     mov dword ptr [rbp - 0x3c], r15d
008F445C  E8 9B FC 09 00                  call 0x1409940fc
008F4461  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
008F4465  8B F8                           mov edi, eax
008F4467  E8 44 8E DB FF                  call 0x1406ad2b0
008F446C  41 BC 34 00 00 C0               mov r12d, 0xc0000034
008F4472  41 3B FC                        cmp edi, r12d
008F4475  74 49                           je 0x1408f44c0
008F4477  BE 7C 01 00 C0                  mov esi, 0xc000017c
008F447C  3B FE                           cmp edi, esi
008F447E  74 40                           je 0x1408f44c0
008F4480  41 8D 4C 24 EF                  lea ecx, [r12 - 0x11]
008F4485  85 FF                           test edi, edi
008F4487  74 04                           je 0x1408f448d
008F4489  3B F9                           cmp edi, ecx
008F448B  75 45                           jne 0x1408f44d2
008F448D  8B 45 C4                        mov eax, dword ptr [rbp - 0x3c]
008F4490  48 8B 55 78                     mov rdx, qword ptr [rbp + 0x78]
008F4494  89 02                           mov dword ptr [rdx], eax
008F4496  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
008F449A  C7 00 12 00 00 00               mov dword ptr [rax], 0x12
008F44A0  85 FF                           test edi, edi
008F44A2  0F 84 A0 00 00 00               je 0x1408f4548
008F44A8  8B D9                           mov ebx, ecx
008F44AA  E9 61 FD FF FF                  jmp 0x1408f4210
008F44AF  BB 23 00 00 C0                  mov ebx, 0xc0000023
008F44B4  E9 57 FD FF FF                  jmp 0x1408f4210
008F44B9  8B D9                           mov ebx, ecx
008F44BB  E9 C7 FE FF FF                  jmp 0x1408f4387
008F44C0  BB 25 02 00 C0                  mov ebx, 0xc0000225
008F44C5  E9 46 FD FF FF                  jmp 0x1408f4210
008F44CA  3B F9                           cmp edi, ecx
008F44CC  0F 84 91 FE FF FF               je 0x1408f4363
008F44D2  8B DF                           mov ebx, edi
008F44D4  E9 37 FD FF FF                  jmp 0x1408f4210
008F44D9  33 D2                           xor edx, edx
008F44DB  E9 D1 FD FF FF                  jmp 0x1408f42b1
008F44E0  BB 30 02 00 C0                  mov ebx, 0xc0000230
008F44E5  E9 26 FD FF FF                  jmp 0x1408f4210
008F44EA  BB 30 02 00 C0                  mov ebx, 0xc0000230
008F44EF  E9 2A FD FF FF                  jmp 0x1408f421e
008F44F4  48 8D 0D 15 9D FF FF            lea rcx, [rip - 0x62eb]
008F44FB  48 3B C1                        cmp rax, rcx
008F44FE  0F 84 08 FE FF FF               je 0x1408f430c
008F4504  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008F4508  48 8D 4D 58                     lea rcx, [rbp + 0x58]
008F450C  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
008F4511  4C 8D 4D C8                     lea r9, [rbp - 0x38]
008F4515  48 8D 4D C4                     lea rcx, [rbp - 0x3c]
008F4519  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008F451E  4C 8D 05 3B 4E 21 00            lea r8, [rip + 0x214e3b]
008F4525  49 8B CE                        mov rcx, r14
008F4528  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008F452D  E8 9E 65 DC FF                  call 0x1406baad0
008F4532  E9 03 FE FF FF                  jmp 0x1408f433a
008F4537  8B D8                           mov ebx, eax
008F4539  E9 D2 FC FF FF                  jmp 0x1408f4210
008F453E  BB 02 00 00 C0                  mov ebx, 0xc0000002
008F4543  E9 B9 FC FF FF                  jmp 0x1408f4201
008F4548  45 85 FF                        test r15d, r15d
008F454B  0F 85 BF FC FF FF               jne 0x1408f4210
008F4551  E9 52 FF FF FF                  jmp 0x1408f44a8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmGetDeviceInterfaceMappedPropertyFromRegValue(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    v_rbx = 0;
    v_stack_p20 = 0;
    v_stack_m78 = 0;
    if (a6 != 0) goto loc_008F4255;
    v_r15 = 0;
loc_008F411B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) < 2) goto loc_008F44EA;
    v_r10 = 0;
loc_008F4133:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2453677) + 16))) goto loc_008F423C;
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2453677)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2453677) + 8));
    }
    if (a1 != 0) goto loc_008F423C;
loc_008F415C:
    if (v_rip + 2453677 == 0) goto loc_008F44EA;
    if (a3 == 0) goto loc_008F439C;
loc_008F4172:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 2) goto loc_008F4269;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 3) goto loc_008F43DA;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 9317569));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9317574));
    }
    if (result != 0) goto loc_008F44E0;
    *(unsigned int *)(a8) = 1;
    *(unsigned int *)(a5) = 17;
    if (0 < 1) goto loc_008F44AF;
    v_stack_m50 = v_xmm0;
    result = RtlInitUnicodeStringEx(v_stack_m50, v_stack_p10, a5, *(unsigned __int64 *)(v_rip + 2453677));
    if (sign_flag) goto loc_008F4201;
    if (*(unsigned __int64 *)(a1 + 288) == 0) goto loc_008F453E;
    a4 = 0;
    result = guard_dispatch_icall(a1, v_stack_m50, v_stack_m78, a4);
loc_008F4201:
    if (!(sign_flag)) {
        a1 = v_stack_m78;
        a1 = (unsigned __int8)(-(a1));
        *(unsigned __int8 *)(a6) = (unsigned __int8)(v_stack_m50);
    }
    if (v_stack_m58 != 0) {
        result = ZwClose(v_stack_m58, v_stack_m50, v_stack_m78, a4);
    }
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)(result));
loc_008F423C:
    v_r11 = 0;
    v_r10 = (unsigned int)((v_r10) + 1);
    a2 = (v_stack_m50) + (16);
    if (((unsigned int)(v_r10)) >= 3) goto loc_008F415C;
    goto loc_008F4133;
loc_008F4255:
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(a7)))));
    v_r13 = (a6) & (v_stack_m58);
    goto loc_008F411B;
loc_008F4269:
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 9317755));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9317760));
    }
    if (result != 0) goto loc_008F44E0;
    a1 = v_stack_m58;
    if (a3 != 0) { a1 = a3; }
    if (a1 == 0) goto loc_008F44D9;
    if (*(unsigned __int64 *)(a1 + 224) == 0) goto loc_008F44D9;
loc_008F42B1:
    v_stack_p28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 8);
    v_stack_p20 = v_stack_m68;
    a3 = 0;
    result = _RegRtlOpenKeyTransacted(a1, v_rip + 2199679, a3, 1);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008F44C0;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000017CULL)))) goto loc_008F44C0;
    if (sign_flag) goto loc_008F4537;
    v_stack_m74 = (unsigned int)((unsigned int)(a7));
    if (*(unsigned __int64 *)(a1 + 520) != 0) goto loc_008F44F4;
loc_008F430C:
    v_stack_p30 = v_stack_p20;
    v_stack_p28 = v_stack_m74;
    v_stack_p20 = v_r13;
    result = PnpRegQueryValueIndirect(a1, v_stack_m68, v_rip + 2183216, v_stack_m70);
loc_008F433A:
    result = ZwClose(v_stack_m68, v_stack_m68, v_rip + 2183216, v_stack_m70);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008F44C0;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC000017CULL)))) goto loc_008F44C0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_008F44CA;
loc_008F4363:
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(v_stack_m74));
    *(unsigned int *)(a5) = 18;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_008F44B9;
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_008F44B9;
loc_008F4387:
    if (v_stack_p20 == 0) goto loc_008F4210;
    *(unsigned int *)(a5) = 25;
    goto loc_008F4210;
loc_008F439C:
    v_stack_p30 = v_stack_m58;
    v_stack_p28 = (unsigned __int8)(v_stack_p8);
    v_stack_p20 = 1;
    result = _CmOpenDeviceInterfaceRegKey(a1, (unsigned int)(0xC0000034ULL), 48, v_stack_m70);
    if (sign_flag) goto loc_008F4210;
    goto loc_008F4172;
loc_008F43DA:
    if (((unsigned int)(result)) != 256) goto loc_008F44E0;
    result = (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)))) - (*(unsigned __int64 *)(v_rip - 9318239));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9318244));
    }
    if (result != 0) goto loc_008F44E0;
    v_stack_p30 = v_stack_m60;
    v_stack_p28 = 0;
    v_stack_p20 = 1;
    result = _CmOpenDeviceInterfaceRegKey(a1, (unsigned int)(0xC0000034ULL), 49, v_stack_m70);
    if (sign_flag) goto loc_008F4210;
    v_stack_p28 = v_stack_m74;
    v_stack_p20 = v_r13;
    v_stack_m74 = (unsigned int)((unsigned int)(a7));
    result = PnpCtxRegQueryValue(a1, v_stack_m60, v_rip + 2200477, v_stack_m70);
    result = ZwClose(v_stack_m60, v_stack_m60, v_rip + 2200477, v_stack_m70);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008F44C0;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC000017CULL)))) goto loc_008F44C0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_008F448D;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC0000034ULL) - 17))) goto loc_008F44D2;
loc_008F448D:
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(v_stack_m74));
    *(unsigned int *)(a5) = 18;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_008F4548;
loc_008F44A8:
    goto loc_008F4210;
loc_008F44AF:
    goto loc_008F4210;
loc_008F44B9:
    goto loc_008F4387;
loc_008F44C0:
    goto loc_008F4210;
loc_008F44CA:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC0000034ULL) - 17))) goto loc_008F4363;
loc_008F44D2:
    goto loc_008F4210;
loc_008F44D9:
    a2 = 0;
    goto loc_008F42B1;
loc_008F44E0:
    goto loc_008F4210;
loc_008F44EA:
    goto loc_008F421E;
loc_008F44F4:
    if (a5 == (v_rip - 25323)) goto loc_008F430C;
    v_stack_p30 = v_stack_p20;
    v_stack_p28 = v_stack_m74;
    v_stack_p20 = v_r13;
    result = guard_dispatch_icall(a1, v_stack_m68, v_rip + 2182715, v_stack_m70);
    goto loc_008F433A;
loc_008F4537:
    goto loc_008F4210;
loc_008F453E:
    goto loc_008F4201;
loc_008F4548:
    if ((unsigned int)((unsigned int)(a7)) != 0) goto loc_008F4210;
    goto loc_008F44A8;
}
```

## 5. (Beta) C Style

```c
int64_t CmGetDeviceInterfaceMappedPropertyFromRegValue(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, void *Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m78;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    local_rbx = 0;
    v_stack_p20 = 0;
    v_stack_m78 = 0;
    if (Arg6 != 0) goto loc_008F4255;
    local_r15 = 0;
loc_008F411B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) < 2) goto loc_008F44EA;
    local_r10 = 0;
loc_008F4133:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != (*(uint32_t *)(*(uint64_t *)(v_rip + 0x2570AD) + 0x10))) goto loc_008F423C;
    Arg1 = (*(uint64_t *)(arg4)) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0x2570AD)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg4 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0x2570AD) + 0x8));
    }
    if (Arg1 != NULL) goto loc_008F423C;
loc_008F415C:
    if (v_rip + 2453677 == 0) goto loc_008F44EA;
    if (Arg3 == 0) goto loc_008F439C;
loc_008F4172:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 2) goto loc_008F4269;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 3) goto loc_008F43DA;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x8E2CC1));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E2CC6));
    }
    if (result != 0) goto loc_008F44E0;
    *(uint32_t *)(arg8) = 1;
    *(uint32_t *)(arg5) = 17;
    if (0 < 1) goto loc_008F44AF;
    v_stack_m50 = v_xmm0;
    result = RtlInitUnicodeStringEx(v_stack_m50, v_stack_p10, Arg5, *(uint64_t *)(v_rip + 0x2570AD));
    if (sign_flag) goto loc_008F4201;
    if (*(uint64_t *)(arg1 + 0x120) == 0) goto loc_008F453E;
    Arg4 = 0;
    result = guard_dispatch_icall(Arg1, v_stack_m50, v_stack_m78, Arg4);
loc_008F4201:
    if (!(sign_flag)) {
        Arg1 = v_stack_m78;
        Arg1 = (uint8_t)(-(Arg1));
        *(uint8_t *)(Arg6) = (uint8_t)(v_stack_m50);
    }
    if (v_stack_m58 != 0) {
        result = ZwClose(v_stack_m58, v_stack_m50, v_stack_m78, Arg4);
    }
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)(result));
loc_008F423C:
    local_r11 = 0;
    local_r10 = (uint32_t)((local_r10) + 1);
    Arg2 = (v_stack_m50) + (16);
    if (((uint32_t)(local_r10)) >= 3) goto loc_008F415C;
    goto loc_008F4133;
loc_008F4255:
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(Arg7)))));
    local_r13 = (Arg6) & (v_stack_m58);
    goto loc_008F411B;
loc_008F4269:
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x8E2D7B));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E2D80));
    }
    if (result != 0) goto loc_008F44E0;
    Arg1 = v_stack_m58;
    if (Arg3 != 0) { Arg1 = Arg3; }
    if (Arg1 == NULL) goto loc_008F44D9;
    if (*(uint64_t *)(arg1 + 0xE0) == 0) goto loc_008F44D9;
loc_008F42B1:
    v_stack_p28 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x8);
    v_stack_p20 = v_stack_m68;
    Arg3 = 0;
    result = _RegRtlOpenKeyTransacted(Arg1, v_rip + 2199679, Arg3, 1);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008F44C0;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000017CULL)))) goto loc_008F44C0;
    if (sign_flag) goto loc_008F4537;
    v_stack_m74 = (uint32_t)((uint32_t)(Arg7));
    if (*(uint64_t *)(arg1 + 0x208) != 0) goto loc_008F44F4;
loc_008F430C:
    v_stack_p30 = v_stack_p20;
    v_stack_p28 = v_stack_m74;
    v_stack_p20 = local_r13;
    result = PnpRegQueryValueIndirect(Arg1, v_stack_m68, v_rip + 2183216, v_stack_m70);
loc_008F433A:
    result = ZwClose(v_stack_m68, v_stack_m68, v_rip + 2183216, v_stack_m70);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008F44C0;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC000017CULL)))) goto loc_008F44C0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_008F44CA;
loc_008F4363:
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(v_stack_m74));
    *(uint32_t *)(arg5) = 18;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_008F44B9;
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_008F44B9;
loc_008F4387:
    if (v_stack_p20 == 0) goto loc_008F4210;
    *(uint32_t *)(arg5) = 25;
    goto loc_008F4210;
loc_008F439C:
    v_stack_p30 = v_stack_m58;
    v_stack_p28 = (uint8_t)(v_stack_p8);
    v_stack_p20 = 1;
    result = _CmOpenDeviceInterfaceRegKey(Arg1, (uint32_t)(0xC0000034ULL), 48, v_stack_m70);
    if (sign_flag) goto loc_008F4210;
    goto loc_008F4172;
loc_008F43DA:
    if (((uint32_t)(result)) != 256) goto loc_008F44E0;
    result = (*(uint64_t *)((uint32_t)((uint32_t)(result)))) - (*(uint64_t *)(v_rip - 0x8E2F5F));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E2F64));
    }
    if (result != 0) goto loc_008F44E0;
    v_stack_p30 = v_stack_m60;
    v_stack_p28 = 0;
    v_stack_p20 = 1;
    result = _CmOpenDeviceInterfaceRegKey(Arg1, (uint32_t)(0xC0000034ULL), 49, v_stack_m70);
    if (sign_flag) goto loc_008F4210;
    v_stack_p28 = v_stack_m74;
    v_stack_p20 = local_r13;
    v_stack_m74 = (uint32_t)((uint32_t)(Arg7));
    result = PnpCtxRegQueryValue(Arg1, v_stack_m60, v_rip + 2200477, v_stack_m70);
    result = ZwClose(v_stack_m60, v_stack_m60, v_rip + 2200477, v_stack_m70);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008F44C0;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC000017CULL)))) goto loc_008F44C0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_008F448D;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC0000034ULL) - 17))) goto loc_008F44D2;
loc_008F448D:
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(v_stack_m74));
    *(uint32_t *)(arg5) = 18;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_008F4548;
loc_008F44A8:
    goto loc_008F4210;
loc_008F44AF:
    goto loc_008F4210;
loc_008F44B9:
    goto loc_008F4387;
loc_008F44C0:
    goto loc_008F4210;
loc_008F44CA:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC0000034ULL) - 17))) goto loc_008F4363;
loc_008F44D2:
    goto loc_008F4210;
loc_008F44D9:
    Arg2 = 0;
    goto loc_008F42B1;
loc_008F44E0:
    goto loc_008F4210;
loc_008F44EA:
    goto loc_008F421E;
loc_008F44F4:
    if (Arg5 == (v_rip - 25323)) goto loc_008F430C;
    v_stack_p30 = v_stack_p20;
    v_stack_p28 = v_stack_m74;
    v_stack_p20 = local_r13;
    result = guard_dispatch_icall(Arg1, v_stack_m68, v_rip + 2182715, v_stack_m70);
    goto loc_008F433A;
loc_008F4537:
    goto loc_008F4210;
loc_008F453E:
    goto loc_008F4201;
loc_008F4548:
    if ((uint32_t)((uint32_t)(Arg7)) != 0) goto loc_008F4210;
    goto loc_008F44A8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R/W` |
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x0` | `32` | `R/W` |
| `Arg8` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F40BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
