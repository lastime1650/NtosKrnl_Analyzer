# PnpDeviceRaisePropertyChangeEventWorker

- RVA: `0x008F80E0`–`0x008F85EC` (길이 `1,292` bytes)
- VA: `0x00000001408F80E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087B68`
- 디코드: `329`개 명령, `1,292/1,292` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x008F8188` → [PiPnpRtlObjectEventCallback](PiPnpRtlObjectEventCallback_function_008F8600.md) (function, `0x008F8600`)
- `0x008F81F5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F82A0` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x008F8303` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008F83D2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F8420` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F843F` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x008F8456` → [PnpStringFromGuid](PnpStringFromGuid_function_008F5A2C.md) (function, `0x008F5A2C`)
- `0x008F84E3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F8540` → [_CmGetMatchingFilteredDeviceInterfaceList](../A0/_CmGetMatchingFilteredDeviceInterfaceList_function_00A09610.md) (function, `0x00A09610`)
- `0x008F856D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F859F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F85CE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PnpRaiseNtPlugPlayDevicePropertyChangeEvent](PnpRaiseNtPlugPlayDevicePropertyChangeEvent_function_008F7D80.md) at `0x008F7DED`
- [PnpObjectRaisePropertyChangeEvent](PnpObjectRaisePropertyChangeEvent_function_008F7E94.md) at `0x008F7ED6`
- [_CmAddDeviceToContainerWorker](_CmAddDeviceToContainerWorker_function_008FF2EC.md) at `0x008FF4F0`

### Static image references
- `0x008F80F7` → RVA `0x00E0A740` (`.data`; read)
- `0x008F8152` → RVA `0x008F8600` (`PiPnpRtlObjectEventCallback`; read)
- `0x008F8191` → RVA `0x00001D48` (`.rdata`; read)
- `0x008F8217` → RVA `0x00001E90` (`.rdata`; read)
- `0x008F828E` → RVA `0x00011568` (`.rdata`; read)
- `0x008F82B2` → RVA `0x00001D20` (`.rdata`; read)
- `0x008F8372` → RVA `0x000115B8` (`.rdata`; read)
- `0x008F837F` → RVA `0x000115C0` (`.rdata`; read)
- `0x008F83DF` → RVA `0x00011460` (`.rdata`; read)
- `0x008F83EC` → RVA `0x00011468` (`.rdata`; read)
- `0x008F8438` → RVA `0x00011590` (`.rdata`; read)
- `0x008F8478` → RVA `0x00001E98` (`.rdata`; read)
- `0x008F8531` → RVA `0x0082DD40` (`PnpUpdateInterfacesCallback`; read)
- `0x008F857A` → RVA `0x00011728` (`.rdata`; read)
- `0x008F8587` → RVA `0x00011730` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x008F81F5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F8303` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008F83D2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F8420` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F843F` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x008F84E3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F856D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F859F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F85CE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F80E0  40 55                           push rbp
008F80E2  53                              push rbx
008F80E3  56                              push rsi
008F80E4  57                              push rdi
008F80E5  41 54                           push r12
008F80E7  41 55                           push r13
008F80E9  41 57                           push r15
008F80EB  48 8D 6C 24 D0                  lea rbp, [rsp - 0x30]
008F80F0  48 81 EC 30 01 00 00            sub rsp, 0x130
008F80F7  48 8B 05 42 26 51 00            mov rax, qword ptr [rip + 0x512642]
008F80FE  48 33 C4                        xor rax, rsp
008F8101  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
008F8105  48 8B 9D 90 00 00 00            mov rbx, qword ptr [rbp + 0x90]
008F810C  0F 57 C0                        xorps xmm0, xmm0
008F810F  4C 8B AD 98 00 00 00            mov r13, qword ptr [rbp + 0x98]
008F8116  49 8B F0                        mov rsi, r8
008F8119  4C 89 45 98                     mov qword ptr [rbp - 0x68], r8
008F811D  49 8B F9                        mov rdi, r9
008F8120  45 33 C0                        xor r8d, r8d
008F8123  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
008F8127  44 89 45 90                     mov dword ptr [rbp - 0x70], r8d
008F812B  4C 8B E1                        mov r12, rcx
008F812E  44 89 45 80                     mov dword ptr [rbp - 0x80], r8d
008F8132  F3 0F 7F 44 24 70               movdqu xmmword ptr [rsp + 0x70], xmm0
008F8138  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
008F813C  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
008F8140  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
008F8144  4D 85 C9                        test r9, r9
008F8147  0F 84 08 02 00 00               je 0x1408f8355
008F814D  44 88 44 24 60                  mov byte ptr [rsp + 0x60], r8b
008F8152  48 8D 05 A7 04 00 00            lea rax, [rip + 0x4a7]
008F8159  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008F815E  41 B9 04 00 00 00               mov r9d, 4
008F8164  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
008F8169  4C 3B E8                        cmp r13, rax
008F816C  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
008F8171  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008F8176  49 8B CC                        mov rcx, r12
008F8179  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F817E  45 8D 41 FD                     lea r8d, [r9 - 3]
008F8182  0F 85 14 04 00 00               jne 0x1408f859c
008F8188  E8 73 04 00 00                  call 0x1408f8600
008F818D  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
008F8191  48 8D 3D B0 9B 70 FF            lea rdi, [rip - 0x8f6450]
008F8198  BE 0E 00 00 00                  mov esi, 0xe
008F819D  44 8B 0F                        mov r9d, dword ptr [rdi]
008F81A0  33 D2                           xor edx, edx
008F81A2  41 3B D1                        cmp edx, r9d
008F81A5  73 53                           jae 0x1408f81fa
008F81A7  48 8B 47 F8                     mov rax, qword ptr [rdi - 8]
008F81AB  4C 8B 04 D0                     mov r8, qword ptr [rax + rdx*8]
008F81AF  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
008F81B3  39 43 10                        cmp dword ptr [rbx + 0x10], eax
008F81B6  74 04                           je 0x1408f81bc
008F81B8  FF C2                           inc edx
008F81BA  EB E6                           jmp 0x1408f81a2
008F81BC  48 8B 0B                        mov rcx, qword ptr [rbx]
008F81BF  49 2B 08                        sub rcx, qword ptr [r8]
008F81C2  75 08                           jne 0x1408f81cc
008F81C4  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008F81C8  49 2B 48 08                     sub rcx, qword ptr [r8 + 8]
008F81CC  48 85 C9                        test rcx, rcx
008F81CF  75 E7                           jne 0x1408f81b8
008F81D1  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F81D5  44 8D 49 04                     lea r9d, [rcx + 4]
008F81D9  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008F81DE  44 8D 41 01                     lea r8d, [rcx + 1]
008F81E2  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008F81E7  49 8B D7                        mov rdx, r15
008F81EA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F81EF  49 8B CC                        mov rcx, r12
008F81F2  49 8B C5                        mov rax, r13
008F81F5  E8 D6 28 DC FF                  call 0x1406baad0
008F81FA  48 83 C7 18                     add rdi, 0x18
008F81FE  48 83 EE 01                     sub rsi, 1
008F8202  75 99                           jne 0x1408f819d
008F8204  44 8A 7C 24 60                  mov r15b, byte ptr [rsp + 0x60]
008F8209  33 D2                           xor edx, edx
008F820B  83 FA 03                        cmp edx, 3
008F820E  73 36                           jae 0x1408f8246
008F8210  4C 8D 14 52                     lea r10, [rdx + rdx*2]
008F8214  45 33 C0                        xor r8d, r8d
008F8217  48 8D 3D 72 9C 70 FF            lea rdi, [rip - 0x8f638e]
008F821E  46 8B 5C D7 08                  mov r11d, dword ptr [rdi + r10*8 + 8]
008F8223  45 3B C3                        cmp r8d, r11d
008F8226  73 1A                           jae 0x1408f8242
008F8228  4A 8B 04 D7                     mov rax, qword ptr [rdi + r10*8]
008F822C  4E 8B 0C C0                     mov r9, qword ptr [rax + r8*8]
008F8230  41 8B 41 10                     mov eax, dword ptr [r9 + 0x10]
008F8234  39 43 10                        cmp dword ptr [rbx + 0x10], eax
008F8237  0F 84 DE 00 00 00               je 0x1408f831b
008F823D  41 FF C0                        inc r8d
008F8240  EB E1                           jmp 0x1408f8223
008F8242  FF C2                           inc edx
008F8244  EB C5                           jmp 0x1408f820b
008F8246  40 32 FF                        xor dil, dil
008F8249  45 84 FF                        test r15b, r15b
008F824C  0F 84 3F 01 00 00               je 0x1408f8391
008F8252  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
008F8257  48 8D 45 80                     lea rax, [rbp - 0x80]
008F825B  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
008F825F  41 B8 01 00 00 00               mov r8d, 1
008F8265  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
008F8269  48 8B D6                        mov rdx, rsi
008F826C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008F8271  49 8B CC                        mov rcx, r12
008F8274  C7 44 24 40 10 00 00 00         mov dword ptr [rsp + 0x40], 0x10
008F827C  48 8D 45 C0                     lea rax, [rbp - 0x40]
008F8280  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F8285  48 8D 45 90                     lea rax, [rbp - 0x70]
008F8289  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F828E  48 8D 05 D3 92 71 FF            lea rax, [rip - 0x8e6d2d]
008F8295  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F829A  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
008F82A0  E8 DB 9E FE FF                  call 0x1408e2180
008F82A5  3D 25 02 00 C0                  cmp eax, 0xc0000225
008F82AA  0F 85 F3 00 00 00               jne 0x1408f83a3
008F82B0  33 D2                           xor edx, edx
008F82B2  48 8D 3D 67 9A 70 FF            lea rdi, [rip - 0x8f6599]
008F82B9  83 FA 01                        cmp edx, 1
008F82BC  73 2B                           jae 0x1408f82e9
008F82BE  4C 8D 14 52                     lea r10, [rdx + rdx*2]
008F82C2  45 33 C0                        xor r8d, r8d
008F82C5  46 8B 5C D7 08                  mov r11d, dword ptr [rdi + r10*8 + 8]
008F82CA  45 3B C3                        cmp r8d, r11d
008F82CD  73 16                           jae 0x1408f82e5
008F82CF  4A 8B 04 D7                     mov rax, qword ptr [rdi + r10*8]
008F82D3  4E 8B 0C C0                     mov r9, qword ptr [rax + r8*8]
008F82D7  41 8B 41 10                     mov eax, dword ptr [r9 + 0x10]
008F82DB  39 43 10                        cmp dword ptr [rbx + 0x10], eax
008F82DE  74 5C                           je 0x1408f833c
008F82E0  41 FF C0                        inc r8d
008F82E3  EB E5                           jmp 0x1408f82ca
008F82E5  FF C2                           inc edx
008F82E7  EB D0                           jmp 0x1408f82b9
008F82E9  32 C0                           xor al, al
008F82EB  45 84 FF                        test r15b, r15b
008F82EE  0F 85 03 02 00 00               jne 0x1408f84f7
008F82F4  84 C0                           test al, al
008F82F6  0F 85 FB 01 00 00               jne 0x1408f84f7
008F82FC  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
008F8300  48 33 CC                        xor rcx, rsp
008F8303  E8 38 43 DB FF                  call 0x1406ac640
008F8308  48 81 C4 30 01 00 00            add rsp, 0x130
008F830F  41 5F                           pop r15
008F8311  41 5D                           pop r13
008F8313  41 5C                           pop r12
008F8315  5F                              pop rdi
008F8316  5E                              pop rsi
008F8317  5B                              pop rbx
008F8318  5D                              pop rbp
008F8319  C3                              ret
008F831A  CC                              int3
008F831B  48 8B 0B                        mov rcx, qword ptr [rbx]
008F831E  49 2B 09                        sub rcx, qword ptr [r9]
008F8321  75 08                           jne 0x1408f832b
008F8323  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008F8327  49 2B 49 08                     sub rcx, qword ptr [r9 + 8]
008F832B  48 85 C9                        test rcx, rcx
008F832E  0F 85 09 FF FF FF               jne 0x1408f823d
008F8334  40 B7 01                        mov dil, 1
008F8337  E9 0D FF FF FF                  jmp 0x1408f8249
008F833C  48 8B 0B                        mov rcx, qword ptr [rbx]
008F833F  49 2B 09                        sub rcx, qword ptr [r9]
008F8342  75 08                           jne 0x1408f834c
008F8344  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008F8348  49 2B 49 08                     sub rcx, qword ptr [r9 + 8]
008F834C  48 85 C9                        test rcx, rcx
008F834F  75 8F                           jne 0x1408f82e0
008F8351  B0 01                           mov al, 1
008F8353  EB 96                           jmp 0x1408f82eb
008F8355  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
008F8358  83 F9 06                        cmp ecx, 6
008F835B  74 7F                           je 0x1408f83dc
008F835D  83 F9 64                        cmp ecx, 0x64
008F8360  0F 84 11 02 00 00               je 0x1408f8577
008F8366  83 F9 65                        cmp ecx, 0x65
008F8369  0F 85 DE FD FF FF               jne 0x1408f814d
008F836F  48 8B 03                        mov rax, qword ptr [rbx]
008F8372  48 2B 05 3F 92 71 FF            sub rax, qword ptr [rip - 0x8e6dc1]
008F8379  75 0B                           jne 0x1408f8386
008F837B  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008F837F  48 2B 05 3A 92 71 FF            sub rax, qword ptr [rip - 0x8e6dc6]
008F8386  48 85 C0                        test rax, rax
008F8389  0F 85 BE FD FF FF               jne 0x1408f814d
008F838F  EB 6B                           jmp 0x1408f83fc
008F8391  40 84 FF                        test dil, dil
008F8394  0F 85 B8 FE FF FF               jne 0x1408f8252
008F839A  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
008F839E  E9 0D FF FF FF                  jmp 0x1408f82b0
008F83A3  3D 34 00 00 C0                  cmp eax, 0xc0000034
008F83A8  0F 84 02 FF FF FF               je 0x1408f82b0
008F83AE  85 C0                           test eax, eax
008F83B0  79 7C                           jns 0x1408f842e
008F83B2  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
008F83B8  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008F83BD  33 D2                           xor edx, edx
008F83BF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F83C4  49 8B CC                        mov rcx, r12
008F83C7  49 8B C5                        mov rax, r13
008F83CA  44 8D 4A 01                     lea r9d, [rdx + 1]
008F83CE  44 8D 42 05                     lea r8d, [rdx + 5]
008F83D2  E8 F9 26 DC FF                  call 0x1406baad0
008F83D7  E9 D4 FE FF FF                  jmp 0x1408f82b0
008F83DC  48 8B 03                        mov rax, qword ptr [rbx]
008F83DF  48 2B 05 7A 90 71 FF            sub rax, qword ptr [rip - 0x8e6f86]
008F83E6  75 0B                           jne 0x1408f83f3
008F83E8  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008F83EC  48 2B 05 75 90 71 FF            sub rax, qword ptr [rip - 0x8e6f8b]
008F83F3  48 85 C0                        test rax, rax
008F83F6  0F 85 61 FF FF FF               jne 0x1408f835d
008F83FC  41 B9 05 00 00 00               mov r9d, 5
008F8402  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
008F8407  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008F840C  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
008F8411  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F8416  49 8B CC                        mov rcx, r12
008F8419  49 8B C5                        mov rax, r13
008F841C  45 8D 41 FC                     lea r8d, [r9 - 4]
008F8420  E8 AB 26 DC FF                  call 0x1406baad0
008F8425  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
008F8429  E9 24 FD FF FF                  jmp 0x1408f8152
008F842E  41 B8 10 00 00 00               mov r8d, 0x10
008F8434  48 8D 55 C0                     lea rdx, [rbp - 0x40]
008F8438  48 8D 0D 51 91 71 FF            lea rcx, [rip - 0x8e6eaf]
008F843F  E8 2C 22 DC FF                  call 0x1406ba670
008F8444  48 83 F8 10                     cmp rax, 0x10
008F8448  0F 84 62 FE FF FF               je 0x1408f82b0
008F844E  48 8D 55 D0                     lea rdx, [rbp - 0x30]
008F8452  48 8D 4D C0                     lea rcx, [rbp - 0x40]
008F8456  E8 D1 D5 FF FF                  call 0x1408f5a2c
008F845B  85 C0                           test eax, eax
008F845D  0F 88 4F FF FF FF               js 0x1408f83b2
008F8463  45 84 FF                        test r15b, r15b
008F8466  0F 85 3D 01 00 00               jne 0x1408f85a9
008F846C  40 84 FF                        test dil, dil
008F846F  0F 84 3B FE FF FF               je 0x1408f82b0
008F8475  0F 57 C0                        xorps xmm0, xmm0
008F8478  48 8D 3D 19 9A 70 FF            lea rdi, [rip - 0x8f65e7]
008F847F  F3 0F 7F 44 24 68               movdqu xmmword ptr [rsp + 0x68], xmm0
008F8485  BE 03 00 00 00                  mov esi, 3
008F848A  44 8B 0F                        mov r9d, dword ptr [rdi]
008F848D  33 D2                           xor edx, edx
008F848F  41 3B D1                        cmp edx, r9d
008F8492  73 54                           jae 0x1408f84e8
008F8494  48 8B 47 F8                     mov rax, qword ptr [rdi - 8]
008F8498  4C 8B 04 D0                     mov r8, qword ptr [rax + rdx*8]
008F849C  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
008F84A0  39 43 10                        cmp dword ptr [rbx + 0x10], eax
008F84A3  74 04                           je 0x1408f84a9
008F84A5  FF C2                           inc edx
008F84A7  EB E6                           jmp 0x1408f848f
008F84A9  48 8B 0B                        mov rcx, qword ptr [rbx]
008F84AC  49 2B 08                        sub rcx, qword ptr [r8]
008F84AF  75 08                           jne 0x1408f84b9
008F84B1  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008F84B5  49 2B 48 08                     sub rcx, qword ptr [r8 + 8]
008F84B9  48 85 C9                        test rcx, rcx
008F84BC  75 E7                           jne 0x1408f84a5
008F84BE  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008F84C2  44 8D 49 04                     lea r9d, [rcx + 4]
008F84C6  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008F84CB  44 8D 41 05                     lea r8d, [rcx + 5]
008F84CF  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008F84D4  49 8B CC                        mov rcx, r12
008F84D7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F84DC  48 8D 55 D0                     lea rdx, [rbp - 0x30]
008F84E0  49 8B C5                        mov rax, r13
008F84E3  E8 E8 25 DC FF                  call 0x1406baad0
008F84E8  48 83 C7 18                     add rdi, 0x18
008F84EC  48 83 EE 01                     sub rsi, 1
008F84F0  75 98                           jne 0x1408f848a
008F84F2  E9 A3 FE FF FF                  jmp 0x1408f839a
008F84F7  4C 89 6D A0                     mov qword ptr [rbp - 0x60], r13
008F84FB  44 88 7D BC                     mov byte ptr [rbp - 0x44], r15b
008F84FF  84 C0                           test al, al
008F8501  0F 85 D1 00 00 00               jne 0x1408f85d8
008F8507  83 64 24 48 00                  and dword ptr [rsp + 0x48], 0
008F850C  48 8D 45 80                     lea rax, [rbp - 0x80]
008F8510  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008F8515  45 33 C9                        xor r9d, r9d
008F8518  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
008F851D  48 8D 45 A0                     lea rax, [rbp - 0x60]
008F8521  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
008F8527  4C 8B C6                        mov r8, rsi
008F852A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F852F  33 D2                           xor edx, edx
008F8531  48 8D 05 08 58 F3 FF            lea rax, [rip - 0xca7f8]
008F8538  49 8B CC                        mov rcx, r12
008F853B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F8540  E8 CB 10 11 00                  call 0x140a09610
008F8545  85 C0                           test eax, eax
008F8547  0F 89 AF FD FF FF               jns 0x1408f82fc
008F854D  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
008F8553  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008F8558  33 D2                           xor edx, edx
008F855A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F855F  49 8B CC                        mov rcx, r12
008F8562  49 8B C5                        mov rax, r13
008F8565  44 8D 4A 01                     lea r9d, [rdx + 1]
008F8569  44 8D 42 03                     lea r8d, [rdx + 3]
008F856D  E8 5E 25 DC FF                  call 0x1406baad0
008F8572  E9 85 FD FF FF                  jmp 0x1408f82fc
008F8577  48 8B 03                        mov rax, qword ptr [rbx]
008F857A  48 2B 05 A7 91 71 FF            sub rax, qword ptr [rip - 0x8e6e59]
008F8581  75 0B                           jne 0x1408f858e
008F8583  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008F8587  48 2B 05 A2 91 71 FF            sub rax, qword ptr [rip - 0x8e6e5e]
008F858E  48 85 C0                        test rax, rax
008F8591  0F 84 65 FE FF FF               je 0x1408f83fc
008F8597  E9 CA FD FF FF                  jmp 0x1408f8366
008F859C  49 8B C5                        mov rax, r13
008F859F  E8 2C 25 DC FF                  call 0x1406baad0
008F85A4  E9 E4 FB FF FF                  jmp 0x1408f818d
008F85A9  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
008F85AF  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008F85B4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F85B9  48 8D 55 D0                     lea rdx, [rbp - 0x30]
008F85BD  B8 05 00 00 00                  mov eax, 5
008F85C2  49 8B CC                        mov rcx, r12
008F85C5  44 8B C8                        mov r9d, eax
008F85C8  44 8B C0                        mov r8d, eax
008F85CB  49 8B C5                        mov rax, r13
008F85CE  E8 FD 24 DC FF                  call 0x1406baad0
008F85D3  E9 94 FE FF FF                  jmp 0x1408f846c
008F85D8  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
008F85DC  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
008F85E0  C7 45 B8 01 00 00 00            mov dword ptr [rbp - 0x48], 1
008F85E7  E9 1B FF FF FF                  jmp 0x1408f8507
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpDeviceRaisePropertyChangeEventWorker(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int8 v_stack_m108;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int8 v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int8 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 5318210)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mD0 = a3;
    a3 = 0;
    v_stack_mE0 = a2;
    v_stack_mD8 = 0;
    v_stack_mE8 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    if (a4 == 0) goto loc_008F8355;
loc_008F814D:
    v_stack_m108 = 0;
loc_008F8152:
    v_stack_m100 = 0;
    v_stack_mF8 = a4;
    v_stack_mF0 = a5;
    v_stack_m148 = v_stack_m100;
    if (a6 != (v_rip + 1191)) goto loc_008F859C;
    result = PiPnpRtlObjectEventCallback(a1, a2, 4 - 3, 4);
loc_008F818D:
loc_008F819D:
    a2 = 0;
loc_008F81A2:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 9397328))))) goto loc_008F81FA;
    if ((*(unsigned int *)(a5 + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397328 - 8) + a2 * 8) + 16))))) goto loc_008F81BC;
loc_008F81B8:
    a2 = (unsigned int)((a2) + 1);
    goto loc_008F81A2;
loc_008F81BC:
    a1 = (*(unsigned __int64 *)(a5)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397328 - 8) + a2 * 8)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a5 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397328 - 8) + a2 * 8) + 8));
    }
    if (a1 != 0) goto loc_008F81B8;
    v_stack_mF0 = *(unsigned __int64 *)(v_rip - 9397328 + 8);
    v_stack_m148 = v_stack_m100;
    result = guard_dispatch_icall(a1, v_stack_mE0, a1 + 1, a1 + 4);
loc_008F81FA:
    v_rdi = (v_rip - 9397328) + (24);
    v_rsi = (14) - (1);
    if (condition_is_not_equal) goto loc_008F819D;
    a2 = 0;
loc_008F820B:
    if (0 >= 3) goto loc_008F8246;
    a3 = 0;
loc_008F8223:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 9397134 + a2 + a2 * 2 * 8 + 8))))) goto loc_008F8242;
    if ((*(unsigned int *)(a5 + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397134 + a2 + a2 * 2 * 8) + a3 * 8) + 16))))) goto loc_008F831B;
loc_008F823D:
    a3 = (unsigned int)((a3) + 1);
    goto loc_008F8223;
loc_008F8242:
    a2 = (unsigned int)((a2) + 1);
    goto loc_008F820B;
loc_008F8246:
    v_rdi = 0;
loc_008F8249:
    if ((unsigned __int8)(v_stack_m108) == 0) goto loc_008F8391;
loc_008F8252:
    v_stack_m120 = v_stack_mE8;
    v_stack_m128 = 16;
    v_stack_m130 = v_stack_mA8;
    v_stack_m138 = v_stack_mD8;
    v_stack_m140 = v_rip - 9334061;
    result = PnpGetObjectProperty(a1, v_stack_mE0, 1, v_stack_mD0);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_008F83A3;
loc_008F82B0:
    a2 = 0;
loc_008F82B9:
    if (0 >= 1) goto loc_008F82E9;
    a3 = 0;
loc_008F82CA:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 9397657 + a2 + a2 * 2 * 8 + 8))))) goto loc_008F82E5;
    if ((*(unsigned int *)(a5 + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397657 + a2 + a2 * 2 * 8) + a3 * 8) + 16))))) goto loc_008F833C;
loc_008F82E0:
    a3 = (unsigned int)((a3) + 1);
    goto loc_008F82CA;
loc_008F82E5:
    a2 = (unsigned int)((a2) + 1);
    goto loc_008F82B9;
loc_008F82E9:
    result = 0;
loc_008F82EB:
    if ((unsigned __int8)(v_stack_m108) != 0) goto loc_008F84F7;
    if (0 != 0) goto loc_008F84F7;
loc_008F82FC:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397657 + a2 + a2 * 2 * 8) + a3 * 8));
    v_rsp = (v_rsp) + (304);
    return result;
loc_008F831B:
    a1 = (*(unsigned __int64 *)(a5)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397657 + a2 + a2 * 2 * 8) + a3 * 8)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a5 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397657 + a2 + a2 * 2 * 8) + a3 * 8) + 8));
    }
    if (a1 != 0) goto loc_008F823D;
    goto loc_008F8249;
loc_008F833C:
    a1 = (*(unsigned __int64 *)(a5)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397657 + a2 + a2 * 2 * 8) + a3 * 8)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a5 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397657 + a2 + a2 * 2 * 8) + a3 * 8) + 8));
    }
    if (a1 != 0) goto loc_008F82E0;
    goto loc_008F82EB;
loc_008F8355:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)))) == 6) goto loc_008F83DC;
loc_008F835D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)))) == 100) goto loc_008F8577;
loc_008F8366:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)))) != 101) goto loc_008F814D;
    result = (*(unsigned __int64 *)(a5)) - (*(unsigned __int64 *)(v_rip - 9334209));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a5 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9334214));
    }
    if (result != 0) goto loc_008F814D;
    goto loc_008F83FC;
loc_008F8391:
    if (1 != 0) goto loc_008F8252;
loc_008F839A:
    goto loc_008F82B0;
loc_008F83A3:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_008F82B0;
    if (!sign_flag) goto loc_008F842E;
loc_008F83B2:
    a2 = 0;
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(a1, a2, a2 + 5, a2 + 1);
    goto loc_008F82B0;
loc_008F83DC:
    result = (*(unsigned __int64 *)(a5)) - (*(unsigned __int64 *)(v_rip - 9334662));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a5 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9334667));
    }
    if (result != 0) goto loc_008F835D;
loc_008F83FC:
    v_stack_p68 = a2 + 5;
    v_stack_p60 = 1;
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(a1, a2, 5 - 4, 5);
    goto loc_008F8152;
loc_008F842E:
    result = RtlCompareMemory(v_rip - 9334447, v_stack_mA8, 16, 5);
    if (result == 16) goto loc_008F82B0;
    result = PnpStringFromGuid(v_stack_mA8, v_stack_m98, 16, 5);
    if (sign_flag) goto loc_008F83B2;
    if ((unsigned __int8)(v_stack_m108) != 0) goto loc_008F85A9;
loc_008F846C:
    if (1 == 0) goto loc_008F82B0;
    v_stack_p68 = v_xmm0;
loc_008F848A:
    a2 = 0;
loc_008F848F:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 9397735))))) goto loc_008F84E8;
    if ((*(unsigned int *)(a5 + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397735 - 8) + a2 * 8) + 16))))) goto loc_008F84A9;
loc_008F84A5:
    a2 = (unsigned int)((a2) + 1);
    goto loc_008F848F;
loc_008F84A9:
    a1 = (*(unsigned __int64 *)(a5)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397735 - 8) + a2 * 8)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a5 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9397735 - 8) + a2 * 8) + 8));
    }
    if (a1 != 0) goto loc_008F84A5;
    v_stack_p78 = *(unsigned __int64 *)(v_rip - 9397735 + 8);
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(a1, v_stack_m98, a1 + 5, a1 + 4);
loc_008F84E8:
    v_rdi = (v_rip - 9397735) + (24);
    v_rsi = (3) - (1);
    if (condition_is_not_equal) goto loc_008F848A;
    goto loc_008F839A;
loc_008F84F7:
    v_stack_mC8 = a6;
    v_stack_mAC = (unsigned __int8)(v_stack_m108);
    if ((unsigned __int8)(result) != 0) goto loc_008F85D8;
loc_008F8507:
    v_stack_p40 = v_stack_mE8;
    a4 = 0;
    v_stack_p28 = v_stack_mC8;
    a2 = 0;
    v_stack_p20 = v_rip - 829432;
    result = _CmGetMatchingFilteredDeviceInterfaceList(a1, a2, v_rsi, a4);
    if (!sign_flag) goto loc_008F82FC;
    a2 = 0;
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(a1, a2, a2 + 3, a2 + 1);
    goto loc_008F82FC;
loc_008F8577:
    result = (*(unsigned __int64 *)(a5)) - (*(unsigned __int64 *)(v_rip - 9334361));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a5 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9334366));
    }
    if (result == 0) goto loc_008F83FC;
    goto loc_008F8366;
loc_008F859C:
    result = guard_dispatch_icall(a1, a2, a2 + 3, a2 + 1);
    goto loc_008F818D;
loc_008F85A9:
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(a1, v_stack_m98, 5, 5);
    goto loc_008F846C;
loc_008F85D8:
    v_stack_mC0 = a5;
    v_stack_mB8 = v_rdi;
    v_stack_mB0 = 1;
    goto loc_008F8507;
}
```

## 5. (Beta) C Style

```c
int64_t PnpDeviceRaisePropertyChangeEventWorker(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint8_t v_stack_m108;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m68;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint8_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint8_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x512642)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mD0 = Arg3;
    Arg3 = 0;
    v_stack_mE0 = Arg2;
    v_stack_mD8 = 0;
    v_stack_mE8 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    if (Arg4 == 0) goto loc_008F8355;
loc_008F814D:
    v_stack_m108 = 0;
loc_008F8152:
    v_stack_m100 = 0;
    v_stack_mF8 = Arg4;
    v_stack_mF0 = Arg5;
    v_stack_m148 = v_stack_m100;
    if (Arg6 != (v_rip + 1191)) goto loc_008F859C;
    result = PiPnpRtlObjectEventCallback(Arg1, Arg2, 4 - 3, 4);
loc_008F818D:
loc_008F819D:
    Arg2 = 0;
loc_008F81A2:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x8F6450))))) goto loc_008F81FA;
    if ((*(uint32_t *)(arg5 + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6450 - 0x8) + Arg2 * 8) + 0x10))))) goto loc_008F81BC;
loc_008F81B8:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_008F81A2;
loc_008F81BC:
    Arg1 = (*(uint64_t *)(arg5)) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6450 - 0x8) + Arg2 * 8)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg5 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6450 - 0x8) + Arg2 * 8) + 0x8));
    }
    if (Arg1 != 0) goto loc_008F81B8;
    v_stack_mF0 = *(uint64_t *)(v_rip - 0x8F6450 + 0x8);
    v_stack_m148 = v_stack_m100;
    result = guard_dispatch_icall(Arg1, v_stack_mE0, Arg1 + 1, Arg1 + 4);
loc_008F81FA:
    local_rdi = (v_rip - 9397328) + (24);
    local_rsi = (14) - (1);
    if (condition_is_not_equal) goto loc_008F819D;
    Arg2 = 0;
loc_008F820B:
    if (0 >= 3) goto loc_008F8246;
    Arg3 = 0;
loc_008F8223:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x8F638E + Arg2 + Arg2 * 2 * 8 + 0x8))))) goto loc_008F8242;
    if ((*(uint32_t *)(arg5 + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F638E + Arg2 + Arg2 * 2 * 8) + Arg3 * 8) + 0x10))))) goto loc_008F831B;
loc_008F823D:
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_008F8223;
loc_008F8242:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_008F820B;
loc_008F8246:
    local_rdi = 0;
loc_008F8249:
    if ((uint8_t)(v_stack_m108) == 0) goto loc_008F8391;
loc_008F8252:
    v_stack_m120 = v_stack_mE8;
    v_stack_m128 = 16;
    v_stack_m130 = v_stack_mA8;
    v_stack_m138 = v_stack_mD8;
    v_stack_m140 = v_rip - 9334061;
    result = PnpGetObjectProperty(Arg1, v_stack_mE0, 1, v_stack_mD0);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_008F83A3;
loc_008F82B0:
    Arg2 = 0;
loc_008F82B9:
    if (0 >= 1) goto loc_008F82E9;
    Arg3 = 0;
loc_008F82CA:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x8F6599 + Arg2 + Arg2 * 2 * 8 + 0x8))))) goto loc_008F82E5;
    if ((*(uint32_t *)(arg5 + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6599 + Arg2 + Arg2 * 2 * 8) + Arg3 * 8) + 0x10))))) goto loc_008F833C;
loc_008F82E0:
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_008F82CA;
loc_008F82E5:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_008F82B9;
loc_008F82E9:
    result = 0;
loc_008F82EB:
    if ((uint8_t)(v_stack_m108) != 0) goto loc_008F84F7;
    if (0 != 0) goto loc_008F84F7;
loc_008F82FC:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6599 + Arg2 + Arg2 * 2 * 8) + Arg3 * 8));
    local_rsp = (local_rsp) + (304);
    return result;
loc_008F831B:
    Arg1 = (*(uint64_t *)(arg5)) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6599 + Arg2 + Arg2 * 2 * 8) + Arg3 * 8)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg5 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6599 + Arg2 + Arg2 * 2 * 8) + Arg3 * 8) + 0x8));
    }
    if (Arg1 != 0) goto loc_008F823D;
    goto loc_008F8249;
loc_008F833C:
    Arg1 = (*(uint64_t *)(arg5)) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6599 + Arg2 + Arg2 * 2 * 8) + Arg3 * 8)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg5 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F6599 + Arg2 + Arg2 * 2 * 8) + Arg3 * 8) + 0x8));
    }
    if (Arg1 != 0) goto loc_008F82E0;
    goto loc_008F82EB;
loc_008F8355:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)))) == 6) goto loc_008F83DC;
loc_008F835D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)))) == 100) goto loc_008F8577;
loc_008F8366:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)))) != 101) goto loc_008F814D;
    result = (*(uint64_t *)(arg5)) - (*(uint64_t *)(v_rip - 0x8E6DC1));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg5 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E6DC6));
    }
    if (result != 0) goto loc_008F814D;
    goto loc_008F83FC;
loc_008F8391:
    if (1 != 0) goto loc_008F8252;
loc_008F839A:
    goto loc_008F82B0;
loc_008F83A3:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_008F82B0;
    if (!sign_flag) goto loc_008F842E;
loc_008F83B2:
    Arg2 = 0;
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 5, Arg2 + 1);
    goto loc_008F82B0;
loc_008F83DC:
    result = (*(uint64_t *)(arg5)) - (*(uint64_t *)(v_rip - 0x8E6F86));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg5 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E6F8B));
    }
    if (result != 0) goto loc_008F835D;
loc_008F83FC:
    v_stack_p68 = Arg2 + 5;
    v_stack_p60 = 1;
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(Arg1, Arg2, 5 - 4, 5);
    goto loc_008F8152;
loc_008F842E:
    result = RtlCompareMemory(v_rip - 9334447, v_stack_mA8, 16, 5);
    if (result == 16) goto loc_008F82B0;
    result = PnpStringFromGuid(v_stack_mA8, v_stack_m98, 16, 5);
    if (sign_flag) goto loc_008F83B2;
    if ((uint8_t)(v_stack_m108) != 0) goto loc_008F85A9;
loc_008F846C:
    if (1 == 0) goto loc_008F82B0;
    v_stack_p68 = v_xmm0;
loc_008F848A:
    Arg2 = 0;
loc_008F848F:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x8F65E7))))) goto loc_008F84E8;
    if ((*(uint32_t *)(arg5 + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F65E7 - 0x8) + Arg2 * 8) + 0x10))))) goto loc_008F84A9;
loc_008F84A5:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_008F848F;
loc_008F84A9:
    Arg1 = (*(uint64_t *)(arg5)) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F65E7 - 0x8) + Arg2 * 8)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg5 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8F65E7 - 0x8) + Arg2 * 8) + 0x8));
    }
    if (Arg1 != 0) goto loc_008F84A5;
    v_stack_p78 = *(uint64_t *)(v_rip - 0x8F65E7 + 0x8);
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(Arg1, v_stack_m98, Arg1 + 5, Arg1 + 4);
loc_008F84E8:
    local_rdi = (v_rip - 9397735) + (24);
    local_rsi = (3) - (1);
    if (condition_is_not_equal) goto loc_008F848A;
    goto loc_008F839A;
loc_008F84F7:
    v_stack_mC8 = Arg6;
    v_stack_mAC = (uint8_t)(v_stack_m108);
    if ((uint8_t)(result) != 0) goto loc_008F85D8;
loc_008F8507:
    v_stack_p40 = v_stack_mE8;
    Arg4 = 0;
    v_stack_p28 = v_stack_mC8;
    Arg2 = 0;
    v_stack_p20 = v_rip - 829432;
    result = _CmGetMatchingFilteredDeviceInterfaceList(Arg1, Arg2, local_rsi, Arg4);
    if (!sign_flag) goto loc_008F82FC;
    Arg2 = 0;
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 3, Arg2 + 1);
    goto loc_008F82FC;
loc_008F8577:
    result = (*(uint64_t *)(arg5)) - (*(uint64_t *)(v_rip - 0x8E6E59));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg5 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x8E6E5E));
    }
    if (result == 0) goto loc_008F83FC;
    goto loc_008F8366;
loc_008F859C:
    result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 3, Arg2 + 1);
    goto loc_008F818D;
loc_008F85A9:
    v_stack_p20 = v_stack_p68;
    result = guard_dispatch_icall(Arg1, v_stack_m98, 5, 5);
    goto loc_008F846C;
loc_008F85D8:
    v_stack_mC0 = Arg5;
    v_stack_mB8 = local_rdi;
    v_stack_mB0 = 1;
    goto loc_008F8507;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R` |
| `Arg5` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F80E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
