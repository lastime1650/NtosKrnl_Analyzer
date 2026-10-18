# NtManagePartition

- RVA: `0x00902FC0`–`0x00903373` (길이 `947` bytes)
- VA: `0x0000000140902FC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00088900`
- 디코드: `237`개 명령, `947/947` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00903000` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009030A3` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009030B3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009030F1` → [PsReferencePartitionByHandle](PsReferencePartitionByHandle_function_0090337C.md) (function, `0x0090337C`)
- `0x0090312D` → [MmCheckPartitionManagementSupported](MmCheckPartitionManagementSupported_function_00901A80.md) (function, `0x00901A80`)
- `0x00903165` → [MmManagePartitionMemoryInformation](MmManagePartitionMemoryInformation_function_0090343C.md) (function, `0x0090343C`)
- `0x00903194` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x009031A4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009031BC` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x009031D9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0090320B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00903220` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00903253` → [MmManagePartitionGetMemoryEvents](MmManagePartitionGetMemoryEvents_function_00901AB4.md) (function, `0x00901AB4`)
- `0x00903269` → [MmCheckPartitionManagementSupported](MmCheckPartitionManagementSupported_function_00901A80.md) (function, `0x00901A80`)
- `0x009032A9` → [MmManagePartitionInitialAddMemory](../80/MmManagePartitionInitialAddMemory_function_0080E144.md) (function, `0x0080E144`)
- `0x009032B9` → [MmManagePartitionCombineMemory](../80/MmManagePartitionCombineMemory_function_0080DF94.md) (function, `0x0080DF94`)
- `0x009032E1` → [MiCreatePagingFile](../7F/MiCreatePagingFile_function_007FEFF4.md) (function, `0x007FEFF4`)
- `0x009032FB` → [MmManagePartitionMoveMemory](../80/MmManagePartitionMoveMemory_function_0080E1F4.md) (function, `0x0080E1F4`)
- `0x00903310` → [MmManagePartitionNodeInformation](../80/MmManagePartitionNodeInformation_function_0080E490.md) (function, `0x0080E490`)
- `0x0090335A` → [MmIssueMemoryListCommand](../7F/MmIssueMemoryListCommand_function_007FE8B0.md) (function, `0x007FE8B0`)
- `0x00903369` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00902FD3` → RVA `0x00E0A740` (`.data`; read)
- `0x00903038` → RVA `0x00B4ECD0` (`PspPartitionInfoDetails`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00903000` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009030B3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009031A4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009031BC` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (`PAGE` → `.text`)
  - `0x009031D9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0090320B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00903220` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00903369` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00903111` → [sub_00B2095C](../B2/Unknown_function_00B2095C.md) (`tail-transfer`)
  - `0x0090329E` → [sub_00B2095C + 0x69](../B2/Unknown_function_00B2095C.md) (`tail-transfer`)
  - `0x0090331D` → [sub_00B2095C + 0xCD](../B2/Unknown_function_00B2095C.md) (`tail-transfer`)
  - `0x00903326` → [sub_00B2095C + 0xB6](../B2/Unknown_function_00B2095C.md) (`tail-transfer`)
  - `0x0090332F` → [sub_00B2095C + 0xA0](../B2/Unknown_function_00B2095C.md) (`tail-transfer`)
  - `0x00903338` → [sub_00B2095C + 0x87](../B2/Unknown_function_00B2095C.md) (`tail-transfer`)
  - `0x00903341` → [sub_00B2095C + 0x5B](../B2/Unknown_function_00B2095C.md) (`tail-transfer`)
  - `0x0090334A` → [sub_00B2095C + 0x74](../B2/Unknown_function_00B2095C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00902FC0  40 53                           push rbx
00902FC2  56                              push rsi
00902FC3  57                              push rdi
00902FC4  41 54                           push r12
00902FC6  41 55                           push r13
00902FC8  41 56                           push r14
00902FCA  41 57                           push r15
00902FCC  48 81 EC 50 01 00 00            sub rsp, 0x150
00902FD3  48 8B 05 66 77 50 00            mov rax, qword ptr [rip + 0x507766]
00902FDA  48 33 C4                        xor rax, rsp
00902FDD  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00902FE5  4D 8B F9                        mov r15, r9
00902FE8  41 8B D8                        mov ebx, r8d
00902FEB  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00902FF0  48 8B F9                        mov rdi, rcx
00902FF3  33 D2                           xor edx, edx
00902FF5  41 B8 F0 00 00 00               mov r8d, 0xf0
00902FFB  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00903000  E8 3B 3C DC FF                  call 0x1406c6c40
00903005  C6 44 24 31 00                  mov byte ptr [rsp + 0x31], 0
0090300A  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
0090300F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00903018  44 8A B0 32 02 00 00            mov r14b, byte ptr [rax + 0x232]
0090301F  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
00903025  33 F6                           xor esi, esi
00903027  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0090302C  83 FB 0F                        cmp ebx, 0xf
0090302F  0F 83 28 02 00 00               jae 0x14090325d
00903035  44 8B EB                        mov r13d, ebx
00903038  48 8D 05 91 BC 24 00            lea rax, [rip + 0x24bc91]
0090303F  8A 4C D8 07                     mov cl, byte ptr [rax + rbx*8 + 7]
00903043  44 8B A4 24 B0 01 00 00         mov r12d, dword ptr [rsp + 0x1b0]
0090304B  F6 C1 10                        test cl, 0x10
0090304E  75 15                           jne 0x140903065
00903050  0F B7 44 D8 04                  movzx eax, word ptr [rax + rbx*8 + 4]
00903055  44 3B E0                        cmp r12d, eax
00903058  0F 85 9B 01 00 00               jne 0x1409031f9
0090305E  48 8D 05 6B BC 24 00            lea rax, [rip + 0x24bc6b]
00903065  F6 C1 01                        test cl, 1
00903068  74 5C                           je 0x1409030c6
0090306A  45 84 F6                        test r14b, r14b
0090306D  0F 84 8D 01 00 00               je 0x140903200
00903073  45 85 E4                        test r12d, r12d
00903076  74 30                           je 0x1409030a8
00903078  0F B6 44 D8 06                  movzx eax, byte ptr [rax + rbx*8 + 6]
0090307D  48 FF C8                        dec rax
00903080  49 85 C7                        test r15, rax
00903083  75 1E                           jne 0x1409030a3
00903085  41 8B CC                        mov ecx, r12d
00903088  49 03 CF                        add rcx, r15
0090308B  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00903095  48 3B C8                        cmp rcx, rax
00903098  77 05                           ja 0x14090309f
0090309A  49 3B CF                        cmp rcx, r15
0090309D  73 09                           jae 0x1409030a8
0090309F  8A 00                           mov al, byte ptr [rax]
009030A1  EB 05                           jmp 0x1409030a8
009030A3  E8 28 6F F9 FF                  call 0x140899fd0
009030A8  45 8B C4                        mov r8d, r12d
009030AB  49 8B D7                        mov rdx, r15
009030AE  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
009030B3  E8 88 37 DC FF                  call 0x1406c6840
009030B8  EB 0C                           jmp 0x1409030c6
009030BA  8B F8                           mov edi, eax
009030BC  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
009030C1  E9 EC 00 00 00                  jmp 0x1409031b2
009030C6  48 8D 35 03 BC 24 00            lea rsi, [rip + 0x24bc03]
009030CD  8B 34 DE                        mov esi, dword ptr [rsi + rbx*8]
009030D0  83 FB 0B                        cmp ebx, 0xb
009030D3  0F 84 A4 01 00 00               je 0x14090327d
009030D9  48 8D 44 24 38                  lea rax, [rsp + 0x38]
009030DE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009030E3  41 B9 50 73 4D 70               mov r9d, 0x704d7350
009030E9  45 8A C6                        mov r8b, r14b
009030EC  8B D6                           mov edx, esi
009030EE  48 8B CF                        mov rcx, rdi
009030F1  E8 86 02 00 00                  call 0x14090337c
009030F6  8B F8                           mov edi, eax
009030F8  85 C0                           test eax, eax
009030FA  0F 88 F2 00 00 00               js 0x1409031f2
00903100  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00903105  48 8D 05 C4 BB 24 00            lea rax, [rip + 0x24bbc4]
0090310C  F6 44 D8 07 04                  test byte ptr [rax + rbx*8 + 7], 4
00903111  0F 85 45 D8 21 00               jne 0x140b2095c
00903117  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0090311C  48 83 7C 24 48 00               cmp qword ptr [rsp + 0x48], 0
00903122  0F 85 66 01 00 00               jne 0x14090328e
00903128  8B D3                           mov edx, ebx
0090312A  48 8B CE                        mov rcx, rsi
0090312D  E8 4E E9 FF FF                  call 0x140901a80
00903132  8B F8                           mov edi, eax
00903134  85 C0                           test eax, eax
00903136  78 7A                           js 0x1409031b2
00903138  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0090313D  48 85 C9                        test rcx, rcx
00903140  0F 85 21 01 00 00               jne 0x140903267
00903146  83 FB 07                        cmp ebx, 7
00903149  0F 8F CB 01 00 00               jg 0x14090331a
0090314F  0F 84 B0 01 00 00               je 0x140903305
00903155  85 DB                           test ebx, ebx
00903157  0F 85 CA 00 00 00               jne 0x140903227
0090315D  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00903162  48 8B CE                        mov rcx, rsi
00903165  E8 D2 02 00 00                  call 0x14090343c
0090316A  8B F8                           mov edi, eax
0090316C  85 C0                           test eax, eax
0090316E  78 42                           js 0x1409031b2
00903170  48 8D 0D 59 BB 24 00            lea rcx, [rip + 0x24bb59]
00903177  42 F6 44 E9 07 02               test byte ptr [rcx + r13*8 + 7], 2
0090317D  74 33                           je 0x1409031b2
0090317F  45 84 F6                        test r14b, r14b
00903182  0F 84 8D 00 00 00               je 0x140903215
00903188  46 0F B6 44 E9 06               movzx r8d, byte ptr [rcx + r13*8 + 6]
0090318E  41 8B D4                        mov edx, r12d
00903191  49 8B CF                        mov rcx, r15
00903194  E8 27 60 FE FF                  call 0x1408e91c0
00903199  45 8B C4                        mov r8d, r12d
0090319C  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
009031A1  49 8B CF                        mov rcx, r15
009031A4  E8 97 36 DC FF                  call 0x1406c6840
009031A9  EB 07                           jmp 0x1409031b2
009031AB  8B F8                           mov edi, eax
009031AD  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
009031B2  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
009031B7  74 08                           je 0x1409031c1
009031B9  48 8B CE                        mov rcx, rsi
009031BC  E8 AF FC A3 FF                  call 0x140342e70
009031C1  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
009031C6  0F 85 98 01 00 00               jne 0x140903364
009031CC  8B C7                           mov eax, edi
009031CE  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
009031D6  48 33 CC                        xor rcx, rsp
009031D9  E8 62 94 DA FF                  call 0x1406ac640
009031DE  48 81 C4 50 01 00 00            add rsp, 0x150
009031E5  41 5F                           pop r15
009031E7  41 5E                           pop r14
009031E9  41 5D                           pop r13
009031EB  41 5C                           pop r12
009031ED  5F                              pop rdi
009031EE  5E                              pop rsi
009031EF  5B                              pop rbx
009031F0  C3                              ret
009031F1  CC                              int3
009031F2  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
009031F7  EB B9                           jmp 0x1409031b2
009031F9  BF 04 00 00 C0                  mov edi, 0xc0000004
009031FE  EB B2                           jmp 0x1409031b2
00903200  45 8B C4                        mov r8d, r12d
00903203  49 8B D7                        mov rdx, r15
00903206  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0090320B  E8 30 36 DC FF                  call 0x1406c6840
00903210  E9 B1 FE FF FF                  jmp 0x1409030c6
00903215  45 8B C4                        mov r8d, r12d
00903218  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0090321D  49 8B CF                        mov rcx, r15
00903220  E8 1B 36 DC FF                  call 0x1406c6840
00903225  EB 8B                           jmp 0x1409031b2
00903227  83 EB 01                        sub ebx, 1
0090322A  0F 84 BB 00 00 00               je 0x1409032eb
00903230  83 EB 01                        sub ebx, 1
00903233  0F 84 8A 00 00 00               je 0x1409032c3
00903239  83 EB 01                        sub ebx, 1
0090323C  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00903241  48 8B CE                        mov rcx, rsi
00903244  74 6D                           je 0x1409032b3
00903246  83 EB 01                        sub ebx, 1
00903249  74 58                           je 0x1409032a3
0090324B  45 8A C6                        mov r8b, r14b
0090324E  83 FB 01                        cmp ebx, 1
00903251  75 45                           jne 0x140903298
00903253  E8 5C E8 FF FF                  call 0x140901ab4
00903258  E9 0D FF FF FF                  jmp 0x14090316a
0090325D  BF 03 00 00 C0                  mov edi, 0xc0000003
00903262  E9 4B FF FF FF                  jmp 0x1409031b2
00903267  8B D3                           mov edx, ebx
00903269  E8 12 E8 FF FF                  call 0x140901a80
0090326E  8B F8                           mov edi, eax
00903270  85 C0                           test eax, eax
00903272  0F 89 CE FE FF FF               jns 0x140903146
00903278  E9 35 FF FF FF                  jmp 0x1409031b2
0090327D  B8 02 00 00 00                  mov eax, 2
00903282  39 44 24 58                     cmp dword ptr [rsp + 0x58], eax
00903286  0F 44 F0                        cmove esi, eax
00903289  E9 4B FE FF FF                  jmp 0x1409030d9
0090328E  BF F0 00 00 C0                  mov edi, 0xc00000f0
00903293  E9 1A FF FF FF                  jmp 0x1409031b2
00903298  41 B9 01 00 00 00               mov r9d, 1
0090329E  E9 22 D7 21 00                  jmp 0x140b209c5
009032A3  45 8A CE                        mov r9b, r14b
009032A6  4D 8B C7                        mov r8, r15
009032A9  E8 96 AE F0 FF                  call 0x14080e144
009032AE  E9 B7 FE FF FF                  jmp 0x14090316a
009032B3  45 8A CE                        mov r9b, r14b
009032B6  4D 8B C7                        mov r8, r15
009032B9  E8 D6 AC F0 FF                  call 0x14080df94
009032BE  E9 A7 FE FF FF                  jmp 0x14090316a
009032C3  48 8B 06                        mov rax, qword ptr [rsi]
009032C6  4D 8D 47 18                     lea r8, [r15 + 0x18]
009032CA  49 8D 57 10                     lea rdx, [r15 + 0x10]
009032CE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009032D3  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009032D7  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009032DB  45 8A CE                        mov r9b, r14b
009032DE  49 8B CF                        mov rcx, r15
009032E1  E8 0E BD EF FF                  call 0x1407feff4
009032E6  E9 7F FE FF FF                  jmp 0x14090316a
009032EB  45 8A CE                        mov r9b, r14b
009032EE  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
009032F3  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
009032F8  48 8B CE                        mov rcx, rsi
009032FB  E8 F4 AE F0 FF                  call 0x14080e1f4
00903300  E9 65 FE FF FF                  jmp 0x14090316a
00903305  45 8A C6                        mov r8b, r14b
00903308  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0090330D  48 8B CE                        mov rcx, rsi
00903310  E8 7B B1 F0 FF                  call 0x14080e490
00903315  E9 50 FE FF FF                  jmp 0x14090316a
0090331A  83 EB 08                        sub ebx, 8
0090331D  0F 84 06 D7 21 00               je 0x140b20a29
00903323  83 EB 01                        sub ebx, 1
00903326  0F 84 E6 D6 21 00               je 0x140b20a12
0090332C  83 EB 01                        sub ebx, 1
0090332F  0F 84 C7 D6 21 00               je 0x140b209fc
00903335  83 EB 01                        sub ebx, 1
00903338  0F 84 A5 D6 21 00               je 0x140b209e3
0090333E  83 EB 01                        sub ebx, 1
00903341  0F 84 70 D6 21 00               je 0x140b209b7
00903347  83 FB 01                        cmp ebx, 1
0090334A  0F 84 80 D6 21 00               je 0x140b209d0
00903350  4C 8B C6                        mov r8, rsi
00903353  41 8A D6                        mov dl, r14b
00903356  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
0090335A  E8 51 B5 EF FF                  call 0x1407fe8b0
0090335F  E9 06 FE FF FF                  jmp 0x14090316a
00903364  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00903369  E8 02 FB A3 FF                  call 0x140342e70
0090336E  E9 59 FE FF FF                  jmp 0x1409031cc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtManagePartition(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int8 v_stack_m157;
    unsigned __int8 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p78;

    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 5273446)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m140 = a2;
    a2 = 0;
    result = memset(v_stack_m130, a2, 240, a4);
    v_stack_m157 = 0;
    v_stack_m158 = 0;
    v_rsi = 0;
    v_stack_m150 = 0;
    if (((unsigned int)((unsigned int)(a3))) >= 15) goto loc_0090325D;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rip + 2407569 + (unsigned int)(a3) * 8 + 7))) & (16)) != 0) goto loc_00903065;
    if (((unsigned int)((unsigned int)(a5))) != ((unsigned int)(*(unsigned __int16 *)(v_rip + 2407569 + (unsigned int)(a3) * 8 + 4)))) goto loc_009031F9;
loc_00903065:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rip + 2407569 + (unsigned int)(a3) * 8 + 7))) & (1)) == 0) goto loc_009030C6;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00903200;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_009030A8;
    result = (*(unsigned __int8 *)(v_rip + 2407531 + (unsigned int)(a3) * 8 + 6)) - 1;
    if (((a4) & (result)) != 0) goto loc_009030A3;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(a5)))) + (a4);
    if (a1 > result) goto loc_0090309F;
    if (a1 >= a4) goto loc_009030A8;
loc_0090309F:
    goto loc_009030A8;
loc_009030A3:
    result = ExRaiseDatatypeMisalignment(a1, a2, 240, a4);
loc_009030A8:
    result = memcpy(v_stack_m130, a4, (unsigned int)((unsigned int)((unsigned int)(a5))), a4);
    goto loc_009030C6;
loc_009030C6:
    if (((unsigned int)((unsigned int)(a3))) == 11) goto loc_0090327D;
loc_009030D9:
    v_stack_m168 = v_stack_m150;
    result = PsReferencePartitionByHandle(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2407427 + (unsigned int)(a3) * 8)))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(0x704D7350ULL));
    if (sign_flag) goto loc_009031F2;
    v_stack_m158 = 1;
    if (v_stack_m140 != 0) goto loc_0090328E;
    result = MmCheckPartitionManagementSupported(v_stack_m150, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(0x704D7350ULL));
    if (sign_flag) goto loc_009031B2;
    if (v_stack_m148 != 0) goto loc_00903267;
loc_00903146:
    if (((unsigned int)((unsigned int)(a3))) > 7) goto loc_0090331A;
    if (((unsigned int)((unsigned int)(a3))) == 7) goto loc_00903305;
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_00903227;
    result = MmManagePartitionMemoryInformation(v_stack_m150, v_stack_m130, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(0x704D7350ULL));
loc_0090316A:
    if (sign_flag) goto loc_009031B2;
    if (((*(unsigned __int8 *)(v_rip + 2407257 + (unsigned int)((unsigned int)((unsigned int)(a3))) * 8 + 7)) & (2)) == 0) goto loc_009031B2;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00903215;
    result = ProbeForWrite(a4, (unsigned int)((unsigned int)((unsigned int)(a5))), *(unsigned __int8 *)(v_rip + 2407257 + (unsigned int)((unsigned int)((unsigned int)(a3))) * 8 + 6), (unsigned int)(0x704D7350ULL));
    result = memcpy(a4, v_stack_m130, (unsigned int)((unsigned int)((unsigned int)(a5))), (unsigned int)(0x704D7350ULL));
    goto loc_009031B2;
loc_009031B2:
    if (v_stack_m158 != 0) {
        a1 = v_stack_m150;
        result = PsDereferencePartition(a1, v_stack_m130, (unsigned int)((unsigned int)((unsigned int)(a5))), (unsigned int)(0x704D7350ULL));
    }
    if (v_stack_m157 != 0) goto loc_00903364;
loc_009031CC:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m130, (unsigned int)((unsigned int)((unsigned int)(a5))), (unsigned int)(0x704D7350ULL));
    v_rsp = (v_rsp) + (336);
    return result;
loc_009031F2:
    goto loc_009031B2;
loc_009031F9:
    goto loc_009031B2;
loc_00903200:
    result = memcpy(v_stack_p58, a4, (unsigned int)((unsigned int)((unsigned int)(a5))), (unsigned int)(0x704D7350ULL));
    goto loc_009030C6;
loc_00903215:
    result = memcpy(a4, v_stack_p58, (unsigned int)((unsigned int)((unsigned int)(a5))), (unsigned int)(0x704D7350ULL));
    goto loc_009031B2;
loc_00903227:
    v_rbx = (unsigned int)(((unsigned int)(a3)) - (1));
    if (condition_is_equal) goto loc_009032EB;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_009032C3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_009032B3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_009032A3;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00903298;
    result = MmManagePartitionGetMemoryEvents(v_stack_p38, v_stack_p58, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(0x704D7350ULL));
    goto loc_0090316A;
loc_0090325D:
    goto loc_009031B2;
loc_00903267:
    result = MmCheckPartitionManagementSupported(v_stack_p38, (unsigned int)((unsigned int)(v_rbx)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(0x704D7350ULL));
    if (!sign_flag) goto loc_00903146;
    goto loc_009031B2;
loc_0090327D:
    v_rsi = v_stack_p38;
    if (v_stack_p58 == 2) { v_rsi = 2; }
    goto loc_009030D9;
loc_0090328E:
    goto loc_009031B2;
loc_00903298:
loc_009032A3:
    result = MmManagePartitionInitialAddMemory(v_stack_p38, (unsigned int)((unsigned int)(v_rbx)), a4, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_0090316A;
loc_009032B3:
    result = MmManagePartitionCombineMemory(v_stack_p38, (unsigned int)((unsigned int)(v_rbx)), a4, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_0090316A;
loc_009032C3:
    v_stack_p28 = *(unsigned __int64 *)(v_rsi);
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p78));
    result = MiCreatePagingFile(a4, a4 + 16, a4 + 24, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_0090316A;
loc_009032EB:
    result = MmManagePartitionMoveMemory(v_rsi, v_stack_p40, v_stack_p58, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_0090316A;
loc_00903305:
    result = MmManagePartitionNodeInformation(v_rsi, v_stack_p58, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_0090316A;
loc_0090331A:
    v_rbx = (unsigned int)((v_rbx) - (8));
    v_rbx = (unsigned int)((v_rbx) - (1));
    v_rbx = (unsigned int)((v_rbx) - (1));
    v_rbx = (unsigned int)((v_rbx) - (1));
    v_rbx = (unsigned int)((v_rbx) - (1));
    result = MmIssueMemoryListCommand((unsigned int)(v_stack_p58), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_rsi, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_0090316A;
loc_00903364:
    result = PsDereferencePartition(v_stack_p40, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_rsi, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_009031CC;
}
```

## 5. (Beta) C Style

```c
int64_t NtManagePartition(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m130;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint8_t v_stack_m157;
    uint8_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m40;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p58;
    uint32_t v_stack_p78;

    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0x507766)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m140 = Arg2;
    Arg2 = 0;
    result = memset(v_stack_m130, Arg2, 240, Arg4);
    v_stack_m157 = 0;
    v_stack_m158 = 0;
    local_rsi = 0;
    v_stack_m150 = 0;
    if (((uint32_t)((uint32_t)(Arg3))) >= 15) goto loc_0090325D;
    if ((((uint8_t)(*(uint8_t *)(v_rip + 0x24BC91 + (uint32_t)(Arg3) * 8 + 0x7))) & (16)) != 0) goto loc_00903065;
    if (((uint32_t)((uint32_t)(Arg5))) != ((uint32_t)(*(uint16_t *)(v_rip + 0x24BC91 + (uint32_t)(Arg3) * 8 + 0x4)))) goto loc_009031F9;
loc_00903065:
    if ((((uint8_t)(*(uint8_t *)(v_rip + 0x24BC91 + (uint32_t)(Arg3) * 8 + 0x7))) & (1)) == 0) goto loc_009030C6;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00903200;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_009030A8;
    result = (*(uint8_t *)(v_rip + 0x24BC6B + (uint32_t)(Arg3) * 8 + 0x6)) - 1;
    if (((Arg4) & (result)) != 0) goto loc_009030A3;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(Arg5)))) + (Arg4);
    if (Arg1 > result) goto loc_0090309F;
    if (Arg1 >= Arg4) goto loc_009030A8;
loc_0090309F:
    goto loc_009030A8;
loc_009030A3:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, 240, Arg4);
loc_009030A8:
    result = memcpy(v_stack_m130, Arg4, (uint32_t)((uint32_t)((uint32_t)(Arg5))), Arg4);
    goto loc_009030C6;
loc_009030C6:
    if (((uint32_t)((uint32_t)(Arg3))) == 11) goto loc_0090327D;
loc_009030D9:
    v_stack_m168 = v_stack_m150;
    result = PsReferencePartitionByHandle(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x24BC03 + (uint32_t)(Arg3) * 8)))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(0x704D7350ULL));
    if (sign_flag) goto loc_009031F2;
    v_stack_m158 = 1;
    if (v_stack_m140 != 0) goto loc_0090328E;
    result = MmCheckPartitionManagementSupported(v_stack_m150, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(0x704D7350ULL));
    if (sign_flag) goto loc_009031B2;
    if (v_stack_m148 != 0) goto loc_00903267;
loc_00903146:
    if (((uint32_t)((uint32_t)(Arg3))) > 7) goto loc_0090331A;
    if (((uint32_t)((uint32_t)(Arg3))) == 7) goto loc_00903305;
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_00903227;
    result = MmManagePartitionMemoryInformation(v_stack_m150, v_stack_m130, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(0x704D7350ULL));
loc_0090316A:
    if (sign_flag) goto loc_009031B2;
    if (((*(uint8_t *)(v_rip + 0x24BB59 + (uint32_t)((uint32_t)((uint32_t)(Arg3))) * 8 + 0x7)) & (2)) == 0) goto loc_009031B2;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00903215;
    result = ProbeForWrite(Arg4, (uint32_t)((uint32_t)((uint32_t)(Arg5))), *(uint8_t *)(v_rip + 0x24BB59 + (uint32_t)((uint32_t)((uint32_t)(Arg3))) * 8 + 0x6), (uint32_t)(0x704D7350ULL));
    result = memcpy(Arg4, v_stack_m130, (uint32_t)((uint32_t)((uint32_t)(Arg5))), (uint32_t)(0x704D7350ULL));
    goto loc_009031B2;
loc_009031B2:
    if (v_stack_m158 != 0) {
        Arg1 = v_stack_m150;
        result = PsDereferencePartition(Arg1, v_stack_m130, (uint32_t)((uint32_t)((uint32_t)(Arg5))), (uint32_t)(0x704D7350ULL));
    }
    if (v_stack_m157 != 0) goto loc_00903364;
loc_009031CC:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m130, (uint32_t)((uint32_t)((uint32_t)(Arg5))), (uint32_t)(0x704D7350ULL));
    local_rsp = (local_rsp) + (336);
    return result;
loc_009031F2:
    goto loc_009031B2;
loc_009031F9:
    goto loc_009031B2;
loc_00903200:
    result = memcpy(v_stack_p58, Arg4, (uint32_t)((uint32_t)((uint32_t)(Arg5))), (uint32_t)(0x704D7350ULL));
    goto loc_009030C6;
loc_00903215:
    result = memcpy(Arg4, v_stack_p58, (uint32_t)((uint32_t)((uint32_t)(Arg5))), (uint32_t)(0x704D7350ULL));
    goto loc_009031B2;
loc_00903227:
    local_rbx = (uint32_t)(((uint32_t)(Arg3)) - (1));
    if (condition_is_equal) goto loc_009032EB;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_009032C3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_009032B3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_009032A3;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00903298;
    result = MmManagePartitionGetMemoryEvents(v_stack_p38, v_stack_p58, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(0x704D7350ULL));
    goto loc_0090316A;
loc_0090325D:
    goto loc_009031B2;
loc_00903267:
    result = MmCheckPartitionManagementSupported(v_stack_p38, (uint32_t)((uint32_t)(local_rbx)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(0x704D7350ULL));
    if (!sign_flag) goto loc_00903146;
    goto loc_009031B2;
loc_0090327D:
    local_rsi = v_stack_p38;
    if (v_stack_p58 == 2) { local_rsi = 2; }
    goto loc_009030D9;
loc_0090328E:
    goto loc_009031B2;
loc_00903298:
loc_009032A3:
    result = MmManagePartitionInitialAddMemory(v_stack_p38, (uint32_t)((uint32_t)(local_rbx)), Arg4, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_0090316A;
loc_009032B3:
    result = MmManagePartitionCombineMemory(v_stack_p38, (uint32_t)((uint32_t)(local_rbx)), Arg4, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_0090316A;
loc_009032C3:
    v_stack_p28 = *(uint64_t *)(local_rsi);
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p78));
    result = MiCreatePagingFile(Arg4, Arg4 + 16, Arg4 + 24, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_0090316A;
loc_009032EB:
    result = MmManagePartitionMoveMemory(local_rsi, v_stack_p40, v_stack_p58, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_0090316A;
loc_00903305:
    result = MmManagePartitionNodeInformation(local_rsi, v_stack_p58, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_0090316A;
loc_0090331A:
    local_rbx = (uint32_t)((local_rbx) - (8));
    local_rbx = (uint32_t)((local_rbx) - (1));
    local_rbx = (uint32_t)((local_rbx) - (1));
    local_rbx = (uint32_t)((local_rbx) - (1));
    local_rbx = (uint32_t)((local_rbx) - (1));
    result = MmIssueMemoryListCommand((uint32_t)(v_stack_p58), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), local_rsi, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_0090316A;
loc_00903364:
    result = PsDereferencePartition(v_stack_p40, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), local_rsi, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_009031CC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00902FC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
