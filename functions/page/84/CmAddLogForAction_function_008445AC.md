# CmAddLogForAction

- RVA: `0x008445AC`–`0x00844BA9` (길이 `1,533` bytes)
- VA: `0x00000001408445AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00069158`
- 디코드: `394`개 명령, `1,533/1,533` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0084462A` → [CmpConstructName](../85/CmpConstructName_function_00856BE0.md) (function, `0x00856BE0`)
- `0x0084468C` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008446DA` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00844730` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008447D4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00844802` → [CmpCopyCompressedName](CmpCopyCompressedName_function_0084E0D0.md) (function, `0x0084E0D0`)
- `0x00844855` → [CmpGetValueData](../85/CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x00844872` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008448A0` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008448D7` → [HvBufferCheckSum](HvBufferCheckSum_function_00842A04.md) (function, `0x00842A04`)
- `0x008448E6` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnInvalid` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnInvalid`)
- `0x00844912` → [CmpTransWriteLog](CmpTransWriteLog_function_00842A7C.md) (function, `0x00842A7C`)
- `0x00844925` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnInvalid` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnInvalid`)
- `0x0084494C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00844964` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsGetLogFileInformation` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsGetLogFileInformation`)
- `0x00844975` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00844998` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008449A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008449B4` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)
- `0x008449F9` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00844A28` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00844A35` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00844A3F` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00844A49` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00844AC5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00844B05` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00844B30` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00844B46` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00844B76` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [CmSetLastWriteTimeKey](CmSetLastWriteTimeKey_function_00843368.md) at `0x0084366D`
- [CmSetValueKey](CmSetValueKey_function_008457C0.md) at `0x00845E4E`
- [CmDeleteValueKey](CmDeleteValueKey_function_008476E8.md) at `0x00847F5A`
- [CmDeleteKey](CmDeleteKey_function_00848E5C.md) at `0x00849575`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x00948B6E`
- [sub_00B25C42](../B2/Unknown_function_00B25C42.md) at `0x00B25CA1`
- [sub_00B2D804](../B2/Unknown_function_00B2D804.md) at `0x00B2D8CF`

### Static image references
- `0x008448E6` → RVA `0x00151200` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnInvalid (IAT)`; read)
- `0x00844964` → RVA `0x00151240` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsGetLogFileInformation (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00844730` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008447D4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00844872` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0084494C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00844975` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008449A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008449B4` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
  - `0x00844A35` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00844AC5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00844B05` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00844B30` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00844B46` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00844B76` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00844AE7` → [sub_00B16064](../B1/Unknown_function_00B16064.md) (`tail-transfer`)
  - `0x00844B93` → [sub_00B16064](../B1/Unknown_function_00B16064.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008445AC  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
008445B0  55                              push rbp
008445B1  53                              push rbx
008445B2  56                              push rsi
008445B3  57                              push rdi
008445B4  41 54                           push r12
008445B6  41 55                           push r13
008445B8  41 56                           push r14
008445BA  41 57                           push r15
008445BC  48 8B EC                        mov rbp, rsp
008445BF  48 83 EC 78                     sub rsp, 0x78
008445C3  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008445C7  33 DB                           xor ebx, ebx
008445C9  83 C8 FF                        or eax, 0xffffffff
008445CC  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
008445D0  44 8B E8                        mov r13d, eax
008445D3  89 45 C8                        mov dword ptr [rbp - 0x38], eax
008445D6  44 8B F3                        mov r14d, ebx
008445D9  48 8B F1                        mov rsi, rcx
008445DC  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
008445DF  8B FB                           mov edi, ebx
008445E1  89 5D CC                        mov dword ptr [rbp - 0x34], ebx
008445E4  44 8B FB                        mov r15d, ebx
008445E7  89 5D 60                        mov dword ptr [rbp + 0x60], ebx
008445EA  89 5D 48                        mov dword ptr [rbp + 0x48], ebx
008445ED  44 89 75 58                     mov dword ptr [rbp + 0x58], r14d
008445F1  84 C0                           test al, al
008445F3  0F 88 D4 03 00 00               js 0x1408449cd
008445F9  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008445FD  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
00844601  48 8B 80 38 10 00 00            mov rax, qword ptr [rax + 0x1038]
00844608  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0084460C  48 39 58 60                     cmp qword ptr [rax + 0x60], rbx
00844610  0F 84 B7 03 00 00               je 0x1408449cd
00844616  48 39 5A 38                     cmp qword ptr [rdx + 0x38], rbx
0084461A  0F 84 AD 03 00 00               je 0x1408449cd
00844620  83 7E 44 0D                     cmp dword ptr [rsi + 0x44], 0xd
00844624  0F 84 A3 03 00 00               je 0x1408449cd
0084462A  E8 B1 25 01 00                  call 0x140856be0
0084462F  4C 8B E0                        mov r12, rax
00844632  48 85 C0                        test rax, rax
00844635  0F 84 22 04 00 00               je 0x140844a5d
0084463B  8B 56 44                        mov edx, dword ptr [rsi + 0x44]
0084463E  8B CA                           mov ecx, edx
00844640  85 D2                           test edx, edx
00844642  0F 84 C9 03 00 00               je 0x140844a11
00844648  83 E9 02                        sub ecx, 2
0084464B  0F 84 C0 03 00 00               je 0x140844a11
00844651  83 E9 02                        sub ecx, 2
00844654  74 09                           je 0x14084465f
00844656  83 E9 01                        sub ecx, 1
00844659  0F 85 72 03 00 00               jne 0x1408449d1
0084465F  8D 42 FC                        lea eax, [rdx - 4]
00844662  BB 50 00 00 00                  mov ebx, 0x50
00844667  83 F8 01                        cmp eax, 1
0084466A  4C 8D 45 C8                     lea r8, [rbp - 0x38]
0084466E  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00844672  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00844676  77 4E                           ja 0x1408446c6
00844678  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0084467F  44 8B 6E 5C                     mov r13d, dword ptr [rsi + 0x5c]
00844683  41 8B D5                        mov edx, r13d
00844686  0F 84 6D 03 00 00               je 0x1408449f9
0084468C  E8 CF 05 01 00                  call 0x140854c60
00844691  4C 8B F8                        mov r15, rax
00844694  48 85 C0                        test rax, rax
00844697  0F 84 B6 03 00 00               je 0x140844a53
0084469D  8B 40 04                        mov eax, dword ptr [rax + 4]
008446A0  3D 00 00 00 80                  cmp eax, 0x80000000
008446A5  8D 88 00 00 00 80               lea ecx, [rax - 0x80000000]
008446AB  0F 42 C8                        cmovb ecx, eax
008446AE  89 4D 60                        mov dword ptr [rbp + 0x60], ecx
008446B1  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
008446B4  8D 59 50                        lea ebx, [rcx + 0x50]
008446B7  83 FB 50                        cmp ebx, 0x50
008446BA  73 2F                           jae 0x1408446eb
008446BC  BB 95 00 00 C0                  mov ebx, 0xc0000095
008446C1  E9 B9 02 00 00                  jmp 0x14084497f
008446C6  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008446CD  44 8B 6E 58                     mov r13d, dword ptr [rsi + 0x58]
008446D1  41 8B D5                        mov edx, r13d
008446D4  0F 84 4E 03 00 00               je 0x140844a28
008446DA  E8 81 05 01 00                  call 0x140854c60
008446DF  4C 8B F8                        mov r15, rax
008446E2  48 85 C0                        test rax, rax
008446E5  0F 84 68 03 00 00               je 0x140844a53
008446EB  41 0F B7 57 02                  movzx edx, word ptr [r15 + 2]
008446F0  0F B7 CA                        movzx ecx, dx
008446F3  66 03 C9                        add cx, cx
008446F6  41 F6 47 10 01                  test byte ptr [r15 + 0x10], 1
008446FB  66 0F 44 CA                     cmove cx, dx
008446FF  8B D3                           mov edx, ebx
00844701  44 0F B7 F1                     movzx r14d, cx
00844705  44 89 75 58                     mov dword ptr [rbp + 0x58], r14d
00844709  41 03 DE                        add ebx, r14d
0084470C  3B DA                           cmp ebx, edx
0084470E  0F 82 6E 03 00 00               jb 0x140844a82
00844714  41 0F B7 04 24                  movzx eax, word ptr [r12]
00844719  03 D8                           add ebx, eax
0084471B  3B D8                           cmp ebx, eax
0084471D  0F 82 69 03 00 00               jb 0x140844a8c
00844723  8B D3                           mov edx, ebx
00844725  B9 00 01 00 00                  mov ecx, 0x100
0084472A  41 B8 43 4D 20 20               mov r8d, 0x20204d43
00844730  E8 BB D9 33 00                  call 0x140b820f0
00844735  48 8B F8                        mov rdi, rax
00844738  48 85 C0                        test rax, rax
0084473B  0F 84 55 03 00 00               je 0x140844a96
00844741  89 58 04                        mov dword ptr [rax + 4], ebx
00844744  33 DB                           xor ebx, ebx
00844746  C7 40 08 01 00 00 00            mov dword ptr [rax + 8], 1
0084474D  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
00844751  0F 10 40 58                     movups xmm0, xmmword ptr [rax + 0x58]
00844755  F3 0F 7F 47 10                  movdqu xmmword ptr [rdi + 0x10], xmm0
0084475A  41 0F B7 04 24                  movzx eax, word ptr [r12]
0084475F  66 89 47 20                     mov word ptr [rdi + 0x20], ax
00844763  41 0F B7 44 24 02               movzx eax, word ptr [r12 + 2]
00844769  66 89 47 22                     mov word ptr [rdi + 0x22], ax
0084476D  8B 56 44                        mov edx, dword ptr [rsi + 0x44]
00844770  8B CA                           mov ecx, edx
00844772  85 D2                           test edx, edx
00844774  0F 84 D6 03 00 00               je 0x140844b50
0084477A  83 E9 02                        sub ecx, 2
0084477D  0F 84 CD 03 00 00               je 0x140844b50
00844783  83 E9 02                        sub ecx, 2
00844786  74 09                           je 0x140844791
00844788  83 E9 01                        sub ecx, 1
0084478B  0F 85 18 01 00 00               jne 0x1408448a9
00844791  83 4D D0 FF                     or dword ptr [rbp - 0x30], 0xffffffff
00844795  33 C9                           xor ecx, ecx
00844797  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
0084479B  88 4D 50                        mov byte ptr [rbp + 0x50], cl
0084479E  89 4D D4                        mov dword ptr [rbp - 0x2c], ecx
008447A1  83 FA 04                        cmp edx, 4
008447A4  0F 84 43 02 00 00               je 0x1408449ed
008447AA  83 FA 05                        cmp edx, 5
008447AD  8B C1                           mov eax, ecx
008447AF  0F 95 C0                        setne al
008447B2  83 C0 04                        add eax, 4
008447B5  89 47 0C                        mov dword ptr [rdi + 0xc], eax
008447B8  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
008447BC  48 8D 5F 50                     lea rbx, [rdi + 0x50]
008447C0  48 89 5F 28                     mov qword ptr [rdi + 0x28], rbx
008447C4  48 8B CB                        mov rcx, rbx
008447C7  89 47 40                        mov dword ptr [rdi + 0x40], eax
008447CA  45 0F B7 04 24                  movzx r8d, word ptr [r12]
008447CF  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
008447D4  E8 67 20 E8 FF                  call 0x1406c6840
008447D9  41 0F B7 04 24                  movzx eax, word ptr [r12]
008447DE  49 8D 57 14                     lea rdx, [r15 + 0x14]
008447E2  48 03 D8                        add rbx, rax
008447E5  48 89 5F 38                     mov qword ptr [rdi + 0x38], rbx
008447E9  48 8B CB                        mov rcx, rbx
008447EC  41 F6 47 10 01                  test byte ptr [r15 + 0x10], 1
008447F1  0F 84 3B 02 00 00               je 0x140844a32
008447F7  45 0F B7 4F 02                  movzx r9d, word ptr [r15 + 2]
008447FC  4C 8B C2                        mov r8, rdx
008447FF  41 8B D6                        mov edx, r14d
00844802  E8 C9 98 00 00                  call 0x14084e0d0
00844807  33 C0                           xor eax, eax
00844809  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
0084480D  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00844810  66 89 47 32                     mov word ptr [rdi + 0x32], ax
00844814  66 89 47 30                     mov word ptr [rdi + 0x30], ax
00844818  83 7E 44 06                     cmp dword ptr [rsi + 0x44], 6
0084481C  0F 84 E1 01 00 00               je 0x140844a03
00844822  8B 45 60                        mov eax, dword ptr [rbp + 0x60]
00844825  4C 8D 4D 48                     lea r9, [rbp + 0x48]
00844829  89 47 44                        mov dword ptr [rdi + 0x44], eax
0084482C  4D 8B C7                        mov r8, r15
0084482F  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00844833  48 8D 45 D0                     lea rax, [rbp - 0x30]
00844837  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0084483C  41 8B D5                        mov edx, r13d
0084483F  48 8D 45 50                     lea rax, [rbp + 0x50]
00844843  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00844848  48 8D 45 D8                     lea rax, [rbp - 0x28]
0084484C  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00844850  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00844855  E8 56 25 01 00                  call 0x140856db0
0084485A  84 C0                           test al, al
0084485C  0F 84 34 02 00 00               je 0x140844a96
00844862  44 8B 45 48                     mov r8d, dword ptr [rbp + 0x48]
00844866  49 8D 0C 1E                     lea rcx, [r14 + rbx]
0084486A  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
0084486E  48 89 4F 48                     mov qword ptr [rdi + 0x48], rcx
00844872  E8 C9 1F E8 FF                  call 0x1406c6840
00844877  33 C0                           xor eax, eax
00844879  80 7D 50 01                     cmp byte ptr [rbp + 0x50], 1
0084487D  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
00844881  0F 84 B9 02 00 00               je 0x140844b40
00844887  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
0084488B  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0084488F  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00844893  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0084489A  0F 85 A9 01 00 00               jne 0x140844a49
008448A0  E8 9B 16 01 00                  call 0x140855f40
008448A5  33 DB                           xor ebx, ebx
008448A7  EB 24                           jmp 0x1408448cd
008448A9  83 E9 01                        sub ecx, 1
008448AC  0F 84 DF FE FF FF               je 0x140844791
008448B2  83 E9 01                        sub ecx, 1
008448B5  0F 84 5C 02 00 00               je 0x140844b17
008448BB  83 E9 01                        sub ecx, 1
008448BE  0F 84 28 02 00 00               je 0x140844aec
008448C4  83 F9 01                        cmp ecx, 1
008448C7  0F 84 D3 01 00 00               je 0x140844aa0
008448CD  8B 57 04                        mov edx, dword ptr [rdi + 4]
008448D0  48 8B CF                        mov rcx, rdi
008448D3  48 89 5F 28                     mov qword ptr [rdi + 0x28], rbx
008448D7  E8 28 E1 FF FF                  call 0x140842a04
008448DC  89 07                           mov dword ptr [rdi], eax
008448DE  48 8B 4E 38                     mov rcx, qword ptr [rsi + 0x38]
008448E2  48 83 C1 68                     add rcx, 0x68
008448E6  48 FF 15 13 C9 90 FF            call qword ptr [rip - 0x6f36ed]
008448ED  0F 1F 44 00 00                  nop dword ptr [rax + rax]
008448F2  4C 8B 6D E8                     mov r13, qword ptr [rbp - 0x18]
008448F6  48 8B D7                        mov rdx, rdi
008448F9  44 8B 47 04                     mov r8d, dword ptr [rdi + 4]
008448FD  F6 D8                           neg al
008448FF  48 8D 45 E0                     lea rax, [rbp - 0x20]
00844903  49 8B CD                        mov rcx, r13
00844906  45 1B C9                        sbb r9d, r9d
00844909  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084490E  41 83 E1 02                     and r9d, 2
00844912  E8 65 E1 FF FF                  call 0x140842a7c
00844917  8B D8                           mov ebx, eax
00844919  85 C0                           test eax, eax
0084491B  78 1C                           js 0x140844939
0084491D  48 8B 4E 38                     mov rcx, qword ptr [rsi + 0x38]
00844921  48 83 C1 68                     add rcx, 0x68
00844925  48 FF 15 D4 C8 90 FF            call qword ptr [rip - 0x6f372c]
0084492C  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00844931  84 C0                           test al, al
00844933  0F 85 5F 02 00 00               jne 0x140844b98
00844939  BA 78 00 00 00                  mov edx, 0x78
0084493E  B9 00 01 00 00                  mov ecx, 0x100
00844943  41 B8 43 4D 20 20               mov r8d, 0x20204d43
00844949  89 55 50                        mov dword ptr [rbp + 0x50], edx
0084494C  E8 9F D7 33 00                  call 0x140b820f0
00844951  4C 8B F0                        mov r14, rax
00844954  48 85 C0                        test rax, rax
00844957  74 21                           je 0x14084497a
00844959  49 8B 4D 58                     mov rcx, qword ptr [r13 + 0x58]
0084495D  4C 8D 45 50                     lea r8, [rbp + 0x50]
00844961  48 8B D0                        mov rdx, rax
00844964  48 FF 15 D5 C8 90 FF            call qword ptr [rip - 0x6f372b]
0084496B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00844970  33 D2                           xor edx, edx
00844972  49 8B CE                        mov rcx, r14
00844975  E8 F6 DE 33 00                  call 0x140b82870
0084497A  4D 85 FF                        test r15, r15
0084497D  74 1E                           je 0x14084499d
0084497F  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00844983  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00844987  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
0084498B  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00844992  0F 85 A7 00 00 00               jne 0x140844a3f
00844998  E8 A3 15 01 00                  call 0x140855f40
0084499D  48 85 FF                        test rdi, rdi
008449A0  74 0A                           je 0x1408449ac
008449A2  33 D2                           xor edx, edx
008449A4  48 8B CF                        mov rcx, rdi
008449A7  E8 C4 DE 33 00                  call 0x140b82870
008449AC  BA 43 4D 4E 62                  mov edx, 0x624e4d43
008449B1  49 8B CC                        mov rcx, r12
008449B4  E8 27 40 C0 FF                  call 0x1404489e0
008449B9  8B C3                           mov eax, ebx
008449BB  48 83 C4 78                     add rsp, 0x78
008449BF  41 5F                           pop r15
008449C1  41 5E                           pop r14
008449C3  41 5D                           pop r13
008449C5  41 5C                           pop r12
008449C7  5F                              pop rdi
008449C8  5E                              pop rsi
008449C9  5B                              pop rbx
008449CA  5D                              pop rbp
008449CB  C3                              ret
008449CC  CC                              int3
008449CD  33 C0                           xor eax, eax
008449CF  EB EA                           jmp 0x1408449bb
008449D1  83 E9 01                        sub ecx, 1
008449D4  0F 84 85 FC FF FF               je 0x14084465f
008449DA  83 E9 01                        sub ecx, 1
008449DD  0F 85 84 00 00 00               jne 0x140844a67
008449E3  BB 38 00 00 00                  mov ebx, 0x38
008449E8  E9 27 FD FF FF                  jmp 0x140844714
008449ED  C7 47 0C 03 00 00 00            mov dword ptr [rdi + 0xc], 3
008449F4  E9 BF FD FF FF                  jmp 0x1408447b8
008449F9  E8 B2 02 01 00                  call 0x140854cb0
008449FE  E9 8E FC FF FF                  jmp 0x140844691
00844A03  33 DB                           xor ebx, ebx
00844A05  89 5F 44                        mov dword ptr [rdi + 0x44], ebx
00844A08  48 89 5F 48                     mov qword ptr [rdi + 0x48], rbx
00844A0C  E9 BC FE FF FF                  jmp 0x1408448cd
00844A11  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00844A15  48 8B 48 58                     mov rcx, qword ptr [rax + 0x58]
00844A19  8B 59 18                        mov ebx, dword ptr [rcx + 0x18]
00844A1C  BA 40 00 00 00                  mov edx, 0x40
00844A21  03 DA                           add ebx, edx
00844A23  E9 E4 FC FF FF                  jmp 0x14084470c
00844A28  E8 83 02 01 00                  call 0x140854cb0
00844A2D  E9 AD FC FF FF                  jmp 0x1408446df
00844A32  4D 8B C6                        mov r8, r14
00844A35  E8 06 1E E8 FF                  call 0x1406c6840
00844A3A  E9 C8 FD FF FF                  jmp 0x140844807
00844A3F  E8 DC 81 01 00                  call 0x14085cc20
00844A44  E9 54 FF FF FF                  jmp 0x14084499d
00844A49  E8 D2 81 01 00                  call 0x14085cc20
00844A4E  E9 52 FE FF FF                  jmp 0x1408448a5
00844A53  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00844A58  E9 4F FF FF FF                  jmp 0x1408449ac
00844A5D  B8 9A 00 00 C0                  mov eax, 0xc000009a
00844A62  E9 54 FF FF FF                  jmp 0x1408449bb
00844A67  83 E9 01                        sub ecx, 1
00844A6A  0F 84 73 FF FF FF               je 0x1408449e3
00844A70  83 F9 01                        cmp ecx, 1
00844A73  0F 85 9B FC FF FF               jne 0x140844714
00844A79  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
00844A7D  8B 58 18                        mov ebx, dword ptr [rax + 0x18]
00844A80  EB 9A                           jmp 0x140844a1c
00844A82  BB 95 00 00 C0                  mov ebx, 0xc0000095
00844A87  E9 EE FE FF FF                  jmp 0x14084497a
00844A8C  BB 06 01 00 C0                  mov ebx, 0xc0000106
00844A91  E9 E4 FE FF FF                  jmp 0x14084497a
00844A96  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00844A9B  E9 DA FE FF FF                  jmp 0x14084497a
00844AA0  8A 46 64                        mov al, byte ptr [rsi + 0x64]
00844AA3  48 8D 5F 40                     lea rbx, [rdi + 0x40]
00844AA7  F6 D8                           neg al
00844AA9  1B C9                           sbb ecx, ecx
00844AAB  83 E1 02                        and ecx, 2
00844AAE  83 C1 08                        add ecx, 8
00844AB1  89 4F 0C                        mov dword ptr [rdi + 0xc], ecx
00844AB4  48 8B CB                        mov rcx, rbx
00844AB7  48 89 5F 28                     mov qword ptr [rdi + 0x28], rbx
00844ABB  45 0F B7 04 24                  movzx r8d, word ptr [r12]
00844AC0  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00844AC5  E8 76 1D E8 FF                  call 0x1406c6840
00844ACA  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
00844ACE  8B 50 18                        mov edx, dword ptr [rax + 0x18]
00844AD1  89 57 30                        mov dword ptr [rdi + 0x30], edx
00844AD4  44 8B C2                        mov r8d, edx
00844AD7  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00844ADC  48 03 CB                        add rcx, rbx
00844ADF  48 89 4F 38                     mov qword ptr [rdi + 0x38], rcx
00844AE3  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
00844AE7  E9 78 15 2D 00                  jmp 0x140b16064
00844AEC  C7 47 0C 07 00 00 00            mov dword ptr [rdi + 0xc], 7
00844AF3  48 8D 4F 38                     lea rcx, [rdi + 0x38]
00844AF7  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
00844AFB  45 0F B7 04 24                  movzx r8d, word ptr [r12]
00844B00  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00844B05  E8 36 1D E8 FF                  call 0x1406c6840
00844B0A  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
00844B0E  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
00844B12  E9 B6 FD FF FF                  jmp 0x1408448cd
00844B17  C7 47 0C 06 00 00 00            mov dword ptr [rdi + 0xc], 6
00844B1E  48 8D 4F 38                     lea rcx, [rdi + 0x38]
00844B22  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
00844B26  45 0F B7 04 24                  movzx r8d, word ptr [r12]
00844B2B  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00844B30  E8 0B 1D E8 FF                  call 0x1406c6840
00844B35  8B 46 58                        mov eax, dword ptr [rsi + 0x58]
00844B38  89 47 30                        mov dword ptr [rdi + 0x30], eax
00844B3B  E9 8D FD FF FF                  jmp 0x1408448cd
00844B40  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00844B44  33 D2                           xor edx, edx
00844B46  E8 25 DD 33 00                  call 0x140b82870
00844B4B  E9 55 FD FF FF                  jmp 0x1408448a5
00844B50  F7 DA                           neg edx
00844B52  48 8D 5F 40                     lea rbx, [rdi + 0x40]
00844B56  48 8B CB                        mov rcx, rbx
00844B59  1B C0                           sbb eax, eax
00844B5B  F7 D8                           neg eax
00844B5D  FF C0                           inc eax
00844B5F  89 47 0C                        mov dword ptr [rdi + 0xc], eax
00844B62  8B 46 48                        mov eax, dword ptr [rsi + 0x48]
00844B65  89 47 30                        mov dword ptr [rdi + 0x30], eax
00844B68  48 89 5F 28                     mov qword ptr [rdi + 0x28], rbx
00844B6C  45 0F B7 04 24                  movzx r8d, word ptr [r12]
00844B71  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00844B76  E8 C5 1C E8 FF                  call 0x1406c6840
00844B7B  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00844B80  48 03 CB                        add rcx, rbx
00844B83  48 89 4F 38                     mov qword ptr [rdi + 0x38], rcx
00844B87  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00844B8B  48 8B 50 58                     mov rdx, qword ptr [rax + 0x58]
00844B8F  44 8B 42 18                     mov r8d, dword ptr [rdx + 0x18]
00844B93  E9 CC 14 2D 00                  jmp 0x140b16064
00844B98  4C 8B 4E 38                     mov r9, qword ptr [rsi + 0x38]
00844B9C  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
00844BA0  49 89 51 68                     mov qword ptr [r9 + 0x68], rdx
00844BA4  E9 90 FD FF FF                  jmp 0x140844939
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmAddLogForAction(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (120);
    v_rbx = 0;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_m60 = 0;
    v_stack_m78 = (unsigned int)(result);
    v_stack_m74 = 0;
    v_stack_p20 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = 0;
    if (sign_flag) goto loc_008449CD;
    v_stack_m58 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 4152);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 4152) + 96)) == 0) goto loc_008449CD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 56)) == 0) goto loc_008449CD;
    if ((*(unsigned int *)(a1 + 68)) == 13) goto loc_008449CD;
    result = CmpConstructName(*(unsigned __int64 *)(a1 + 48), *(unsigned __int64 *)(a1 + 56), a3, a4);
    if (result == 0) goto loc_00844A5D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68))) == 0) goto loc_00844A11;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68))))) - (2));
    if (condition_is_equal) goto loc_00844A11;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_0084465F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_008449D1;
loc_0084465F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68)) - 4)) > 1) goto loc_008446C6;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) == 0) goto loc_008449F9;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 92)))), v_stack_m78, a4);
loc_00844691:
    if (result == 0) goto loc_00844A53;
    a1 = (unsigned int)(*(unsigned int *)(result + 4)) - 2147483648;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) < 0x80000000ULL) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4))); }
    v_stack_p20 = (unsigned int)(a1);
    v_stack_p8 = (unsigned int)(a1);
    if (((unsigned int)(a1 + 80)) >= 80) goto loc_008446EB;
    goto loc_0084497F;
loc_008446C6:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00844A28;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)))), v_stack_m78, a4);
loc_008446DF:
    if (result == 0) goto loc_00844A53;
loc_008446EB:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result + 2))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(result + 2)))));
    if (((*(unsigned __int8 *)(result + 16)) & (1)) == 0) { a1 = (unsigned __int16)(*(unsigned __int16 *)(result + 2)); }
    v_stack_p18 = (unsigned int)((unsigned __int16)(a1));
    v_rbx = (unsigned int)(((unsigned int)(0xC0000095ULL)) + ((unsigned int)((unsigned __int16)(a1))));
loc_0084470C:
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)))))) goto loc_00844A82;
loc_00844714:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(*(unsigned __int16 *)(result))));
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int16 *)(result)))) goto loc_00844A8C;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x20204D43ULL), a4);
    if (result == 0) goto loc_00844A96;
    *(unsigned int *)(result + 4) = (unsigned int)(v_rbx);
    v_rbx = 0;
    *(unsigned int *)(result + 8) = 1;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int16 *)(result + 32) = (unsigned __int16)(*(unsigned __int16 *)(result));
    *(unsigned __int16 *)(result + 34) = (unsigned __int16)(*(unsigned __int16 *)(result + 2));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68))) == 0) goto loc_00844B50;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68))))) - (2));
    if (condition_is_equal) goto loc_00844B50;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00844791;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_008448A9;
loc_00844791:
    a1 = 0;
    v_stack_m68 = 0;
    v_stack_p10 = 0;
    v_stack_m6C = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68)))) == 4) goto loc_008449ED;
    result = (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68)))) != 5) ? 1 : 0;
    result = (unsigned int)((result) + (4));
    *(unsigned int *)(result + 12) = (unsigned int)(result);
loc_008447B8:
    *(unsigned __int64 *)(result + 40) = result + 80;
    *(unsigned int *)(result + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)));
    result = memcpy(result + 80, *(unsigned __int64 *)(result + 8), *(unsigned __int16 *)(result), a4);
    v_rbx = (result + 80) + (*(unsigned __int16 *)(result));
    *(unsigned __int64 *)(result + 56) = v_rbx;
    if (((*(unsigned __int8 *)(result + 16)) & (1)) == 0) goto loc_00844A32;
    result = CmpCopyCompressedName(v_rbx, (unsigned int)((unsigned int)((unsigned __int16)(a1))), result + 20, *(unsigned __int16 *)(result + 2));
loc_00844807:
    result = 0;
    *(unsigned __int64 *)(result + 56) = 0;
    *(unsigned __int16 *)(result + 50) = (unsigned __int16)((unsigned int)(v_stack_p18));
    *(unsigned __int16 *)(result + 48) = (unsigned __int16)((unsigned int)(v_stack_p18));
    if ((*(unsigned int *)(a1 + 68)) == 6) goto loc_00844A03;
    *(unsigned int *)(result + 68) = (unsigned int)((unsigned int)(v_stack_p20));
    v_stack_m88 = v_stack_m70;
    v_stack_m90 = v_stack_p10;
    v_stack_m98 = v_stack_m68;
    result = CmpGetValueData(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)))), 0, v_stack_p8);
    if ((unsigned __int8)(result) == 0) goto loc_00844A96;
    *(unsigned __int64 *)(result + 72) = (unsigned __int16)(a1) + v_rbx * 1;
    result = memcpy((unsigned __int16)(a1) + v_rbx * 1, v_stack_m68, (unsigned int)(v_stack_p8), v_stack_p8);
    result = 0;
    *(unsigned __int64 *)(result + 72) = 0;
    if (v_stack_p10 == 1) goto loc_00844B40;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) != 0) goto loc_00844A49;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_m70, (unsigned int)(v_stack_p8), v_stack_p8);
loc_008448A5:
    v_rbx = 0;
    goto loc_008448CD;
loc_008448A9:
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32)) - (1));
    if (condition_is_equal) goto loc_00844791;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00844B17;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00844AEC;
    if (((unsigned int)(a1)) == 1) goto loc_00844AA0;
loc_008448CD:
    *(unsigned __int64 *)(result + 40) = 0;
    result = HvBufferCheckSum(result, (unsigned int)(*(unsigned int *)(result + 4)), (unsigned int)(v_stack_p8), v_stack_p8);
    *(unsigned int *)(result) = (unsigned int)(result);
    a1 = (*(unsigned __int64 *)(a1 + 56)) + (104);
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsLsnInvalid(a1, (unsigned int)(*(unsigned int *)(result + 4)), (unsigned int)(v_stack_p8), v_stack_p8);
    result = (unsigned __int8)(-(result));
    v_stack_m98 = v_stack_m60;
    a4 = (unsigned int)((v_stack_p8) & (2));
    result = CmpTransWriteLog(v_stack_m58, result, (unsigned int)(*(unsigned int *)(result + 4)), a4);
    if (sign_flag) goto loc_00844939;
    a1 = (*(unsigned __int64 *)(a1 + 56)) + (104);
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsLsnInvalid(a1, result, (unsigned int)(*(unsigned int *)(result + 4)), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00844B98;
loc_00844939:
    v_stack_p10 = 120;
    result = ExAllocatePool2(256, 120, (unsigned int)(0x20204D43ULL), a4);
    if (result != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m58 + 88);
        a3 = v_stack_p10;
        a2 = result;
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsGetLogFileInformation(a1, a2, a3, a4);
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (result == 0) goto loc_0084499D;
loc_0084497F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32) + 140)) & (1)) != 0) goto loc_00844A3F;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 32), v_stack_m78, a3, a4);
loc_0084499D:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = CmpFreePoolWithTag(result, (unsigned int)(0x624E4D43ULL), a3, a4);
loc_008449BB:
    v_rsp = (v_rsp) + (120);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008449CD:
    result = 0;
    goto loc_008449BB;
loc_008449D1:
    a1 = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0084465F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00844A67;
loc_008449E3:
    goto loc_00844714;
loc_008449ED:
    *(unsigned int *)(result + 12) = 3;
    goto loc_008447B8;
loc_008449F9:
    result = HvpGetCellPaged(a1, (unsigned int)(0x624E4D43ULL), a3, a4);
    goto loc_00844691;
loc_00844A03:
    v_rbx = 0;
    *(unsigned int *)(result + 68) = 0;
    *(unsigned __int64 *)(result + 72) = 0;
    goto loc_008448CD;
loc_00844A11:
loc_00844A1C:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 88) + 24))) + (64));
    goto loc_0084470C;
loc_00844A28:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 88), 64, a3, a4);
    goto loc_008446DF;
loc_00844A32:
    result = memcpy(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 88), 64, result, a4);
    goto loc_00844807;
loc_00844A3F:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 88), 64, result, a4);
    goto loc_0084499D;
loc_00844A49:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 88), 64, result, a4);
    goto loc_008448A5;
loc_00844A53:
    goto loc_008449AC;
loc_00844A5D:
    goto loc_008449BB;
loc_00844A67:
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 88)) - (1));
    if (condition_is_equal) goto loc_008449E3;
    if (((unsigned int)(a1)) != 1) goto loc_00844714;
    goto loc_00844A1C;
loc_00844A82:
    goto loc_0084497A;
loc_00844A8C:
    goto loc_0084497A;
loc_00844A96:
    goto loc_0084497A;
loc_00844AA0:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 100)));
    a1 = (unsigned int)((a1) & (2));
    a1 = (unsigned int)((a1) + (8));
    *(unsigned int *)(result + 12) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 40) = result + 64;
    result = memcpy(result + 64, *(unsigned __int64 *)(result + 8), *(unsigned __int16 *)(result), a4);
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 88) + 24)));
    a1 = (*(unsigned __int16 *)(result)) + (result + 64);
    *(unsigned __int64 *)(result + 56) = a1;
loc_00844AEC:
    *(unsigned int *)(result + 12) = 7;
    *(unsigned __int64 *)(result + 40) = result + 56;
    result = memcpy(result + 56, *(unsigned __int64 *)(result + 8), *(unsigned __int16 *)(result), a4);
    *(unsigned __int64 *)(result + 48) = *(unsigned __int64 *)(a1 + 88);
    goto loc_008448CD;
loc_00844B17:
    *(unsigned int *)(result + 12) = 6;
    *(unsigned __int64 *)(result + 40) = result + 56;
    result = memcpy(result + 56, *(unsigned __int64 *)(result + 8), *(unsigned __int16 *)(result), a4);
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)));
    goto loc_008448CD;
loc_00844B40:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m68, a2, *(unsigned __int16 *)(result), a4);
    goto loc_008448A5;
loc_00844B50:
    a2 = (unsigned int)(-(a2));
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) + 1);
    *(unsigned int *)(result + 12) = (unsigned int)(result);
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72)));
    *(unsigned __int64 *)(result + 40) = result + 64;
    result = memcpy(result + 64, *(unsigned __int64 *)(result + 8), *(unsigned __int16 *)(result), a4);
    a1 = (*(unsigned __int16 *)(result)) + (result + 64);
    *(unsigned __int64 *)(result + 56) = a1;
loc_00844B98:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 104) = v_stack_m60;
    goto loc_00844939;
}
```

## 5. (Beta) C Style

```c
int64_t CmAddLogForAction(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (120);
    local_rbx = 0;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_m60 = 0;
    v_stack_m78 = (uint32_t)(result);
    v_stack_m74 = 0;
    v_stack_p20 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = 0;
    if (sign_flag) goto loc_008449CD;
    v_stack_m58 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x1038);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x1038) + 0x60)) == 0) goto loc_008449CD;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x38)) == 0) goto loc_008449CD;
    if ((*(uint32_t *)(arg1 + 0x44)) == 13) goto loc_008449CD;
    result = CmpConstructName(*(uint64_t *)(arg1 + 0x30), *(uint64_t *)(arg1 + 0x38), a3, a4);
    if (result == 0) goto loc_00844A5D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44))) == 0) goto loc_00844A11;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44))))) - (2));
    if (condition_is_equal) goto loc_00844A11;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_0084465F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_008449D1;
loc_0084465F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44)) - 4)) > 1) goto loc_008446C6;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) == 0) goto loc_008449F9;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5C)))), v_stack_m78, a4);
loc_00844691:
    if (result == 0) goto loc_00844A53;
    Arg1 = (uint32_t)(*(uint32_t *)(result + 0x4)) - 2147483648;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) < 0x80000000ULL) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))); }
    v_stack_p20 = (uint32_t)(Arg1);
    v_stack_p8 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1 + 80)) >= 80) goto loc_008446EB;
    goto loc_0084497F;
loc_008446C6:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00844A28;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)))), v_stack_m78, a4);
loc_008446DF:
    if (result == 0) goto loc_00844A53;
loc_008446EB:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(result + 0x2))) + ((uint16_t)((uint16_t)(*(uint16_t *)(result + 0x2)))));
    if (((*(uint8_t *)(result + 0x10)) & (1)) == 0) { Arg1 = (uint16_t)(*(uint16_t *)(result + 0x2)); }
    v_stack_p18 = (uint32_t)((uint16_t)(Arg1));
    local_rbx = (uint32_t)(((uint32_t)(0xC0000095ULL)) + ((uint32_t)((uint16_t)(Arg1))));
loc_0084470C:
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)))))) goto loc_00844A82;
loc_00844714:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(*(uint16_t *)(result))));
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint16_t *)(result)))) goto loc_00844A8C;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x20204D43ULL), a4);
    if (result == 0) goto loc_00844A96;
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_rbx);
    local_rbx = 0;
    *(uint32_t *)(result + 0x8) = 1;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint16_t *)(result + 0x20) = (uint16_t)(*(uint16_t *)(result));
    *(uint16_t *)(result + 0x22) = (uint16_t)(*(uint16_t *)(result + 0x2));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44))) == 0) goto loc_00844B50;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44))))) - (2));
    if (condition_is_equal) goto loc_00844B50;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00844791;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_008448A9;
loc_00844791:
    Arg1 = 0;
    v_stack_m68 = 0;
    v_stack_p10 = 0;
    v_stack_m6C = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44)))) == 4) goto loc_008449ED;
    result = (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44)))) != 5) ? 1 : 0;
    result = (uint32_t)((result) + (4));
    *(uint32_t *)(result + 0xC) = (uint32_t)(result);
loc_008447B8:
    *(uint64_t *)(result + 0x28) = result + 80;
    *(uint32_t *)(result + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)));
    result = memcpy(result + 80, *(uint64_t *)(result + 0x8), *(uint16_t *)(result), a4);
    local_rbx = (result + 80) + (*(uint16_t *)(result));
    *(uint64_t *)(result + 0x38) = local_rbx;
    if (((*(uint8_t *)(result + 0x10)) & (1)) == 0) goto loc_00844A32;
    result = CmpCopyCompressedName(local_rbx, (uint32_t)((uint32_t)((uint16_t)(Arg1))), result + 20, *(uint16_t *)(result + 0x2));
loc_00844807:
    result = 0;
    *(uint64_t *)(result + 0x38) = 0;
    *(uint16_t *)(result + 0x32) = (uint16_t)((uint32_t)(v_stack_p18));
    *(uint16_t *)(result + 0x30) = (uint16_t)((uint32_t)(v_stack_p18));
    if ((*(uint32_t *)(arg1 + 0x44)) == 6) goto loc_00844A03;
    *(uint32_t *)(result + 0x44) = (uint32_t)((uint32_t)(v_stack_p20));
    v_stack_m88 = v_stack_m70;
    v_stack_m90 = v_stack_p10;
    v_stack_m98 = v_stack_m68;
    result = CmpGetValueData(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)))), 0, v_stack_p8);
    if ((uint8_t)(result) == 0) goto loc_00844A96;
    *(uint64_t *)(result + 0x48) = (uint16_t)(Arg1) + local_rbx * 1;
    result = memcpy((uint16_t)(Arg1) + local_rbx * 1, v_stack_m68, (uint32_t)(v_stack_p8), v_stack_p8);
    result = 0;
    *(uint64_t *)(result + 0x48) = 0;
    if (v_stack_p10 == 1) goto loc_00844B40;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00844A49;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_m70, (uint32_t)(v_stack_p8), v_stack_p8);
loc_008448A5:
    local_rbx = 0;
    goto loc_008448CD;
loc_008448A9:
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20)) - (1));
    if (condition_is_equal) goto loc_00844791;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00844B17;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00844AEC;
    if (((uint32_t)(Arg1)) == 1) goto loc_00844AA0;
loc_008448CD:
    *(uint64_t *)(result + 0x28) = 0;
    result = HvBufferCheckSum(result, (uint32_t)(*(uint32_t *)(result + 0x4)), (uint32_t)(v_stack_p8), v_stack_p8);
    *(uint32_t *)(result) = (uint32_t)(result);
    Arg1 = (*(uint64_t *)(arg1 + 0x38)) + (104);
    result = kernel_indirect_call(Arg1, (uint32_t)(*(uint32_t *)(result + 0x4)), (uint32_t)(v_stack_p8), v_stack_p8);
    result = (uint8_t)(-(result));
    v_stack_m98 = v_stack_m60;
    a4 = (uint32_t)((v_stack_p8) & (2));
    result = CmpTransWriteLog(v_stack_m58, result, (uint32_t)(*(uint32_t *)(result + 0x4)), a4);
    if (sign_flag) goto loc_00844939;
    Arg1 = (*(uint64_t *)(arg1 + 0x38)) + (104);
    result = kernel_indirect_call(Arg1, result, (uint32_t)(*(uint32_t *)(result + 0x4)), a4);
    if ((uint8_t)(result) != 0) goto loc_00844B98;
loc_00844939:
    v_stack_p10 = 120;
    result = ExAllocatePool2(256, 120, (uint32_t)(0x20204D43ULL), a4);
    if (result != 0) {
        Arg1 = *(uint64_t *)(v_stack_m58 + 0x58);
        a3 = v_stack_p10;
        Arg2 = result;
        result = kernel_indirect_call(Arg1, Arg2, a3, a4);
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    if (result == 0) goto loc_0084499D;
loc_0084497F:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00844A3F;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x20), v_stack_m78, a3, a4);
loc_0084499D:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    result = CmpFreePoolWithTag(result, (uint32_t)(0x624E4D43ULL), a3, a4);
loc_008449BB:
    local_rsp = (local_rsp) + (120);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008449CD:
    result = 0;
    goto loc_008449BB;
loc_008449D1:
    Arg1 = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0084465F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00844A67;
loc_008449E3:
    goto loc_00844714;
loc_008449ED:
    *(uint32_t *)(result + 0xC) = 3;
    goto loc_008447B8;
loc_008449F9:
    result = HvpGetCellPaged(Arg1, (uint32_t)(0x624E4D43ULL), a3, a4);
    goto loc_00844691;
loc_00844A03:
    local_rbx = 0;
    *(uint32_t *)(result + 0x44) = 0;
    *(uint64_t *)(result + 0x48) = 0;
    goto loc_008448CD;
loc_00844A11:
loc_00844A1C:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x58) + 0x18))) + (64));
    goto loc_0084470C;
loc_00844A28:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x58), 64, a3, a4);
    goto loc_008446DF;
loc_00844A32:
    result = memcpy(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x58), 64, result, a4);
    goto loc_00844807;
loc_00844A3F:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x58), 64, result, a4);
    goto loc_0084499D;
loc_00844A49:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x58), 64, result, a4);
    goto loc_008448A5;
loc_00844A53:
    goto loc_008449AC;
loc_00844A5D:
    goto loc_008449BB;
loc_00844A67:
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x58)) - (1));
    if (condition_is_equal) goto loc_008449E3;
    if (((uint32_t)(Arg1)) != 1) goto loc_00844714;
    goto loc_00844A1C;
loc_00844A82:
    goto loc_0084497A;
loc_00844A8C:
    goto loc_0084497A;
loc_00844A96:
    goto loc_0084497A;
loc_00844AA0:
    result = (uint8_t)(-(*(uint8_t *)(arg1 + 0x64)));
    Arg1 = (uint32_t)((Arg1) & (2));
    Arg1 = (uint32_t)((Arg1) + (8));
    *(uint32_t *)(result + 0xC) = (uint32_t)(Arg1);
    *(uint64_t *)(result + 0x28) = result + 64;
    result = memcpy(result + 64, *(uint64_t *)(result + 0x8), *(uint16_t *)(result), a4);
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x58) + 0x18)));
    Arg1 = (*(uint16_t *)(result)) + (result + 64);
    *(void **)(result + 0x38) = Arg1;
loc_00844AEC:
    *(uint32_t *)(result + 0xC) = 7;
    *(uint64_t *)(result + 0x28) = result + 56;
    result = memcpy(result + 56, *(uint64_t *)(result + 0x8), *(uint16_t *)(result), a4);
    *(uint64_t *)(result + 0x30) = *(uint64_t *)(arg1 + 0x58);
    goto loc_008448CD;
loc_00844B17:
    *(uint32_t *)(result + 0xC) = 6;
    *(uint64_t *)(result + 0x28) = result + 56;
    result = memcpy(result + 56, *(uint64_t *)(result + 0x8), *(uint16_t *)(result), a4);
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    goto loc_008448CD;
loc_00844B40:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m68, Arg2, *(uint16_t *)(result), a4);
    goto loc_008448A5;
loc_00844B50:
    Arg2 = (uint32_t)(-(Arg2));
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) + 1);
    *(uint32_t *)(result + 0xC) = (uint32_t)(result);
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48)));
    *(uint64_t *)(result + 0x28) = result + 64;
    result = memcpy(result + 64, *(uint64_t *)(result + 0x8), *(uint16_t *)(result), a4);
    Arg1 = (*(uint16_t *)(result)) + (result + 64);
    *(void **)(result + 0x38) = Arg1;
loc_00844B98:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x68) = v_stack_m60;
    goto loc_00844939;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x44` | `32` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x58` | `32` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x5C` | `32` | `R` |
| `Arg1` | `+ 0x64` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008445AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
