# FsRtlCopyWrite

- RVA: `0x00A48210`–`0x00A48695` (길이 `1,157` bytes)
- VA: `0x0000000140A48210`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AFA20`
- 디코드: `268`개 명령, `1,157/1,157` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A4825B` → [IoGetTopLevelIrp](../../text/41/IoGetTopLevelIrp_function_0041D910.md) (function, `0x0041D910`)
- `0x00A4827D` → [CcCanIWrite](../../text/38/CcCanIWrite_function_00388250.md) (function, `0x00388250`)
- `0x00A4829F` → [CcCopyWriteWontFlush](../../text/38/CcCopyWriteWontFlush_function_00386E40.md) (function, `0x00386E40`)
- `0x00A4830A` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A483AC` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (function, `0x0042A7D0`)
- `0x00A483E4` → [CcCopyWrite](../../text/3C/CcCopyWrite_function_003CA4C0.md) (function, `0x003CA4C0`)
- `0x00A48403` → [CcZeroData](../../text/38/CcZeroData_function_00387F00.md) (function, `0x00387F00`)
- `0x00A4843B` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (function, `0x0042A7D0`)
- `0x00A48499` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A4849E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A48522` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A4856C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A4858E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A4859E` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A485EE` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A485FF` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A4862A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A4862F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A48651` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A4865E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A48677` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A48684` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x00A4825B` → [IoGetTopLevelIrp](../../text/41/IoGetTopLevelIrp_function_0041D910.md) (`PAGE` → `.text`)
  - `0x00A4827D` → [CcCanIWrite](../../text/38/CcCanIWrite_function_00388250.md) (`PAGE` → `.text`)
  - `0x00A4829F` → [CcCopyWriteWontFlush](../../text/38/CcCopyWriteWontFlush_function_00386E40.md) (`PAGE` → `.text`)
  - `0x00A4830A` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A483AC` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (`PAGE` → `.text`)
  - `0x00A483E4` → [CcCopyWrite](../../text/3C/CcCopyWrite_function_003CA4C0.md) (`PAGE` → `.text`)
  - `0x00A48403` → [CcZeroData](../../text/38/CcZeroData_function_00387F00.md) (`PAGE` → `.text`)
  - `0x00A4843B` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (`PAGE` → `.text`)
  - `0x00A48499` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A4849E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A48522` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A4856C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A4858E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A4859E` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A485EE` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A485FF` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A4862A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A4862F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A48651` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A4865E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A48677` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A48684` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00A485B0` → [sub_00B3B744](../B3/Unknown_function_00B3B744.md) (`tail-transfer`)
  - `0x00A485CF` → [sub_00B3B744 + 0x7](../B3/Unknown_function_00B3B744.md) (`tail-transfer`)
  - `0x00A485E6` → [sub_00B3B744 + 0x2D](../B3/Unknown_function_00B3B744.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A48210  48 8B C4                        mov rax, rsp
00A48213  44 88 48 20                     mov byte ptr [rax + 0x20], r9b
00A48217  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00A4821B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00A4821F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A48223  53                              push rbx
00A48224  56                              push rsi
00A48225  57                              push rdi
00A48226  41 54                           push r12
00A48228  41 55                           push r13
00A4822A  41 56                           push r14
00A4822C  41 57                           push r15
00A4822E  48 81 EC 90 00 00 00            sub rsp, 0x90
00A48235  41 8A F1                        mov sil, r9b
00A48238  41 8B D8                        mov ebx, r8d
00A4823B  48 8B FA                        mov rdi, rdx
00A4823E  4C 8B E9                        mov r13, rcx
00A48241  45 33 E4                        xor r12d, r12d
00A48244  C6 40 88 01                     mov byte ptr [rax - 0x78], 1
00A48248  44 88 64 24 52                  mov byte ptr [rsp + 0x52], r12b
00A4824D  83 3A FF                        cmp dword ptr [rdx], -1
00A48250  0F 84 BC 03 00 00               je 0x140a48612
00A48256  44 88 64 24 51                  mov byte ptr [rsp + 0x51], r12b
00A4825B  E8 B0 56 9D FF                  call 0x14041d910
00A48260  48 85 C0                        test rax, rax
00A48263  0F 85 51 02 00 00               jne 0x140a484ba
00A48269  4D 8B 7D 18                     mov r15, qword ptr [r13 + 0x18]
00A4826D  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
00A48272  45 33 C9                        xor r9d, r9d
00A48275  44 8A C6                        mov r8b, sil
00A48278  8B D3                           mov edx, ebx
00A4827A  49 8B CD                        mov rcx, r13
00A4827D  E8 CE FF 93 FF                  call 0x140388250
00A48282  84 C0                           test al, al
00A48284  0F 84 30 02 00 00               je 0x140a484ba
00A4828A  41 8B 45 50                     mov eax, dword ptr [r13 + 0x50]
00A4828E  A8 10                           test al, 0x10
00A48290  0F 85 24 02 00 00               jne 0x140a484ba
00A48296  44 8B C3                        mov r8d, ebx
00A48299  48 8B D7                        mov rdx, rdi
00A4829C  49 8B CD                        mov rcx, r13
00A4829F  E8 9C EB 93 FF                  call 0x140386e40
00A482A4  84 C0                           test al, al
00A482A6  0F 84 0E 02 00 00               je 0x140a484ba
00A482AC  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00A482B4  44 89 20                        mov dword ptr [rax], r12d
00A482B7  48 8B CB                        mov rcx, rbx
00A482BA  48 89 58 08                     mov qword ptr [rax + 8], rbx
00A482BE  85 DB                           test ebx, ebx
00A482C0  0F 84 C8 03 00 00               je 0x140a4868e
00A482C6  49 8B F4                        mov rsi, r12
00A482C9  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
00A482CE  4D 8B F4                        mov r14, r12
00A482D1  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00A482D6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A482DF  48 83 CA FF                     or rdx, 0xffffffffffffffff
00A482E3  66 01 90 E4 01 00 00            add word ptr [rax + 0x1e4], dx
00A482EA  90                              nop
00A482EB  44 38 64 24 51                  cmp byte ptr [rsp + 0x51], r12b
00A482F0  75 0D                           jne 0x140a482ff
00A482F2  48 03 0F                        add rcx, qword ptr [rdi]
00A482F5  49 3B 4F 28                     cmp rcx, qword ptr [r15 + 0x28]
00A482F9  0F 8E 62 02 00 00               jle 0x140a48561
00A482FF  8A 94 24 E8 00 00 00            mov dl, byte ptr [rsp + 0xe8]
00A48306  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00A4830A  E8 11 CB 7C FF                  call 0x140214e20
00A4830F  84 C0                           test al, al
00A48311  0F 84 18 03 00 00               je 0x140a4862f
00A48317  44 8A D6                        mov r10b, sil
00A4831A  44 38 64 24 51                  cmp byte ptr [rsp + 0x51], r12b
00A4831F  0F 85 E4 02 00 00               jne 0x140a48609
00A48325  48 8B 3F                        mov rdi, qword ptr [rdi]
00A48328  48 03 DF                        add rbx, rdi
00A4832B  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00A48330  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00A48335  4D 39 65 30                     cmp qword ptr [r13 + 0x30], r12
00A48339  0F 84 E7 02 00 00               je 0x140a48626
00A4833F  45 8A 47 05                     mov r8b, byte ptr [r15 + 5]
00A48343  45 84 C0                        test r8b, r8b
00A48346  0F 84 DA 02 00 00               je 0x140a48626
00A4834C  4D 8B 4F 28                     mov r9, qword ptr [r15 + 0x28]
00A48350  49 8D 81 00 20 00 00            lea rax, [r9 + 0x2000]
00A48357  48 3B F8                        cmp rdi, rax
00A4835A  0F 8D C6 02 00 00               jge 0x140a48626
00A48360  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00A4836A  48 2B CF                        sub rcx, rdi
00A4836D  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00A48374  48 3B CA                        cmp rcx, rdx
00A48377  0F 8C A9 02 00 00               jl 0x140a48626
00A4837D  49 3B 5F 18                     cmp rbx, qword ptr [r15 + 0x18]
00A48381  0F 8F 9F 02 00 00               jg 0x140a48626
00A48387  45 84 D2                        test r10b, r10b
00A4838A  0F 85 F1 01 00 00               jne 0x140a48581
00A48390  41 80 F8 02                     cmp r8b, 2
00A48394  0F 84 24 01 00 00               je 0x140a484be
00A4839A  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00A4839E  48 3B D8                        cmp rbx, rax
00A483A1  0F 8F 8D 01 00 00               jg 0x140a48534
00A483A7  B9 04 00 00 00                  mov ecx, 4
00A483AC  E8 1F 24 9E FF                  call 0x14042a7d0
00A483B1  90                              nop
00A483B2  49 3B 7F 28                     cmp rdi, qword ptr [r15 + 0x28]
00A483B6  7F 37                           jg 0x140a483ef
00A483B8  44 38 64 24 50                  cmp byte ptr [rsp + 0x50], r12b
00A483BD  74 4F                           je 0x140a4840e
00A483BF  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00A483C7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A483CC  44 8A 8C 24 E8 00 00 00         mov r9b, byte ptr [rsp + 0xe8]
00A483D4  44 8B 84 24 E0 00 00 00         mov r8d, dword ptr [rsp + 0xe0]
00A483DC  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00A483E1  49 8B CD                        mov rcx, r13
00A483E4  E8 D7 20 98 FF                  call 0x1403ca4c0
00A483E9  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00A483ED  EB 1F                           jmp 0x140a4840e
00A483EF  49 8D 57 28                     lea rdx, [r15 + 0x28]
00A483F3  44 8A 8C 24 E8 00 00 00         mov r9b, byte ptr [rsp + 0xe8]
00A483FB  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00A48400  49 8B CD                        mov rcx, r13
00A48403  E8 F8 FA 93 FF                  call 0x140387f00
00A48408  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00A4840C  EB AA                           jmp 0x140a483b8
00A4840E  EB 29                           jmp 0x140a48439
00A48410  C6 44 24 50 00                  mov byte ptr [rsp + 0x50], 0
00A48415  45 33 E4                        xor r12d, r12d
00A48418  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
00A48420  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
00A48425  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00A4842A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00A4842F  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00A48434  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00A48439  33 C9                           xor ecx, ecx
00A4843B  E8 90 23 9E FF                  call 0x14042a7d0
00A48440  44 38 64 24 50                  cmp byte ptr [rsp + 0x50], r12b
00A48445  0F 84 89 01 00 00               je 0x140a485d4
00A4844B  49 3B 5F 28                     cmp rbx, qword ptr [r15 + 0x28]
00A4844F  7E 12                           jle 0x140a48463
00A48451  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00A48455  41 39 47 2C                     cmp dword ptr [r15 + 0x2c], eax
00A48459  0F 85 09 02 00 00               jne 0x140a48668
00A4845F  49 89 5F 28                     mov qword ptr [r15 + 0x28], rbx
00A48463  41 0F BA 6D 50 0C               bts dword ptr [r13 + 0x50], 0xc
00A48469  44 38 64 24 52                  cmp byte ptr [rsp + 0x52], r12b
00A4846E  74 12                           je 0x140a48482
00A48470  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
00A48474  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00A48478  48 89 59 08                     mov qword ptr [rcx + 8], rbx
00A4847C  41 0F BA 6D 50 0D               bts dword ptr [r13 + 0x50], 0xd
00A48482  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00A48489  48 03 C7                        add rax, rdi
00A4848C  49 89 45 68                     mov qword ptr [r13 + 0x68], rax
00A48490  44 8A 64 24 50                  mov r12b, byte ptr [rsp + 0x50]
00A48495  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00A48499  E8 72 75 81 FF                  call 0x14025fa10
00A4849E  E8 0D 54 81 FF                  call 0x14025d8b0
00A484A3  41 8A C4                        mov al, r12b
00A484A6  48 81 C4 90 00 00 00            add rsp, 0x90
00A484AD  41 5F                           pop r15
00A484AF  41 5E                           pop r14
00A484B1  41 5D                           pop r13
00A484B3  41 5C                           pop r12
00A484B5  5F                              pop rdi
00A484B6  5E                              pop rsi
00A484B7  5B                              pop rbx
00A484B8  C3                              ret
00A484B9  CC                              int3
00A484BA  32 C0                           xor al, al
00A484BC  EB E8                           jmp 0x140a484a6
00A484BE  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00A484C6  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00A484CA  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
00A484CE  0F 57 C0                        xorps xmm0, xmm0
00A484D1  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
00A484D9  4C 8B 94 24 D8 00 00 00         mov r10, qword ptr [rsp + 0xd8]
00A484E1  49 83 3A FF                     cmp qword ptr [r10], -1
00A484E5  0F 84 4E 01 00 00               je 0x140a48639
00A484EB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00A484EF  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A484F4  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00A484FC  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A48501  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
00A48506  8B 8C 24 F0 00 00 00            mov ecx, dword ptr [rsp + 0xf0]
00A4850D  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00A48511  44 8A 8C 24 E8 00 00 00         mov r9b, byte ptr [rsp + 0xe8]
00A48519  44 8B C2                        mov r8d, edx
00A4851C  49 8B D2                        mov rdx, r10
00A4851F  49 8B CD                        mov rcx, r13
00A48522  E8 A9 25 C7 FF                  call 0x1406baad0
00A48527  84 C0                           test al, al
00A48529  0F 84 66 FF FF FF               je 0x140a48495
00A4852F  E9 66 FE FF FF                  jmp 0x140a4839a
00A48534  C6 44 24 52 01                  mov byte ptr [rsp + 0x52], 1
00A48539  48 8B F0                        mov rsi, rax
00A4853C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A48541  4D 8B 77 28                     mov r14, qword ptr [r15 + 0x28]
00A48545  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
00A4854A  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00A4854E  41 39 47 24                     cmp dword ptr [r15 + 0x24], eax
00A48552  0F 85 EA 00 00 00               jne 0x140a48642
00A48558  49 89 5F 20                     mov qword ptr [r15 + 0x20], rbx
00A4855C  E9 46 FE FF FF                  jmp 0x140a483a7
00A48561  8A 94 24 E8 00 00 00            mov dl, byte ptr [rsp + 0xe8]
00A48568  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00A4856C  E8 4F 96 7C FF                  call 0x140211bc0
00A48571  84 C0                           test al, al
00A48573  0F 84 B6 00 00 00               je 0x140a4862f
00A48579  41 B2 01                        mov r10b, 1
00A4857C  E9 99 FD FF FF                  jmp 0x140a4831a
00A48581  49 3B D9                        cmp rbx, r9
00A48584  0F 8E 06 FE FF FF               jle 0x140a48390
00A4858A  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00A4858E  E8 7D 74 81 FF                  call 0x14025fa10
00A48593  8A 94 24 E8 00 00 00            mov dl, byte ptr [rsp + 0xe8]
00A4859A  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00A4859E  E8 7D C8 7C FF                  call 0x140214e20
00A485A3  84 C0                           test al, al
00A485A5  0F 84 84 00 00 00               je 0x140a4862f
00A485AB  44 38 64 24 51                  cmp byte ptr [rsp + 0x51], r12b
00A485B0  0F 84 8E 31 0F 00               je 0x140b3b744
00A485B6  49 8B 7F 20                     mov rdi, qword ptr [r15 + 0x20]
00A485BA  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00A485BF  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00A485C6  48 8D 1C 17                     lea rbx, [rdi + rdx]
00A485CA  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00A485CF  E9 77 31 0F 00                  jmp 0x140b3b74b
00A485D4  44 38 64 24 52                  cmp byte ptr [rsp + 0x52], r12b
00A485D9  0F 84 B1 FE FF FF               je 0x140a48490
00A485DF  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
00A485E3  48 85 C9                        test rcx, rcx
00A485E6  0F 84 85 31 0F 00               je 0x140b3b771
00A485EC  B2 01                           mov dl, 1
00A485EE  E8 2D C8 7C FF                  call 0x140214e20
00A485F3  49 89 77 20                     mov qword ptr [r15 + 0x20], rsi
00A485F7  4D 89 77 28                     mov qword ptr [r15 + 0x28], r14
00A485FB  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
00A485FF  E8 0C 74 81 FF                  call 0x14025fa10
00A48604  E9 87 FE FF FF                  jmp 0x140a48490
00A48609  49 8B 7F 20                     mov rdi, qword ptr [r15 + 0x20]
00A4860D  E9 16 FD FF FF                  jmp 0x140a48328
00A48612  83 7A 04 FF                     cmp dword ptr [rdx + 4], -1
00A48616  C6 44 24 51 01                  mov byte ptr [rsp + 0x51], 1
00A4861B  0F 84 3A FC FF FF               je 0x140a4825b
00A48621  E9 30 FC FF FF                  jmp 0x140a48256
00A48626  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00A4862A  E8 E1 73 81 FF                  call 0x14025fa10
00A4862F  E8 7C 52 81 FF                  call 0x14025d8b0
00A48634  E9 81 FE FF FF                  jmp 0x140a484ba
00A48639  4D 8D 57 20                     lea r10, [r15 + 0x20]
00A4863D  E9 A9 FE FF FF                  jmp 0x140a484eb
00A48642  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
00A48646  48 85 C9                        test rcx, rcx
00A48649  0F 84 09 FF FF FF               je 0x140a48558
00A4864F  B2 01                           mov dl, 1
00A48651  E8 CA C7 7C FF                  call 0x140214e20
00A48656  49 89 5F 20                     mov qword ptr [r15 + 0x20], rbx
00A4865A  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
00A4865E  E8 AD 73 81 FF                  call 0x14025fa10
00A48663  E9 3F FD FF FF                  jmp 0x140a483a7
00A48668  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
00A4866C  48 85 C9                        test rcx, rcx
00A4866F  0F 84 EA FD FF FF               je 0x140a4845f
00A48675  B2 01                           mov dl, 1
00A48677  E8 A4 C7 7C FF                  call 0x140214e20
00A4867C  49 89 5F 28                     mov qword ptr [r15 + 0x28], rbx
00A48680  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
00A48684  E8 87 73 81 FF                  call 0x14025fa10
00A48689  E9 D5 FD FF FF                  jmp 0x140a48463
00A4868E  B0 01                           mov al, 1
00A48690  E9 11 FE FF FF                  jmp 0x140a484a6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlCopyWrite(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_m76;
    unsigned __int8 v_stack_m77;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p51;
    unsigned __int8 v_stack_p52;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_pD8;
    unsigned int v_stack_pE0;
    unsigned __int8 v_stack_pE8;

    *(unsigned __int8 *)(v_rsp + 32) = (unsigned __int8)(a4);
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    v_r12 = 0;
    *(unsigned __int8 *)(v_rsp - 120) = 1;
    v_stack_m76 = 0;
    if ((*(unsigned int *)(a2)) == -1) goto loc_00A48612;
loc_00A48256:
    v_stack_m77 = 0;
loc_00A4825B:
    result = IoGetTopLevelIrp(a1, a2, a3, a4);
    if (result != 0) goto loc_00A484BA;
    v_stack_m50 = *(unsigned __int64 *)(a1 + 24);
    a4 = 0;
    result = CcCanIWrite(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)((unsigned __int8)(a4)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A484BA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (16)) != 0) goto loc_00A484BA;
    result = CcCopyWriteWontFlush(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A484BA;
    *(unsigned int *)(a7) = 0;
    *(unsigned __int64 *)(a7 + 8) = (unsigned int)(a3);
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00A4868E;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    a2 = (a2) | (-1);
    if (v_stack_m77 != 0) goto loc_00A482FF;
    a1 = ((unsigned int)(a3)) + (*(unsigned __int64 *)(a2));
    if (a1 <= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40))) goto loc_00A48561;
loc_00A482FF:
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8), v_stack_p20, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A4862F;
loc_00A4831A:
    if (v_stack_m77 != 0) goto loc_00A48609;
loc_00A48328:
    v_rbx = ((unsigned int)(a3)) + (*(unsigned __int64 *)(a2));
    v_stack_m68 = v_rbx;
    v_stack_m70 = *(unsigned __int64 *)(a2);
    if ((*(unsigned __int64 *)(a1 + 48)) == 0) goto loc_00A48626;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 5)) == 0) goto loc_00A48626;
    if ((*(unsigned __int64 *)(a2)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) + 8192)) goto loc_00A48626;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8)) - (*(unsigned __int64 *)(a2));
    if (a1 < ((unsigned int)(v_stack_p18))) goto loc_00A48626;
    if (v_rbx > (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 24))) goto loc_00A48626;
    if (0 != 0) goto loc_00A48581;
loc_00A48390:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 5))) == 2) goto loc_00A484BE;
loc_00A4839A:
    if (v_rbx > (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32))) goto loc_00A48534;
loc_00A483A7:
    result = IoSetTopLevelIrp(4, (unsigned int)(v_stack_p18), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 5), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40));
    if ((*(unsigned __int64 *)(a2)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40))) goto loc_00A483EF;
loc_00A483B8:
    if (v_stack_m78 == 0) goto loc_00A4840E;
    v_stack_mA8 = a6;
    result = CcCopyWrite(a1, v_stack_m70, (unsigned int)(v_stack_p18), v_stack_p20);
    v_stack_m78 = (unsigned __int8)(result);
    goto loc_00A4840E;
loc_00A483EF:
    result = CcZeroData(a1, *(unsigned __int64 *)(a1 + 24) + 40, v_stack_m70, v_stack_p20);
    v_stack_m78 = (unsigned __int8)(result);
    goto loc_00A483B8;
loc_00A4840E:
    goto loc_00A48439;
loc_00A48439:
    a1 = 0;
    result = IoSetTopLevelIrp(a1, *(unsigned __int64 *)(a1 + 24) + 40, v_stack_m70, v_stack_p20);
    if (v_stack_m78 == 0) goto loc_00A485D4;
    if (v_rbx <= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40))) goto loc_00A48463;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 44)) != ((unsigned int)((unsigned int)(v_stack_m64)))) goto loc_00A48668;
loc_00A4845F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) = v_rbx;
loc_00A48463:
    result = (unsigned int)(v_stack_m64);
    if (v_stack_m76 != 0) {
        result = *(unsigned __int64 *)(a1 + 40);
        a1 = *(unsigned __int64 *)(result + 8);
        *(unsigned __int64 *)(a1 + 8) = v_rbx;
    }
    result = ((unsigned int)(v_stack_p18)) + (*(unsigned __int64 *)(a2));
    *(unsigned __int64 *)(a1 + 104) = result;
loc_00A48490:
loc_00A48495:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8), *(unsigned __int64 *)(a1 + 24) + 40, v_stack_m70, v_stack_p20);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8), *(unsigned __int64 *)(a1 + 24) + 40, v_stack_m70, v_stack_p20);
loc_00A484A6:
    v_rsp = (v_rsp) + (144);
    return (unsigned __int8)(v_stack_m78);
loc_00A484BA:
    result = 0;
    goto loc_00A484A6;
loc_00A484BE:
    v_stack_p80 = v_xmm0;
    if ((*(unsigned __int64 *)(v_stack_pD8)) == -1) goto loc_00A48639;
loc_00A484EB:
    v_stack_p38 = a8;
    v_stack_p30 = v_stack_p80;
    v_stack_p28 = (unsigned __int8)(v_stack_m78);
    v_stack_p20 = (unsigned int)((unsigned int)(a5));
    result = guard_dispatch_icall(a1, v_stack_pD8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    if ((unsigned __int8)(result) == 0) goto loc_00A48495;
    goto loc_00A4839A;
loc_00A48534:
    v_stack_p52 = 1;
    v_stack_p68 = result;
    v_stack_p70 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 36)) != ((unsigned int)((unsigned int)(v_stack_p64)))) goto loc_00A48642;
loc_00A48558:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) = v_rbx;
    goto loc_00A483A7;
loc_00A48561:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8), v_stack_pE8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    if ((unsigned __int8)(result) == 0) goto loc_00A4862F;
    goto loc_00A4831A;
loc_00A48581:
    if (v_rbx <= v_stack_pE8) goto loc_00A48390;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8), v_stack_pE8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8), v_stack_pE8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    if ((unsigned __int8)(result) == 0) goto loc_00A4862F;
    v_stack_p58 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32);
    v_stack_p60 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + (unsigned int)(v_stack_pE0) * 1;
loc_00A485D4:
    if (v_stack_p52 == ((unsigned __int8)(v_stack_m78))) goto loc_00A48490;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16), 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16), 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    goto loc_00A48490;
loc_00A48609:
    goto loc_00A48328;
loc_00A48612:
    v_stack_p51 = 1;
    if ((*(unsigned int *)(1 + 4)) == -1) goto loc_00A4825B;
    goto loc_00A48256;
loc_00A48626:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8), 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
loc_00A4862F:
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8), 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    goto loc_00A484BA;
loc_00A48639:
    goto loc_00A484EB;
loc_00A48642:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16) == 0) goto loc_00A48558;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16), 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + (unsigned int)(v_stack_pE0) * 1;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16), 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    goto loc_00A483A7;
loc_00A48668:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16) == 0) goto loc_00A4845F;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16), 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + (unsigned int)(v_stack_pE0) * 1;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16), 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 40)), v_stack_pE8);
    goto loc_00A48463;
loc_00A4868E:
    goto loc_00A484A6;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlCopyWrite(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, void *Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint8_t v_stack_m76;
    uint8_t v_stack_m77;
    uint8_t v_stack_m78;
    uint64_t v_stack_mA8;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p51;
    uint8_t v_stack_p52;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_pD8;
    uint32_t v_stack_pE0;
    uint8_t v_stack_pE8;

    *(uint8_t *)(local_rsp + 0x20) = (uint8_t)(Arg4);
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    local_r12 = 0;
    *(uint8_t *)(local_rsp - 0x78) = 1;
    v_stack_m76 = 0;
    if ((*(uint32_t *)(arg2)) == -1) goto loc_00A48612;
loc_00A48256:
    v_stack_m77 = 0;
loc_00A4825B:
    result = IoGetTopLevelIrp(Arg1, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00A484BA;
    v_stack_m50 = *(uint64_t *)(arg1 + 0x18);
    Arg4 = 0;
    result = CcCanIWrite(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)((uint8_t)(Arg4)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A484BA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (16)) != 0) goto loc_00A484BA;
    result = CcCopyWriteWontFlush(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A484BA;
    *(uint32_t *)(arg7) = 0;
    *(uint64_t *)(arg7 + 0x8) = (uint32_t)(Arg3);
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00A4868E;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    Arg2 = (Arg2) | (-1);
    if (v_stack_m77 != 0) goto loc_00A482FF;
    Arg1 = ((uint32_t)(Arg3)) + (*(uint64_t *)(arg2));
    if (Arg1 <= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28))) goto loc_00A48561;
loc_00A482FF:
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8), v_stack_p20, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A4862F;
loc_00A4831A:
    if (v_stack_m77 != 0) goto loc_00A48609;
loc_00A48328:
    local_rbx = ((uint32_t)(Arg3)) + (*(uint64_t *)(arg2));
    v_stack_m68 = local_rbx;
    v_stack_m70 = *(uint64_t *)(arg2);
    if ((*(uint64_t *)(arg1 + 0x30)) == 0) goto loc_00A48626;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x5)) == 0) goto loc_00A48626;
    if ((*(uint64_t *)(arg2)) >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) + 8192)) goto loc_00A48626;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8)) - (*(uint64_t *)(arg2));
    if (Arg1 < ((uint32_t)(v_stack_p18))) goto loc_00A48626;
    if (local_rbx > (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x18))) goto loc_00A48626;
    if (0 != 0) goto loc_00A48581;
loc_00A48390:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x5))) == 2) goto loc_00A484BE;
loc_00A4839A:
    if (local_rbx > (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20))) goto loc_00A48534;
loc_00A483A7:
    result = IoSetTopLevelIrp(4, (uint32_t)(v_stack_p18), *(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x5), *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28));
    if ((*(uint64_t *)(arg2)) > (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28))) goto loc_00A483EF;
loc_00A483B8:
    if (v_stack_m78 == 0) goto loc_00A4840E;
    v_stack_mA8 = Arg6;
    result = CcCopyWrite(Arg1, v_stack_m70, (uint32_t)(v_stack_p18), v_stack_p20);
    v_stack_m78 = (uint8_t)(result);
    goto loc_00A4840E;
loc_00A483EF:
    result = CcZeroData(Arg1, *(uint64_t *)(arg1 + 0x18) + 40, v_stack_m70, v_stack_p20);
    v_stack_m78 = (uint8_t)(result);
    goto loc_00A483B8;
loc_00A4840E:
    goto loc_00A48439;
loc_00A48439:
    Arg1 = 0;
    result = IoSetTopLevelIrp(Arg1, *(uint64_t *)(arg1 + 0x18) + 40, v_stack_m70, v_stack_p20);
    if (v_stack_m78 == 0) goto loc_00A485D4;
    if (local_rbx <= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28))) goto loc_00A48463;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x2C)) != ((uint32_t)((uint32_t)(v_stack_m64)))) goto loc_00A48668;
loc_00A4845F:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) = local_rbx;
loc_00A48463:
    result = (uint32_t)(v_stack_m64);
    if (v_stack_m76 != 0) {
        result = *(uint64_t *)(arg1 + 0x28);
        Arg1 = *(uint64_t *)(result + 0x8);
        *(uint64_t *)(arg1 + 0x8) = local_rbx;
    }
    result = ((uint32_t)(v_stack_p18)) + (*(uint64_t *)(arg2));
    *(uint64_t *)(arg1 + 0x68) = result;
loc_00A48490:
loc_00A48495:
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8), *(uint64_t *)(arg1 + 0x18) + 40, v_stack_m70, v_stack_p20);
    result = KeLeaveCriticalRegion(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8), *(uint64_t *)(arg1 + 0x18) + 40, v_stack_m70, v_stack_p20);
loc_00A484A6:
    local_rsp = (local_rsp) + (144);
    return (uint8_t)(v_stack_m78);
loc_00A484BA:
    result = 0;
    goto loc_00A484A6;
loc_00A484BE:
    v_stack_p80 = v_xmm0;
    if ((*(uint64_t *)(v_stack_pD8)) == -1) goto loc_00A48639;
loc_00A484EB:
    v_stack_p38 = Arg8;
    v_stack_p30 = v_stack_p80;
    v_stack_p28 = (uint8_t)(v_stack_m78);
    v_stack_p20 = (uint32_t)((uint32_t)(Arg5));
    result = guard_dispatch_icall(Arg1, v_stack_pD8, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    if ((uint8_t)(result) == 0) goto loc_00A48495;
    goto loc_00A4839A;
loc_00A48534:
    v_stack_p52 = 1;
    v_stack_p68 = result;
    v_stack_p70 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x24)) != ((uint32_t)((uint32_t)(v_stack_p64)))) goto loc_00A48642;
loc_00A48558:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) = local_rbx;
    goto loc_00A483A7;
loc_00A48561:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8), v_stack_pE8, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    if ((uint8_t)(result) == 0) goto loc_00A4862F;
    goto loc_00A4831A;
loc_00A48581:
    if (local_rbx <= v_stack_pE8) goto loc_00A48390;
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8), v_stack_pE8, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8), v_stack_pE8, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    if ((uint8_t)(result) == 0) goto loc_00A4862F;
    v_stack_p58 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20);
    v_stack_p60 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + (uint32_t)(v_stack_pE0) * 1;
loc_00A485D4:
    if (v_stack_p52 == ((uint8_t)(v_stack_m78))) goto loc_00A48490;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10), 1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) = result;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28);
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10), 1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    goto loc_00A48490;
loc_00A48609:
    goto loc_00A48328;
loc_00A48612:
    v_stack_p51 = 1;
    if ((*(uint32_t *)(1 + 0x4)) == -1) goto loc_00A4825B;
    goto loc_00A48256;
loc_00A48626:
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8), 1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
loc_00A4862F:
    result = KeLeaveCriticalRegion(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8), 1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    goto loc_00A484BA;
loc_00A48639:
    goto loc_00A484EB;
loc_00A48642:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10) == 0) goto loc_00A48558;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10), 1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + (uint32_t)(v_stack_pE0) * 1;
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10), 1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    goto loc_00A483A7;
loc_00A48668:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10) == 0) goto loc_00A4845F;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10), 1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + (uint32_t)(v_stack_pE0) * 1;
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10), 1, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 40)), v_stack_pE8);
    goto loc_00A48463;
loc_00A4868E:
    goto loc_00A484A6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R/W` |
| `Arg1` | `+ 0x68` | `64` | `W` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg7` | `+ 0x0` | `32` | `W` |
| `Arg7` | `+ 0x8` | `64` | `W` |
| `Arg8` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A48210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
