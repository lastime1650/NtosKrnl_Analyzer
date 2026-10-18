# DrvDbSetDriverPackageMappedProperty

- RVA: `0x00834848`–`0x00834DC0` (길이 `1,400` bytes)
- VA: `0x0000000140834848`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D030C`
- 디코드: `368`개 명령, `1,400/1,400` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0083495C` → [DrvDbOpenDriverPackageRegKey](../93/DrvDbOpenDriverPackageRegKey_function_00931014.md) (function, `0x00931014`)
- `0x008349AB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008349E6` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x00834A39` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00834A42` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00834A6C` → [PnpCtxRegSetValue](../99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x00834A7F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00834AF2` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00834B13` → [DrvDbGetDriverPackageSignerScore](../92/DrvDbGetDriverPackageSignerScore_function_0092F428.md) (function, `0x0092F428`)
- `0x00834B4C` → [DrvDbSetRegValueMappedProperty](DrvDbSetRegValueMappedProperty_function_00834DC8.md) (function, `0x00834DC8`)
- `0x00834BD3` → [DrvDbGetDriverPackageSignerName](DrvDbGetDriverPackageSignerName_function_00833E24.md) (function, `0x00833E24`)
- `0x00834BFC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00834C30` → [DrvDbGetDriverPackageSignerName](DrvDbGetDriverPackageSignerName_function_00833E24.md) (function, `0x00833E24`)
- `0x00834C54` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00834C86` → [DrvDbSetDriverPackageMappedProperty](DrvDbSetDriverPackageMappedProperty_function_00834848.md) (function, `0x00834848`)
- `0x00834CA6` → [DrvDbSetRegValueMappedProperty](DrvDbSetRegValueMappedProperty_function_00834DC8.md) (function, `0x00834DC8`)
- `0x00834CBB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00834CCD` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00834CF6` → [DrvDbGetDriverPackageSignerScore](../92/DrvDbGetDriverPackageSignerScore_function_0092F428.md) (function, `0x0092F428`)
- `0x00834D21` → [DrvDbGetDriverPackageSignerName](DrvDbGetDriverPackageSignerName_function_00833E24.md) (function, `0x00833E24`)
- `0x00834D4C` → [DrvDbSetRegValueMappedProperty](DrvDbSetRegValueMappedProperty_function_00834DC8.md) (function, `0x00834DC8`)
- `0x00834D93` → [DrvDbSetDriverPackageMappedProperty](DrvDbSetDriverPackageMappedProperty_function_00834848.md) (function, `0x00834848`)

### Direct callers
- [DrvDbSetDriverPackageMappedProperty](DrvDbSetDriverPackageMappedProperty_function_00834848.md) at `0x00834C86`
- [DrvDbSetDriverPackageMappedProperty](DrvDbSetDriverPackageMappedProperty_function_00834848.md) at `0x00834D93`
- [DrvDbDispatchDriverPackage](../93/DrvDbDispatchDriverPackage_function_009303A0.md) at `0x00930525`

### Static image references
- `0x0083487A` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008349DB` → RVA `0x00B0D9A0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00834A8D` → RVA `0x00B0D9B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00834AA5` → RVA `0x00022AA0` (`.rdata`; read)
- `0x00834AB2` → RVA `0x00022AA8` (`.rdata`; read)
- `0x00834B70` → RVA `0x00011EE0` (`.rdata`; read)
- `0x00834B7D` → RVA `0x00011EE8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x008349AB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00834A39` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00834A42` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00834A7F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00834AF2` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00834BFC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00834C54` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00834CBB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00834CCD` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00834848  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0083484D  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00834852  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00834857  55                              push rbp
00834858  56                              push rsi
00834859  57                              push rdi
0083485A  41 54                           push r12
0083485C  41 55                           push r13
0083485E  41 56                           push r14
00834860  41 57                           push r15
00834862  48 8B EC                        mov rbp, rsp
00834865  48 83 EC 60                     sub rsp, 0x60
00834869  45 33 ED                        xor r13d, r13d
0083486C  49 8B F9                        mov rdi, r9
0083486F  49 8B F0                        mov rsi, r8
00834872  4C 89 6D F0                     mov qword ptr [rbp - 0x10], r13
00834876  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0083487A  4C 8D 0D 7F B7 7C FF            lea r9, [rip - 0x834881]
00834881  44 89 6D E4                     mov dword ptr [rbp - 0x1c], r13d
00834885  45 8B FD                        mov r15d, r13d
00834888  4C 89 6D F8                     mov qword ptr [rbp - 8], r13
0083488C  45 8B C5                        mov r8d, r13d
0083488F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00834893  48 8B DA                        mov rbx, rdx
00834896  4C 8B D1                        mov r10, rcx
00834899  41 83 F8 0C                     cmp r8d, 0xc
0083489D  73 37                           jae 0x1408348d6
0083489F  41 8B C0                        mov eax, r8d
008348A2  49 8B 94 C1 60 A4 E0 00         mov rdx, qword ptr [r9 + rax*8 + 0xe0a460]
008348AA  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008348AD  39 42 10                        cmp dword ptr [rdx + 0x10], eax
008348B0  75 15                           jne 0x1408348c7
008348B2  48 8B 0A                        mov rcx, qword ptr [rdx]
008348B5  48 2B 0F                        sub rcx, qword ptr [rdi]
008348B8  75 08                           jne 0x1408348c2
008348BA  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
008348BE  48 2B 4F 08                     sub rcx, qword ptr [rdi + 8]
008348C2  48 85 C9                        test rcx, rcx
008348C5  74 05                           je 0x1408348cc
008348C7  41 FF C0                        inc r8d
008348CA  EB CD                           jmp 0x140834899
008348CC  BB 22 00 00 C0                  mov ebx, 0xc0000022
008348D1  E9 CF 04 00 00                  jmp 0x140834da5
008348D6  41 8B D5                        mov edx, r13d
008348D9  83 FA 29                        cmp edx, 0x29
008348DC  0F 83 BE 04 00 00               jae 0x140834da0
008348E2  8B C2                           mov eax, edx
008348E4  4D 8D A1 70 C6 00 00            lea r12, [r9 + 0xc670]
008348EB  48 8D 0C 80                     lea rcx, [rax + rax*4]
008348EF  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008348F2  4D 8D 24 CC                     lea r12, [r12 + rcx*8]
008348F6  4D 8B 04 24                     mov r8, qword ptr [r12]
008348FA  41 39 40 10                     cmp dword ptr [r8 + 0x10], eax
008348FE  75 15                           jne 0x140834915
00834900  49 8B 08                        mov rcx, qword ptr [r8]
00834903  48 2B 0F                        sub rcx, qword ptr [rdi]
00834906  75 08                           jne 0x140834910
00834908  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
0083490C  48 2B 4F 08                     sub rcx, qword ptr [rdi + 8]
00834910  48 85 C9                        test rcx, rcx
00834913  74 04                           je 0x140834919
00834915  FF C2                           inc edx
00834917  EB C0                           jmp 0x1408348d9
00834919  4D 85 E4                        test r12, r12
0083491C  0F 84 7E 04 00 00               je 0x140834da0
00834922  44 8B 75 60                     mov r14d, dword ptr [rbp + 0x60]
00834926  45 3B 74 24 08                  cmp r14d, dword ptr [r12 + 8]
0083492B  74 0F                           je 0x14083493c
0083492D  45 85 F6                        test r14d, r14d
00834930  74 0A                           je 0x14083493c
00834932  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00834937  E9 69 04 00 00                  jmp 0x140834da5
0083493C  48 85 F6                        test rsi, rsi
0083493F  75 2E                           jne 0x14083496f
00834941  48 8D 45 F0                     lea rax, [rbp - 0x10]
00834945  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0083494A  45 33 C9                        xor r9d, r9d
0083494D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00834952  44 8D 46 03                     lea r8d, [rsi + 3]
00834956  48 8B D3                        mov rdx, rbx
00834959  49 8B CA                        mov rcx, r10
0083495C  E8 B3 C6 0F 00                  call 0x140931014
00834961  8B D8                           mov ebx, eax
00834963  85 C0                           test eax, eax
00834965  0F 88 55 03 00 00               js 0x140834cc0
0083496B  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0083496F  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
00834974  85 C0                           test eax, eax
00834976  0F 84 0D 01 00 00               je 0x140834a89
0083497C  45 85 F6                        test r14d, r14d
0083497F  74 0F                           je 0x140834990
00834981  39 45 70                        cmp dword ptr [rbp + 0x70], eax
00834984  74 10                           je 0x140834996
00834986  BB 01 00 00 C0                  mov ebx, 0xc0000001
0083498B  E9 30 03 00 00                  jmp 0x140834cc0
00834990  44 39 6D 70                     cmp dword ptr [rbp + 0x70], r13d
00834994  EB EE                           jmp 0x140834984
00834996  B8 30 00 00 00                  mov eax, 0x30
0083499B  41 B8 50 44 44 42               mov r8d, 0x42444450
008349A1  8B D0                           mov edx, eax
008349A3  89 45 E0                        mov dword ptr [rbp - 0x20], eax
008349A6  B9 00 01 00 00                  mov ecx, 0x100
008349AB  E8 40 D7 34 00                  call 0x140b820f0
008349B0  48 8B F8                        mov rdi, rax
008349B3  48 85 C0                        test rax, rax
008349B6  75 0A                           jne 0x1408349c2
008349B8  BB 17 00 00 C0                  mov ebx, 0xc0000017
008349BD  E9 FE 02 00 00                  jmp 0x140834cc0
008349C2  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
008349C6  48 8D 45 E0                     lea rax, [rbp - 0x20]
008349CA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008349CF  4C 8D 4D E8                     lea r9, [rbp - 0x18]
008349D3  48 85 F6                        test rsi, rsi
008349D6  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008349DB  4C 8D 05 BE 8F 2D 00            lea r8, [rip + 0x2d8fbe]
008349E2  48 0F 45 D6                     cmovne rdx, rsi
008349E6  E8 11 F7 15 00                  call 0x1409940fc
008349EB  8B D8                           mov ebx, eax
008349ED  3D 34 00 00 C0                  cmp eax, 0xc0000034
008349F2  75 10                           jne 0x140834a04
008349F4  0F 57 C0                        xorps xmm0, xmm0
008349F7  0F 11 07                        movups xmmword ptr [rdi], xmm0
008349FA  0F 11 47 10                     movups xmmword ptr [rdi + 0x10], xmm0
008349FE  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
00834A02  EB 1E                           jmp 0x140834a22
00834A04  3D 23 00 00 C0                  cmp eax, 0xc0000023
00834A09  75 07                           jne 0x140834a12
00834A0B  BB E5 00 00 C0                  mov ebx, 0xc00000e5
00834A10  EB 68                           jmp 0x140834a7a
00834A12  85 C0                           test eax, eax
00834A14  78 64                           js 0x140834a7a
00834A16  83 7D E8 03                     cmp dword ptr [rbp - 0x18], 3
00834A1A  75 59                           jne 0x140834a75
00834A1C  83 7D E0 30                     cmp dword ptr [rbp - 0x20], 0x30
00834A20  75 53                           jne 0x140834a75
00834A22  41 8B 44 24 1C                  mov eax, dword ptr [r12 + 0x1c]
00834A27  45 8B 44 24 20                  mov r8d, dword ptr [r12 + 0x20]
00834A2C  48 8D 0C 38                     lea rcx, [rax + rdi]
00834A30  45 85 F6                        test r14d, r14d
00834A33  74 0B                           je 0x140834a40
00834A35  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00834A39  E8 02 1E E9 FF                  call 0x1406c6840
00834A3E  EB 07                           jmp 0x140834a47
00834A40  33 D2                           xor edx, edx
00834A42  E8 F9 21 E9 FF                  call 0x1406c6c40
00834A47  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00834A4B  4C 8D 05 4E 8F 2D 00            lea r8, [rip + 0x2d8f4e]
00834A52  48 85 F6                        test rsi, rsi
00834A55  C7 44 24 28 30 00 00 00         mov dword ptr [rsp + 0x28], 0x30
00834A5D  41 B9 03 00 00 00               mov r9d, 3
00834A63  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00834A68  48 0F 45 D6                     cmovne rdx, rsi
00834A6C  E8 1B D1 15 00                  call 0x140991b8c
00834A71  8B D8                           mov ebx, eax
00834A73  EB 05                           jmp 0x140834a7a
00834A75  BB 01 00 00 C0                  mov ebx, 0xc0000001
00834A7A  33 D2                           xor edx, edx
00834A7C  48 8B CF                        mov rcx, rdi
00834A7F  E8 EC DD 34 00                  call 0x140b82870
00834A84  E9 28 02 00 00                  jmp 0x140834cb1
00834A89  83 7F 10 07                     cmp dword ptr [rdi + 0x10], 7
00834A8D  48 8D 15 1C 8F 2D 00            lea rdx, [rip + 0x2d8f1c]
00834A94  44 8B 6D 70                     mov r13d, dword ptr [rbp + 0x70]
00834A98  4C 8B 7D 68                     mov r15, qword ptr [rbp + 0x68]
00834A9C  0F 85 BF 00 00 00               jne 0x140834b61
00834AA2  48 8B 07                        mov rax, qword ptr [rdi]
00834AA5  48 2B 05 F4 DF 7E FF            sub rax, qword ptr [rip - 0x81200c]
00834AAC  75 0B                           jne 0x140834ab9
00834AAE  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00834AB2  48 2B 05 EF DF 7E FF            sub rax, qword ptr [rip - 0x812011]
00834AB9  33 C9                           xor ecx, ecx
00834ABB  48 85 C0                        test rax, rax
00834ABE  0F 85 9F 00 00 00               jne 0x140834b63
00834AC4  41 83 FE 12                     cmp r14d, 0x12
00834AC8  0F 85 95 00 00 00               jne 0x140834b63
00834ACE  41 83 FD 02                     cmp r13d, 2
00834AD2  0F 86 8B 00 00 00               jbe 0x140834b63
00834AD8  4D 85 FF                        test r15, r15
00834ADB  0F 84 82 00 00 00               je 0x140834b63
00834AE1  49 8B C5                        mov rax, r13
00834AE4  48 D1 E8                        shr rax, 1
00834AE7  66 41 39 4C 47 FE               cmp word ptr [r15 + rax*2 - 2], cx
00834AED  75 74                           jne 0x140834b63
00834AEF  49 8B CF                        mov rcx, r15
00834AF2  E8 89 B5 CC FF                  call 0x140500080
00834AF7  33 C9                           xor ecx, ecx
00834AF9  85 C0                           test eax, eax
00834AFB  75 66                           jne 0x140834b63
00834AFD  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
00834B01  4C 8D 4D E4                     lea r9, [rbp - 0x1c]
00834B05  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00834B09  48 85 F6                        test rsi, rsi
00834B0C  48 8B D3                        mov rdx, rbx
00834B0F  4C 0F 45 C6                     cmovne r8, rsi
00834B13  E8 10 A9 0F 00                  call 0x14092f428
00834B18  85 C0                           test eax, eax
00834B1A  0F 88 6B 01 00 00               js 0x140834c8b
00834B20  BB 03 00 00 0D                  mov ebx, 0xd000003
00834B25  39 5D E4                        cmp dword ptr [rbp - 0x1c], ebx
00834B28  0F 85 5D 01 00 00               jne 0x140834c8b
00834B2E  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00834B32  45 33 ED                        xor r13d, r13d
00834B35  48 85 F6                        test rsi, rsi
00834B38  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00834B3D  4D 8B C4                        mov r8, r12
00834B40  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00834B45  48 0F 45 D6                     cmovne rdx, rsi
00834B49  45 33 C9                        xor r9d, r9d
00834B4C  E8 77 02 00 00                  call 0x140834dc8
00834B51  3D 25 02 00 C0                  cmp eax, 0xc0000225
00834B56  41 8B DD                        mov ebx, r13d
00834B59  0F 45 D8                        cmovne ebx, eax
00834B5C  E9 5F 01 00 00                  jmp 0x140834cc0
00834B61  33 C9                           xor ecx, ecx
00834B63  83 7F 10 08                     cmp dword ptr [rdi + 0x10], 8
00834B67  0F 85 1E 01 00 00               jne 0x140834c8b
00834B6D  48 8B 07                        mov rax, qword ptr [rdi]
00834B70  48 2B 05 69 D3 7D FF            sub rax, qword ptr [rip - 0x822c97]
00834B77  75 0B                           jne 0x140834b84
00834B79  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00834B7D  48 2B 05 64 D3 7D FF            sub rax, qword ptr [rip - 0x822c9c]
00834B84  48 85 C0                        test rax, rax
00834B87  0F 85 FE 00 00 00               jne 0x140834c8b
00834B8D  BB 03 00 00 0D                  mov ebx, 0xd000003
00834B92  41 83 FE 07                     cmp r14d, 7
00834B96  0F 85 3B 01 00 00               jne 0x140834cd7
00834B9C  41 83 FD 04                     cmp r13d, 4
00834BA0  0F 85 E5 00 00 00               jne 0x140834c8b
00834BA6  4D 85 FF                        test r15, r15
00834BA9  0F 84 DC 00 00 00               je 0x140834c8b
00834BAF  41 39 1F                        cmp dword ptr [r15], ebx
00834BB2  0F 85 24 01 00 00               jne 0x140834cdc
00834BB8  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
00834BBC  48 8D 45 E0                     lea rax, [rbp - 0x20]
00834BC0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00834BC5  48 85 F6                        test rsi, rsi
00834BC8  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00834BCC  4C 0F 45 C6                     cmovne r8, rsi
00834BD0  45 33 C9                        xor r9d, r9d
00834BD3  E8 4C F2 FF FF                  call 0x140833e24
00834BD8  3D 23 00 00 C0                  cmp eax, 0xc0000023
00834BDD  0F 85 A8 00 00 00               jne 0x140834c8b
00834BE3  83 7D E0 12                     cmp dword ptr [rbp - 0x20], 0x12
00834BE7  0F 85 9E 00 00 00               jne 0x140834c8b
00834BED  41 8D 56 1D                     lea edx, [r14 + 0x1d]
00834BF1  B9 00 01 00 00                  mov ecx, 0x100
00834BF6  41 B8 50 44 44 42               mov r8d, 0x42444450
00834BFC  E8 EF D4 34 00                  call 0x140b820f0
00834C01  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00834C05  48 8B D8                        mov rbx, rax
00834C08  48 85 C0                        test rax, rax
00834C0B  0F 84 A7 FD FF FF               je 0x1408349b8
00834C11  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
00834C15  48 8D 45 E0                     lea rax, [rbp - 0x20]
00834C19  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00834C1E  48 85 F6                        test rsi, rsi
00834C21  4C 8B CB                        mov r9, rbx
00834C24  C7 44 24 20 12 00 00 00         mov dword ptr [rsp + 0x20], 0x12
00834C2C  4C 0F 45 C6                     cmovne r8, rsi
00834C30  E8 EF F1 FF FF                  call 0x140833e24
00834C35  33 D2                           xor edx, edx
00834C37  85 C0                           test eax, eax
00834C39  78 50                           js 0x140834c8b
00834C3B  8B 45 E0                        mov eax, dword ptr [rbp - 0x20]
00834C3E  85 C0                           test eax, eax
00834C40  74 49                           je 0x140834c8b
00834C42  FF C8                           dec eax
00834C44  66 39 14 43                     cmp word ptr [rbx + rax*2], dx
00834C48  75 41                           jne 0x140834c8b
00834C4A  48 8D 15 5F 8D 2D 00            lea rdx, [rip + 0x2d8d5f]
00834C51  48 8B CB                        mov rcx, rbx
00834C54  E8 27 B4 CC FF                  call 0x140500080
00834C59  33 D2                           xor edx, edx
00834C5B  85 C0                           test eax, eax
00834C5D  75 2C                           jne 0x140834c8b
00834C5F  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
00834C63  4C 8D 0D 36 DE 7E FF            lea r9, [rip - 0x8121ca]
00834C6A  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00834C6E  48 85 F6                        test rsi, rsi
00834C71  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00834C75  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00834C7A  4C 0F 45 C6                     cmovne r8, rsi
00834C7E  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00834C82  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
00834C86  E8 BD FB FF FF                  call 0x140834848
00834C8B  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00834C8F  48 85 F6                        test rsi, rsi
00834C92  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00834C97  45 8B CE                        mov r9d, r14d
00834C9A  48 0F 45 D6                     cmovne rdx, rsi
00834C9E  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00834CA3  4D 8B C4                        mov r8, r12
00834CA6  E8 1D 01 00 00                  call 0x140834dc8
00834CAB  4C 8B 7D F8                     mov r15, qword ptr [rbp - 8]
00834CAF  8B D8                           mov ebx, eax
00834CB1  4D 85 FF                        test r15, r15
00834CB4  74 0A                           je 0x140834cc0
00834CB6  33 D2                           xor edx, edx
00834CB8  49 8B CF                        mov rcx, r15
00834CBB  E8 B0 DB 34 00                  call 0x140b82870
00834CC0  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00834CC4  48 85 C9                        test rcx, rcx
00834CC7  0F 84 D8 00 00 00               je 0x140834da5
00834CCD  E8 DE 85 E7 FF                  call 0x1406ad2b0
00834CD2  E9 CE 00 00 00                  jmp 0x140834da5
00834CD7  45 85 F6                        test r14d, r14d
00834CDA  75 AF                           jne 0x140834c8b
00834CDC  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
00834CE0  4C 8D 4D E4                     lea r9, [rbp - 0x1c]
00834CE4  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
00834CE8  48 85 F6                        test rsi, rsi
00834CEB  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00834CEF  48 8B D7                        mov rdx, rdi
00834CF2  4C 0F 45 C6                     cmovne r8, rsi
00834CF6  E8 2D A7 0F 00                  call 0x14092f428
00834CFB  33 D2                           xor edx, edx
00834CFD  85 C0                           test eax, eax
00834CFF  78 8A                           js 0x140834c8b
00834D01  39 5D E4                        cmp dword ptr [rbp - 0x1c], ebx
00834D04  75 85                           jne 0x140834c8b
00834D06  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
00834D0A  48 8D 45 E0                     lea rax, [rbp - 0x20]
00834D0E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00834D13  48 85 F6                        test rsi, rsi
00834D16  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00834D1A  4C 0F 45 C6                     cmovne r8, rsi
00834D1E  45 33 C9                        xor r9d, r9d
00834D21  E8 FE F0 FF FF                  call 0x140833e24
00834D26  3D 25 02 00 C0                  cmp eax, 0xc0000225
00834D2B  0F 85 5A FF FF FF               jne 0x140834c8b
00834D31  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00834D35  48 85 F6                        test rsi, rsi
00834D38  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00834D3D  45 8B CE                        mov r9d, r14d
00834D40  48 0F 45 D6                     cmovne rdx, rsi
00834D44  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00834D49  4D 8B C4                        mov r8, r12
00834D4C  E8 77 00 00 00                  call 0x140834dc8
00834D51  45 33 ED                        xor r13d, r13d
00834D54  8B D8                           mov ebx, eax
00834D56  85 C0                           test eax, eax
00834D58  0F 88 62 FF FF FF               js 0x140834cc0
00834D5E  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
00834D62  48 8D 05 47 8C 2D 00            lea rax, [rip + 0x2d8c47]
00834D69  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00834D6D  4C 8D 0D 2C DD 7E FF            lea r9, [rip - 0x8122d4]
00834D74  48 85 F6                        test rsi, rsi
00834D77  C7 44 24 30 24 00 00 00         mov dword ptr [rsp + 0x30], 0x24
00834D7F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00834D84  48 8B D7                        mov rdx, rdi
00834D87  4C 0F 45 C6                     cmovne r8, rsi
00834D8B  C7 44 24 20 12 00 00 00         mov dword ptr [rsp + 0x20], 0x12
00834D93  E8 B0 FA FF FF                  call 0x140834848
00834D98  41 8B DD                        mov ebx, r13d
00834D9B  E9 20 FF FF FF                  jmp 0x140834cc0
00834DA0  BB 16 00 00 C0                  mov ebx, 0xc0000016
00834DA5  8B C3                           mov eax, ebx
00834DA7  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00834DAF  48 83 C4 60                     add rsp, 0x60
00834DB3  41 5F                           pop r15
00834DB5  41 5E                           pop r14
00834DB7  41 5D                           pop r13
00834DB9  41 5C                           pop r12
00834DBB  5F                              pop rdi
00834DBC  5E                              pop rsi
00834DBD  5D                              pop rbp
00834DBE  C3                              ret
00834DBF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DrvDbSetDriverPackageMappedProperty(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    v_r13 = 0;
    v_stack_m48 = 0;
    v_stack_m50 = 0;
    v_stack_m54 = 0;
    v_stack_m40 = 0;
    v_stack_m58 = 0;
loc_00834899:
    if (0 >= 12) goto loc_008348D6;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8603777 + 0 * 8 + 14722144) + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))))) goto loc_008348C7;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8603777 + 0 * 8 + 14722144))) - (*(unsigned __int64 *)(a4));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8603777 + 0 * 8 + 14722144) + 8);
        a1 = (a1) - (*(unsigned __int64 *)(a4 + 8));
    }
    if (a1 == 0) goto loc_008348CC;
loc_008348C7:
    a3 = (unsigned int)((0) + 1);
    goto loc_00834899;
loc_008348CC:
    goto loc_00834DA5;
loc_008348D6:
loc_008348D9:
    if (0 >= 41) goto loc_00834DA0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8) + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))))) goto loc_00834915;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8))) - (*(unsigned __int64 *)(a4));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8) + 8);
        a1 = (a1) - (*(unsigned __int64 *)(a4 + 8));
    }
    if (a1 == 0) goto loc_00834919;
loc_00834915:
    a2 = (unsigned int)((0) + 1);
    goto loc_008348D9;
loc_00834919:
    if (v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 == 0) goto loc_00834DA0;
    if (((unsigned int)((unsigned int)(a5))) == (*(unsigned int *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 + 8))) goto loc_0083493C;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_0083493C;
    goto loc_00834DA5;
loc_0083493C:
    if (a3 != 0) goto loc_0083496F;
    v_stack_m70 = 0;
    a4 = 0;
    v_stack_m78 = v_stack_m48;
    result = DrvDbOpenDriverPackageRegKey(a1, (unsigned int)(0xC000000DULL), a3 + 3, a4);
    if (sign_flag) goto loc_00834CC0;
loc_0083496F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 + 32))) == 0) goto loc_00834A89;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_00834990;
loc_00834984:
    if (a7 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 + 32))))) goto loc_00834996;
    goto loc_00834CC0;
loc_00834990:
    goto loc_00834984;
loc_00834996:
    v_stack_m58 = 48;
    result = ExAllocatePool2(256, 48, (unsigned int)(0x42444450ULL), a4);
    if (result != 0) goto loc_008349C2;
loc_008349B8:
    goto loc_00834CC0;
loc_008349C2:
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = result;
    a2 = v_stack_m48;
    if (a3 != 0) { a2 = a3; }
    result = PnpCtxRegQueryValue(256, a2, v_rip + 2985918, v_stack_m50);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00834A04;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    goto loc_00834A22;
loc_00834A04:
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00834A12;
    goto loc_00834A7A;
loc_00834A12:
    if (sign_flag) goto loc_00834A7A;
    if (v_stack_m50 != 3) goto loc_00834A75;
    if (v_stack_m58 != 48) goto loc_00834A75;
loc_00834A22:
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_00834A40;
    result = memcpy((unsigned int)(*(unsigned int *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 + 28)) + result * 1, a6, (unsigned int)(*(unsigned int *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 + 32)), v_stack_m50);
    goto loc_00834A47;
loc_00834A40:
    a2 = 0;
    result = memset((unsigned int)(*(unsigned int *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 + 28)) + result * 1, a2, (unsigned int)(*(unsigned int *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 + 32)), v_stack_m50);
loc_00834A47:
    v_stack_m70 = 48;
    v_stack_m78 = result;
    a2 = v_stack_m48;
    if (a3 != 0) { a2 = a3; }
    result = PnpCtxRegSetValue((unsigned int)(*(unsigned int *)(v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 + 28)) + result * 1, a2, v_rip + 2985806, 3);
    goto loc_00834A7A;
loc_00834A75:
loc_00834A7A:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rip + 2985806, 3);
    goto loc_00834CB1;
loc_00834A89:
    if ((*(unsigned int *)(result + 16)) != 7) goto loc_00834B61;
    result = (*(unsigned __int64 *)(result)) - (*(unsigned __int64 *)(v_rip - 8462348));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(result + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8462353));
    }
    a1 = 0;
    if (result != 0) goto loc_00834B63;
    if (((unsigned int)((unsigned int)(a5))) != 18) goto loc_00834B63;
    if (((unsigned int)((unsigned int)(a7))) <= 2) goto loc_00834B63;
    if (a6 == 0) goto loc_00834B63;
    result = ((unsigned int)(a7)) >> (1);
    if ((*(unsigned __int16 *)(a6 + result * 2 - 2)) != 0) goto loc_00834B63;
    result = wcsicmp(a6, v_rip + 2985756, v_rip + 2985806, 3);
    a1 = 0;
    if ((unsigned int)(result) != 0) goto loc_00834B63;
    a3 = v_stack_m48;
    if (a3 != 0) { a3 = a3; }
    result = DrvDbGetDriverPackageSignerScore(v_stack_p8, (unsigned int)(0xC0000001ULL), a3, v_stack_m54);
    if (sign_flag) goto loc_00834C8B;
    if (v_stack_m54 != ((unsigned int)((unsigned int)(0xD000003ULL)))) goto loc_00834C8B;
    v_r13 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    a2 = v_stack_m48;
    if (a3 != 0) { a2 = a3; }
    a4 = 0;
    result = DrvDbSetRegValueMappedProperty(v_stack_p8, a2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, a4);
    v_rbx = 0;
    if (((unsigned int)(result)) != 0xC0000225ULL) { v_rbx = (unsigned int)(result); }
    goto loc_00834CC0;
loc_00834B61:
    a1 = 0;
loc_00834B63:
    if ((*(unsigned int *)(result + 16)) != 8) goto loc_00834C8B;
    result = (*(unsigned __int64 *)(result)) - (*(unsigned __int64 *)(v_rip - 8531095));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(result + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8531100));
    }
    if (result != 0) goto loc_00834C8B;
    if (((unsigned int)((unsigned int)(a5))) != 7) goto loc_00834CD7;
    if (0 != 4) goto loc_00834C8B;
    if (a6 == 0) goto loc_00834C8B;
    if ((*(unsigned int *)(a6)) != ((unsigned int)((unsigned int)(0xD000003ULL)))) goto loc_00834CDC;
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = 0;
    a3 = v_stack_m48;
    if (a3 != 0) { a3 = a3; }
    a4 = 0;
    result = DrvDbGetDriverPackageSignerName(a1, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00834C8B;
    if (v_stack_m58 != 18) goto loc_00834C8B;
    result = ExAllocatePool2(256, (unsigned int)(a5) + 29, (unsigned int)(0x42444450ULL), a4);
    v_stack_m40 = result;
    if (result == 0) goto loc_008349B8;
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = 18;
    a3 = v_stack_m48;
    if (a3 != 0) { a3 = a3; }
    result = DrvDbGetDriverPackageSignerName(256, (unsigned int)(a5) + 29, a3, result);
    a2 = 0;
    if (sign_flag) goto loc_00834C8B;
    if ((unsigned int)((unsigned int)(v_stack_m58)) == 0) goto loc_00834C8B;
    result = (unsigned int)(((unsigned int)(v_stack_m58)) - 1);
    if ((*(unsigned __int16 *)(result + result * 2)) != 0) goto loc_00834C8B;
    result = wcsicmp(result, v_rip + 2985311, a3, result);
    a2 = 0;
    if ((unsigned int)(result) == 0) {
        a3 = v_stack_m48;
        a4 = v_rip - 8462794;
        a1 = v_stack_p8;
        v_stack_m68 = 0;
        v_stack_m70 = 0;
        if (a3 != 0) { a3 = a3; }
        v_stack_m78 = 0;
        a2 = v_stack_p10;
        result = DrvDbSetDriverPackageMappedProperty(a1, a2, a3, a4);
    }
    v_stack_m70 = 0;
    a2 = v_stack_m48;
    if (a3 != 0) { a2 = a3; }
    v_stack_m78 = a6;
    result = DrvDbSetRegValueMappedProperty(a1, a2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
loc_00834CB1:
    if (v_stack_m40 != 0) {
        a2 = 0;
        a1 = v_stack_m40;
        result = ExFreePoolWithTag(a1, a2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    }
    if (v_stack_m48 == 0) goto loc_00834DA5;
    result = ZwClose(v_stack_m48, a2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    goto loc_00834DA5;
loc_00834CD7:
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00834C8B;
loc_00834CDC:
    a3 = v_stack_m48;
    if (a3 != 0) { a3 = a3; }
    result = DrvDbGetDriverPackageSignerScore(v_stack_p8, v_stack_p10, a3, v_stack_m54);
    a2 = 0;
    if (sign_flag) goto loc_00834C8B;
    if (v_stack_m54 != ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00834C8B;
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = 0;
    a3 = v_stack_m48;
    if (a3 != 0) { a3 = a3; }
    a4 = 0;
    result = DrvDbGetDriverPackageSignerName(v_stack_p8, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00834C8B;
    v_stack_m70 = 0;
    a2 = v_stack_m48;
    if (a3 != 0) { a2 = a3; }
    v_stack_m78 = v_stack_m40;
    result = DrvDbSetRegValueMappedProperty(v_stack_p8, a2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    v_r13 = 0;
    if (sign_flag) goto loc_00834CC0;
    v_stack_m68 = 36;
    v_stack_m70 = v_rip + 2985031;
    a3 = v_stack_m48;
    if (a3 != 0) { a3 = a3; }
    v_stack_m78 = 18;
    result = DrvDbSetDriverPackageMappedProperty(v_stack_p8, v_stack_p10, a3, v_rip - 8463060);
    goto loc_00834CC0;
loc_00834DA0:
loc_00834DA5:
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000016ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t DrvDbSetDriverPackageMappedProperty(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    local_r13 = 0;
    v_stack_m48 = 0;
    v_stack_m50 = 0;
    v_stack_m54 = 0;
    v_stack_m40 = 0;
    v_stack_m58 = 0;
loc_00834899:
    if (0 >= 12) goto loc_008348D6;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip - 0x834881 + 0x0 * 8 + 0xE0A460) + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10))))) goto loc_008348C7;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x834881 + 0x0 * 8 + 0xE0A460))) - (*(uint64_t *)(arg4));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x834881 + 0x0 * 8 + 0xE0A460) + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(arg4 + 0x8));
    }
    if (Arg1 == 0) goto loc_008348CC;
loc_008348C7:
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00834899;
loc_008348CC:
    goto loc_00834DA5;
loc_008348D6:
loc_008348D9:
    if (0 >= 41) goto loc_00834DA0;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8) + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10))))) goto loc_00834915;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8))) - (*(uint64_t *)(arg4));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8) + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(arg4 + 0x8));
    }
    if (Arg1 == 0) goto loc_00834919;
loc_00834915:
    Arg2 = (uint32_t)((0) + 1);
    goto loc_008348D9;
loc_00834919:
    if (v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8 == 0) goto loc_00834DA0;
    if (((uint32_t)((uint32_t)(Arg5))) == (*(uint32_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8 + 0x8))) goto loc_0083493C;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_0083493C;
    goto loc_00834DA5;
loc_0083493C:
    if (Arg3 != 0) goto loc_0083496F;
    v_stack_m70 = 0;
    Arg4 = 0;
    v_stack_m78 = v_stack_m48;
    result = DrvDbOpenDriverPackageRegKey(Arg1, (uint32_t)(0xC000000DULL), Arg3 + 3, Arg4);
    if (sign_flag) goto loc_00834CC0;
loc_0083496F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8 + 0x20))) == 0) goto loc_00834A89;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_00834990;
loc_00834984:
    if (Arg7 == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8 + 0x20))))) goto loc_00834996;
    goto loc_00834CC0;
loc_00834990:
    goto loc_00834984;
loc_00834996:
    v_stack_m58 = 48;
    result = ExAllocatePool2(256, 48, (uint32_t)(0x42444450ULL), Arg4);
    if (result != 0) goto loc_008349C2;
loc_008349B8:
    goto loc_00834CC0;
loc_008349C2:
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = result;
    Arg2 = v_stack_m48;
    if (Arg3 != 0) { Arg2 = Arg3; }
    result = PnpCtxRegQueryValue(256, Arg2, v_rip + 2985918, v_stack_m50);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00834A04;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    goto loc_00834A22;
loc_00834A04:
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00834A12;
    goto loc_00834A7A;
loc_00834A12:
    if (sign_flag) goto loc_00834A7A;
    if (v_stack_m50 != 3) goto loc_00834A75;
    if (v_stack_m58 != 48) goto loc_00834A75;
loc_00834A22:
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_00834A40;
    result = memcpy((uint32_t)(*(uint32_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8 + 0x1C)) + result * 1, Arg6, (uint32_t)(*(uint32_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8 + 0x20)), v_stack_m50);
    goto loc_00834A47;
loc_00834A40:
    Arg2 = 0;
    result = memset((uint32_t)(*(uint32_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8 + 0x1C)) + result * 1, Arg2, (uint32_t)(*(uint32_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8 + 0x20)), v_stack_m50);
loc_00834A47:
    v_stack_m70 = 48;
    v_stack_m78 = result;
    Arg2 = v_stack_m48;
    if (Arg3 != 0) { Arg2 = Arg3; }
    result = PnpCtxRegSetValue((uint32_t)(*(uint32_t *)(v_rip - 0x834881 + 0xC670 + 0x0 + 0x0 * 4 * 8 + 0x1C)) + result * 1, Arg2, v_rip + 2985806, 3);
    goto loc_00834A7A;
loc_00834A75:
loc_00834A7A:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_rip + 2985806, 3);
    goto loc_00834CB1;
loc_00834A89:
    if ((*(uint32_t *)(result + 0x10)) != 7) goto loc_00834B61;
    result = (*(uint64_t *)(result)) - (*(uint64_t *)(v_rip - 0x81200C));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(result + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x812011));
    }
    Arg1 = 0;
    if (result != 0) goto loc_00834B63;
    if (((uint32_t)((uint32_t)(Arg5))) != 18) goto loc_00834B63;
    if (((uint32_t)((uint32_t)(Arg7))) <= 2) goto loc_00834B63;
    if (Arg6 == 0) goto loc_00834B63;
    result = ((uint32_t)(Arg7)) >> (1);
    if ((*(uint16_t *)(Arg6 + result * 2 - 0x2)) != 0) goto loc_00834B63;
    result = wcsicmp(Arg6, v_rip + 2985756, v_rip + 2985806, 3);
    Arg1 = 0;
    if ((uint32_t)(result) != 0) goto loc_00834B63;
    Arg3 = v_stack_m48;
    if (Arg3 != 0) { Arg3 = Arg3; }
    result = DrvDbGetDriverPackageSignerScore(v_stack_p8, (uint32_t)(0xC0000001ULL), Arg3, v_stack_m54);
    if (sign_flag) goto loc_00834C8B;
    if (v_stack_m54 != ((uint32_t)((uint32_t)(0xD000003ULL)))) goto loc_00834C8B;
    local_r13 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    Arg2 = v_stack_m48;
    if (Arg3 != 0) { Arg2 = Arg3; }
    Arg4 = 0;
    result = DrvDbSetRegValueMappedProperty(v_stack_p8, Arg2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, Arg4);
    local_rbx = 0;
    if (((uint32_t)(result)) != 0xC0000225ULL) { local_rbx = (uint32_t)(result); }
    goto loc_00834CC0;
loc_00834B61:
    Arg1 = 0;
loc_00834B63:
    if ((*(uint32_t *)(result + 0x10)) != 8) goto loc_00834C8B;
    result = (*(uint64_t *)(result)) - (*(uint64_t *)(v_rip - 0x822C97));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(result + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x822C9C));
    }
    if (result != 0) goto loc_00834C8B;
    if (((uint32_t)((uint32_t)(Arg5))) != 7) goto loc_00834CD7;
    if (0 != 4) goto loc_00834C8B;
    if (Arg6 == 0) goto loc_00834C8B;
    if ((*(uint32_t *)(Arg6)) != ((uint32_t)((uint32_t)(0xD000003ULL)))) goto loc_00834CDC;
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = 0;
    Arg3 = v_stack_m48;
    if (Arg3 != 0) { Arg3 = Arg3; }
    Arg4 = 0;
    result = DrvDbGetDriverPackageSignerName(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00834C8B;
    if (v_stack_m58 != 18) goto loc_00834C8B;
    result = ExAllocatePool2(256, (uint32_t)(Arg5) + 29, (uint32_t)(0x42444450ULL), Arg4);
    v_stack_m40 = result;
    if (result == 0) goto loc_008349B8;
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = 18;
    Arg3 = v_stack_m48;
    if (Arg3 != 0) { Arg3 = Arg3; }
    result = DrvDbGetDriverPackageSignerName(256, (uint32_t)(Arg5) + 29, Arg3, result);
    Arg2 = 0;
    if (sign_flag) goto loc_00834C8B;
    if ((uint32_t)((uint32_t)(v_stack_m58)) == 0) goto loc_00834C8B;
    result = (uint32_t)(((uint32_t)(v_stack_m58)) - 1);
    if ((*(uint16_t *)(result + result * 2)) != 0) goto loc_00834C8B;
    result = wcsicmp(result, v_rip + 2985311, Arg3, result);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) {
        Arg3 = v_stack_m48;
        Arg4 = v_rip - 8462794;
        Arg1 = v_stack_p8;
        v_stack_m68 = 0;
        v_stack_m70 = 0;
        if (Arg3 != 0) { Arg3 = Arg3; }
        v_stack_m78 = 0;
        Arg2 = v_stack_p10;
        result = DrvDbSetDriverPackageMappedProperty(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = 0;
    Arg2 = v_stack_m48;
    if (Arg3 != 0) { Arg2 = Arg3; }
    v_stack_m78 = Arg6;
    result = DrvDbSetRegValueMappedProperty(Arg1, Arg2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
loc_00834CB1:
    if (v_stack_m40 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m40;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    }
    if (v_stack_m48 == 0) goto loc_00834DA5;
    result = ZwClose(v_stack_m48, Arg2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    goto loc_00834DA5;
loc_00834CD7:
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00834C8B;
loc_00834CDC:
    Arg3 = v_stack_m48;
    if (Arg3 != 0) { Arg3 = Arg3; }
    result = DrvDbGetDriverPackageSignerScore(v_stack_p8, v_stack_p10, Arg3, v_stack_m54);
    Arg2 = 0;
    if (sign_flag) goto loc_00834C8B;
    if (v_stack_m54 != ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00834C8B;
    v_stack_m70 = v_stack_m58;
    v_stack_m78 = 0;
    Arg3 = v_stack_m48;
    if (Arg3 != 0) { Arg3 = Arg3; }
    Arg4 = 0;
    result = DrvDbGetDriverPackageSignerName(v_stack_p8, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00834C8B;
    v_stack_m70 = 0;
    Arg2 = v_stack_m48;
    if (Arg3 != 0) { Arg2 = Arg3; }
    v_stack_m78 = v_stack_m40;
    result = DrvDbSetRegValueMappedProperty(v_stack_p8, Arg2, v_rip - 8603777 + 50800 + 0 + 0 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    local_r13 = 0;
    if (sign_flag) goto loc_00834CC0;
    v_stack_m68 = 36;
    v_stack_m70 = v_rip + 2985031;
    Arg3 = v_stack_m48;
    if (Arg3 != 0) { Arg3 = Arg3; }
    v_stack_m78 = 18;
    result = DrvDbSetDriverPackageMappedProperty(v_stack_p8, v_stack_p10, Arg3, v_rip - 8463060);
    goto loc_00834CC0;
loc_00834DA0:
loc_00834DA5:
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000016ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00834848&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
