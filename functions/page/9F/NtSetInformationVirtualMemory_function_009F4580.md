# NtSetInformationVirtualMemory

- RVA: `0x009F4580`–`0x009F4E4A` (길이 `2,250` bytes)
- VA: `0x00000001409F4580`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A65AC`
- 디코드: `474`개 명령, `2,250/2,250` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009F473C` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009F47BE` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x009F480A` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009F4817` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009F4824` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009F48C5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009F48E4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009F49D0` → [MiGetEffectivePagePriorityThread](../../text/36/MiGetEffectivePagePriorityThread_function_003626E0.md) (function, `0x003626E0`)
- `0x009F4A21` → [PsGetIoPriorityThread](../../text/34/PsGetIoPriorityThread_function_00343930.md) (function, `0x00343930`)
- `0x009F4A44` → [MiPrefetchVirtualMemory](../../text/36/MiPrefetchVirtualMemory_function_0036C560.md) (function, `0x0036C560`)
- `0x009F4AA8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009F4B22` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009F4B77` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009F4BAA` → [MiProcessVaRangesInfoClass](MiProcessVaRangesInfoClass_function_009F4E50.md) (function, `0x009F4E50`)
- `0x009F4BFF` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009F4C9B` → [MiCfgMarkValidEntries](MiCfgMarkValidEntries_function_009F4FE8.md) (function, `0x009F4FE8`)
- `0x009F4D00` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F4D89` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x009F4DC1` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x009F4DE3` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009F4DFE` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009F4E18` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009F4E27` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009F4E36` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009F4595` → RVA `0x00E0A740` (`.data`; read)
- `0x009F4AF2` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x009F4BCF` → RVA `0x00FC6BD8` (`ALMOSTRO`; read)
- `0x009F4D14` → RVA `0x00E375AC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x009F48C5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009F48E4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009F49D0` → [MiGetEffectivePagePriorityThread](../../text/36/MiGetEffectivePagePriorityThread_function_003626E0.md) (`PAGE` → `.text`)
  - `0x009F4A21` → [PsGetIoPriorityThread](../../text/34/PsGetIoPriorityThread_function_00343930.md) (`PAGE` → `.text`)
  - `0x009F4A44` → [MiPrefetchVirtualMemory](../../text/36/MiPrefetchVirtualMemory_function_0036C560.md) (`PAGE` → `.text`)
  - `0x009F4AA8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009F4B77` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009F4D00` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F4D89` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x009F4DC1` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x009F4DE3` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009F4DFE` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009F4E18` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009F4E27` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009F4E36` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x009F4C41` → [sub_00B31388 + 0x26](../B3/Unknown_function_00B31388.md) (`tail-transfer`)
  - `0x009F4D1A` → [sub_00B31388](../B3/Unknown_function_00B31388.md) (`tail-transfer`)
  - `0x009F4DAA` → [sub_00B31388 + 0x14](../B3/Unknown_function_00B31388.md) (`tail-transfer`)
  - `0x009F4DCE` → [sub_00B31388 + 0x14](../B3/Unknown_function_00B31388.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009F4580  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
009F4585  57                              push rdi
009F4586  41 54                           push r12
009F4588  41 55                           push r13
009F458A  41 56                           push r14
009F458C  41 57                           push r15
009F458E  48 81 EC 40 03 00 00            sub rsp, 0x340
009F4595  48 8B 05 A4 61 41 00            mov rax, qword ptr [rip + 0x4161a4]
009F459C  48 33 C4                        xor rax, rsp
009F459F  48 89 84 24 30 03 00 00         mov qword ptr [rsp + 0x330], rax
009F45A7  4D 8B D9                        mov r11, r9
009F45AA  4C 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r9
009F45B2  4C 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], r8
009F45BA  44 8B F2                        mov r14d, edx
009F45BD  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
009F45C2  48 8B 94 24 90 03 00 00         mov rdx, qword ptr [rsp + 0x390]
009F45CA  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
009F45D2  48 83 A4 24 80 00 00 00 00      and qword ptr [rsp + 0x80], 0
009F45DB  0F 57 C0                        xorps xmm0, xmm0
009F45DE  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
009F45E6  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
009F45EE  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
009F45F6  83 A4 24 90 00 00 00 00         and dword ptr [rsp + 0x90], 0
009F45FE  48 83 A4 24 C8 00 00 00 00      and qword ptr [rsp + 0xc8], 0
009F4607  45 33 FF                        xor r15d, r15d
009F460A  44 89 7C 24 78                  mov dword ptr [rsp + 0x78], r15d
009F460F  33 DB                           xor ebx, ebx
009F4611  89 5C 24 74                     mov dword ptr [rsp + 0x74], ebx
009F4615  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
009F461D  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
009F4622  33 FF                           xor edi, edi
009F4624  21 5C 24 60                     and dword ptr [rsp + 0x60], ebx
009F4628  41 8B CE                        mov ecx, r14d
009F462B  45 85 F6                        test r14d, r14d
009F462E  74 2B                           je 0x1409f465b
009F4630  83 E9 01                        sub ecx, 1
009F4633  74 26                           je 0x1409f465b
009F4635  83 E9 01                        sub ecx, 1
009F4638  0F 84 9D 04 00 00               je 0x1409f4adb
009F463E  83 E9 01                        sub ecx, 1
009F4641  74 18                           je 0x1409f465b
009F4643  83 E9 01                        sub ecx, 1
009F4646  74 13                           je 0x1409f465b
009F4648  83 E9 01                        sub ecx, 1
009F464B  74 0E                           je 0x1409f465b
009F464D  83 E9 01                        sub ecx, 1
009F4650  74 09                           je 0x1409f465b
009F4652  83 F9 01                        cmp ecx, 1
009F4655  0F 85 AF 06 00 00               jne 0x1409f4d0a
009F465B  48 85 D2                        test rdx, rdx
009F465E  0F 84 09 07 00 00               je 0x1409f4d6d
009F4664  8B 8C 24 98 03 00 00            mov ecx, dword ptr [rsp + 0x398]
009F466B  83 F9 04                        cmp ecx, 4
009F466E  0F 85 77 04 00 00               jne 0x1409f4aeb
009F4674  44 3B F1                        cmp r14d, ecx
009F4677  0F 84 97 06 00 00               je 0x1409f4d14
009F467D  41 BC 01 00 00 00               mov r12d, 1
009F4683  49 8D 40 FF                     lea rax, [r8 - 1]
009F4687  49 B9 FE FF FF FF FF FF FF 0F   movabs r9, 0xffffffffffffffe
009F4691  49 3B C1                        cmp rax, r9
009F4694  0F 87 A6 07 00 00               ja 0x1409f4e40
009F469A  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
009F46A3  4C 89 94 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r10
009F46AB  4D 8B 8A B8 00 00 00            mov r9, qword ptr [r10 + 0xb8]
009F46B2  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
009F46BA  41 83 FE 02                     cmp r14d, 2
009F46BE  0F 84 4F 05 00 00               je 0x1409f4c13
009F46C4  33 C0                           xor eax, eax
009F46C6  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
009F46CE  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
009F46D6  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
009F46DE  45 8A 92 32 02 00 00            mov r10b, byte ptr [r10 + 0x232]
009F46E5  44 88 54 24 50                  mov byte ptr [rsp + 0x50], r10b
009F46EA  45 84 D2                        test r10b, r10b
009F46ED  0F 84 43 04 00 00               je 0x1409f4b36
009F46F3  49 8B C0                        mov rax, r8
009F46F6  48 C1 E0 04                     shl rax, 4
009F46FA  48 85 C0                        test rax, rax
009F46FD  0F 84 F8 00 00 00               je 0x1409f47fb
009F4703  41 F6 C3 03                     test r11b, 3
009F4707  0F 85 FD 00 00 00               jne 0x1409f480a
009F470D  4E 8D 04 18                     lea r8, [rax + r11]
009F4711  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
009F471B  4D 3B C7                        cmp r8, r15
009F471E  0F 87 EB 00 00 00               ja 0x1409f480f
009F4724  4D 3B C3                        cmp r8, r11
009F4727  0F 82 E2 00 00 00               jb 0x1409f480f
009F472D  41 83 FE 02                     cmp r14d, 2
009F4731  74 0F                           je 0x1409f4742
009F4733  F6 C2 03                        test dl, 3
009F4736  0F 84 07 01 00 00               je 0x1409f4843
009F473C  E8 8F 58 EA FF                  call 0x140899fd0
009F4741  CC                              int3
009F4742  85 C9                           test ecx, ecx
009F4744  74 1E                           je 0x1409f4764
009F4746  F6 C2 03                        test dl, 3
009F4749  0F 85 C8 00 00 00               jne 0x1409f4817
009F474F  48 03 CA                        add rcx, rdx
009F4752  49 3B CF                        cmp rcx, r15
009F4755  0F 87 C1 00 00 00               ja 0x1409f481c
009F475B  48 3B CA                        cmp rcx, rdx
009F475E  0F 82 B8 00 00 00               jb 0x1409f481c
009F4764  0F 10 12                        movups xmm2, xmmword ptr [rdx]
009F4767  0F 11 94 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm2
009F476F  0F 10 42 10                     movups xmm0, xmmword ptr [rdx + 0x10]
009F4773  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
009F477B  F2 0F 10 4A 20                  movsd xmm1, qword ptr [rdx + 0x20]
009F4780  F2 0F 11 8C 24 C0 00 00 00      movsd qword ptr [rsp + 0xc0], xmm1
009F4789  66 0F 7E D0                     movd eax, xmm2
009F478D  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
009F4791  85 C0                           test eax, eax
009F4793  0F 84 A0 00 00 00               je 0x1409f4839
009F4799  44 8B E8                        mov r13d, eax
009F479C  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
009F47A4  48 C1 E8 20                     shr rax, 0x20
009F47A8  85 C0                           test eax, eax
009F47AA  0F 85 89 00 00 00               jne 0x1409f4839
009F47B0  8D 50 04                        lea edx, [rax + 4]
009F47B3  44 8B C2                        mov r8d, edx
009F47B6  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
009F47BE  E8 FD 49 EF FF                  call 0x1408e91c0
009F47C3  49 C1 E5 04                     shl r13, 4
009F47C7  4D 85 ED                        test r13, r13
009F47CA  74 20                           je 0x1409f47ec
009F47CC  F6 84 24 B0 00 00 00 03         test byte ptr [rsp + 0xb0], 3
009F47D4  75 4E                           jne 0x1409f4824
009F47D6  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
009F47DE  4A 8D 0C 28                     lea rcx, [rax + r13]
009F47E2  49 3B CF                        cmp rcx, r15
009F47E5  77 42                           ja 0x1409f4829
009F47E7  48 3B C8                        cmp rcx, rax
009F47EA  72 3D                           jb 0x1409f4829
009F47EC  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
009F47F4  44 8A 54 24 50                  mov r10b, byte ptr [rsp + 0x50]
009F47F9  EB 64                           jmp 0x1409f485f
009F47FB  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
009F4805  E9 23 FF FF FF                  jmp 0x1409f472d
009F480A  E8 C1 57 EA FF                  call 0x140899fd0
009F480F  41 8A 07                        mov al, byte ptr [r15]
009F4812  E9 16 FF FF FF                  jmp 0x1409f472d
009F4817  E8 B4 57 EA FF                  call 0x140899fd0
009F481C  41 8A 07                        mov al, byte ptr [r15]
009F481F  E9 40 FF FF FF                  jmp 0x1409f4764
009F4824  E8 A7 57 EA FF                  call 0x140899fd0
009F4829  41 8A 07                        mov al, byte ptr [r15]
009F482C  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
009F4833  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
009F4837  EB B3                           jmp 0x1409f47ec
009F4839  B8 F3 00 00 C0                  mov eax, 0xc00000f3
009F483E  E9 5A 02 00 00                  jmp 0x1409f4a9d
009F4843  49 3B D7                        cmp rdx, r15
009F4846  4C 0F 42 FA                     cmovb r15, rdx
009F484A  90                              nop
009F484B  41 8A 07                        mov al, byte ptr [r15]
009F484E  8B 02                           mov eax, dword ptr [rdx]
009F4850  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009F4854  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
009F485B  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
009F485F  44 8B 6C 24 7C                  mov r13d, dword ptr [rsp + 0x7c]
009F4864  EB 05                           jmp 0x1409f486b
009F4866  E9 32 02 00 00                  jmp 0x1409f4a9d
009F486B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009F4870  48 83 F9 FF                     cmp rcx, -1
009F4874  0F 85 78 02 00 00               jne 0x1409f4af2
009F487A  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
009F4882  4C 8D BC 24 30 02 00 00         lea r15, [rsp + 0x230]
009F488A  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
009F4892  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
009F489A  48 83 F8 10                     cmp rax, 0x10
009F489E  0F 87 D3 04 00 00               ja 0x1409f4d77
009F48A4  41 83 FE 02                     cmp r14d, 2
009F48A8  0F 84 06 03 00 00               je 0x1409f4bb4
009F48AE  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
009F48B6  49 C1 E0 04                     shl r8, 4
009F48BA  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
009F48C2  49 8B CF                        mov rcx, r15
009F48C5  E8 76 1F CD FF                  call 0x1406c6840
009F48CA  41 83 FE 02                     cmp r14d, 2
009F48CE  75 19                           jne 0x1409f48e9
009F48D0  45 8B C5                        mov r8d, r13d
009F48D3  49 C1 E0 04                     shl r8, 4
009F48D7  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
009F48DF  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009F48E4  E8 57 1F CD FF                  call 0x1406c6840
009F48E9  EB 26                           jmp 0x1409f4911
009F48EB  8B F8                           mov edi, eax
009F48ED  41 BC 01 00 00 00               mov r12d, 1
009F48F3  4C 8B BC 24 88 00 00 00         mov r15, qword ptr [rsp + 0x88]
009F48FB  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
009F4900  8B 5C 24 74                     mov ebx, dword ptr [rsp + 0x74]
009F4904  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
009F490C  E9 44 01 00 00                  jmp 0x1409f4a55
009F4911  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009F4919  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
009F4921  48 39 88 B8 00 00 00            cmp qword ptr [rax + 0xb8], rcx
009F4928  0F 85 25 02 00 00               jne 0x1409f4b53
009F492E  45 33 D2                        xor r10d, r10d
009F4931  49 8B D7                        mov rdx, r15
009F4934  4C 8B 9C 24 98 00 00 00         mov r11, qword ptr [rsp + 0x98]
009F493C  4D 8B C3                        mov r8, r11
009F493F  49 C1 E0 04                     shl r8, 4
009F4943  4D 03 C7                        add r8, r15
009F4946  49 3B D0                        cmp rdx, r8
009F4949  73 63                           jae 0x1409f49ae
009F494B  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
009F494F  48 85 C9                        test rcx, rcx
009F4952  0F 84 6F 01 00 00               je 0x1409f4ac7
009F4958  4C 8B 0A                        mov r9, qword ptr [rdx]
009F495B  49 8D 41 FF                     lea rax, [r9 - 1]
009F495F  48 03 C1                        add rax, rcx
009F4962  49 3B C1                        cmp rax, r9
009F4965  0F 82 5C 01 00 00               jb 0x1409f4ac7
009F496B  49 8D 41 FF                     lea rax, [r9 - 1]
009F496F  48 03 C1                        add rax, rcx
009F4972  49 B9 FF FF FE FF FF 7F 00 00   movabs r9, 0x7ffffffeffff
009F497C  49 3B C1                        cmp rax, r9
009F497F  0F 87 42 01 00 00               ja 0x1409f4ac7
009F4985  8B 02                           mov eax, dword ptr [rdx]
009F4987  25 FF 0F 00 00                  and eax, 0xfff
009F498C  48 05 FF 0F 00 00               add rax, 0xfff
009F4992  48 03 C1                        add rax, rcx
009F4995  48 C1 E8 0C                     shr rax, 0xc
009F4999  49 03 C2                        add rax, r10
009F499C  49 3B C2                        cmp rax, r10
009F499F  0F 82 22 01 00 00               jb 0x1409f4ac7
009F49A5  4C 8B D0                        mov r10, rax
009F49A8  48 83 C2 10                     add rdx, 0x10
009F49AC  EB 98                           jmp 0x1409f4946
009F49AE  45 85 F6                        test r14d, r14d
009F49B1  0F 85 CA 01 00 00               jne 0x1409f4b81
009F49B7  F7 44 24 60 FE FF FF FF         test dword ptr [rsp + 0x60], 0xfffffffe
009F49BF  0F 85 CD 01 00 00               jne 0x1409f4b92
009F49C5  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
009F49CD  49 8B C8                        mov rcx, r8
009F49D0  E8 0B DD 96 FF                  call 0x1403626e0
009F49D5  83 E0 07                        and eax, 7
009F49D8  83 F8 05                        cmp eax, 5
009F49DB  1B D2                           sbb edx, edx
009F49DD  83 E2 40                        and edx, 0x40
009F49E0  81 C2 00 00 02 00               add edx, 0x20000
009F49E6  0B D0                           or edx, eax
009F49E8  8B CA                           mov ecx, edx
009F49EA  83 E1 07                        and ecx, 7
009F49ED  8D 04 CD 00 00 00 00            lea eax, [rcx*8]
009F49F4  0B C2                           or eax, edx
009F49F6  83 F9 05                        cmp ecx, 5
009F49F9  73 06                           jae 0x1409f4a01
009F49FB  83 E0 EF                        and eax, 0xffffffef
009F49FE  83 C8 28                        or eax, 0x28
009F4A01  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
009F4A05  41 22 D4                        and dl, r12b
009F4A08  F6 DA                           neg dl
009F4A0A  45 1B C9                        sbb r9d, r9d
009F4A0D  41 81 E1 00 C0 03 00            and r9d, 0x3c000
009F4A14  41 81 C1 00 40 00 00            add r9d, 0x4000
009F4A1B  44 0B C8                        or r9d, eax
009F4A1E  49 8B C8                        mov rcx, r8
009F4A21  E8 0A EF 94 FF                  call 0x140343930
009F4A26  41 3B C4                        cmp eax, r12d
009F4A29  0F 8E A2 00 00 00               jle 0x1409f4ad1
009F4A2F  4C 8B 84 24 80 00 00 00         mov r8, qword ptr [rsp + 0x80]
009F4A37  49 81 C0 00 04 00 00            add r8, 0x400
009F4A3E  49 8B D7                        mov rdx, r15
009F4A41  49 8B CB                        mov rcx, r11
009F4A44  E8 17 7B 97 FF                  call 0x14036c560
009F4A49  8B F8                           mov edi, eax
009F4A4B  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
009F4A50  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
009F4A55  41 84 DC                        test r12b, bl
009F4A58  0F 85 B0 03 00 00               jne 0x1409f4e0e
009F4A5E  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
009F4A66  48 85 C9                        test rcx, rcx
009F4A69  0F 85 B3 03 00 00               jne 0x1409f4e22
009F4A6F  49 83 FD FF                     cmp r13, -1
009F4A73  0F 85 F1 00 00 00               jne 0x1409f4b6a
009F4A79  48 8D 84 24 30 02 00 00         lea rax, [rsp + 0x230]
009F4A81  4C 3B F8                        cmp r15, rax
009F4A84  0F 85 A7 03 00 00               jne 0x1409f4e31
009F4A8A  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
009F4A92  4C 3B F0                        cmp r14, rax
009F4A95  0F 85 60 02 00 00               jne 0x1409f4cfb
009F4A9B  8B C7                           mov eax, edi
009F4A9D  48 8B 8C 24 30 03 00 00         mov rcx, qword ptr [rsp + 0x330]
009F4AA5  48 33 CC                        xor rcx, rsp
009F4AA8  E8 93 7B CB FF                  call 0x1406ac640
009F4AAD  48 8B 9C 24 78 03 00 00         mov rbx, qword ptr [rsp + 0x378]
009F4AB5  48 81 C4 40 03 00 00            add rsp, 0x340
009F4ABC  41 5F                           pop r15
009F4ABE  41 5E                           pop r14
009F4AC0  41 5D                           pop r13
009F4AC2  41 5C                           pop r12
009F4AC4  5F                              pop rdi
009F4AC5  C3                              ret
009F4AC6  CC                              int3
009F4AC7  BF F2 00 00 C0                  mov edi, 0xc00000f2
009F4ACC  E9 7A FF FF FF                  jmp 0x1409f4a4b
009F4AD1  41 0F BA E9 0A                  bts r9d, 0xa
009F4AD6  E9 54 FF FF FF                  jmp 0x1409f4a2f
009F4ADB  8B 8C 24 98 03 00 00            mov ecx, dword ptr [rsp + 0x398]
009F4AE2  83 F9 28                        cmp ecx, 0x28
009F4AE5  0F 84 92 FB FF FF               je 0x1409f467d
009F4AEB  B8 F4 00 00 C0                  mov eax, 0xc00000f4
009F4AF0  EB AB                           jmp 0x1409f4a9d
009F4AF2  4C 8B 05 9F 1F 5D 00            mov r8, qword ptr [rip + 0x5d1f9f]
009F4AF9  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
009F4AFF  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
009F4B05  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
009F4B0D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009F4B12  C7 44 24 20 4D 6D 50 66         mov dword ptr [rsp + 0x20], 0x66506d4d
009F4B1A  45 8A CA                        mov r9b, r10b
009F4B1D  BA 08 00 00 00                  mov edx, 8
009F4B22  E8 29 4B E7 FF                  call 0x140869650
009F4B27  8B F8                           mov edi, eax
009F4B29  85 C0                           test eax, eax
009F4B2B  0F 89 51 FD FF FF               jns 0x1409f4882
009F4B31  E9 67 FF FF FF                  jmp 0x1409f4a9d
009F4B36  41 83 FE 02                     cmp r14d, 2
009F4B3A  0F 84 EA 01 00 00               je 0x1409f4d2a
009F4B40  8B 02                           mov eax, dword ptr [rdx]
009F4B42  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009F4B46  44 8B AC 24 A0 00 00 00         mov r13d, dword ptr [rsp + 0xa0]
009F4B4E  E9 18 FD FF FF                  jmp 0x1409f486b
009F4B53  41 8D 46 FD                     lea eax, [r14 - 3]
009F4B57  41 3B C4                        cmp eax, r12d
009F4B5A  0F 87 79 02 00 00               ja 0x1409f4dd9
009F4B60  BF EF 00 00 C0                  mov edi, 0xc00000ef
009F4B65  E9 E1 FE FF FF                  jmp 0x1409f4a4b
009F4B6A  BA 4D 6D 50 66                  mov edx, 0x66506d4d
009F4B6F  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009F4B77  E8 64 2D 90 FF                  call 0x1402f78e0
009F4B7C  E9 F8 FE FF FF                  jmp 0x1409f4a79
009F4B81  41 83 EE 01                     sub r14d, 1
009F4B85  0F 85 B2 00 00 00               jne 0x1409f4c3d
009F4B8B  83 7C 24 60 05                  cmp dword ptr [rsp + 0x60], 5
009F4B90  76 0A                           jbe 0x1409f4b9c
009F4B92  BF F3 00 00 C0                  mov edi, 0xc00000f3
009F4B97  E9 AF FE FF FF                  jmp 0x1409f4a4b
009F4B9C  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
009F4BA1  45 8B C4                        mov r8d, r12d
009F4BA4  49 8B D7                        mov rdx, r15
009F4BA7  49 8B CB                        mov rcx, r11
009F4BAA  E8 A1 02 00 00                  call 0x1409f4e50
009F4BAF  E9 95 FE FF FF                  jmp 0x1409f4a49
009F4BB4  41 83 FD 10                     cmp r13d, 0x10
009F4BB8  0F 87 F1 01 00 00               ja 0x1409f4daf
009F4BBE  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
009F4BC6  48 85 C9                        test rcx, rcx
009F4BC9  0F 84 DF FC FF FF               je 0x1409f48ae
009F4BCF  4C 8B 05 02 20 5D 00            mov r8, qword ptr [rip + 0x5d2002]
009F4BD6  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
009F4BDC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
009F4BE2  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
009F4BEA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009F4BEF  C7 44 24 20 4D 6D 50 66         mov dword ptr [rsp + 0x20], 0x66506d4d
009F4BF7  44 8A 4C 24 50                  mov r9b, byte ptr [rsp + 0x50]
009F4BFC  41 8B D4                        mov edx, r12d
009F4BFF  E8 4C 4A E7 FF                  call 0x140869650
009F4C04  8B F8                           mov edi, eax
009F4C06  85 C0                           test eax, eax
009F4C08  0F 88 3D FE FF FF               js 0x1409f4a4b
009F4C0E  E9 9B FC FF FF                  jmp 0x1409f48ae
009F4C13  41 F7 81 50 07 00 00 00 01 00 00  test dword ptr [r9 + 0x750], 0x100
009F4C1E  0F 84 A0 FA FF FF               je 0x1409f46c4
009F4C24  41 F7 82 A0 05 00 00 00 00 04 00  test dword ptr [r10 + 0x5a0], 0x40000
009F4C2F  45 0F 44 FC                     cmove r15d, r12d
009F4C33  44 89 7C 24 78                  mov dword ptr [rsp + 0x78], r15d
009F4C38  E9 87 FA FF FF                  jmp 0x1409f46c4
009F4C3D  41 83 EE 01                     sub r14d, 1
009F4C41  0F 85 67 C7 13 00               jne 0x140b313ae
009F4C47  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
009F4C4C  4D 3B DC                        cmp r11, r12
009F4C4F  0F 85 9C 00 00 00               jne 0x1409f4cf1
009F4C55  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
009F4C5D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009F4C62  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
009F4C6A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009F4C6F  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009F4C73  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009F4C77  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
009F4C7F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009F4C84  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
009F4C89  4D 8B CE                        mov r9, r14
009F4C8C  4D 8B 47 08                     mov r8, qword ptr [r15 + 8]
009F4C90  49 8B 17                        mov rdx, qword ptr [r15]
009F4C93  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009F4C9B  E8 48 03 00 00                  call 0x1409f4fe8
009F4CA0  8B F8                           mov edi, eax
009F4CA2  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
009F4CA6  85 DB                           test ebx, ebx
009F4CA8  0F 85 46 01 00 00               jne 0x1409f4df4
009F4CAE  8B 8C 24 90 00 00 00            mov ecx, dword ptr [rsp + 0x90]
009F4CB5  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009F4CBD  89 08                           mov dword ptr [rax], ecx
009F4CBF  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
009F4CC4  E9 8C FD FF FF                  jmp 0x1409f4a55
009F4CC9  41 BC 01 00 00 00               mov r12d, 1
009F4CCF  8B 7C 24 78                     mov edi, dword ptr [rsp + 0x78]
009F4CD3  4C 8B BC 24 88 00 00 00         mov r15, qword ptr [rsp + 0x88]
009F4CDB  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
009F4CE0  8B 5C 24 74                     mov ebx, dword ptr [rsp + 0x74]
009F4CE4  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
009F4CEC  E9 64 FD FF FF                  jmp 0x1409f4a55
009F4CF1  BF F2 00 00 C0                  mov edi, 0xc00000f2
009F4CF6  E9 55 FD FF FF                  jmp 0x1409f4a50
009F4CFB  33 D2                           xor edx, edx
009F4CFD  49 8B CE                        mov rcx, r14
009F4D00  E8 6B DB 18 00                  call 0x140b82870
009F4D05  E9 91 FD FF FF                  jmp 0x1409f4a9b
009F4D0A  B8 F0 00 00 C0                  mov eax, 0xc00000f0
009F4D0F  E9 89 FD FF FF                  jmp 0x1409f4a9d
009F4D14  39 1D 92 28 44 00               cmp dword ptr [rip + 0x442892], ebx
009F4D1A  0F 85 68 C6 13 00               jne 0x140b31388
009F4D20  B8 BB 00 00 C0                  mov eax, 0xc00000bb
009F4D25  E9 73 FD FF FF                  jmp 0x1409f4a9d
009F4D2A  0F 10 12                        movups xmm2, xmmword ptr [rdx]
009F4D2D  0F 11 94 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm2
009F4D35  0F 10 42 10                     movups xmm0, xmmword ptr [rdx + 0x10]
009F4D39  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
009F4D41  F2 0F 10 4A 20                  movsd xmm1, qword ptr [rdx + 0x20]
009F4D46  F2 0F 11 8C 24 C0 00 00 00      movsd qword ptr [rsp + 0xc0], xmm1
009F4D4F  66 41 0F 7E D5                  movd r13d, xmm2
009F4D54  45 85 ED                        test r13d, r13d
009F4D57  74 14                           je 0x1409f4d6d
009F4D59  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
009F4D61  48 C1 E8 20                     shr rax, 0x20
009F4D65  85 C0                           test eax, eax
009F4D67  0F 84 FE FA FF FF               je 0x1409f486b
009F4D6D  B8 F3 00 00 C0                  mov eax, 0xc00000f3
009F4D72  E9 26 FD FF FF                  jmp 0x1409f4a9d
009F4D77  48 8B D0                        mov rdx, rax
009F4D7A  48 C1 E2 04                     shl rdx, 4
009F4D7E  B9 40 00 00 00                  mov ecx, 0x40
009F4D83  41 B8 4D 6D 4D 72               mov r8d, 0x724d6d4d
009F4D89  E8 B2 67 96 FF                  call 0x14035b540
009F4D8E  4C 8B F8                        mov r15, rax
009F4D91  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
009F4D99  48 85 C0                        test rax, rax
009F4D9C  0F 85 02 FB FF FF               jne 0x1409f48a4
009F4DA2  4C 8D BC 24 30 02 00 00         lea r15, [rsp + 0x230]
009F4DAA  E9 ED C5 13 00                  jmp 0x140b3139c
009F4DAF  41 8B D5                        mov edx, r13d
009F4DB2  48 C1 E2 04                     shl rdx, 4
009F4DB6  B9 40 00 00 00                  mov ecx, 0x40
009F4DBB  41 B8 4D 6D 4D 72               mov r8d, 0x724d6d4d
009F4DC1  E8 7A 67 96 FF                  call 0x14035b540
009F4DC6  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
009F4DCB  48 85 C0                        test rax, rax
009F4DCE  0F 84 C8 C5 13 00               je 0x140b3139c
009F4DD4  E9 E5 FD FF FF                  jmp 0x1409f4bbe
009F4DD9  4C 8D 84 24 F8 00 00 00         lea r8, [rsp + 0xf8]
009F4DE1  33 D2                           xor edx, edx
009F4DE3  E8 38 1A 82 FF                  call 0x140216820
009F4DE8  41 8B DC                        mov ebx, r12d
009F4DEB  89 5C 24 74                     mov dword ptr [rsp + 0x74], ebx
009F4DEF  E9 3A FB FF FF                  jmp 0x1409f492e
009F4DF4  33 D2                           xor edx, edx
009F4DF6  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
009F4DFE  E8 2D 2F 82 FF                  call 0x140217d30
009F4E03  33 DB                           xor ebx, ebx
009F4E05  89 5C 24 74                     mov dword ptr [rsp + 0x74], ebx
009F4E09  E9 A0 FE FF FF                  jmp 0x1409f4cae
009F4E0E  33 D2                           xor edx, edx
009F4E10  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
009F4E18  E8 13 2F 82 FF                  call 0x140217d30
009F4E1D  E9 3C FC FF FF                  jmp 0x1409f4a5e
009F4E22  BA 4D 6D 50 66                  mov edx, 0x66506d4d
009F4E27  E8 B4 2A 90 FF                  call 0x1402f78e0
009F4E2C  E9 3E FC FF FF                  jmp 0x1409f4a6f
009F4E31  33 D2                           xor edx, edx
009F4E33  49 8B CF                        mov rcx, r15
009F4E36  E8 35 DA 18 00                  call 0x140b82870
009F4E3B  E9 4A FC FF FF                  jmp 0x1409f4a8a
009F4E40  B8 F1 00 00 C0                  mov eax, 0xc00000f1
009F4E45  E9 53 FC FF FF                  jmp 0x1409f4a9d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetInformationVirtualMemory(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned int v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned int v_stack_m2EC;
    unsigned int v_stack_m2F0;
    unsigned int v_stack_m2F4;
    unsigned __int64 v_stack_m300;
    unsigned int v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int8 v_stack_m318;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p230;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p74;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned int v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pF8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (832);
    result = (*(unsigned __int64 *)(v_rip + 4284836)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m288 = a4;
    v_stack_m2D0 = a3;
    v_stack_m300 = a1;
    v_stack_m290 = a1;
    v_stack_m270 = v_xmm0;
    v_stack_m260 = v_xmm0;
    v_stack_m250 = v_xmm0;
    v_r15 = 0;
    v_stack_m2F0 = 0;
    v_rbx = 0;
    v_stack_m2F4 = 0;
    v_stack_m310 = v_stack_m238;
    v_rdi = 0;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_009F465B;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - (1));
    if (condition_is_equal) goto loc_009F465B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F4ADB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F465B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F465B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F465B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F465B;
    if (((unsigned int)(a1)) != 1) goto loc_009F4D0A;
loc_009F465B:
    if (a5 == 0) goto loc_009F4D6D;
    if (((unsigned int)((unsigned int)(a6))) != 4) goto loc_009F4AEB;
    if (((unsigned int)((unsigned int)(a2))) == ((unsigned int)((unsigned int)(a6)))) goto loc_009F4D14;
loc_009F467D:
    if ((a3 - 1) > a4) goto loc_009F4E40;
    v_stack_m298 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m2E0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if (((unsigned int)((unsigned int)(a2))) == 2) goto loc_009F4C13;
loc_009F46C4:
    result = 0;
    v_stack_m2C8 = v_xmm0;
    v_stack_m2B8 = v_xmm0;
    v_stack_m2A8 = 0;
    v_stack_m318 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_009F4B36;
    result = (a3) << (4);
    if (result == 0) goto loc_009F47FB;
    if ((((unsigned __int8)(a4)) & (3)) != 0) goto loc_009F480A;
    if ((result + a4 * 1) > 0) goto loc_009F480F;
    if ((result + a4 * 1) < a4) goto loc_009F480F;
loc_009F472D:
    if (((unsigned int)((unsigned int)(a2))) == 2) goto loc_009F4742;
    if ((((unsigned __int8)(a5)) & (3)) == 0) goto loc_009F4843;
    result = ExRaiseDatatypeMisalignment((unsigned int)(a6), a5, result + a4 * 1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
loc_009F4742:
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_009F4764;
    if ((((unsigned __int8)(a5)) & (3)) != 0) goto loc_009F4817;
    a1 = ((unsigned int)(a6)) + (a5);
    if (a1 > 0) goto loc_009F481C;
    if (a1 < a5) goto loc_009F481C;
loc_009F4764:
    v_stack_m2C8 = v_xmm2;
    v_stack_m2B8 = v_xmm0;
    v_stack_m2A8 = v_xmm1;
    v_stack_m2EC = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_009F4839;
    result = (v_stack_m2C8) >> (32);
    if ((unsigned int)(result) != 0) goto loc_009F4839;
    result = ProbeForWrite(v_stack_m2C0, result + 4, (unsigned int)((unsigned int)(result + 4)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    v_r13 = ((unsigned int)((unsigned int)(result))) << (4);
    if (v_r13 == 0) goto loc_009F47EC;
    if (((v_stack_m2B8) & (3)) != 0) goto loc_009F4824;
    if ((v_stack_m2B8 + v_r13 * 1) > 0) goto loc_009F4829;
    if ((v_stack_m2B8 + v_r13 * 1) < v_stack_m2B8) goto loc_009F4829;
loc_009F47EC:
    goto loc_009F485F;
loc_009F47FB:
    goto loc_009F472D;
loc_009F480A:
    result = ExRaiseDatatypeMisalignment(v_stack_m2B8 + v_r13 * 1, result + 4, (unsigned int)((unsigned int)(result + 4)), v_stack_m2E0);
loc_009F480F:
    goto loc_009F472D;
loc_009F4817:
    result = ExRaiseDatatypeMisalignment(v_stack_m2B8 + v_r13 * 1, result + 4, (unsigned int)((unsigned int)(result + 4)), v_stack_m2E0);
loc_009F481C:
    goto loc_009F4764;
loc_009F4824:
    result = ExRaiseDatatypeMisalignment(v_stack_m2B8 + v_r13 * 1, result + 4, (unsigned int)((unsigned int)(result + 4)), v_stack_m2E0);
loc_009F4829:
    v_stack_m2EC = (unsigned int)((unsigned int)(v_stack_m2C8));
    goto loc_009F47EC;
loc_009F4839:
    goto loc_009F4A9D;
loc_009F4843:
    if ((result + 4) < 0) { v_r15 = result + 4; }
    v_stack_m308 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    v_stack_m2EC = (unsigned int)((unsigned int)(v_stack_m2C8));
loc_009F485F:
    goto loc_009F486B;
loc_009F486B:
    if (v_stack_m300 != -1) goto loc_009F4AF2;
    v_stack_m2E8 = v_stack_m2E0;
loc_009F4882:
    v_stack_m2E0 = v_stack_m138;
    if (v_stack_m2D0 > 16) goto loc_009F4D77;
loc_009F48A4:
    if (((unsigned int)((unsigned int)(a2))) == 2) goto loc_009F4BB4;
loc_009F48AE:
    a3 = (v_stack_m2D0) << (4);
    result = memcpy(v_stack_m138, v_stack_m288, a3, v_stack_m2E0);
    if (((unsigned int)((unsigned int)(a2))) == 2) {
        a3 = (unsigned int)((unsigned int)(v_stack_m2EC));
        a3 = (a3) << (4);
        a2 = v_stack_m2B8;
        a1 = v_stack_m310;
        result = memcpy(a1, a2, a3, v_stack_m2E0);
    }
    goto loc_009F4911;
loc_009F4911:
    if ((*(unsigned __int64 *)(v_stack_m298 + 184)) != v_stack_m2E8) goto loc_009F4B53;
loc_009F492E:
    v_r10 = 0;
    a3 = (v_stack_m2D0) << (4);
    a3 = (a3) + (v_stack_m138);
loc_009F4946:
    if (v_stack_m138 >= a3) goto loc_009F49AE;
    if (*(unsigned __int64 *)(v_stack_m138 + 8) == 0) goto loc_009F4AC7;
    result = (*(unsigned __int64 *)(v_stack_m138) - 1) + (*(unsigned __int64 *)(v_stack_m138 + 8));
    if (result < (*(unsigned __int64 *)(v_stack_m138))) goto loc_009F4AC7;
    result = (*(unsigned __int64 *)(v_stack_m138) - 1) + (*(unsigned __int64 *)(v_stack_m138 + 8));
    if (result > (*(unsigned __int64 *)(v_stack_m138))) goto loc_009F4AC7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m138))) & (0xFFFULL));
    result = (result) + (0xFFFULL);
    result = (result) + (*(unsigned __int64 *)(v_stack_m138 + 8));
    result = (result) >> (12);
    result = (result) + (0);
    if (result < 0) goto loc_009F4AC7;
    a2 = (v_stack_m138) + (16);
    goto loc_009F4946;
loc_009F49AE:
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_009F4B81;
    if (((v_stack_m308) & (0xFFFFFFFEULL)) != 0) goto loc_009F4B92;
    result = MiGetEffectivePagePriorityThread(v_stack_m298, a2, v_stack_m298, *(unsigned __int64 *)(v_stack_m138));
    result = (unsigned int)((result) & (7));
    a2 = (unsigned int)((a2) & (64));
    a2 = (unsigned int)((a2) + (0x20000ULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(a2)) & (7));
    result = (unsigned int)((a1 * 8) | (a2));
    if (((unsigned int)(a1)) < 5) {
        result = (unsigned int)((result) & (0xFFFFFFEFULL));
        result = (unsigned int)((result) | (40));
    }
    a2 = (unsigned __int8)(((unsigned int)(v_stack_m308)) & (1));
    a2 = (unsigned __int8)(-(a2));
    a4 = (unsigned int)((*(unsigned __int64 *)(v_stack_m138)) & (0x3C000ULL));
    a4 = (unsigned int)((a4) + (0x4000ULL));
    a4 = (unsigned int)((a4) | ((unsigned int)(result)));
    result = PsGetIoPriorityThread(v_stack_m298, a2, v_stack_m298, a4);
    if (((unsigned int)(result)) <= 1) goto loc_009F4AD1;
loc_009F4A2F:
    a3 = (v_stack_m2E8) + (0x400ULL);
    result = MiPrefetchVirtualMemory(v_stack_m2D0, v_stack_m138, a3, a4);
loc_009F4A49:
loc_009F4A4B:
loc_009F4A50:
loc_009F4A55:
    if (((1) & (0)) != 0) goto loc_009F4E0E;
loc_009F4A5E:
    if (v_stack_m2A0 != 0) goto loc_009F4E22;
loc_009F4A6F:
    if (v_stack_m300 != -1) goto loc_009F4B6A;
loc_009F4A79:
    if (v_stack_m138 != v_stack_m138) goto loc_009F4E31;
loc_009F4A8A:
    if (v_stack_m310 != v_stack_m238) goto loc_009F4CFB;
loc_009F4A9B:
loc_009F4A9D:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m138, a3, a4);
    v_rsp = (v_rsp) + (832);
    return result;
loc_009F4AC7:
    goto loc_009F4A4B;
loc_009F4AD1:
    goto loc_009F4A2F;
loc_009F4ADB:
    if (((unsigned int)((unsigned int)(a6))) == 40) goto loc_009F467D;
loc_009F4AEB:
    goto loc_009F4A9D;
loc_009F4AF2:
    v_stack_p28 = v_stack_p80;
    v_stack_p20 = 0x66506D4DULL;
    result = ObpReferenceObjectByHandleWithTag((unsigned int)(a6), 8, *(unsigned __int64 *)(v_rip + 6102943), (unsigned __int8)(result));
    if (!sign_flag) goto loc_009F4882;
    goto loc_009F4A9D;
loc_009F4B36:
    if (((unsigned int)(v_stack_m310)) == 2) goto loc_009F4D2A;
    v_stack_p60 = (unsigned int)((unsigned int)(*(unsigned int *)(8)));
    goto loc_009F486B;
loc_009F4B53:
    if (((unsigned int)(v_stack_m310 - 3)) > 1) goto loc_009F4DD9;
    goto loc_009F4A4B;
loc_009F4B6A:
    result = ObfDereferenceObjectWithTag(v_stack_p80, (unsigned int)(0x66506D4DULL), *(unsigned __int64 *)(v_rip + 6102943), (unsigned __int8)(result));
    goto loc_009F4A79;
loc_009F4B81:
    v_r14 = (unsigned int)((v_stack_m310) - (1));
    if (condition_is_not_equal) goto loc_009F4C3D;
    if (v_stack_p60 <= 5) goto loc_009F4B9C;
loc_009F4B92:
    goto loc_009F4A4B;
loc_009F4B9C:
    result = MiProcessVaRangesInfoClass(v_stack_m2D0, v_stack_m138, 1, (unsigned int)(v_stack_p60));
    goto loc_009F4A49;
loc_009F4BB4:
    if (((unsigned int)((unsigned int)(v_stack_pA0))) > 16) goto loc_009F4DAF;
loc_009F4BBE:
    if (v_stack_pB8 == 0) goto loc_009F48AE;
    v_stack_p28 = v_stack_pC8;
    v_stack_p20 = 0x66506D4DULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_pB8, 1, *(unsigned __int64 *)(v_rip + 6103042), v_stack_p50);
    if (sign_flag) goto loc_009F4A4B;
    goto loc_009F48AE;
loc_009F4C13:
    if (((*(unsigned int *)(v_stack_p50 + 1872)) & (256)) == 0) goto loc_009F46C4;
    v_r15 = v_stack_m138;
    if (((*(unsigned int *)(result + 1440)) & (0x40000ULL)) == 0) { v_r15 = 1; }
    v_stack_p78 = (unsigned int)(v_r15);
    goto loc_009F46C4;
loc_009F4C3D:
    v_r14 = (unsigned int)((v_r14) - (1));
    if (v_stack_m2D0 != 1) goto loc_009F4CF1;
    v_stack_p40 = v_stack_pC0;
    v_stack_p38 = v_stack_pC8;
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_p78));
    v_stack_p28 = v_stack_p90;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_pA0));
    result = MiCfgMarkValidEntries(v_stack_p80, *(unsigned __int64 *)(v_r15), *(unsigned __int64 *)(v_r15 + 8), v_stack_p58);
    v_stack_p78 = (unsigned int)(result);
    if ((unsigned int)(v_stack_p10) != 0) goto loc_009F4DF4;
loc_009F4CAE:
    *(unsigned int *)(v_stack_pA8) = (unsigned int)((unsigned int)(v_stack_p90));
    goto loc_009F4A55;
loc_009F4CF1:
    goto loc_009F4A50;
loc_009F4CFB:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p58, a2, *(unsigned __int64 *)(v_r15 + 8), v_stack_p58);
    goto loc_009F4A9B;
loc_009F4D0A:
    goto loc_009F4A9D;
loc_009F4D14:
    goto loc_009F4A9D;
loc_009F4D2A:
    v_stack_pA0 = v_xmm2;
    v_stack_pB0 = v_xmm0;
    v_stack_pC0 = v_xmm1;
    if ((unsigned int)(v_stack_p68) == 0) goto loc_009F4D6D;
    result = (v_stack_pA0) >> (32);
    if ((unsigned int)(result) == 0) goto loc_009F486B;
loc_009F4D6D:
    goto loc_009F4A9D;
loc_009F4D77:
    a2 = ((unsigned int)(0xC00000F3ULL)) << (4);
    result = MiAllocatePool(64, a2, (unsigned int)(0x724D6D4DULL), v_stack_p58);
    v_stack_p88 = result;
    if (result != 0) goto loc_009F48A4;
loc_009F4DAF:
    a2 = ((unsigned int)((unsigned int)(v_stack_p68))) << (4);
    result = MiAllocatePool(64, a2, (unsigned int)(0x724D6D4DULL), v_stack_p58);
    v_stack_p58 = result;
    goto loc_009F4BBE;
loc_009F4DD9:
    a2 = 0;
    result = KiStackAttachProcess(64, a2, v_stack_pF8, v_stack_p58);
    v_stack_p74 = 1;
    goto loc_009F492E;
loc_009F4DF4:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF8, a2, v_stack_pF8, v_stack_p58);
    v_rbx = 0;
    v_stack_p74 = 0;
    goto loc_009F4CAE;
loc_009F4E0E:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF8, a2, v_stack_pF8, v_stack_p58);
    goto loc_009F4A5E;
loc_009F4E22:
    result = ObfDereferenceObjectWithTag(v_stack_pF8, (unsigned int)(0x66506D4DULL), v_stack_pF8, v_stack_p58);
    goto loc_009F4A6F;
loc_009F4E31:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p230, a2, v_stack_pF8, v_stack_p58);
    goto loc_009F4A8A;
loc_009F4E40:
    goto loc_009F4A9D;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetInformationVirtualMemory(int64_t Arg1, int32_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint64_t v_stack_m238;
    uint64_t v_stack_m250;
    uint64_t v_stack_m260;
    uint64_t v_stack_m270;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint32_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint32_t v_stack_m2EC;
    uint32_t v_stack_m2F0;
    uint32_t v_stack_m2F4;
    uint64_t v_stack_m300;
    uint32_t v_stack_m308;
    uint64_t v_stack_m310;
    uint8_t v_stack_m318;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p230;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p74;
    uint32_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint32_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pF8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (832);
    result = (*(uint64_t *)(v_rip + 0x4161A4)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m288 = Arg4;
    v_stack_m2D0 = Arg3;
    v_stack_m300 = Arg1;
    v_stack_m290 = Arg1;
    v_stack_m270 = v_xmm0;
    v_stack_m260 = v_xmm0;
    v_stack_m250 = v_xmm0;
    local_r15 = 0;
    v_stack_m2F0 = 0;
    local_rbx = 0;
    v_stack_m2F4 = 0;
    v_stack_m310 = v_stack_m238;
    local_rdi = 0;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_009F465B;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - (1));
    if (condition_is_equal) goto loc_009F465B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F4ADB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F465B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F465B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F465B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F465B;
    if (((uint32_t)(Arg1)) != 1) goto loc_009F4D0A;
loc_009F465B:
    if (Arg5 == 0) goto loc_009F4D6D;
    if (((uint32_t)((uint32_t)(Arg6))) != 4) goto loc_009F4AEB;
    if (((uint32_t)((uint32_t)(Arg2))) == ((uint32_t)((uint32_t)(Arg6)))) goto loc_009F4D14;
loc_009F467D:
    if ((Arg3 - 1) > Arg4) goto loc_009F4E40;
    v_stack_m298 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m2E0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if (((uint32_t)((uint32_t)(Arg2))) == 2) goto loc_009F4C13;
loc_009F46C4:
    result = 0;
    v_stack_m2C8 = v_xmm0;
    v_stack_m2B8 = v_xmm0;
    v_stack_m2A8 = 0;
    v_stack_m318 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_009F4B36;
    result = (Arg3) << (4);
    if (result == 0) goto loc_009F47FB;
    if ((((uint8_t)(Arg4)) & (3)) != 0) goto loc_009F480A;
    if ((result + Arg4 * 1) > 0) goto loc_009F480F;
    if ((result + Arg4 * 1) < Arg4) goto loc_009F480F;
loc_009F472D:
    if (((uint32_t)((uint32_t)(Arg2))) == 2) goto loc_009F4742;
    if ((((uint8_t)(Arg5)) & (3)) == 0) goto loc_009F4843;
    result = ExRaiseDatatypeMisalignment((uint32_t)(Arg6), Arg5, result + Arg4 * 1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
loc_009F4742:
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_009F4764;
    if ((((uint8_t)(Arg5)) & (3)) != 0) goto loc_009F4817;
    Arg1 = ((uint32_t)(Arg6)) + (Arg5);
    if (Arg1 > 0) goto loc_009F481C;
    if (Arg1 < Arg5) goto loc_009F481C;
loc_009F4764:
    v_stack_m2C8 = v_xmm2;
    v_stack_m2B8 = v_xmm0;
    v_stack_m2A8 = v_xmm1;
    v_stack_m2EC = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_009F4839;
    result = (v_stack_m2C8) >> (32);
    if ((uint32_t)(result) != 0) goto loc_009F4839;
    result = ProbeForWrite(v_stack_m2C0, result + 4, (uint32_t)((uint32_t)(result + 4)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    local_r13 = ((uint32_t)((uint32_t)(result))) << (4);
    if (local_r13 == 0) goto loc_009F47EC;
    if (((v_stack_m2B8) & (3)) != 0) goto loc_009F4824;
    if ((v_stack_m2B8 + local_r13 * 1) > 0) goto loc_009F4829;
    if ((v_stack_m2B8 + local_r13 * 1) < v_stack_m2B8) goto loc_009F4829;
loc_009F47EC:
    goto loc_009F485F;
loc_009F47FB:
    goto loc_009F472D;
loc_009F480A:
    result = ExRaiseDatatypeMisalignment(v_stack_m2B8 + local_r13 * 1, result + 4, (uint32_t)((uint32_t)(result + 4)), v_stack_m2E0);
loc_009F480F:
    goto loc_009F472D;
loc_009F4817:
    result = ExRaiseDatatypeMisalignment(v_stack_m2B8 + local_r13 * 1, result + 4, (uint32_t)((uint32_t)(result + 4)), v_stack_m2E0);
loc_009F481C:
    goto loc_009F4764;
loc_009F4824:
    result = ExRaiseDatatypeMisalignment(v_stack_m2B8 + local_r13 * 1, result + 4, (uint32_t)((uint32_t)(result + 4)), v_stack_m2E0);
loc_009F4829:
    v_stack_m2EC = (uint32_t)((uint32_t)(v_stack_m2C8));
    goto loc_009F47EC;
loc_009F4839:
    goto loc_009F4A9D;
loc_009F4843:
    if ((result + 4) < 0) { local_r15 = result + 4; }
    v_stack_m308 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    v_stack_m2EC = (uint32_t)((uint32_t)(v_stack_m2C8));
loc_009F485F:
    goto loc_009F486B;
loc_009F486B:
    if (v_stack_m300 != -1) goto loc_009F4AF2;
    v_stack_m2E8 = v_stack_m2E0;
loc_009F4882:
    v_stack_m2E0 = v_stack_m138;
    if (v_stack_m2D0 > 16) goto loc_009F4D77;
loc_009F48A4:
    if (((uint32_t)((uint32_t)(Arg2))) == 2) goto loc_009F4BB4;
loc_009F48AE:
    Arg3 = (v_stack_m2D0) << (4);
    result = memcpy(v_stack_m138, v_stack_m288, Arg3, v_stack_m2E0);
    if (((uint32_t)((uint32_t)(Arg2))) == 2) {
        Arg3 = (uint32_t)((uint32_t)(v_stack_m2EC));
        Arg3 = (Arg3) << (4);
        Arg2 = v_stack_m2B8;
        Arg1 = v_stack_m310;
        result = memcpy(Arg1, Arg2, Arg3, v_stack_m2E0);
    }
    goto loc_009F4911;
loc_009F4911:
    if ((*(uint64_t *)(v_stack_m298 + 0xB8)) != v_stack_m2E8) goto loc_009F4B53;
loc_009F492E:
    local_r10 = 0;
    Arg3 = (v_stack_m2D0) << (4);
    Arg3 = (Arg3) + (v_stack_m138);
loc_009F4946:
    if (v_stack_m138 >= Arg3) goto loc_009F49AE;
    if (*(uint64_t *)(v_stack_m138 + 0x8) == 0) goto loc_009F4AC7;
    result = (*(uint64_t *)(v_stack_m138) - 1) + (*(uint64_t *)(v_stack_m138 + 0x8));
    if (result < (*(uint64_t *)(v_stack_m138))) goto loc_009F4AC7;
    result = (*(uint64_t *)(v_stack_m138) - 1) + (*(uint64_t *)(v_stack_m138 + 0x8));
    if (result > (*(uint64_t *)(v_stack_m138))) goto loc_009F4AC7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m138))) & (0xFFFULL));
    result = (result) + (0xFFFULL);
    result = (result) + (*(uint64_t *)(v_stack_m138 + 0x8));
    result = (result) >> (12);
    result = (result) + (0);
    if (result < 0) goto loc_009F4AC7;
    Arg2 = (v_stack_m138) + (16);
    goto loc_009F4946;
loc_009F49AE:
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_009F4B81;
    if (((v_stack_m308) & (0xFFFFFFFEULL)) != 0) goto loc_009F4B92;
    result = MiGetEffectivePagePriorityThread(v_stack_m298, Arg2, v_stack_m298, *(uint64_t *)(v_stack_m138));
    result = (uint32_t)((result) & (7));
    Arg2 = (uint32_t)((Arg2) & (64));
    Arg2 = (uint32_t)((Arg2) + (0x20000ULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(Arg2)) & (7));
    result = (uint32_t)((Arg1 * 8) | (Arg2));
    if (((uint32_t)(Arg1)) < 5) {
        result = (uint32_t)((result) & (0xFFFFFFEFULL));
        result = (uint32_t)((result) | (40));
    }
    Arg2 = (uint8_t)(((uint32_t)(v_stack_m308)) & (1));
    Arg2 = (uint8_t)(-(Arg2));
    Arg4 = (uint32_t)((*(uint64_t *)(v_stack_m138)) & (0x3C000ULL));
    Arg4 = (uint32_t)((Arg4) + (0x4000ULL));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(result)));
    result = PsGetIoPriorityThread(v_stack_m298, Arg2, v_stack_m298, Arg4);
    if (((uint32_t)(result)) <= 1) goto loc_009F4AD1;
loc_009F4A2F:
    Arg3 = (v_stack_m2E8) + (0x400ULL);
    result = MiPrefetchVirtualMemory(v_stack_m2D0, v_stack_m138, Arg3, Arg4);
loc_009F4A49:
loc_009F4A4B:
loc_009F4A50:
loc_009F4A55:
    if (((1) & (0)) != 0) goto loc_009F4E0E;
loc_009F4A5E:
    if (v_stack_m2A0 != 0) goto loc_009F4E22;
loc_009F4A6F:
    if (v_stack_m300 != -1) goto loc_009F4B6A;
loc_009F4A79:
    if (v_stack_m138 != v_stack_m138) goto loc_009F4E31;
loc_009F4A8A:
    if (v_stack_m310 != v_stack_m238) goto loc_009F4CFB;
loc_009F4A9B:
loc_009F4A9D:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m138, Arg3, Arg4);
    local_rsp = (local_rsp) + (832);
    return result;
loc_009F4AC7:
    goto loc_009F4A4B;
loc_009F4AD1:
    goto loc_009F4A2F;
loc_009F4ADB:
    if (((uint32_t)((uint32_t)(Arg6))) == 40) goto loc_009F467D;
loc_009F4AEB:
    goto loc_009F4A9D;
loc_009F4AF2:
    v_stack_p28 = v_stack_p80;
    v_stack_p20 = 0x66506D4DULL;
    result = ObpReferenceObjectByHandleWithTag((uint32_t)(Arg6), 8, *(uint64_t *)(v_rip + 0x5D1F9F), (uint8_t)(result));
    if (!sign_flag) goto loc_009F4882;
    goto loc_009F4A9D;
loc_009F4B36:
    if (((uint32_t)(v_stack_m310)) == 2) goto loc_009F4D2A;
    v_stack_p60 = (uint32_t)((uint32_t)(*(uint32_t *)(8)));
    goto loc_009F486B;
loc_009F4B53:
    if (((uint32_t)(v_stack_m310 - 3)) > 1) goto loc_009F4DD9;
    goto loc_009F4A4B;
loc_009F4B6A:
    result = ObfDereferenceObjectWithTag(v_stack_p80, (uint32_t)(0x66506D4DULL), *(uint64_t *)(v_rip + 0x5D1F9F), (uint8_t)(result));
    goto loc_009F4A79;
loc_009F4B81:
    local_r14 = (uint32_t)((v_stack_m310) - (1));
    if (condition_is_not_equal) goto loc_009F4C3D;
    if (v_stack_p60 <= 5) goto loc_009F4B9C;
loc_009F4B92:
    goto loc_009F4A4B;
loc_009F4B9C:
    result = MiProcessVaRangesInfoClass(v_stack_m2D0, v_stack_m138, 1, (uint32_t)(v_stack_p60));
    goto loc_009F4A49;
loc_009F4BB4:
    if (((uint32_t)((uint32_t)(v_stack_pA0))) > 16) goto loc_009F4DAF;
loc_009F4BBE:
    if (v_stack_pB8 == 0) goto loc_009F48AE;
    v_stack_p28 = v_stack_pC8;
    v_stack_p20 = 0x66506D4DULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_pB8, 1, *(uint64_t *)(v_rip + 0x5D2002), v_stack_p50);
    if (sign_flag) goto loc_009F4A4B;
    goto loc_009F48AE;
loc_009F4C13:
    if (((*(uint32_t *)(v_stack_p50 + 0x750)) & (256)) == 0) goto loc_009F46C4;
    local_r15 = v_stack_m138;
    if (((*(uint32_t *)(result + 0x5A0)) & (0x40000ULL)) == 0) { local_r15 = 1; }
    v_stack_p78 = (uint32_t)(local_r15);
    goto loc_009F46C4;
loc_009F4C3D:
    local_r14 = (uint32_t)((local_r14) - (1));
    if (v_stack_m2D0 != 1) goto loc_009F4CF1;
    v_stack_p40 = v_stack_pC0;
    v_stack_p38 = v_stack_pC8;
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_p78));
    v_stack_p28 = v_stack_p90;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_pA0));
    result = MiCfgMarkValidEntries(v_stack_p80, *(uint64_t *)(local_r15), *(uint64_t *)(local_r15 + 0x8), v_stack_p58);
    v_stack_p78 = (uint32_t)(result);
    if ((uint32_t)(v_stack_p10) != 0) goto loc_009F4DF4;
loc_009F4CAE:
    *(uint32_t *)(v_stack_pA8) = (uint32_t)((uint32_t)(v_stack_p90));
    goto loc_009F4A55;
loc_009F4CF1:
    goto loc_009F4A50;
loc_009F4CFB:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p58, Arg2, *(uint64_t *)(local_r15 + 0x8), v_stack_p58);
    goto loc_009F4A9B;
loc_009F4D0A:
    goto loc_009F4A9D;
loc_009F4D14:
    goto loc_009F4A9D;
loc_009F4D2A:
    v_stack_pA0 = v_xmm2;
    v_stack_pB0 = v_xmm0;
    v_stack_pC0 = v_xmm1;
    if ((uint32_t)(v_stack_p68) == 0) goto loc_009F4D6D;
    result = (v_stack_pA0) >> (32);
    if ((uint32_t)(result) == 0) goto loc_009F486B;
loc_009F4D6D:
    goto loc_009F4A9D;
loc_009F4D77:
    Arg2 = ((uint32_t)(0xC00000F3ULL)) << (4);
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x724D6D4DULL), v_stack_p58);
    v_stack_p88 = result;
    if (result != 0) goto loc_009F48A4;
loc_009F4DAF:
    Arg2 = ((uint32_t)((uint32_t)(v_stack_p68))) << (4);
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x724D6D4DULL), v_stack_p58);
    v_stack_p58 = result;
    goto loc_009F4BBE;
loc_009F4DD9:
    Arg2 = 0;
    result = KiStackAttachProcess(64, Arg2, v_stack_pF8, v_stack_p58);
    v_stack_p74 = 1;
    goto loc_009F492E;
loc_009F4DF4:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF8, Arg2, v_stack_pF8, v_stack_p58);
    local_rbx = 0;
    v_stack_p74 = 0;
    goto loc_009F4CAE;
loc_009F4E0E:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF8, Arg2, v_stack_pF8, v_stack_p58);
    goto loc_009F4A5E;
loc_009F4E22:
    result = ObfDereferenceObjectWithTag(v_stack_pF8, (uint32_t)(0x66506D4DULL), v_stack_pF8, v_stack_p58);
    goto loc_009F4A6F;
loc_009F4E31:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p230, Arg2, v_stack_pF8, v_stack_p58);
    goto loc_009F4A8A;
loc_009F4E40:
    goto loc_009F4A9D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `- 0x1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F4580&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
