# PiDrvDbOverlayCopyKeys

- RVA: `0x007413FC`–`0x00741987` (길이 `1,419` bytes)
- VA: `0x00000001407413FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9340`
- 디코드: `401`개 명령, `1,419/1,419` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007414A7` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x007414CF` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x0074151C` → [PnpCtxRegCreateKey](../A6/PnpCtxRegCreateKey_function_00A692E4.md) (function, `0x00A692E4`)
- `0x0074154F` → [PnpCtxRegQueryInfoKey](../99/PnpCtxRegQueryInfoKey_function_009945FC.md) (function, `0x009945FC`)
- `0x00741588` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007415AE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007415DE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0074160E` → [PnpCtxRegEnumKey](../99/PnpCtxRegEnumKey_function_009929C0.md) (function, `0x009929C0`)
- `0x0074163A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0074164D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0074169B` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x00741714` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x0074174B` → [PnpCtxRegQueryInfoKey](../99/PnpCtxRegQueryInfoKey_function_009945FC.md) (function, `0x009945FC`)
- `0x00741763` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007417A2` → [PiDrvDbOverlayCopyKeys](PiDrvDbOverlayCopyKeys_function_007413FC.md) (function, `0x007413FC`)
- `0x0074181A` → [PnpCtxRegEnumValue](../99/PnpCtxRegEnumValue_function_0099364C.md) (function, `0x0099364C`)
- `0x00741847` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0074185A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00741881` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00741894` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007418D2` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x007418F5` → [PnpCtxRegSetValue](../99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x00741913` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00741922` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00741935` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00741943` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00741951` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0074195F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0074196D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiDrvDbOverlayCopyKeys](PiDrvDbOverlayCopyKeys_function_007413FC.md) at `0x007417A2`
- [PiDrvDbOverlayNodeHive](PiDrvDbOverlayNodeHive_function_00741990.md) at `0x00741B89`
- [PiDrvDbOverlayNodeHive](PiDrvDbOverlayNodeHive_function_00741990.md) at `0x00741D24`

### Static image references
- `0x00741415` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x007414CF` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x00741588` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007415AE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007415DE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0074163A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0074164D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0074169B` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x00741763` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00741847` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0074185A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00741881` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00741894` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00741913` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00741922` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00741935` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00741943` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00741951` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0074195F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0074196D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007413FC  40 55                           push rbp
007413FE  53                              push rbx
007413FF  56                              push rsi
00741400  57                              push rdi
00741401  41 54                           push r12
00741403  41 55                           push r13
00741405  41 56                           push r14
00741407  41 57                           push r15
00741409  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
0074140E  48 81 EC B8 00 00 00            sub rsp, 0xb8
00741415  48 8B 05 24 93 6C 00            mov rax, qword ptr [rip + 0x6c9324]
0074141C  48 33 C4                        xor rax, rsp
0074141F  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00741423  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00741427  4D 8B F0                        mov r14, r8
0074142A  45 33 C0                        xor r8d, r8d
0074142D  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00741431  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00741434  4D 8B E1                        mov r12, r9
00741437  89 45 B7                        mov dword ptr [rbp - 0x49], eax
0074143A  41 8B F0                        mov esi, r8d
0074143D  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
00741444  41 8B F8                        mov edi, r8d
00741447  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0074144B  45 8D 48 08                     lea r9d, [r8 + 8]
0074144F  33 C0                           xor eax, eax
00741451  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
00741455  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00741459  45 8B E8                        mov r13d, r8d
0074145C  89 45 EF                        mov dword ptr [rbp - 0x11], eax
0074145F  45 8B F8                        mov r15d, r8d
00741462  4C 89 45 C7                     mov qword ptr [rbp - 0x39], r8
00741466  48 8D 45 A7                     lea rax, [rbp - 0x59]
0074146A  4C 89 45 D7                     mov qword ptr [rbp - 0x29], r8
0074146E  4C 89 45 AF                     mov qword ptr [rbp - 0x51], r8
00741472  44 89 45 BB                     mov dword ptr [rbp - 0x45], r8d
00741476  44 89 45 BF                     mov dword ptr [rbp - 0x41], r8d
0074147A  44 89 45 8F                     mov dword ptr [rbp - 0x71], r8d
0074147E  44 89 45 9B                     mov dword ptr [rbp - 0x65], r8d
00741482  44 89 45 97                     mov dword ptr [rbp - 0x69], r8d
00741486  44 89 45 93                     mov dword ptr [rbp - 0x6d], r8d
0074148A  44 89 45 C3                     mov dword ptr [rbp - 0x3d], r8d
0074148E  44 89 45 9F                     mov dword ptr [rbp - 0x61], r8d
00741492  4C 8B C2                        mov r8, rdx
00741495  48 8B D1                        mov rdx, rcx
00741498  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0074149D  33 C9                           xor ecx, ecx
0074149F  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
007414A7  E8 0C E3 1A 00                  call 0x1408ef7b8
007414AC  8B D8                           mov ebx, eax
007414AE  85 C0                           test eax, eax
007414B0  0F 88 84 04 00 00               js 0x14074193a
007414B6  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
007414BA  48 8D 45 9F                     lea rax, [rbp - 0x61]
007414BE  45 8D 4F 0C                     lea r9d, [r15 + 0xc]
007414C2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007414C7  4C 8D 45 E7                     lea r8, [rbp - 0x19]
007414CB  41 8D 57 05                     lea edx, [r15 + 5]
007414CF  E8 BC BE F6 FF                  call 0x1406ad390
007414D4  33 C9                           xor ecx, ecx
007414D6  41 8D 57 01                     lea edx, [r15 + 1]
007414DA  85 C0                           test eax, eax
007414DC  78 16                           js 0x1407414f4
007414DE  F6 45 EB 02                     test byte ptr [rbp - 0x15], 2
007414E2  74 0A                           je 0x1407414ee
007414E4  BB 2D 00 00 80                  mov ebx, 0x8000002d
007414E9  E9 4C 04 00 00                  jmp 0x14074193a
007414EE  84 55 EB                        test byte ptr [rbp - 0x15], dl
007414F1  0F 45 F2                        cmovne esi, edx
007414F4  48 8D 45 BF                     lea rax, [rbp - 0x41]
007414F8  44 8B CE                        mov r9d, esi
007414FB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00741500  4D 8B C4                        mov r8, r12
00741503  48 8D 45 C7                     lea rax, [rbp - 0x39]
00741507  49 8B D6                        mov rdx, r14
0074150A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0074150F  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00741514  C7 44 24 20 1F 00 06 00         mov dword ptr [rsp + 0x20], 0x6001f
0074151C  E8 C3 7D 32 00                  call 0x140a692e4
00741521  33 F6                           xor esi, esi
00741523  8B D8                           mov ebx, eax
00741525  85 C0                           test eax, eax
00741527  0F 88 0D 04 00 00               js 0x14074193a
0074152D  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00741531  48 8D 45 93                     lea rax, [rbp - 0x6d]
00741535  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0074153A  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
0074153E  48 8D 45 9B                     lea rax, [rbp - 0x65]
00741542  45 33 C0                        xor r8d, r8d
00741545  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0074154A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0074154F  E8 A8 30 25 00                  call 0x1409945fc
00741554  41 BE 50 70 64 62               mov r14d, 0x62647050
0074155A  41 BC 00 01 00 00               mov r12d, 0x100
00741560  85 C0                           test eax, eax
00741562  78 3B                           js 0x14074159f
00741564  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00741567  39 45 8F                        cmp dword ptr [rbp - 0x71], eax
0074156A  0F 47 45 8F                     cmova eax, dword ptr [rbp - 0x71]
0074156E  44 8D 2C 45 02 00 00 00         lea r13d, [rax*2 + 2]
00741576  44 89 6D 97                     mov dword ptr [rbp - 0x69], r13d
0074157A  45 85 ED                        test r13d, r13d
0074157D  74 20                           je 0x14074159f
0074157F  41 8B D5                        mov edx, r13d
00741582  45 8B C6                        mov r8d, r14d
00741585  41 8B CC                        mov ecx, r12d
00741588  E8 63 0B 44 00                  call 0x140b820f0
0074158D  48 8B F8                        mov rdi, rax
00741590  48 85 C0                        test rax, rax
00741593  75 0A                           jne 0x14074159f
00741595  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0074159A  E9 9B 03 00 00                  jmp 0x14074193a
0074159F  8B 45 93                        mov eax, dword ptr [rbp - 0x6d]
007415A2  85 C0                           test eax, eax
007415A4  74 1F                           je 0x1407415c5
007415A6  8B D0                           mov edx, eax
007415A8  45 8B C6                        mov r8d, r14d
007415AB  49 8B CC                        mov rcx, r12
007415AE  E8 3D 0B 44 00                  call 0x140b820f0
007415B3  4C 8B F8                        mov r15, rax
007415B6  48 85 C0                        test rax, rax
007415B9  75 0A                           jne 0x1407415c5
007415BB  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007415C0  E9 44 03 00 00                  jmp 0x140741909
007415C5  48 39 75 CF                     cmp qword ptr [rbp - 0x31], rsi
007415C9  74 21                           je 0x1407415ec
007415CB  8B 45 B7                        mov eax, dword ptr [rbp - 0x49]
007415CE  85 C0                           test eax, eax
007415D0  74 1A                           je 0x1407415ec
007415D2  8B D0                           mov edx, eax
007415D4  45 8B C6                        mov r8d, r14d
007415D7  48 C1 E2 03                     shl rdx, 3
007415DB  49 8B CC                        mov rcx, r12
007415DE  E8 0D 0B 44 00                  call 0x140b820f0
007415E3  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
007415E7  48 85 C0                        test rax, rax
007415EA  74 CF                           je 0x1407415bb
007415EC  44 8B E6                        mov r12d, esi
007415EF  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
007415F3  41 8B C5                        mov eax, r13d
007415F6  D1 E8                           shr eax, 1
007415F8  4C 8B CF                        mov r9, rdi
007415FB  89 45 8F                        mov dword ptr [rbp - 0x71], eax
007415FE  45 8B C4                        mov r8d, r12d
00741601  48 8D 45 8F                     lea rax, [rbp - 0x71]
00741605  44 89 65 9B                     mov dword ptr [rbp - 0x65], r12d
00741609  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0074160E  E8 AD 13 25 00                  call 0x1409929c0
00741613  3D 1A 00 00 80                  cmp eax, 0x8000001a
00741618  0F 84 B8 01 00 00               je 0x1407417d6
0074161E  3D 23 00 00 C0                  cmp eax, 0xc0000023
00741623  75 41                           jne 0x140741666
00741625  8B 45 8F                        mov eax, dword ptr [rbp - 0x71]
00741628  44 8D 2C 00                     lea r13d, [rax + rax]
0074162C  44 89 6D 97                     mov dword ptr [rbp - 0x69], r13d
00741630  48 85 FF                        test rdi, rdi
00741633  74 0A                           je 0x14074163f
00741635  33 D2                           xor edx, edx
00741637  48 8B CF                        mov rcx, rdi
0074163A  E8 31 12 44 00                  call 0x140b82870
0074163F  41 8B D5                        mov edx, r13d
00741642  B9 00 01 00 00                  mov ecx, 0x100
00741647  41 B8 50 70 64 62               mov r8d, 0x62647050
0074164D  E8 9E 0A 44 00                  call 0x140b820f0
00741652  48 8B F8                        mov rdi, rax
00741655  48 85 C0                        test rax, rax
00741658  0F 84 6E 01 00 00               je 0x1407417cc
0074165E  41 FF CC                        dec r12d
00741661  E9 5E 01 00 00                  jmp 0x1407417c4
00741666  85 C0                           test eax, eax
00741668  0F 88 99 02 00 00               js 0x140741907
0074166E  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00741672  44 8B EE                        mov r13d, esi
00741675  48 85 C9                        test rcx, rcx
00741678  74 75                           je 0x1407416ef
0074167A  8B 75 8F                        mov esi, dword ptr [rbp - 0x71]
0074167D  45 33 C0                        xor r8d, r8d
00741680  85 F6                           test esi, esi
00741682  74 69                           je 0x1407416ed
00741684  45 8B F0                        mov r14d, r8d
00741687  44 3B 75 B7                     cmp r14d, dword ptr [rbp - 0x49]
0074168B  73 54                           jae 0x1407416e1
0074168D  45 8B E6                        mov r12d, r14d
00741690  44 8D 46 FF                     lea r8d, [rsi - 1]
00741694  48 8B D7                        mov rdx, rdi
00741697  4A 8B 0C E1                     mov rcx, qword ptr [rcx + r12*8]
0074169B  E8 20 EB DB FF                  call 0x1405001c0
007416A0  45 33 C0                        xor r8d, r8d
007416A3  85 C0                           test eax, eax
007416A5  75 2E                           jne 0x1407416d5
007416A7  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
007416AB  4A 8B 04 E0                     mov rax, qword ptr [rax + r12*8]
007416AF  48 8D 14 70                     lea rdx, [rax + rsi*2]
007416B3  0F B7 42 FE                     movzx eax, word ptr [rdx - 2]
007416B7  66 85 C0                        test ax, ax
007416BA  74 22                           je 0x1407416de
007416BC  66 83 F8 5C                     cmp ax, 0x5c
007416C0  75 13                           jne 0x1407416d5
007416C2  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
007416C6  48 85 C9                        test rcx, rcx
007416C9  74 0A                           je 0x1407416d5
007416CB  41 8B C5                        mov eax, r13d
007416CE  41 FF C5                        inc r13d
007416D1  48 89 14 C1                     mov qword ptr [rcx + rax*8], rdx
007416D5  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
007416D9  41 FF C6                        inc r14d
007416DC  EB A9                           jmp 0x140741687
007416DE  41 8B F0                        mov esi, r8d
007416E1  44 8B 65 9B                     mov r12d, dword ptr [rbp - 0x65]
007416E5  85 F6                           test esi, esi
007416E7  0F 84 D1 00 00 00               je 0x1407417be
007416ED  33 F6                           xor esi, esi
007416EF  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
007416F3  48 85 C0                        test rax, rax
007416F6  74 79                           je 0x140741771
007416F8  48 8D 4D AF                     lea rcx, [rbp - 0x51]
007416FC  45 33 C9                        xor r9d, r9d
007416FF  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00741704  4C 8B C7                        mov r8, rdi
00741707  33 C9                           xor ecx, ecx
00741709  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00741711  48 8B D0                        mov rdx, rax
00741714  E8 9F E0 1A 00                  call 0x1408ef7b8
00741719  3D 34 00 00 C0                  cmp eax, 0xc0000034
0074171E  75 09                           jne 0x140741729
00741720  48 89 75 AF                     mov qword ptr [rbp - 0x51], rsi
00741724  E9 97 00 00 00                  jmp 0x1407417c0
00741729  85 C0                           test eax, eax
0074172B  0F 88 D6 01 00 00               js 0x140741907
00741731  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
00741735  4C 8D 45 BB                     lea r8, [rbp - 0x45]
00741739  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
0074173E  45 33 C9                        xor r9d, r9d
00741741  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00741746  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0074174B  E8 AC 2E 25 00                  call 0x1409945fc
00741750  8B D8                           mov ebx, eax
00741752  85 C0                           test eax, eax
00741754  0F 88 AF 01 00 00               js 0x140741909
0074175A  39 75 BB                        cmp dword ptr [rbp - 0x45], esi
0074175D  75 12                           jne 0x140741771
0074175F  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00741763  E8 48 BB F6 FF                  call 0x1406ad2b0
00741768  48 8B D6                        mov rdx, rsi
0074176B  48 89 55 AF                     mov qword ptr [rbp - 0x51], rdx
0074176F  EB 04                           jmp 0x140741775
00741771  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
00741775  4C 8B 45 C7                     mov r8, qword ptr [rbp - 0x39]
00741779  41 8B C5                        mov eax, r13d
0074177C  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00741781  F7 D8                           neg eax
00741783  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00741788  4C 8B CF                        mov r9, rdi
0074178B  48 1B C9                        sbb rcx, rcx
0074178E  48 8B D7                        mov rdx, rdi
00741791  48 23 4D D7                     and rcx, qword ptr [rbp - 0x29]
00741795  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0074179A  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
0074179E  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
007417A2  E8 55 FC FF FF                  call 0x1407413fc
007417A7  8B D8                           mov ebx, eax
007417A9  3D 2D 00 00 80                  cmp eax, 0x8000002d
007417AE  75 04                           jne 0x1407417b4
007417B0  8B DE                           mov ebx, esi
007417B2  EB 0C                           jmp 0x1407417c0
007417B4  85 C0                           test eax, eax
007417B6  0F 88 4D 01 00 00               js 0x140741909
007417BC  EB 02                           jmp 0x1407417c0
007417BE  33 F6                           xor esi, esi
007417C0  44 8B 6D 97                     mov r13d, dword ptr [rbp - 0x69]
007417C4  41 FF C4                        inc r12d
007417C7  E9 23 FE FF FF                  jmp 0x1407415ef
007417CC  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007417D1  E9 42 01 00 00                  jmp 0x140741918
007417D6  85 DB                           test ebx, ebx
007417D8  0F 88 2B 01 00 00               js 0x140741909
007417DE  44 8B 65 93                     mov r12d, dword ptr [rbp - 0x6d]
007417E2  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
007417E6  48 8D 45 93                     lea rax, [rbp - 0x6d]
007417EA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007417EF  45 8B F5                        mov r14d, r13d
007417F2  48 8D 45 C3                     lea rax, [rbp - 0x3d]
007417F6  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
007417FB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00741800  4C 8B CF                        mov r9, rdi
00741803  48 8D 45 8F                     lea rax, [rbp - 0x71]
00741807  41 D1 EE                        shr r14d, 1
0074180A  44 8B C6                        mov r8d, esi
0074180D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00741812  44 89 75 8F                     mov dword ptr [rbp - 0x71], r14d
00741816  44 89 65 93                     mov dword ptr [rbp - 0x6d], r12d
0074181A  E8 2D 1E 25 00                  call 0x14099364c
0074181F  3D 1A 00 00 80                  cmp eax, 0x8000001a
00741824  0F 84 DF 00 00 00               je 0x140741909
0074182A  3D 23 00 00 C0                  cmp eax, 0xc0000023
0074182F  75 78                           jne 0x1407418a9
00741831  8B 45 8F                        mov eax, dword ptr [rbp - 0x71]
00741834  41 3B C6                        cmp eax, r14d
00741837  76 32                           jbe 0x14074186b
00741839  44 8D 2C 00                     lea r13d, [rax + rax]
0074183D  48 85 FF                        test rdi, rdi
00741840  74 0A                           je 0x14074184c
00741842  33 D2                           xor edx, edx
00741844  48 8B CF                        mov rcx, rdi
00741847  E8 24 10 44 00                  call 0x140b82870
0074184C  41 8B D5                        mov edx, r13d
0074184F  B9 00 01 00 00                  mov ecx, 0x100
00741854  41 B8 50 70 64 62               mov r8d, 0x62647050
0074185A  E8 91 08 44 00                  call 0x140b820f0
0074185F  48 8B F8                        mov rdi, rax
00741862  48 85 C0                        test rax, rax
00741865  0F 84 61 FF FF FF               je 0x1407417cc
0074186B  44 8B 75 93                     mov r14d, dword ptr [rbp - 0x6d]
0074186F  45 3B F4                        cmp r14d, r12d
00741872  76 31                           jbe 0x1407418a5
00741874  45 8B E6                        mov r12d, r14d
00741877  4D 85 FF                        test r15, r15
0074187A  74 0A                           je 0x140741886
0074187C  33 D2                           xor edx, edx
0074187E  49 8B CF                        mov rcx, r15
00741881  E8 EA 0F 44 00                  call 0x140b82870
00741886  49 8B D6                        mov rdx, r14
00741889  B9 00 01 00 00                  mov ecx, 0x100
0074188E  41 B8 50 70 64 62               mov r8d, 0x62647050
00741894  E8 57 08 44 00                  call 0x140b820f0
00741899  4C 8B F8                        mov r15, rax
0074189C  48 85 C0                        test rax, rax
0074189F  0F 84 16 FD FF FF               je 0x1407415bb
007418A5  FF CE                           dec esi
007418A7  EB 57                           jmp 0x140741900
007418A9  45 33 F6                        xor r14d, r14d
007418AC  85 C0                           test eax, eax
007418AE  78 57                           js 0x140741907
007418B0  83 7D BF 02                     cmp dword ptr [rbp - 0x41], 2
007418B4  75 28                           jne 0x1407418de
007418B6  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
007418BA  48 8D 45 9F                     lea rax, [rbp - 0x61]
007418BE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007418C3  45 33 C9                        xor r9d, r9d
007418C6  4C 8B C7                        mov r8, rdi
007418C9  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
007418CE  44 89 75 9F                     mov dword ptr [rbp - 0x61], r14d
007418D2  E8 25 28 25 00                  call 0x1409940fc
007418D7  3D 23 00 00 C0                  cmp eax, 0xc0000023
007418DC  74 22                           je 0x140741900
007418DE  8B 45 93                        mov eax, dword ptr [rbp - 0x6d]
007418E1  4C 8B C7                        mov r8, rdi
007418E4  44 8B 4D C3                     mov r9d, dword ptr [rbp - 0x3d]
007418E8  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
007418EC  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007418F0  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
007418F5  E8 92 02 25 00                  call 0x140991b8c
007418FA  8B D8                           mov ebx, eax
007418FC  85 C0                           test eax, eax
007418FE  78 09                           js 0x140741909
00741900  FF C6                           inc esi
00741902  E9 DB FE FF FF                  jmp 0x1407417e2
00741907  8B D8                           mov ebx, eax
00741909  48 85 FF                        test rdi, rdi
0074190C  74 0A                           je 0x140741918
0074190E  33 D2                           xor edx, edx
00741910  48 8B CF                        mov rcx, rdi
00741913  E8 58 0F 44 00                  call 0x140b82870
00741918  4D 85 FF                        test r15, r15
0074191B  74 0A                           je 0x140741927
0074191D  33 D2                           xor edx, edx
0074191F  49 8B CF                        mov rcx, r15
00741922  E8 49 0F 44 00                  call 0x140b82870
00741927  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
0074192B  48 85 C0                        test rax, rax
0074192E  74 0A                           je 0x14074193a
00741930  33 D2                           xor edx, edx
00741932  48 8B C8                        mov rcx, rax
00741935  E8 36 0F 44 00                  call 0x140b82870
0074193A  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
0074193E  48 85 C9                        test rcx, rcx
00741941  74 05                           je 0x140741948
00741943  E8 68 B9 F6 FF                  call 0x1406ad2b0
00741948  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
0074194C  48 85 C9                        test rcx, rcx
0074194F  74 05                           je 0x140741956
00741951  E8 5A B9 F6 FF                  call 0x1406ad2b0
00741956  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
0074195A  48 85 C9                        test rcx, rcx
0074195D  74 05                           je 0x140741964
0074195F  E8 4C B9 F6 FF                  call 0x1406ad2b0
00741964  8B C3                           mov eax, ebx
00741966  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
0074196A  48 33 CC                        xor rcx, rsp
0074196D  E8 CE AC F6 FF                  call 0x1406ac640
00741972  48 81 C4 B8 00 00 00            add rsp, 0xb8
00741979  41 5F                           pop r15
0074197B  41 5E                           pop r14
0074197D  41 5D                           pop r13
0074197F  41 5C                           pop r12
00741981  5F                              pop rdi
00741982  5E                              pop rsi
00741983  5B                              pop rbx
00741984  5D                              pop rbp
00741985  C3                              ret
00741986  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDrvDbOverlayCopyKeys(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int8 v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;

    v_rsp = (v_rsp) - (184);
    result = (*(unsigned __int64 *)(v_rip + 7115556)) ^ (v_rsp);
    v_stack_m50 = result;
    a3 = 0;
    v_stack_m78 = a6;
    v_stack_m90 = (unsigned int)((unsigned int)(a7));
    v_stack_m68 = a8;
    result = 0;
    v_stack_mA0 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m80 = 0;
    v_stack_m70 = 0;
    v_stack_m98 = 0;
    v_stack_m8C = 0;
    v_stack_m88 = 0;
    v_stack_mB8 = 0;
    v_stack_mAC = 0;
    v_stack_mB0 = 0;
    v_stack_mB4 = 0;
    v_stack_m84 = 0;
    v_stack_mA8 = 0;
    v_stack_mD0 = v_stack_mA0;
    a1 = 0;
    v_stack_mD8 = 0x20019ULL;
    result = PnpCtxRegOpenKey(a1, a1, a2, a3 + 8);
    if (sign_flag) goto loc_0074193A;
    v_stack_mD8 = v_stack_mA8;
    result = ZwQueryKey(v_stack_mA0, 0 + 5, v_stack_m60, 0 + 12);
    a1 = 0;
    if (sign_flag) goto loc_007414F4;
    if (((v_stack_m5C) & (2)) == 0) goto loc_007414EE;
    goto loc_0074193A;
loc_007414EE:
    v_rsi = 0;
    if (((v_stack_m5C) & ((unsigned __int8)(0 + 1))) != 0) { v_rsi = (unsigned int)(0 + 1); }
loc_007414F4:
    v_stack_mC0 = v_stack_m88;
    v_stack_mC8 = v_stack_m80;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0x6001FULL;
    result = PnpCtxRegCreateKey(a1, 0, a4, (unsigned int)((unsigned int)(v_rsi)));
    v_rsi = 0;
    if (sign_flag) goto loc_0074193A;
    v_stack_mC8 = v_stack_mB4;
    a3 = 0;
    v_stack_mD0 = v_stack_mAC;
    v_stack_mD8 = 0;
    result = PnpCtxRegQueryInfoKey(a1, v_stack_mA0, a3, v_stack_mB8);
    if (sign_flag) goto loc_0074159F;
    result = (unsigned int)(v_stack_mAC);
    if (v_stack_mB8 > ((unsigned int)((unsigned int)(v_stack_mAC)))) { result = v_stack_mB8; }
    v_stack_mB0 = (unsigned int)(result * 2 + 2);
    if ((unsigned int)(result * 2 + 2) == 0) goto loc_0074159F;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result * 2 + 2)), (unsigned int)((unsigned int)((unsigned int)(0x62647050ULL))), v_stack_mB8);
    if (result != 0) goto loc_0074159F;
    goto loc_0074193A;
loc_0074159F:
    if ((unsigned int)((unsigned int)(v_stack_mB4)) == 0) goto loc_007415C5;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))), (unsigned int)((unsigned int)((unsigned int)(0x62647050ULL))), v_stack_mB8);
    if (result != 0) goto loc_007415C5;
loc_007415BB:
    goto loc_00741909;
loc_007415C5:
    if (v_stack_m78 == 0) goto loc_007415EC;
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) goto loc_007415EC;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m90)))) << (3);
    result = ExAllocatePool2(256, a2, (unsigned int)((unsigned int)((unsigned int)(0x62647050ULL))), v_stack_mB8);
    v_stack_m70 = result;
    if (result == 0) goto loc_007415BB;
loc_007415EC:
loc_007415EF:
    result = (unsigned int)(((unsigned int)((unsigned int)(result * 2 + 2))) >> (1));
    v_stack_mB8 = (unsigned int)(result);
    v_stack_mAC = 0;
    v_stack_mD8 = v_stack_mB8;
    result = PnpCtxRegEnumKey(256, v_stack_mA0, 0, result);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_007417D6;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00741666;
    v_stack_mB0 = (unsigned int)((unsigned int)(v_stack_mB8) + (unsigned int)(v_stack_mB8) * 1);
    result = (unsigned int)(v_stack_mB8);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, 0, result);
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8) + (unsigned int)(v_stack_mB8) * 1)), (unsigned int)(0x62647050ULL), result);
    if (result == 0) goto loc_007417CC;
    v_r12 = (unsigned int)((0) - 1);
    goto loc_007417C4;
loc_00741666:
    if (sign_flag) goto loc_00741907;
    if (v_stack_m78 == 0) goto loc_007416EF;
    a3 = 0;
    if ((unsigned int)((unsigned int)(v_stack_mB8)) == 0) goto loc_007416ED;
loc_00741687:
    if (0 >= v_stack_m90) goto loc_007416E1;
    result = wcsnicmp(*(unsigned __int64 *)(v_stack_m78 + 0 * 8), result, (unsigned int)(v_stack_mB8) - 1, result);
    a3 = 0;
    if ((unsigned int)(result) != 0) goto loc_007416D5;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m78 + 0 * 8) + (unsigned int)(v_stack_mB8) * 2 - 2)) == 0) goto loc_007416DE;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m78 + 0 * 8) + (unsigned int)(v_stack_mB8) * 2 - 2))) != 92) goto loc_007416D5;
    result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m78 + 0 * 8) + (unsigned int)(v_stack_mB8) * 2 - 2);
    v_r13 = 0;
    if (v_stack_m70 != 0) {
        result = 0;
        v_r13 = (unsigned int)((0) + 1);
        *(unsigned __int64 *)(v_stack_m70 + result * 8) = *(unsigned __int64 *)(v_stack_m78 + 0 * 8) + (unsigned int)(v_stack_mB8) * 2;
    }
    v_r14 = (unsigned int)((0) + 1);
    goto loc_00741687;
loc_007416DE:
loc_007416E1:
    if (0 == 0) goto loc_007417BE;
loc_007416ED:
    v_rsi = 0;
loc_007416EF:
    if (v_stack_m68 == 0) goto loc_00741771;
    a4 = 0;
    v_stack_mD0 = v_stack_m98;
    a1 = 0;
    v_stack_mD8 = 0x20019ULL;
    result = PnpCtxRegOpenKey(a1, v_stack_m68, result, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00741729;
    v_stack_m98 = 0;
    goto loc_007417C0;
loc_00741729:
    if (sign_flag) goto loc_00741907;
    v_stack_mC8 = 0;
    a4 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    result = PnpCtxRegQueryInfoKey(a1, v_stack_m98, v_stack_m8C, a4);
    if (sign_flag) goto loc_00741909;
    if (v_stack_m8C != 0) goto loc_00741771;
    result = ZwClose(v_stack_m98, v_stack_m98, v_stack_m8C, a4);
    v_stack_m98 = 0;
    goto loc_00741775;
loc_00741771:
loc_00741775:
    v_stack_mC0 = v_stack_m98;
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r13))));
    v_stack_mC8 = (unsigned int)(v_r13);
    a1 = (v_stack_m98) & (v_stack_m70);
    v_stack_mD0 = a1;
    v_stack_mD8 = 0;
    result = PiDrvDbOverlayCopyKeys(v_stack_mA0, result, v_stack_m80, result);
    if (((unsigned int)(result)) != 0x8000002DULL) goto loc_007417B4;
    goto loc_007417C0;
loc_007417B4:
    if (sign_flag) goto loc_00741909;
    goto loc_007417C0;
loc_007417BE:
    v_rsi = 0;
loc_007417C0:
loc_007417C4:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_mAC)) + 1);
    goto loc_007415EF;
loc_007417CC:
    goto loc_00741918;
loc_007417D6:
    if (sign_flag) goto loc_00741909;
loc_007417E2:
    v_stack_mC0 = v_stack_mB4;
    v_stack_mC8 = result;
    v_stack_mD0 = v_stack_m84;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mB0)))) >> (1));
    v_stack_mD8 = v_stack_mB8;
    v_stack_mB8 = (unsigned int)(v_r14);
    v_stack_mB4 = (unsigned int)((unsigned int)(v_stack_mB4));
    result = PnpCtxRegEnumValue(v_stack_mA0, v_stack_mA0, 0, result);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_00741909;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007418A9;
    if (((unsigned int)((unsigned int)(v_stack_mB8))) <= ((unsigned int)(v_r14))) goto loc_0074186B;
    result = (unsigned int)(v_stack_mB8);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, 0, result);
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB8) + (unsigned int)(v_stack_mB8) * 1)), (unsigned int)(0x62647050ULL), result);
    if (result == 0) goto loc_007417CC;
loc_0074186B:
    if (((unsigned int)((unsigned int)(v_stack_mB4))) <= ((unsigned int)((unsigned int)(v_stack_mB4)))) goto loc_007418A5;
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x62647050ULL), result);
    }
    result = ExAllocatePool2(256, (unsigned int)(v_stack_mB4), (unsigned int)(0x62647050ULL), result);
    if (result == 0) goto loc_007415BB;
loc_007418A5:
    v_rsi = (unsigned int)((v_rsi) - 1);
    goto loc_00741900;
loc_007418A9:
    v_r14 = 0;
    if (sign_flag) goto loc_00741907;
    if (v_stack_m88 != 2) goto loc_007418DE;
    v_stack_mD0 = v_stack_mA8;
    a4 = 0;
    v_stack_mD8 = 0;
    v_stack_mA8 = 0;
    result = PnpCtxRegQueryValue(256, v_stack_m80, result, a4);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00741900;
loc_007418DE:
    v_stack_mD0 = (unsigned int)((unsigned int)(v_stack_mB4));
    v_stack_mD8 = result;
    result = PnpCtxRegSetValue(256, v_stack_m80, result, (unsigned int)(v_stack_m84));
    if (sign_flag) goto loc_00741909;
loc_00741900:
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_007417E2;
loc_00741907:
loc_00741909:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, result, (unsigned int)(v_stack_m84));
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, result, (unsigned int)(v_stack_m84));
    }
    result = v_stack_m70;
    if (v_stack_m70 != 0) {
        a2 = 0;
        a1 = v_stack_m70;
        result = ExFreePoolWithTag(a1, a2, result, (unsigned int)(v_stack_m84));
    }
    if (v_stack_mA0 != 0) {
        result = ZwClose(v_stack_mA0, a2, result, (unsigned int)(v_stack_m84));
    }
    if (v_stack_m80 != 0) {
        result = ZwClose(v_stack_m80, a2, result, (unsigned int)(v_stack_m84));
    }
    if (v_stack_m98 != 0) {
        result = ZwClose(v_stack_m98, a2, result, (unsigned int)(v_stack_m84));
    }
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, result, (unsigned int)(v_stack_m84));
    v_rsp = (v_rsp) + (184);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDrvDbOverlayCopyKeys(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m47;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint8_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;

    local_rsp = (local_rsp) - (184);
    result = (*(uint64_t *)(v_rip + 0x6C9324)) ^ (local_rsp);
    v_stack_m50 = result;
    Arg3 = 0;
    v_stack_m78 = Arg6;
    v_stack_m90 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m68 = Arg8;
    result = 0;
    v_stack_mA0 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m80 = 0;
    v_stack_m70 = 0;
    v_stack_m98 = 0;
    v_stack_m8C = 0;
    v_stack_m88 = 0;
    v_stack_mB8 = 0;
    v_stack_mAC = 0;
    v_stack_mB0 = 0;
    v_stack_mB4 = 0;
    v_stack_m84 = 0;
    v_stack_mA8 = 0;
    v_stack_mD0 = v_stack_mA0;
    Arg1 = 0;
    v_stack_mD8 = 0x20019ULL;
    result = PnpCtxRegOpenKey(Arg1, Arg1, Arg2, Arg3 + 8);
    if (sign_flag) goto loc_0074193A;
    v_stack_mD8 = v_stack_mA8;
    result = ZwQueryKey(v_stack_mA0, 0 + 5, v_stack_m60, 0 + 12);
    Arg1 = 0;
    if (sign_flag) goto loc_007414F4;
    if (((v_stack_m5C) & (2)) == 0) goto loc_007414EE;
    goto loc_0074193A;
loc_007414EE:
    local_rsi = 0;
    if (((v_stack_m5C) & ((uint8_t)(0 + 1))) != 0) { local_rsi = (uint32_t)(0 + 1); }
loc_007414F4:
    v_stack_mC0 = v_stack_m88;
    v_stack_mC8 = v_stack_m80;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0x6001FULL;
    result = PnpCtxRegCreateKey(Arg1, 0, Arg4, (uint32_t)((uint32_t)(local_rsi)));
    local_rsi = 0;
    if (sign_flag) goto loc_0074193A;
    v_stack_mC8 = v_stack_mB4;
    Arg3 = 0;
    v_stack_mD0 = v_stack_mAC;
    v_stack_mD8 = 0;
    result = PnpCtxRegQueryInfoKey(Arg1, v_stack_mA0, Arg3, v_stack_mB8);
    if (sign_flag) goto loc_0074159F;
    result = (uint32_t)(v_stack_mAC);
    if (v_stack_mB8 > ((uint32_t)((uint32_t)(v_stack_mAC)))) { result = v_stack_mB8; }
    v_stack_mB0 = (uint32_t)(result * 2 + 2);
    if ((uint32_t)(result * 2 + 2) == 0) goto loc_0074159F;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result * 2 + 2)), (uint32_t)((uint32_t)((uint32_t)(0x62647050ULL))), v_stack_mB8);
    if (result != 0) goto loc_0074159F;
    goto loc_0074193A;
loc_0074159F:
    if ((uint32_t)((uint32_t)(v_stack_mB4)) == 0) goto loc_007415C5;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))), (uint32_t)((uint32_t)((uint32_t)(0x62647050ULL))), v_stack_mB8);
    if (result != 0) goto loc_007415C5;
loc_007415BB:
    goto loc_00741909;
loc_007415C5:
    if (v_stack_m78 == 0) goto loc_007415EC;
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) goto loc_007415EC;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m90)))) << (3);
    result = ExAllocatePool2(256, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x62647050ULL))), v_stack_mB8);
    v_stack_m70 = result;
    if (result == 0) goto loc_007415BB;
loc_007415EC:
loc_007415EF:
    result = (uint32_t)(((uint32_t)((uint32_t)(result * 2 + 2))) >> (1));
    v_stack_mB8 = (uint32_t)(result);
    v_stack_mAC = 0;
    v_stack_mD8 = v_stack_mB8;
    result = PnpCtxRegEnumKey(256, v_stack_mA0, 0, result);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_007417D6;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00741666;
    v_stack_mB0 = (uint32_t)((uint32_t)(v_stack_mB8) + (uint32_t)(v_stack_mB8) * 1);
    result = (uint32_t)(v_stack_mB8);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, 0, result);
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8) + (uint32_t)(v_stack_mB8) * 1)), (uint32_t)(0x62647050ULL), result);
    if (result == 0) goto loc_007417CC;
    local_r12 = (uint32_t)((0) - 1);
    goto loc_007417C4;
loc_00741666:
    if (sign_flag) goto loc_00741907;
    if (v_stack_m78 == 0) goto loc_007416EF;
    Arg3 = 0;
    if ((uint32_t)((uint32_t)(v_stack_mB8)) == 0) goto loc_007416ED;
loc_00741687:
    if (0 >= v_stack_m90) goto loc_007416E1;
    result = wcsnicmp(*(uint64_t *)(v_stack_m78 + 0x0 * 8), result, (uint32_t)(v_stack_mB8) - 1, result);
    Arg3 = 0;
    if ((uint32_t)(result) != 0) goto loc_007416D5;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m78 + 0x0 * 8) + (uint32_t)(v_stack_mB8) * 2 - 0x2)) == 0) goto loc_007416DE;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m78 + 0x0 * 8) + (uint32_t)(v_stack_mB8) * 2 - 0x2))) != 92) goto loc_007416D5;
    result = *(uint16_t *)(*(uint64_t *)(v_stack_m78 + 0x0 * 8) + (uint32_t)(v_stack_mB8) * 2 - 0x2);
    local_r13 = 0;
    if (v_stack_m70 != 0) {
        result = 0;
        local_r13 = (uint32_t)((0) + 1);
        *(uint64_t *)(v_stack_m70 + result * 8) = *(uint64_t *)(v_stack_m78 + 0x0 * 8) + (uint32_t)(v_stack_mB8) * 2;
    }
    local_r14 = (uint32_t)((0) + 1);
    goto loc_00741687;
loc_007416DE:
loc_007416E1:
    if (0 == 0) goto loc_007417BE;
loc_007416ED:
    local_rsi = 0;
loc_007416EF:
    if (v_stack_m68 == 0) goto loc_00741771;
    Arg4 = 0;
    v_stack_mD0 = v_stack_m98;
    Arg1 = 0;
    v_stack_mD8 = 0x20019ULL;
    result = PnpCtxRegOpenKey(Arg1, v_stack_m68, result, Arg4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00741729;
    v_stack_m98 = 0;
    goto loc_007417C0;
loc_00741729:
    if (sign_flag) goto loc_00741907;
    v_stack_mC8 = 0;
    Arg4 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    result = PnpCtxRegQueryInfoKey(Arg1, v_stack_m98, v_stack_m8C, Arg4);
    if (sign_flag) goto loc_00741909;
    if (v_stack_m8C != 0) goto loc_00741771;
    result = ZwClose(v_stack_m98, v_stack_m98, v_stack_m8C, Arg4);
    v_stack_m98 = 0;
    goto loc_00741775;
loc_00741771:
loc_00741775:
    v_stack_mC0 = v_stack_m98;
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r13))));
    v_stack_mC8 = (uint32_t)(local_r13);
    Arg1 = (v_stack_m98) & (v_stack_m70);
    v_stack_mD0 = Arg1;
    v_stack_mD8 = 0;
    result = PiDrvDbOverlayCopyKeys(v_stack_mA0, result, v_stack_m80, result);
    if (((uint32_t)(result)) != 0x8000002DULL) goto loc_007417B4;
    goto loc_007417C0;
loc_007417B4:
    if (sign_flag) goto loc_00741909;
    goto loc_007417C0;
loc_007417BE:
    local_rsi = 0;
loc_007417C0:
loc_007417C4:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_mAC)) + 1);
    goto loc_007415EF;
loc_007417CC:
    goto loc_00741918;
loc_007417D6:
    if (sign_flag) goto loc_00741909;
loc_007417E2:
    v_stack_mC0 = v_stack_mB4;
    v_stack_mC8 = result;
    v_stack_mD0 = v_stack_m84;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mB0)))) >> (1));
    v_stack_mD8 = v_stack_mB8;
    v_stack_mB8 = (uint32_t)(local_r14);
    v_stack_mB4 = (uint32_t)((uint32_t)(v_stack_mB4));
    result = PnpCtxRegEnumValue(v_stack_mA0, v_stack_mA0, 0, result);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_00741909;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007418A9;
    if (((uint32_t)((uint32_t)(v_stack_mB8))) <= ((uint32_t)(local_r14))) goto loc_0074186B;
    result = (uint32_t)(v_stack_mB8);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, 0, result);
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB8) + (uint32_t)(v_stack_mB8) * 1)), (uint32_t)(0x62647050ULL), result);
    if (result == 0) goto loc_007417CC;
loc_0074186B:
    if (((uint32_t)((uint32_t)(v_stack_mB4))) <= ((uint32_t)((uint32_t)(v_stack_mB4)))) goto loc_007418A5;
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x62647050ULL), result);
    }
    result = ExAllocatePool2(256, (uint32_t)(v_stack_mB4), (uint32_t)(0x62647050ULL), result);
    if (result == 0) goto loc_007415BB;
loc_007418A5:
    local_rsi = (uint32_t)((local_rsi) - 1);
    goto loc_00741900;
loc_007418A9:
    local_r14 = 0;
    if (sign_flag) goto loc_00741907;
    if (v_stack_m88 != 2) goto loc_007418DE;
    v_stack_mD0 = v_stack_mA8;
    Arg4 = 0;
    v_stack_mD8 = 0;
    v_stack_mA8 = 0;
    result = PnpCtxRegQueryValue(256, v_stack_m80, result, Arg4);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00741900;
loc_007418DE:
    v_stack_mD0 = (uint32_t)((uint32_t)(v_stack_mB4));
    v_stack_mD8 = result;
    result = PnpCtxRegSetValue(256, v_stack_m80, result, (uint32_t)(v_stack_m84));
    if (sign_flag) goto loc_00741909;
loc_00741900:
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_007417E2;
loc_00741907:
loc_00741909:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, result, (uint32_t)(v_stack_m84));
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, result, (uint32_t)(v_stack_m84));
    }
    result = v_stack_m70;
    if (v_stack_m70 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m70;
        result = ExFreePoolWithTag(Arg1, Arg2, result, (uint32_t)(v_stack_m84));
    }
    if (v_stack_mA0 != 0) {
        result = ZwClose(v_stack_mA0, Arg2, result, (uint32_t)(v_stack_m84));
    }
    if (v_stack_m80 != 0) {
        result = ZwClose(v_stack_m80, Arg2, result, (uint32_t)(v_stack_m84));
    }
    if (v_stack_m98 != 0) {
        result = ZwClose(v_stack_m98, Arg2, result, (uint32_t)(v_stack_m84));
    }
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, result, (uint32_t)(v_stack_m84));
    local_rsp = (local_rsp) + (184);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007413FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
