# SmProcessConfigRequest

- RVA: `0x007A62E4`–`0x007A6721` (길이 `1,085` bytes)
- VA: `0x00000001407A62E4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D1BF4`
- 디코드: `282`개 명령, `1,085/1,085` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007A6434` → [SmpGetProcessPartition](../../text/4A/SmpGetProcessPartition_function_004A3CCC.md) (function, `0x004A3CCC`)
- `0x007A6460` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007A6479` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007A64B2` → [MmStoreSetTrimPolicy](../../text/69/MmStoreSetTrimPolicy_function_00693544.md) (function, `0x00693544`)
- `0x007A64C7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007A64CF` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007A64D4` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007A64FC` → [PsReferencePartitionByHandle](../90/PsReferencePartitionByHandle_function_0090337C.md) (function, `0x0090337C`)
- `0x007A65B7` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x007A6637` → [SmpGetProcessPartition](../../text/4A/SmpGetProcessPartition_function_004A3CCC.md) (function, `0x004A3CCC`)
- `0x007A665F` → [PsReferencePartitionByHandle](../90/PsReferencePartitionByHandle_function_0090337C.md) (function, `0x0090337C`)
- `0x007A6675` → [SmCreatePartition](../A4/SmCreatePartition_function_00A4BC90.md) (function, `0x00A4BC90`)
- `0x007A66D6` → [SmpSystemStoreCreate](SmpSystemStoreCreate_function_007A8024.md) (function, `0x007A8024`)
- `0x007A66F1` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x007A6714` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007A671A` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [SmSetStoreInformation](../A7/SmSetStoreInformation_function_00A781B8.md) at `0x00A782CE`

### Static image references
- `0x007A654D` → RVA `0x00E37394` (`.data`; write)
- `0x007A6565` → RVA `0x00E67AD8` (`.data`; write)
- `0x007A65B0` → RVA `0x00FD9AD0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x007A6434` → [SmpGetProcessPartition](../../text/4A/SmpGetProcessPartition_function_004A3CCC.md) (`PAGE` → `.text`)
  - `0x007A6460` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007A6479` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007A64B2` → [MmStoreSetTrimPolicy](../../text/69/MmStoreSetTrimPolicy_function_00693544.md) (`PAGE` → `.text`)
  - `0x007A64C7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007A64CF` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007A64D4` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007A6637` → [SmpGetProcessPartition](../../text/4A/SmpGetProcessPartition_function_004A3CCC.md) (`PAGE` → `.text`)
  - `0x007A66F1` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007A62E4  48 8B C4                        mov rax, rsp
007A62E7  48 89 58 08                     mov qword ptr [rax + 8], rbx
007A62EB  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
007A62EF  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
007A62F3  41 54                           push r12
007A62F5  41 56                           push r14
007A62F7  41 57                           push r15
007A62F9  48 83 EC 60                     sub rsp, 0x60
007A62FD  45 8A E0                        mov r12b, r8b
007A6300  4C 8B C9                        mov r9, rcx
007A6303  48 83 60 20 00                  and qword ptr [rax + 0x20], 0
007A6308  0F 57 C0                        xorps xmm0, xmm0
007A630B  0F 11 40 C0                     movups xmmword ptr [rax - 0x40], xmm0
007A630F  0F 11 40 D0                     movups xmmword ptr [rax - 0x30], xmm0
007A6313  83 60 B8 00                     and dword ptr [rax - 0x48], 0
007A6317  83 FA 20                        cmp edx, 0x20
007A631A  73 0A                           jae 0x1407a6326
007A631C  BB 06 02 00 C0                  mov ebx, 0xc0000206
007A6321  E9 BB 03 00 00                  jmp 0x1407a66e1
007A6326  45 84 E4                        test r12b, r12b
007A6329  74 2A                           je 0x1407a6355
007A632B  41 F6 C1 07                     test r9b, 7
007A632F  0F 85 DF 03 00 00               jne 0x1407a6714
007A6335  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
007A633F  49 8B CE                        mov rcx, r14
007A6342  4D 3B CE                        cmp r9, r14
007A6345  49 0F 42 C9                     cmovb rcx, r9
007A6349  8A 01                           mov al, byte ptr [rcx]
007A634B  88 01                           mov byte ptr [rcx], al
007A634D  8A 41 1F                        mov al, byte ptr [rcx + 0x1f]
007A6350  88 41 1F                        mov byte ptr [rcx + 0x1f], al
007A6353  EB 0A                           jmp 0x1407a635f
007A6355  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
007A635F  41 0F 10 01                     movups xmm0, xmmword ptr [r9]
007A6363  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
007A6368  41 0F 10 49 10                  movups xmm1, xmmword ptr [r9 + 0x10]
007A636D  0F 11 4C 24 48                  movups xmmword ptr [rsp + 0x48], xmm1
007A6372  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
007A6377  41 80 F8 09                     cmp r8b, 9
007A637B  74 0A                           je 0x1407a6387
007A637D  BB 59 00 00 C0                  mov ebx, 0xc0000059
007A6382  E9 5A 03 00 00                  jmp 0x1407a66e1
007A6387  83 FA 20                        cmp edx, 0x20
007A638A  74 0A                           je 0x1407a6396
007A638C  BB 04 00 00 C0                  mov ebx, 0xc0000004
007A6391  E9 4B 03 00 00                  jmp 0x1407a66e1
007A6396  41 F7 C0 00 FF FF 00            test r8d, 0xffff00
007A639D  75 46                           jne 0x1407a63e5
007A639F  41 8B D0                        mov edx, r8d
007A63A2  C1 EA 18                        shr edx, 0x18
007A63A5  83 FA 04                        cmp edx, 4
007A63A8  73 3B                           jae 0x1407a63e5
007A63AA  33 C9                           xor ecx, ecx
007A63AC  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
007A63B1  48 85 DB                        test rbx, rbx
007A63B4  0F 94 C1                        sete cl
007A63B7  33 C0                           xor eax, eax
007A63B9  48 39 44 24 50                  cmp qword ptr [rsp + 0x50], rax
007A63BE  0F 94 C0                        sete al
007A63C1  3B C8                           cmp ecx, eax
007A63C3  75 20                           jne 0x1407a63e5
007A63C5  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
007A63CA  48 85 F6                        test rsi, rsi
007A63CD  74 09                           je 0x1407a63d8
007A63CF  85 D2                           test edx, edx
007A63D1  74 05                           je 0x1407a63d8
007A63D3  83 FA 03                        cmp edx, 3
007A63D6  75 0D                           jne 0x1407a63e5
007A63D8  48 85 DB                        test rbx, rbx
007A63DB  74 12                           je 0x1407a63ef
007A63DD  85 D2                           test edx, edx
007A63DF  0F 84 8B 01 00 00               je 0x1407a6570
007A63E5  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007A63EA  E9 F2 02 00 00                  jmp 0x1407a66e1
007A63EF  85 D2                           test edx, edx
007A63F1  0F 84 79 01 00 00               je 0x1407a6570
007A63F7  83 EA 01                        sub edx, 1
007A63FA  0F 84 58 01 00 00               je 0x1407a6558
007A6400  83 EA 01                        sub edx, 1
007A6403  0F 84 21 01 00 00               je 0x1407a652a
007A6409  83 FA 01                        cmp edx, 1
007A640C  0F 85 C9 02 00 00               jne 0x1407a66db
007A6412  49 C1 E8 20                     shr r8, 0x20
007A6416  44 3B C2                        cmp r8d, edx
007A6419  77 CA                           ja 0x1407a63e5
007A641B  48 85 F6                        test rsi, rsi
007A641E  0F 85 BA 00 00 00               jne 0x1407a64de
007A6424  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007A642D  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
007A6434  E8 93 D8 CF FF                  call 0x1404a3ccc
007A6439  48 8B F0                        mov rsi, rax
007A643C  48 8D BE 68 08 00 00            lea rdi, [rsi + 0x868]
007A6443  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007A644C  48 83 CB FF                     or rbx, 0xffffffffffffffff
007A6450  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007A6457  90                              nop
007A6458  45 33 C0                        xor r8d, r8d
007A645B  33 D2                           xor edx, edx
007A645D  48 8B CF                        mov rcx, rdi
007A6460  E8 CB 9D A6 FF                  call 0x140210230
007A6465  4C 8B F0                        mov r14, rax
007A6468  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
007A646E  73 0E                           jae 0x1407a647e
007A6470  4C 8B C7                        mov r8, rdi
007A6473  48 8B D0                        mov rdx, rax
007A6476  48 8B CF                        mov rcx, rdi
007A6479  E8 12 98 A6 FF                  call 0x14020fc90
007A647E  4D 85 F6                        test r14, r14
007A6481  74 05                           je 0x1407a6488
007A6483  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
007A6488  8B 54 24 3C                     mov edx, dword ptr [rsp + 0x3c]
007A648C  8B CA                           mov ecx, edx
007A648E  83 E1 01                        and ecx, 1
007A6491  C1 E1 07                        shl ecx, 7
007A6494  8B 86 58 08 00 00               mov eax, dword ptr [rsi + 0x858]
007A649A  0F BA F0 07                     btr eax, 7
007A649E  0B C8                           or ecx, eax
007A64A0  89 8E 58 08 00 00               mov dword ptr [rsi + 0x858], ecx
007A64A6  F6 C1 01                        test cl, 1
007A64A9  74 0C                           je 0x1407a64b7
007A64AB  48 8B 8E 30 08 00 00            mov rcx, qword ptr [rsi + 0x830]
007A64B2  E8 8D D0 EE FF                  call 0x140693544
007A64B7  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
007A64BC  80 E3 06                        and bl, 6
007A64BF  80 FB 02                        cmp bl, 2
007A64C2  75 08                           jne 0x1407a64cc
007A64C4  48 8B CF                        mov rcx, rdi
007A64C7  E8 04 F9 AB FF                  call 0x140265dd0
007A64CC  48 8B CF                        mov rcx, rdi
007A64CF  E8 2C B1 B3 FF                  call 0x1402e1600
007A64D4  E8 D7 73 AB FF                  call 0x14025d8b0
007A64D9  E9 FD 01 00 00                  jmp 0x1407a66db
007A64DE  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
007A64E6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007A64EB  41 B9 53 6D 43 52               mov r9d, 0x52436d53
007A64F1  45 8A C4                        mov r8b, r12b
007A64F4  BA 02 00 00 00                  mov edx, 2
007A64F9  48 8B CE                        mov rcx, rsi
007A64FC  E8 7B CE 15 00                  call 0x14090337c
007A6501  8B D8                           mov ebx, eax
007A6503  85 C0                           test eax, eax
007A6505  0F 88 D6 01 00 00               js 0x1407a66e1
007A650B  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
007A6513  48 8B 70 18                     mov rsi, qword ptr [rax + 0x18]
007A6517  48 85 F6                        test rsi, rsi
007A651A  0F 85 1C FF FF FF               jne 0x1407a643c
007A6520  BB A9 01 00 C0                  mov ebx, 0xc00001a9
007A6525  E9 B7 01 00 00                  jmp 0x1407a66e1
007A652A  8B 4C 24 3C                     mov ecx, dword ptr [rsp + 0x3c]
007A652E  8D 41 FC                        lea eax, [rcx - 4]
007A6531  83 F8 1C                        cmp eax, 0x1c
007A6534  0F 87 AB FE FF FF               ja 0x1407a63e5
007A653A  85 C9                           test ecx, ecx
007A653C  0F 84 A3 FE FF FF               je 0x1407a63e5
007A6542  8D 41 FF                        lea eax, [rcx - 1]
007A6545  85 C1                           test ecx, eax
007A6547  0F 85 98 FE FF FF               jne 0x1407a63e5
007A654D  89 0D 41 0E 69 00               mov dword ptr [rip + 0x690e41], ecx
007A6553  E9 83 01 00 00                  jmp 0x1407a66db
007A6558  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007A655C  83 F8 01                        cmp eax, 1
007A655F  0F 87 80 FE FF FF               ja 0x1407a63e5
007A6565  89 05 6D 15 6C 00               mov dword ptr [rip + 0x6c156d], eax
007A656B  E9 6B 01 00 00                  jmp 0x1407a66db
007A6570  8B 7C 24 3C                     mov edi, dword ptr [rsp + 0x3c]
007A6574  81 FF 00 20 00 00               cmp edi, 0x2000
007A657A  0F 83 65 FE FF FF               jae 0x1407a63e5
007A6580  44 8B FF                        mov r15d, edi
007A6583  41 D1 EF                        shr r15d, 1
007A6586  41 8B C7                        mov eax, r15d
007A6589  83 E0 03                        and eax, 3
007A658C  83 F8 03                        cmp eax, 3
007A658F  0F 83 50 FE FF FF               jae 0x1407a63e5
007A6595  8B CF                           mov ecx, edi
007A6597  83 E1 18                        and ecx, 0x18
007A659A  83 F9 18                        cmp ecx, 0x18
007A659D  0F 83 42 FE FF FF               jae 0x1407a63e5
007A65A3  83 F8 02                        cmp eax, 2
007A65A6  74 05                           je 0x1407a65ad
007A65A8  83 F9 10                        cmp ecx, 0x10
007A65AB  75 1D                           jne 0x1407a65ca
007A65AD  41 8A D4                        mov dl, r12b
007A65B0  48 8B 0D 19 35 83 00            mov rcx, qword ptr [rip + 0x833519]
007A65B7  E8 64 B8 0C 00                  call 0x140871e20
007A65BC  84 C0                           test al, al
007A65BE  75 0A                           jne 0x1407a65ca
007A65C0  BB 22 00 00 C0                  mov ebx, 0xc0000022
007A65C5  E9 17 01 00 00                  jmp 0x1407a66e1
007A65CA  40 84 FF                        test dil, dil
007A65CD  79 0A                           jns 0x1407a65d9
007A65CF  0F BA E7 08                     bt edi, 8
007A65D3  0F 83 0C FE FF FF               jae 0x1407a63e5
007A65D9  48 85 DB                        test rbx, rbx
007A65DC  74 44                           je 0x1407a6622
007A65DE  48 83 7C 24 50 04               cmp qword ptr [rsp + 0x50], 4
007A65E4  0F 85 FB FD FF FF               jne 0x1407a63e5
007A65EA  45 84 E4                        test r12b, r12b
007A65ED  74 24                           je 0x1407a6613
007A65EF  F6 C3 03                        test bl, 3
007A65F2  0F 85 22 01 00 00               jne 0x1407a671a
007A65F8  49 3B DE                        cmp rbx, r14
007A65FB  49 0F 43 DE                     cmovae rbx, r14
007A65FF  8A 03                           mov al, byte ptr [rbx]
007A6601  88 03                           mov byte ptr [rbx], al
007A6603  8A 43 03                        mov al, byte ptr [rbx + 3]
007A6606  88 43 03                        mov byte ptr [rbx + 3], al
007A6609  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
007A660E  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
007A6613  8B 03                           mov eax, dword ptr [rbx]
007A6615  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007A6619  EB 07                           jmp 0x1407a6622
007A661B  8B D8                           mov ebx, eax
007A661D  E9 BF 00 00 00                  jmp 0x1407a66e1
007A6622  48 85 F6                        test rsi, rsi
007A6625  75 1A                           jne 0x1407a6641
007A6627  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007A6630  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
007A6637  E8 90 D6 CF FF                  call 0x1404a3ccc
007A663C  48 8B D0                        mov rdx, rax
007A663F  EB 43                           jmp 0x1407a6684
007A6641  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
007A6649  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007A664E  41 B9 53 6D 43 52               mov r9d, 0x52436d53
007A6654  45 8A C4                        mov r8b, r12b
007A6657  BA 02 00 00 00                  mov edx, 2
007A665C  48 8B CE                        mov rcx, rsi
007A665F  E8 18 CD 15 00                  call 0x14090337c
007A6664  8B D8                           mov ebx, eax
007A6666  85 C0                           test eax, eax
007A6668  78 77                           js 0x1407a66e1
007A666A  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
007A6672  48 8B CF                        mov rcx, rdi
007A6675  E8 16 56 2A 00                  call 0x140a4bc90
007A667A  8B D8                           mov ebx, eax
007A667C  85 C0                           test eax, eax
007A667E  78 61                           js 0x1407a66e1
007A6680  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
007A6684  8B 8A B0 08 00 00               mov ecx, dword ptr [rdx + 0x8b0]
007A668A  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007A668E  44 8B C0                        mov r8d, eax
007A6691  41 83 E0 01                     and r8d, 1
007A6695  41 C1 E0 04                     shl r8d, 4
007A6699  25 E0 1F 00 00                  and eax, 0x1fe0
007A669E  44 0B C0                        or r8d, eax
007A66A1  45 03 C0                        add r8d, r8d
007A66A4  81 E1 10 C0 FF FF               and ecx, 0xffffc010
007A66AA  44 0B C1                        or r8d, ecx
007A66AD  41 83 E7 0F                     and r15d, 0xf
007A66B1  45 0B C7                        or r8d, r15d
007A66B4  48 83 7C 24 48 00               cmp qword ptr [rsp + 0x48], 0
007A66BA  74 0A                           je 0x1407a66c6
007A66BC  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
007A66C0  89 82 B4 08 00 00               mov dword ptr [rdx + 0x8b4], eax
007A66C6  44 89 82 B0 08 00 00            mov dword ptr [rdx + 0x8b0], r8d
007A66CD  41 F6 C0 03                     test r8b, 3
007A66D1  74 08                           je 0x1407a66db
007A66D3  48 8B CA                        mov rcx, rdx
007A66D6  E8 49 19 00 00                  call 0x1407a8024
007A66DB  33 DB                           xor ebx, ebx
007A66DD  EB 02                           jmp 0x1407a66e1
007A66DF  8B D8                           mov ebx, eax
007A66E1  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
007A66E9  48 85 FF                        test rdi, rdi
007A66EC  74 08                           je 0x1407a66f6
007A66EE  48 8B CF                        mov rcx, rdi
007A66F1  E8 7A C7 B9 FF                  call 0x140342e70
007A66F6  8B C3                           mov eax, ebx
007A66F8  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
007A66FD  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
007A6701  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
007A6705  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
007A6709  49 8B E3                        mov rsp, r11
007A670C  41 5F                           pop r15
007A670E  41 5E                           pop r14
007A6710  41 5C                           pop r12
007A6712  C3                              ret
007A6713  CC                              int3
007A6714  E8 B7 38 0F 00                  call 0x140899fd0
007A6719  90                              nop
007A671A  E8 B1 38 0F 00                  call 0x140899fd0
007A671F  90                              nop
007A6720  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmProcessConfigRequest(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (96);
    *(unsigned __int64 *)(v_rsp - 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 48) = v_xmm0;
    if (a2 >= 32) goto loc_007A6326;
    goto loc_007A66E1;
loc_007A6326:
    if (a3 == 0) goto loc_007A6355;
    if ((((unsigned __int8)(a1)) & (7)) != 0) goto loc_007A6714;
    a1 = v_r14;
    if (a1 < v_r14) { a1 = a1; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(a1 + 31) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 31));
    goto loc_007A635F;
loc_007A6355:
loc_007A635F:
    v_stack_m40 = v_xmm0;
    v_stack_m30 = v_xmm1;
    if (((unsigned __int8)(v_stack_m40)) == 9) goto loc_007A6387;
    goto loc_007A66E1;
loc_007A6387:
    if (a2 == 32) goto loc_007A6396;
    goto loc_007A66E1;
loc_007A6396:
    if ((((unsigned int)(v_stack_m40)) & (0xFFFF00ULL)) != 0) goto loc_007A63E5;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m40))) >> (24));
    if (a2 >= 4) goto loc_007A63E5;
    a1 = 0;
    a1 = (v_stack_m30 == 0) ? 1 : 0;
    result = 0;
    result = (v_stack_m28 == 0) ? 1 : 0;
    if (((unsigned int)(a1)) != ((unsigned int)(result))) goto loc_007A63E5;
    if (v_stack_m38 == 0) goto loc_007A63D8;
    if (a2 == 0) goto loc_007A63D8;
    if (a2 != 3) goto loc_007A63E5;
loc_007A63D8:
    if (v_stack_m30 == 0) goto loc_007A63EF;
    if (a2 == 0) goto loc_007A6570;
loc_007A63E5:
    goto loc_007A66E1;
loc_007A63EF:
    if (a2 == 0) goto loc_007A6570;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_007A6558;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_007A652A;
    if (a2 != 1) goto loc_007A66DB;
    a3 = (v_stack_m40) >> (32);
    if (a3 > a2) goto loc_007A63E5;
    if (v_stack_m38 != 0) goto loc_007A64DE;
    result = SmpGetProcessPartition(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, a3, a1);
loc_007A643C:
    v_rbx = ((unsigned int)(0xC000000DULL)) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 2152, a2, a3, a1);
    if (!(condition_is_above_or_equal)) {
        a3 = result + 2152;
        a2 = result;
        a1 = result + 2152;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a1);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m3C)))) & (1));
    a1 = (unsigned int)((a1) << (7));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(*(unsigned int *)(result + 2136)))));
    *(unsigned int *)(result + 2136) = (unsigned int)(a1);
    result = (unsigned int)(*(unsigned int *)(result + 2136));
    if ((((unsigned __int8)(a1)) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(result + 2096);
        result = MmStoreSetTrimPolicy(a1, (unsigned int)(v_stack_m3C), a3, a1);
    }
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = result + 2152;
        result = ExfTryToWakePushLock(a1, (unsigned int)(v_stack_m3C), a3, a1);
    }
    result = KeAbPostRelease(result + 2152, (unsigned int)(v_stack_m3C), a3, a1);
    result = KeLeaveCriticalRegion(result + 2152, (unsigned int)(v_stack_m3C), a3, a1);
    goto loc_007A66DB;
loc_007A64DE:
    v_stack_m58 = v_stack_p20;
    result = PsReferencePartitionByHandle(result, 2, a3, (unsigned int)(0x52436D53ULL));
    if (sign_flag) goto loc_007A66E1;
    if (*(unsigned __int64 *)(v_stack_p20 + 24) != 0) goto loc_007A643C;
    goto loc_007A66E1;
loc_007A652A:
    if (((unsigned int)((unsigned int)(v_stack_m3C) - 4)) > 28) goto loc_007A63E5;
    if ((unsigned int)((unsigned int)(v_stack_m3C)) == 0) goto loc_007A63E5;
    if ((((unsigned int)((unsigned int)(v_stack_m3C))) & ((unsigned int)((unsigned int)(v_stack_m3C) - 1))) != 0) goto loc_007A63E5;
    *(unsigned int *)(v_rip + 6884929) = (unsigned int)((unsigned int)(v_stack_m3C));
    goto loc_007A66DB;
loc_007A6558:
    if (((unsigned int)((unsigned int)(v_stack_m3C))) > 1) goto loc_007A63E5;
    *(unsigned int *)(v_rip + 7083373) = (unsigned int)((unsigned int)(v_stack_m3C));
    goto loc_007A66DB;
loc_007A6570:
    if (((unsigned int)((unsigned int)(v_stack_m3C))) >= 0x2000ULL) goto loc_007A63E5;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m3C)))) >> (1));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (3));
    if (((unsigned int)(result)) >= 3) goto loc_007A63E5;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m3C)))) & (24));
    if (((unsigned int)(a1)) >= 24) goto loc_007A63E5;
    if (((unsigned int)(result)) == 2) goto loc_007A65AD;
    if (((unsigned int)(a1)) != 16) goto loc_007A65CA;
loc_007A65AD:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 8598809), a3, a3, (unsigned int)(0x52436D53ULL));
    if ((unsigned __int8)(result) != 0) goto loc_007A65CA;
    goto loc_007A66E1;
loc_007A65CA:
    if (!sign_flag) goto loc_007A65D9;
    if (condition_is_above_or_equal) goto loc_007A63E5;
loc_007A65D9:
    if ((unsigned int)(0xC0000022ULL) == 0) goto loc_007A6622;
    if (v_stack_m28 != 4) goto loc_007A63E5;
    if (a3 == 0) goto loc_007A6613;
    if ((((unsigned __int8)((unsigned int)(0xC0000022ULL))) & (3)) != 0) goto loc_007A671A;
    v_rbx = (unsigned int)(0xC0000022ULL);
    if (((unsigned int)(0xC0000022ULL)) >= result) { v_rbx = result; }
    *(unsigned __int8 *)(v_rbx) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx));
    *(unsigned __int8 *)(v_rbx + 3) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 3));
loc_007A6613:
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m30)));
    goto loc_007A6622;
loc_007A6622:
    if (v_stack_m38 != 0) goto loc_007A6641;
    result = SmpGetProcessPartition(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a3, (unsigned int)(0x52436D53ULL));
    goto loc_007A6684;
loc_007A6641:
    v_stack_m58 = v_stack_p20;
    result = PsReferencePartitionByHandle(v_stack_m38, 2, a3, (unsigned int)(0x52436D53ULL));
    if (sign_flag) goto loc_007A66E1;
    result = SmCreatePartition(v_stack_p20, 2, a3, (unsigned int)(0x52436D53ULL));
    if (sign_flag) goto loc_007A66E1;
loc_007A6684:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m3C)))) & (1));
    a3 = (unsigned int)((a3) << (4));
    result = (unsigned int)(((unsigned int)(v_stack_m3C)) & (0x1FE0ULL));
    a3 = (unsigned int)((a3) | ((unsigned int)(result)));
    a3 = (unsigned int)((a3) + (a3));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 24) + 2224))) & (0xFFFFC010ULL));
    a3 = (unsigned int)((a3) | ((unsigned int)(a1)));
    v_r15 = (unsigned int)((v_r15) & (15));
    a3 = (unsigned int)((a3) | ((unsigned int)(v_r15)));
    if (v_stack_m30 != 0) {
        result = v_stack_m48;
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 24) + 2228) = (unsigned int)(result);
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 24) + 2224) = a3;
    if (((a3) & (3)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p20 + 24);
        result = SmpSystemStoreCreate(a1, *(unsigned __int64 *)(v_stack_p20 + 24), a3, (unsigned int)(0x52436D53ULL));
    }
    v_rbx = 0;
    goto loc_007A66E1;
loc_007A66E1:
    if (v_stack_p20 != 0) {
        a1 = v_stack_p20;
        result = PsDereferencePartition(a1, *(unsigned __int64 *)(v_stack_p20 + 24), a3, (unsigned int)(0x52436D53ULL));
    }
    return 0;
loc_007A6714:
    result = ExRaiseDatatypeMisalignment(a1, *(unsigned __int64 *)(v_stack_p20 + 24), a3, (unsigned int)(0x52436D53ULL));
loc_007A671A:
    result = ExRaiseDatatypeMisalignment(a1, *(unsigned __int64 *)(v_stack_p20 + 24), a3, (unsigned int)(0x52436D53ULL));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SmProcessConfigRequest(int64_t Arg1, int32_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (96);
    *(uint64_t *)(local_rsp - 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x30) = v_xmm0;
    if (Arg2 >= 32) goto loc_007A6326;
    goto loc_007A66E1;
loc_007A6326:
    if (Arg3 == 0) goto loc_007A6355;
    if ((((uint8_t)(Arg1)) & (7)) != 0) goto loc_007A6714;
    Arg1 = local_r14;
    if (Arg1 < local_r14) { Arg1 = Arg1; }
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(Arg1 + 0x1F) = (uint8_t)(*(uint8_t *)(Arg1 + 0x1F));
    goto loc_007A635F;
loc_007A6355:
loc_007A635F:
    v_stack_m40 = v_xmm0;
    v_stack_m30 = v_xmm1;
    if (((uint8_t)(v_stack_m40)) == 9) goto loc_007A6387;
    goto loc_007A66E1;
loc_007A6387:
    if (Arg2 == 32) goto loc_007A6396;
    goto loc_007A66E1;
loc_007A6396:
    if ((((uint32_t)(v_stack_m40)) & (0xFFFF00ULL)) != 0) goto loc_007A63E5;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m40))) >> (24));
    if (Arg2 >= 4) goto loc_007A63E5;
    Arg1 = 0;
    Arg1 = (v_stack_m30 == 0) ? 1 : 0;
    result = 0;
    result = (v_stack_m28 == 0) ? 1 : 0;
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) goto loc_007A63E5;
    if (v_stack_m38 == 0) goto loc_007A63D8;
    if (Arg2 == 0) goto loc_007A63D8;
    if (Arg2 != 3) goto loc_007A63E5;
loc_007A63D8:
    if (v_stack_m30 == 0) goto loc_007A63EF;
    if (Arg2 == 0) goto loc_007A6570;
loc_007A63E5:
    goto loc_007A66E1;
loc_007A63EF:
    if (Arg2 == 0) goto loc_007A6570;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_007A6558;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_007A652A;
    if (Arg2 != 1) goto loc_007A66DB;
    Arg3 = (v_stack_m40) >> (32);
    if (Arg3 > Arg2) goto loc_007A63E5;
    if (v_stack_m38 != 0) goto loc_007A64DE;
    result = SmpGetProcessPartition(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, Arg3, Arg1);
loc_007A643C:
    local_rbx = ((uint32_t)(0xC000000DULL)) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 2152, Arg2, Arg3, Arg1);
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 2152;
        Arg2 = result;
        Arg1 = result + 2152;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg1);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m3C)))) & (1));
    Arg1 = (uint32_t)((Arg1) << (7));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x858)))));
    *(uint32_t *)(result + 0x858) = (uint32_t)(Arg1);
    result = (uint32_t)(*(uint32_t *)(result + 0x858));
    if ((((uint8_t)(Arg1)) & (1)) != 0) {
        Arg1 = *(uint64_t *)(result + 0x830);
        result = MmStoreSetTrimPolicy(Arg1, (uint32_t)(v_stack_m3C), Arg3, Arg1);
    }
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = result + 2152;
        result = ExfTryToWakePushLock(Arg1, (uint32_t)(v_stack_m3C), Arg3, Arg1);
    }
    result = KeAbPostRelease(result + 2152, (uint32_t)(v_stack_m3C), Arg3, Arg1);
    result = KeLeaveCriticalRegion(result + 2152, (uint32_t)(v_stack_m3C), Arg3, Arg1);
    goto loc_007A66DB;
loc_007A64DE:
    v_stack_m58 = v_stack_p20;
    result = PsReferencePartitionByHandle(result, 2, Arg3, (uint32_t)(0x52436D53ULL));
    if (sign_flag) goto loc_007A66E1;
    if (*(uint64_t *)(v_stack_p20 + 0x18) != 0) goto loc_007A643C;
    goto loc_007A66E1;
loc_007A652A:
    if (((uint32_t)((uint32_t)(v_stack_m3C) - 4)) > 28) goto loc_007A63E5;
    if ((uint32_t)((uint32_t)(v_stack_m3C)) == 0) goto loc_007A63E5;
    if ((((uint32_t)((uint32_t)(v_stack_m3C))) & ((uint32_t)((uint32_t)(v_stack_m3C) - 1))) != 0) goto loc_007A63E5;
    *(uint32_t *)(v_rip + 0x690E41) = (uint32_t)((uint32_t)(v_stack_m3C));
    goto loc_007A66DB;
loc_007A6558:
    if (((uint32_t)((uint32_t)(v_stack_m3C))) > 1) goto loc_007A63E5;
    *(uint32_t *)(v_rip + 0x6C156D) = (uint32_t)((uint32_t)(v_stack_m3C));
    goto loc_007A66DB;
loc_007A6570:
    if (((uint32_t)((uint32_t)(v_stack_m3C))) >= 0x2000ULL) goto loc_007A63E5;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m3C)))) >> (1));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (3));
    if (((uint32_t)(result)) >= 3) goto loc_007A63E5;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m3C)))) & (24));
    if (((uint32_t)(Arg1)) >= 24) goto loc_007A63E5;
    if (((uint32_t)(result)) == 2) goto loc_007A65AD;
    if (((uint32_t)(Arg1)) != 16) goto loc_007A65CA;
loc_007A65AD:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x833519), Arg3, Arg3, (uint32_t)(0x52436D53ULL));
    if ((uint8_t)(result) != 0) goto loc_007A65CA;
    goto loc_007A66E1;
loc_007A65CA:
    if (!sign_flag) goto loc_007A65D9;
    if (condition_is_above_or_equal) goto loc_007A63E5;
loc_007A65D9:
    if ((uint32_t)(0xC0000022ULL) == 0) goto loc_007A6622;
    if (v_stack_m28 != 4) goto loc_007A63E5;
    if (Arg3 == 0) goto loc_007A6613;
    if ((((uint8_t)((uint32_t)(0xC0000022ULL))) & (3)) != 0) goto loc_007A671A;
    local_rbx = (uint32_t)(0xC0000022ULL);
    if (((uint32_t)(0xC0000022ULL)) >= result) { local_rbx = result; }
    *(uint8_t *)(local_rbx) = (uint8_t)(*(uint8_t *)(local_rbx));
    *(uint8_t *)(local_rbx + 0x3) = (uint8_t)(*(uint8_t *)(local_rbx + 0x3));
loc_007A6613:
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m30)));
    goto loc_007A6622;
loc_007A6622:
    if (v_stack_m38 != 0) goto loc_007A6641;
    result = SmpGetProcessPartition(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg3, (uint32_t)(0x52436D53ULL));
    goto loc_007A6684;
loc_007A6641:
    v_stack_m58 = v_stack_p20;
    result = PsReferencePartitionByHandle(v_stack_m38, 2, Arg3, (uint32_t)(0x52436D53ULL));
    if (sign_flag) goto loc_007A66E1;
    result = SmCreatePartition(v_stack_p20, 2, Arg3, (uint32_t)(0x52436D53ULL));
    if (sign_flag) goto loc_007A66E1;
loc_007A6684:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m3C)))) & (1));
    Arg3 = (uint32_t)((Arg3) << (4));
    result = (uint32_t)(((uint32_t)(v_stack_m3C)) & (0x1FE0ULL));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(result)));
    Arg3 = (uint32_t)((Arg3) + (Arg3));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x18) + 0x8B0))) & (0xFFFFC010ULL));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg1)));
    local_r15 = (uint32_t)((local_r15) & (15));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(local_r15)));
    if (v_stack_m30 != 0) {
        result = v_stack_m48;
        *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x18) + 0x8B4) = (uint32_t)(result);
    }
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x18) + 0x8B0) = Arg3;
    if (((Arg3) & (3)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_p20 + 0x18);
        result = SmpSystemStoreCreate(Arg1, *(uint64_t *)(v_stack_p20 + 0x18), Arg3, (uint32_t)(0x52436D53ULL));
    }
    local_rbx = 0;
    goto loc_007A66E1;
loc_007A66E1:
    if (v_stack_p20 != 0) {
        Arg1 = v_stack_p20;
        result = PsDereferencePartition(Arg1, *(uint64_t *)(v_stack_p20 + 0x18), Arg3, (uint32_t)(0x52436D53ULL));
    }
    return 0;
loc_007A6714:
    result = ExRaiseDatatypeMisalignment(Arg1, *(uint64_t *)(v_stack_p20 + 0x18), Arg3, (uint32_t)(0x52436D53ULL));
loc_007A671A:
    result = ExRaiseDatatypeMisalignment(Arg1, *(uint64_t *)(v_stack_p20 + 0x18), Arg3, (uint32_t)(0x52436D53ULL));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007A62E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
