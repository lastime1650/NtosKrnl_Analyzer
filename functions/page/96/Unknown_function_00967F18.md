# sub_00967F18

- RVA: `0x00967F18`–`0x00968ACE` (길이 `2,998` bytes)
- VA: `0x0000000140967F18`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095180`
- 디코드: `782`개 명령, `2,998/2,998` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00967F6D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00967FC6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00967FE3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0096800D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096802B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009680CE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096850B` → [sub_00967B70](Unknown_function_00967B70.md) (function, `0x00967B70`)
- `0x0096853B` → [sub_00967BF0](Unknown_function_00967BF0.md) (function, `0x00967BF0`)
- `0x0096856D` → [sub_00967B40](Unknown_function_00967B40.md) (function, `0x00967B40`)
- `0x00968590` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009685AE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00968633` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00968647` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0096865B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00968669` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00968691` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009686B1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009687C0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096884C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0096887D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00968891` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009688A5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009688B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00968986` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009689CC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00968268` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00968304` → RVA `0x009EA4B0` (`PAGE`; read)
- `0x009683AE` → RVA `0x00A11250` (`PAGE`; read)
- `0x009684A5` → RVA `0x00967A50` (`PAGE`; read)
- `0x009684E0` → RVA `0x00967B70` (`PAGE`; read)
- `0x00968518` → RVA `0x00967BF0` (`PAGE`; read)
- `0x00968548` → RVA `0x00967B40` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x00967F6D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00967FC6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00967FE3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0096800D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096802B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009680CE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00968590` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009685AE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00968633` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00968647` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0096865B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00968669` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00968691` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009686B1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009687C0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096884C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0096887D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00968891` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009688A5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009688B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00968986` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009689CC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **34**
  - `0x00967F1F` → [sub_00967CA6 + 0x10C](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00967F38` → [sub_00967CA6 + 0x10C](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00967F78` → [sub_00968AF6 + 0x2249](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00967FB2` → [sub_00968AF6 + 0x2268](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00967FCE` → [sub_00968AF6 + 0x2275](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968043` → [sub_00968AF6 + 0x227D](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968054` → [sub_00968AF6 + 0x227D](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x0096805E` → [sub_00968AF6 + 0x227D](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x0096806B` → [sub_00968AF6 + 0x227D](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968078` → [sub_00968AF6 + 0x227D](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968086` → [sub_00968AF6 + 0x227D](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968093` → [sub_00968AF6 + 0x227D](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x009685FA` → [sub_00968AF6 + 0x1A](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x0096861E` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096867D` → [sub_00968AF6 + 0x2253](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968699` → [sub_00968AF6 + 0x2260](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x009686CD` → [sub_00967CA6 + 0x111](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009686D9` → [sub_00968AF6 + 0x2A](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x009686F4` → [sub_00968AF6 + 0x2287](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968717` → [sub_00968AF6 + 0x1A](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x0096872D` → [sub_00968AF6 + 0x1A](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x0096876D` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096877A` → [sub_00968AF6 + 0xA](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x0096879D` → [sub_00968AF6 + 0xA](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x009687A8` → [sub_00968AF6 + 0xA](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x009687CB` → [sub_00968AF6 + 0x2297](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x009687E1` → [sub_00968AF6 + 0x22A1](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x009687FE` → [sub_00968AF6 + 0xD0A](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968812` → [sub_00968AF6 + 0x2136](Unknown_function_00968AF6.md) (`tail-transfer`)
  - `0x00968835` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00968842` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x00968864` → [sub_00967CA6 + 0x132](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x0096886C` → [sub_00967CA6 + 0x111](Unknown_function_00967CA6.md) (`tail-transfer`)
  - `0x009688B8` → [sub_00967CA6 + 0x111](Unknown_function_00967CA6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00967F18  41 8D 48 04                     lea ecx, [r8 + 4]
00967F1C  41 3B C8                        cmp ecx, r8d
00967F1F  0F 82 8D FE FF FF               jb 0x140967db2
00967F25  8B C2                           mov eax, edx
00967F27  2B C1                           sub eax, ecx
00967F29  3B C6                           cmp eax, esi
00967F2B  0F 82 97 07 00 00               jb 0x1409686c8
00967F31  44 8D 04 0E                     lea r8d, [rsi + rcx]
00967F35  44 3B C1                        cmp r8d, ecx
00967F38  0F 82 74 FE FF FF               jb 0x140967db2
00967F3E  41 3B D0                        cmp edx, r8d
00967F41  0F 85 81 07 00 00               jne 0x1409686c8
00967F47  42 8D 0C 36                     lea ecx, [rsi + r14]
00967F4B  8B C2                           mov eax, edx
00967F4D  41 03 CD                        add ecx, r13d
00967F50  48 83 C1 0C                     add rcx, 0xc
00967F54  48 3B C8                        cmp rcx, rax
00967F57  0F 85 6B 07 00 00               jne 0x1409686c8
00967F5D  BA 30 00 00 00                  mov edx, 0x30
00967F62  B9 00 01 00 00                  mov ecx, 0x100
00967F67  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00967F6D  E8 7E A1 21 00                  call 0x140b820f0
00967F72  48 8B D8                        mov rbx, rax
00967F75  48 85 C0                        test rax, rax
00967F78  0F 84 C1 2D 00 00               je 0x14096ad3f
00967F7E  0F 57 C0                        xorps xmm0, xmm0
00967F81  0F 11 00                        movups xmmword ptr [rax], xmm0
00967F84  0F 11 40 10                     movups xmmword ptr [rax + 0x10], xmm0
00967F88  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00967F8C  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00967F90  33 FF                           xor edi, edi
00967F92  48 83 C0 04                     add rax, 4
00967F96  0F 85 DB 06 00 00               jne 0x140968677
00967F9C  89 3B                           mov dword ptr [rbx], edi
00967F9E  48 89 7B 08                     mov qword ptr [rbx + 8], rdi
00967FA2  4D 85 FF                        test r15, r15
00967FA5  0F 84 10 07 00 00               je 0x1409686bb
00967FAB  44 89 73 10                     mov dword ptr [rbx + 0x10], r14d
00967FAF  45 85 F6                        test r14d, r14d
00967FB2  0F 84 A6 2D 00 00               je 0x14096ad5e
00967FB8  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00967FBE  49 8B D6                        mov rdx, r14
00967FC1  B9 00 01 00 00                  mov ecx, 0x100
00967FC6  E8 25 A1 21 00                  call 0x140b820f0
00967FCB  48 85 C0                        test rax, rax
00967FCE  0F 84 97 2D 00 00               je 0x14096ad6b
00967FD4  4D 8B C6                        mov r8, r14
00967FD7  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00967FDB  49 8B D7                        mov rdx, r15
00967FDE  48 8B C8                        mov rcx, rax
00967FE1  33 FF                           xor edi, edi
00967FE3  E8 58 E8 D5 FF                  call 0x1406c6840
00967FE8  45 33 FF                        xor r15d, r15d
00967FEB  4D 85 E4                        test r12, r12
00967FEE  0F 84 CD 0A 00 00               je 0x140968ac1
00967FF4  89 73 20                        mov dword ptr [rbx + 0x20], esi
00967FF7  85 F6                           test esi, esi
00967FF9  0F 84 73 0A 00 00               je 0x140968a72
00967FFF  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00968005  48 8B D6                        mov rdx, rsi
00968008  B9 00 01 00 00                  mov ecx, 0x100
0096800D  E8 DE A0 21 00                  call 0x140b820f0
00968012  48 85 C0                        test rax, rax
00968015  0F 84 08 06 00 00               je 0x140968623
0096801B  4C 8B C6                        mov r8, rsi
0096801E  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00968022  49 8B D4                        mov rdx, r12
00968025  48 8B C8                        mov rcx, rax
00968028  41 8B FF                        mov edi, r15d
0096802B  E8 10 E8 D5 FF                  call 0x1406c6840
00968030  85 FF                           test edi, edi
00968032  0F 88 31 08 00 00               js 0x140968869
00968038  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0096803D  4C 8B E3                        mov r12, rbx
00968040  48 85 DB                        test rbx, rbx
00968043  0F 84 2A 2D 00 00               je 0x14096ad73
00968049  4C 8B 73 08                     mov r14, qword ptr [rbx + 8]
0096804D  4C 89 75 08                     mov qword ptr [rbp + 8], r14
00968051  4D 85 F6                        test r14, r14
00968054  0F 84 19 2D 00 00               je 0x14096ad73
0096805A  8B 0B                           mov ecx, dword ptr [rbx]
0096805C  85 C9                           test ecx, ecx
0096805E  0F 84 0F 2D 00 00               je 0x14096ad73
00968064  48 8B 5B 28                     mov rbx, qword ptr [rbx + 0x28]
00968068  48 85 DB                        test rbx, rbx
0096806B  0F 84 02 2D 00 00               je 0x14096ad73
00968071  41 8B 54 24 20                  mov edx, dword ptr [r12 + 0x20]
00968076  85 D2                           test edx, edx
00968078  0F 84 F5 2C 00 00               je 0x14096ad73
0096807E  49 8B 74 24 18                  mov rsi, qword ptr [r12 + 0x18]
00968083  48 85 F6                        test rsi, rsi
00968086  0F 84 E7 2C 00 00               je 0x14096ad73
0096808C  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
00968091  85 C0                           test eax, eax
00968093  0F 84 DA 2C 00 00               je 0x14096ad73
00968099  83 FA 08                        cmp edx, 8
0096809C  0F 85 AF 07 00 00               jne 0x140968851
009680A2  3D A0 00 00 00                  cmp eax, 0xa0
009680A7  0F 85 A4 07 00 00               jne 0x140968851
009680AD  48 83 F9 08                     cmp rcx, 8
009680B1  0F 86 9A 07 00 00               jbe 0x140968851
009680B7  48 8B 1B                        mov rbx, qword ptr [rbx]
009680BA  48 8D 51 F8                     lea rdx, [rcx - 8]
009680BE  8D 48 60                        lea ecx, [rax + 0x60]
009680C1  48 89 55 F0                     mov qword ptr [rbp - 0x10], rdx
009680C5  41 B8 53 4C 53 20               mov r8d, 0x20534c53
009680CB  40 32 FF                        xor dil, dil
009680CE  E8 1D A0 21 00                  call 0x140b820f0
009680D3  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
009680D7  48 85 C0                        test rax, rax
009680DA  0F 84 71 07 00 00               je 0x140968851
009680E0  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
009680E4  4D 8B E6                        mov r12, r14
009680E7  4D 8B F1                        mov r14, r9
009680EA  48 89 9D 10 01 00 00            mov qword ptr [rbp + 0x110], rbx
009680F1  41 83 E6 07                     and r14d, 7
009680F5  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
009680F9  4C 89 75 C0                     mov qword ptr [rbp - 0x40], r14
009680FD  B9 1E 00 00 00                  mov ecx, 0x1e
00968102  0F 85 B5 07 00 00               jne 0x1409688bd
00968108  B9 FF FF FF FF                  mov ecx, 0xffffffff
0096810D  44 89 7D A4                     mov dword ptr [rbp - 0x5c], r15d
00968111  89 4D 88                        mov dword ptr [rbp - 0x78], ecx
00968114  4C 8D 9E 9E 00 00 00            lea r11, [rsi + 0x9e]
0096811B  89 4D A8                        mov dword ptr [rbp - 0x58], ecx
0096811E  45 8B EF                        mov r13d, r15d
00968121  48 8D 4E 7E                     lea rcx, [rsi + 0x7e]
00968125  4C 89 5D F8                     mov qword ptr [rbp - 8], r11
00968129  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
0096812D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00968132  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00968137  49 8B C9                        mov rcx, r9
0096813A  48 C1 E9 03                     shr rcx, 3
0096813E  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00968142  48 85 C9                        test rcx, rcx
00968145  0F 84 71 04 00 00               je 0x1409685bc
0096814B  48 83 C0 07                     add rax, 7
0096814F  4D 8D 44 24 02                  lea r8, [r12 + 2]
00968154  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00968158  66 90                           nop
0096815A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00968160  41 0F B6 40 FF                  movzx eax, byte ptr [r8 - 1]
00968165  41 0F B6 48 FE                  movzx ecx, byte ptr [r8 - 2]
0096816A  41 0F B6 50 02                  movzx edx, byte ptr [r8 + 2]
0096816F  44 0F B7 8D 12 01 00 00         movzx r9d, word ptr [rbp + 0x112]
00968177  C1 E1 08                        shl ecx, 8
0096817A  0B C8                           or ecx, eax
0096817C  C1 E2 08                        shl edx, 8
0096817F  41 0F B6 00                     movzx eax, byte ptr [r8]
00968183  C1 E1 08                        shl ecx, 8
00968186  0B C8                           or ecx, eax
00968188  41 0F B6 40 01                  movzx eax, byte ptr [r8 + 1]
0096818D  C1 E1 08                        shl ecx, 8
00968190  0B C8                           or ecx, eax
00968192  41 0F B6 40 03                  movzx eax, byte ptr [r8 + 3]
00968197  44 33 F9                        xor r15d, ecx
0096819A  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
0096819D  0B D0                           or edx, eax
0096819F  41 0F B6 40 04                  movzx eax, byte ptr [r8 + 4]
009681A4  C1 E2 08                        shl edx, 8
009681A7  0B D0                           or edx, eax
009681A9  41 0F B6 40 05                  movzx eax, byte ptr [r8 + 5]
009681AE  C1 E2 08                        shl edx, 8
009681B1  49 83 C0 08                     add r8, 8
009681B5  0B D0                           or edx, eax
009681B7  4C 89 45 38                     mov qword ptr [rbp + 0x38], r8
009681BB  44 33 EA                        xor r13d, edx
009681BE  89 55 C8                        mov dword ptr [rbp - 0x38], edx
009681C1  8B 95 14 01 00 00               mov edx, dword ptr [rbp + 0x114]
009681C7  8B C2                           mov eax, edx
009681C9  33 C3                           xor eax, ebx
009681CB  44 0F B7 D2                     movzx r10d, dx
009681CF  44 33 E8                        xor r13d, eax
009681D2  44 0F B7 C3                     movzx r8d, bx
009681D6  45 33 EF                        xor r13d, r15d
009681D9  41 8B CD                        mov ecx, r13d
009681DC  41 8B C5                        mov eax, r13d
009681DF  41 33 C9                        xor ecx, r9d
009681E2  C1 E8 08                        shr eax, 8
009681E5  41 0F AF CA                     imul ecx, r10d
009681E9  33 C8                           xor ecx, eax
009681EB  44 33 F9                        xor r15d, ecx
009681EE  8B CA                           mov ecx, edx
009681F0  41 2B CF                        sub ecx, r15d
009681F3  41 8B C7                        mov eax, r15d
009681F6  C1 C9 0B                        ror ecx, 0xb
009681F9  41 0F AF C9                     imul ecx, r9d
009681FD  C1 C8 0C                        ror eax, 0xc
00968200  2B C8                           sub ecx, eax
00968202  44 33 E9                        xor r13d, ecx
00968205  41 33 D5                        xor edx, r13d
00968208  41 8B C5                        mov eax, r13d
0096820B  C1 C8 1E                        ror eax, 0x1e
0096820E  C1 CA 18                        ror edx, 0x18
00968211  41 0F AF D0                     imul edx, r8d
00968215  2B D0                           sub edx, eax
00968217  44 33 FA                        xor r15d, edx
0096821A  0F B7 95 16 01 00 00            movzx edx, word ptr [rbp + 0x116]
00968221  41 8B CF                        mov ecx, r15d
00968224  41 8B C7                        mov eax, r15d
00968227  2B CB                           sub ecx, ebx
00968229  C1 C8 09                        ror eax, 9
0096822C  C1 C9 04                        ror ecx, 4
0096822F  0F AF CA                        imul ecx, edx
00968232  33 C8                           xor ecx, eax
00968234  44 33 E9                        xor r13d, ecx
00968237  8B CB                           mov ecx, ebx
00968239  41 2B CD                        sub ecx, r13d
0096823C  41 8B C5                        mov eax, r13d
0096823F  C1 C9 0A                        ror ecx, 0xa
00968242  41 0F AF CA                     imul ecx, r10d
00968246  C1 C8 04                        ror eax, 4
00968249  03 C8                           add ecx, eax
0096824B  44 33 F9                        xor r15d, ecx
0096824E  8B CA                           mov ecx, edx
00968250  41 33 CF                        xor ecx, r15d
00968253  41 8B C7                        mov eax, r15d
00968256  C1 C9 1C                        ror ecx, 0x1c
00968259  41 0F AF C9                     imul ecx, r9d
0096825D  C1 C8 10                        ror eax, 0x10
00968260  2B C8                           sub ecx, eax
00968262  44 33 E9                        xor r13d, ecx
00968265  41 8B CD                        mov ecx, r13d
00968268  48 8D 3D 91 7D 69 FF            lea rdi, [rip - 0x96826f]
0096826F  C1 C9 07                        ror ecx, 7
00968272  41 8B C1                        mov eax, r9d
00968275  41 33 C5                        xor eax, r13d
00968278  41 BC 10 00 00 00               mov r12d, 0x10
0096827E  41 0F AF C0                     imul eax, r8d
00968282  41 BE 1E 00 00 00               mov r14d, 0x1e
00968288  49 8B F3                        mov rsi, r11
0096828B  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
0096828F  2B C1                           sub eax, ecx
00968291  44 33 F8                        xor r15d, eax
00968294  41 8B C7                        mov eax, r15d
00968297  2B C3                           sub eax, ebx
00968299  2B C2                           sub eax, edx
0096829B  44 33 E8                        xor r13d, eax
0096829E  41 2B DD                        sub ebx, r13d
009682A1  41 8B C5                        mov eax, r13d
009682A4  C1 C8 0B                        ror eax, 0xb
009682A7  C1 CB 09                        ror ebx, 9
009682AA  41 0F AF DA                     imul ebx, r10d
009682AE  33 D8                           xor ebx, eax
009682B0  44 33 FB                        xor r15d, ebx
009682B3  48 8B 5D 18                     mov rbx, qword ptr [rbp + 0x18]
009682B7  41 8B CF                        mov ecx, r15d
009682BA  41 8B C7                        mov eax, r15d
009682BD  41 2B CA                        sub ecx, r10d
009682C0  C1 E8 0D                        shr eax, 0xd
009682C3  41 0F AF C9                     imul ecx, r9d
009682C7  2B C8                           sub ecx, eax
009682C9  44 33 E9                        xor r13d, ecx
009682CC  41 8B C5                        mov eax, r13d
009682CF  41 2B C2                        sub eax, r10d
009682D2  8B C8                           mov ecx, eax
009682D4  C1 E9 1D                        shr ecx, 0x1d
009682D7  8D 04 C5 00 00 00 00            lea eax, [rax*8]
009682DE  0B C8                           or ecx, eax
009682E0  41 8B C5                        mov eax, r13d
009682E3  41 0F AF C8                     imul ecx, r8d
009682E7  C1 E8 0F                        shr eax, 0xf
009682EA  33 C8                           xor ecx, eax
009682EC  44 33 F9                        xor r15d, ecx
009682EF  90                              nop
009682F0  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
009682F4  3C 1F                           cmp al, 0x1f
009682F6  0F 83 A3 00 00 00               jae 0x14096839f
009682FC  48 8B 84 C7 C0 84 FD 00         mov rax, qword ptr [rdi + rax*8 + 0xfd84c0]
00968304  48 8D 15 A5 21 08 00            lea rdx, [rip + 0x821a5]
0096830B  0F B6 4B 01                     movzx ecx, byte ptr [rbx + 1]
0096830F  4D 8D 56 01                     lea r10, [r14 + 1]
00968313  44 0F B6 0B                     movzx r9d, byte ptr [rbx]
00968317  44 0F B6 63 FF                  movzx r12d, byte ptr [rbx - 1]
0096831C  44 0F B6 5B FE                  movzx r11d, byte ptr [rbx - 2]
00968321  48 3B C2                        cmp rax, rdx
00968324  0F 85 B6 01 00 00               jne 0x1409684e0
0096832A  41 83 E2 03                     and r10d, 3
0096832E  41 0F B6 CB                     movzx ecx, r11b
00968332  48 B8 89 88 88 88 88 88 88 88   movabs rax, 0x8888888888888889
0096833C  49 F7 E3                        mul r11
0096833F  42 0F B7 84 55 10 01 00 00      movzx eax, word ptr [rbp + r10*2 + 0x110]
00968348  48 C1 EA 03                     shr rdx, 3
0096834C  4C 6B C2 0F                     imul r8, rdx, 0xf
00968350  41 8B D7                        mov edx, r15d
00968353  41 2A C8                        sub cl, r8b
00968356  F7 D2                           not edx
00968358  44 8B CA                        mov r9d, edx
0096835B  FE C1                           inc cl
0096835D  41 D3 E9                        shr r9d, cl
00968360  45 2A C3                        sub r8b, r11b
00968363  41 8D 48 1F                     lea ecx, [r8 + 0x1f]
00968367  D3 E2                           shl edx, cl
00968369  44 0B CA                        or r9d, edx
0096836C  44 03 C8                        add r9d, eax
0096836F  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00968379  49 F7 E4                        mul r12
0096837C  49 8D 42 01                     lea rax, [r10 + 1]
00968380  48 D1 EA                        shr rdx, 1
00968383  49 03 D4                        add rdx, r12
00968386  48 03 C2                        add rax, rdx
00968389  83 E0 03                        and eax, 3
0096838C  0F B7 8C 45 10 01 00 00         movzx ecx, word ptr [rbp + rax*2 + 0x110]
00968394  44 0F AF C9                     imul r9d, ecx
00968398  4C 8B 65 B8                     mov r12, qword ptr [rbp - 0x48]
0096839C  45 33 E9                        xor r13d, r9d
0096839F  0F B6 06                        movzx eax, byte ptr [rsi]
009683A2  3C 1F                           cmp al, 0x1f
009683A4  73 4D                           jae 0x1409683f3
009683A6  48 8B 84 C7 C0 84 FD 00         mov rax, qword ptr [rdi + rax*8 + 0xfd84c0]
009683AE  4C 8D 15 9B 8E 0A 00            lea r10, [rip + 0xa8e9b]
009683B5  0F B6 4B FD                     movzx ecx, byte ptr [rbx - 3]
009683B9  44 0F B6 4B FC                  movzx r9d, byte ptr [rbx - 4]
009683BE  44 0F B6 43 FB                  movzx r8d, byte ptr [rbx - 5]
009683C3  0F B6 53 FA                     movzx edx, byte ptr [rbx - 6]
009683C7  49 3B C2                        cmp rax, r10
009683CA  0F 85 D5 00 00 00               jne 0x1409684a5
009683D0  49 8B D6                        mov rdx, r14
009683D3  41 8B C5                        mov eax, r13d
009683D6  83 E2 01                        and edx, 1
009683D9  33 84 95 10 01 00 00            xor eax, dword ptr [rbp + rdx*4 + 0x110]
009683E0  48 8D 4A FF                     lea rcx, [rdx - 1]
009683E4  83 E1 01                        and ecx, 1
009683E7  8B 94 8D 10 01 00 00            mov edx, dword ptr [rbp + rcx*4 + 0x110]
009683EE  2B D0                           sub edx, eax
009683F0  44 33 FA                        xor r15d, edx
009683F3  49 83 EE 02                     sub r14, 2
009683F7  48 83 EE 02                     sub rsi, 2
009683FB  48 83 EB 08                     sub rbx, 8
009683FF  49 83 EC 01                     sub r12, 1
00968403  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
00968407  0F 85 E3 FE FF FF               jne 0x1409682f0
0096840D  4C 8B 5D D0                     mov r11, qword ptr [rbp - 0x30]
00968411  44 33 7D A4                     xor r15d, dword ptr [rbp - 0x5c]
00968415  44 33 6D A8                     xor r13d, dword ptr [rbp - 0x58]
00968419  41 8B CF                        mov ecx, r15d
0096841C  8B 7D C8                        mov edi, dword ptr [rbp - 0x38]
0096841F  41 8B C7                        mov eax, r15d
00968422  C1 E8 08                        shr eax, 8
00968425  41 8B D5                        mov edx, r13d
00968428  45 88 7B FC                     mov byte ptr [r11 - 4], r15b
0096842C  45 88 2B                        mov byte ptr [r11], r13b
0096842F  C1 E1 18                        shl ecx, 0x18
00968432  0B C8                           or ecx, eax
00968434  C1 E2 18                        shl edx, 0x18
00968437  41 88 4B FB                     mov byte ptr [r11 - 5], cl
0096843B  44 8B C1                        mov r8d, ecx
0096843E  41 C1 E0 18                     shl r8d, 0x18
00968442  41 8B C5                        mov eax, r13d
00968445  C1 E8 08                        shr eax, 8
00968448  0B D0                           or edx, eax
0096844A  C1 E9 08                        shr ecx, 8
0096844D  41 88 53 FF                     mov byte ptr [r11 - 1], dl
00968451  44 0B C1                        or r8d, ecx
00968454  45 88 43 FA                     mov byte ptr [r11 - 6], r8b
00968458  8B C2                           mov eax, edx
0096845A  C1 E0 18                        shl eax, 0x18
0096845D  C1 EA 08                        shr edx, 8
00968460  0B C2                           or eax, edx
00968462  41 C1 C8 08                     ror r8d, 8
00968466  41 88 43 FE                     mov byte ptr [r11 - 2], al
0096846A  C1 C8 08                        ror eax, 8
0096846D  45 88 43 F9                     mov byte ptr [r11 - 7], r8b
00968471  41 88 43 FD                     mov byte ptr [r11 - 3], al
00968475  49 83 C3 08                     add r11, 8
00968479  48 83 6D C0 01                  sub qword ptr [rbp - 0x40], 1
0096847E  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
00968481  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00968484  89 7D A8                        mov dword ptr [rbp - 0x58], edi
00968487  4C 89 5D D0                     mov qword ptr [rbp - 0x30], r11
0096848B  0F 84 24 01 00 00               je 0x1409685b5
00968491  48 8B 9D 10 01 00 00            mov rbx, qword ptr [rbp + 0x110]
00968498  4C 8B 45 38                     mov r8, qword ptr [rbp + 0x38]
0096849C  4C 8B 5D F8                     mov r11, qword ptr [rbp - 8]
009684A0  E9 BB FC FF FF                  jmp 0x140968160
009684A5  4C 8D 15 A4 F5 FF FF            lea r10, [rip - 0xa5c]
009684AC  49 3B C2                        cmp rax, r10
009684AF  0F 85 93 00 00 00               jne 0x140968548
009684B5  49 8B C6                        mov rax, r14
009684B8  41 8B D5                        mov edx, r13d
009684BB  83 E0 03                        and eax, 3
009684BE  0F B7 8C 45 10 01 00 00         movzx ecx, word ptr [rbp + rax*2 + 0x110]
009684C6  49 8B C6                        mov rax, r14
009684C9  48 D1 E8                        shr rax, 1
009684CC  2B D1                           sub edx, ecx
009684CE  48 FF C8                        dec rax
009684D1  83 E0 01                        and eax, 1
009684D4  33 94 85 10 01 00 00            xor edx, dword ptr [rbp + rax*4 + 0x110]
009684DB  E9 10 FF FF FF                  jmp 0x1409683f0
009684E0  48 8D 15 89 F6 FF FF            lea rdx, [rip - 0x977]
009684E7  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
009684EC  4D 8B C4                        mov r8, r12
009684EF  48 3B C2                        cmp rax, rdx
009684F2  75 24                           jne 0x140968518
009684F4  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
009684FB  49 8B D3                        mov rdx, r11
009684FE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968503  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00968508  49 8B CA                        mov rcx, r10
0096850B  E8 60 F6 FF FF                  call 0x140967b70
00968510  44 8B C8                        mov r9d, eax
00968513  E9 80 FE FF FF                  jmp 0x140968398
00968518  48 8D 15 D1 F6 FF FF            lea rdx, [rip - 0x92f]
0096851F  48 3B C2                        cmp rax, rdx
00968522  75 55                           jne 0x140968579
00968524  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
0096852B  49 8B D3                        mov rdx, r11
0096852E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968533  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00968538  49 8B CA                        mov rcx, r10
0096853B  E8 B0 F6 FF FF                  call 0x140967bf0
00968540  44 8B C8                        mov r9d, eax
00968543  E9 50 FE FF FF                  jmp 0x140968398
00968548  4C 8D 15 F1 F5 FF FF            lea r10, [rip - 0xa0f]
0096854F  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00968554  49 3B C2                        cmp rax, r10
00968557  75 41                           jne 0x14096859a
00968559  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
00968560  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00968565  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0096856A  49 8B CE                        mov rcx, r14
0096856D  E8 CE F5 FF FF                  call 0x140967b40
00968572  8B D0                           mov edx, eax
00968574  E9 77 FE FF FF                  jmp 0x1409683f0
00968579  48 8D 95 10 01 00 00            lea rdx, [rbp + 0x110]
00968580  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00968585  49 8B D3                        mov rdx, r11
00968588  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0096858D  49 8B CA                        mov rcx, r10
00968590  E8 3B 25 D5 FF                  call 0x1406baad0
00968595  E9 76 FF FF FF                  jmp 0x140968510
0096859A  4C 8D 95 10 01 00 00            lea r10, [rbp + 0x110]
009685A1  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
009685A6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009685AB  49 8B CE                        mov rcx, r14
009685AE  E8 1D 25 D5 FF                  call 0x1406baad0
009685B3  EB BD                           jmp 0x140968572
009685B5  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
009685B9  40 32 FF                        xor dil, dil
009685BC  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
009685C0  45 33 FF                        xor r15d, r15d
009685C3  41 8B C7                        mov eax, r15d
009685C6  4D 85 C9                        test r9, r9
009685C9  74 11                           je 0x1409685dc
009685CB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
009685D0  41 32 3C 00                     xor dil, byte ptr [r8 + rax]
009685D4  48 FF C0                        inc rax
009685D7  49 3B C1                        cmp rax, r9
009685DA  72 F4                           jb 0x1409685d0
009685DC  48 8B 55 08                     mov rdx, qword ptr [rbp + 8]
009685E0  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
009685E5  40 0F B6 C7                     movzx eax, dil
009685E9  49 3B 04 11                     cmp rax, qword ptr [r9 + rdx]
009685ED  0F 85 54 02 00 00               jne 0x140968847
009685F3  4D 8B F0                        mov r14, r8
009685F6  41 83 F9 04                     cmp r9d, 4
009685FA  0F 82 10 05 00 00               jb 0x140968b10
00968600  41 8B 00                        mov eax, dword ptr [r8]
00968603  49 8D 50 04                     lea rdx, [r8 + 4]
00968607  89 45 C8                        mov dword ptr [rbp - 0x38], eax
0096860A  49 3B D0                        cmp rdx, r8
0096860D  0F 83 BF 00 00 00               jae 0x1409686d2
00968613  BF 95 00 00 C0                  mov edi, 0xc0000095
00968618  4D 8B EF                        mov r13, r15
0096861B  49 8B F7                        mov rsi, r15
0096861E  E9 B5 F7 FF FF                  jmp 0x140967dd8
00968623  BF 17 00 00 C0                  mov edi, 0xc0000017
00968628  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0096862C  48 85 C9                        test rcx, rcx
0096862F  74 0B                           je 0x14096863c
00968631  33 D2                           xor edx, edx
00968633  E8 38 A2 21 00                  call 0x140b82870
00968638  4C 89 7B 08                     mov qword ptr [rbx + 8], r15
0096863C  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00968640  48 85 C9                        test rcx, rcx
00968643  74 0B                           je 0x140968650
00968645  33 D2                           xor edx, edx
00968647  E8 24 A2 21 00                  call 0x140b82870
0096864C  4C 89 7B 18                     mov qword ptr [rbx + 0x18], r15
00968650  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00968654  48 85 C9                        test rcx, rcx
00968657  74 0B                           je 0x140968664
00968659  33 D2                           xor edx, edx
0096865B  E8 10 A2 21 00                  call 0x140b82870
00968660  4C 89 7B 28                     mov qword ptr [rbx + 0x28], r15
00968664  33 D2                           xor edx, edx
00968666  48 8B CB                        mov rcx, rbx
00968669  E8 02 A2 21 00                  call 0x140b82870
0096866E  48 8B 5D 18                     mov rbx, qword ptr [rbp + 0x18]
00968672  E9 B9 F9 FF FF                  jmp 0x140968030
00968677  44 89 2B                        mov dword ptr [rbx], r13d
0096867A  45 85 ED                        test r13d, r13d
0096867D  0F 84 C6 26 00 00               je 0x14096ad49
00968683  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00968689  49 8B D5                        mov rdx, r13
0096868C  B9 00 01 00 00                  mov ecx, 0x100
00968691  E8 5A 9A 21 00                  call 0x140b820f0
00968696  48 85 C0                        test rax, rax
00968699  0F 84 B7 26 00 00               je 0x14096ad56
0096869F  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
009686A3  4D 8B C5                        mov r8, r13
009686A6  48 83 C2 04                     add rdx, 4
009686AA  48 89 43 08                     mov qword ptr [rbx + 8], rax
009686AE  48 8B C8                        mov rcx, rax
009686B1  E8 8A E1 D5 FF                  call 0x1406c6840
009686B6  E9 E7 F8 FF FF                  jmp 0x140967fa2
009686BB  44 89 7B 10                     mov dword ptr [rbx + 0x10], r15d
009686BF  4C 89 7B 18                     mov qword ptr [rbx + 0x18], r15
009686C3  E9 23 F9 FF FF                  jmp 0x140967feb
009686C8  BF 3E 00 00 C0                  mov edi, 0xc000003e
009686CD  E9 E5 F6 FF FF                  jmp 0x140967db7
009686D2  41 8D 41 FC                     lea eax, [r9 - 4]
009686D6  83 F8 04                        cmp eax, 4
009686D9  0F 82 41 04 00 00               jb 0x140968b20
009686DF  8B 32                           mov esi, dword ptr [rdx]
009686E1  48 8D 5A 04                     lea rbx, [rdx + 4]
009686E5  48 3B DA                        cmp rbx, rdx
009686E8  0F 82 25 FF FF FF               jb 0x140968613
009686EE  41 8D 41 F8                     lea eax, [r9 - 8]
009686F2  3B C6                           cmp eax, esi
009686F4  0F 82 83 26 00 00               jb 0x14096ad7d
009686FA  8D 46 08                        lea eax, [rsi + 8]
009686FD  83 F8 08                        cmp eax, 8
00968700  0F 82 0D FF FF FF               jb 0x140968613
00968706  41 8B C9                        mov ecx, r9d
00968709  48 8D 14 1E                     lea rdx, [rsi + rbx]
0096870D  44 8B DE                        mov r11d, esi
00968710  49 8D 04 08                     lea rax, [r8 + rcx]
00968714  48 3B C2                        cmp rax, rdx
00968717  0F 82 F3 03 00 00               jb 0x140968b10
0096871D  49 8B C0                        mov rax, r8
00968720  48 2B C6                        sub rax, rsi
00968723  48 2B C3                        sub rax, rbx
00968726  48 03 C1                        add rax, rcx
00968729  48 83 F8 08                     cmp rax, 8
0096872D  0F 83 DD 03 00 00               jae 0x140968b10
00968733  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00968738  4D 8B EF                        mov r13, r15
0096873B  41 8B FF                        mov edi, r15d
0096873E  48 85 DB                        test rbx, rbx
00968741  74 6B                           je 0x1409687ae
00968743  48 8B CB                        mov rcx, rbx
00968746  48 3B D3                        cmp rdx, rbx
00968749  0F 82 EB 00 00 00               jb 0x14096883a
0096874F  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00968754  48 3B CA                        cmp rcx, rdx
00968757  73 4F                           jae 0x1409687a8
00968759  48 8D 41 04                     lea rax, [rcx + 4]
0096875D  48 3B C1                        cmp rax, rcx
00968760  73 10                           jae 0x140968772
00968762  BF 95 00 00 C0                  mov edi, 0xc0000095
00968767  4D 8B FD                        mov r15, r13
0096876A  49 8B F5                        mov rsi, r13
0096876D  E9 66 F6 FF FF                  jmp 0x140967dd8
00968772  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00968777  48 3B C2                        cmp rax, rdx
0096877A  0F 87 80 03 00 00               ja 0x140968b00
00968780  8B 01                           mov eax, dword ptr [rcx]
00968782  83 C0 04                        add eax, 4
00968785  83 F8 04                        cmp eax, 4
00968788  72 D8                           jb 0x140968762
0096878A  44 8B C0                        mov r8d, eax
0096878D  4C 03 C1                        add r8, rcx
00968790  4C 3B C1                        cmp r8, rcx
00968793  72 CD                           jb 0x140968762
00968795  33 FF                           xor edi, edi
00968797  49 8B C8                        mov rcx, r8
0096879A  4C 3B C2                        cmp r8, rdx
0096879D  0F 87 5D 03 00 00               ja 0x140968b00
009687A3  41 FF C7                        inc r15d
009687A6  EB AC                           jmp 0x140968754
009687A8  0F 85 52 03 00 00               jne 0x140968b00
009687AE  85 F6                           test esi, esi
009687B0  74 24                           je 0x1409687d6
009687B2  41 B8 53 4C 53 20               mov r8d, 0x20534c53
009687B8  48 8B D6                        mov rdx, rsi
009687BB  B9 00 01 00 00                  mov ecx, 0x100
009687C0  E8 2B 99 21 00                  call 0x140b820f0
009687C5  4C 8B E8                        mov r13, rax
009687C8  48 85 C0                        test rax, rax
009687CB  0F 84 BC 25 00 00               je 0x14096ad8d
009687D1  33 FF                           xor edi, edi
009687D3  4C 8B DE                        mov r11, rsi
009687D6  4D 8B F4                        mov r14, r12
009687D9  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
009687DE  48 85 DB                        test rbx, rbx
009687E1  0F 85 B0 25 00 00               jne 0x14096ad97
009687E7  4C 89 6D 98                     mov qword ptr [rbp - 0x68], r13
009687EB  89 75 94                        mov dword ptr [rbp - 0x6c], esi
009687EE  44 89 7D 90                     mov dword ptr [rbp - 0x70], r15d
009687F2  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
009687F7  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
009687FC  85 FF                           test edi, edi
009687FE  0F 88 FC 0F 00 00               js 0x140969800
00968804  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00968809  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0096880E  44 39 7D C8                     cmp dword ptr [rbp - 0x38], r15d
00968812  0F 84 14 24 00 00               je 0x14096ac2c
00968818  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0096881D  BF 3E 00 00 C0                  mov edi, 0xc000003e
00968822  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00968827  4D 8B FD                        mov r15, r13
0096882A  4D 8B E6                        mov r12, r14
0096882D  49 8B F5                        mov rsi, r13
00968830  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00968835  E9 9E F5 FF FF                  jmp 0x140967dd8
0096883A  BF 95 00 00 C0                  mov edi, 0xc0000095
0096883F  49 8B F5                        mov rsi, r13
00968842  E9 91 F5 FF FF                  jmp 0x140967dd8
00968847  33 D2                           xor edx, edx
00968849  49 8B C8                        mov rcx, r8
0096884C  E8 1F A0 21 00                  call 0x140b82870
00968851  BF 01 00 00 C0                  mov edi, 0xc0000001
00968856  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0096885B  4D 8B EE                        mov r13, r14
0096885E  4D 8B FE                        mov r15, r14
00968861  49 8B F6                        mov rsi, r14
00968864  E9 6F F5 FF FF                  jmp 0x140967dd8
00968869  48 85 DB                        test rbx, rbx
0096886C  0F 84 45 F5 FF FF               je 0x140967db7
00968872  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00968876  48 85 C9                        test rcx, rcx
00968879  74 0B                           je 0x140968886
0096887B  33 D2                           xor edx, edx
0096887D  E8 EE 9F 21 00                  call 0x140b82870
00968882  4C 89 7B 08                     mov qword ptr [rbx + 8], r15
00968886  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
0096888A  48 85 C9                        test rcx, rcx
0096888D  74 0B                           je 0x14096889a
0096888F  33 D2                           xor edx, edx
00968891  E8 DA 9F 21 00                  call 0x140b82870
00968896  4C 89 7B 18                     mov qword ptr [rbx + 0x18], r15
0096889A  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
0096889E  48 85 C9                        test rcx, rcx
009688A1  74 0B                           je 0x1409688ae
009688A3  33 D2                           xor edx, edx
009688A5  E8 C6 9F 21 00                  call 0x140b82870
009688AA  4C 89 7B 28                     mov qword ptr [rbx + 0x28], r15
009688AE  33 D2                           xor edx, edx
009688B0  48 8B CB                        mov rcx, rbx
009688B3  E8 B8 9F 21 00                  call 0x140b82870
009688B8  E9 FA F4 FF FF                  jmp 0x140967db7
009688BD  45 33 C9                        xor r9d, r9d
009688C0  45 33 D2                        xor r10d, r10d
009688C3  B8 FF FF FF FF                  mov eax, 0xffffffff
009688C8  44 89 4D A8                     mov dword ptr [rbp - 0x58], r9d
009688CC  45 33 C0                        xor r8d, r8d
009688CF  89 45 88                        mov dword ptr [rbp - 0x78], eax
009688D2  44 89 55 A4                     mov dword ptr [rbp - 0x5c], r10d
009688D6  44 8B E8                        mov r13d, eax
009688D9  45 85 F6                        test r14d, r14d
009688DC  74 40                           je 0x14096891e
009688DE  4C 8B 5C 24 70                  mov r11, qword ptr [rsp + 0x70]
009688E3  41 8D 51 38                     lea edx, [r9 + 0x38]
009688E7  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
009688EC  41 0F B6 04 24                  movzx eax, byte ptr [r12]
009688F1  49 FF C4                        inc r12
009688F4  41 83 F8 04                     cmp r8d, 4
009688F8  0F 83 7E 01 00 00               jae 0x140968a7c
009688FE  8D 4A E0                        lea ecx, [rdx - 0x20]
00968901  D3 E0                           shl eax, cl
00968903  44 0B D0                        or r10d, eax
00968906  41 FF C0                        inc r8d
00968909  83 EA 08                        sub edx, 8
0096890C  45 3B C6                        cmp r8d, r14d
0096890F  7C DB                           jl 0x1409688ec
00968911  44 89 55 A4                     mov dword ptr [rbp - 0x5c], r10d
00968915  B9 1E 00 00 00                  mov ecx, 0x1e
0096891A  44 89 4D A8                     mov dword ptr [rbp - 0x58], r9d
0096891E  48 8B F9                        mov rdi, rcx
00968921  48 8D 86 9E 00 00 00            lea rax, [rsi + 0x9e]
00968928  48 8D 4E 7E                     lea rcx, [rsi + 0x7e]
0096892C  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00968930  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
00968934  4C 8D 35 C5 76 69 FF            lea r14, [rip - 0x96893b]
0096893B  48 8B D9                        mov rbx, rcx
0096893E  48 8B F0                        mov rsi, rax
00968941  B9 10 00 00 00                  mov ecx, 0x10
00968946  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0096894A  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
0096894E  3C 1F                           cmp al, 0x1f
00968950  73 40                           jae 0x140968992
00968952  44 0F B6 53 01                  movzx r10d, byte ptr [rbx + 1]
00968957  4C 8D 9D 10 01 00 00            lea r11, [rbp + 0x110]
0096895E  49 8B 84 C6 C0 84 FD 00         mov rax, qword ptr [r14 + rax*8 + 0xfd84c0]
00968966  48 8D 4F 01                     lea rcx, [rdi + 1]
0096896A  44 0F B6 0B                     movzx r9d, byte ptr [rbx]
0096896E  44 0F B6 43 FF                  movzx r8d, byte ptr [rbx - 1]
00968973  0F B6 53 FE                     movzx edx, byte ptr [rbx - 2]
00968977  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
0096897C  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
00968981  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00968986  E8 45 21 D5 FF                  call 0x1406baad0
0096898B  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
0096898F  44 33 E8                        xor r13d, eax
00968992  0F B6 06                        movzx eax, byte ptr [rsi]
00968995  3C 1F                           cmp al, 0x1f
00968997  73 3F                           jae 0x1409689d8
00968999  0F B6 4B FD                     movzx ecx, byte ptr [rbx - 3]
0096899D  4C 8D 95 10 01 00 00            lea r10, [rbp + 0x110]
009689A4  49 8B 84 C6 C0 84 FD 00         mov rax, qword ptr [r14 + rax*8 + 0xfd84c0]
009689AC  44 0F B6 4B FC                  movzx r9d, byte ptr [rbx - 4]
009689B1  44 0F B6 43 FB                  movzx r8d, byte ptr [rbx - 5]
009689B6  0F B6 53 FA                     movzx edx, byte ptr [rbx - 6]
009689BA  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
009689BF  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
009689C4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009689C9  48 8B CF                        mov rcx, rdi
009689CC  E8 FF 20 D5 FF                  call 0x1406baad0
009689D1  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
009689D5  44 33 F8                        xor r15d, eax
009689D8  48 83 EF 02                     sub rdi, 2
009689DC  48 83 EE 02                     sub rsi, 2
009689E0  48 83 EB 08                     sub rbx, 8
009689E4  48 83 E9 01                     sub rcx, 1
009689E8  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
009689EC  0F 85 58 FF FF FF               jne 0x14096894a
009689F2  44 33 7D A4                     xor r15d, dword ptr [rbp - 0x5c]
009689F6  45 33 D2                        xor r10d, r10d
009689F9  44 33 6D A8                     xor r13d, dword ptr [rbp - 0x58]
009689FD  45 8B C7                        mov r8d, r15d
00968A00  4C 8B 75 C0                     mov r14, qword ptr [rbp - 0x40]
00968A04  45 8B CD                        mov r9d, r13d
00968A07  41 0F B6 FA                     movzx edi, r10b
00968A0B  45 85 F6                        test r14d, r14d
00968A0E  0F 84 8B 00 00 00               je 0x140968a9f
00968A14  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
00968A18  4C 8D 5A 01                     lea r11, [rdx + 1]
00968A1C  41 83 FA 04                     cmp r10d, 4
00968A20  73 66                           jae 0x140968a88
00968A22  41 8B C8                        mov ecx, r8d
00968A25  41 8B C0                        mov eax, r8d
00968A28  C1 E9 18                        shr ecx, 0x18
00968A2B  C1 E0 08                        shl eax, 8
00968A2E  44 8B C1                        mov r8d, ecx
00968A31  44 0B C0                        or r8d, eax
00968A34  41 8B C0                        mov eax, r8d
00968A37  41 FF C2                        inc r10d
00968A3A  88 02                           mov byte ptr [rdx], al
00968A3C  49 8B D3                        mov rdx, r11
00968A3F  45 3B D6                        cmp r10d, r14d
00968A42  7C D4                           jl 0x140968a18
00968A44  49 8B C3                        mov rax, r11
00968A47  41 83 FE 04                     cmp r14d, 4
00968A4B  76 58                           jbe 0x140968aa5
00968A4D  B9 08 00 00 00                  mov ecx, 8
00968A52  41 2B CE                        sub ecx, r14d
00968A55  C1 E1 03                        shl ecx, 3
00968A58  41 D3 ED                        shr r13d, cl
00968A5B  41 D3 E5                        shl r13d, cl
00968A5E  48 8B 9D 10 01 00 00            mov rbx, qword ptr [rbp + 0x110]
00968A65  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
00968A69  4C 8B 5D F8                     mov r11, qword ptr [rbp - 8]
00968A6D  E9 C5 F6 FF FF                  jmp 0x140968137
00968A72  BF 3E 00 00 C0                  mov edi, 0xc000003e
00968A77  E9 AC FB FF FF                  jmp 0x140968628
00968A7C  8B CA                           mov ecx, edx
00968A7E  D3 E0                           shl eax, cl
00968A80  44 0B C8                        or r9d, eax
00968A83  E9 7E FE FF FF                  jmp 0x140968906
00968A88  41 8B C9                        mov ecx, r9d
00968A8B  41 8B C1                        mov eax, r9d
00968A8E  C1 E9 18                        shr ecx, 0x18
00968A91  C1 E0 08                        shl eax, 8
00968A94  44 8B C9                        mov r9d, ecx
00968A97  44 0B C8                        or r9d, eax
00968A9A  41 8B C1                        mov eax, r9d
00968A9D  EB 98                           jmp 0x140968a37
00968A9F  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00968AA3  EB A2                           jmp 0x140968a47
00968AA5  45 33 ED                        xor r13d, r13d
00968AA8  41 83 FE 04                     cmp r14d, 4
00968AAC  73 B0                           jae 0x140968a5e
00968AAE  B9 04 00 00 00                  mov ecx, 4
00968AB3  41 2B CE                        sub ecx, r14d
00968AB6  C1 E1 03                        shl ecx, 3
00968AB9  41 D3 EF                        shr r15d, cl
00968ABC  41 D3 E7                        shl r15d, cl
00968ABF  EB 9D                           jmp 0x140968a5e
00968AC1  44 89 7B 20                     mov dword ptr [rbx + 0x20], r15d
00968AC5  4C 89 7B 28                     mov qword ptr [rbx + 0x28], r15
00968AC9  E9 62 F5 FF FF                  jmp 0x140968030
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00967F18(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14)
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
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p70;

    result = (unsigned int)(((unsigned int)(a2)) - ((unsigned int)(a3 + 4)));
    if (((unsigned int)(result)) < ((unsigned int)(v_rsi))) goto loc_009686C8;
    if (a2 != ((unsigned int)(v_rsi + a3 + 4 * 1))) goto loc_009686C8;
    a1 = (unsigned int)((v_rsi + v_r14 * 1) + ((unsigned int)(v_r13)));
    a1 = (a1) + (12);
    if (a1 != ((unsigned int)(a2))) goto loc_009686C8;
    result = ExAllocatePool2(256, 48, (unsigned int)(0x20534C53ULL), a4);
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    v_rdi = 0;
    result = (*(unsigned __int64 *)(v_rbp - 72)) + (4);
    if (condition_is_not_equal) goto loc_00968677;
    *(unsigned int *)(result) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
loc_00967FA2:
    if (v_r15 == 0) goto loc_009686BB;
    *(unsigned int *)(result + 16) = (unsigned int)(v_r14);
    result = ExAllocatePool2(256, v_r14, (unsigned int)(0x20534C53ULL), a4);
    *(unsigned __int64 *)(result + 24) = result;
    v_rdi = 0;
    result = memcpy(result, v_r15, v_r14, a4);
    v_r15 = 0;
loc_00967FEB:
    if (v_r12 == 0) goto loc_00968AC1;
    *(unsigned int *)(result + 32) = (unsigned int)(v_rsi);
    if ((unsigned int)(v_rsi) == 0) goto loc_00968A72;
    result = ExAllocatePool2(256, v_rsi, (unsigned int)(0x20534C53ULL), a4);
    if (result == 0) goto loc_00968623;
    *(unsigned __int64 *)(result + 40) = result;
    result = memcpy(result, v_r12, v_rsi, a4);
loc_00968030:
    if (sign_flag) goto loc_00968869;
    v_stack_p70 = result;
    *(unsigned __int64 *)(v_rbp + 8) = *(unsigned __int64 *)(result + 8);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 32)))) != 8) goto loc_00968851;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))) != 160) goto loc_00968851;
    if (((unsigned int)(*(unsigned int *)(result))) <= 8) goto loc_00968851;
    *(unsigned __int64 *)(v_rbp - 16) = (unsigned int)(*(unsigned int *)(result)) - 8;
    v_rdi = 0;
    result = ExAllocatePool2((unsigned int)(*(unsigned int *)(result + 16)) + 96, (unsigned int)(*(unsigned int *)(result)) - 8, (unsigned int)(0x20534C53ULL), a4);
    *(unsigned __int64 *)(v_rbp - 40) = result;
    if (result == 0) goto loc_00968851;
    *(unsigned __int64 *)(v_rbp + 272) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 40));
    v_r14 = (unsigned int)((*(unsigned __int64 *)(v_rbp - 16)) & (7));
    *(unsigned __int64 *)(v_rbp - 72) = result;
    *(unsigned __int64 *)(v_rbp - 64) = v_r14;
    if (condition_is_not_equal) goto loc_009688BD;
    *(unsigned int *)(v_rbp - 92) = 0;
    *(unsigned int *)(v_rbp - 120) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_rbp - 88) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rbp - 8) = *(unsigned __int64 *)(result + 24) + 158;
    *(unsigned __int64 *)(v_rbp + 24) = *(unsigned __int64 *)(result + 24) + 126;
    v_stack_p70 = a14;
loc_00968137:
    a1 = (*(unsigned __int64 *)(v_rbp - 16)) >> (3);
    *(unsigned __int64 *)(v_rbp - 64) = a1;
    if (a1 == 0) goto loc_009685BC;
    result = (result) + (7);
    *(unsigned __int64 *)(v_rbp - 48) = result;
loc_00968160:
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 8) + 2 - 2)) << (8));
    a1 = (unsigned int)((a1) | ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 8) + 2 - 1))));
    a2 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 8) + 2 + 2)) << (8));
    a1 = (unsigned int)((a1) << (8));
    a1 = (unsigned int)((a1) | ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 8) + 2))));
    a1 = (unsigned int)((a1) << (8));
    a1 = (unsigned int)((a1) | ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 8) + 2 + 1))));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(a1)));
    *(unsigned int *)(v_rbp - 24) = (unsigned int)(a1);
    a2 = (unsigned int)((a2) | ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 8) + 2 + 3))));
    a2 = (unsigned int)((a2) << (8));
    a2 = (unsigned int)((a2) | ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 8) + 2 + 4))));
    a2 = (unsigned int)((a2) << (8));
    a3 = (*(unsigned __int64 *)(result + 8) + 2) + (8);
    a2 = (unsigned int)((a2) | ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 8) + 2 + 5))));
    *(unsigned __int64 *)(v_rbp + 56) = a3;
    v_r13 = (unsigned int)((0) ^ (a2));
    *(unsigned int *)(v_rbp - 56) = a2;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 276))))) ^ ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)))));
    v_r13 = (unsigned int)((v_r13) ^ ((unsigned int)(result)));
    v_r13 = (unsigned int)((v_r13) ^ ((unsigned int)(v_r15)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) ^ ((unsigned int)(*(unsigned __int16 *)(v_rbp + 274))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) >> (8));
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp + 276))))));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(a1)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 276))))) - ((unsigned int)(v_r15)));
    a1 = (unsigned int)((a1) * ((unsigned int)(*(unsigned __int16 *)(v_rbp + 274))));
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)((unsigned int)(v_r15)))));
    v_r13 = (unsigned int)((v_r13) ^ ((unsigned int)(a1)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 276))) ^ ((unsigned int)(v_r13)));
    a2 = (unsigned int)((a2) * ((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40))))));
    a2 = (unsigned int)((a2) - ((unsigned int)((unsigned int)((unsigned int)(v_r13)))));
    v_r15 = (unsigned int)((v_r15) ^ (a2));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) - ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)))));
    a1 = (unsigned int)((a1) * ((unsigned int)(*(unsigned __int16 *)(v_rbp + 278))));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)((unsigned int)(v_r15)))));
    v_r13 = (unsigned int)((v_r13) ^ ((unsigned int)(a1)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40))))) - ((unsigned int)(v_r13)));
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp + 276))))));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)((unsigned int)(v_r13)))));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(a1)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbp + 278)))) ^ ((unsigned int)(v_r15)));
    a1 = (unsigned int)((a1) * ((unsigned int)(*(unsigned __int16 *)(v_rbp + 274))));
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)((unsigned int)(v_r15)))));
    v_r13 = (unsigned int)((v_r13) ^ ((unsigned int)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbp + 274)))) ^ ((unsigned int)(v_r13)));
    result = (unsigned int)((result) * ((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40))))));
    *(unsigned __int64 *)(v_rbp - 72) = 16;
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)((unsigned int)(v_r13)))));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) - ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)))));
    result = (unsigned int)((result) - ((unsigned int)(*(unsigned __int16 *)(v_rbp + 278))));
    v_r13 = (unsigned int)((v_r13) ^ ((unsigned int)(result)));
    v_rbx = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40))) - ((unsigned int)(v_r13)));
    v_rbx = (unsigned int)((v_rbx) * ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp + 276))))));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)((unsigned int)((unsigned int)(v_r13)))));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(v_rbx)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) - ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp + 276))))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) >> (13));
    a1 = (unsigned int)((a1) * ((unsigned int)(*(unsigned __int16 *)(v_rbp + 274))));
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    v_r13 = (unsigned int)((v_r13) ^ ((unsigned int)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp + 276))))));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (29));
    a1 = (unsigned int)((a1) | ((unsigned int)(result * 8)));
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40))))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) >> (15));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(a1)));
loc_009682F0:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 24) + 158 + 1))) >= 31) goto loc_0096839F;
    if ((*(unsigned __int64 *)(v_rip - 9863791 + *(unsigned __int8 *)(*(unsigned __int64 *)(result + 24) + 158 + 1) * 8 + 16614592)) != (v_rip + 532901)) goto loc_009684E0;
    v_r10 = (unsigned int)((30 + 1) & (3));
    a2 = (v_rip + 532901) >> (3);
    a3 = ((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)))) * (a2);
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 24) - 2))) - ((unsigned __int8)(a3)));
    a2 = (unsigned int)(~((unsigned int)((unsigned int)(v_r15))));
    a1 = (unsigned __int8)((a1) + 1);
    a4 = (unsigned int)(((unsigned int)(a2)) >> ((unsigned __int8)(a1)));
    a3 = (unsigned __int8)((a3) - ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 24) - 2))));
    a2 = (unsigned int)((a2) << ((unsigned __int8)(a3 + 31)));
    a4 = (unsigned int)((a4) | (a2));
    a4 = (unsigned int)((a4) + ((unsigned int)(*(unsigned __int16 *)(v_rbp + v_r10 * 2 + 272))));
    a2 = (a2) >> (1);
    a2 = (a2) + (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 24) - 1));
    result = (v_r10 + 1) + (a2);
    result = (unsigned int)((result) & (3));
    a4 = (unsigned int)((a4) * ((unsigned int)(*(unsigned __int16 *)(v_rbp + result * 2 + 272))));
loc_00968398:
    v_r13 = (unsigned int)((v_r13) ^ ((unsigned int)(a4)));
loc_0096839F:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 24) + 158))) >= 31) goto loc_009683F3;
    if ((*(unsigned __int64 *)(v_rip - 9863791 + *(unsigned __int8 *)(*(unsigned __int64 *)(result + 24) + 158) * 8 + 16614592)) != (v_rip + 691867)) goto loc_009684A5;
    a2 = (unsigned int)((30) & (1));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) ^ (*(unsigned int *)(v_rbp + a2 * 4 + 272)));
    a1 = (unsigned int)((a2 - 1) & (1));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + a1 * 4 + 272))) - ((unsigned int)(result)));
loc_009683F0:
    v_r15 = (unsigned int)((v_r15) ^ (a2));
loc_009683F3:
    v_r14 = (30) - (2);
    v_rsi = (*(unsigned __int64 *)(result + 24) + 158) - (2);
    v_rbx = (*(unsigned __int64 *)(v_rbp + 24)) - (8);
    v_r12 = (*(unsigned __int64 *)(v_rbp - 72)) - (1);
    *(unsigned __int64 *)(v_rbp - 72) = v_r12;
    if (condition_is_not_equal) goto loc_009682F0;
    v_r15 = (unsigned int)((v_r15) ^ (*(unsigned int *)(v_rbp - 92)));
    v_r13 = (unsigned int)((v_r13) ^ (*(unsigned int *)(v_rbp - 88)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) >> (8));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 48) - 4) = (unsigned __int8)(v_r15);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 48)) = (unsigned __int8)(v_r13);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) << (24));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) << (24));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 48) - 5) = (unsigned __int8)(a1);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) << (24));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) >> (8));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    a1 = (unsigned int)((a1) >> (8));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 48) - 1) = (unsigned __int8)(a2);
    a3 = (unsigned int)((a3) | ((unsigned int)(a1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 48) - 6) = (unsigned __int8)(a3);
    result = (unsigned int)(((unsigned int)(a2)) << (24));
    a2 = (unsigned int)((a2) >> (8));
    result = (unsigned int)((result) | (a2));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 48) - 2) = (unsigned __int8)(result);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 48) - 7) = (unsigned __int8)(a3);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 48) - 3) = (unsigned __int8)(result);
    v_r11 = (*(unsigned __int64 *)(v_rbp - 48)) + (8);
    *(unsigned int *)(v_rbp - 92) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 24)));
    *(unsigned int *)(v_rbp - 88) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 56)));
    *(unsigned __int64 *)(v_rbp - 48) = v_r11;
    if (condition_is_equal) goto loc_009685B5;
    goto loc_00968160;
loc_009684A5:
    if (((unsigned int)(*(unsigned int *)(v_rbp - 24))) != (v_rip - 2652)) goto loc_00968548;
    result = (unsigned int)((v_r14) & (3));
    result = (v_r14) >> (1);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - ((unsigned int)(*(unsigned __int16 *)(v_rbp + result * 2 + 272))));
    result = (result) - 1;
    result = (unsigned int)((result) & (1));
    a2 = (unsigned int)((a2) ^ (*(unsigned int *)(v_rbp + result * 4 + 272)));
    goto loc_009683F0;
loc_009684E0:
    v_stack_p30 = (unsigned int)(v_r15);
    if (result != (v_rip - 2423)) goto loc_00968518;
    v_stack_p28 = v_rbp + 272;
    v_stack_p20 = *(unsigned __int16 *)(v_rbp + result * 2 + 272);
    result = sub_00967B70(v_rip - 2652, *(unsigned __int64 *)(v_rbp - 8), v_r12, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 24) - 4));
loc_00968510:
    goto loc_00968398;
loc_00968518:
    if (result != (v_rip - 2351)) goto loc_00968579;
    v_stack_p28 = v_rbp + 272;
    v_stack_p20 = v_rip - 2652;
    result = sub_00967BF0(v_rip - 2652, *(unsigned __int64 *)(v_rbp - 8), v_r12, (unsigned int)((unsigned int)(result)));
    goto loc_00968398;
loc_00968548:
    v_stack_p30 = (unsigned int)(v_r13);
    if (result != (v_rip - 2575)) goto loc_0096859A;
    v_stack_p28 = v_rbp + 272;
    v_stack_p20 = v_rip - 2652;
    result = sub_00967B40(v_r14, *(unsigned __int64 *)(v_rbp - 8), v_r12, (unsigned int)((unsigned int)(result)));
loc_00968572:
    goto loc_009683F0;
loc_00968579:
    v_stack_p28 = v_rbp + 272;
    v_stack_p20 = v_r14;
    result = guard_dispatch_icall(v_rip - 2575, *(unsigned __int64 *)(v_rbp - 8), v_r12, (unsigned int)((unsigned int)(result)));
    goto loc_00968510;
loc_0096859A:
    v_stack_p28 = v_rbp + 272;
    v_stack_p20 = v_rip - 2575;
    result = guard_dispatch_icall(v_r14, *(unsigned __int64 *)(v_rbp - 8), v_r12, (unsigned int)((unsigned int)(result)));
    goto loc_00968572;
loc_009685B5:
    v_rdi = 0;
loc_009685BC:
    v_r15 = 0;
    if (*(unsigned __int64 *)(v_rbp - 16) == 0) goto loc_009685DC;
loc_009685D0:
    v_rdi = (unsigned __int8)((v_rdi) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 40) + 0 * 1)));
    result = (0) + 1;
    if (result < (*(unsigned __int64 *)(v_rbp - 16))) goto loc_009685D0;
loc_009685DC:
    if (((unsigned __int8)(v_rdi)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 16) + *(unsigned __int64 *)(v_rbp + 8) * 1))) goto loc_00968847;
    *(unsigned int *)(v_rbp - 56) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 40))));
    if ((*(unsigned __int64 *)(v_rbp - 40) + 4) >= (*(unsigned __int64 *)(v_rbp - 40))) goto loc_009686D2;
loc_00968613:
loc_00968623:
loc_00968628:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 40)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 8), a2, *(unsigned __int64 *)(v_rbp - 40), *(unsigned __int64 *)(v_rbp - 16));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 8) = 0;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 24) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 24), a2, *(unsigned __int64 *)(v_rbp - 40), *(unsigned __int64 *)(v_rbp - 16));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 24) = 0;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 40) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 40), a2, *(unsigned __int64 *)(v_rbp - 40), *(unsigned __int64 *)(v_rbp - 16));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 40) = 0;
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rbp + 272), a2, *(unsigned __int64 *)(v_rbp - 40), *(unsigned __int64 *)(v_rbp - 16));
    goto loc_00968030;
loc_00968677:
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 24)) = 0;
    result = ExAllocatePool2(256, 0, (unsigned int)(0x20534C53ULL), *(unsigned __int64 *)(v_rbp - 16));
    a2 = (*(unsigned __int64 *)(v_rbp - 72)) + (4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 24) + 8) = result;
    result = memcpy(result, a2, 0, *(unsigned __int64 *)(v_rbp - 16));
    goto loc_00967FA2;
loc_009686BB:
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 24) + 16) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 24) + 24) = 0;
    goto loc_00967FEB;
loc_009686C8:
loc_009686D2:
    if ((a2 + 4) < a2) goto loc_00968613;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)) + 8)) < 8) goto loc_00968613;
    result = (0) - ((unsigned int)(*(unsigned int *)(a2)));
    result = (result) - (a2 + 4);
    result = (result) + ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 16))));
    v_stack_p58 = 0;
    if (a2 + 4 == 0) goto loc_009687AE;
    if (((unsigned int)(*(unsigned int *)(a2)) + a2 + 4 * 1) < (a2 + 4)) goto loc_0096883A;
    v_stack_p58 = *(unsigned __int64 *)(v_rbp - 40);
loc_00968754:
    if ((a2 + 4) >= ((unsigned int)(*(unsigned int *)(a2)) + a2 + 4 * 1)) goto loc_009687A8;
    if ((a2 + 4 + 4) >= (a2 + 4)) goto loc_00968772;
loc_00968762:
loc_00968772:
    v_stack_p58 = *(unsigned __int64 *)(v_rbp - 40);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00968762;
    a3 = ((unsigned int)((unsigned int)(result))) + (a2 + 4);
    if (a3 < (a2 + 4)) goto loc_00968762;
    v_rdi = 0;
    v_r15 = (unsigned int)((0) + 1);
    goto loc_00968754;
loc_009687A8:
loc_009687AE:
    if (0 == 0) goto loc_009687D6;
    result = ExAllocatePool2(256, 0, (unsigned int)(0x20534C53ULL), *(unsigned __int64 *)(v_rbp - 16));
    v_rdi = 0;
loc_009687D6:
    *(unsigned __int64 *)(v_rbp - 104) = result;
    *(unsigned int *)(v_rbp - 108) = 0;
    *(unsigned int *)(v_rbp - 112) = (unsigned int)(v_r15);
    v_stack_p58 = a11;
    v_stack_p70 = a14;
    v_stack_p58 = a11;
    v_stack_p70 = a14;
    v_stack_p58 = a11;
loc_0096883A:
loc_00968847:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(0x20534C53ULL), a2, (unsigned int)(0x20534C53ULL), *(unsigned __int64 *)(v_rbp - 16));
loc_00968851:
loc_00968869:
    if (*(unsigned __int64 *)(a2 + 4 + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a2 + 4 + 8), a2, (unsigned int)(0x20534C53ULL), *(unsigned __int64 *)(v_rbp - 16));
        *(unsigned __int64 *)(a2 + 4 + 8) = a11;
    }
    if (*(unsigned __int64 *)(a2 + 4 + 24) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a2 + 4 + 24), a2, (unsigned int)(0x20534C53ULL), *(unsigned __int64 *)(v_rbp - 16));
        *(unsigned __int64 *)(a2 + 4 + 24) = a11;
    }
    if (*(unsigned __int64 *)(a2 + 4 + 40) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a2 + 4 + 40), a2, (unsigned int)(0x20534C53ULL), *(unsigned __int64 *)(v_rbp - 16));
        *(unsigned __int64 *)(a2 + 4 + 40) = a11;
    }
    a2 = 0;
    result = ExFreePoolWithTag(a2 + 4, a2, (unsigned int)(0x20534C53ULL), *(unsigned __int64 *)(v_rbp - 16));
loc_009688BD:
    a4 = 0;
    v_r10 = 0;
    *(unsigned int *)(v_rbp - 88) = 0;
    a3 = 0;
    *(unsigned int *)(v_rbp - 120) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_rbp - 92) = 0;
    if ((unsigned int)(a11) == 0) goto loc_0096891E;
    v_stack_p70 = a14;
loc_009688EC:
    v_r12 = (a14) + 1;
    if (0 >= 4) goto loc_00968A7C;
    result = (unsigned int)((*(unsigned __int8 *)(a14)) << ((unsigned __int8)(a4 + 56 - 32)));
    v_r10 = (unsigned int)((v_r10) | ((unsigned int)(result)));
loc_00968906:
    a3 = (unsigned int)((a3) + 1);
    a2 = (unsigned int)((a4 + 56) - (8));
    if (((unsigned int)(a3)) < ((unsigned int)(a11))) goto loc_009688EC;
    *(unsigned int *)(v_rbp - 92) = (unsigned int)(v_r10);
    *(unsigned int *)(v_rbp - 88) = 0;
loc_0096891E:
    *(unsigned __int64 *)(v_rbp - 8) = a11 + 158;
    *(unsigned __int64 *)(v_rbp + 24) = a11 + 126;
    *(unsigned __int64 *)(v_rbp - 48) = 16;
loc_0096894A:
    result = *(unsigned __int8 *)(a11 + 158 + 1);
    v_r11 = a14;
    v_r13 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (((unsigned __int8)(*(unsigned __int8 *)(a11 + 158 + 1))) < 31) {
        v_r10 = *(unsigned __int8 *)(a11 + 126 + 1);
        v_r11 = v_rbp + 272;
        result = *(unsigned __int64 *)(v_rip - 9865531 + *(unsigned __int8 *)(a11 + 158 + 1) * 8 + 16614592);
        a1 = 30 + 1;
        a4 = *(unsigned __int8 *)(a11 + 126);
        a3 = *(unsigned __int8 *)(a11 + 126 - 1);
        a2 = *(unsigned __int8 *)(a11 + 126 - 2);
        v_stack_p30 = (unsigned int)(a11);
        v_stack_p28 = v_r11;
        v_stack_p20 = v_r10;
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rbp - 48);
        v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) ^ ((unsigned int)(result)));
    }
    result = *(unsigned __int8 *)(a11 + 158);
    v_r15 = a11;
    if (((unsigned __int8)(*(unsigned __int8 *)(a11 + 158))) < 31) {
        a1 = *(unsigned __int8 *)(a11 + 126 - 3);
        v_r10 = v_rbp + 272;
        result = *(unsigned __int64 *)(v_rip - 9865531 + *(unsigned __int8 *)(a11 + 158) * 8 + 16614592);
        a4 = *(unsigned __int8 *)(a11 + 126 - 4);
        a3 = *(unsigned __int8 *)(a11 + 126 - 5);
        a2 = *(unsigned __int8 *)(a11 + 126 - 6);
        v_stack_p30 = (unsigned int)(v_r13);
        v_stack_p28 = v_r10;
        v_stack_p20 = a1;
        a1 = 30;
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rbp - 48);
        v_r15 = (unsigned int)((a11) ^ ((unsigned int)(result)));
    }
    v_rdi = (30) - (2);
    v_rsi = (a11 + 158) - (2);
    v_rbx = (a11 + 126) - (8);
    a1 = (a1) - (1);
    *(unsigned __int64 *)(v_rbp - 48) = a1;
    if (condition_is_not_equal) goto loc_0096894A;
    v_r15 = (unsigned int)((v_r15) ^ (*(unsigned int *)(v_rbp - 92)));
    v_r10 = 0;
    v_r13 = (unsigned int)((v_r13) ^ (*(unsigned int *)(v_rbp - 88)));
    if ((unsigned int)(*(unsigned __int64 *)(v_rbp - 64)) == 0) goto loc_00968A9F;
loc_00968A18:
    if (0 >= 4) goto loc_00968A88;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15))))) >> (24));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15))))) << (8));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | ((unsigned int)(result)));
loc_00968A37:
    v_r10 = (unsigned int)((v_r10) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp - 72)) = (unsigned __int8)((unsigned int)((unsigned int)(a3)));
    if (((unsigned int)(v_r10)) < ((unsigned int)(*(unsigned __int64 *)(v_rbp - 64)))) goto loc_00968A18;
loc_00968A47:
    if (((unsigned int)(*(unsigned __int64 *)(v_rbp - 64))) <= 4) goto loc_00968AA5;
    a1 = (unsigned int)((8) - ((unsigned int)(*(unsigned __int64 *)(v_rbp - 64))));
    a1 = (unsigned int)((a1) << (3));
    v_r13 = (unsigned int)((v_r13) >> ((unsigned __int8)(a1)));
    v_r13 = (unsigned int)((v_r13) << ((unsigned __int8)(a1)));
loc_00968A5E:
    goto loc_00968137;
loc_00968A72:
    goto loc_00968628;
loc_00968A7C:
    result = (unsigned int)((*(unsigned __int64 *)(v_rbp - 72) + 1) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 72) + 1)))));
    a4 = (unsigned int)((*(unsigned __int64 *)(v_rbp - 16)) | ((unsigned int)(result)));
    goto loc_00968906;
loc_00968A88:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (24));
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) << (8));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | ((unsigned int)(result)));
    goto loc_00968A37;
loc_00968A9F:
    goto loc_00968A47;
loc_00968AA5:
    v_r13 = 0;
    if (((unsigned int)(*(unsigned __int64 *)(v_rbp - 64))) >= 4) goto loc_00968A5E;
    a1 = (unsigned int)((4) - ((unsigned int)(*(unsigned __int64 *)(v_rbp - 64))));
    a1 = (unsigned int)((a1) << (3));
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)(a1)));
    v_r15 = (unsigned int)((v_r15) << ((unsigned __int8)(a1)));
    goto loc_00968A5E;
loc_00968AC1:
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 272) + 32) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 272) + 40) = v_r15;
    goto loc_00968030;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00967F18(int64_t Arg1, int32_t Arg2, void *Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, int64_t Arg11, uint64_t Arg12, int64_t Arg13, int64_t Arg14)
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
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p58;
    uint64_t v_stack_p70;

    result = (uint32_t)(((uint32_t)(Arg2)) - ((uint32_t)(Arg3 + 4)));
    if (((uint32_t)(result)) < ((uint32_t)(local_rsi))) goto loc_009686C8;
    if (Arg2 != ((uint32_t)(local_rsi + Arg3 + 4 * 1))) goto loc_009686C8;
    Arg1 = (uint32_t)((local_rsi + local_r14 * 1) + ((uint32_t)(local_r13)));
    Arg1 = (Arg1) + (12);
    if (Arg1 != ((uint32_t)(Arg2))) goto loc_009686C8;
    result = ExAllocatePool2(256, 48, (uint32_t)(0x20534C53ULL), Arg4);
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    local_rdi = 0;
    result = (*(uint64_t *)(local_rbp - 0x48)) + (4);
    if (condition_is_not_equal) goto loc_00968677;
    *(uint32_t *)(result) = 0;
    *(uint64_t *)(result + 0x8) = 0;
loc_00967FA2:
    if (local_r15 == 0) goto loc_009686BB;
    *(uint32_t *)(result + 0x10) = (uint32_t)(local_r14);
    result = ExAllocatePool2(256, local_r14, (uint32_t)(0x20534C53ULL), Arg4);
    *(uint64_t *)(result + 0x18) = result;
    local_rdi = 0;
    result = memcpy(result, local_r15, local_r14, Arg4);
    local_r15 = 0;
loc_00967FEB:
    if (local_r12 == 0) goto loc_00968AC1;
    *(uint32_t *)(result + 0x20) = (uint32_t)(local_rsi);
    if ((uint32_t)(local_rsi) == 0) goto loc_00968A72;
    result = ExAllocatePool2(256, local_rsi, (uint32_t)(0x20534C53ULL), Arg4);
    if (result == 0) goto loc_00968623;
    *(uint64_t *)(result + 0x28) = result;
    result = memcpy(result, local_r12, local_rsi, Arg4);
loc_00968030:
    if (sign_flag) goto loc_00968869;
    v_stack_p70 = result;
    *(uint64_t *)(local_rbp + 0x8) = *(uint64_t *)(result + 0x8);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)))) != 8) goto loc_00968851;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) != 160) goto loc_00968851;
    if (((uint32_t)(*(uint32_t *)(result))) <= 8) goto loc_00968851;
    *(uint64_t *)(local_rbp - 0x10) = (uint32_t)(*(uint32_t *)(result)) - 8;
    local_rdi = 0;
    result = ExAllocatePool2((uint32_t)(*(uint32_t *)(result + 0x10)) + 96, (uint32_t)(*(uint32_t *)(result)) - 8, (uint32_t)(0x20534C53ULL), Arg4);
    *(uint64_t *)(local_rbp - 0x28) = result;
    if (result == 0) goto loc_00968851;
    *(uint64_t *)(local_rbp + 0x110) = *(uint64_t *)(*(uint64_t *)(result + 0x28));
    local_r14 = (uint32_t)((*(uint64_t *)(local_rbp - 0x10)) & (7));
    *(uint64_t *)(local_rbp - 0x48) = result;
    *(uint64_t *)(local_rbp - 0x40) = local_r14;
    if (condition_is_not_equal) goto loc_009688BD;
    *(uint32_t *)(local_rbp - 0x5C) = 0;
    *(uint32_t *)(local_rbp - 0x78) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(local_rbp - 0x58) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint64_t *)(local_rbp - 0x8) = *(uint64_t *)(result + 0x18) + 158;
    *(uint64_t *)(local_rbp + 0x18) = *(uint64_t *)(result + 0x18) + 126;
    v_stack_p70 = Arg14;
loc_00968137:
    Arg1 = (*(uint64_t *)(local_rbp - 0x10)) >> (3);
    *(uint64_t *)(local_rbp - 0x40) = Arg1;
    if (Arg1 == 0) goto loc_009685BC;
    result = (result) + (7);
    *(uint64_t *)(local_rbp - 0x30) = result;
loc_00968160:
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result + 0x8) + 0x2 - 0x2)) << (8));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8) + 0x2 - 0x1))));
    Arg2 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result + 0x8) + 0x2 + 0x2)) << (8));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8) + 0x2))));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8) + 0x2 + 0x1))));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(local_rbp - 0x18) = (uint32_t)(Arg1);
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8) + 0x2 + 0x3))));
    Arg2 = (uint32_t)((Arg2) << (8));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8) + 0x2 + 0x4))));
    Arg2 = (uint32_t)((Arg2) << (8));
    Arg3 = (*(uint64_t *)(result + 0x8) + 2) + (8);
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8) + 0x2 + 0x5))));
    *(void **)(local_rbp + 0x38) = Arg3;
    local_r13 = (uint32_t)((0) ^ (Arg2));
    *(uint32_t *)(local_rbp - 0x38) = Arg2;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x114))))) ^ ((uint32_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28)))));
    local_r13 = (uint32_t)((local_r13) ^ ((uint32_t)(result)));
    local_r13 = (uint32_t)((local_r13) ^ ((uint32_t)(local_r15)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) ^ ((uint32_t)(*(uint16_t *)(local_rbp + 0x112))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) >> (8));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x114))))));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(Arg1)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x114))))) - ((uint32_t)(local_r15)));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(*(uint16_t *)(local_rbp + 0x112))));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)((uint32_t)(local_r15)))));
    local_r13 = (uint32_t)((local_r13) ^ ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x114))) ^ ((uint32_t)(local_r13)));
    Arg2 = (uint32_t)((Arg2) * ((uint32_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28))))));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)((uint32_t)((uint32_t)(local_r13)))));
    local_r15 = (uint32_t)((local_r15) ^ (Arg2));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) - ((uint32_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28)))));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(*(uint16_t *)(local_rbp + 0x116))));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)((uint32_t)(local_r15)))));
    local_r13 = (uint32_t)((local_r13) ^ ((uint32_t)(Arg1)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28))))) - ((uint32_t)(local_r13)));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x114))))));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)((uint32_t)(local_r13)))));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(Arg1)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbp + 0x116)))) ^ ((uint32_t)(local_r15)));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(*(uint16_t *)(local_rbp + 0x112))));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)((uint32_t)(local_r15)))));
    local_r13 = (uint32_t)((local_r13) ^ ((uint32_t)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbp + 0x112)))) ^ ((uint32_t)(local_r13)));
    result = (uint32_t)((result) * ((uint32_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28))))));
    *(uint64_t *)(local_rbp - 0x48) = 16;
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)((uint32_t)(local_r13)))));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) - ((uint32_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28)))));
    result = (uint32_t)((result) - ((uint32_t)(*(uint16_t *)(local_rbp + 0x116))));
    local_r13 = (uint32_t)((local_r13) ^ ((uint32_t)(result)));
    local_rbx = (uint32_t)((*(uint64_t *)(*(uint64_t *)(result + 0x28))) - ((uint32_t)(local_r13)));
    local_rbx = (uint32_t)((local_rbx) * ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x114))))));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)((uint32_t)((uint32_t)(local_r13)))));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(local_rbx)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) - ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x114))))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) >> (13));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(*(uint16_t *)(local_rbp + 0x112))));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    local_r13 = (uint32_t)((local_r13) ^ ((uint32_t)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x114))))));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (29));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result * 8)));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28))))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) >> (15));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(Arg1)));
loc_009682F0:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x18) + 0x9E + 0x1))) >= 31) goto loc_0096839F;
    if ((*(uint64_t *)(v_rip - 0x96826F + *(uint8_t *)(*(uint64_t *)(result + 0x18) + 0x9E + 0x1) * 8 + 0xFD84C0)) != (v_rip + 532901)) goto loc_009684E0;
    local_r10 = (uint32_t)((30 + 1) & (3));
    Arg2 = (v_rip + 532901) >> (3);
    Arg3 = ((uint16_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28)))) * (Arg2);
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp + 0x18) - 0x2))) - ((uint8_t)(Arg3)));
    Arg2 = (uint32_t)(~((uint32_t)((uint32_t)(local_r15))));
    Arg1 = (uint8_t)((Arg1) + 1);
    Arg4 = (uint32_t)(((uint32_t)(Arg2)) >> ((uint8_t)(Arg1)));
    Arg3 = (uint8_t)((Arg3) - ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp + 0x18) - 0x2))));
    Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg3 + 31)));
    Arg4 = (uint32_t)((Arg4) | (Arg2));
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(*(uint16_t *)(local_rbp + local_r10 * 2 + 0x110))));
    Arg2 = (Arg2) >> (1);
    Arg2 = (Arg2) + (*(uint8_t *)(*(uint64_t *)(local_rbp + 0x18) - 0x1));
    result = (local_r10 + 1) + (Arg2);
    result = (uint32_t)((result) & (3));
    Arg4 = (uint32_t)((Arg4) * ((uint32_t)(*(uint16_t *)(local_rbp + result * 2 + 0x110))));
loc_00968398:
    local_r13 = (uint32_t)((local_r13) ^ ((uint32_t)(Arg4)));
loc_0096839F:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x18) + 0x9E))) >= 31) goto loc_009683F3;
    if ((*(uint64_t *)(v_rip - 0x96826F + *(uint8_t *)(*(uint64_t *)(result + 0x18) + 0x9E) * 8 + 0xFD84C0)) != (v_rip + 691867)) goto loc_009684A5;
    Arg2 = (uint32_t)((30) & (1));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) ^ (*(uint32_t *)(local_rbp + Arg2 * 4 + 0x110)));
    Arg1 = (uint32_t)((Arg2 - 1) & (1));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + Arg1 * 4 + 0x110))) - ((uint32_t)(result)));
loc_009683F0:
    local_r15 = (uint32_t)((local_r15) ^ (Arg2));
loc_009683F3:
    local_r14 = (30) - (2);
    local_rsi = (*(uint64_t *)(result + 0x18) + 158) - (2);
    local_rbx = (*(uint64_t *)(local_rbp + 0x18)) - (8);
    local_r12 = (*(uint64_t *)(local_rbp - 0x48)) - (1);
    *(uint64_t *)(local_rbp - 0x48) = local_r12;
    if (condition_is_not_equal) goto loc_009682F0;
    local_r15 = (uint32_t)((local_r15) ^ (*(uint32_t *)(local_rbp - 0x5C)));
    local_r13 = (uint32_t)((local_r13) ^ (*(uint32_t *)(local_rbp - 0x58)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) >> (8));
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x30) - 0x4) = (uint8_t)(local_r15);
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x30)) = (uint8_t)(local_r13);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) << (24));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) << (24));
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x30) - 0x5) = (uint8_t)(Arg1);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) << (24));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) >> (8));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) >> (8));
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x30) - 0x1) = (uint8_t)(Arg2);
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg1)));
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x30) - 0x6) = (uint8_t)(Arg3);
    result = (uint32_t)(((uint32_t)(Arg2)) << (24));
    Arg2 = (uint32_t)((Arg2) >> (8));
    result = (uint32_t)((result) | (Arg2));
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x30) - 0x2) = (uint8_t)(result);
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x30) - 0x7) = (uint8_t)(Arg3);
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x30) - 0x3) = (uint8_t)(result);
    local_r11 = (*(uint64_t *)(local_rbp - 0x30)) + (8);
    *(uint32_t *)(local_rbp - 0x5C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x18)));
    *(uint32_t *)(local_rbp - 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x38)));
    *(uint64_t *)(local_rbp - 0x30) = local_r11;
    if (condition_is_equal) goto loc_009685B5;
    goto loc_00968160;
loc_009684A5:
    if (((uint32_t)(*(uint32_t *)(local_rbp - 0x18))) != (v_rip - 2652)) goto loc_00968548;
    result = (uint32_t)((local_r14) & (3));
    result = (local_r14) >> (1);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - ((uint32_t)(*(uint16_t *)(local_rbp + result * 2 + 0x110))));
    result = (result) - 1;
    result = (uint32_t)((result) & (1));
    Arg2 = (uint32_t)((Arg2) ^ (*(uint32_t *)(local_rbp + result * 4 + 0x110)));
    goto loc_009683F0;
loc_009684E0:
    v_stack_p30 = (uint32_t)(local_r15);
    if (result != (v_rip - 2423)) goto loc_00968518;
    v_stack_p28 = local_rbp + 272;
    v_stack_p20 = *(uint16_t *)(local_rbp + result * 2 + 0x110);
    result = sub_00967B70(v_rip - 2652, *(uint64_t *)(local_rbp - 0x8), local_r12, *(uint8_t *)(*(uint64_t *)(local_rbp + 0x18) - 0x4));
loc_00968510:
    goto loc_00968398;
loc_00968518:
    if (result != (v_rip - 2351)) goto loc_00968579;
    v_stack_p28 = local_rbp + 272;
    v_stack_p20 = v_rip - 2652;
    result = sub_00967BF0(v_rip - 2652, *(uint64_t *)(local_rbp - 0x8), local_r12, (uint32_t)((uint32_t)(result)));
    goto loc_00968398;
loc_00968548:
    v_stack_p30 = (uint32_t)(local_r13);
    if (result != (v_rip - 2575)) goto loc_0096859A;
    v_stack_p28 = local_rbp + 272;
    v_stack_p20 = v_rip - 2652;
    result = sub_00967B40(local_r14, *(uint64_t *)(local_rbp - 0x8), local_r12, (uint32_t)((uint32_t)(result)));
loc_00968572:
    goto loc_009683F0;
loc_00968579:
    v_stack_p28 = local_rbp + 272;
    v_stack_p20 = local_r14;
    result = guard_dispatch_icall(v_rip - 2575, *(uint64_t *)(local_rbp - 0x8), local_r12, (uint32_t)((uint32_t)(result)));
    goto loc_00968510;
loc_0096859A:
    v_stack_p28 = local_rbp + 272;
    v_stack_p20 = v_rip - 2575;
    result = guard_dispatch_icall(local_r14, *(uint64_t *)(local_rbp - 0x8), local_r12, (uint32_t)((uint32_t)(result)));
    goto loc_00968572;
loc_009685B5:
    local_rdi = 0;
loc_009685BC:
    local_r15 = 0;
    if (*(uint64_t *)(local_rbp - 0x10) == 0) goto loc_009685DC;
loc_009685D0:
    local_rdi = (uint8_t)((local_rdi) ^ (*(uint8_t *)(*(uint64_t *)(local_rbp - 0x28) + 0x0 * 1)));
    result = (0) + 1;
    if (result < (*(uint64_t *)(local_rbp - 0x10))) goto loc_009685D0;
loc_009685DC:
    if (((uint8_t)(local_rdi)) != (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x10) + *(uint64_t *)(local_rbp + 0x8) * 1))) goto loc_00968847;
    *(uint32_t *)(local_rbp - 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x28))));
    if ((*(uint64_t *)(local_rbp - 0x28) + 4) >= (*(uint64_t *)(local_rbp - 0x28))) goto loc_009686D2;
loc_00968613:
loc_00968623:
loc_00968628:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x28)));
    if (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x8), Arg2, *(uint64_t *)(local_rbp - 0x28), *(uint64_t *)(local_rbp - 0x10));
        *(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x8) = 0;
    }
    if (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x18) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x18), Arg2, *(uint64_t *)(local_rbp - 0x28), *(uint64_t *)(local_rbp - 0x10));
        *(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x18) = 0;
    }
    if (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x28) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x28), Arg2, *(uint64_t *)(local_rbp - 0x28), *(uint64_t *)(local_rbp - 0x10));
        *(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x28) = 0;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rbp + 0x110), Arg2, *(uint64_t *)(local_rbp - 0x28), *(uint64_t *)(local_rbp - 0x10));
    goto loc_00968030;
loc_00968677:
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x18)) = 0;
    result = ExAllocatePool2(256, 0, (uint32_t)(0x20534C53ULL), *(uint64_t *)(local_rbp - 0x10));
    Arg2 = (*(uint64_t *)(local_rbp - 0x48)) + (4);
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x18) + 0x8) = result;
    result = memcpy(result, Arg2, 0, *(uint64_t *)(local_rbp - 0x10));
    goto loc_00967FA2;
loc_009686BB:
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x18) + 0x10) = 0;
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x18) + 0x18) = 0;
    goto loc_00967FEB;
loc_009686C8:
loc_009686D2:
    if ((Arg2 + 4) < Arg2) goto loc_00968613;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)) + 8)) < 8) goto loc_00968613;
    result = (0) - ((uint32_t)(*(uint32_t *)(Arg2)));
    result = (result) - (Arg2 + 4);
    result = (result) + ((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x10))));
    v_stack_p58 = 0;
    if (Arg2 + 4 == 0) goto loc_009687AE;
    if (((uint32_t)(*(uint32_t *)(Arg2)) + Arg2 + 4 * 1) < (Arg2 + 4)) goto loc_0096883A;
    v_stack_p58 = *(uint64_t *)(local_rbp - 0x28);
loc_00968754:
    if ((Arg2 + 4) >= ((uint32_t)(*(uint32_t *)(Arg2)) + Arg2 + 4 * 1)) goto loc_009687A8;
    if ((Arg2 + 4 + 4) >= (Arg2 + 4)) goto loc_00968772;
loc_00968762:
loc_00968772:
    v_stack_p58 = *(uint64_t *)(local_rbp - 0x28);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x4))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00968762;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (Arg2 + 4);
    if (Arg3 < (Arg2 + 4)) goto loc_00968762;
    local_rdi = 0;
    local_r15 = (uint32_t)((0) + 1);
    goto loc_00968754;
loc_009687A8:
loc_009687AE:
    if (0 == 0) goto loc_009687D6;
    result = ExAllocatePool2(256, 0, (uint32_t)(0x20534C53ULL), *(uint64_t *)(local_rbp - 0x10));
    local_rdi = 0;
loc_009687D6:
    *(uint64_t *)(local_rbp - 0x68) = result;
    *(uint32_t *)(local_rbp - 0x6C) = 0;
    *(uint32_t *)(local_rbp - 0x70) = (uint32_t)(local_r15);
    v_stack_p58 = Arg11;
    v_stack_p70 = Arg14;
    v_stack_p58 = Arg11;
    v_stack_p70 = Arg14;
    v_stack_p58 = Arg11;
loc_0096883A:
loc_00968847:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(0x20534C53ULL), Arg2, (uint32_t)(0x20534C53ULL), *(uint64_t *)(local_rbp - 0x10));
loc_00968851:
loc_00968869:
    if (*(uint64_t *)(Arg2 + 0x4 + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(Arg2 + 0x4 + 0x8), Arg2, (uint32_t)(0x20534C53ULL), *(uint64_t *)(local_rbp - 0x10));
        *(uint64_t *)(Arg2 + 0x4 + 0x8) = Arg11;
    }
    if (*(uint64_t *)(Arg2 + 0x4 + 0x18) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(Arg2 + 0x4 + 0x18), Arg2, (uint32_t)(0x20534C53ULL), *(uint64_t *)(local_rbp - 0x10));
        *(uint64_t *)(Arg2 + 0x4 + 0x18) = Arg11;
    }
    if (*(uint64_t *)(Arg2 + 0x4 + 0x28) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(Arg2 + 0x4 + 0x28), Arg2, (uint32_t)(0x20534C53ULL), *(uint64_t *)(local_rbp - 0x10));
        *(uint64_t *)(Arg2 + 0x4 + 0x28) = Arg11;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg2 + 4, Arg2, (uint32_t)(0x20534C53ULL), *(uint64_t *)(local_rbp - 0x10));
loc_009688BD:
    Arg4 = 0;
    local_r10 = 0;
    *(uint32_t *)(local_rbp - 0x58) = 0;
    Arg3 = 0;
    *(uint32_t *)(local_rbp - 0x78) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(local_rbp - 0x5C) = 0;
    if ((uint32_t)(Arg11) == 0) goto loc_0096891E;
    v_stack_p70 = Arg14;
loc_009688EC:
    local_r12 = (Arg14) + 1;
    if (0 >= 4) goto loc_00968A7C;
    result = (uint32_t)((*(uint8_t *)(Arg14)) << ((uint8_t)(Arg4 + 56 - 32)));
    local_r10 = (uint32_t)((local_r10) | ((uint32_t)(result)));
loc_00968906:
    Arg3 = (uint32_t)((Arg3) + 1);
    Arg2 = (uint32_t)((Arg4 + 56) - (8));
    if (((uint32_t)(Arg3)) < ((uint32_t)(Arg11))) goto loc_009688EC;
    *(uint32_t *)(local_rbp - 0x5C) = (uint32_t)(local_r10);
    *(uint32_t *)(local_rbp - 0x58) = 0;
loc_0096891E:
    *(uint64_t *)(local_rbp - 0x8) = Arg11 + 158;
    *(uint64_t *)(local_rbp + 0x18) = Arg11 + 126;
    *(uint64_t *)(local_rbp - 0x30) = 16;
loc_0096894A:
    result = *(uint8_t *)(Arg11 + 0x9E + 0x1);
    local_r11 = Arg14;
    local_r13 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (((uint8_t)(*(uint8_t *)(Arg11 + 0x9E + 0x1))) < 31) {
        local_r10 = *(uint8_t *)(Arg11 + 0x7E + 0x1);
        local_r11 = local_rbp + 272;
        result = *(uint64_t *)(v_rip - 0x96893B + *(uint8_t *)(Arg11 + 0x9E + 0x1) * 8 + 0xFD84C0);
        Arg1 = 30 + 1;
        Arg4 = *(uint8_t *)(Arg11 + 0x7E);
        Arg3 = *(uint8_t *)(Arg11 + 0x7E - 0x1);
        Arg2 = *(uint8_t *)(Arg11 + 0x7E - 0x2);
        v_stack_p30 = (uint32_t)(Arg11);
        v_stack_p28 = local_r11;
        v_stack_p20 = local_r10;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(local_rbp - 0x30);
        local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) ^ ((uint32_t)(result)));
    }
    result = *(uint8_t *)(Arg11 + 0x9E);
    local_r15 = Arg11;
    if (((uint8_t)(*(uint8_t *)(Arg11 + 0x9E))) < 31) {
        Arg1 = *(uint8_t *)(Arg11 + 0x7E - 0x3);
        local_r10 = local_rbp + 272;
        result = *(uint64_t *)(v_rip - 0x96893B + *(uint8_t *)(Arg11 + 0x9E) * 8 + 0xFD84C0);
        Arg4 = *(uint8_t *)(Arg11 + 0x7E - 0x4);
        Arg3 = *(uint8_t *)(Arg11 + 0x7E - 0x5);
        Arg2 = *(uint8_t *)(Arg11 + 0x7E - 0x6);
        v_stack_p30 = (uint32_t)(local_r13);
        v_stack_p28 = local_r10;
        v_stack_p20 = Arg1;
        Arg1 = 30;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(local_rbp - 0x30);
        local_r15 = (uint32_t)((Arg11) ^ ((uint32_t)(result)));
    }
    local_rdi = (30) - (2);
    local_rsi = (Arg11 + 158) - (2);
    local_rbx = (Arg11 + 126) - (8);
    Arg1 = (Arg1) - (1);
    *(uint64_t *)(local_rbp - 0x30) = Arg1;
    if (condition_is_not_equal) goto loc_0096894A;
    local_r15 = (uint32_t)((local_r15) ^ (*(uint32_t *)(local_rbp - 0x5C)));
    local_r10 = 0;
    local_r13 = (uint32_t)((local_r13) ^ (*(uint32_t *)(local_rbp - 0x58)));
    if ((uint32_t)(*(uint64_t *)(local_rbp - 0x40)) == 0) goto loc_00968A9F;
loc_00968A18:
    if (0 >= 4) goto loc_00968A88;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15))))) >> (24));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15))))) << (8));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | ((uint32_t)(result)));
loc_00968A37:
    local_r10 = (uint32_t)((local_r10) + 1);
    *(uint8_t *)(*(uint64_t *)(local_rbp - 0x48)) = (uint8_t)((uint32_t)((uint32_t)(Arg3)));
    if (((uint32_t)(local_r10)) < ((uint32_t)(*(uint64_t *)(local_rbp - 0x40)))) goto loc_00968A18;
loc_00968A47:
    if (((uint32_t)(*(uint64_t *)(local_rbp - 0x40))) <= 4) goto loc_00968AA5;
    Arg1 = (uint32_t)((8) - ((uint32_t)(*(uint64_t *)(local_rbp - 0x40))));
    Arg1 = (uint32_t)((Arg1) << (3));
    local_r13 = (uint32_t)((local_r13) >> ((uint8_t)(Arg1)));
    local_r13 = (uint32_t)((local_r13) << ((uint8_t)(Arg1)));
loc_00968A5E:
    goto loc_00968137;
loc_00968A72:
    goto loc_00968628;
loc_00968A7C:
    result = (uint32_t)((*(uint64_t *)(local_rbp - 0x48) + 1) << ((uint8_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x48) + 1)))));
    Arg4 = (uint32_t)((*(uint64_t *)(local_rbp - 0x10)) | ((uint32_t)(result)));
    goto loc_00968906;
loc_00968A88:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) >> (24));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) << (8));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | ((uint32_t)(result)));
    goto loc_00968A37;
loc_00968A9F:
    goto loc_00968A47;
loc_00968AA5:
    local_r13 = 0;
    if (((uint32_t)(*(uint64_t *)(local_rbp - 0x40))) >= 4) goto loc_00968A5E;
    Arg1 = (uint32_t)((4) - ((uint32_t)(*(uint64_t *)(local_rbp - 0x40))));
    Arg1 = (uint32_t)((Arg1) << (3));
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)(Arg1)));
    local_r15 = (uint32_t)((local_r15) << ((uint8_t)(Arg1)));
    goto loc_00968A5E;
loc_00968AC1:
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x20) = (uint32_t)(local_r15);
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x110) + 0x28) = local_r15;
    goto loc_00968030;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00967F18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
