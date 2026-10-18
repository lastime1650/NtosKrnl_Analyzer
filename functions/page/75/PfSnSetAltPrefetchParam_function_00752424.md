# PfSnSetAltPrefetchParam

- RVA: `0x00752424`–`0x007528A9` (길이 `1,157` bytes)
- VA: `0x0000000140752424`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CBBE4`
- 디코드: `281`개 명령, `1,157/1,157` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0075246A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007524E9` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00752549` → [PfSnCheckScenario](../95/PfSnCheckScenario_function_0095EF5C.md) (function, `0x0095EF5C`)
- `0x00752563` → [PfCalculateProcessHash](../96/PfCalculateProcessHash_function_00960310.md) (function, `0x00960310`)
- `0x007525E6` → [PfSnCalculateScenarioNameAndHash](../95/PfSnCalculateScenarioNameAndHash_function_0095FD18.md) (function, `0x0095FD18`)
- `0x00752626` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00752645` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007526A0` → [FsRtlAcquirePushLockExclusive](../../text/4A/FsRtlAcquirePushLockExclusive_function_004A05F4.md) (function, `0x004A05F4`)
- `0x007526AD` → [PfSnAltProfileFindByScenarioId](../95/PfSnAltProfileFindByScenarioId_function_0095FC3C.md) (function, `0x0095FC3C`)
- `0x007526E1` → [PfSnAltProfileFindByProcess](../90/PfSnAltProfileFindByProcess_function_00903D4C.md) (function, `0x00903D4C`)
- `0x00752727` → [PfSnAltProfileTreeCompareByProcess](../90/PfSnAltProfileTreeCompareByProcess_function_00903DD8.md) (function, `0x00903DD8`)
- `0x0075276F` → [RtlRbInsertNodeEx](../../text/2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x007527AE` → [PfSnAltProfileTreeCompareByScenarioId](../95/PfSnAltProfileTreeCompareByScenarioId_function_0095FCD0.md) (function, `0x0095FCD0`)
- `0x007527F7` → [RtlRbInsertNodeEx](../../text/2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x00752803` → [PfLockExclusiveRelease](../../text/49/PfLockExclusiveRelease_function_00491D88.md) (function, `0x00491D88`)
- `0x00752838` → [PfLockExclusiveRelease](../../text/49/PfLockExclusiveRelease_function_00491D88.md) (function, `0x00491D88`)
- `0x0075284C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00752859` → [PfSnAltProfileCleanup](PfSnAltProfileCleanup_function_00752270.md) (function, `0x00752270`)
- `0x00752866` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00752878` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0075288A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9DE1`

### Static image references
- `0x00752439` → RVA `0x00E0A740` (`.data`; read)
- `0x007524BB` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00752699` → RVA `0x00E67388` (`.data`; read)
- `0x007526EF` → RVA `0x00E67370` (`.data`; read)
- `0x007526F6` → RVA `0x00E67368` (`.data`; read)
- `0x00752774` → RVA `0x00E67380` (`.data`; read)
- `0x0075277B` → RVA `0x00E67378` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x0075246A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00752626` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00752645` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007526A0` → [FsRtlAcquirePushLockExclusive](../../text/4A/FsRtlAcquirePushLockExclusive_function_004A05F4.md) (`PAGE` → `.text`)
  - `0x0075276F` → [RtlRbInsertNodeEx](../../text/2E/RtlRbInsertNodeEx_function_002E4570.md) (`PAGE` → `.text`)
  - `0x007527F7` → [RtlRbInsertNodeEx](../../text/2E/RtlRbInsertNodeEx_function_002E4570.md) (`PAGE` → `.text`)
  - `0x00752803` → [PfLockExclusiveRelease](../../text/49/PfLockExclusiveRelease_function_00491D88.md) (`PAGE` → `.text`)
  - `0x00752838` → [PfLockExclusiveRelease](../../text/49/PfLockExclusiveRelease_function_00491D88.md) (`PAGE` → `.text`)
  - `0x0075284C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00752866` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00752878` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0075288A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00752424  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00752429  57                              push rdi
0075242A  41 54                           push r12
0075242C  41 55                           push r13
0075242E  41 56                           push r14
00752430  41 57                           push r15
00752432  48 81 EC 20 02 00 00            sub rsp, 0x220
00752439  48 8B 05 00 83 6B 00            mov rax, qword ptr [rip + 0x6b8300]
00752440  48 33 C4                        xor rax, rsp
00752443  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
0075244B  41 8A D9                        mov bl, r9b
0075244E  45 8B E8                        mov r13d, r8d
00752451  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00752459  48 8B F9                        mov rdi, rcx
0075245C  33 D2                           xor edx, edx
0075245E  44 8D 42 44                     lea r8d, [rdx + 0x44]
00752462  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
0075246A  E8 D1 47 F7 FF                  call 0x1406c6c40
0075246F  0F 57 C0                        xorps xmm0, xmm0
00752472  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
0075247A  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
0075247F  83 64 24 70 00                  and dword ptr [rsp + 0x70], 0
00752484  83 64 24 78 00                  and dword ptr [rsp + 0x78], 0
00752489  83 64 24 74 00                  and dword ptr [rsp + 0x74], 0
0075248E  83 A4 24 84 00 00 00 00         and dword ptr [rsp + 0x84], 0
00752496  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
0075249E  48 83 A4 24 90 00 00 00 00      and qword ptr [rsp + 0x90], 0
007524A7  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
007524AD  45 33 F6                        xor r14d, r14d
007524B0  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
007524B8  45 33 FF                        xor r15d, r15d
007524BB  4C 8B 05 D6 45 87 00            mov r8, qword ptr [rip + 0x8745d6]
007524C2  4C 21 74 24 38                  and qword ptr [rsp + 0x38], r14
007524C7  4C 21 74 24 30                  and qword ptr [rsp + 0x30], r14
007524CC  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007524D1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007524D6  C7 44 24 20 50 66 57 73         mov dword ptr [rsp + 0x20], 0x73576650
007524DE  44 8A CB                        mov r9b, bl
007524E1  BA 00 02 00 00                  mov edx, 0x200
007524E6  48 8B CF                        mov rcx, rdi
007524E9  E8 62 71 11 00                  call 0x140869650
007524EE  8B F8                           mov edi, eax
007524F0  85 C0                           test eax, eax
007524F2  0F 88 2F 03 00 00               js 0x140752827
007524F8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00752501  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00752506  4C 3B A0 B8 00 00 00            cmp r12, qword ptr [rax + 0xb8]
0075250D  74 0A                           je 0x140752519
0075250F  BF 0D 00 00 C0                  mov edi, 0xc000000d
00752514  E9 13 03 00 00                  jmp 0x14075282c
00752519  41 83 FD 04                     cmp r13d, 4
0075251D  74 0A                           je 0x140752529
0075251F  BF 04 00 00 C0                  mov edi, 0xc0000004
00752524  E9 03 03 00 00                  jmp 0x14075282c
00752529  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
00752531  8B 1B                           mov ebx, dword ptr [rbx]
00752533  89 9C 24 98 00 00 00            mov dword ptr [rsp + 0x98], ebx
0075253A  83 FB 10                        cmp ebx, 0x10
0075253D  77 D0                           ja 0x14075250f
0075253F  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
00752547  33 C9                           xor ecx, ecx
00752549  E8 0E CA 20 00                  call 0x14095ef5c
0075254E  8B F8                           mov edi, eax
00752550  85 C0                           test eax, eax
00752552  0F 88 D4 02 00 00               js 0x14075282c
00752558  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00752560  49 8B CC                        mov rcx, r12
00752563  E8 A8 DD 20 00                  call 0x140960310
00752568  8B F8                           mov edi, eax
0075256A  85 C0                           test eax, eax
0075256C  0F 88 BA 02 00 00               js 0x14075282c
00752572  41 BD 00 01 00 00               mov r13d, 0x100
00752578  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
0075257D  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00752585  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0075258A  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0075258F  48 8D 84 24 84 00 00 00         lea rax, [rsp + 0x84]
00752597  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0075259C  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
007525A4  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007525A9  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007525AE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007525B3  48 8D 44 24 74                  lea rax, [rsp + 0x74]
007525B8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007525BD  48 8D 44 24 78                  lea rax, [rsp + 0x78]
007525C2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007525C7  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007525CC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007525D1  4C 8D 4C 24 7C                  lea r9, [rsp + 0x7c]
007525D6  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
007525DE  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
007525E6  E8 2D D7 20 00                  call 0x14095fd18
007525EB  8B F8                           mov edi, eax
007525ED  85 C0                           test eax, eax
007525EF  0F 88 37 02 00 00               js 0x14075282c
007525F5  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
007525F9  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
00752600  44 8B 44 24 74                  mov r8d, dword ptr [rsp + 0x74]
00752605  44 03 44 24 78                  add r8d, dword ptr [rsp + 0x78]
0075260A  44 03 44 24 7C                  add r8d, dword ptr [rsp + 0x7c]
0075260F  44 89 84 24 FC 00 00 00         mov dword ptr [rsp + 0xfc], r8d
00752617  41 8D 7D 80                     lea edi, [r13 - 0x80]
0075261B  41 B8 43 63 50 66               mov r8d, 0x66506343
00752621  8B D7                           mov edx, edi
00752623  41 8B CD                        mov ecx, r13d
00752626  E8 C5 FA 42 00                  call 0x140b820f0
0075262B  4C 8B F0                        mov r14, rax
0075262E  48 85 C0                        test rax, rax
00752631  75 0A                           jne 0x14075263d
00752633  BF 9A 00 00 C0                  mov edi, 0xc000009a
00752638  E9 EF 01 00 00                  jmp 0x14075282c
0075263D  4C 8B C7                        mov r8, rdi
00752640  33 D2                           xor edx, edx
00752642  49 8B CE                        mov rcx, r14
00752645  E8 F6 45 F7 FF                  call 0x1406c6c40
0075264A  41 89 5E 7C                     mov dword ptr [r14 + 0x7c], ebx
0075264E  4D 89 66 30                     mov qword ptr [r14 + 0x30], r12
00752652  0F 28 84 24 C0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xc0]
0075265A  41 0F 11 46 38                  movups xmmword ptr [r14 + 0x38], xmm0
0075265F  0F 28 8C 24 D0 00 00 00         movaps xmm1, xmmword ptr [rsp + 0xd0]
00752667  41 0F 11 4E 48                  movups xmmword ptr [r14 + 0x48], xmm1
0075266C  0F 28 84 24 E0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xe0]
00752674  41 0F 11 46 58                  movups xmmword ptr [r14 + 0x58], xmm0
00752679  0F 28 8C 24 F0 00 00 00         movaps xmm1, xmmword ptr [rsp + 0xf0]
00752681  41 0F 11 4E 68                  movups xmmword ptr [r14 + 0x68], xmm1
00752686  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
0075268D  41 89 46 78                     mov dword ptr [r14 + 0x78], eax
00752691  45 33 E4                        xor r12d, r12d
00752694  45 8D 7C 24 01                  lea r15d, [r12 + 1]
00752699  48 8D 0D E8 4C 71 00            lea rcx, [rip + 0x714ce8]
007526A0  E8 4F DF D4 FF                  call 0x1404a05f4
007526A5  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
007526AD  E8 8A D5 20 00                  call 0x14095fc3c
007526B2  48 85 C0                        test rax, rax
007526B5  74 1E                           je 0x1407526d5
007526B7  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
007526BB  49 39 4E 30                     cmp qword ptr [r14 + 0x30], rcx
007526BF  74 0A                           je 0x1407526cb
007526C1  BF 18 07 00 C0                  mov edi, 0xc0000718
007526C6  E9 61 01 00 00                  jmp 0x14075282c
007526CB  89 58 7C                        mov dword ptr [rax + 0x7c], ebx
007526CE  33 FF                           xor edi, edi
007526D0  E9 57 01 00 00                  jmp 0x14075282c
007526D5  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
007526D9  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007526DE  48 8B C8                        mov rcx, rax
007526E1  E8 66 16 1B 00                  call 0x140903d4c
007526E6  48 85 C0                        test rax, rax
007526E9  0F 85 20 FE FF FF               jne 0x14075250f
007526EF  48 8B 05 7A 4C 71 00            mov rax, qword ptr [rip + 0x714c7a]
007526F6  48 8B 1D 6B 4C 71 00            mov rbx, qword ptr [rip + 0x714c6b]
007526FD  4C 8D 2D 64 4C 71 00            lea r13, [rip + 0x714c64]
00752704  41 84 C7                        test r15b, al
00752707  74 08                           je 0x140752711
00752709  48 85 DB                        test rbx, rbx
0075270C  74 03                           je 0x140752711
0075270E  49 33 DD                        xor rbx, r13
00752711  0F B6 F8                        movzx edi, al
00752714  41 23 FF                        and edi, r15d
00752717  45 32 C0                        xor r8b, r8b
0075271A  48 85 DB                        test rbx, rbx
0075271D  74 47                           je 0x140752766
0075271F  48 8B D3                        mov rdx, rbx
00752722  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00752727  E8 AC 16 1B 00                  call 0x140903dd8
0075272C  85 C0                           test eax, eax
0075272E  78 1A                           js 0x14075274a
00752730  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00752734  85 FF                           test edi, edi
00752736  74 08                           je 0x140752740
00752738  48 85 C0                        test rax, rax
0075273B  74 08                           je 0x140752745
0075273D  48 33 C3                        xor rax, rbx
00752740  48 85 C0                        test rax, rax
00752743  75 19                           jne 0x14075275e
00752745  45 8A C7                        mov r8b, r15b
00752748  EB 1C                           jmp 0x140752766
0075274A  48 8B 03                        mov rax, qword ptr [rbx]
0075274D  85 FF                           test edi, edi
0075274F  74 08                           je 0x140752759
00752751  48 85 C0                        test rax, rax
00752754  74 0D                           je 0x140752763
00752756  48 33 C3                        xor rax, rbx
00752759  48 85 C0                        test rax, rax
0075275C  74 05                           je 0x140752763
0075275E  48 8B D8                        mov rbx, rax
00752761  EB BC                           jmp 0x14075271f
00752763  45 32 C0                        xor r8b, r8b
00752766  4D 8B CE                        mov r9, r14
00752769  48 8B D3                        mov rdx, rbx
0075276C  49 8B CD                        mov rcx, r13
0075276F  E8 FC 1D B9 FF                  call 0x1402e4570
00752774  48 8B 05 05 4C 71 00            mov rax, qword ptr [rip + 0x714c05]
0075277B  48 8B 1D F6 4B 71 00            mov rbx, qword ptr [rip + 0x714bf6]
00752782  4C 8D 2D EF 4B 71 00            lea r13, [rip + 0x714bef]
00752789  41 84 C7                        test r15b, al
0075278C  74 08                           je 0x140752796
0075278E  48 85 DB                        test rbx, rbx
00752791  74 03                           je 0x140752796
00752793  49 33 DD                        xor rbx, r13
00752796  0F B6 F8                        movzx edi, al
00752799  41 23 FF                        and edi, r15d
0075279C  45 32 C0                        xor r8b, r8b
0075279F  48 85 DB                        test rbx, rbx
007527A2  74 49                           je 0x1407527ed
007527A4  49 8D 46 38                     lea rax, [r14 + 0x38]
007527A8  48 8B D3                        mov rdx, rbx
007527AB  48 8B C8                        mov rcx, rax
007527AE  E8 1D D5 20 00                  call 0x14095fcd0
007527B3  85 C0                           test eax, eax
007527B5  78 1A                           js 0x1407527d1
007527B7  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
007527BB  85 FF                           test edi, edi
007527BD  74 08                           je 0x1407527c7
007527BF  48 85 C0                        test rax, rax
007527C2  74 08                           je 0x1407527cc
007527C4  48 33 C3                        xor rax, rbx
007527C7  48 85 C0                        test rax, rax
007527CA  75 19                           jne 0x1407527e5
007527CC  45 8A C7                        mov r8b, r15b
007527CF  EB 1C                           jmp 0x1407527ed
007527D1  48 8B 03                        mov rax, qword ptr [rbx]
007527D4  85 FF                           test edi, edi
007527D6  74 08                           je 0x1407527e0
007527D8  48 85 C0                        test rax, rax
007527DB  74 0D                           je 0x1407527ea
007527DD  48 33 C3                        xor rax, rbx
007527E0  48 85 C0                        test rax, rax
007527E3  74 05                           je 0x1407527ea
007527E5  48 8B D8                        mov rbx, rax
007527E8  EB BA                           jmp 0x1407527a4
007527EA  45 32 C0                        xor r8b, r8b
007527ED  4D 8D 4E 18                     lea r9, [r14 + 0x18]
007527F1  48 8B D3                        mov rdx, rbx
007527F4  49 8B CD                        mov rcx, r13
007527F7  E8 74 1D B9 FF                  call 0x1402e4570
007527FC  48 8D 0D 85 4B 71 00            lea rcx, [rip + 0x714b85]
00752803  E8 80 F5 D3 FF                  call 0x140491d88
00752808  45 33 FF                        xor r15d, r15d
0075280B  45 33 F6                        xor r14d, r14d
0075280E  E9 BB FE FF FF                  jmp 0x1407526ce
00752813  8B F8                           mov edi, eax
00752815  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
0075281D  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00752822  45 8B FE                        mov r15d, r14d
00752825  EB 05                           jmp 0x14075282c
00752827  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
0075282C  45 85 FF                        test r15d, r15d
0075282F  74 0C                           je 0x14075283d
00752831  48 8D 0D 50 4B 71 00            lea rcx, [rip + 0x714b50]
00752838  E8 4B F5 D3 FF                  call 0x140491d88
0075283D  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00752845  48 85 C9                        test rcx, rcx
00752848  74 07                           je 0x140752851
0075284A  33 D2                           xor edx, edx
0075284C  E8 1F 00 43 00                  call 0x140b82870
00752851  4D 85 F6                        test r14, r14
00752854  74 15                           je 0x14075286b
00752856  49 8B CE                        mov rcx, r14
00752859  E8 12 FA FF FF                  call 0x140752270
0075285E  BA 43 63 50 66                  mov edx, 0x66506343
00752863  49 8B CE                        mov rcx, r14
00752866  E8 05 00 43 00                  call 0x140b82870
0075286B  4D 85 E4                        test r12, r12
0075286E  74 0D                           je 0x14075287d
00752870  BA 50 66 57 73                  mov edx, 0x73576650
00752875  49 8B CC                        mov rcx, r12
00752878  E8 63 50 BA FF                  call 0x1402f78e0
0075287D  8B C7                           mov eax, edi
0075287F  48 8B 8C 24 10 02 00 00         mov rcx, qword ptr [rsp + 0x210]
00752887  48 33 CC                        xor rcx, rsp
0075288A  E8 B1 9D F5 FF                  call 0x1406ac640
0075288F  48 8B 9C 24 68 02 00 00         mov rbx, qword ptr [rsp + 0x268]
00752897  48 81 C4 20 02 00 00            add rsp, 0x220
0075289E  41 5F                           pop r15
007528A0  41 5E                           pop r14
007528A2  41 5D                           pop r13
007528A4  41 5C                           pop r12
007528A6  5F                              pop rdi
007528A7  C3                              ret
007528A8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnSetAltPrefetchParam(__int64 a1, __int64 a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned int v_stack_m1D4;
    unsigned int v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (544);
    result = (*(unsigned __int64 *)(v_rip + 7045888)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m1B0 = a2;
    a2 = 0;
    result = memset(v_stack_m188, a2, a2 + 68, a4);
    v_stack_m198 = v_xmm0;
    v_r14 = 0;
    v_stack_m1A0 = 0;
    v_r15 = 0;
    v_stack_m220 = v_stack_m1E0;
    v_stack_m228 = 0x73576650ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, 512, *(unsigned __int64 *)(v_rip + 8865238), a4);
    if (sign_flag) goto loc_00752827;
    if (v_stack_m1E0 == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_00752519;
loc_0075250F:
    goto loc_0075282C;
loc_00752519:
    if (((unsigned int)((unsigned int)(a3))) == 4) goto loc_00752529;
    goto loc_0075282C;
loc_00752529:
    v_stack_m1B0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0)))) > 16) goto loc_0075250F;
    a1 = 0;
    result = PfSnCheckScenario(a1, v_stack_m1C8, *(unsigned __int64 *)(v_rip + 8865238), a4);
    if (sign_flag) goto loc_0075282C;
    result = PfCalculateProcessHash(v_stack_m1E0, v_stack_m1B8, *(unsigned __int64 *)(v_rip + 8865238), a4);
    if (sign_flag) goto loc_0075282C;
    v_stack_m1E0 = 256;
    v_stack_m1F0 = v_stack_m1B8;
    v_stack_m1F8 = v_stack_m1E0;
    v_stack_m200 = v_stack_m1C4;
    v_stack_m208 = v_stack_m138;
    v_stack_m210 = v_stack_m1E0;
    v_stack_m218 = v_stack_m1D4;
    v_stack_m220 = v_stack_m1D0;
    v_stack_m228 = v_stack_m1D8;
    result = PfSnCalculateScenarioNameAndHash(v_stack_m1E0, v_stack_m188, v_stack_m198, v_stack_m1CC);
    if (sign_flag) goto loc_0075282C;
    v_stack_m148 = (unsigned int)((unsigned int)(v_stack_m1D8));
    a3 = (unsigned int)(((unsigned int)(v_stack_m1D4)) + (v_stack_m1D0));
    a3 = (unsigned int)((a3) + (v_stack_m1CC));
    v_stack_m14C = a3;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(256 - 128)), (unsigned int)(0x66506343ULL), v_stack_m1CC);
    if (result != 0) goto loc_0075263D;
    goto loc_0075282C;
loc_0075263D:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0xC000009AULL), v_stack_m1CC);
    *(unsigned int *)(result + 124) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0)));
    *(unsigned __int64 *)(result + 48) = v_stack_m1E0;
    *(unsigned __int64 *)(result + 56) = v_xmm0;
    *(unsigned __int64 *)(result + 72) = v_xmm1;
    *(unsigned __int64 *)(result + 88) = v_xmm0;
    *(unsigned __int64 *)(result + 104) = v_xmm1;
    *(unsigned int *)(result + 120) = (unsigned int)((unsigned int)(v_stack_m148));
    v_r12 = 0;
    result = FsRtlAcquirePushLockExclusive(v_rip + 7425256, a2, (unsigned int)(0xC000009AULL), v_stack_m1CC);
    result = PfSnAltProfileFindByScenarioId(v_stack_m188, a2, (unsigned int)(0xC000009AULL), v_stack_m1CC);
    if (result == 0) goto loc_007526D5;
    if ((*(unsigned __int64 *)(result + 48)) == (*(unsigned __int64 *)(result + 48))) goto loc_007526CB;
    goto loc_0075282C;
loc_007526CB:
    *(unsigned int *)(result + 124) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B0)));
loc_007526CE:
    v_rdi = 0;
    goto loc_0075282C;
loc_007526D5:
    v_stack_m1E0 = *(unsigned __int64 *)(result + 48);
    result = PfSnAltProfileFindByProcess(*(unsigned __int64 *)(result + 48), a2, (unsigned int)(0xC000009AULL), v_stack_m1CC);
    if (result != 0) goto loc_0075250F;
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 7425146)))) == 0) goto loc_00752711;
    v_rbx = *(unsigned __int64 *)(v_rip + 7425131);
    if (*(unsigned __int64 *)(v_rip + 7425131) != 0) {
        v_rbx = (*(unsigned __int64 *)(v_rip + 7425131)) ^ (v_rip + 7425124);
    }
    v_rdi = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_rip + 7425146))) & ((unsigned int)(v_r12 + 1)));
    a3 = 0;
    if (v_rbx == 0) goto loc_00752766;
loc_0075271F:
    result = PfSnAltProfileTreeCompareByProcess(v_stack_m1E0, v_rbx, a3, v_stack_m1CC);
    if (sign_flag) goto loc_0075274A;
    if ((unsigned int)(v_rdi) == 0) goto loc_00752740;
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_00752745;
    result = (*(unsigned __int64 *)(v_rbx + 8)) ^ (v_rbx);
loc_00752740:
    if (result != 0) goto loc_0075275E;
loc_00752745:
    goto loc_00752766;
loc_0075274A:
    if ((unsigned int)(v_rdi) == 0) goto loc_00752759;
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_00752763;
    result = (*(unsigned __int64 *)(v_rbx)) ^ (v_rbx);
loc_00752759:
    if (result == 0) goto loc_00752763;
loc_0075275E:
    goto loc_0075271F;
loc_00752763:
    a3 = 0;
loc_00752766:
    result = RtlRbInsertNodeEx(v_rip + 7425124, result, a3, result);
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 7425029)))) == 0) goto loc_00752796;
    v_rbx = *(unsigned __int64 *)(v_rip + 7425014);
    if (*(unsigned __int64 *)(v_rip + 7425014) != 0) {
        v_rbx = (*(unsigned __int64 *)(v_rip + 7425014)) ^ (v_rip + 7425007);
    }
    v_rdi = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_rip + 7425029))) & ((unsigned int)(v_r12 + 1)));
    a3 = 0;
    if (v_rbx == 0) goto loc_007527ED;
loc_007527A4:
    result = PfSnAltProfileTreeCompareByScenarioId(result + 56, v_rbx, a3, result);
    if (sign_flag) goto loc_007527D1;
    if ((unsigned int)(v_rdi) == 0) goto loc_007527C7;
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_007527CC;
    result = (*(unsigned __int64 *)(v_rbx + 8)) ^ (v_rbx);
loc_007527C7:
    if (result != 0) goto loc_007527E5;
loc_007527CC:
    goto loc_007527ED;
loc_007527D1:
    if ((unsigned int)(v_rdi) == 0) goto loc_007527E0;
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_007527EA;
    result = (*(unsigned __int64 *)(v_rbx)) ^ (v_rbx);
loc_007527E0:
    if (result == 0) goto loc_007527EA;
loc_007527E5:
    goto loc_007527A4;
loc_007527EA:
    a3 = 0;
loc_007527ED:
    result = RtlRbInsertNodeEx(v_rip + 7425007, result, a3, result + 24);
    result = PfLockExclusiveRelease(v_rip + 7424901, result, a3, result + 24);
    v_r15 = 0;
    v_r14 = 0;
    goto loc_007526CE;
loc_00752827:
loc_0075282C:
    if (0 != 0) {
        a1 = v_rip + 7424848;
        result = PfLockExclusiveRelease(a1, result, a3, result + 24);
    }
    if (v_stack_m1B8 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m1B8, a2, a3, result + 24);
    }
    if (0 != 0) {
        a1 = 0;
        result = PfSnAltProfileCleanup(a1, a2, a3, result + 24);
        a2 = 0x66506343ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, result + 24);
    }
    if (v_stack_m1E0 != 0) {
        a2 = 0x73576650ULL;
        a1 = v_stack_m1E0;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, result + 24);
    }
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, result + 24);
    v_rsp = (v_rsp) + (544);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnSetAltPrefetchParam(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint32_t v_stack_m1D4;
    uint32_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m38;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (544);
    result = (*(uint64_t *)(v_rip + 0x6B8300)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m1B0 = Arg2;
    Arg2 = 0;
    result = memset(v_stack_m188, Arg2, Arg2 + 68, Arg4);
    v_stack_m198 = v_xmm0;
    local_r14 = 0;
    v_stack_m1A0 = 0;
    local_r15 = 0;
    v_stack_m220 = v_stack_m1E0;
    v_stack_m228 = 0x73576650ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg1, 512, *(uint64_t *)(v_rip + 0x8745D6), Arg4);
    if (sign_flag) goto loc_00752827;
    if (v_stack_m1E0 == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_00752519;
loc_0075250F:
    goto loc_0075282C;
loc_00752519:
    if (((uint32_t)((uint32_t)(Arg3))) == 4) goto loc_00752529;
    goto loc_0075282C;
loc_00752529:
    v_stack_m1B0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0)))) > 16) goto loc_0075250F;
    Arg1 = 0;
    result = PfSnCheckScenario(Arg1, v_stack_m1C8, *(uint64_t *)(v_rip + 0x8745D6), Arg4);
    if (sign_flag) goto loc_0075282C;
    result = PfCalculateProcessHash(v_stack_m1E0, v_stack_m1B8, *(uint64_t *)(v_rip + 0x8745D6), Arg4);
    if (sign_flag) goto loc_0075282C;
    v_stack_m1E0 = 256;
    v_stack_m1F0 = v_stack_m1B8;
    v_stack_m1F8 = v_stack_m1E0;
    v_stack_m200 = v_stack_m1C4;
    v_stack_m208 = v_stack_m138;
    v_stack_m210 = v_stack_m1E0;
    v_stack_m218 = v_stack_m1D4;
    v_stack_m220 = v_stack_m1D0;
    v_stack_m228 = v_stack_m1D8;
    result = PfSnCalculateScenarioNameAndHash(v_stack_m1E0, v_stack_m188, v_stack_m198, v_stack_m1CC);
    if (sign_flag) goto loc_0075282C;
    v_stack_m148 = (uint32_t)((uint32_t)(v_stack_m1D8));
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m1D4)) + (v_stack_m1D0));
    Arg3 = (uint32_t)((Arg3) + (v_stack_m1CC));
    v_stack_m14C = Arg3;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(256 - 128)), (uint32_t)(0x66506343ULL), v_stack_m1CC);
    if (result != 0) goto loc_0075263D;
    goto loc_0075282C;
loc_0075263D:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0xC000009AULL), v_stack_m1CC);
    *(uint32_t *)(result + 0x7C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0)));
    *(uint64_t *)(result + 0x30) = v_stack_m1E0;
    *(uint64_t *)(result + 0x38) = v_xmm0;
    *(uint64_t *)(result + 0x48) = v_xmm1;
    *(uint64_t *)(result + 0x58) = v_xmm0;
    *(uint64_t *)(result + 0x68) = v_xmm1;
    *(uint32_t *)(result + 0x78) = (uint32_t)((uint32_t)(v_stack_m148));
    local_r12 = 0;
    result = FsRtlAcquirePushLockExclusive(v_rip + 7425256, Arg2, (uint32_t)(0xC000009AULL), v_stack_m1CC);
    result = PfSnAltProfileFindByScenarioId(v_stack_m188, Arg2, (uint32_t)(0xC000009AULL), v_stack_m1CC);
    if (result == 0) goto loc_007526D5;
    if ((*(uint64_t *)(result + 0x30)) == (*(uint64_t *)(result + 0x30))) goto loc_007526CB;
    goto loc_0075282C;
loc_007526CB:
    *(uint32_t *)(result + 0x7C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0)));
loc_007526CE:
    local_rdi = 0;
    goto loc_0075282C;
loc_007526D5:
    v_stack_m1E0 = *(uint64_t *)(result + 0x30);
    result = PfSnAltProfileFindByProcess(*(uint64_t *)(result + 0x30), Arg2, (uint32_t)(0xC000009AULL), v_stack_m1CC);
    if (result != 0) goto loc_0075250F;
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(*(uint64_t *)(v_rip + 0x714C7A)))) == 0) goto loc_00752711;
    local_rbx = *(uint64_t *)(v_rip + 0x714C6B);
    if (*(uint64_t *)(v_rip + 0x714C6B) != 0) {
        local_rbx = (*(uint64_t *)(v_rip + 0x714C6B)) ^ (v_rip + 7425124);
    }
    local_rdi = (uint32_t)(((uint8_t)(*(uint64_t *)(v_rip + 0x714C7A))) & ((uint32_t)(local_r12 + 1)));
    Arg3 = 0;
    if (local_rbx == 0) goto loc_00752766;
loc_0075271F:
    result = PfSnAltProfileTreeCompareByProcess(v_stack_m1E0, local_rbx, Arg3, v_stack_m1CC);
    if (sign_flag) goto loc_0075274A;
    if ((uint32_t)(local_rdi) == 0) goto loc_00752740;
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_00752745;
    result = (*(uint64_t *)(local_rbx + 0x8)) ^ (local_rbx);
loc_00752740:
    if (result != 0) goto loc_0075275E;
loc_00752745:
    goto loc_00752766;
loc_0075274A:
    if ((uint32_t)(local_rdi) == 0) goto loc_00752759;
    if (*(uint64_t *)(local_rbx) == 0) goto loc_00752763;
    result = (*(uint64_t *)(local_rbx)) ^ (local_rbx);
loc_00752759:
    if (result == 0) goto loc_00752763;
loc_0075275E:
    goto loc_0075271F;
loc_00752763:
    Arg3 = 0;
loc_00752766:
    result = RtlRbInsertNodeEx(v_rip + 7425124, result, Arg3, result);
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(*(uint64_t *)(v_rip + 0x714C05)))) == 0) goto loc_00752796;
    local_rbx = *(uint64_t *)(v_rip + 0x714BF6);
    if (*(uint64_t *)(v_rip + 0x714BF6) != 0) {
        local_rbx = (*(uint64_t *)(v_rip + 0x714BF6)) ^ (v_rip + 7425007);
    }
    local_rdi = (uint32_t)(((uint8_t)(*(uint64_t *)(v_rip + 0x714C05))) & ((uint32_t)(local_r12 + 1)));
    Arg3 = 0;
    if (local_rbx == 0) goto loc_007527ED;
loc_007527A4:
    result = PfSnAltProfileTreeCompareByScenarioId(result + 56, local_rbx, Arg3, result);
    if (sign_flag) goto loc_007527D1;
    if ((uint32_t)(local_rdi) == 0) goto loc_007527C7;
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_007527CC;
    result = (*(uint64_t *)(local_rbx + 0x8)) ^ (local_rbx);
loc_007527C7:
    if (result != 0) goto loc_007527E5;
loc_007527CC:
    goto loc_007527ED;
loc_007527D1:
    if ((uint32_t)(local_rdi) == 0) goto loc_007527E0;
    if (*(uint64_t *)(local_rbx) == 0) goto loc_007527EA;
    result = (*(uint64_t *)(local_rbx)) ^ (local_rbx);
loc_007527E0:
    if (result == 0) goto loc_007527EA;
loc_007527E5:
    goto loc_007527A4;
loc_007527EA:
    Arg3 = 0;
loc_007527ED:
    result = RtlRbInsertNodeEx(v_rip + 7425007, result, Arg3, result + 24);
    result = PfLockExclusiveRelease(v_rip + 7424901, result, Arg3, result + 24);
    local_r15 = 0;
    local_r14 = 0;
    goto loc_007526CE;
loc_00752827:
loc_0075282C:
    if (0 != 0) {
        Arg1 = v_rip + 7424848;
        result = PfLockExclusiveRelease(Arg1, result, Arg3, result + 24);
    }
    if (v_stack_m1B8 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m1B8, Arg2, Arg3, result + 24);
    }
    if (0 != 0) {
        Arg1 = 0;
        result = PfSnAltProfileCleanup(Arg1, Arg2, Arg3, result + 24);
        Arg2 = 0x66506343ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, result + 24);
    }
    if (v_stack_m1E0 != 0) {
        Arg2 = 0x73576650ULL;
        Arg1 = v_stack_m1E0;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, result + 24);
    }
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, result + 24);
    local_rsp = (local_rsp) + (544);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00752424&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
