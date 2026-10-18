# AslPathWildcardFindNext

- RVA: `0x0081BB2C`–`0x0081C274` (길이 `1,864` bytes)
- VA: `0x000000014081BB2C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D9D44`
- 디코드: `464`개 명령, `1,864/1,864` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x0081BB9D` → [AslAlloc](../95/AslAlloc_function_0095BD34.md) (function, `0x0095BD34`)
- `0x0081BBE1` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081BC2D` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081BC55` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081BC8F` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081BCB4` → [AslpPathWildcardFreeMatchNode](AslpPathWildcardFreeMatchNode_function_0081C918.md) (function, `0x0081C918`)
- `0x0081BCDA` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081BD17` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081BD34` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081BD5F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0081BD6E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081BDC7` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081BDDF` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081BE02` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0081BE18` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081BE2F` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0081BE48` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081BE5F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0081BE6C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0081BE86` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0081BEC8` → [ZwQueryDirectoryFile](../../text/6A/ZwQueryDirectoryFile_function_006AD770.md) (function, `0x006AD770`)
- `0x0081BEFA` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081BF2A` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081BF9B` → [AslpPathWildcardAllocMatchNode](AslpPathWildcardAllocMatchNode_function_0081C620.md) (function, `0x0081C620`)
- `0x0081C016` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081C031` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081C052` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0081C068` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081C08F` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0081C0A4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0081C0BB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0081C0C8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0081C0E9` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (function, `0x00448380`)
- `0x0081C13B` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081C184` → [RtlStringCbCopyNW](../../text/39/RtlStringCbCopyNW_function_003905E8.md) (function, `0x003905E8`)
- `0x0081C1C0` → [RtlStringCbCatNW](../../text/69/RtlStringCbCatNW_function_0069D224.md) (function, `0x0069D224`)
- `0x0081C1E5` → [RtlStringCbCatNW](../../text/69/RtlStringCbCatNW_function_0069D224.md) (function, `0x0069D224`)
- `0x0081C21D` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081C242` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081C251` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)

### Direct callers
- [SdbpCheckMatchingWildcardFiles](SdbpCheckMatchingWildcardFiles_function_00814E30.md) at `0x00815026`
- [AslPathWildcardFindFirst](AslPathWildcardFindFirst_function_0081B534.md) at `0x0081BA9B`

### Static image references
- `0x0081BC16` → RVA `0x0003F3C8` (`.rdata`; read)
- `0x0081BC23` → RVA `0x0003F2E0` (`.rdata`; read)
- `0x0081BC73` → RVA `0x0003F0D0` (`.rdata`; read)
- `0x0081BC80` → RVA `0x0003F0F8` (`.rdata`; read)
- `0x0081BC94` → RVA `0x0003F140` (`.rdata`; read)
- `0x0081BCA5` → RVA `0x0003F118` (`.rdata`; read)
- `0x0081BEDF` → RVA `0x0003F3F0` (`.rdata`; read)
- `0x0081BF03` → RVA `0x0003F428` (`.rdata`; read)
- `0x0081C124` → RVA `0x0003F448` (`.rdata`; read)
- `0x0081C155` → RVA `0x0003F2B8` (`.rdata`; read)
- `0x0081C18F` → RVA `0x0003F1F8` (`.rdata`; read)
- `0x0081C1B6` → RVA `0x0001BD80` (`.rdata`; read)
- `0x0081C1CB` → RVA `0x0003F478` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **29**
  - `0x0081BBE1` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081BC55` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081BCDA` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081BD17` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081BD34` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081BD5F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0081BD6E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081BDC7` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081BDDF` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081BE02` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0081BE18` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081BE2F` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0081BE48` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081BE5F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0081BE6C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0081BE86` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0081BEC8` → [ZwQueryDirectoryFile](../../text/6A/ZwQueryDirectoryFile_function_006AD770.md) (`PAGE` → `.text`)
  - `0x0081C016` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081C031` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081C052` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0081C068` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081C08F` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0081C0A4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0081C0BB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0081C0C8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0081C0E9` → [ULongLongMult](../../text/44/ULongLongMult_function_00448380.md) (`PAGE` → `.text`)
  - `0x0081C184` → [RtlStringCbCopyNW](../../text/39/RtlStringCbCopyNW_function_003905E8.md) (`PAGE` → `.text`)
  - `0x0081C1C0` → [RtlStringCbCatNW](../../text/69/RtlStringCbCatNW_function_0069D224.md) (`PAGE` → `.text`)
  - `0x0081C1E5` → [RtlStringCbCatNW](../../text/69/RtlStringCbCatNW_function_0069D224.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0081BB2C  48 8B C4                        mov rax, rsp
0081BB2F  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
0081BB33  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0081BB37  48 89 48 08                     mov qword ptr [rax + 8], rcx
0081BB3B  55                              push rbp
0081BB3C  56                              push rsi
0081BB3D  57                              push rdi
0081BB3E  41 54                           push r12
0081BB40  41 55                           push r13
0081BB42  41 56                           push r14
0081BB44  41 57                           push r15
0081BB46  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0081BB4A  48 81 EC A0 00 00 00            sub rsp, 0xa0
0081BB51  49 8B F8                        mov rdi, r8
0081BB54  49 83 F8 FF                     cmp r8, -1
0081BB58  75 0A                           jne 0x14081bb64
0081BB5A  B8 06 00 00 80                  mov eax, 0x80000006
0081BB5F  E9 F4 06 00 00                  jmp 0x14081c258
0081BB64  48 85 C9                        test rcx, rcx
0081BB67  75 0A                           jne 0x14081bb73
0081BB69  B8 EF 00 00 C0                  mov eax, 0xc00000ef
0081BB6E  E9 E5 06 00 00                  jmp 0x14081c258
0081BB73  48 85 FF                        test rdi, rdi
0081BB76  75 0A                           jne 0x14081bb82
0081BB78  B8 F1 00 00 C0                  mov eax, 0xc00000f1
0081BB7D  E9 D6 06 00 00                  jmp 0x14081c258
0081BB82  0F 57 C0                        xorps xmm0, xmm0
0081BB85  0F 57 C9                        xorps xmm1, xmm1
0081BB88  BA 68 02 00 00                  mov edx, 0x268
0081BB8D  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
0081BB91  0F 11 4D E7                     movups xmmword ptr [rbp - 0x19], xmm1
0081BB95  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
0081BB99  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
0081BB9D  E8 92 01 14 00                  call 0x14095bd34
0081BBA2  4C 8B E0                        mov r12, rax
0081BBA5  48 85 C0                        test rax, rax
0081BBA8  75 0A                           jne 0x14081bbb4
0081BBAA  BB 17 00 00 C0                  mov ebx, 0xc0000017
0081BBAF  E9 A2 06 00 00                  jmp 0x14081c256
0081BBB4  41 BD 01 00 00 00               mov r13d, 1
0081BBBA  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0081BBBE  49 3B C5                        cmp rax, r13
0081BBC1  0F 82 82 06 00 00               jb 0x14081c249
0081BBC7  48 8D 50 FF                     lea rdx, [rax - 1]
0081BBCB  48 3B D0                        cmp rdx, rax
0081BBCE  0F 83 32 06 00 00               jae 0x14081c206
0081BBD4  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0081BBD8  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
0081BBDC  48 83 65 6F 00                  and qword ptr [rbp + 0x6f], 0
0081BBE1  E8 9A C7 C2 FF                  call 0x140448380
0081BBE6  85 C0                           test eax, eax
0081BBE8  0F 88 18 06 00 00               js 0x14081c206
0081BBEE  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
0081BBF2  48 8B 75 6F                     mov rsi, qword ptr [rbp + 0x6f]
0081BBF6  48 03 F1                        add rsi, rcx
0081BBF9  48 3B F1                        cmp rsi, rcx
0081BBFC  0F 82 04 06 00 00               jb 0x14081c206
0081BC02  48 85 F6                        test rsi, rsi
0081BC05  0F 84 FB 05 00 00               je 0x14081c206
0081BC0B  48 83 7E 18 00                  cmp qword ptr [rsi + 0x18], 0
0081BC10  0F 85 68 02 00 00               jne 0x14081be7e
0081BC16  4C 8D 0D AB 37 82 FF            lea r9, [rip - 0x7dc855]
0081BC1D  41 B8 CD 09 00 00               mov r8d, 0x9cd
0081BC23  48 8D 15 B6 36 82 FF            lea rdx, [rip - 0x7dc94a]
0081BC2A  41 8B CD                        mov ecx, r13d
0081BC2D  E8 BA 28 14 00                  call 0x14095e4ec
0081BC32  E9 F8 02 00 00                  jmp 0x14081bf2f
0081BC37  BB 1A 00 00 80                  mov ebx, 0x8000001a
0081BC3C  EB 56                           jmp 0x14081bc94
0081BC3E  33 C0                           xor eax, eax
0081BC40  48 8D 51 FF                     lea rdx, [rcx - 1]
0081BC44  48 3B D1                        cmp rdx, rcx
0081BC47  73 25                           jae 0x14081bc6e
0081BC49  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0081BC4D  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
0081BC51  48 21 45 6F                     and qword ptr [rbp + 0x6f], rax
0081BC55  E8 26 C7 C2 FF                  call 0x140448380
0081BC5A  85 C0                           test eax, eax
0081BC5C  78 15                           js 0x14081bc73
0081BC5E  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
0081BC62  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0081BC66  48 03 C1                        add rax, rcx
0081BC69  48 3B C1                        cmp rax, rcx
0081BC6C  72 05                           jb 0x14081bc73
0081BC6E  48 85 C0                        test rax, rax
0081BC71  75 3E                           jne 0x14081bcb1
0081BC73  4C 8D 0D 56 34 82 FF            lea r9, [rip - 0x7dcbaa]
0081BC7A  41 B8 25 08 00 00               mov r8d, 0x825
0081BC80  48 8D 15 71 34 82 FF            lea rdx, [rip - 0x7dcb8f]
0081BC87  41 8B CD                        mov ecx, r13d
0081BC8A  BB E5 00 00 C0                  mov ebx, 0xc00000e5
0081BC8F  E8 58 28 14 00                  call 0x14095e4ec
0081BC94  48 8D 15 A5 34 82 FF            lea rdx, [rip - 0x7dcb5b]
0081BC9B  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0081BC9F  41 B8 40 08 00 00               mov r8d, 0x840
0081BCA5  4C 8D 0D 6C 34 82 FF            lea r9, [rip - 0x7dcb94]
0081BCAC  E9 87 04 00 00                  jmp 0x14081c138
0081BCB1  48 8B C8                        mov rcx, rax
0081BCB4  E8 5F 0C 00 00                  call 0x14081c918
0081BCB9  4C 8B 57 20                     mov r10, qword ptr [rdi + 0x20]
0081BCBD  4D 8D 4A FF                     lea r9, [r10 - 1]
0081BCC1  4D 3B CA                        cmp r9, r10
0081BCC4  0F 83 F0 FE FF FF               jae 0x14081bbba
0081BCCA  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0081BCCE  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
0081BCD2  48 83 65 6F 00                  and qword ptr [rbp + 0x6f], 0
0081BCD7  49 8B D1                        mov rdx, r9
0081BCDA  E8 A1 C6 C2 FF                  call 0x140448380
0081BCDF  85 C0                           test eax, eax
0081BCE1  0F 88 D3 FE FF FF               js 0x14081bbba
0081BCE7  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
0081BCEB  48 8B 75 6F                     mov rsi, qword ptr [rbp + 0x6f]
0081BCEF  48 03 F1                        add rsi, rcx
0081BCF2  48 3B F1                        cmp rsi, rcx
0081BCF5  0F 82 BF FE FF FF               jb 0x14081bbba
0081BCFB  48 8B 5F 20                     mov rbx, qword ptr [rdi + 0x20]
0081BCFF  49 2B D9                        sub rbx, r9
0081BD02  48 83 EB 01                     sub rbx, 1
0081BD06  48 89 5D 77                     mov qword ptr [rbp + 0x77], rbx
0081BD0A  74 58                           je 0x14081bd64
0081BD0C  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0081BD10  4C 8D 45 77                     lea r8, [rbp + 0x77]
0081BD14  48 8B CB                        mov rcx, rbx
0081BD17  E8 64 C6 C2 FF                  call 0x140448380
0081BD1C  85 C0                           test eax, eax
0081BD1E  0F 88 96 FE FF FF               js 0x14081bbba
0081BD24  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0081BD28  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
0081BD2C  48 83 65 6F 00                  and qword ptr [rbp + 0x6f], 0
0081BD31  49 8B D2                        mov rdx, r10
0081BD34  E8 47 C6 C2 FF                  call 0x140448380
0081BD39  85 C0                           test eax, eax
0081BD3B  0F 88 79 FE FF FF               js 0x14081bbba
0081BD41  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
0081BD45  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
0081BD49  48 03 D1                        add rdx, rcx
0081BD4C  48 3B D1                        cmp rdx, rcx
0081BD4F  0F 82 65 FE FF FF               jb 0x14081bbba
0081BD55  48 8B 5D 77                     mov rbx, qword ptr [rbp + 0x77]
0081BD59  48 8B CE                        mov rcx, rsi
0081BD5C  4C 8B C3                        mov r8, rbx
0081BD5F  E8 DC AA EA FF                  call 0x1406c6840
0081BD64  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
0081BD68  48 8D 0C 33                     lea rcx, [rbx + rsi]
0081BD6C  33 D2                           xor edx, edx
0081BD6E  E8 CD AE EA FF                  call 0x1406c6c40
0081BD73  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
0081BD77  49 FF C8                        dec r8
0081BD7A  4C 89 47 20                     mov qword ptr [rdi + 0x20], r8
0081BD7E  49 83 F8 10                     cmp r8, 0x10
0081BD82  0F 86 32 FE FF FF               jbe 0x14081bbba
0081BD88  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0081BD8C  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0081BD90  48 8B C1                        mov rax, rcx
0081BD93  48 0F AF C2                     imul rax, rdx
0081BD97  48 3D 00 04 00 00               cmp rax, 0x400
0081BD9D  0F 82 17 FE FF FF               jb 0x14081bbba
0081BDA3  48 8B C1                        mov rax, rcx
0081BDA6  48 C1 E8 02                     shr rax, 2
0081BDAA  4C 3B C0                        cmp r8, rax
0081BDAD  0F 83 07 FE FF FF               jae 0x14081bbba
0081BDB3  48 83 65 6F 00                  and qword ptr [rbp + 0x6f], 0
0081BDB8  4C 8D 45 77                     lea r8, [rbp + 0x77]
0081BDBC  48 83 65 77 00                  and qword ptr [rbp + 0x77], 0
0081BDC1  48 8B F1                        mov rsi, rcx
0081BDC4  48 D1 EE                        shr rsi, 1
0081BDC7  E8 B4 C5 C2 FF                  call 0x140448380
0081BDCC  85 C0                           test eax, eax
0081BDCE  0F 88 E6 FD FF FF               js 0x14081bbba
0081BDD4  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0081BDD8  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
0081BDDC  48 8B CE                        mov rcx, rsi
0081BDDF  E8 9C C5 C2 FF                  call 0x140448380
0081BDE4  85 C0                           test eax, eax
0081BDE6  0F 88 CE FD FF FF               js 0x14081bbba
0081BDEC  4C 8B 7F 38                     mov r15, qword ptr [rdi + 0x38]
0081BDF0  41 B8 52 54 61 72               mov r8d, 0x72615452
0081BDF6  41 8B CD                        mov ecx, r13d
0081BDF9  4D 85 FF                        test r15, r15
0081BDFC  75 2A                           jne 0x14081be28
0081BDFE  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
0081BE02  E8 09 62 36 00                  call 0x140b82010
0081BE07  48 8B D8                        mov rbx, rax
0081BE0A  48 85 C0                        test rax, rax
0081BE0D  74 0E                           je 0x14081be1d
0081BE0F  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
0081BE13  33 D2                           xor edx, edx
0081BE15  48 8B C8                        mov rcx, rax
0081BE18  E8 23 AE EA FF                  call 0x1406c6c40
0081BE1D  48 85 DB                        test rbx, rbx
0081BE20  0F 84 94 FD FF FF               je 0x14081bbba
0081BE26  EB 49                           jmp 0x14081be71
0081BE28  4C 8B 75 6F                     mov r14, qword ptr [rbp + 0x6f]
0081BE2C  49 8B D6                        mov rdx, r14
0081BE2F  E8 DC 61 36 00                  call 0x140b82010
0081BE34  48 8B D8                        mov rbx, rax
0081BE37  48 85 C0                        test rax, rax
0081BE3A  0F 84 7A FD FF FF               je 0x14081bbba
0081BE40  4D 8B C6                        mov r8, r14
0081BE43  33 D2                           xor edx, edx
0081BE45  48 8B C8                        mov rcx, rax
0081BE48  E8 F3 AD EA FF                  call 0x1406c6c40
0081BE4D  4C 39 75 77                     cmp qword ptr [rbp + 0x77], r14
0081BE51  49 8B D7                        mov rdx, r15
0081BE54  48 8B CB                        mov rcx, rbx
0081BE57  4C 0F 42 75 77                  cmovb r14, qword ptr [rbp + 0x77]
0081BE5C  4D 8B C6                        mov r8, r14
0081BE5F  E8 DC A9 EA FF                  call 0x1406c6840
0081BE64  BA 52 54 61 72                  mov edx, 0x72615452
0081BE69  49 8B CF                        mov rcx, r15
0081BE6C  E8 FF 69 36 00                  call 0x140b82870
0081BE71  48 89 5F 38                     mov qword ptr [rdi + 0x38], rbx
0081BE75  48 89 77 28                     mov qword ptr [rdi + 0x28], rsi
0081BE79  E9 3C FD FF FF                  jmp 0x14081bbba
0081BE7E  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
0081BE82  48 8D 4D E7                     lea rcx, [rbp - 0x19]
0081BE86  E8 F5 E8 C0 FF                  call 0x14042a780
0081BE8B  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
0081BE8F  48 8D 45 E7                     lea rax, [rbp - 0x19]
0081BE93  C6 44 24 50 00                  mov byte ptr [rsp + 0x50], 0
0081BE98  45 33 C9                        xor r9d, r9d
0081BE9B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0081BEA0  45 33 C0                        xor r8d, r8d
0081BEA3  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
0081BEA8  48 8D 45 F7                     lea rax, [rbp - 9]
0081BEAC  C7 44 24 38 03 00 00 00         mov dword ptr [rsp + 0x38], 3
0081BEB4  33 D2                           xor edx, edx
0081BEB6  C7 44 24 30 68 02 00 00         mov dword ptr [rsp + 0x30], 0x268
0081BEBE  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0081BEC3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0081BEC8  E8 A3 18 E9 FF                  call 0x1406ad770
0081BECD  85 C0                           test eax, eax
0081BECF  79 70                           jns 0x14081bf41
0081BED1  3D 06 00 00 80                  cmp eax, 0x80000006
0081BED6  74 57                           je 0x14081bf2f
0081BED8  3D 0F 00 00 C0                  cmp eax, 0xc000000f
0081BEDD  74 50                           je 0x14081bf2f
0081BEDF  4C 8D 0D 0A 35 82 FF            lea r9, [rip - 0x7dcaf6]
0081BEE6  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0081BEEA  41 B8 E5 09 00 00               mov r8d, 0x9e5
0081BEF0  48 8D 15 E9 33 82 FF            lea rdx, [rip - 0x7dcc17]
0081BEF7  41 8B CD                        mov ecx, r13d
0081BEFA  E8 ED 25 14 00                  call 0x14095e4ec
0081BEFF  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
0081BF03  4C 8D 0D 1E 35 82 FF            lea r9, [rip - 0x7dcae2]
0081BF0A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0081BF0F  48 8D 15 CA 33 82 FF            lea rdx, [rip - 0x7dcc36]
0081BF16  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0081BF1A  41 B8 E6 09 00 00               mov r8d, 0x9e6
0081BF20  B9 02 00 00 00                  mov ecx, 2
0081BF25  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0081BF2A  E8 BD 25 14 00                  call 0x14095e4ec
0081BF2F  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0081BF33  49 3B CD                        cmp rcx, r13
0081BF36  0F 82 FB FC FF FF               jb 0x14081bc37
0081BF3C  E9 FD FC FF FF                  jmp 0x14081bc3e
0081BF41  41 8B 44 24 3C                  mov eax, dword ptr [r12 + 0x3c]
0081BF46  83 F8 04                        cmp eax, 4
0081BF49  75 12                           jne 0x14081bf5d
0081BF4B  66 41 83 7C 24 5E 2E            cmp word ptr [r12 + 0x5e], 0x2e
0081BF52  75 1B                           jne 0x14081bf6f
0081BF54  66 41 83 7C 24 60 2E            cmp word ptr [r12 + 0x60], 0x2e
0081BF5B  EB 0C                           jmp 0x14081bf69
0081BF5D  83 F8 02                        cmp eax, 2
0081BF60  75 0D                           jne 0x14081bf6f
0081BF62  66 41 83 7C 24 5E 2E            cmp word ptr [r12 + 0x5e], 0x2e
0081BF69  0F 84 4B FC FF FF               je 0x14081bbba
0081BF6F  45 8B 4C 24 38                  mov r9d, dword ptr [r12 + 0x38]
0081BF74  4D 8D 74 24 5E                  lea r14, [r12 + 0x5e]
0081BF79  41 0F B7 44 24 3C               movzx eax, word ptr [r12 + 0x3c]
0081BF7F  48 8D 4D 07                     lea rcx, [rbp + 7]
0081BF83  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
0081BF87  48 8B D6                        mov rdx, rsi
0081BF8A  41 C1 E9 04                     shr r9d, 4
0081BF8E  66 89 44 24 28                  mov word ptr [rsp + 0x28], ax
0081BF93  45 23 CD                        and r9d, r13d
0081BF96  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0081BF9B  E8 80 06 00 00                  call 0x14081c620
0081BFA0  3D 73 02 00 C0                  cmp eax, 0xc0000273
0081BFA5  0F 84 C5 01 00 00               je 0x14081c170
0081BFAB  3D 03 01 00 C0                  cmp eax, 0xc0000103
0081BFB0  0F 84 04 FC FF FF               je 0x14081bbba
0081BFB6  3D BA 00 00 C0                  cmp eax, 0xc00000ba
0081BFBB  0F 84 F9 FB FF FF               je 0x14081bbba
0081BFC1  85 C0                           test eax, eax
0081BFC3  0F 88 57 01 00 00               js 0x14081c120
0081BFC9  4C 8B 6F 20                     mov r13, qword ptr [rdi + 0x20]
0081BFCD  4C 8B 4F 28                     mov r9, qword ptr [rdi + 0x28]
0081BFD1  4D 3B E9                        cmp r13, r9
0081BFD4  0F 82 FF 00 00 00               jb 0x14081c0d9
0081BFDA  49 8D 4D 01                     lea rcx, [r13 + 1]
0081BFDE  49 3B C9                        cmp rcx, r9
0081BFE1  0F 86 5E 01 00 00               jbe 0x14081c145
0081BFE7  48 8B 77 30                     mov rsi, qword ptr [rdi + 0x30]
0081BFEB  48 FF CE                        dec rsi
0081BFEE  48 8D 04 0E                     lea rax, [rsi + rcx]
0081BFF2  48 3B C1                        cmp rax, rcx
0081BFF5  0F 82 53 01 00 00               jb 0x14081c14e
0081BFFB  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0081BFFF  4C 8D 45 77                     lea r8, [rbp + 0x77]
0081C003  48 83 65 77 00                  and qword ptr [rbp + 0x77], 0
0081C008  48 F7 D6                        not rsi
0081C00B  48 83 65 6F 00                  and qword ptr [rbp + 0x6f], 0
0081C010  49 8B C9                        mov rcx, r9
0081C013  48 23 F0                        and rsi, rax
0081C016  E8 65 C3 C2 FF                  call 0x140448380
0081C01B  85 C0                           test eax, eax
0081C01D  79 07                           jns 0x14081c026
0081C01F  BB 95 00 00 C0                  mov ebx, 0xc0000095
0081C024  EB 51                           jmp 0x14081c077
0081C026  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0081C02A  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
0081C02E  48 8B CE                        mov rcx, rsi
0081C031  E8 4A C3 C2 FF                  call 0x140448380
0081C036  85 C0                           test eax, eax
0081C038  78 E5                           js 0x14081c01f
0081C03A  4C 8B 7F 38                     mov r15, qword ptr [rdi + 0x38]
0081C03E  41 B8 52 54 61 72               mov r8d, 0x72615452
0081C044  B9 01 00 00 00                  mov ecx, 1
0081C049  4D 85 FF                        test r15, r15
0081C04C  75 3A                           jne 0x14081c088
0081C04E  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
0081C052  E8 B9 5F 36 00                  call 0x140b82010
0081C057  48 8B D8                        mov rbx, rax
0081C05A  48 85 C0                        test rax, rax
0081C05D  74 0E                           je 0x14081c06d
0081C05F  4C 8B 45 6F                     mov r8, qword ptr [rbp + 0x6f]
0081C063  33 D2                           xor edx, edx
0081C065  48 8B C8                        mov rcx, rax
0081C068  E8 D3 AB EA FF                  call 0x1406c6c40
0081C06D  48 85 DB                        test rbx, rbx
0081C070  75 5B                           jne 0x14081c0cd
0081C072  BB 17 00 00 C0                  mov ebx, 0xc0000017
0081C077  85 DB                           test ebx, ebx
0081C079  74 5E                           je 0x14081c0d9
0081C07B  8B C3                           mov eax, ebx
0081C07D  0F 88 D2 00 00 00               js 0x14081c155
0081C083  E9 2C FB FF FF                  jmp 0x14081bbb4
0081C088  4C 8B 75 6F                     mov r14, qword ptr [rbp + 0x6f]
0081C08C  49 8B D6                        mov rdx, r14
0081C08F  E8 7C 5F 36 00                  call 0x140b82010
0081C094  48 8B D8                        mov rbx, rax
0081C097  48 85 C0                        test rax, rax
0081C09A  74 D6                           je 0x14081c072
0081C09C  4D 8B C6                        mov r8, r14
0081C09F  33 D2                           xor edx, edx
0081C0A1  48 8B C8                        mov rcx, rax
0081C0A4  E8 97 AB EA FF                  call 0x1406c6c40
0081C0A9  4C 39 75 77                     cmp qword ptr [rbp + 0x77], r14
0081C0AD  49 8B D7                        mov rdx, r15
0081C0B0  48 8B CB                        mov rcx, rbx
0081C0B3  4C 0F 42 75 77                  cmovb r14, qword ptr [rbp + 0x77]
0081C0B8  4D 8B C6                        mov r8, r14
0081C0BB  E8 80 A7 EA FF                  call 0x1406c6840
0081C0C0  BA 52 54 61 72                  mov edx, 0x72615452
0081C0C5  49 8B CF                        mov rcx, r15
0081C0C8  E8 A3 67 36 00                  call 0x140b82870
0081C0CD  48 89 5F 38                     mov qword ptr [rdi + 0x38], rbx
0081C0D1  33 DB                           xor ebx, ebx
0081C0D3  48 89 77 28                     mov qword ptr [rdi + 0x28], rsi
0081C0D7  EB 9E                           jmp 0x14081c077
0081C0D9  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0081C0DD  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
0081C0E1  48 83 65 6F 00                  and qword ptr [rbp + 0x6f], 0
0081C0E6  49 8B D5                        mov rdx, r13
0081C0E9  E8 92 C2 C2 FF                  call 0x140448380
0081C0EE  85 C0                           test eax, eax
0081C0F0  78 5C                           js 0x14081c14e
0081C0F2  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
0081C0F6  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
0081C0FA  48 03 D1                        add rdx, rcx
0081C0FD  48 3B D1                        cmp rdx, rcx
0081C100  72 4C                           jb 0x14081c14e
0081C102  0F 10 45 07                     movups xmm0, xmmword ptr [rbp + 7]
0081C106  41 BD 01 00 00 00               mov r13d, 1
0081C10C  0F 11 02                        movups xmmword ptr [rdx], xmm0
0081C10F  0F 10 4D 17                     movups xmm1, xmmword ptr [rbp + 0x17]
0081C113  0F 11 4A 10                     movups xmmword ptr [rdx + 0x10], xmm1
0081C117  4C 01 6F 20                     add qword ptr [rdi + 0x20], r13
0081C11B  E9 9A FA FF FF                  jmp 0x14081bbba
0081C120  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0081C124  4C 8D 0D 1D 33 82 FF            lea r9, [rip - 0x7dcce3]
0081C12B  41 B8 1F 0A 00 00               mov r8d, 0xa1f
0081C131  48 8D 15 A8 31 82 FF            lea rdx, [rip - 0x7dce58]
0081C138  41 8B CD                        mov ecx, r13d
0081C13B  E8 AC 23 14 00                  call 0x14095e4ec
0081C140  E9 75 FA FF FF                  jmp 0x14081bbba
0081C145  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0081C14A  8B C3                           mov eax, ebx
0081C14C  EB 07                           jmp 0x14081c155
0081C14E  B8 95 00 00 C0                  mov eax, 0xc0000095
0081C153  8B D8                           mov ebx, eax
0081C155  4C 8D 0D 5C 31 82 FF            lea r9, [rip - 0x7dcea4]
0081C15C  41 B8 17 0A 00 00               mov r8d, 0xa17
0081C162  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0081C166  B9 01 00 00 00                  mov ecx, 1
0081C16B  E9 CB 00 00 00                  jmp 0x14081c23b
0081C170  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
0081C174  BA 08 02 00 00                  mov edx, 0x208
0081C179  44 0F B7 0E                     movzx r9d, word ptr [rsi]
0081C17D  49 8B CD                        mov rcx, r13
0081C180  4C 8B 46 08                     mov r8, qword ptr [rsi + 8]
0081C184  E8 5F 44 B7 FF                  call 0x1403905e8
0081C189  8B D8                           mov ebx, eax
0081C18B  85 C0                           test eax, eax
0081C18D  79 0F                           jns 0x14081c19e
0081C18F  4C 8D 0D 62 30 82 FF            lea r9, [rip - 0x7dcf9e]
0081C196  41 B8 2F 0A 00 00               mov r8d, 0xa2f
0081C19C  EB C4                           jmp 0x14081c162
0081C19E  0F B7 0E                        movzx ecx, word ptr [rsi]
0081C1A1  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0081C1A5  48 D1 E9                        shr rcx, 1
0081C1A8  66 83 7C 48 FE 5C               cmp word ptr [rax + rcx*2 - 2], 0x5c
0081C1AE  74 2A                           je 0x14081c1da
0081C1B0  41 B9 02 00 00 00               mov r9d, 2
0081C1B6  4C 8D 05 C3 FB 7F FF            lea r8, [rip - 0x80043d]
0081C1BD  49 8B CD                        mov rcx, r13
0081C1C0  E8 5F 10 E8 FF                  call 0x14069d224
0081C1C5  8B D8                           mov ebx, eax
0081C1C7  85 C0                           test eax, eax
0081C1C9  79 0F                           jns 0x14081c1da
0081C1CB  4C 8D 0D A6 32 82 FF            lea r9, [rip - 0x7dcd5a]
0081C1D2  41 B8 36 0A 00 00               mov r8d, 0xa36
0081C1D8  EB 88                           jmp 0x14081c162
0081C1DA  45 8B 4C 24 3C                  mov r9d, dword ptr [r12 + 0x3c]
0081C1DF  4D 8B C6                        mov r8, r14
0081C1E2  49 8B CD                        mov rcx, r13
0081C1E5  E8 3A 10 E8 FF                  call 0x14069d224
0081C1EA  8B D8                           mov ebx, eax
0081C1EC  85 C0                           test eax, eax
0081C1EE  79 12                           jns 0x14081c202
0081C1F0  4C 8D 0D 81 32 82 FF            lea r9, [rip - 0x7dcd7f]
0081C1F7  41 B8 3D 0A 00 00               mov r8d, 0xa3d
0081C1FD  E9 60 FF FF FF                  jmp 0x14081c162
0081C202  33 DB                           xor ebx, ebx
0081C204  EB 48                           jmp 0x14081c24e
0081C206  4C 8D 0D C3 2E 82 FF            lea r9, [rip - 0x7dd13d]
0081C20D  41 B8 25 08 00 00               mov r8d, 0x825
0081C213  48 8D 15 DE 2E 82 FF            lea rdx, [rip - 0x7dd122]
0081C21A  41 8B CD                        mov ecx, r13d
0081C21D  E8 CA 22 14 00                  call 0x14095e4ec
0081C222  BB E5 00 00 C0                  mov ebx, 0xc00000e5
0081C227  4C 8D 0D EA 2E 82 FF            lea r9, [rip - 0x7dd116]
0081C22E  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0081C232  41 B8 C8 09 00 00               mov r8d, 0x9c8
0081C238  41 8B CD                        mov ecx, r13d
0081C23B  48 8D 15 9E 30 82 FF            lea rdx, [rip - 0x7dcf62]
0081C242  E8 A5 22 14 00                  call 0x14095e4ec
0081C247  EB 05                           jmp 0x14081c24e
0081C249  BB 06 00 00 80                  mov ebx, 0x80000006
0081C24E  49 8B D4                        mov rdx, r12
0081C251  E8 1E F4 13 00                  call 0x14095b674
0081C256  8B C3                           mov eax, ebx
0081C258  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
0081C260  48 81 C4 A0 00 00 00            add rsp, 0xa0
0081C267  41 5F                           pop r15
0081C269  41 5E                           pop r14
0081C26B  41 5D                           pop r13
0081C26D  41 5C                           pop r12
0081C26F  5F                              pop rdi
0081C270  5E                              pop rsi
0081C271  5D                              pop rbp
0081C272  C3                              ret
0081C273  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AslPathWildcardFindNext(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int8 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    if (a3 != -1) goto loc_0081BB64;
    goto loc_0081C258;
loc_0081BB64:
    if (a1 != 0) goto loc_0081BB73;
    goto loc_0081C258;
loc_0081BB73:
    if (a3 != 0) goto loc_0081BB82;
    goto loc_0081C258;
loc_0081BB82:
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm0;
    result = AslAlloc(a1, 616, a3, a4);
    if (result != 0) goto loc_0081BBB4;
    goto loc_0081C256;
loc_0081BBB4:
loc_0081BBBA:
    if ((*(unsigned __int64 *)(a3 + 32)) < 1) goto loc_0081C249;
    if ((*(unsigned __int64 *)(a3 + 32) - 1) >= (*(unsigned __int64 *)(a3 + 32))) goto loc_0081C206;
    result = ULongLongMult(*(unsigned __int64 *)(a3 + 24), *(unsigned __int64 *)(a3 + 32) - 1, v_rsp - 95 + 111, a4);
    if (sign_flag) goto loc_0081C206;
    v_rsi = (*(unsigned __int64 *)(v_rsp - 95 + 111)) + (*(unsigned __int64 *)(a3 + 56));
    if (v_rsi < (*(unsigned __int64 *)(a3 + 56))) goto loc_0081C206;
    if (v_rsi == 0) goto loc_0081C206;
    if ((*(unsigned __int64 *)(v_rsi + 24)) != 0) goto loc_0081BE7E;
    result = AslLogCallPrintf(1, v_rip - 8243530, (unsigned int)(0x9CDULL), v_rip - 8243285);
    goto loc_0081BF2F;
loc_0081BC37:
    goto loc_0081BC94;
loc_0081BC3E:
    result = 0;
    if ((1 - 1) >= 1) goto loc_0081BC6E;
    result = ULongLongMult(*(unsigned __int64 *)(a3 + 24), 1 - 1, v_rsp - 95 + 111, v_rip - 8243285);
    if (sign_flag) goto loc_0081BC73;
    result = (*(unsigned __int64 *)(v_rsp - 95 + 111)) + (*(unsigned __int64 *)(a3 + 56));
    if (result < (*(unsigned __int64 *)(a3 + 56))) goto loc_0081BC73;
loc_0081BC6E:
    if (result != 0) goto loc_0081BCB1;
loc_0081BC73:
    result = AslLogCallPrintf(1, v_rip - 8244111, (unsigned int)(0x825ULL), v_rip - 8244138);
loc_0081BC94:
    v_stack_mB8 = (unsigned int)((unsigned int)(0xC00000E5ULL));
    goto loc_0081C138;
loc_0081BCB1:
    result = AslpPathWildcardFreeMatchNode(result, v_rip - 8244059, (unsigned int)(0x840ULL), v_rip - 8244116);
    if ((*(unsigned __int64 *)(a3 + 32) - 1) >= (*(unsigned __int64 *)(a3 + 32))) goto loc_0081BBBA;
    result = ULongLongMult(*(unsigned __int64 *)(a3 + 24), *(unsigned __int64 *)(a3 + 32) - 1, v_rsp - 95 + 111, *(unsigned __int64 *)(a3 + 32) - 1);
    if (sign_flag) goto loc_0081BBBA;
    v_rsi = (*(unsigned __int64 *)(v_rsp - 95 + 111)) + (*(unsigned __int64 *)(a3 + 56));
    if (v_rsi < (*(unsigned __int64 *)(a3 + 56))) goto loc_0081BBBA;
    v_rbx = (*(unsigned __int64 *)(a3 + 32)) - (*(unsigned __int64 *)(a3 + 32) - 1);
    v_rbx = (v_rbx) - (1);
    *(unsigned __int64 *)(v_rsp - 95 + 119) = v_rbx;
    if (condition_is_equal) goto loc_0081BD64;
    result = ULongLongMult(v_rbx, *(unsigned __int64 *)(a3 + 24), v_rsp - 95 + 119, *(unsigned __int64 *)(a3 + 32) - 1);
    if (sign_flag) goto loc_0081BBBA;
    result = ULongLongMult(*(unsigned __int64 *)(a3 + 24), *(unsigned __int64 *)(a3 + 32), v_rsp - 95 + 111, *(unsigned __int64 *)(a3 + 32) - 1);
    if (sign_flag) goto loc_0081BBBA;
    a2 = (*(unsigned __int64 *)(v_rsp - 95 + 111)) + (*(unsigned __int64 *)(a3 + 56));
    if (a2 < (*(unsigned __int64 *)(a3 + 56))) goto loc_0081BBBA;
    result = memcpy(v_rsi, a2, *(unsigned __int64 *)(v_rsp - 95 + 119), *(unsigned __int64 *)(a3 + 32) - 1);
loc_0081BD64:
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rsp - 95 + 119) + v_rsi * 1, a2, *(unsigned __int64 *)(a3 + 24), *(unsigned __int64 *)(a3 + 32) - 1);
    a3 = (*(unsigned __int64 *)(a3 + 32)) - 1;
    *(unsigned __int64 *)(a3 + 32) = a3;
    if (a3 <= 16) goto loc_0081BBBA;
    result = (*(unsigned __int64 *)(a3 + 40)) * (*(unsigned __int64 *)(a3 + 24));
    if (result < 0x400ULL) goto loc_0081BBBA;
    result = (*(unsigned __int64 *)(a3 + 40)) >> (2);
    if (a3 >= result) goto loc_0081BBBA;
    v_rsi = (*(unsigned __int64 *)(a3 + 40)) >> (1);
    result = ULongLongMult(*(unsigned __int64 *)(a3 + 40), *(unsigned __int64 *)(a3 + 24), v_rsp - 95 + 119, *(unsigned __int64 *)(a3 + 32) - 1);
    if (sign_flag) goto loc_0081BBBA;
    result = ULongLongMult(v_rsi, *(unsigned __int64 *)(a3 + 24), v_rsp - 95 + 111, *(unsigned __int64 *)(a3 + 32) - 1);
    if (sign_flag) goto loc_0081BBBA;
    if (*(unsigned __int64 *)(a3 + 56) != 0) goto loc_0081BE28;
    result = ExAllocatePoolWithTag(1, *(unsigned __int64 *)(v_rsp - 95 + 111), (unsigned int)(0x72615452ULL), *(unsigned __int64 *)(a3 + 32) - 1);
    if (result != 0) {
        a3 = *(unsigned __int64 *)(v_rsp - 95 + 111);
        a2 = 0;
        a1 = result;
        result = memset(a1, a2, a3, *(unsigned __int64 *)(a3 + 32) - 1);
    }
    if (result == 0) goto loc_0081BBBA;
    goto loc_0081BE71;
loc_0081BE28:
    result = ExAllocatePoolWithTag(a1, *(unsigned __int64 *)(v_rsp - 95 + 111), a3, *(unsigned __int64 *)(a3 + 32) - 1);
    if (result == 0) goto loc_0081BBBA;
    a2 = 0;
    result = memset(result, a2, *(unsigned __int64 *)(v_rsp - 95 + 111), *(unsigned __int64 *)(a3 + 32) - 1);
    v_r14 = *(unsigned __int64 *)(v_rsp - 95 + 111);
    if ((*(unsigned __int64 *)(v_rsp - 95 + 119)) < (*(unsigned __int64 *)(v_rsp - 95 + 111))) { v_r14 = *(unsigned __int64 *)(v_rsp - 95 + 119); }
    result = memcpy(result, *(unsigned __int64 *)(a3 + 56), v_r14, *(unsigned __int64 *)(a3 + 32) - 1);
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a3 + 56), (unsigned int)(0x72615452ULL), v_r14, *(unsigned __int64 *)(a3 + 32) - 1);
loc_0081BE71:
    *(unsigned __int64 *)(a3 + 56) = result;
    *(unsigned __int64 *)(a3 + 40) = v_rsi;
    goto loc_0081BBBA;
loc_0081BE7E:
    result = RtlInitUnicodeString(v_rsp - 95 - 25, *(unsigned __int64 *)(v_rsi + 16), v_r14, *(unsigned __int64 *)(a3 + 32) - 1);
    v_stack_m88 = 0;
    a4 = 0;
    v_stack_m90 = v_rsp - 95 - 25;
    a3 = 0;
    v_stack_m98 = 1;
    v_stack_mA0 = 3;
    a2 = 0;
    v_stack_mA8 = 616;
    v_stack_mB0 = result;
    v_stack_mB8 = v_rsp - 95 - 9;
    result = ZwQueryDirectoryFile(*(unsigned __int64 *)(v_rsi + 24), a2, a3, a4);
    if (!sign_flag) goto loc_0081BF41;
    if (((unsigned int)(result)) == 0x80000006ULL) goto loc_0081BF2F;
    if (((unsigned int)(result)) != 0xC000000FULL) {
        a4 = v_rip - 8243958;
        v_stack_mB8 = (unsigned int)(result);
        a3 = 0x9E5ULL;
        a2 = v_rip - 8244247;
        a1 = 1;
        result = AslLogCallPrintf(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(v_rsp - 95 - 17);
        a4 = v_rip - 8243938;
        v_stack_mB0 = result;
        a2 = v_rip - 8244278;
        result = *(unsigned __int64 *)(v_rsi + 8);
        a3 = 0x9E6ULL;
        a1 = 2;
        v_stack_mB8 = result;
        result = AslLogCallPrintf(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(a3 + 32)) < 1) goto loc_0081BC37;
    goto loc_0081BC3E;
loc_0081BF41:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 60)))) != 4) goto loc_0081BF5D;
    if ((*(unsigned __int16 *)(result + 94)) != 46) goto loc_0081BF6F;
    goto loc_0081BF69;
loc_0081BF5D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 60)))) != 2) goto loc_0081BF6F;
loc_0081BF69:
    if ((*(unsigned __int16 *)(result + 94)) == 46) goto loc_0081BBBA;
loc_0081BF6F:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 56))) >> (4));
    v_stack_mB0 = (unsigned __int16)(*(unsigned __int16 *)(result + 60));
    a4 = (unsigned int)((a4) & (1));
    v_stack_mB8 = result + 94;
    result = AslpPathWildcardAllocMatchNode(v_rsp - 95 + 7, v_rsi, *(unsigned __int64 *)(v_rsi + 16), a4);
    if (((unsigned int)(result)) == 0xC0000273ULL) goto loc_0081C170;
    if (((unsigned int)(result)) == 0xC0000103ULL) goto loc_0081BBBA;
    if (((unsigned int)(result)) == 0xC00000BAULL) goto loc_0081BBBA;
    if (sign_flag) goto loc_0081C120;
    if ((*(unsigned __int64 *)(a3 + 32)) < (*(unsigned __int64 *)(a3 + 40))) goto loc_0081C0D9;
    if ((*(unsigned __int64 *)(a3 + 32) + 1) <= (*(unsigned __int64 *)(a3 + 40))) goto loc_0081C145;
    v_rsi = (*(unsigned __int64 *)(a3 + 48)) - 1;
    if ((v_rsi + *(unsigned __int64 *)(a3 + 32) + 1 * 1) < (*(unsigned __int64 *)(a3 + 32) + 1)) goto loc_0081C14E;
    v_rsi = ~(v_rsi);
    v_rsi = (v_rsi) & (v_rsi + *(unsigned __int64 *)(a3 + 32) + 1 * 1);
    result = ULongLongMult(*(unsigned __int64 *)(a3 + 40), *(unsigned __int64 *)(a3 + 24), v_rsp - 95 + 119, *(unsigned __int64 *)(a3 + 40));
    if (!sign_flag) goto loc_0081C026;
loc_0081C01F:
    goto loc_0081C077;
loc_0081C026:
    result = ULongLongMult(v_rsi, *(unsigned __int64 *)(a3 + 24), v_rsp - 95 + 111, *(unsigned __int64 *)(a3 + 40));
    if (sign_flag) goto loc_0081C01F;
    if (*(unsigned __int64 *)(a3 + 56) != 0) goto loc_0081C088;
    result = ExAllocatePoolWithTag(1, *(unsigned __int64 *)(v_rsp - 95 + 111), (unsigned int)(0x72615452ULL), *(unsigned __int64 *)(a3 + 40));
    if (result != 0) {
        a3 = *(unsigned __int64 *)(v_rsp - 95 + 111);
        a2 = 0;
        a1 = result;
        result = memset(a1, a2, a3, *(unsigned __int64 *)(a3 + 40));
    }
    if (result != 0) goto loc_0081C0CD;
loc_0081C072:
loc_0081C077:
    if ((unsigned int)((unsigned int)(0xC0000017ULL)) == 0) goto loc_0081C0D9;
    if (sign_flag) goto loc_0081C155;
    goto loc_0081BBB4;
loc_0081C088:
    result = ExAllocatePoolWithTag(a1, *(unsigned __int64 *)(v_rsp - 95 + 111), a3, *(unsigned __int64 *)(a3 + 40));
    if (result == 0) goto loc_0081C072;
    a2 = 0;
    result = memset(result, a2, *(unsigned __int64 *)(v_rsp - 95 + 111), *(unsigned __int64 *)(a3 + 40));
    v_r14 = *(unsigned __int64 *)(v_rsp - 95 + 111);
    if ((*(unsigned __int64 *)(v_rsp - 95 + 119)) < (*(unsigned __int64 *)(v_rsp - 95 + 111))) { v_r14 = *(unsigned __int64 *)(v_rsp - 95 + 119); }
    result = memcpy(result, *(unsigned __int64 *)(a3 + 56), v_r14, *(unsigned __int64 *)(a3 + 40));
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a3 + 56), (unsigned int)(0x72615452ULL), v_r14, *(unsigned __int64 *)(a3 + 40));
loc_0081C0CD:
    *(unsigned __int64 *)(a3 + 56) = result;
    v_rbx = 0;
    *(unsigned __int64 *)(a3 + 40) = v_rsi;
    goto loc_0081C077;
loc_0081C0D9:
    result = ULongLongMult(*(unsigned __int64 *)(a3 + 24), *(unsigned __int64 *)(a3 + 32), v_rsp - 95 + 111, *(unsigned __int64 *)(a3 + 40));
    if (sign_flag) goto loc_0081C14E;
    a2 = (*(unsigned __int64 *)(v_rsp - 95 + 111)) + (*(unsigned __int64 *)(a3 + 56));
    if (a2 < (*(unsigned __int64 *)(a3 + 56))) goto loc_0081C14E;
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int64 *)(a2 + 16) = v_xmm1;
    goto loc_0081BBBA;
loc_0081C120:
    v_stack_mB8 = (unsigned int)(result);
loc_0081C138:
    result = AslLogCallPrintf(1, v_rip - 8244824, (unsigned int)(0xA1FULL), v_rip - 8244451);
    goto loc_0081BBBA;
loc_0081C145:
    goto loc_0081C155;
loc_0081C14E:
loc_0081C155:
loc_0081C162:
    v_stack_mB8 = (unsigned int)((unsigned int)(0xC0000095ULL));
    goto loc_0081C23B;
loc_0081C170:
    result = RtlStringCbCopyNW(*(unsigned __int64 *)(v_rsp - 95 + 103), 520, *(unsigned __int64 *)(v_rsi + 8), *(unsigned __int16 *)(v_rsi));
    if (!sign_flag) goto loc_0081C19E;
    goto loc_0081C162;
loc_0081C19E:
    a1 = (*(unsigned __int16 *)(v_rsi)) >> (1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsi + 8) + a1 * 2 - 2)) == 92) goto loc_0081C1DA;
    result = RtlStringCbCatNW(*(unsigned __int64 *)(v_rsp - 95 + 103), 520, v_rip - 8389693, 2);
    if (!sign_flag) goto loc_0081C1DA;
    goto loc_0081C162;
loc_0081C1DA:
    result = RtlStringCbCatNW(*(unsigned __int64 *)(v_rsp - 95 + 103), 520, v_r14, (unsigned int)(*(unsigned int *)(result + 60)));
    if (!sign_flag) goto loc_0081C202;
    goto loc_0081C162;
loc_0081C202:
    v_rbx = 0;
    goto loc_0081C24E;
loc_0081C206:
    result = AslLogCallPrintf((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 103))), v_rip - 8245538, (unsigned int)(0x825ULL), v_rip - 8245565);
    v_stack_mB8 = (unsigned int)((unsigned int)(0xC00000E5ULL));
loc_0081C23B:
    result = AslLogCallPrintf((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 103))), v_rip - 8245090, (unsigned int)(0x9C8ULL), v_rip - 8245526);
    goto loc_0081C24E;
loc_0081C249:
loc_0081C24E:
    result = AslFree((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 103))), result, (unsigned int)(0x9C8ULL), v_rip - 8245526);
loc_0081C256:
loc_0081C258:
    v_rsp = (v_rsp) + (160);
    return (unsigned int)((unsigned int)((unsigned int)(0x80000006ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t AslPathWildcardFindNext(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m88;
    uint64_t v_stack_m90;
    uint8_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    if (Arg3 != -1) goto loc_0081BB64;
    goto loc_0081C258;
loc_0081BB64:
    if (Arg1 != 0) goto loc_0081BB73;
    goto loc_0081C258;
loc_0081BB73:
    if (Arg3 != 0) goto loc_0081BB82;
    goto loc_0081C258;
loc_0081BB82:
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm0;
    result = AslAlloc(Arg1, 616, Arg3, a4);
    if (result != 0) goto loc_0081BBB4;
    goto loc_0081C256;
loc_0081BBB4:
loc_0081BBBA:
    if ((*(uint64_t *)(Arg3 + 0x20)) < 1) goto loc_0081C249;
    if ((*(uint64_t *)(Arg3 + 0x20) - 1) >= (*(uint64_t *)(Arg3 + 0x20))) goto loc_0081C206;
    result = ULongLongMult(*(uint64_t *)(Arg3 + 0x18), *(uint64_t *)(Arg3 + 0x20) - 1, local_rsp - 95 + 111, a4);
    if (sign_flag) goto loc_0081C206;
    local_rsi = (*(uint64_t *)(local_rsp - 0x5F + 0x6F)) + (*(uint64_t *)(Arg3 + 0x38));
    if (local_rsi < (*(uint64_t *)(Arg3 + 0x38))) goto loc_0081C206;
    if (local_rsi == 0) goto loc_0081C206;
    if ((*(uint64_t *)(local_rsi + 0x18)) != 0) goto loc_0081BE7E;
    result = AslLogCallPrintf(1, v_rip - 8243530, (uint32_t)(0x9CDULL), v_rip - 8243285);
    goto loc_0081BF2F;
loc_0081BC37:
    goto loc_0081BC94;
loc_0081BC3E:
    result = 0;
    if ((1 - 1) >= 1) goto loc_0081BC6E;
    result = ULongLongMult(*(uint64_t *)(Arg3 + 0x18), 1 - 1, local_rsp - 95 + 111, v_rip - 8243285);
    if (sign_flag) goto loc_0081BC73;
    result = (*(uint64_t *)(local_rsp - 0x5F + 0x6F)) + (*(uint64_t *)(Arg3 + 0x38));
    if (result < (*(uint64_t *)(Arg3 + 0x38))) goto loc_0081BC73;
loc_0081BC6E:
    if (result != 0) goto loc_0081BCB1;
loc_0081BC73:
    result = AslLogCallPrintf(1, v_rip - 8244111, (uint32_t)(0x825ULL), v_rip - 8244138);
loc_0081BC94:
    v_stack_mB8 = (uint32_t)((uint32_t)(0xC00000E5ULL));
    goto loc_0081C138;
loc_0081BCB1:
    result = AslpPathWildcardFreeMatchNode(result, v_rip - 8244059, (uint32_t)(0x840ULL), v_rip - 8244116);
    if ((*(uint64_t *)(Arg3 + 0x20) - 1) >= (*(uint64_t *)(Arg3 + 0x20))) goto loc_0081BBBA;
    result = ULongLongMult(*(uint64_t *)(Arg3 + 0x18), *(uint64_t *)(Arg3 + 0x20) - 1, local_rsp - 95 + 111, *(uint64_t *)(Arg3 + 0x20) - 1);
    if (sign_flag) goto loc_0081BBBA;
    local_rsi = (*(uint64_t *)(local_rsp - 0x5F + 0x6F)) + (*(uint64_t *)(Arg3 + 0x38));
    if (local_rsi < (*(uint64_t *)(Arg3 + 0x38))) goto loc_0081BBBA;
    local_rbx = (*(uint64_t *)(Arg3 + 0x20)) - (*(uint64_t *)(Arg3 + 0x20) - 1);
    local_rbx = (local_rbx) - (1);
    *(uint64_t *)(local_rsp - 0x5F + 0x77) = local_rbx;
    if (condition_is_equal) goto loc_0081BD64;
    result = ULongLongMult(local_rbx, *(uint64_t *)(Arg3 + 0x18), local_rsp - 95 + 119, *(uint64_t *)(Arg3 + 0x20) - 1);
    if (sign_flag) goto loc_0081BBBA;
    result = ULongLongMult(*(uint64_t *)(Arg3 + 0x18), *(uint64_t *)(Arg3 + 0x20), local_rsp - 95 + 111, *(uint64_t *)(Arg3 + 0x20) - 1);
    if (sign_flag) goto loc_0081BBBA;
    Arg2 = (*(uint64_t *)(local_rsp - 0x5F + 0x6F)) + (*(uint64_t *)(Arg3 + 0x38));
    if (Arg2 < (*(uint64_t *)(Arg3 + 0x38))) goto loc_0081BBBA;
    result = memcpy(local_rsi, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x77), *(uint64_t *)(Arg3 + 0x20) - 1);
loc_0081BD64:
    Arg2 = 0;
    result = memset(*(uint64_t *)(local_rsp - 0x5F + 0x77) + local_rsi * 1, Arg2, *(uint64_t *)(Arg3 + 0x18), *(uint64_t *)(Arg3 + 0x20) - 1);
    Arg3 = (*(uint64_t *)(Arg3 + 0x20)) - 1;
    *(uint64_t *)(Arg3 + 0x20) = Arg3;
    if (Arg3 <= 16) goto loc_0081BBBA;
    result = (*(uint64_t *)(Arg3 + 0x28)) * (*(uint64_t *)(Arg3 + 0x18));
    if (result < 0x400ULL) goto loc_0081BBBA;
    result = (*(uint64_t *)(Arg3 + 0x28)) >> (2);
    if (Arg3 >= result) goto loc_0081BBBA;
    local_rsi = (*(uint64_t *)(Arg3 + 0x28)) >> (1);
    result = ULongLongMult(*(uint64_t *)(Arg3 + 0x28), *(uint64_t *)(Arg3 + 0x18), local_rsp - 95 + 119, *(uint64_t *)(Arg3 + 0x20) - 1);
    if (sign_flag) goto loc_0081BBBA;
    result = ULongLongMult(local_rsi, *(uint64_t *)(Arg3 + 0x18), local_rsp - 95 + 111, *(uint64_t *)(Arg3 + 0x20) - 1);
    if (sign_flag) goto loc_0081BBBA;
    if (*(uint64_t *)(Arg3 + 0x38) != 0) goto loc_0081BE28;
    result = ExAllocatePoolWithTag(1, *(uint64_t *)(local_rsp - 0x5F + 0x6F), (uint32_t)(0x72615452ULL), *(uint64_t *)(Arg3 + 0x20) - 1);
    if (result != 0) {
        Arg3 = *(uint64_t *)(local_rsp - 0x5F + 0x6F);
        Arg2 = 0;
        Arg1 = result;
        result = memset(Arg1, Arg2, Arg3, *(uint64_t *)(Arg3 + 0x20) - 1);
    }
    if (result == 0) goto loc_0081BBBA;
    goto loc_0081BE71;
loc_0081BE28:
    result = ExAllocatePoolWithTag(Arg1, *(uint64_t *)(local_rsp - 0x5F + 0x6F), Arg3, *(uint64_t *)(Arg3 + 0x20) - 1);
    if (result == 0) goto loc_0081BBBA;
    Arg2 = 0;
    result = memset(result, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x6F), *(uint64_t *)(Arg3 + 0x20) - 1);
    local_r14 = *(uint64_t *)(local_rsp - 0x5F + 0x6F);
    if ((*(uint64_t *)(local_rsp - 0x5F + 0x77)) < (*(uint64_t *)(local_rsp - 0x5F + 0x6F))) { local_r14 = *(uint64_t *)(local_rsp - 0x5F + 0x77); }
    result = memcpy(result, *(uint64_t *)(Arg3 + 0x38), local_r14, *(uint64_t *)(Arg3 + 0x20) - 1);
    result = ExFreePoolWithTag(*(uint64_t *)(Arg3 + 0x38), (uint32_t)(0x72615452ULL), local_r14, *(uint64_t *)(Arg3 + 0x20) - 1);
loc_0081BE71:
    *(uint64_t *)(Arg3 + 0x38) = result;
    *(uint64_t *)(Arg3 + 0x28) = local_rsi;
    goto loc_0081BBBA;
loc_0081BE7E:
    result = RtlInitUnicodeString(local_rsp - 95 - 25, *(uint64_t *)(local_rsi + 0x10), local_r14, *(uint64_t *)(Arg3 + 0x20) - 1);
    v_stack_m88 = 0;
    a4 = 0;
    v_stack_m90 = local_rsp - 95 - 25;
    Arg3 = 0;
    v_stack_m98 = 1;
    v_stack_mA0 = 3;
    Arg2 = 0;
    v_stack_mA8 = 616;
    v_stack_mB0 = result;
    v_stack_mB8 = local_rsp - 95 - 9;
    result = ZwQueryDirectoryFile(*(uint64_t *)(local_rsi + 0x18), Arg2, Arg3, a4);
    if (!sign_flag) goto loc_0081BF41;
    if (((uint32_t)(result)) == 0x80000006ULL) goto loc_0081BF2F;
    if (((uint32_t)(result)) != 0xC000000FULL) {
        a4 = v_rip - 8243958;
        v_stack_mB8 = (uint32_t)(result);
        Arg3 = 0x9E5ULL;
        Arg2 = v_rip - 8244247;
        Arg1 = 1;
        result = AslLogCallPrintf(Arg1, Arg2, Arg3, a4);
        result = *(uint64_t *)(local_rsp - 0x5F - 0x11);
        a4 = v_rip - 8243938;
        v_stack_mB0 = result;
        Arg2 = v_rip - 8244278;
        result = *(uint64_t *)(local_rsi + 0x8);
        Arg3 = 0x9E6ULL;
        Arg1 = 2;
        v_stack_mB8 = result;
        result = AslLogCallPrintf(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint64_t *)(Arg3 + 0x20)) < 1) goto loc_0081BC37;
    goto loc_0081BC3E;
loc_0081BF41:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x3C)))) != 4) goto loc_0081BF5D;
    if ((*(uint16_t *)(result + 0x5E)) != 46) goto loc_0081BF6F;
    goto loc_0081BF69;
loc_0081BF5D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x3C)))) != 2) goto loc_0081BF6F;
loc_0081BF69:
    if ((*(uint16_t *)(result + 0x5E)) == 46) goto loc_0081BBBA;
loc_0081BF6F:
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x38))) >> (4));
    v_stack_mB0 = (uint16_t)(*(uint16_t *)(result + 0x3C));
    a4 = (uint32_t)((a4) & (1));
    v_stack_mB8 = result + 94;
    result = AslpPathWildcardAllocMatchNode(local_rsp - 95 + 7, local_rsi, *(uint64_t *)(local_rsi + 0x10), a4);
    if (((uint32_t)(result)) == 0xC0000273ULL) goto loc_0081C170;
    if (((uint32_t)(result)) == 0xC0000103ULL) goto loc_0081BBBA;
    if (((uint32_t)(result)) == 0xC00000BAULL) goto loc_0081BBBA;
    if (sign_flag) goto loc_0081C120;
    if ((*(uint64_t *)(Arg3 + 0x20)) < (*(uint64_t *)(Arg3 + 0x28))) goto loc_0081C0D9;
    if ((*(uint64_t *)(Arg3 + 0x20) + 1) <= (*(uint64_t *)(Arg3 + 0x28))) goto loc_0081C145;
    local_rsi = (*(uint64_t *)(Arg3 + 0x30)) - 1;
    if ((local_rsi + *(uint64_t *)(Arg3 + 0x20) + 1 * 1) < (*(uint64_t *)(Arg3 + 0x20) + 1)) goto loc_0081C14E;
    local_rsi = ~(local_rsi);
    local_rsi = (local_rsi) & (local_rsi + *(uint64_t *)(Arg3 + 0x20) + 1 * 1);
    result = ULongLongMult(*(uint64_t *)(Arg3 + 0x28), *(uint64_t *)(Arg3 + 0x18), local_rsp - 95 + 119, *(uint64_t *)(Arg3 + 0x28));
    if (!sign_flag) goto loc_0081C026;
loc_0081C01F:
    goto loc_0081C077;
loc_0081C026:
    result = ULongLongMult(local_rsi, *(uint64_t *)(Arg3 + 0x18), local_rsp - 95 + 111, *(uint64_t *)(Arg3 + 0x28));
    if (sign_flag) goto loc_0081C01F;
    if (*(uint64_t *)(Arg3 + 0x38) != 0) goto loc_0081C088;
    result = ExAllocatePoolWithTag(1, *(uint64_t *)(local_rsp - 0x5F + 0x6F), (uint32_t)(0x72615452ULL), *(uint64_t *)(Arg3 + 0x28));
    if (result != 0) {
        Arg3 = *(uint64_t *)(local_rsp - 0x5F + 0x6F);
        Arg2 = 0;
        Arg1 = result;
        result = memset(Arg1, Arg2, Arg3, *(uint64_t *)(Arg3 + 0x28));
    }
    if (result != 0) goto loc_0081C0CD;
loc_0081C072:
loc_0081C077:
    if ((uint32_t)((uint32_t)(0xC0000017ULL)) == 0) goto loc_0081C0D9;
    if (sign_flag) goto loc_0081C155;
    goto loc_0081BBB4;
loc_0081C088:
    result = ExAllocatePoolWithTag(Arg1, *(uint64_t *)(local_rsp - 0x5F + 0x6F), Arg3, *(uint64_t *)(Arg3 + 0x28));
    if (result == 0) goto loc_0081C072;
    Arg2 = 0;
    result = memset(result, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x6F), *(uint64_t *)(Arg3 + 0x28));
    local_r14 = *(uint64_t *)(local_rsp - 0x5F + 0x6F);
    if ((*(uint64_t *)(local_rsp - 0x5F + 0x77)) < (*(uint64_t *)(local_rsp - 0x5F + 0x6F))) { local_r14 = *(uint64_t *)(local_rsp - 0x5F + 0x77); }
    result = memcpy(result, *(uint64_t *)(Arg3 + 0x38), local_r14, *(uint64_t *)(Arg3 + 0x28));
    result = ExFreePoolWithTag(*(uint64_t *)(Arg3 + 0x38), (uint32_t)(0x72615452ULL), local_r14, *(uint64_t *)(Arg3 + 0x28));
loc_0081C0CD:
    *(uint64_t *)(Arg3 + 0x38) = result;
    local_rbx = 0;
    *(uint64_t *)(Arg3 + 0x28) = local_rsi;
    goto loc_0081C077;
loc_0081C0D9:
    result = ULongLongMult(*(uint64_t *)(Arg3 + 0x18), *(uint64_t *)(Arg3 + 0x20), local_rsp - 95 + 111, *(uint64_t *)(Arg3 + 0x28));
    if (sign_flag) goto loc_0081C14E;
    Arg2 = (*(uint64_t *)(local_rsp - 0x5F + 0x6F)) + (*(uint64_t *)(Arg3 + 0x38));
    if (Arg2 < (*(uint64_t *)(Arg3 + 0x38))) goto loc_0081C14E;
    *(uint64_t *)(Arg2) = v_xmm0;
    *(uint64_t *)(Arg2 + 0x10) = v_xmm1;
    goto loc_0081BBBA;
loc_0081C120:
    v_stack_mB8 = (uint32_t)(result);
loc_0081C138:
    result = AslLogCallPrintf(1, v_rip - 8244824, (uint32_t)(0xA1FULL), v_rip - 8244451);
    goto loc_0081BBBA;
loc_0081C145:
    goto loc_0081C155;
loc_0081C14E:
loc_0081C155:
loc_0081C162:
    v_stack_mB8 = (uint32_t)((uint32_t)(0xC0000095ULL));
    goto loc_0081C23B;
loc_0081C170:
    result = RtlStringCbCopyNW(*(uint64_t *)(local_rsp - 0x5F + 0x67), 520, *(uint64_t *)(local_rsi + 0x8), *(uint16_t *)(local_rsi));
    if (!sign_flag) goto loc_0081C19E;
    goto loc_0081C162;
loc_0081C19E:
    Arg1 = (*(uint16_t *)(local_rsi)) >> (1);
    if ((*(uint16_t *)(*(uint64_t *)(local_rsi + 0x8) + Arg1 * 2 - 0x2)) == 92) goto loc_0081C1DA;
    result = RtlStringCbCatNW(*(uint64_t *)(local_rsp - 0x5F + 0x67), 520, v_rip - 8389693, 2);
    if (!sign_flag) goto loc_0081C1DA;
    goto loc_0081C162;
loc_0081C1DA:
    result = RtlStringCbCatNW(*(uint64_t *)(local_rsp - 0x5F + 0x67), 520, local_r14, (uint32_t)(*(uint32_t *)(result + 0x3C)));
    if (!sign_flag) goto loc_0081C202;
    goto loc_0081C162;
loc_0081C202:
    local_rbx = 0;
    goto loc_0081C24E;
loc_0081C206:
    result = AslLogCallPrintf((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x67))), v_rip - 8245538, (uint32_t)(0x825ULL), v_rip - 8245565);
    v_stack_mB8 = (uint32_t)((uint32_t)(0xC00000E5ULL));
loc_0081C23B:
    result = AslLogCallPrintf((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x67))), v_rip - 8245090, (uint32_t)(0x9C8ULL), v_rip - 8245526);
    goto loc_0081C24E;
loc_0081C249:
loc_0081C24E:
    result = AslFree((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x67))), result, (uint32_t)(0x9C8ULL), v_rip - 8245526);
loc_0081C256:
loc_0081C258:
    local_rsp = (local_rsp) + (160);
    return (uint32_t)((uint32_t)((uint32_t)(0x80000006ULL)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0081BB2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
