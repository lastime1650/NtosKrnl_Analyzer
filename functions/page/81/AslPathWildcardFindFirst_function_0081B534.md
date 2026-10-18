# AslPathWildcardFindFirst

- RVA: `0x0081B534`–`0x0081BB25` (길이 `1,521` bytes)
- VA: `0x000000014081B534`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D9D28`
- 디코드: `404`개 명령, `1,521/1,521` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0081B5C9` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x0081B5F0` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081B5FE` → [AslPathCleanUstr](AslPathCleanUstr_function_0081AE0C.md) (function, `0x0081AE0C`)
- `0x0081B626` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081B641` → [RtlUShortAdd](../../text/47/RtlUShortAdd_function_00474F70.md) (function, `0x00474F70`)
- `0x0081B661` → [AslAlloc](../95/AslAlloc_function_0095BD34.md) (function, `0x0095BD34`)
- `0x0081B687` → [RtlStringCbCopyNW](../../text/39/RtlStringCbCopyNW_function_003905E8.md) (function, `0x003905E8`)
- `0x0081B6A7` → [AslpPathWildcardMakeLeaves](AslpPathWildcardMakeLeaves_function_0081C960.md) (function, `0x0081C960`)
- `0x0081B6D4` → [AslDoesFileExistNtPath](AslDoesFileExistNtPath_function_00819BF4.md) (function, `0x00819BF4`)
- `0x0081B6F2` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (function, `0x0026E9A4`)
- `0x0081B71C` → [AslAlloc](../95/AslAlloc_function_0095BD34.md) (function, `0x0095BD34`)
- `0x0081B744` → [wcsncmp](../../text/50/wcsncmp_function_00501CA0.md) (function, `0x00501CA0`)
- `0x0081B7C4` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081B7E2` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081B803` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0081B819` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081B82C` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0081B841` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081B858` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0081B865` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0081B88E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0081B8B0` → [AslpPathWildcardAllocMatchNode](AslpPathWildcardAllocMatchNode_function_0081C620.md) (function, `0x0081C620`)
- `0x0081B8E4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0081B919` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081B97F` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081B99D` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081B9BE` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0081B9D4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081B9E7` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0081B9FC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081BA13` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0081BA20` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0081BA56` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081BA9B` → [AslPathWildcardFindNext](AslPathWildcardFindNext_function_0081BB2C.md) (function, `0x0081BB2C`)
- `0x0081BAC8` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081BAD5` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0081BAE2` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)
- `0x0081BAEF` → [AslpPathWildcardFreeFindContext](AslpPathWildcardFreeFindContext_function_0081C844.md) (function, `0x0081C844`)
- `0x0081BAF8` → [AslpPathWildcardFreeMatchNode](AslpPathWildcardFreeMatchNode_function_0081C918.md) (function, `0x0081C918`)

### Direct callers
- [SdbpCheckMatchingWildcardFiles](SdbpCheckMatchingWildcardFiles_function_00814E30.md) at `0x00814FB6`

### Static image references
- `0x0081B5D7` → RVA `0x0003F178` (`.rdata`; read)
- `0x0081B5E4` → RVA `0x0003F198` (`.rdata`; read)
- `0x0081B609` → RVA `0x0003F1B8` (`.rdata`; read)
- `0x0081B64C` → RVA `0x0003F1D8` (`.rdata`; read)
- `0x0081B692` → RVA `0x0003F1F8` (`.rdata`; read)
- `0x0081B6B5` → RVA `0x0003F218` (`.rdata`; read)
- `0x0081B73A` → RVA `0x0001BAC0` (`.rdata`; read)
- `0x0081B8BF` → RVA `0x0003F270` (`.rdata`; read)
- `0x0081B8FC` → RVA `0x0003E5D0` (`.rdata`; read)
- `0x0081B90D` → RVA `0x0003F158` (`.rdata`; read)
- `0x0081B91E` → RVA `0x0003F240` (`.rdata`; read)
- `0x0081BAAF` → RVA `0x0003F2B8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x0081B641` → [RtlUShortAdd](../../text/47/RtlUShortAdd_function_00474F70.md) (`PAGE` → `.text`)
  - `0x0081B687` → [RtlStringCbCopyNW](../../text/39/RtlStringCbCopyNW_function_003905E8.md) (`PAGE` → `.text`)
  - `0x0081B6F2` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (`PAGE` → `.text`)
  - `0x0081B744` → [wcsncmp](../../text/50/wcsncmp_function_00501CA0.md) (`PAGE` → `.text`)
  - `0x0081B7C4` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081B7E2` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081B803` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0081B819` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081B82C` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0081B841` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081B858` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0081B865` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0081B88E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0081B8E4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0081B97F` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081B99D` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081B9BE` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0081B9D4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081B9E7` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0081B9FC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081BA13` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0081BA20` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0081BA56` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0081B534  48 8B C4                        mov rax, rsp
0081B537  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
0081B53B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0081B53F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0081B543  48 89 48 08                     mov qword ptr [rax + 8], rcx
0081B547  55                              push rbp
0081B548  56                              push rsi
0081B549  57                              push rdi
0081B54A  41 54                           push r12
0081B54C  41 55                           push r13
0081B54E  41 56                           push r14
0081B550  41 57                           push r15
0081B552  48 8B EC                        mov rbp, rsp
0081B555  48 81 EC 80 00 00 00            sub rsp, 0x80
0081B55C  45 33 E4                        xor r12d, r12d
0081B55F  49 8B F9                        mov rdi, r9
0081B562  49 8B F0                        mov rsi, r8
0081B565  4C 8B F1                        mov r14, rcx
0081B568  48 85 C9                        test rcx, rcx
0081B56B  75 0A                           jne 0x14081b577
0081B56D  B8 EF 00 00 C0                  mov eax, 0xc00000ef
0081B572  E9 92 05 00 00                  jmp 0x14081bb09
0081B577  48 85 F6                        test rsi, rsi
0081B57A  0F 84 84 05 00 00               je 0x14081bb04
0081B580  66 45 39 20                     cmp word ptr [r8], r12w
0081B584  0F 84 7A 05 00 00               je 0x14081bb04
0081B58A  48 85 FF                        test rdi, rdi
0081B58D  75 0A                           jne 0x14081b599
0081B58F  B8 F2 00 00 C0                  mov eax, 0xc00000f2
0081B594  E9 70 05 00 00                  jmp 0x14081bb09
0081B599  0F 57 C0                        xorps xmm0, xmm0
0081B59C  66 44 89 21                     mov word ptr [rcx], r12w
0081B5A0  0F 57 C9                        xorps xmm1, xmm1
0081B5A3  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
0081B5A7  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0081B5AB  66 44 89 65 48                  mov word ptr [rbp + 0x48], r12w
0081B5B0  48 8B D6                        mov rdx, rsi
0081B5B3  4D 89 21                        mov qword ptr [r9], r12
0081B5B6  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0081B5BA  4D 8B FC                        mov r15, r12
0081B5BD  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0081B5C1  0F 11 4D E0                     movups xmmword ptr [rbp - 0x20], xmm1
0081B5C5  0F 11 4D F0                     movups xmmword ptr [rbp - 0x10], xmm1
0081B5C9  E8 92 22 1A 00                  call 0x1409bd860
0081B5CE  84 C0                           test al, al
0081B5D0  75 28                           jne 0x14081b5fa
0081B5D2  BB 17 00 00 C0                  mov ebx, 0xc0000017
0081B5D7  4C 8D 0D 9A 3B 82 FF            lea r9, [rip - 0x7dc466]
0081B5DE  41 B8 C2 08 00 00               mov r8d, 0x8c2
0081B5E4  48 8D 15 AD 3B 82 FF            lea rdx, [rip - 0x7dc453]
0081B5EB  B9 01 00 00 00                  mov ecx, 1
0081B5F0  E8 F7 2E 14 00                  call 0x14095e4ec
0081B5F5  E9 D7 04 00 00                  jmp 0x14081bad1
0081B5FA  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0081B5FE  E8 09 F8 FF FF                  call 0x14081ae0c
0081B603  8B D8                           mov ebx, eax
0081B605  85 C0                           test eax, eax
0081B607  79 27                           jns 0x14081b630
0081B609  4C 8D 0D A8 3B 82 FF            lea r9, [rip - 0x7dc458]
0081B610  41 B8 D7 08 00 00               mov r8d, 0x8d7
0081B616  48 8D 15 7B 3B 82 FF            lea rdx, [rip - 0x7dc485]
0081B61D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0081B621  B9 01 00 00 00                  mov ecx, 1
0081B626  E8 C1 2E 14 00                  call 0x14095e4ec
0081B62B  E9 A1 04 00 00                  jmp 0x14081bad1
0081B630  0F B7 4D C0                     movzx ecx, word ptr [rbp - 0x40]
0081B634  4C 8D 45 48                     lea r8, [rbp + 0x48]
0081B638  41 BD 04 00 00 00               mov r13d, 4
0081B63E  41 8B D5                        mov edx, r13d
0081B641  E8 2A 99 C5 FF                  call 0x140474f70
0081B646  8B D8                           mov ebx, eax
0081B648  85 C0                           test eax, eax
0081B64A  79 0F                           jns 0x14081b65b
0081B64C  4C 8D 0D 85 3B 82 FF            lea r9, [rip - 0x7dc47b]
0081B653  41 B8 DD 08 00 00               mov r8d, 0x8dd
0081B659  EB BB                           jmp 0x14081b616
0081B65B  0F B7 5D 48                     movzx ebx, word ptr [rbp + 0x48]
0081B65F  8B D3                           mov edx, ebx
0081B661  E8 CE 06 14 00                  call 0x14095bd34
0081B666  4C 8B F8                        mov r15, rax
0081B669  48 85 C0                        test rax, rax
0081B66C  75 0A                           jne 0x14081b678
0081B66E  BB 17 00 00 C0                  mov ebx, 0xc0000017
0081B673  E9 59 04 00 00                  jmp 0x14081bad1
0081B678  44 0F B7 4D C0                  movzx r9d, word ptr [rbp - 0x40]
0081B67D  48 8B D3                        mov rdx, rbx
0081B680  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
0081B684  49 8B CF                        mov rcx, r15
0081B687  E8 5C 4F B7 FF                  call 0x1403905e8
0081B68C  8B D8                           mov ebx, eax
0081B68E  85 C0                           test eax, eax
0081B690  79 12                           jns 0x14081b6a4
0081B692  4C 8D 0D 5F 3B 82 FF            lea r9, [rip - 0x7dc4a1]
0081B699  41 B8 E9 08 00 00               mov r8d, 0x8e9
0081B69F  E9 72 FF FF FF                  jmp 0x14081b616
0081B6A4  49 8B CF                        mov rcx, r15
0081B6A7  E8 B4 12 00 00                  call 0x14081c960
0081B6AC  85 C0                           test eax, eax
0081B6AE  75 17                           jne 0x14081b6c7
0081B6B0  BB 39 00 00 C0                  mov ebx, 0xc0000039
0081B6B5  4C 8D 0D 5C 3B 82 FF            lea r9, [rip - 0x7dc4a4]
0081B6BC  41 B8 FB 08 00 00               mov r8d, 0x8fb
0081B6C2  E9 1D FF FF FF                  jmp 0x14081b5e4
0081B6C7  83 F8 01                        cmp eax, 1
0081B6CA  75 4B                           jne 0x14081b717
0081B6CC  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0081B6D0  48 83 0F FF                     or qword ptr [rdi], 0xffffffffffffffff
0081B6D4  E8 1B E5 FF FF                  call 0x140819bf4
0081B6D9  85 C0                           test eax, eax
0081B6DB  75 0A                           jne 0x14081b6e7
0081B6DD  BB 06 00 00 80                  mov ebx, 0x80000006
0081B6E2  E9 EA 03 00 00                  jmp 0x14081bad1
0081B6E7  4C 8B C6                        mov r8, rsi
0081B6EA  BA 04 01 00 00                  mov edx, 0x104
0081B6EF  49 8B CE                        mov rcx, r14
0081B6F2  E8 AD 32 A5 FF                  call 0x14026e9a4
0081B6F7  8B D8                           mov ebx, eax
0081B6F9  85 C0                           test eax, eax
0081B6FB  79 12                           jns 0x14081b70f
0081B6FD  4C 8D 0D F4 3A 82 FF            lea r9, [rip - 0x7dc50c]
0081B704  41 B8 0D 09 00 00               mov r8d, 0x90d
0081B70A  E9 07 FF FF FF                  jmp 0x14081b616
0081B70F  41 8B DC                        mov ebx, r12d
0081B712  E9 BA 03 00 00                  jmp 0x14081bad1
0081B717  BA 40 00 00 00                  mov edx, 0x40
0081B71C  E8 13 06 14 00                  call 0x14095bd34
0081B721  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0081B725  48 8B F8                        mov rdi, rax
0081B728  48 85 C0                        test rax, rax
0081B72B  75 0A                           jne 0x14081b737
0081B72D  BB 17 00 00 C0                  mov ebx, 0xc0000017
0081B732  E9 96 03 00 00                  jmp 0x14081bacd
0081B737  4D 8B C5                        mov r8, r13
0081B73A  48 8D 15 7F 03 80 FF            lea rdx, [rip - 0x7ffc81]
0081B741  48 8B CE                        mov rcx, rsi
0081B744  E8 57 65 CE FF                  call 0x140501ca0
0081B749  41 8B CC                        mov ecx, r12d
0081B74C  0F 57 C0                        xorps xmm0, xmm0
0081B74F  85 C0                           test eax, eax
0081B751  BA 20 00 00 00                  mov edx, 0x20
0081B756  BE 0D 00 00 C0                  mov esi, 0xc000000d
0081B75B  0F 95 C1                        setne cl
0081B75E  89 0F                           mov dword ptr [rdi], ecx
0081B760  4C 89 7F 08                     mov qword ptr [rdi + 8], r15
0081B764  4D 8B FC                        mov r15, r12
0081B767  0F 11 47 10                     movups xmmword ptr [rdi + 0x10], xmm0
0081B76B  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
0081B76F  0F 11 47 30                     movups xmmword ptr [rdi + 0x30], xmm0
0081B773  4C 89 67 28                     mov qword ptr [rdi + 0x28], r12
0081B777  48 C7 47 30 10 00 00 00         mov qword ptr [rdi + 0x30], 0x10
0081B77F  4C 89 67 20                     mov qword ptr [rdi + 0x20], r12
0081B783  4C 89 67 38                     mov qword ptr [rdi + 0x38], r12
0081B787  48 89 57 18                     mov qword ptr [rdi + 0x18], rdx
0081B78B  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0081B78F  48 83 F9 08                     cmp rcx, 8
0081B793  72 07                           jb 0x14081b79c
0081B795  8B DE                           mov ebx, esi
0081B797  E9 3A 01 00 00                  jmp 0x14081b8d6
0081B79C  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
0081B7A0  4C 8D 70 FF                     lea r14, [rax - 1]
0081B7A4  48 83 C0 07                     add rax, 7
0081B7A8  48 83 F8 08                     cmp rax, 8
0081B7AC  0F 82 1F 01 00 00               jb 0x14081b8d1
0081B7B2  49 F7 D6                        not r14
0081B7B5  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
0081B7B9  4C 8D 45 B0                     lea r8, [rbp - 0x50]
0081B7BD  4C 89 65 48                     mov qword ptr [rbp + 0x48], r12
0081B7C1  4C 23 F0                        and r14, rax
0081B7C4  E8 B7 CB C2 FF                  call 0x140448380
0081B7C9  85 C0                           test eax, eax
0081B7CB  79 0A                           jns 0x14081b7d7
0081B7CD  BB 95 00 00 C0                  mov ebx, 0xc0000095
0081B7D2  E9 AB 00 00 00                  jmp 0x14081b882
0081B7D7  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0081B7DB  4C 8D 45 48                     lea r8, [rbp + 0x48]
0081B7DF  49 8B CE                        mov rcx, r14
0081B7E2  E8 99 CB C2 FF                  call 0x140448380
0081B7E7  85 C0                           test eax, eax
0081B7E9  78 E2                           js 0x14081b7cd
0081B7EB  4C 8B 6F 38                     mov r13, qword ptr [rdi + 0x38]
0081B7EF  41 B8 52 54 61 72               mov r8d, 0x72615452
0081B7F5  B9 01 00 00 00                  mov ecx, 1
0081B7FA  4D 85 ED                        test r13, r13
0081B7FD  75 26                           jne 0x14081b825
0081B7FF  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0081B803  E8 08 68 36 00                  call 0x140b82010
0081B808  48 8B D8                        mov rbx, rax
0081B80B  48 85 C0                        test rax, rax
0081B80E  74 0E                           je 0x14081b81e
0081B810  4C 8B 45 48                     mov r8, qword ptr [rbp + 0x48]
0081B814  33 D2                           xor edx, edx
0081B816  48 8B C8                        mov rcx, rax
0081B819  E8 22 B4 EA FF                  call 0x1406c6c40
0081B81E  48 85 DB                        test rbx, rbx
0081B821  75 4A                           jne 0x14081b86d
0081B823  EB 58                           jmp 0x14081b87d
0081B825  4C 8B 65 48                     mov r12, qword ptr [rbp + 0x48]
0081B829  49 8B D4                        mov rdx, r12
0081B82C  E8 DF 67 36 00                  call 0x140b82010
0081B831  48 8B D8                        mov rbx, rax
0081B834  48 85 C0                        test rax, rax
0081B837  74 41                           je 0x14081b87a
0081B839  4D 8B C4                        mov r8, r12
0081B83C  33 D2                           xor edx, edx
0081B83E  48 8B C8                        mov rcx, rax
0081B841  E8 FA B3 EA FF                  call 0x1406c6c40
0081B846  4C 39 65 B0                     cmp qword ptr [rbp - 0x50], r12
0081B84A  49 8B D5                        mov rdx, r13
0081B84D  48 8B CB                        mov rcx, rbx
0081B850  4C 0F 42 65 B0                  cmovb r12, qword ptr [rbp - 0x50]
0081B855  4D 8B C4                        mov r8, r12
0081B858  E8 E3 AF EA FF                  call 0x1406c6840
0081B85D  BA 52 54 61 72                  mov edx, 0x72615452
0081B862  49 8B CD                        mov rcx, r13
0081B865  E8 06 70 36 00                  call 0x140b82870
0081B86A  45 33 E4                        xor r12d, r12d
0081B86D  48 89 5F 38                     mov qword ptr [rdi + 0x38], rbx
0081B871  41 8B DC                        mov ebx, r12d
0081B874  4C 89 77 28                     mov qword ptr [rdi + 0x28], r14
0081B878  EB 08                           jmp 0x14081b882
0081B87A  45 33 E4                        xor r12d, r12d
0081B87D  BB 17 00 00 C0                  mov ebx, 0xc0000017
0081B882  85 DB                           test ebx, ebx
0081B884  75 50                           jne 0x14081b8d6
0081B886  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0081B88A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0081B88E  E8 ED EE C0 FF                  call 0x14042a780
0081B893  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
0081B897  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0081B89B  41 B9 01 00 00 00               mov r9d, 1
0081B8A1  66 44 89 64 24 28               mov word ptr [rsp + 0x28], r12w
0081B8A7  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0081B8AB  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0081B8B0  E8 6B 0D 00 00                  call 0x14081c620
0081B8B5  8B D8                           mov ebx, eax
0081B8B7  85 C0                           test eax, eax
0081B8B9  79 79                           jns 0x14081b934
0081B8BB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0081B8BF  4C 8D 0D AA 39 82 FF            lea r9, [rip - 0x7dc656]
0081B8C6  41 B8 40 09 00 00               mov r8d, 0x940
0081B8CC  E9 EB 01 00 00                  jmp 0x14081babc
0081B8D1  BB 95 00 00 C0                  mov ebx, 0xc0000095
0081B8D6  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
0081B8DA  48 85 C9                        test rcx, rcx
0081B8DD  74 0A                           je 0x14081b8e9
0081B8DF  BA 52 54 61 72                  mov edx, 0x72615452
0081B8E4  E8 87 6F 36 00                  call 0x140b82870
0081B8E9  0F 57 C0                        xorps xmm0, xmm0
0081B8EC  0F 11 47 10                     movups xmmword ptr [rdi + 0x10], xmm0
0081B8F0  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
0081B8F4  0F 11 47 30                     movups xmmword ptr [rdi + 0x30], xmm0
0081B8F8  85 DB                           test ebx, ebx
0081B8FA  79 8A                           jns 0x14081b886
0081B8FC  4C 8D 0D CD 2C 82 FF            lea r9, [rip - 0x7dd333]
0081B903  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0081B907  41 B8 6A 08 00 00               mov r8d, 0x86a
0081B90D  48 8D 15 44 38 82 FF            lea rdx, [rip - 0x7dc7bc]
0081B914  B9 01 00 00 00                  mov ecx, 1
0081B919  E8 CE 2B 14 00                  call 0x14095e4ec
0081B91E  4C 8D 0D 1B 39 82 FF            lea r9, [rip - 0x7dc6e5]
0081B925  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0081B929  41 B8 33 09 00 00               mov r8d, 0x933
0081B92F  E9 88 01 00 00                  jmp 0x14081babc
0081B934  4C 8B 6F 20                     mov r13, qword ptr [rdi + 0x20]
0081B938  4C 8B 4F 28                     mov r9, qword ptr [rdi + 0x28]
0081B93C  4D 3B E9                        cmp r13, r9
0081B93F  0F 82 02 01 00 00               jb 0x14081ba47
0081B945  49 8D 4D 01                     lea rcx, [r13 + 1]
0081B949  49 3B C9                        cmp rcx, r9
0081B94C  0F 86 57 01 00 00               jbe 0x14081baa9
0081B952  48 8B 77 30                     mov rsi, qword ptr [rdi + 0x30]
0081B956  48 FF CE                        dec rsi
0081B959  48 8D 04 0E                     lea rax, [rsi + rcx]
0081B95D  48 3B C1                        cmp rax, rcx
0081B960  0F 82 3E 01 00 00               jb 0x14081baa4
0081B966  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0081B96A  4C 8D 45 B0                     lea r8, [rbp - 0x50]
0081B96E  48 F7 D6                        not rsi
0081B971  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
0081B975  49 8B C9                        mov rcx, r9
0081B978  4C 89 65 48                     mov qword ptr [rbp + 0x48], r12
0081B97C  48 23 F0                        and rsi, rax
0081B97F  E8 FC C9 C2 FF                  call 0x140448380
0081B984  85 C0                           test eax, eax
0081B986  79 0A                           jns 0x14081b992
0081B988  BB 95 00 00 C0                  mov ebx, 0xc0000095
0081B98D  E9 AB 00 00 00                  jmp 0x14081ba3d
0081B992  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0081B996  4C 8D 45 48                     lea r8, [rbp + 0x48]
0081B99A  48 8B CE                        mov rcx, rsi
0081B99D  E8 DE C9 C2 FF                  call 0x140448380
0081B9A2  85 C0                           test eax, eax
0081B9A4  78 E2                           js 0x14081b988
0081B9A6  4C 8B 67 38                     mov r12, qword ptr [rdi + 0x38]
0081B9AA  41 B8 52 54 61 72               mov r8d, 0x72615452
0081B9B0  B9 01 00 00 00                  mov ecx, 1
0081B9B5  4D 85 E4                        test r12, r12
0081B9B8  75 26                           jne 0x14081b9e0
0081B9BA  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0081B9BE  E8 4D 66 36 00                  call 0x140b82010
0081B9C3  48 8B D8                        mov rbx, rax
0081B9C6  48 85 C0                        test rax, rax
0081B9C9  74 0E                           je 0x14081b9d9
0081B9CB  4C 8B 45 48                     mov r8, qword ptr [rbp + 0x48]
0081B9CF  33 D2                           xor edx, edx
0081B9D1  48 8B C8                        mov rcx, rax
0081B9D4  E8 67 B2 EA FF                  call 0x1406c6c40
0081B9D9  48 85 DB                        test rbx, rbx
0081B9DC  75 4A                           jne 0x14081ba28
0081B9DE  EB 58                           jmp 0x14081ba38
0081B9E0  4C 8B 75 48                     mov r14, qword ptr [rbp + 0x48]
0081B9E4  49 8B D6                        mov rdx, r14
0081B9E7  E8 24 66 36 00                  call 0x140b82010
0081B9EC  48 8B D8                        mov rbx, rax
0081B9EF  48 85 C0                        test rax, rax
0081B9F2  74 41                           je 0x14081ba35
0081B9F4  4D 8B C6                        mov r8, r14
0081B9F7  33 D2                           xor edx, edx
0081B9F9  48 8B C8                        mov rcx, rax
0081B9FC  E8 3F B2 EA FF                  call 0x1406c6c40
0081BA01  4C 39 75 B0                     cmp qword ptr [rbp - 0x50], r14
0081BA05  49 8B D4                        mov rdx, r12
0081BA08  48 8B CB                        mov rcx, rbx
0081BA0B  4C 0F 42 75 B0                  cmovb r14, qword ptr [rbp - 0x50]
0081BA10  4D 8B C6                        mov r8, r14
0081BA13  E8 28 AE EA FF                  call 0x1406c6840
0081BA18  BA 52 54 61 72                  mov edx, 0x72615452
0081BA1D  49 8B CC                        mov rcx, r12
0081BA20  E8 4B 6E 36 00                  call 0x140b82870
0081BA25  45 33 E4                        xor r12d, r12d
0081BA28  48 89 5F 38                     mov qword ptr [rdi + 0x38], rbx
0081BA2C  41 8B DC                        mov ebx, r12d
0081BA2F  48 89 77 28                     mov qword ptr [rdi + 0x28], rsi
0081BA33  EB 08                           jmp 0x14081ba3d
0081BA35  45 33 E4                        xor r12d, r12d
0081BA38  BB 17 00 00 C0                  mov ebx, 0xc0000017
0081BA3D  85 DB                           test ebx, ebx
0081BA3F  74 06                           je 0x14081ba47
0081BA41  8B F3                           mov esi, ebx
0081BA43  79 3D                           jns 0x14081ba82
0081BA45  EB 64                           jmp 0x14081baab
0081BA47  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0081BA4B  4C 8D 45 48                     lea r8, [rbp + 0x48]
0081BA4F  49 8B D5                        mov rdx, r13
0081BA52  4C 89 65 48                     mov qword ptr [rbp + 0x48], r12
0081BA56  E8 25 C9 C2 FF                  call 0x140448380
0081BA5B  85 C0                           test eax, eax
0081BA5D  78 45                           js 0x14081baa4
0081BA5F  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
0081BA63  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0081BA67  48 03 D1                        add rdx, rcx
0081BA6A  48 3B D1                        cmp rdx, rcx
0081BA6D  72 35                           jb 0x14081baa4
0081BA6F  0F 10 45 E0                     movups xmm0, xmmword ptr [rbp - 0x20]
0081BA73  0F 11 02                        movups xmmword ptr [rdx], xmm0
0081BA76  0F 10 4D F0                     movups xmm1, xmmword ptr [rbp - 0x10]
0081BA7A  0F 11 4A 10                     movups xmmword ptr [rdx + 0x10], xmm1
0081BA7E  48 FF 47 20                     inc qword ptr [rdi + 0x20]
0081BA82  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0081BA86  0F 57 C0                        xorps xmm0, xmm0
0081BA89  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
0081BA8D  4C 8B C7                        mov r8, rdi
0081BA90  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0081BA94  48 89 38                        mov qword ptr [rax], rdi
0081BA97  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0081BA9B  E8 8C 00 00 00                  call 0x14081bb2c
0081BAA0  8B D8                           mov ebx, eax
0081BAA2  EB 29                           jmp 0x14081bacd
0081BAA4  BE 95 00 00 C0                  mov esi, 0xc0000095
0081BAA9  8B DE                           mov ebx, esi
0081BAAB  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
0081BAAF  4C 8D 0D 02 38 82 FF            lea r9, [rip - 0x7dc7fe]
0081BAB6  41 B8 46 09 00 00               mov r8d, 0x946
0081BABC  48 8D 15 D5 36 82 FF            lea rdx, [rip - 0x7dc92b]
0081BAC3  B9 01 00 00 00                  mov ecx, 1
0081BAC8  E8 1F 2A 14 00                  call 0x14095e4ec
0081BACD  48 8B 7D 58                     mov rdi, qword ptr [rbp + 0x58]
0081BAD1  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0081BAD5  E8 26 4D 1A 00                  call 0x1409c0800
0081BADA  4D 85 FF                        test r15, r15
0081BADD  74 08                           je 0x14081bae7
0081BADF  49 8B D7                        mov rdx, r15
0081BAE2  E8 8D FB 13 00                  call 0x14095b674
0081BAE7  85 DB                           test ebx, ebx
0081BAE9  79 15                           jns 0x14081bb00
0081BAEB  48 8D 4D B8                     lea rcx, [rbp - 0x48]
0081BAEF  E8 50 0D 00 00                  call 0x14081c844
0081BAF4  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0081BAF8  E8 1B 0E 00 00                  call 0x14081c918
0081BAFD  4C 89 27                        mov qword ptr [rdi], r12
0081BB00  8B C3                           mov eax, ebx
0081BB02  EB 05                           jmp 0x14081bb09
0081BB04  B8 F1 00 00 C0                  mov eax, 0xc00000f1
0081BB09  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
0081BB11  48 81 C4 80 00 00 00            add rsp, 0x80
0081BB18  41 5F                           pop r15
0081BB1A  41 5E                           pop r14
0081BB1C  41 5D                           pop r13
0081BB1E  41 5C                           pop r12
0081BB20  5F                              pop rdi
0081BB21  5E                              pop rsi
0081BB22  5D                              pop rbp
0081BB23  C3                              ret
0081BB24  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AslPathWildcardFindFirst(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int16 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int16 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (128);
    v_r12 = 0;
    if (a1 != 0) goto loc_0081B577;
    goto loc_0081BB09;
loc_0081B577:
    if (a3 == 0) goto loc_0081BB04;
    if ((*(unsigned __int16 *)(a3)) == 0) goto loc_0081BB04;
    if (a4 != 0) goto loc_0081B599;
    goto loc_0081BB09;
loc_0081B599:
    *(unsigned __int16 *)(a1) = 0;
    v_stack_m80 = 0;
    v_stack_p10 = 0;
    *(unsigned __int64 *)(a4) = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm1;
    v_stack_m48 = v_xmm1;
    result = RtlCreateUnicodeString(v_stack_m78, a3, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0081B5FA;
loc_0081B5E4:
    result = AslLogCallPrintf(1, v_rip - 8242259, (unsigned int)(0x8C2ULL), v_rip - 8242278);
    goto loc_0081BAD1;
loc_0081B5FA:
    result = AslPathCleanUstr(v_stack_m78, v_rip - 8242259, (unsigned int)(0x8C2ULL), v_rip - 8242278);
    if (!sign_flag) goto loc_0081B630;
loc_0081B616:
    v_stack_m98 = (unsigned int)(result);
    result = AslLogCallPrintf(1, v_rip - 8242309, (unsigned int)(0x8D7ULL), v_rip - 8242264);
    goto loc_0081BAD1;
loc_0081B630:
    result = RtlUShortAdd(v_stack_m78, 4, v_stack_p10, v_rip - 8242264);
    if (!sign_flag) goto loc_0081B65B;
    goto loc_0081B616;
loc_0081B65B:
    result = AslAlloc(v_stack_m78, (unsigned int)((unsigned int)(v_stack_p10)), (unsigned int)(0x8DDULL), v_rip - 8242299);
    if (result != 0) goto loc_0081B678;
    goto loc_0081BAD1;
loc_0081B678:
    result = RtlStringCbCopyNW(result, (unsigned int)(0xC0000017ULL), v_stack_m70, v_stack_m78);
    if (!sign_flag) goto loc_0081B6A4;
    goto loc_0081B616;
loc_0081B6A4:
    result = AslpPathWildcardMakeLeaves(result, (unsigned int)(0xC0000017ULL), (unsigned int)(0x8E9ULL), v_rip - 8242337);
    if ((unsigned int)(result) != 0) goto loc_0081B6C7;
    goto loc_0081B5E4;
loc_0081B6C7:
    if (((unsigned int)(result)) != 1) goto loc_0081B717;
    result = AslDoesFileExistNtPath(v_stack_m70, (unsigned int)(0xC0000017ULL), (unsigned int)(0x8FBULL), v_rip - 8242340);
    if ((unsigned int)(result) != 0) goto loc_0081B6E7;
    goto loc_0081BAD1;
loc_0081B6E7:
    result = RtlStringCchCopyW(a1, 260, a3, v_rip - 8242340);
    if (!sign_flag) goto loc_0081B70F;
    goto loc_0081B616;
loc_0081B70F:
    goto loc_0081BAD1;
loc_0081B717:
    result = AslAlloc(a1, 64, (unsigned int)(0x90DULL), v_rip - 8242444);
    v_stack_m80 = result;
    if (result != 0) goto loc_0081B737;
    goto loc_0081BACD;
loc_0081B737:
    result = wcsncmp(a3, v_rip - 8387713, 4, v_rip - 8242444);
    a1 = ((unsigned int)(result) != 0) ? 1 : 0;
    *(unsigned int *)(result) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm0;
    *(unsigned __int64 *)(result + 40) = 0;
    *(unsigned __int64 *)(result + 48) = 16;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 56) = 0;
    *(unsigned __int64 *)(result + 24) = 32;
    if ((*(unsigned __int64 *)(result + 40)) < 8) goto loc_0081B79C;
    goto loc_0081B8D6;
loc_0081B79C:
    result = (*(unsigned __int64 *)(result + 48)) + (7);
    if (result < 8) goto loc_0081B8D1;
    v_r14 = ~(*(unsigned __int64 *)(result + 48) - 1);
    v_stack_m88 = 0;
    v_stack_p10 = 0;
    v_r14 = (v_r14) & (result);
    result = ULongLongMult(*(unsigned __int64 *)(result + 40), 32, v_stack_m88, v_rip - 8242444);
    if (!sign_flag) goto loc_0081B7D7;
loc_0081B7CD:
    goto loc_0081B882;
loc_0081B7D7:
    result = ULongLongMult(v_r14, *(unsigned __int64 *)(result + 24), v_stack_p10, v_rip - 8242444);
    if (sign_flag) goto loc_0081B7CD;
    if (*(unsigned __int64 *)(result + 56) != 0) goto loc_0081B825;
    result = ExAllocatePoolWithTag(1, v_stack_p10, (unsigned int)(0x72615452ULL), v_rip - 8242444);
    if (result != 0) {
        a3 = v_stack_p10;
        a2 = 0;
        a1 = result;
        result = memset(a1, a2, a3, v_rip - 8242444);
    }
    if (result != 0) goto loc_0081B86D;
    goto loc_0081B87D;
loc_0081B825:
    result = ExAllocatePoolWithTag(a1, v_stack_p10, a3, v_rip - 8242444);
    if (result == 0) goto loc_0081B87A;
    a2 = 0;
    result = memset(result, a2, v_stack_p10, v_rip - 8242444);
    v_r12 = v_stack_p10;
    if (v_stack_m88 < v_stack_p10) { v_r12 = v_stack_m88; }
    result = memcpy(result, *(unsigned __int64 *)(result + 56), v_r12, v_rip - 8242444);
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 56), (unsigned int)(0x72615452ULL), v_r12, v_rip - 8242444);
    v_r12 = 0;
loc_0081B86D:
    *(unsigned __int64 *)(result + 56) = result;
    *(unsigned __int64 *)(result + 40) = v_r14;
    goto loc_0081B882;
loc_0081B87A:
    v_r12 = 0;
loc_0081B87D:
loc_0081B882:
    if ((unsigned int)((unsigned int)(0xC0000017ULL)) != 0) goto loc_0081B8D6;
loc_0081B886:
    result = RtlInitUnicodeString(v_stack_m68, *(unsigned __int64 *)(result + 8), v_r12, v_rip - 8242444);
    v_stack_m90 = 0;
    v_stack_m98 = 0;
    result = AslpPathWildcardAllocMatchNode(v_stack_m58, v_stack_m68, *(unsigned __int64 *)(result + 8), 1);
    if (!sign_flag) goto loc_0081B934;
    v_stack_m98 = (unsigned int)(result);
    goto loc_0081BABC;
loc_0081B8D1:
loc_0081B8D6:
    if (*(unsigned __int64 *)(result + 56) != 0) {
        a2 = 0x72615452ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 56), a2, (unsigned int)(0x940ULL), v_rip - 8242774);
    }
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm0;
    if (!sign_flag) goto loc_0081B886;
    v_stack_m98 = (unsigned int)((unsigned int)(0xC0000095ULL));
    result = AslLogCallPrintf(1, v_rip - 8243132, (unsigned int)(0x86AULL), v_rip - 8246067);
    v_stack_m98 = (unsigned int)((unsigned int)(0xC0000095ULL));
    goto loc_0081BABC;
loc_0081B934:
    if ((*(unsigned __int64 *)(result + 32)) < (*(unsigned __int64 *)(result + 40))) goto loc_0081BA47;
    if ((*(unsigned __int64 *)(result + 32) + 1) <= (*(unsigned __int64 *)(result + 40))) goto loc_0081BAA9;
    v_rsi = (*(unsigned __int64 *)(result + 48)) - 1;
    if ((v_rsi + *(unsigned __int64 *)(result + 32) + 1 * 1) < (*(unsigned __int64 *)(result + 32) + 1)) goto loc_0081BAA4;
    v_rsi = ~(v_rsi);
    v_stack_m88 = 0;
    v_stack_p10 = 0;
    v_rsi = (v_rsi) & (v_rsi + *(unsigned __int64 *)(result + 32) + 1 * 1);
    result = ULongLongMult(*(unsigned __int64 *)(result + 40), *(unsigned __int64 *)(result + 24), v_stack_m88, *(unsigned __int64 *)(result + 40));
    if (!sign_flag) goto loc_0081B992;
loc_0081B988:
    goto loc_0081BA3D;
loc_0081B992:
    result = ULongLongMult(v_rsi, *(unsigned __int64 *)(result + 24), v_stack_p10, *(unsigned __int64 *)(result + 40));
    if (sign_flag) goto loc_0081B988;
    if (*(unsigned __int64 *)(result + 56) != 0) goto loc_0081B9E0;
    result = ExAllocatePoolWithTag(1, v_stack_p10, (unsigned int)(0x72615452ULL), *(unsigned __int64 *)(result + 40));
    if (result != 0) {
        a3 = v_stack_p10;
        a2 = 0;
        a1 = result;
        result = memset(a1, a2, a3, *(unsigned __int64 *)(result + 40));
    }
    if (result != 0) goto loc_0081BA28;
    goto loc_0081BA38;
loc_0081B9E0:
    result = ExAllocatePoolWithTag(a1, v_stack_p10, a3, *(unsigned __int64 *)(result + 40));
    if (result == 0) goto loc_0081BA35;
    a2 = 0;
    result = memset(result, a2, v_stack_p10, *(unsigned __int64 *)(result + 40));
    v_r14 = v_stack_p10;
    if (v_stack_m88 < v_stack_p10) { v_r14 = v_stack_m88; }
    result = memcpy(result, *(unsigned __int64 *)(result + 56), v_r14, *(unsigned __int64 *)(result + 40));
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 56), (unsigned int)(0x72615452ULL), v_r14, *(unsigned __int64 *)(result + 40));
    v_r12 = 0;
loc_0081BA28:
    *(unsigned __int64 *)(result + 56) = result;
    *(unsigned __int64 *)(result + 40) = v_rsi;
    goto loc_0081BA3D;
loc_0081BA35:
    v_r12 = 0;
loc_0081BA38:
loc_0081BA3D:
    if ((unsigned int)((unsigned int)(0xC0000017ULL)) == 0) goto loc_0081BA47;
    if (!sign_flag) goto loc_0081BA82;
    goto loc_0081BAAB;
loc_0081BA47:
    v_stack_p10 = 0;
    result = ULongLongMult(*(unsigned __int64 *)(result + 24), *(unsigned __int64 *)(result + 32), v_stack_p10, *(unsigned __int64 *)(result + 40));
    if (sign_flag) goto loc_0081BAA4;
    a2 = (v_stack_p10) + (*(unsigned __int64 *)(result + 56));
    if (a2 < (*(unsigned __int64 *)(result + 56))) goto loc_0081BAA4;
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int64 *)(a2 + 16) = v_xmm1;
loc_0081BA82:
    v_stack_m58 = v_xmm0;
    *(unsigned __int64 *)(v_stack_p20) = result;
    v_stack_m48 = v_xmm0;
    result = AslPathWildcardFindNext(v_stack_p8, a2, result, *(unsigned __int64 *)(result + 40));
    goto loc_0081BACD;
loc_0081BAA4:
loc_0081BAA9:
loc_0081BAAB:
    v_stack_m98 = (unsigned int)((unsigned int)(0xC0000095ULL));
loc_0081BABC:
    result = AslLogCallPrintf(1, v_rip - 8243499, (unsigned int)(0x946ULL), v_rip - 8243198);
loc_0081BACD:
loc_0081BAD1:
    result = RtlFreeAnsiString(v_stack_m78, v_rip - 8243499, (unsigned int)(0x946ULL), v_rip - 8243198);
    if (0 != 0) {
        a2 = 0;
        result = AslFree(v_stack_m78, a2, (unsigned int)(0x946ULL), v_rip - 8243198);
    }
    if (sign_flag) {
        a1 = v_stack_m80;
        result = AslpPathWildcardFreeFindContext(a1, a2, (unsigned int)(0x946ULL), v_rip - 8243198);
        a1 = v_stack_m58;
        result = AslpPathWildcardFreeMatchNode(a1, a2, (unsigned int)(0x946ULL), v_rip - 8243198);
        *(unsigned __int64 *)(v_stack_p20) = 0;
    }
    goto loc_0081BB09;
loc_0081BB04:
loc_0081BB09:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)(0xC00000F1ULL);
}
```

## 5. (Beta) C Style

```c
int64_t AslPathWildcardFindFirst(int64_t Arg1, int64_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint16_t v_stack_m90;
    uint32_t v_stack_m98;
    uint16_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (128);
    local_r12 = 0;
    if (Arg1 != 0) goto loc_0081B577;
    goto loc_0081BB09;
loc_0081B577:
    if (Arg3 == NULL) goto loc_0081BB04;
    if ((*(uint16_t *)(arg3)) == 0) goto loc_0081BB04;
    if (Arg4 != NULL) goto loc_0081B599;
    goto loc_0081BB09;
loc_0081B599:
    *(uint16_t *)(Arg1) = 0;
    v_stack_m80 = 0;
    v_stack_p10 = 0;
    *(uint64_t *)(arg4) = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm1;
    v_stack_m48 = v_xmm1;
    result = RtlCreateUnicodeString(v_stack_m78, Arg3, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0081B5FA;
loc_0081B5E4:
    result = AslLogCallPrintf(1, v_rip - 8242259, (uint32_t)(0x8C2ULL), v_rip - 8242278);
    goto loc_0081BAD1;
loc_0081B5FA:
    result = AslPathCleanUstr(v_stack_m78, v_rip - 8242259, (uint32_t)(0x8C2ULL), v_rip - 8242278);
    if (!sign_flag) goto loc_0081B630;
loc_0081B616:
    v_stack_m98 = (uint32_t)(result);
    result = AslLogCallPrintf(1, v_rip - 8242309, (uint32_t)(0x8D7ULL), v_rip - 8242264);
    goto loc_0081BAD1;
loc_0081B630:
    result = RtlUShortAdd(v_stack_m78, 4, v_stack_p10, v_rip - 8242264);
    if (!sign_flag) goto loc_0081B65B;
    goto loc_0081B616;
loc_0081B65B:
    result = AslAlloc(v_stack_m78, (uint32_t)((uint32_t)(v_stack_p10)), (uint32_t)(0x8DDULL), v_rip - 8242299);
    if (result != 0) goto loc_0081B678;
    goto loc_0081BAD1;
loc_0081B678:
    result = RtlStringCbCopyNW(result, (uint32_t)(0xC0000017ULL), v_stack_m70, v_stack_m78);
    if (!sign_flag) goto loc_0081B6A4;
    goto loc_0081B616;
loc_0081B6A4:
    result = AslpPathWildcardMakeLeaves(result, (uint32_t)(0xC0000017ULL), (uint32_t)(0x8E9ULL), v_rip - 8242337);
    if ((uint32_t)(result) != 0) goto loc_0081B6C7;
    goto loc_0081B5E4;
loc_0081B6C7:
    if (((uint32_t)(result)) != 1) goto loc_0081B717;
    result = AslDoesFileExistNtPath(v_stack_m70, (uint32_t)(0xC0000017ULL), (uint32_t)(0x8FBULL), v_rip - 8242340);
    if ((uint32_t)(result) != 0) goto loc_0081B6E7;
    goto loc_0081BAD1;
loc_0081B6E7:
    result = RtlStringCchCopyW(Arg1, 260, Arg3, v_rip - 8242340);
    if (!sign_flag) goto loc_0081B70F;
    goto loc_0081B616;
loc_0081B70F:
    goto loc_0081BAD1;
loc_0081B717:
    result = AslAlloc(Arg1, 64, (uint32_t)(0x90DULL), v_rip - 8242444);
    v_stack_m80 = result;
    if (result != 0) goto loc_0081B737;
    goto loc_0081BACD;
loc_0081B737:
    result = wcsncmp(Arg3, v_rip - 8387713, 4, v_rip - 8242444);
    Arg1 = ((uint32_t)(result) != 0) ? 1 : 0;
    *(uint32_t *)(result) = (uint32_t)(Arg1);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm0;
    *(uint64_t *)(result + 0x28) = 0;
    *(uint64_t *)(result + 0x30) = 16;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x38) = 0;
    *(uint64_t *)(result + 0x18) = 32;
    if ((*(uint64_t *)(result + 0x28)) < 8) goto loc_0081B79C;
    goto loc_0081B8D6;
loc_0081B79C:
    result = (*(uint64_t *)(result + 0x30)) + (7);
    if (result < 8) goto loc_0081B8D1;
    local_r14 = ~(*(uint64_t *)(result + 0x30) - 1);
    v_stack_m88 = 0;
    v_stack_p10 = 0;
    local_r14 = (local_r14) & (result);
    result = ULongLongMult(*(uint64_t *)(result + 0x28), 32, v_stack_m88, v_rip - 8242444);
    if (!sign_flag) goto loc_0081B7D7;
loc_0081B7CD:
    goto loc_0081B882;
loc_0081B7D7:
    result = ULongLongMult(local_r14, *(uint64_t *)(result + 0x18), v_stack_p10, v_rip - 8242444);
    if (sign_flag) goto loc_0081B7CD;
    if (*(uint64_t *)(result + 0x38) != 0) goto loc_0081B825;
    result = ExAllocatePoolWithTag(1, v_stack_p10, (uint32_t)(0x72615452ULL), v_rip - 8242444);
    if (result != 0) {
        Arg3 = v_stack_p10;
        Arg2 = 0;
        Arg1 = result;
        result = memset(Arg1, Arg2, Arg3, v_rip - 8242444);
    }
    if (result != 0) goto loc_0081B86D;
    goto loc_0081B87D;
loc_0081B825:
    result = ExAllocatePoolWithTag(Arg1, v_stack_p10, Arg3, v_rip - 8242444);
    if (result == 0) goto loc_0081B87A;
    Arg2 = 0;
    result = memset(result, Arg2, v_stack_p10, v_rip - 8242444);
    local_r12 = v_stack_p10;
    if (v_stack_m88 < v_stack_p10) { local_r12 = v_stack_m88; }
    result = memcpy(result, *(uint64_t *)(result + 0x38), local_r12, v_rip - 8242444);
    result = ExFreePoolWithTag(*(uint64_t *)(result + 0x38), (uint32_t)(0x72615452ULL), local_r12, v_rip - 8242444);
    local_r12 = 0;
loc_0081B86D:
    *(uint64_t *)(result + 0x38) = result;
    *(uint64_t *)(result + 0x28) = local_r14;
    goto loc_0081B882;
loc_0081B87A:
    local_r12 = 0;
loc_0081B87D:
loc_0081B882:
    if ((uint32_t)((uint32_t)(0xC0000017ULL)) != 0) goto loc_0081B8D6;
loc_0081B886:
    result = RtlInitUnicodeString(v_stack_m68, *(uint64_t *)(result + 0x8), local_r12, v_rip - 8242444);
    v_stack_m90 = 0;
    v_stack_m98 = 0;
    result = AslpPathWildcardAllocMatchNode(v_stack_m58, v_stack_m68, *(uint64_t *)(result + 0x8), 1);
    if (!sign_flag) goto loc_0081B934;
    v_stack_m98 = (uint32_t)(result);
    goto loc_0081BABC;
loc_0081B8D1:
loc_0081B8D6:
    if (*(uint64_t *)(result + 0x38) != 0) {
        Arg2 = 0x72615452ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x38), Arg2, (uint32_t)(0x940ULL), v_rip - 8242774);
    }
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm0;
    if (!sign_flag) goto loc_0081B886;
    v_stack_m98 = (uint32_t)((uint32_t)(0xC0000095ULL));
    result = AslLogCallPrintf(1, v_rip - 8243132, (uint32_t)(0x86AULL), v_rip - 8246067);
    v_stack_m98 = (uint32_t)((uint32_t)(0xC0000095ULL));
    goto loc_0081BABC;
loc_0081B934:
    if ((*(uint64_t *)(result + 0x20)) < (*(uint64_t *)(result + 0x28))) goto loc_0081BA47;
    if ((*(uint64_t *)(result + 0x20) + 1) <= (*(uint64_t *)(result + 0x28))) goto loc_0081BAA9;
    local_rsi = (*(uint64_t *)(result + 0x30)) - 1;
    if ((local_rsi + *(uint64_t *)(result + 0x20) + 1 * 1) < (*(uint64_t *)(result + 0x20) + 1)) goto loc_0081BAA4;
    local_rsi = ~(local_rsi);
    v_stack_m88 = 0;
    v_stack_p10 = 0;
    local_rsi = (local_rsi) & (local_rsi + *(uint64_t *)(result + 0x20) + 1 * 1);
    result = ULongLongMult(*(uint64_t *)(result + 0x28), *(uint64_t *)(result + 0x18), v_stack_m88, *(uint64_t *)(result + 0x28));
    if (!sign_flag) goto loc_0081B992;
loc_0081B988:
    goto loc_0081BA3D;
loc_0081B992:
    result = ULongLongMult(local_rsi, *(uint64_t *)(result + 0x18), v_stack_p10, *(uint64_t *)(result + 0x28));
    if (sign_flag) goto loc_0081B988;
    if (*(uint64_t *)(result + 0x38) != 0) goto loc_0081B9E0;
    result = ExAllocatePoolWithTag(1, v_stack_p10, (uint32_t)(0x72615452ULL), *(uint64_t *)(result + 0x28));
    if (result != 0) {
        Arg3 = v_stack_p10;
        Arg2 = 0;
        Arg1 = result;
        result = memset(Arg1, Arg2, Arg3, *(uint64_t *)(result + 0x28));
    }
    if (result != 0) goto loc_0081BA28;
    goto loc_0081BA38;
loc_0081B9E0:
    result = ExAllocatePoolWithTag(Arg1, v_stack_p10, Arg3, *(uint64_t *)(result + 0x28));
    if (result == 0) goto loc_0081BA35;
    Arg2 = 0;
    result = memset(result, Arg2, v_stack_p10, *(uint64_t *)(result + 0x28));
    local_r14 = v_stack_p10;
    if (v_stack_m88 < v_stack_p10) { local_r14 = v_stack_m88; }
    result = memcpy(result, *(uint64_t *)(result + 0x38), local_r14, *(uint64_t *)(result + 0x28));
    result = ExFreePoolWithTag(*(uint64_t *)(result + 0x38), (uint32_t)(0x72615452ULL), local_r14, *(uint64_t *)(result + 0x28));
    local_r12 = 0;
loc_0081BA28:
    *(uint64_t *)(result + 0x38) = result;
    *(uint64_t *)(result + 0x28) = local_rsi;
    goto loc_0081BA3D;
loc_0081BA35:
    local_r12 = 0;
loc_0081BA38:
loc_0081BA3D:
    if ((uint32_t)((uint32_t)(0xC0000017ULL)) == 0) goto loc_0081BA47;
    if (!sign_flag) goto loc_0081BA82;
    goto loc_0081BAAB;
loc_0081BA47:
    v_stack_p10 = 0;
    result = ULongLongMult(*(uint64_t *)(result + 0x18), *(uint64_t *)(result + 0x20), v_stack_p10, *(uint64_t *)(result + 0x28));
    if (sign_flag) goto loc_0081BAA4;
    Arg2 = (v_stack_p10) + (*(uint64_t *)(result + 0x38));
    if (Arg2 < (*(uint64_t *)(result + 0x38))) goto loc_0081BAA4;
    *(uint64_t *)(Arg2) = v_xmm0;
    *(uint64_t *)(Arg2 + 0x10) = v_xmm1;
loc_0081BA82:
    v_stack_m58 = v_xmm0;
    *(uint64_t *)(v_stack_p20) = result;
    v_stack_m48 = v_xmm0;
    result = AslPathWildcardFindNext(v_stack_p8, Arg2, result, *(uint64_t *)(result + 0x28));
    goto loc_0081BACD;
loc_0081BAA4:
loc_0081BAA9:
loc_0081BAAB:
    v_stack_m98 = (uint32_t)((uint32_t)(0xC0000095ULL));
loc_0081BABC:
    result = AslLogCallPrintf(1, v_rip - 8243499, (uint32_t)(0x946ULL), v_rip - 8243198);
loc_0081BACD:
loc_0081BAD1:
    result = RtlFreeAnsiString(v_stack_m78, v_rip - 8243499, (uint32_t)(0x946ULL), v_rip - 8243198);
    if (0 != 0) {
        Arg2 = 0;
        result = AslFree(v_stack_m78, Arg2, (uint32_t)(0x946ULL), v_rip - 8243198);
    }
    if (sign_flag) {
        Arg1 = v_stack_m80;
        result = AslpPathWildcardFreeFindContext(Arg1, Arg2, (uint32_t)(0x946ULL), v_rip - 8243198);
        Arg1 = v_stack_m58;
        result = AslpPathWildcardFreeMatchNode(Arg1, Arg2, (uint32_t)(0x946ULL), v_rip - 8243198);
        *(uint64_t *)(v_stack_p20) = 0;
    }
    goto loc_0081BB09;
loc_0081BB04:
loc_0081BB09:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)(0xC00000F1ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0081B534&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
