# PnpGetDeviceLocationStrings

- RVA: `0x00A286C0`–`0x00A28D2F` (길이 `1,647` bytes)
- VA: `0x0000000140A286C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC0B4`
- 디코드: `457`개 명령, `1,647/1,647` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A2877D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A287A2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A287F8` → [PnpQueryInterface](PnpQueryInterface_function_00A28D38.md) (function, `0x00A28D38`)
- `0x00A28823` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A28840` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2885D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2886C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2892E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A2894F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2896F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A289C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A28A00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A28A29` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A28B8D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A28D25` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiProcessNewDeviceNode](PiProcessNewDeviceNode_function_00A28F20.md) at `0x00A2A0CC`
- [sub_00B38904](../B3/Unknown_function_00B38904.md) at `0x00B38A8D`

### Static image references
- `0x00A28731` → RVA `0x00F8C438` (`.data`; read)
- `0x00A287DA` → RVA `0x00019F60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00A2877D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A287A2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A28823` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A28840` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2885D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2886C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2892E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A2894F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2896F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A289C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A28A00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A28A29` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A28B8D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A28D25` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A286C0  48 8B C4                        mov rax, rsp
00A286C3  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00A286C7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00A286CB  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A286CF  55                              push rbp
00A286D0  53                              push rbx
00A286D1  56                              push rsi
00A286D2  57                              push rdi
00A286D3  41 54                           push r12
00A286D5  41 55                           push r13
00A286D7  41 56                           push r14
00A286D9  41 57                           push r15
00A286DB  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00A286DF  48 81 EC B8 00 00 00            sub rsp, 0xb8
00A286E6  33 FF                           xor edi, edi
00A286E8  4C 8B F1                        mov r14, rcx
00A286EB  33 C9                           xor ecx, ecx
00A286ED  48 89 7D A7                     mov qword ptr [rbp - 0x59], rdi
00A286F1  0F 57 C0                        xorps xmm0, xmm0
00A286F4  48 89 4D 0F                     mov qword ptr [rbp + 0xf], rcx
00A286F8  83 C9 FF                        or ecx, 0xffffffff
00A286FB  40 88 7D AF                     mov byte ptr [rbp - 0x51], dil
00A286FF  89 4D B3                        mov dword ptr [rbp - 0x4d], ecx
00A28702  49 8B C0                        mov rax, r8
00A28705  89 4D 97                        mov dword ptr [rbp - 0x69], ecx
00A28708  8B F7                           mov esi, edi
00A2870A  48 89 7D D7                     mov qword ptr [rbp - 0x29], rdi
00A2870E  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00A28712  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00A28716  4D 85 F6                        test r14, r14
00A28719  0F 84 32 01 00 00               je 0x140a28851
00A2871F  48 85 D2                        test rdx, rdx
00A28722  0F 84 29 01 00 00               je 0x140a28851
00A28728  48 85 C0                        test rax, rax
00A2872B  0F 84 20 01 00 00               je 0x140a28851
00A28731  48 8B 0D 00 3D 56 00            mov rcx, qword ptr [rip + 0x563d00]
00A28738  48 89 3A                        mov qword ptr [rdx], rdi
00A2873B  41 89 38                        mov dword ptr [r8], edi
00A2873E  4C 3B F1                        cmp r14, rcx
00A28741  0F 84 49 01 00 00               je 0x140a28890
00A28747  44 8B FF                        mov r15d, edi
00A2874A  8D 57 01                        lea edx, [rdi + 1]
00A2874D  49 8B C6                        mov rax, r14
00A28750  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00A28754  44 03 FA                        add r15d, edx
00A28757  48 3B C1                        cmp rax, rcx
00A2875A  75 F4                           jne 0x140a28750
00A2875C  41 BC 50 70 73 75               mov r12d, 0x75737050
00A28762  41 8B DF                        mov ebx, r15d
00A28765  45 8B C4                        mov r8d, r12d
00A28768  44 89 7D CB                     mov dword ptr [rbp - 0x35], r15d
00A2876C  4A 8D 14 FD 00 00 00 00         lea rdx, [r15*8]
00A28774  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
00A28778  B9 00 01 00 00                  mov ecx, 0x100
00A2877D  E8 6E 99 15 00                  call 0x140b820f0
00A28782  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00A28786  4C 8B E8                        mov r13, rax
00A28789  48 85 C0                        test rax, rax
00A2878C  0F 84 3E 05 00 00               je 0x140a28cd0
00A28792  4A 8D 14 BD 00 00 00 00         lea rdx, [r15*4]
00A2879A  45 8B C4                        mov r8d, r12d
00A2879D  B9 00 01 00 00                  mov ecx, 0x100
00A287A2  E8 49 99 15 00                  call 0x140b820f0
00A287A7  45 33 DB                        xor r11d, r11d
00A287AA  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00A287AE  4C 8B E0                        mov r12, rax
00A287B1  48 85 C0                        test rax, rax
00A287B4  0F 84 20 05 00 00               je 0x140a28cda
00A287BA  41 8D 43 01                     lea eax, [r11 + 1]
00A287BE  45 8B EB                        mov r13d, r11d
00A287C1  8B F0                           mov esi, eax
00A287C3  89 45 9B                        mov dword ptr [rbp - 0x65], eax
00A287C6  41 8B DB                        mov ebx, r11d
00A287C9  4C 3B 35 68 3C 56 00            cmp r14, qword ptr [rip + 0x563c68]
00A287D0  0F 84 0F 02 00 00               je 0x140a289e5
00A287D6  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00A287DA  48 8D 15 7F 17 5F FF            lea rdx, [rip - 0xa0e881]
00A287E1  44 8B C0                        mov r8d, eax
00A287E4  41 B9 28 00 00 00               mov r9d, 0x28
00A287EA  48 8D 45 EF                     lea rax, [rbp - 0x11]
00A287EE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A287F3  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00A287F8  E8 3B 05 00 00                  call 0x140a28d38
00A287FD  45 33 DB                        xor r11d, r11d
00A28800  8B F8                           mov edi, eax
00A28802  85 C0                           test eax, eax
00A28804  0F 88 B0 02 00 00               js 0x140a28aba
00A2880A  48 8B 45 0F                     mov rax, qword ptr [rbp + 0xf]
00A2880E  48 85 C0                        test rax, rax
00A28811  0F 84 DF 04 00 00               je 0x140a28cf6
00A28817  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00A2881B  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00A2881F  4C 89 5D A7                     mov qword ptr [rbp - 0x59], r11
00A28823  E8 A8 22 C9 FF                  call 0x1406baad0
00A28828  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00A2882C  45 33 DB                        xor r11d, r11d
00A2882F  8B F8                           mov edi, eax
00A28831  85 C0                           test eax, eax
00A28833  79 62                           jns 0x140a28897
00A28835  48 85 C9                        test rcx, rcx
00A28838  0F 84 24 01 00 00               je 0x140a28962
00A2883E  33 D2                           xor edx, edx
00A28840  E8 2B A0 15 00                  call 0x140b82870
00A28845  45 33 DB                        xor r11d, r11d
00A28848  4C 89 5D A7                     mov qword ptr [rbp - 0x59], r11
00A2884C  E9 11 01 00 00                  jmp 0x140a28962
00A28851  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A28856  EB 23                           jmp 0x140a2887b
00A28858  33 D2                           xor edx, edx
00A2885A  49 8B CD                        mov rcx, r13
00A2885D  E8 0E A0 15 00                  call 0x140b82870
00A28862  4D 85 E4                        test r12, r12
00A28865  74 0A                           je 0x140a28871
00A28867  33 D2                           xor edx, edx
00A28869  49 8B CC                        mov rcx, r12
00A2886C  E8 FF 9F 15 00                  call 0x140b82870
00A28871  85 FF                           test edi, edi
00A28873  0F 88 9E 04 00 00               js 0x140a28d17
00A28879  8B C7                           mov eax, edi
00A2887B  48 81 C4 B8 00 00 00            add rsp, 0xb8
00A28882  41 5F                           pop r15
00A28884  41 5E                           pop r14
00A28886  41 5D                           pop r13
00A28888  41 5C                           pop r12
00A2888A  5F                              pop rdi
00A2888B  5E                              pop rsi
00A2888C  5B                              pop rbx
00A2888D  5D                              pop rbp
00A2888E  C3                              ret
00A2888F  CC                              int3
00A28890  B8 0E 00 00 C0                  mov eax, 0xc000000e
00A28895  EB E4                           jmp 0x140a2887b
00A28897  48 85 C9                        test rcx, rcx
00A2889A  0F 84 44 04 00 00               je 0x140a28ce4
00A288A0  45 8B FD                        mov r15d, r13d
00A288A3  45 8B C3                        mov r8d, r11d
00A288A6  45 8B CB                        mov r9d, r11d
00A288A9  41 8B D3                        mov edx, r11d
00A288AC  47 89 1C BC                     mov dword ptr [r12 + r15*4], r11d
00A288B0  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00A288B4  66 44 39 19                     cmp word ptr [rcx], r11w
00A288B8  74 56                           je 0x140a28910
00A288BA  41 BE 01 00 00 00               mov r14d, 1
00A288C0  49 83 CA FF                     or r10, 0xffffffffffffffff
00A288C4  45 03 C6                        add r8d, r14d
00A288C7  49 8B C2                        mov rax, r10
00A288CA  47 89 04 BC                     mov dword ptr [r12 + r15*4], r8d
00A288CE  48 FF C0                        inc rax
00A288D1  66 44 39 1C 41                  cmp word ptr [rcx + rax*2], r11w
00A288D6  75 F6                           jne 0x140a288ce
00A288D8  FF C0                           inc eax
00A288DA  44 03 C8                        add r9d, eax
00A288DD  49 8B C2                        mov rax, r10
00A288E0  48 FF C0                        inc rax
00A288E3  66 44 39 1C 41                  cmp word ptr [rcx + rax*2], r11w
00A288E8  75 F6                           jne 0x140a288e0
00A288EA  3B C2                           cmp eax, edx
00A288EC  0F 46 C2                        cmovbe eax, edx
00A288EF  8B D0                           mov edx, eax
00A288F1  49 8B C2                        mov rax, r10
00A288F4  48 FF C0                        inc rax
00A288F7  66 44 39 1C 41                  cmp word ptr [rcx + rax*2], r11w
00A288FC  75 F6                           jne 0x140a288f4
00A288FE  48 8D 0C 41                     lea rcx, [rcx + rax*2]
00A28902  48 83 C1 02                     add rcx, 2
00A28906  66 44 39 19                     cmp word ptr [rcx], r11w
00A2890A  75 B8                           jne 0x140a288c4
00A2890C  4C 8B 75 67                     mov r14, qword ptr [rbp + 0x67]
00A28910  41 0F AF F0                     imul esi, r8d
00A28914  03 DA                           add ebx, edx
00A28916  41 B8 50 70 73 75               mov r8d, 0x75737050
00A2891C  B9 00 01 00 00                  mov ecx, 0x100
00A28921  89 75 9B                        mov dword ptr [rbp - 0x65], esi
00A28924  41 8D 71 01                     lea esi, [r9 + 1]
00A28928  48 03 F6                        add rsi, rsi
00A2892B  48 8B D6                        mov rdx, rsi
00A2892E  E8 BD 97 15 00                  call 0x140b820f0
00A28933  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00A28937  4A 89 04 F9                     mov qword ptr [rcx + r15*8], rax
00A2893B  48 85 C0                        test rax, rax
00A2893E  0F 85 DB 00 00 00               jne 0x140a28a1f
00A28944  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A28949  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00A2894D  33 D2                           xor edx, edx
00A2894F  E8 1C 9F 15 00                  call 0x140b82870
00A28954  44 8B 7D CB                     mov r15d, dword ptr [rbp - 0x35]
00A28958  45 33 DB                        xor r11d, r11d
00A2895B  8B 75 9B                        mov esi, dword ptr [rbp - 0x65]
00A2895E  4C 89 5D A7                     mov qword ptr [rbp - 0x59], r11
00A28962  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
00A28966  48 85 C0                        test rax, rax
00A28969  74 0C                           je 0x140a28977
00A2896B  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00A2896F  E8 5C 21 C9 FF                  call 0x1406baad0
00A28974  45 33 DB                        xor r11d, r11d
00A28977  85 FF                           test edi, edi
00A28979  78 21                           js 0x140a2899c
00A2897B  81 FF 20 01 00 00               cmp edi, 0x120
00A28981  74 5B                           je 0x140a289de
00A28983  45 3B EF                        cmp r13d, r15d
00A28986  74 56                           je 0x140a289de
00A28988  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
00A2898C  B8 01 00 00 00                  mov eax, 1
00A28991  03 D8                           add ebx, eax
00A28993  4C 89 75 67                     mov qword ptr [rbp + 0x67], r14
00A28997  E9 2D FE FF FF                  jmp 0x140a287c9
00A2899C  48 8B 75 D7                     mov rsi, qword ptr [rbp - 0x29]
00A289A0  4C 8B 6D BF                     mov r13, qword ptr [rbp - 0x41]
00A289A4  44 39 5D CB                     cmp dword ptr [rbp - 0x35], r11d
00A289A8  0F 86 AA FE FF FF               jbe 0x140a28858
00A289AE  4C 8B 75 E7                     mov r14, qword ptr [rbp - 0x19]
00A289B2  49 8B DD                        mov rbx, r13
00A289B5  B8 01 00 00 00                  mov eax, 1
00A289BA  48 8B 0B                        mov rcx, qword ptr [rbx]
00A289BD  48 85 C9                        test rcx, rcx
00A289C0  74 0E                           je 0x140a289d0
00A289C2  33 D2                           xor edx, edx
00A289C4  E8 A7 9E 15 00                  call 0x140b82870
00A289C9  45 33 DB                        xor r11d, r11d
00A289CC  41 8D 43 01                     lea eax, [r11 + 1]
00A289D0  48 83 C3 08                     add rbx, 8
00A289D4  4C 2B F0                        sub r14, rax
00A289D7  75 E1                           jne 0x140a289ba
00A289D9  E9 7A FE FF FF                  jmp 0x140a28858
00A289DE  B8 01 00 00 00                  mov eax, 1
00A289E3  03 D8                           add ebx, eax
00A289E5  0F AF DE                        imul ebx, esi
00A289E8  B9 00 01 00 00                  mov ecx, 0x100
00A289ED  41 B8 50 70 73 75               mov r8d, 0x75737050
00A289F3  44 89 5D DF                     mov dword ptr [rbp - 0x21], r11d
00A289F7  41 8B FB                        mov edi, r11d
00A289FA  8D 14 18                        lea edx, [rax + rbx]
00A289FD  48 03 D2                        add rdx, rdx
00A28A00  E8 EB 96 15 00                  call 0x140b820f0
00A28A05  45 33 DB                        xor r11d, r11d
00A28A08  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00A28A0C  48 8B F0                        mov rsi, rax
00A28A0F  48 85 C0                        test rax, rax
00A28A12  0F 85 AA 00 00 00               jne 0x140a28ac2
00A28A18  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A28A1D  EB 81                           jmp 0x140a289a0
00A28A1F  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00A28A23  4C 8B C6                        mov r8, rsi
00A28A26  48 8B C8                        mov rcx, rax
00A28A29  E8 12 DE C9 FF                  call 0x1406c6840
00A28A2E  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00A28A32  45 33 C9                        xor r9d, r9d
00A28A35  4A 8B 04 F9                     mov rax, qword ptr [rcx + r15*8]
00A28A39  66 44 39 08                     cmp word ptr [rax], r9w
00A28A3D  74 60                           je 0x140a28a9f
00A28A3F  44 8B 65 B3                     mov r12d, dword ptr [rbp - 0x4d]
00A28A43  45 8D 51 01                     lea r10d, [r9 + 1]
00A28A47  44 8B 75 AF                     mov r14d, dword ptr [rbp - 0x51]
00A28A4B  41 8A D1                        mov dl, r9b
00A28A4E  45 8A C1                        mov r8b, r9b
00A28A51  0F B7 08                        movzx ecx, word ptr [rax]
00A28A54  66 83 F9 21                     cmp cx, 0x21
00A28A58  74 57                           je 0x140a28ab1
00A28A5A  66 83 F9 40                     cmp cx, 0x40
00A28A5E  0F 84 8A 02 00 00               je 0x140a28cee
00A28A64  45 84 C0                        test r8b, r8b
00A28A67  45 0F B6 F6                     movzx r14d, r14b
00A28A6B  45 0F 45 F2                     cmovne r14d, r10d
00A28A6F  84 D2                           test dl, dl
00A28A71  75 34                           jne 0x140a28aa7
00A28A73  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A28A77  48 FF C1                        inc rcx
00A28A7A  66 44 39 0C 48                  cmp word ptr [rax + rcx*2], r9w
00A28A7F  75 F6                           jne 0x140a28a77
00A28A81  48 8D 04 48                     lea rax, [rax + rcx*2]
00A28A85  48 83 C0 02                     add rax, 2
00A28A89  66 44 39 08                     cmp word ptr [rax], r9w
00A28A8D  75 BC                           jne 0x140a28a4b
00A28A8F  44 89 75 AF                     mov dword ptr [rbp - 0x51], r14d
00A28A93  4C 8B 75 67                     mov r14, qword ptr [rbp + 0x67]
00A28A97  44 89 65 B3                     mov dword ptr [rbp - 0x4d], r12d
00A28A9B  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
00A28A9F  41 FF C5                        inc r13d
00A28AA2  E9 A2 FE FF FF                  jmp 0x140a28949
00A28AA7  41 83 FC FF                     cmp r12d, -1
00A28AAB  45 0F 44 E5                     cmove r12d, r13d
00A28AAF  EB C2                           jmp 0x140a28a73
00A28AB1  41 8A D2                        mov dl, r10b
00A28AB4  48 83 C0 02                     add rax, 2
00A28AB8  EB 97                           jmp 0x140a28a51
00A28ABA  49 8B F3                        mov rsi, r11
00A28ABD  E9 DE FE FF FF                  jmp 0x140a289a0
00A28AC2  45 8D 55 FF                     lea r10d, [r13 - 1]
00A28AC6  48 8B D8                        mov rbx, rax
00A28AC9  41 8B F3                        mov esi, r11d
00A28ACC  44 89 55 9F                     mov dword ptr [rbp - 0x61], r10d
00A28AD0  44 89 5D B7                     mov dword ptr [rbp - 0x49], r11d
00A28AD4  44 39 5D 9B                     cmp dword ptr [rbp - 0x65], r11d
00A28AD8  0F 86 9D 01 00 00               jbe 0x140a28c7b
00A28ADE  8B 7D 9B                        mov edi, dword ptr [rbp - 0x65]
00A28AE1  45 8B E2                        mov r12d, r10d
00A28AE4  8B C7                           mov eax, edi
00A28AE6  4C 8B F3                        mov r14, rbx
00A28AE9  45 8A EB                        mov r13b, r11b
00A28AEC  45 8A CB                        mov r9b, r11b
00A28AEF  45 8A FB                        mov r15b, r11b
00A28AF2  8B 4D 97                        mov ecx, dword ptr [rbp - 0x69]
00A28AF5  33 D2                           xor edx, edx
00A28AF7  89 45 C7                        mov dword ptr [rbp - 0x39], eax
00A28AFA  45 8B DC                        mov r11d, r12d
00A28AFD  89 4D 97                        mov dword ptr [rbp - 0x69], ecx
00A28B00  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00A28B04  44 88 4D 67                     mov byte ptr [rbp + 0x67], r9b
00A28B08  46 8B 04 99                     mov r8d, dword ptr [rcx + r11*4]
00A28B0C  41 F7 F0                        div r8d
00A28B0F  33 D2                           xor edx, edx
00A28B11  8B C8                           mov ecx, eax
00A28B13  8B C6                           mov eax, esi
00A28B15  F7 F1                           div ecx
00A28B17  33 D2                           xor edx, edx
00A28B19  41 F7 F0                        div r8d
00A28B1C  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00A28B20  4A 8B 34 D8                     mov rsi, qword ptr [rax + r11*8]
00A28B24  45 33 DB                        xor r11d, r11d
00A28B27  85 D2                           test edx, edx
00A28B29  0F 85 AE 00 00 00               jne 0x140a28bdd
00A28B2F  41 8A D3                        mov dl, r11b
00A28B32  45 8A C3                        mov r8b, r11b
00A28B35  41 BB 01 00 00 00               mov r11d, 1
00A28B3B  0F B7 06                        movzx eax, word ptr [rsi]
00A28B3E  66 83 F8 21                     cmp ax, 0x21
00A28B42  0F 84 FA 00 00 00               je 0x140a28c42
00A28B48  66 83 F8 40                     cmp ax, 0x40
00A28B4C  0F 84 4D 01 00 00               je 0x140a28c9f
00A28B52  41 BB 00 00 00 00               mov r11d, 0
00A28B58  45 3B E2                        cmp r12d, r10d
00A28B5B  0F 84 A6 00 00 00               je 0x140a28c07
00A28B61  84 D2                           test dl, dl
00A28B63  0F 85 B6 00 00 00               jne 0x140a28c1f
00A28B69  44 88 5D 67                     mov byte ptr [rbp + 0x67], r11b
00A28B6D  45 84 C0                        test r8b, r8b
00A28B70  0F 85 2E 01 00 00               jne 0x140a28ca4
00A28B76  49 83 C8 FF                     or r8, 0xffffffffffffffff
00A28B7A  49 FF C0                        inc r8
00A28B7D  66 46 39 1C 46                  cmp word ptr [rsi + r8*2], r11w
00A28B82  75 F6                           jne 0x140a28b7a
00A28B84  4D 03 C0                        add r8, r8
00A28B87  48 8B D6                        mov rdx, rsi
00A28B8A  49 8B CE                        mov rcx, r14
00A28B8D  E8 AE DC C9 FF                  call 0x1406c6840
00A28B92  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A28B96  45 33 DB                        xor r11d, r11d
00A28B99  48 FF C1                        inc rcx
00A28B9C  66 44 39 1C 4E                  cmp word ptr [rsi + rcx*2], r11w
00A28BA1  75 F6                           jne 0x140a28b99
00A28BA3  4D 8D 34 4E                     lea r14, [r14 + rcx*2]
00A28BA7  45 85 E4                        test r12d, r12d
00A28BAA  0F 84 9E 00 00 00               je 0x140a28c4e
00A28BB0  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
00A28BB4  33 D2                           xor edx, edx
00A28BB6  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
00A28BB9  44 8A 4D 67                     mov r9b, byte ptr [rbp + 0x67]
00A28BBD  8B 75 B7                        mov esi, dword ptr [rbp - 0x49]
00A28BC0  44 8B 55 9F                     mov r10d, dword ptr [rbp - 0x61]
00A28BC4  41 8B CC                        mov ecx, r12d
00A28BC7  66 41 C7 06 23 00               mov word ptr [r14], 0x23
00A28BCD  49 83 C6 02                     add r14, 2
00A28BD1  41 F7 34 88                     div dword ptr [r8 + rcx*4]
00A28BD5  41 FF CC                        dec r12d
00A28BD8  E9 15 FF FF FF                  jmp 0x140a28af2
00A28BDD  8B CA                           mov ecx, edx
00A28BDF  BF 01 00 00 00                  mov edi, 1
00A28BE4  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A28BE8  48 FF C0                        inc rax
00A28BEB  66 44 39 1C 46                  cmp word ptr [rsi + rax*2], r11w
00A28BF0  75 F6                           jne 0x140a28be8
00A28BF2  48 8D 34 46                     lea rsi, [rsi + rax*2]
00A28BF6  48 83 C6 02                     add rsi, 2
00A28BFA  48 2B CF                        sub rcx, rdi
00A28BFD  75 E5                           jne 0x140a28be4
00A28BFF  8B 7D 9B                        mov edi, dword ptr [rbp - 0x65]
00A28C02  E9 28 FF FF FF                  jmp 0x140a28b2f
00A28C07  88 55 67                        mov byte ptr [rbp + 0x67], dl
00A28C0A  44 8A EA                        mov r13b, dl
00A28C0D  44 8A CA                        mov r9b, dl
00A28C10  44 8A FA                        mov r15b, dl
00A28C13  84 D2                           test dl, dl
00A28C15  0F 84 E5 00 00 00               je 0x140a28d00
00A28C1B  44 89 65 97                     mov dword ptr [rbp - 0x69], r12d
00A28C1F  44 38 5D AF                     cmp byte ptr [rbp - 0x51], r11b
00A28C23  0F 84 E0 00 00 00               je 0x140a28d09
00A28C29  41 8A C1                        mov al, r9b
00A28C2C  44 89 65 97                     mov dword ptr [rbp - 0x69], r12d
00A28C30  F6 D8                           neg al
00A28C32  41 BD 01 00 00 00               mov r13d, 1
00A28C38  1A C9                           sbb cl, cl
00A28C3A  44 22 F9                        and r15b, cl
00A28C3D  E9 2B FF FF FF                  jmp 0x140a28b6d
00A28C42  41 8A D3                        mov dl, r11b
00A28C45  48 83 C6 02                     add rsi, 2
00A28C49  E9 ED FE FF FF                  jmp 0x140a28b3b
00A28C4E  45 84 ED                        test r13b, r13b
00A28C51  74 73                           je 0x140a28cc6
00A28C53  45 84 FF                        test r15b, r15b
00A28C56  74 08                           je 0x140a28c60
00A28C58  8B 45 B3                        mov eax, dword ptr [rbp - 0x4d]
00A28C5B  39 45 97                        cmp dword ptr [rbp - 0x69], eax
00A28C5E  76 66                           jbe 0x140a28cc6
00A28C60  44 8B 55 9F                     mov r10d, dword ptr [rbp - 0x61]
00A28C64  8B 75 B7                        mov esi, dword ptr [rbp - 0x49]
00A28C67  FF C6                           inc esi
00A28C69  89 75 B7                        mov dword ptr [rbp - 0x49], esi
00A28C6C  3B F7                           cmp esi, edi
00A28C6E  0F 82 6D FE FF FF               jb 0x140a28ae1
00A28C74  8B 7D DF                        mov edi, dword ptr [rbp - 0x21]
00A28C77  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
00A28C7B  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00A28C7F  48 8B 75 D7                     mov rsi, qword ptr [rbp - 0x29]
00A28C83  66 44 89 1B                     mov word ptr [rbx], r11w
00A28C87  48 2B DE                        sub rbx, rsi
00A28C8A  48 83 C3 02                     add rbx, 2
00A28C8E  48 89 30                        mov qword ptr [rax], rsi
00A28C91  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00A28C95  48 D1 FB                        sar rbx, 1
00A28C98  89 18                           mov dword ptr [rax], ebx
00A28C9A  E9 01 FD FF FF                  jmp 0x140a289a0
00A28C9F  45 8A C3                        mov r8b, r11b
00A28CA2  EB A1                           jmp 0x140a28c45
00A28CA4  41 83 CB FF                     or r11d, 0xffffffff
00A28CA8  88 55 67                        mov byte ptr [rbp + 0x67], dl
00A28CAB  84 D2                           test dl, dl
00A28CAD  4C 8B F3                        mov r14, rbx
00A28CB0  44 8A EA                        mov r13b, dl
00A28CB3  44 8A FA                        mov r15b, dl
00A28CB6  45 0F 45 DC                     cmovne r11d, r12d
00A28CBA  44 89 5D 97                     mov dword ptr [rbp - 0x69], r11d
00A28CBE  45 33 DB                        xor r11d, r11d
00A28CC1  E9 B0 FE FF FF                  jmp 0x140a28b76
00A28CC6  66 45 89 1E                     mov word ptr [r14], r11w
00A28CCA  49 8D 5E 02                     lea rbx, [r14 + 2]
00A28CCE  EB 90                           jmp 0x140a28c60
00A28CD0  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A28CD5  E9 9F FB FF FF                  jmp 0x140a28879
00A28CDA  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A28CDF  E9 C0 FC FF FF                  jmp 0x140a289a4
00A28CE4  BF BB 00 00 C0                  mov edi, 0xc00000bb
00A28CE9  E9 47 FB FF FF                  jmp 0x140a28835
00A28CEE  45 8A C2                        mov r8b, r10b
00A28CF1  E9 BE FD FF FF                  jmp 0x140a28ab4
00A28CF6  BF 01 00 00 C0                  mov edi, 0xc0000001
00A28CFB  E9 62 FC FF FF                  jmp 0x140a28962
00A28D00  83 4D 97 FF                     or dword ptr [rbp - 0x69], 0xffffffff
00A28D04  E9 60 FE FF FF                  jmp 0x140a28b69
00A28D09  45 84 FF                        test r15b, r15b
00A28D0C  0F 84 52 FF FF FF               je 0x140a28c64
00A28D12  E9 12 FF FF FF                  jmp 0x140a28c29
00A28D17  48 85 F6                        test rsi, rsi
00A28D1A  0F 84 59 FB FF FF               je 0x140a28879
00A28D20  33 D2                           xor edx, edx
00A28D22  48 8B CE                        mov rcx, rsi
00A28D25  E8 46 9B 15 00                  call 0x140b82870
00A28D2A  E9 4A FB FF FF                  jmp 0x140a28879
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpGetDeviceLocationStrings(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (184);
    v_rdi = 0;
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = 0;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    *(unsigned __int8 *)(v_rsp - 95 - 81) = 0;
    *(unsigned int *)(v_rsp - 95 - 77) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_rsp - 95 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_xmm0;
    if (a1 == 0) goto loc_00A28851;
    if (a2 == 0) goto loc_00A28851;
    if (a3 == 0) goto loc_00A28851;
    *(unsigned __int64 *)(a2) = 0;
    *(unsigned int *)(a3) = 0;
    if (a1 == (*(unsigned __int64 *)(v_rip + 5651712))) goto loc_00A28890;
loc_00A28750:
    v_r15 = (unsigned int)((0) + ((unsigned int)(v_rdi + 1)));
    if ((*(unsigned __int64 *)(a1 + 16)) != (*(unsigned __int64 *)(v_rip + 5651712))) goto loc_00A28750;
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = (unsigned int)((unsigned int)(v_r15));
    result = ExAllocatePool2(256, v_r15 * 8, (unsigned int)((unsigned int)((unsigned int)(0x75737050ULL))), a4);
    *(unsigned __int64 *)(v_rsp - 95 - 65) = result;
    if (result == 0) goto loc_00A28CD0;
    result = ExAllocatePool2(256, v_r15 * 4, (unsigned int)((unsigned int)((unsigned int)(0x75737050ULL))), a4);
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = result;
    if (result == 0) goto loc_00A28CDA;
    *(unsigned int *)(v_rsp - 95 - 101) = (unsigned int)(v_r11 + 1);
loc_00A287C9:
    if (a1 == (*(unsigned __int64 *)(v_rip + 5651560))) goto loc_00A289E5;
    v_stack_mD0 = v_rsp - 95 - 17;
    v_stack_mD8 = 0;
    result = PnpQueryInterface(*(unsigned __int64 *)(a1 + 32), v_rip - 10545281, (unsigned int)((unsigned int)(v_r11 + 1)), 40);
    v_r11 = 0;
    if (sign_flag) goto loc_00A28ABA;
    if (*(unsigned __int64 *)(v_rsp - 95 + 15) == 0) goto loc_00A28CF6;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 95 - 9), v_rsp - 95 - 89, (unsigned int)((unsigned int)(v_r11 + 1)), 40);
    v_r11 = 0;
    if (!sign_flag) goto loc_00A28897;
loc_00A28835:
    if (*(unsigned __int64 *)(v_rsp - 95 - 89) == 0) goto loc_00A28962;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 - 89), a2, (unsigned int)((unsigned int)(v_r11 + 1)), 40);
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = 0;
    goto loc_00A28962;
loc_00A28851:
    goto loc_00A2887B;
loc_00A28858:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)((unsigned int)(v_r11 + 1)), 40);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(v_r11 + 1)), 40);
    }
    if (sign_flag) goto loc_00A28D17;
loc_00A28879:
loc_00A2887B:
    v_rsp = (v_rsp) + (184);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A28890:
    goto loc_00A2887B;
loc_00A28897:
    if (a1 == 0) goto loc_00A28CE4;
    *(unsigned int *)(result + 0 * 4) = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 89))) == 0) goto loc_00A28910;
    v_r10 = (v_r10) | (-1);
loc_00A288C4:
    a3 = (unsigned int)((0) + (1));
    *(unsigned int *)(result + 0 * 4) = (unsigned int)(a3);
loc_00A288CE:
    result = (v_r10) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 89) + result * 2)) != 0) goto loc_00A288CE;
    result = (unsigned int)((result) + 1);
    a4 = (unsigned int)((0) + ((unsigned int)(result)));
loc_00A288E0:
    result = (v_r10) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 89) + result * 2)) != 0) goto loc_00A288E0;
    if (((unsigned int)(result)) <= 0) { result = 0; }
loc_00A288F4:
    result = (v_r10) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 89) + result * 2)) != 0) goto loc_00A288F4;
    a1 = (*(unsigned __int64 *)(v_rsp - 95 - 89) + result * 2) + (2);
    if ((*(unsigned __int16 *)(a1)) != 0) goto loc_00A288C4;
loc_00A28910:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r11 + 1))) * ((unsigned int)(a3)));
    v_rbx = (unsigned int)((0) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    *(unsigned int *)(v_rsp - 95 - 101) = (unsigned int)(v_rsi);
    v_rsi = (a4 + 1) + (a4 + 1);
    result = ExAllocatePool2(256, v_rsi, (unsigned int)(0x75737050ULL), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + 0 * 8) = result;
    if (result != 0) goto loc_00A28A1F;
loc_00A28949:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 - 89), a2, (unsigned int)(0x75737050ULL), a4);
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = 0;
loc_00A28962:
    result = *(unsigned __int64 *)(v_rsp - 95 + 7);
    if (*(unsigned __int64 *)(v_rsp - 95 + 7) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 9);
        result = guard_dispatch_icall(a1, a2, (unsigned int)(0x75737050ULL), a4);
        v_r11 = 0;
    }
    if (sign_flag) goto loc_00A2899C;
    if (((unsigned int)((unsigned int)(0xC000009AULL))) == 288) goto loc_00A289DE;
    if (0 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 53))))) goto loc_00A289DE;
    v_rbx = (unsigned int)((v_rbx) + (1));
    *(unsigned __int64 *)(v_rsp - 95 + 103) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 16);
    goto loc_00A287C9;
loc_00A2899C:
loc_00A289A0:
loc_00A289A4:
    if ((*(unsigned int *)(v_rsp - 95 - 53)) <= 0) goto loc_00A28858;
loc_00A289BA:
    result = 1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65)) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65)), a2, (unsigned int)(0x75737050ULL), a4);
        v_r11 = 0;
        result = v_r11 + 1;
    }
    v_rbx = (*(unsigned __int64 *)(v_rsp - 95 - 65)) + (8);
    v_r14 = (*(unsigned __int64 *)(v_rsp - 95 - 25)) - (result);
    if (condition_is_not_equal) goto loc_00A289BA;
    goto loc_00A28858;
loc_00A289DE:
    v_rbx = (unsigned int)((v_rbx) + (1));
loc_00A289E5:
    v_rbx = (unsigned int)((v_rbx) * ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 41))));
    *(unsigned int *)(v_rsp - 95 - 33) = 0;
    a2 = (1 + v_rbx * 1) + (1 + v_rbx * 1);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x75737050ULL), a4);
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = result;
    if (result != 0) goto loc_00A28AC2;
    goto loc_00A289A0;
loc_00A28A1F:
    result = memcpy(result, *(unsigned __int64 *)(v_rsp - 95 - 89), result, a4);
    a4 = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)) * 8))) == 0) goto loc_00A28A9F;
loc_00A28A4B:
loc_00A28A51:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)) * 8)))) == 33) goto loc_00A28AB1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)) * 8)))) == 64) goto loc_00A28CEE;
    v_r14 = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81)));
    if (0 != 0) { v_r14 = (unsigned int)(a4 + 1); }
    if (0 != 0) goto loc_00A28AA7;
loc_00A28A73:
    a1 = (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)) * 8))) | (-1);
loc_00A28A77:
    a1 = (a1) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)) * 8) + a1 * 2)) != 0) goto loc_00A28A77;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)) * 8) + a1 * 2) + (2);
    if ((*(unsigned __int16 *)(result)) != 0) goto loc_00A28A4B;
    *(unsigned int *)(v_rsp - 95 - 81) = (unsigned int)(v_r14);
    *(unsigned int *)(v_rsp - 95 - 77) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77)));
loc_00A28A9F:
    v_r13 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 95 - 65)) + 1);
    goto loc_00A28949;
loc_00A28AA7:
    v_r12 = *(unsigned __int64 *)(v_rsp - 95 - 49);
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 49))) == -1) { v_r12 = (unsigned int)(v_r13); }
    goto loc_00A28A73;
loc_00A28AB1:
loc_00A28AB4:
    result = (result) + (2);
    goto loc_00A28A51;
loc_00A28ABA:
    goto loc_00A289A0;
loc_00A28AC2:
    *(unsigned int *)(v_rsp - 95 - 97) = (unsigned int)(v_r13 - 1);
    *(unsigned int *)(v_rsp - 95 - 73) = 0;
    if ((*(unsigned int *)(v_rsp - 95 - 101)) <= 0) goto loc_00A28C7B;
loc_00A28AE1:
loc_00A28AF2:
    a2 = 0;
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)))));
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 105)));
    *(unsigned __int8 *)(v_rsp - 95 + 103) = 0;
    a2 = 0;
    a2 = 0;
    v_r11 = 0;
    if (0 != 0) goto loc_00A28BDD;
loc_00A28B2F:
loc_00A28B3B:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13 - 1)))) * 8)))) == 33) goto loc_00A28C42;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13 - 1)))) * 8)))) == 64) goto loc_00A28C9F;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r13 - 1)))) == ((unsigned int)(v_r13 - 1))) goto loc_00A28C07;
    if (0 != 0) goto loc_00A28C1F;
loc_00A28B69:
    *(unsigned __int8 *)(v_rsp - 95 + 103) = 0;
loc_00A28B6D:
    if (0 != 0) goto loc_00A28CA4;
loc_00A28B76:
    a3 = (0) | (-1);
loc_00A28B7A:
    a3 = (a3) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13 - 1)))) * 8) + a3 * 2)) != 0) goto loc_00A28B7A;
    a3 = (a3) + (a3);
    result = memcpy(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13 - 1)))) * 8), a3, 0);
    a1 = (result) | (-1);
    v_r11 = 0;
loc_00A28B99:
    a1 = (a1) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 65) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13 - 1)))) * 8) + a1 * 2)) != 0) goto loc_00A28B99;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r13 - 1))) == 0) goto loc_00A28C4E;
    a2 = 0;
    *(unsigned __int16 *)(result + a1 * 2) = 35;
    v_r14 = (result + a1 * 2) + (2);
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_r13 - 1))) - 1);
    goto loc_00A28AF2;
loc_00A28BDD:
loc_00A28BE4:
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57))) | (-1);
loc_00A28BE8:
    result = (result) + 1;
    if ((*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)) + result * 2)) != 0) goto loc_00A28BE8;
    v_rsi = ((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)) + result * 2) + (2);
    a1 = (0) - (1);
    if (condition_is_not_equal) goto loc_00A28BE4;
    goto loc_00A28B2F;
loc_00A28C07:
    *(unsigned __int8 *)(v_rsp - 95 + 103) = 0;
    if (0 == 0) goto loc_00A28D00;
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)(v_r12);
loc_00A28C1F:
    if ((*(unsigned __int8 *)(v_rsp - 95 - 81)) == 0) goto loc_00A28D09;
loc_00A28C29:
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)(v_r12);
    result = (unsigned __int8)(-(0));
    v_r15 = (unsigned __int8)((0) & ((unsigned __int8)(a1)));
    goto loc_00A28B6D;
loc_00A28C42:
loc_00A28C45:
    v_rsi = (v_rsi) + (2);
    goto loc_00A28B3B;
loc_00A28C4E:
    if (1 == 0) goto loc_00A28CC6;
    if ((unsigned __int8)(v_r15) == 0) goto loc_00A28C60;
    if ((*(unsigned int *)(v_rsp - 95 - 105)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))))) goto loc_00A28CC6;
loc_00A28C60:
loc_00A28C64:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))) + 1);
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101))))) goto loc_00A28AE1;
loc_00A28C7B:
    *(unsigned __int16 *)(result) = 0;
    v_rbx = (result) - (*(unsigned __int64 *)(v_rsp - 95 - 41));
    v_rbx = (v_rbx) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111)) = *(unsigned __int64 *)(v_rsp - 95 - 41);
    v_rbx = (v_rbx) >> (1);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119)) = (unsigned int)(v_rbx);
    goto loc_00A289A0;
loc_00A28C9F:
    goto loc_00A28C45;
loc_00A28CA4:
    v_r11 = (unsigned int)((v_r11) | (0xFFFFFFFFULL));
    *(unsigned __int8 *)(v_rsp - 95 + 103) = 0;
    if (0 != 0) { v_r11 = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 49)); }
    *(unsigned int *)(v_rsp - 95 - 105) = (unsigned int)(v_r11);
    v_r11 = 0;
    goto loc_00A28B76;
loc_00A28CC6:
    *(unsigned __int16 *)(v_rbx) = 0;
    goto loc_00A28C60;
loc_00A28CD0:
    goto loc_00A28879;
loc_00A28CDA:
    goto loc_00A289A4;
loc_00A28CE4:
    goto loc_00A28835;
loc_00A28CEE:
    goto loc_00A28AB4;
loc_00A28CF6:
    goto loc_00A28962;
loc_00A28D00:
    goto loc_00A28B69;
loc_00A28D09:
    if (0 == 0) goto loc_00A28C64;
    goto loc_00A28C29;
loc_00A28D17:
    if (*(unsigned __int64 *)(v_rsp - 95 - 41) == 0) goto loc_00A28879;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 - 41), a2, (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97))), 0);
    goto loc_00A28879;
}
```

## 5. (Beta) C Style

```c
int64_t PnpGetDeviceLocationStrings(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;

    *(void **)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (184);
    local_rdi = 0;
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = 0;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    *(uint8_t *)(local_rsp - 0x5F - 0x51) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x4D) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)(Arg1);
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = v_xmm0;
    if (Arg1 == 0) goto loc_00A28851;
    if (Arg2 == 0) goto loc_00A28851;
    if (Arg3 == NULL) goto loc_00A28851;
    *(uint64_t *)(Arg2) = 0;
    *(uint32_t *)(arg3) = 0;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x563D00))) goto loc_00A28890;
loc_00A28750:
    local_r15 = (uint32_t)((0) + ((uint32_t)(local_rdi + 1)));
    if ((*(uint64_t *)(Arg1 + 0x10)) != (*(uint64_t *)(v_rip + 0x563D00))) goto loc_00A28750;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(local_r15);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = (uint32_t)((uint32_t)(local_r15));
    result = ExAllocatePool2(256, local_r15 * 8, (uint32_t)((uint32_t)((uint32_t)(0x75737050ULL))), a4);
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = result;
    if (result == 0) goto loc_00A28CD0;
    result = ExAllocatePool2(256, local_r15 * 4, (uint32_t)((uint32_t)((uint32_t)(0x75737050ULL))), a4);
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = result;
    if (result == 0) goto loc_00A28CDA;
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = (uint32_t)(local_r11 + 1);
loc_00A287C9:
    if (Arg1 == (*(uint64_t *)(v_rip + 0x563C68))) goto loc_00A289E5;
    v_stack_mD0 = local_rsp - 95 - 17;
    v_stack_mD8 = 0;
    result = PnpQueryInterface(*(uint64_t *)(Arg1 + 0x20), v_rip - 10545281, (uint32_t)((uint32_t)(local_r11 + 1)), 40);
    local_r11 = 0;
    if (sign_flag) goto loc_00A28ABA;
    if (*(uint64_t *)(local_rsp - 0x5F + 0xF) == 0) goto loc_00A28CF6;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = 0;
    result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x5F - 0x9), local_rsp - 95 - 89, (uint32_t)((uint32_t)(local_r11 + 1)), 40);
    local_r11 = 0;
    if (!sign_flag) goto loc_00A28897;
loc_00A28835:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x59) == 0) goto loc_00A28962;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F - 0x59), Arg2, (uint32_t)((uint32_t)(local_r11 + 1)), 40);
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = 0;
    goto loc_00A28962;
loc_00A28851:
    goto loc_00A2887B;
loc_00A28858:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)((uint32_t)(local_r11 + 1)), 40);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(local_r11 + 1)), 40);
    }
    if (sign_flag) goto loc_00A28D17;
loc_00A28879:
loc_00A2887B:
    local_rsp = (local_rsp) + (184);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A28890:
    goto loc_00A2887B;
loc_00A28897:
    if (Arg1 == 0) goto loc_00A28CE4;
    *(uint32_t *)(result + 0x0 * 4) = 0;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x59))) == 0) goto loc_00A28910;
    local_r10 = (local_r10) | (-1);
loc_00A288C4:
    Arg3 = (uint32_t)((0) + (1));
    *(uint32_t *)(result + 0x0 * 4) = (uint32_t)(Arg3);
loc_00A288CE:
    result = (local_r10) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x59) + result * 2)) != 0) goto loc_00A288CE;
    result = (uint32_t)((result) + 1);
    a4 = (uint32_t)((0) + ((uint32_t)(result)));
loc_00A288E0:
    result = (local_r10) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x59) + result * 2)) != 0) goto loc_00A288E0;
    if (((uint32_t)(result)) <= 0) { result = 0; }
loc_00A288F4:
    result = (local_r10) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x59) + result * 2)) != 0) goto loc_00A288F4;
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F - 0x59) + result * 2) + (2);
    if ((*(uint16_t *)(Arg1)) != 0) goto loc_00A288C4;
loc_00A28910:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r11 + 1))) * ((uint32_t)(Arg3)));
    local_rbx = (uint32_t)((0) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = (uint32_t)(local_rsi);
    local_rsi = (a4 + 1) + (a4 + 1);
    result = ExAllocatePool2(256, local_rsi, (uint32_t)(0x75737050ULL), a4);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + 0x0 * 8) = result;
    if (result != 0) goto loc_00A28A1F;
loc_00A28949:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F - 0x59), Arg2, (uint32_t)(0x75737050ULL), a4);
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = 0;
loc_00A28962:
    result = *(uint64_t *)(local_rsp - 0x5F + 0x7);
    if (*(uint64_t *)(local_rsp - 0x5F + 0x7) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x9);
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)(0x75737050ULL), a4);
        local_r11 = 0;
    }
    if (sign_flag) goto loc_00A2899C;
    if (((uint32_t)((uint32_t)(0xC000009AULL))) == 288) goto loc_00A289DE;
    if (0 == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35))))) goto loc_00A289DE;
    local_rbx = (uint32_t)((local_rbx) + (1));
    *(uint64_t *)(local_rsp - 0x5F + 0x67) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x10);
    goto loc_00A287C9;
loc_00A2899C:
loc_00A289A0:
loc_00A289A4:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x35)) <= 0) goto loc_00A28858;
loc_00A289BA:
    result = 1;
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41)) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41)), Arg2, (uint32_t)(0x75737050ULL), a4);
        local_r11 = 0;
        result = local_r11 + 1;
    }
    local_rbx = (*(uint64_t *)(local_rsp - 0x5F - 0x41)) + (8);
    local_r14 = (*(uint64_t *)(local_rsp - 0x5F - 0x19)) - (result);
    if (condition_is_not_equal) goto loc_00A289BA;
    goto loc_00A28858;
loc_00A289DE:
    local_rbx = (uint32_t)((local_rbx) + (1));
loc_00A289E5:
    local_rbx = (uint32_t)((local_rbx) * ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x29))));
    *(uint32_t *)(local_rsp - 0x5F - 0x21) = 0;
    Arg2 = (1 + local_rbx * 1) + (1 + local_rbx * 1);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x75737050ULL), a4);
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = result;
    if (result != 0) goto loc_00A28AC2;
    goto loc_00A289A0;
loc_00A28A1F:
    result = memcpy(result, *(uint64_t *)(local_rsp - 0x5F - 0x59), result, a4);
    a4 = 0;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)) * 8))) == 0) goto loc_00A28A9F;
loc_00A28A4B:
loc_00A28A51:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)) * 8)))) == 33) goto loc_00A28AB1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)) * 8)))) == 64) goto loc_00A28CEE;
    local_r14 = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51)));
    if (0 != 0) { local_r14 = (uint32_t)(a4 + 1); }
    if (0 != 0) goto loc_00A28AA7;
loc_00A28A73:
    Arg1 = (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)) * 8))) | (-1);
loc_00A28A77:
    Arg1 = (Arg1) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)) * 8) + Arg1 * 2)) != 0) goto loc_00A28A77;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)) * 8) + Arg1 * 2) + (2);
    if ((*(uint16_t *)(result)) != 0) goto loc_00A28A4B;
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = (uint32_t)(local_r14);
    *(uint32_t *)(local_rsp - 0x5F - 0x4D) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D)));
loc_00A28A9F:
    local_r13 = (uint32_t)((*(uint64_t *)(local_rsp - 0x5F - 0x41)) + 1);
    goto loc_00A28949;
loc_00A28AA7:
    local_r12 = *(uint64_t *)(local_rsp - 0x5F - 0x31);
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x31))) == -1) { local_r12 = (uint32_t)(local_r13); }
    goto loc_00A28A73;
loc_00A28AB1:
loc_00A28AB4:
    result = (result) + (2);
    goto loc_00A28A51;
loc_00A28ABA:
    goto loc_00A289A0;
loc_00A28AC2:
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = (uint32_t)(local_r13 - 1);
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = 0;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x65)) <= 0) goto loc_00A28C7B;
loc_00A28AE1:
loc_00A28AF2:
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)))));
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x69)));
    *(uint8_t *)(local_rsp - 0x5F + 0x67) = 0;
    Arg2 = 0;
    Arg2 = 0;
    local_r11 = 0;
    if (0 != 0) goto loc_00A28BDD;
loc_00A28B2F:
loc_00A28B3B:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13 - 0x1)))) * 8)))) == 33) goto loc_00A28C42;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13 - 0x1)))) * 8)))) == 64) goto loc_00A28C9F;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r13 - 1)))) == ((uint32_t)(local_r13 - 1))) goto loc_00A28C07;
    if (0 != 0) goto loc_00A28C1F;
loc_00A28B69:
    *(uint8_t *)(local_rsp - 0x5F + 0x67) = 0;
loc_00A28B6D:
    if (0 != 0) goto loc_00A28CA4;
loc_00A28B76:
    Arg3 = (0) | (-1);
loc_00A28B7A:
    Arg3 = (Arg3) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13 - 0x1)))) * 8) + arg3 * 2)) != 0) goto loc_00A28B7A;
    Arg3 = (Arg3) + (Arg3);
    result = memcpy(result, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13 - 0x1)))) * 8), Arg3, 0);
    Arg1 = (result) | (-1);
    local_r11 = 0;
loc_00A28B99:
    Arg1 = (Arg1) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x41) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13 - 0x1)))) * 8) + Arg1 * 2)) != 0) goto loc_00A28B99;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r13 - 1))) == 0) goto loc_00A28C4E;
    Arg2 = 0;
    *(uint16_t *)(result + Arg1 * 2) = 35;
    local_r14 = (result + Arg1 * 2) + (2);
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_r13 - 1))) - 1);
    goto loc_00A28AF2;
loc_00A28BDD:
loc_00A28BE4:
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39))) | (-1);
loc_00A28BE8:
    result = (result) + 1;
    if ((*(uint16_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)) + result * 2)) != 0) goto loc_00A28BE8;
    local_rsi = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)) + result * 2) + (2);
    Arg1 = (0) - (1);
    if (condition_is_not_equal) goto loc_00A28BE4;
    goto loc_00A28B2F;
loc_00A28C07:
    *(uint8_t *)(local_rsp - 0x5F + 0x67) = 0;
    if (0 == 0) goto loc_00A28D00;
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)(local_r12);
loc_00A28C1F:
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x51)) == 0) goto loc_00A28D09;
loc_00A28C29:
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)(local_r12);
    result = (uint8_t)(-(0));
    local_r15 = (uint8_t)((0) & ((uint8_t)(Arg1)));
    goto loc_00A28B6D;
loc_00A28C42:
loc_00A28C45:
    local_rsi = (local_rsi) + (2);
    goto loc_00A28B3B;
loc_00A28C4E:
    if (1 == 0) goto loc_00A28CC6;
    if ((uint8_t)(local_r15) == 0) goto loc_00A28C60;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x69)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))))) goto loc_00A28CC6;
loc_00A28C60:
loc_00A28C64:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))) + 1);
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65))))) goto loc_00A28AE1;
loc_00A28C7B:
    *(uint16_t *)(result) = 0;
    local_rbx = (result) - (*(uint64_t *)(local_rsp - 0x5F - 0x29));
    local_rbx = (local_rbx) + (2);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F)) = *(uint64_t *)(local_rsp - 0x5F - 0x29);
    local_rbx = (local_rbx) >> (1);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77)) = (uint32_t)(local_rbx);
    goto loc_00A289A0;
loc_00A28C9F:
    goto loc_00A28C45;
loc_00A28CA4:
    local_r11 = (uint32_t)((local_r11) | (0xFFFFFFFFULL));
    *(uint8_t *)(local_rsp - 0x5F + 0x67) = 0;
    if (0 != 0) { local_r11 = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x31)); }
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = (uint32_t)(local_r11);
    local_r11 = 0;
    goto loc_00A28B76;
loc_00A28CC6:
    *(uint16_t *)(local_rbx) = 0;
    goto loc_00A28C60;
loc_00A28CD0:
    goto loc_00A28879;
loc_00A28CDA:
    goto loc_00A289A4;
loc_00A28CE4:
    goto loc_00A28835;
loc_00A28CEE:
    goto loc_00A28AB4;
loc_00A28CF6:
    goto loc_00A28962;
loc_00A28D00:
    goto loc_00A28B69;
loc_00A28D09:
    if (0 == 0) goto loc_00A28C64;
    goto loc_00A28C29;
loc_00A28D17:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x29) == 0) goto loc_00A28879;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F - 0x29), Arg2, (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61))), 0);
    goto loc_00A28879;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A286C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
