# NtGetWriteWatch

- RVA: `0x002A7CE0`–`0x002A85E9` (길이 `2,313` bytes)
- VA: `0x00000001402A7CE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00068CC0`
- 디코드: `505`개 명령, `2,313/2,313` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002A7E17` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x002A7F39` → [MiObtainReferencedVadEx](../31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x002A7F92` → [MiGetVadMandatoryPageSize](MiGetVadMandatoryPageSize_function_002A85F0.md) (function, `0x002A85F0`)
- `0x002A7FD4` → [MiLocateLockedVadEvent](MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x002A7FF8` → [MiGetVadMandatoryPageSize](MiGetVadMandatoryPageSize_function_002A85F0.md) (function, `0x002A85F0`)
- `0x002A8015` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002A804E` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002A80AD` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002A80E5` → [MiWorkingSetIsContended](MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x002A80F2` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x002A811A` → [MiGetNextPageTable](../2C/MiGetNextPageTable_function_002C2EE0.md) (function, `0x002C2EE0`)
- `0x002A8148` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002A817D` → [MiUnlockAndDereferenceVad](../31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x002A81DE` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x002A827B` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002A8286` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x002A8334` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x002A8380` → [ObReferenceObjectByHandleWithTag](../../page/86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x002A83AC` → [KiStackAttachProcess](../21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x002A8425` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002A842A` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002A8441` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002A8449` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002A84F1` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x002A8512` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x002A8522` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002A8527` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002A853A` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002A854A` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002A855E` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x002A8575` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x002A85A4` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002A85DF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002A7CF3` → RVA `0x00E0A740` (`.data`; read)
- `0x002A8371` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x002A83FA` → RVA `0x00014578` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x002A7E17` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (`.text` → `PAGE`)
  - `0x002A8380` → [ObReferenceObjectByHandleWithTag](../../page/86/ObReferenceObjectByHandleWithTag_function_00869610.md) (`.text` → `PAGE`)
  - `0x002A85DF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x002A83E2` → [sub_006DAFCA](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A841C` → [sub_006DAFCA + 0x13](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A8435` → [sub_006DAFCA + 0x13](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A8461` → [sub_006DAFCA + 0x82](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A846A` → [sub_006DAFCA + 0x2B](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A8474` → [sub_006DAFCA + 0x2B](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A84AE` → [sub_006DAFCA + 0xB9](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A84B6` → [sub_006DAFCA + 0x96](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A84D0` → [sub_006DAFCA + 0xF4](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A84EB` → [sub_006DAFCA + 0x163](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)
  - `0x002A851A` → [sub_006DAFCA + 0x163](../6D/Unknown_function_006DAFCA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002A7CE0  40 53                           push rbx
002A7CE2  56                              push rsi
002A7CE3  57                              push rdi
002A7CE4  41 54                           push r12
002A7CE6  41 55                           push r13
002A7CE8  41 56                           push r14
002A7CEA  41 57                           push r15
002A7CEC  48 81 EC 30 09 00 00            sub rsp, 0x930
002A7CF3  48 8B 05 46 2A B6 00            mov rax, qword ptr [rip + 0xb62a46]
002A7CFA  48 33 C4                        xor rax, rsp
002A7CFD  48 89 84 24 20 09 00 00         mov qword ptr [rsp + 0x920], rax
002A7D05  4D 8B E1                        mov r12, r9
002A7D08  49 8B F0                        mov rsi, r8
002A7D0B  8B C2                           mov eax, edx
002A7D0D  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
002A7D11  4C 8B F1                        mov r14, rcx
002A7D14  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
002A7D1C  4C 8B AC 24 A0 09 00 00         mov r13, qword ptr [rsp + 0x9a0]
002A7D24  4C 89 AC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r13
002A7D2C  48 8B 94 24 98 09 00 00         mov rdx, qword ptr [rsp + 0x998]
002A7D34  48 89 94 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdx
002A7D3C  4C 8B 8C 24 90 09 00 00         mov r9, qword ptr [rsp + 0x990]
002A7D44  4C 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r9
002A7D4C  48 83 A4 24 80 00 00 00 00      and qword ptr [rsp + 0x80], 0
002A7D55  83 64 24 78 00                  and dword ptr [rsp + 0x78], 0
002A7D5A  83 64 24 48 00                  and dword ptr [rsp + 0x48], 0
002A7D5F  0F 57 C0                        xorps xmm0, xmm0
002A7D62  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
002A7D6A  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
002A7D72  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
002A7D7A  48 83 64 24 50 00               and qword ptr [rsp + 0x50], 0
002A7D80  A9 FE FF FF FF                  test eax, 0xfffffffe
002A7D85  0F 85 94 05 00 00               jne 0x1402a831f
002A7D8B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002A7D94  4C 8B B8 B8 00 00 00            mov r15, qword ptr [rax + 0xb8]
002A7D9B  40 8A B8 32 02 00 00            mov dil, byte ptr [rax + 0x232]
002A7DA2  40 84 FF                        test dil, dil
002A7DA5  75 10                           jne 0x1402a7db7
002A7DA7  48 8B 02                        mov rax, qword ptr [rdx]
002A7DAA  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
002A7DB2  E9 9A 00 00 00                  jmp 0x1402a7e51
002A7DB7  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
002A7DC1  48 3B F0                        cmp rsi, rax
002A7DC4  77 63                           ja 0x1402a7e29
002A7DC6  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
002A7DD0  48 8B C3                        mov rax, rbx
002A7DD3  48 2B C6                        sub rax, rsi
002A7DD6  49 3B C4                        cmp rax, r12
002A7DD9  72 58                           jb 0x1402a7e33
002A7DDB  48 8B CB                        mov rcx, rbx
002A7DDE  48 3B D3                        cmp rdx, rbx
002A7DE1  48 0F 42 CA                     cmovb rcx, rdx
002A7DE5  48 8B 01                        mov rax, qword ptr [rcx]
002A7DE8  48 89 01                        mov qword ptr [rcx], rax
002A7DEB  48 8B 12                        mov rdx, qword ptr [rdx]
002A7DEE  48 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdx
002A7DF6  48 85 D2                        test rdx, rdx
002A7DF9  74 42                           je 0x1402a7e3d
002A7DFB  48 B8 FF FF FF FF FF FF FF 1F   movabs rax, 0x1fffffffffffffff
002A7E05  48 3B D0                        cmp rdx, rax
002A7E08  77 3D                           ja 0x1402a7e47
002A7E0A  48 C1 E2 03                     shl rdx, 3
002A7E0E  41 B8 08 00 00 00               mov r8d, 8
002A7E14  49 8B C9                        mov rcx, r9
002A7E17  E8 A4 13 64 00                  call 0x1408e91c0
002A7E1C  4C 3B EB                        cmp r13, rbx
002A7E1F  49 0F 42 DD                     cmovb rbx, r13
002A7E23  8B 03                           mov eax, dword ptr [rbx]
002A7E25  89 03                           mov dword ptr [rbx], eax
002A7E27  EB 28                           jmp 0x1402a7e51
002A7E29  B8 F1 00 00 C0                  mov eax, 0xc00000f1
002A7E2E  E9 6F 02 00 00                  jmp 0x1402a80a2
002A7E33  B8 F2 00 00 C0                  mov eax, 0xc00000f2
002A7E38  E9 65 02 00 00                  jmp 0x1402a80a2
002A7E3D  B8 F3 00 00 C0                  mov eax, 0xc00000f3
002A7E42  E9 5B 02 00 00                  jmp 0x1402a80a2
002A7E47  B8 F3 00 00 C0                  mov eax, 0xc00000f3
002A7E4C  E9 51 02 00 00                  jmp 0x1402a80a2
002A7E51  EB 05                           jmp 0x1402a7e58
002A7E53  E9 4A 02 00 00                  jmp 0x1402a80a2
002A7E58  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
002A7E60  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
002A7E65  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
002A7E6D  48 8D 14 C5 00 00 00 00         lea rdx, [rax*8]
002A7E75  48 3D 00 01 00 00               cmp rax, 0x100
002A7E7B  0F 87 A8 04 00 00               ja 0x1402a8329
002A7E81  B8 01 00 00 00                  mov eax, 1
002A7E86  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
002A7E8E  45 33 ED                        xor r13d, r13d
002A7E91  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
002A7E99  33 C0                           xor eax, eax
002A7E9B  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
002A7EA3  33 DB                           xor ebx, ebx
002A7EA5  49 83 FE FF                     cmp r14, -1
002A7EA9  0F 85 A5 04 00 00               jne 0x1402a8354
002A7EAF  4C 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r15
002A7EB7  48 21 9C 24 88 00 00 00         and qword ptr [rsp + 0x88], rbx
002A7EBF  4C 8D 76 FF                     lea r14, [rsi - 1]
002A7EC3  4D 03 F4                        add r14, r12
002A7EC6  49 3B F6                        cmp rsi, r14
002A7EC9  0F 87 C9 04 00 00               ja 0x1402a8398
002A7ECF  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
002A7ED7  4C 3B F9                        cmp r15, rcx
002A7EDA  0F 85 C2 04 00 00               jne 0x1402a83a2
002A7EE0  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
002A7EE8  48 05 00 04 00 00               add rax, 0x400
002A7EEE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002A7EF3  48 8B FE                        mov rdi, rsi
002A7EF6  48 C1 EF 09                     shr rdi, 9
002A7EFA  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
002A7F04  48 23 FA                        and rdi, rdx
002A7F07  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
002A7F11  48 8B C1                        mov rax, rcx
002A7F14  48 03 F8                        add rdi, rax
002A7F17  4D 8B FE                        mov r15, r14
002A7F1A  49 C1 EF 09                     shr r15, 9
002A7F1E  4C 23 FA                        and r15, rdx
002A7F21  48 8B C1                        mov rax, rcx
002A7F24  4C 03 F8                        add r15, rax
002A7F27  4C 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r15
002A7F2F  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
002A7F34  33 D2                           xor edx, edx
002A7F36  48 8B CE                        mov rcx, rsi
002A7F39  E8 52 E7 06 00                  call 0x140316690
002A7F3E  4C 8B C0                        mov r8, rax
002A7F41  48 85 C0                        test rax, rax
002A7F44  0F 84 71 04 00 00               je 0x1402a83bb
002A7F4A  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
002A7F52  44 8B 48 30                     mov r9d, dword ptr [rax + 0x30]
002A7F56  45 8B D1                        mov r10d, r9d
002A7F59  41 8B C1                        mov eax, r9d
002A7F5C  B9 00 00 60 00                  mov ecx, 0x600000
002A7F61  23 C1                           and eax, ecx
002A7F63  3B C1                           cmp eax, ecx
002A7F65  0F 85 60 04 00 00               jne 0x1402a83cb
002A7F6B  41 0F B6 48 21                  movzx ecx, byte ptr [r8 + 0x21]
002A7F70  48 C1 E1 20                     shl rcx, 0x20
002A7F74  41 8B 40 1C                     mov eax, dword ptr [r8 + 0x1c]
002A7F78  48 0B C8                        or rcx, rax
002A7F7B  48 C1 E1 0C                     shl rcx, 0xc
002A7F7F  48 81 C9 FF 0F 00 00            or rcx, 0xfff
002A7F86  4C 3B F1                        cmp r14, rcx
002A7F89  0F 87 3C 04 00 00               ja 0x1402a83cb
002A7F8F  49 8B C8                        mov rcx, r8
002A7F92  E8 59 06 00 00                  call 0x1402a85f0
002A7F97  4C 8B F0                        mov r14, rax
002A7F9A  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
002A7FA2  B9 01 00 00 00                  mov ecx, 1
002A7FA7  48 3B C1                        cmp rax, rcx
002A7FAA  0F 87 25 04 00 00               ja 0x1402a83d5
002A7FB0  B8 00 00 A0 00                  mov eax, 0xa00000
002A7FB5  44 23 C8                        and r9d, eax
002A7FB8  44 3B C8                        cmp r9d, eax
002A7FBB  0F 84 31 04 00 00               je 0x1402a83f2
002A7FC1  4C 8B E1                        mov r12, rcx
002A7FC4  4C 89 A4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r12
002A7FCC  BA 04 00 00 00                  mov edx, 4
002A7FD1  49 8B C8                        mov rcx, r8
002A7FD4  E8 33 FA FF FF                  call 0x1402a7a0c
002A7FD9  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002A7FDE  41 0F B6 50 20                  movzx edx, byte ptr [r8 + 0x20]
002A7FE3  48 C1 E2 20                     shl rdx, 0x20
002A7FE7  41 8B 48 18                     mov ecx, dword ptr [r8 + 0x18]
002A7FEB  48 0B D1                        or rdx, rcx
002A7FEE  48 C1 EE 0C                     shr rsi, 0xc
002A7FF2  48 2B F2                        sub rsi, rdx
002A7FF5  49 8B C8                        mov rcx, r8
002A7FF8  E8 F3 05 00 00                  call 0x1402a85f0
002A7FFD  4C 8B C0                        mov r8, rax
002A8000  33 D2                           xor edx, edx
002A8002  48 8B C6                        mov rax, rsi
002A8005  49 F7 F0                        div r8
002A8008  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002A800D  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
002A8012  48 8B CE                        mov rcx, rsi
002A8015  E8 D6 4B FD FF                  call 0x14027cbf0
002A801A  88 44 24 40                     mov byte ptr [rsp + 0x40], al
002A801E  49 3B FF                        cmp rdi, r15
002A8021  0F 86 9F 00 00 00               jbe 0x1402a80c6
002A8027  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002A802C  48 85 C0                        test rax, rax
002A802F  0F 85 EA 04 00 00               jne 0x1402a851f
002A8035  F6 C3 04                        test bl, 4
002A8038  0F 85 F3 04 00 00               jne 0x1402a8531
002A803E  4D 85 ED                        test r13, r13
002A8041  0F 85 FD 04 00 00               jne 0x1402a8544
002A8047  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
002A804B  48 8B CE                        mov rcx, rsi
002A804E  E8 3D 56 FD FF                  call 0x14027d690
002A8053  33 FF                           xor edi, edi
002A8055  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
002A805D  48 85 C0                        test rax, rax
002A8060  0F 85 14 01 00 00               jne 0x1402a817a
002A8066  B8 01 00 00 00                  mov eax, 1
002A806B  84 D8                           test al, bl
002A806D  0F 85 E1 04 00 00               jne 0x1402a8554
002A8073  48 83 BC 24 D0 00 00 00 FF      cmp qword ptr [rsp + 0xd0], -1
002A807C  0F 85 E6 04 00 00               jne 0x1402a8568
002A8082  85 FF                           test edi, edi
002A8084  0F 84 F5 04 00 00               je 0x1402a857f
002A808A  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
002A808F  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
002A8097  48 3B D8                        cmp rbx, rax
002A809A  0F 85 3A 05 00 00               jne 0x1402a85da
002A80A0  8B C7                           mov eax, edi
002A80A2  48 8B 8C 24 20 09 00 00         mov rcx, qword ptr [rsp + 0x920]
002A80AA  48 33 CC                        xor rcx, rsp
002A80AD  E8 8E 45 40 00                  call 0x1406ac640
002A80B2  48 81 C4 30 09 00 00            add rsp, 0x930
002A80B9  41 5F                           pop r15
002A80BB  41 5E                           pop r14
002A80BD  41 5D                           pop r13
002A80BF  41 5C                           pop r12
002A80C1  5F                              pop rdi
002A80C2  5E                              pop rsi
002A80C3  5B                              pop rbx
002A80C4  C3                              ret
002A80C5  CC                              int3
002A80C6  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002A80CB  48 83 C0 08                     add rax, 8
002A80CF  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
002A80D7  4D 85 ED                        test r13, r13
002A80DA  0F 85 34 03 00 00               jne 0x1402a8414
002A80E0  33 D2                           xor edx, edx
002A80E2  48 8B CE                        mov rcx, rsi
002A80E5  E8 36 64 00 00                  call 0x1402ae520
002A80EA  85 C0                           test eax, eax
002A80EC  0F 85 48 03 00 00               jne 0x1402a843a
002A80F2  E8 E9 F2 FC FF                  call 0x1402773e0
002A80F7  85 C0                           test eax, eax
002A80F9  0F 85 3B 03 00 00               jne 0x1402a843a
002A80FF  48 8D 44 24 78                  lea rax, [rsp + 0x78]
002A8104  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002A8109  41 B9 01 00 00 00               mov r9d, 1
002A810F  44 8A 44 24 40                  mov r8b, byte ptr [rsp + 0x40]
002A8114  49 8B D7                        mov rdx, r15
002A8117  48 8B CF                        mov rcx, rdi
002A811A  E8 C1 AD 01 00                  call 0x1402c2ee0
002A811F  48 8B C8                        mov rcx, rax
002A8122  48 85 C0                        test rax, rax
002A8125  75 60                           jne 0x1402a8187
002A8127  49 8D 4F 08                     lea rcx, [r15 + 8]
002A812B  48 2B CF                        sub rcx, rdi
002A812E  48 C1 F9 03                     sar rcx, 3
002A8132  33 D2                           xor edx, edx
002A8134  48 8B C1                        mov rax, rcx
002A8137  49 F7 F6                        div r14
002A813A  48 8B F0                        mov rsi, rax
002A813D  83 CB 04                        or ebx, 4
002A8140  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
002A8148  E8 33 0D FA FF                  call 0x140248e80
002A814D  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
002A8152  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
002A8157  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
002A815C  41 B9 01 00 00 00               mov r9d, 1
002A8162  48 85 F6                        test rsi, rsi
002A8165  0F 85 E8 02 00 00               jne 0x1402a8453
002A816B  49 3B FF                        cmp rdi, r15
002A816E  76 40                           jbe 0x1402a81b0
002A8170  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
002A8175  E9 AD FE FF FF                  jmp 0x1402a8027
002A817A  48 8B C8                        mov rcx, rax
002A817D  E8 DE EC 06 00                  call 0x140316e60
002A8182  E9 DF FE FF FF                  jmp 0x1402a8066
002A8187  4C 8B E8                        mov r13, rax
002A818A  49 C1 ED 09                     shr r13, 9
002A818E  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002A8198  4C 23 E8                        and r13, rax
002A819B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002A81A5  48 8B C0                        mov rax, rax
002A81A8  4C 03 E8                        add r13, rax
002A81AB  E9 7B FF FF FF                  jmp 0x1402a812b
002A81B0  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
002A81B4  85 D2                           test edx, edx
002A81B6  0F 85 BD 02 00 00               jne 0x1402a8479
002A81BC  4D 8B C4                        mov r8, r12
002A81BF  33 D2                           xor edx, edx
002A81C1  49 8B C0                        mov rax, r8
002A81C4  49 F7 F6                        div r14
002A81C7  4C 8B C8                        mov r9, rax
002A81CA  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
002A81D2  49 3B FF                        cmp rdi, r15
002A81D5  0F 87 98 00 00 00               ja 0x1402a8273
002A81DB  48 8B CF                        mov rcx, rdi
002A81DE  E8 BD 3E FD FF                  call 0x14027c0a0
002A81E3  4C 8B E0                        mov r12, rax
002A81E6  83 E3 FD                        and ebx, 0xfffffffd
002A81E9  48 8B F7                        mov rsi, rdi
002A81EC  49 8B 53 18                     mov rdx, qword ptr [r11 + 0x18]
002A81F0  4C 0F A3 12                     bt qword ptr [rdx], r10
002A81F4  0F 92 C1                        setb cl
002A81F7  41 B8 01 00 00 00               mov r8d, 1
002A81FD  41 3A C8                        cmp cl, r8b
002A8200  0F 84 B5 02 00 00               je 0x1402a84bb
002A8206  45 33 F6                        xor r14d, r14d
002A8209  48 8B 06                        mov rax, qword ptr [rsi]
002A820C  A8 42                           test al, 0x42
002A820E  0F 95 C1                        setne cl
002A8211  41 84 C0                        test r8b, al
002A8214  0F 95 C0                        setne al
002A8217  84 C8                           test al, cl
002A8219  0F 85 B6 02 00 00               jne 0x1402a84d5
002A821F  48 83 C6 08                     add rsi, 8
002A8223  45 03 F0                        add r14d, r8d
002A8226  41 8B C6                        mov eax, r14d
002A8229  48 3B 84 24 A8 00 00 00         cmp rax, qword ptr [rsp + 0xa8]
002A8231  72 D6                           jb 0x1402a8209
002A8233  4C 8B B4 24 90 00 00 00         mov r14, qword ptr [rsp + 0x90]
002A823B  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
002A8243  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
002A8248  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
002A824D  F6 C3 02                        test bl, 2
002A8250  75 78                           jne 0x1402a82ca
002A8252  4D 03 D1                        add r10, r9
002A8255  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
002A825A  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
002A8262  4A 8D 3C E7                     lea rdi, [rdi + r12*8]
002A8266  48 F7 C7 FF 0F 00 00            test rdi, 0xfff
002A826D  0F 85 5F FF FF FF               jne 0x1402a81d2
002A8273  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
002A827B  E8 60 15 FA FF                  call 0x1402497e0
002A8280  83 E3 FB                        and ebx, 0xfffffffb
002A8283  48 8B CF                        mov rcx, rdi
002A8286  E8 15 3E FD FF                  call 0x14027c0a0
002A828B  48 8B F8                        mov rdi, rax
002A828E  48 C1 EF 09                     shr rdi, 9
002A8292  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002A829C  48 23 F8                        and rdi, rax
002A829F  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002A82A9  48 8B C0                        mov rax, rax
002A82AC  48 03 F8                        add rdi, rax
002A82AF  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
002A82B7  49 3B FF                        cmp rdi, r15
002A82BA  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
002A82BF  0F 86 12 FE FF FF               jbe 0x1402a80d7
002A82C5  E9 5D FD FF FF                  jmp 0x1402a8027
002A82CA  33 C0                           xor eax, eax
002A82CC  49 8B CE                        mov rcx, r14
002A82CF  48 C1 E1 0C                     shl rcx, 0xc
002A82D3  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
002A82DB  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
002A82E3  8D 70 01                        lea esi, [rax + 1]
002A82E6  49 3B C1                        cmp rax, r9
002A82E9  0F 83 63 FF FF FF               jae 0x1402a8252
002A82EF  4D 89 20                        mov qword ptr [r8], r12
002A82F2  49 83 C0 08                     add r8, 8
002A82F6  4C 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], r8
002A82FE  48 03 D6                        add rdx, rsi
002A8301  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
002A8309  48 3B 94 24 A0 00 00 00         cmp rdx, qword ptr [rsp + 0xa0]
002A8311  0F 84 59 FE FF FF               je 0x1402a8170
002A8317  48 03 C6                        add rax, rsi
002A831A  4C 03 E1                        add r12, rcx
002A831D  EB C7                           jmp 0x1402a82e6
002A831F  B8 F0 00 00 C0                  mov eax, 0xc00000f0
002A8324  E9 79 FD FF FF                  jmp 0x1402a80a2
002A8329  B9 41 00 00 00                  mov ecx, 0x41
002A832E  41 B8 4D 6D 47 63               mov r8d, 0x63476d4d
002A8334  E8 07 32 0B 00                  call 0x14035b540
002A8339  48 8B C8                        mov rcx, rax
002A833C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002A8341  48 85 C0                        test rax, rax
002A8344  0F 85 37 FB FF FF               jne 0x1402a7e81
002A834A  B8 9A 00 00 C0                  mov eax, 0xc000009a
002A834F  E9 4E FD FF FF                  jmp 0x1402a80a2
002A8354  48 21 44 24 30                  and qword ptr [rsp + 0x30], rax
002A8359  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
002A8361  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002A8366  C7 44 24 20 4D 6D 57 77         mov dword ptr [rsp + 0x20], 0x77576d4d
002A836E  44 8A CF                        mov r9b, dil
002A8371  4C 8B 05 20 E7 D1 00            mov r8, qword ptr [rip + 0xd1e720]
002A8378  BA 08 00 00 00                  mov edx, 8
002A837D  49 8B CE                        mov rcx, r14
002A8380  E8 8B 12 5C 00                  call 0x140869610
002A8385  8B F8                           mov edi, eax
002A8387  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
002A838B  85 C0                           test eax, eax
002A838D  0F 88 F7 FC FF FF               js 0x1402a808a
002A8393  E9 1F FB FF FF                  jmp 0x1402a7eb7
002A8398  BF F2 00 00 C0                  mov edi, 0xc00000f2
002A839D  E9 B3 FC FF FF                  jmp 0x1402a8055
002A83A2  4C 8D 84 24 F0 00 00 00         lea r8, [rsp + 0xf0]
002A83AA  33 D2                           xor edx, edx
002A83AC  E8 6F E4 F6 FF                  call 0x140216820
002A83B1  BB 01 00 00 00                  mov ebx, 1
002A83B6  E9 25 FB FF FF                  jmp 0x1402a7ee0
002A83BB  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
002A83BF  81 FF A0 00 00 C0               cmp edi, 0xc00000a0
002A83C5  0F 85 8A FC FF FF               jne 0x1402a8055
002A83CB  BF EF 00 00 C0                  mov edi, 0xc00000ef
002A83D0  E9 80 FC FF FF                  jmp 0x1402a8055
002A83D5  48 8B C8                        mov rcx, rax
002A83D8  48 C1 E1 0C                     shl rcx, 0xc
002A83DC  48 FF C9                        dec rcx
002A83DF  48 85 F1                        test rcx, rsi
002A83E2  0F 84 E2 2B 43 00               je 0x1406dafca
002A83E8  BF F1 00 00 C0                  mov edi, 0xc00000f1
002A83ED  E9 63 FC FF FF                  jmp 0x1402a8055
002A83F2  49 C1 EA 13                     shr r10, 0x13
002A83F6  41 83 E2 03                     and r10d, 3
002A83FA  48 8D 05 77 C1 D6 FF            lea rax, [rip - 0x293e89]
002A8401  41 BC 10 00 00 00               mov r12d, 0x10
002A8407  4E 39 24 D0                     cmp qword ptr [rax + r10*8], r12
002A840B  4C 0F 45 E1                     cmovne r12, rcx
002A840F  E9 B0 FB FF FF                  jmp 0x1402a7fc4
002A8414  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
002A8419  48 85 F6                        test rsi, rsi
002A841C  0F 84 BB 2B 43 00               je 0x1406dafdd
002A8422  48 8B CE                        mov rcx, rsi
002A8425  E8 96 9B 06 00                  call 0x140311fc0
002A842A  E8 41 B8 06 00                  call 0x140313c70
002A842F  48 83 64 24 50 00               and qword ptr [rsp + 0x50], 0
002A8435  E9 A3 2B 43 00                  jmp 0x1406dafdd
002A843A  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
002A843E  48 8B CE                        mov rcx, rsi
002A8441  E8 4A 52 FD FF                  call 0x14027d690
002A8446  48 8B CE                        mov rcx, rsi
002A8449  E8 A2 47 FD FF                  call 0x14027cbf0
002A844E  E9 AC FC FF FF                  jmp 0x1402a80ff
002A8453  49 8B 4B 18                     mov rcx, qword ptr [r11 + 0x18]
002A8457  4C 0F A3 11                     bt qword ptr [rcx], r10
002A845B  0F 92 C0                        setb al
002A845E  41 3A C1                        cmp al, r9b
002A8461  0F 85 E5 2B 43 00               jne 0x1406db04c
002A8467  45 84 C1                        test r9b, r8b
002A846A  0F 84 85 2B 43 00               je 0x1406daff5
002A8470  4C 0F B3 11                     btr qword ptr [rcx], r10
002A8474  E9 7C 2B 43 00                  jmp 0x1406daff5
002A8479  49 8B FD                        mov rdi, r13
002A847C  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
002A8484  48 C1 E9 09                     shr rcx, 9
002A8488  49 BF F8 FF FF FF 7F 00 00 00   movabs r15, 0x7ffffffff8
002A8492  49 23 CF                        and rcx, r15
002A8495  48 BE 00 00 00 00 80 F6 FF FF   movabs rsi, 0xfffff68000000000
002A849F  48 8B C6                        mov rax, rsi
002A84A2  48 03 C8                        add rcx, rax
002A84A5  41 B8 00 02 00 00               mov r8d, 0x200
002A84AB  41 3B D1                        cmp edx, r9d
002A84AE  0F 86 CF 2B 43 00               jbe 0x1406db083
002A84B4  FF CA                           dec edx
002A84B6  E9 A5 2B 43 00                  jmp 0x1406db060
002A84BB  83 CB 02                        or ebx, 2
002A84BE  44 84 44 24 60                  test byte ptr [rsp + 0x60], r8b
002A84C3  0F 84 84 FD FF FF               je 0x1402a824d
002A84C9  4C 0F B3 12                     btr qword ptr [rdx], r10
002A84CD  45 33 F6                        xor r14d, r14d
002A84D0  E9 E9 2B 43 00                  jmp 0x1406db0be
002A84D5  83 CB 02                        or ebx, 2
002A84D8  44 84 44 24 60                  test byte ptr [rsp + 0x60], r8b
002A84DD  0F 84 50 FD FF FF               je 0x1402a8233
002A84E3  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002A84E8  48 85 C0                        test rax, rax
002A84EB  0F 85 3C 2C 43 00               jne 0x1406db12d
002A84F1  E8 9A A7 F9 FF                  call 0x140242c90
002A84F6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002A84FB  C7 44 24 20 0A 00 00 00         mov dword ptr [rsp + 0x20], 0xa
002A8503  45 33 C9                        xor r9d, r9d
002A8506  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
002A850A  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
002A850F  48 8B C8                        mov rcx, rax
002A8512  E8 E9 C9 FE FF                  call 0x140294f00
002A8517  48 8B C1                        mov rax, rcx
002A851A  E9 0E 2C 43 00                  jmp 0x1406db12d
002A851F  48 8B C8                        mov rcx, rax
002A8522  E8 99 9A 06 00                  call 0x140311fc0
002A8527  E8 44 B7 06 00                  call 0x140313c70
002A852C  E9 04 FB FF FF                  jmp 0x1402a8035
002A8531  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
002A8536  48 83 C1 08                     add rcx, 8
002A853A  E8 A1 12 FA FF                  call 0x1402497e0
002A853F  E9 FA FA FF FF                  jmp 0x1402a803e
002A8544  49 8B D5                        mov rdx, r13
002A8547  48 8B CE                        mov rcx, rsi
002A854A  E8 71 E9 F6 FF                  call 0x140216ec0
002A854F  E9 F3 FA FF FF                  jmp 0x1402a8047
002A8554  33 D2                           xor edx, edx
002A8556  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
002A855E  E8 CD F7 F6 FF                  call 0x140217d30
002A8563  E9 0B FB FF FF                  jmp 0x1402a8073
002A8568  BA 4D 6D 57 77                  mov edx, 0x77576d4d
002A856D  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
002A8575  E8 66 F3 04 00                  call 0x1402f78e0
002A857A  E9 03 FB FF FF                  jmp 0x1402a8082
002A857F  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
002A8587  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
002A858C  48 85 C9                        test rcx, rcx
002A858F  74 23                           je 0x1402a85b4
002A8591  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
002A8599  4C 8D 04 F5 00 00 00 00         lea r8, [rsi*8]
002A85A1  48 8B D3                        mov rdx, rbx
002A85A4  E8 97 E2 41 00                  call 0x1406c6840
002A85A9  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
002A85B1  48 89 30                        mov qword ptr [rax], rsi
002A85B4  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002A85BC  C1 E0 0C                        shl eax, 0xc
002A85BF  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
002A85C7  89 01                           mov dword ptr [rcx], eax
002A85C9  E9 C1 FA FF FF                  jmp 0x1402a808f
002A85CE  8B F8                           mov edi, eax
002A85D0  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
002A85D5  E9 B5 FA FF FF                  jmp 0x1402a808f
002A85DA  33 D2                           xor edx, edx
002A85DC  48 8B CB                        mov rcx, rbx
002A85DF  E8 8C A2 8D 00                  call 0x140b82870
002A85E4  E9 B7 FA FF FF                  jmp 0x1402a80a0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtGetWriteWatch(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m848;
    unsigned __int64 v_stack_m858;
    unsigned __int64 v_stack_m868;
    unsigned __int64 v_stack_m878;
    unsigned __int64 v_stack_m880;
    unsigned __int64 v_stack_m888;
    unsigned __int64 v_stack_m890;
    unsigned __int64 v_stack_m898;
    unsigned __int64 v_stack_m8A0;
    unsigned __int64 v_stack_m8A8;
    unsigned __int64 v_stack_m8C0;
    unsigned __int64 v_stack_m8C8;
    unsigned __int64 v_stack_m8D0;
    unsigned __int64 v_stack_m8D8;
    unsigned __int64 v_stack_m8E0;
    unsigned __int64 v_stack_m8E8;
    unsigned int v_stack_m8F0;
    unsigned __int64 v_stack_m8F8;
    unsigned __int64 v_stack_m900;
    unsigned int v_stack_m908;
    unsigned __int64 v_stack_m910;
    unsigned __int64 v_stack_m918;
    unsigned int v_stack_m920;
    unsigned __int8 v_stack_m928;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (0x930ULL);
    result = (*(unsigned __int64 *)(v_rip + 11938374)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m908 = a2;
    v_stack_m898 = a1;
    v_stack_m880 = a7;
    v_stack_m888 = a6;
    v_stack_m890 = a5;
    v_stack_m878 = v_xmm0;
    v_stack_m868 = v_xmm0;
    v_stack_m858 = v_xmm0;
    if ((((unsigned int)((unsigned int)(a2))) & (0xFFFFFFFEULL)) != 0) goto loc_002A831F;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_002A7DB7;
    v_stack_m8C8 = *(unsigned __int64 *)(a6);
    goto loc_002A7E51;
loc_002A7DB7:
    if (a3 > (*(unsigned __int64 *)(a6))) goto loc_002A7E29;
    result = (v_rbx) - (a3);
    if (result < a4) goto loc_002A7E33;
    a1 = v_rbx;
    if (a6 < v_rbx) { a1 = a6; }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    v_stack_m8C8 = *(unsigned __int64 *)(a6);
    if (*(unsigned __int64 *)(a6) == 0) goto loc_002A7E3D;
    if ((*(unsigned __int64 *)(a6)) > (*(unsigned __int64 *)(a1))) goto loc_002A7E47;
    a2 = (*(unsigned __int64 *)(a6)) << (3);
    result = ProbeForWrite(a5, a2, 8, a5);
    if (a7 < v_rbx) { v_rbx = a7; }
    *(unsigned int *)(v_rbx) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)));
    goto loc_002A7E51;
loc_002A7E29:
    goto loc_002A80A2;
loc_002A7E33:
    goto loc_002A80A2;
loc_002A7E3D:
    goto loc_002A80A2;
loc_002A7E47:
    goto loc_002A80A2;
loc_002A7E51:
    goto loc_002A7E58;
loc_002A7E58:
    v_stack_m8F8 = v_stack_m848;
    if (v_stack_m8C8 > 256) goto loc_002A8329;
loc_002A7E81:
    v_stack_m8D8 = 1;
    v_r13 = 0;
    v_stack_m8D0 = v_stack_m848;
    result = 0;
    v_stack_m8A0 = 0;
    v_rbx = 0;
    if (a1 != -1) goto loc_002A8354;
    v_stack_m8E8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
loc_002A7EB7:
    v_r14 = (a3 - 1) + (a4);
    if (a3 > v_r14) goto loc_002A8398;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != v_stack_m8E8) goto loc_002A83A2;
loc_002A7EE0:
    result = (v_stack_m8E8) + (0x400ULL);
    v_stack_m910 = result;
    v_rdi = (a3) >> (9);
    v_rdi = (v_rdi) & (v_stack_m8C8 * 8);
    v_rdi = (v_rdi) + (v_stack_m8E8);
    v_r15 = (v_r14) >> (9);
    v_r15 = (v_r15) & (v_stack_m8C8 * 8);
    v_r15 = (v_r15) + (v_stack_m8E8);
    v_stack_m8A8 = v_r15;
    a2 = 0;
    result = MiObtainReferencedVadEx(a3, a2, v_stack_m920, a5);
    if (result == 0) goto loc_002A83BB;
    v_stack_m8A0 = result;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & ((unsigned int)((unsigned int)(0x600000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x600000ULL)))) goto loc_002A83CB;
    a1 = (*(unsigned __int8 *)(result + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 28)));
    a1 = (a1) << (12);
    a1 = (a1) | (0xFFFULL);
    if (v_r14 > a1) goto loc_002A83CB;
    result = MiGetVadMandatoryPageSize(result, a2, result, (unsigned int)(*(unsigned int *)(result + 48)));
    v_stack_m8D8 = result;
    if (result > 1) goto loc_002A83D5;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & ((unsigned int)((unsigned int)(0xA00000ULL))));
    if (((unsigned int)(a4)) == ((unsigned int)((unsigned int)(0xA00000ULL)))) goto loc_002A83F2;
loc_002A7FC4:
    v_stack_m8C0 = 1;
    result = MiLocateLockedVadEvent(result, 4, result, a4);
    v_stack_m900 = result;
    a2 = (*(unsigned __int8 *)(result + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(result + 24)));
    v_rsi = (a3) >> (12);
    v_rsi = (v_rsi) - (a2);
    result = MiGetVadMandatoryPageSize(result, a2, result, a4);
    a2 = 0;
    v_stack_m920 = v_rsi;
    result = MiLockWorkingSetShared(v_stack_m910, a2, result, a4);
    v_stack_m928 = (unsigned __int8)(result);
    if (v_rdi <= v_r15) goto loc_002A80C6;
loc_002A8027:
    if (v_stack_m918 != 0) goto loc_002A851F;
loc_002A8035:
    if (((0) & (4)) != 0) goto loc_002A8531;
loc_002A803E:
    if (0 != 0) goto loc_002A8544;
loc_002A8047:
    result = MiUnlockWorkingSetShared(v_stack_m910, v_stack_m928, result, a4);
    v_rdi = 0;
loc_002A8055:
    if (v_stack_m8A0 != 0) goto loc_002A817A;
loc_002A8066:
    if (((1) & (0)) != 0) goto loc_002A8554;
loc_002A8073:
    if (v_stack_m898 != -1) goto loc_002A8568;
loc_002A8082:
    if (0 == 0) goto loc_002A857F;
loc_002A808A:
loc_002A808F:
    if (v_stack_m8F8 != v_stack_m848) goto loc_002A85DA;
loc_002A80A0:
loc_002A80A2:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m928, result, a4);
    v_rsp = (v_rsp) + (0x930ULL);
    return result;
loc_002A80C6:
    result = (v_stack_p68) + (8);
    v_stack_pB8 = result;
loc_002A80D7:
    if (0 != 0) goto loc_002A8414;
    a2 = 0;
    result = MiWorkingSetIsContended(v_stack_m910, a2, result, a4);
    if ((unsigned int)(result) != 0) goto loc_002A843A;
    result = KeShouldYieldProcessor(v_stack_m910, a2, result, a4);
    if ((unsigned int)(result) != 0) goto loc_002A843A;
loc_002A80FF:
    v_stack_p20 = v_stack_p78;
    result = MiGetNextPageTable(0, v_r15, v_stack_p40, 1);
    if (result != 0) goto loc_002A8187;
loc_002A812B:
    a1 = (v_r15 + 8) - (0);
    a1 = (a1) >> (3);
    a2 = 0;
    v_rbx = (unsigned int)((v_stack_m8F8) | (4));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pB8, a2, v_stack_p40, 1);
    if (a1 != 0) goto loc_002A8453;
    if (0 <= v_r15) goto loc_002A81B0;
loc_002A8170:
    goto loc_002A8027;
loc_002A817A:
    result = MiUnlockAndDereferenceVad(result, a2, (unsigned int)(v_stack_p60), 1);
    goto loc_002A8066;
loc_002A8187:
    v_r13 = (result) >> (9);
    v_r13 = (v_r13) & (result);
    v_r13 = (v_r13) + (result);
    goto loc_002A812B;
loc_002A81B0:
    if ((unsigned int)((unsigned int)(v_stack_p78)) != 0) goto loc_002A8479;
    a2 = 0;
    v_stack_pB0 = 1;
loc_002A81D2:
    if (0 > v_r15) goto loc_002A8273;
    result = MiGetLeafVa(0, a2, 1, 1);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    a1 = (condition_is_below) ? 1 : 0;
    if (((unsigned __int8)(a1)) == 1) goto loc_002A84BB;
    v_r14 = 0;
loc_002A8209:
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(0))) & (66)) != 0) ? 1 : 0;
    result = (((1) & ((unsigned __int8)(*(unsigned __int64 *)(0)))) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_002A84D5;
    v_rsi = (0) + (8);
    v_r14 = (unsigned int)((v_r14) + (1));
    if (((unsigned int)((unsigned int)(v_r14))) < v_stack_pA8) goto loc_002A8209;
loc_002A8233:
loc_002A824D:
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_002A82CA;
loc_002A8252:
    v_r10 = (v_stack_p48) + (v_stack_pB0);
    v_stack_p48 = v_r10;
    if (((v_rdi + v_stack_pA8 * 8) & (0xFFFULL)) != 0) goto loc_002A81D2;
loc_002A8273:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_pB8, *(unsigned __int64 *)(v_stack_p68 + 24), 1, v_stack_pB0);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFBULL));
    result = MiGetLeafVa(v_rdi + v_stack_pA8 * 8, *(unsigned __int64 *)(v_stack_p68 + 24), 1, v_stack_pB0);
    v_rdi = (result) >> (9);
    v_rdi = (v_rdi) & (result);
    v_rdi = (v_rdi) + (result);
    if (v_rdi <= v_stack_pC0) goto loc_002A80D7;
    goto loc_002A8027;
loc_002A82CA:
    result = 0;
    a1 = (v_stack_p90) << (12);
loc_002A82E6:
    if (0 >= v_stack_pB0) goto loc_002A8252;
    *(unsigned __int64 *)(v_stack_p98) = v_stack_pA8;
    a3 = (v_stack_p98) + (8);
    v_stack_p98 = a3;
    a2 = (v_stack_p88) + (result + 1);
    v_stack_p88 = a2;
    if (a2 == v_stack_pA0) goto loc_002A8170;
    result = (result) + (result + 1);
    v_r12 = (v_stack_pA8) + (a1);
    goto loc_002A82E6;
loc_002A831F:
    goto loc_002A80A2;
loc_002A8329:
    result = MiAllocatePool(65, a2, (unsigned int)(0x63476D4DULL), v_stack_pB0);
    v_stack_p70 = result;
    if (result != 0) goto loc_002A7E81;
    goto loc_002A80A2;
loc_002A8354:
    v_stack_p28 = v_stack_p80;
    v_stack_p20 = 0x77576D4DULL;
    result = ObReferenceObjectByHandleWithTag(v_stack_p90, 8, *(unsigned __int64 *)(v_rip + 13756192), (unsigned __int8)(v_rdi));
    v_stack_p48 = (unsigned int)(result);
    if (sign_flag) goto loc_002A808A;
    goto loc_002A7EB7;
loc_002A8398:
    goto loc_002A8055;
loc_002A83A2:
    a2 = 0;
    result = KiStackAttachProcess(v_stack_p90, a2, v_stack_pF0, (unsigned __int8)(v_rdi));
    goto loc_002A7EE0;
loc_002A83BB:
    if (((unsigned int)((unsigned int)(v_stack_p48))) != 0xC00000A0ULL) goto loc_002A8055;
loc_002A83CB:
    goto loc_002A8055;
loc_002A83D5:
    a1 = (result) << (12);
    a1 = (a1) - 1;
    goto loc_002A8055;
loc_002A83F2:
    v_r10 = (v_r10) >> (19);
    v_r10 = (unsigned int)((v_r10) & (3));
    v_r12 = 16;
    if ((*(unsigned __int64 *)(v_rip - 2702985 + v_r10 * 8)) != 16) { v_r12 = a1; }
    goto loc_002A7FC4;
loc_002A8414:
    result = MiFlushTbList(v_stack_p50, a2, v_stack_pF0, (unsigned __int8)(v_rdi));
    result = MiReleaseProcessorFlushList(v_stack_p50, a2, v_stack_pF0, (unsigned __int8)(v_rdi));
loc_002A843A:
    result = MiUnlockWorkingSetShared(v_stack_p50, v_stack_p40, v_stack_pF0, (unsigned __int8)(v_rdi));
    result = MiLockWorkingSetShared(v_stack_p50, v_stack_p40, v_stack_pF0, (unsigned __int8)(v_rdi));
    goto loc_002A80FF;
loc_002A8453:
    result = (condition_is_below) ? 1 : 0;
loc_002A8479:
    a1 = (v_stack_pC0) >> (9);
    a1 = (a1) & (v_stack_pC0);
    a1 = (a1) + (v_stack_p50);
    a2 = (unsigned int)((v_stack_p40) - 1);
loc_002A84BB:
    v_rbx = (unsigned int)((1) | (2));
    if (((v_stack_p60) & (512)) == 0) goto loc_002A824D;
    v_r14 = 0;
loc_002A84D5:
    v_rbx = (unsigned int)((v_rbx) | (2));
    if (((v_stack_p60) & (512)) == 0) goto loc_002A8233;
    result = MiGetProcessorFlushList(a1, a2, 512, (unsigned __int8)(v_rdi));
    v_stack_p50 = result;
    v_stack_p20 = 10;
    a4 = 0;
    result = MiInitializeTbFlushList(result, v_stack_p58, (unsigned int)(*(unsigned int *)(result + 12)), a4);
loc_002A851F:
    result = MiFlushTbList(result, v_stack_p58, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    result = MiReleaseProcessorFlushList(result, v_stack_p58, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_002A8035;
loc_002A8531:
    a1 = (v_stack_p68) + (8);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(a1, v_stack_p58, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_002A803E;
loc_002A8544:
    result = MiUnlockPageTable(v_stack_p50, v_r13, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_002A8047;
loc_002A8554:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF0, a2, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_002A8073;
loc_002A8568:
    result = ObfDereferenceObjectWithTag(v_stack_p80, (unsigned int)(0x77576D4DULL), (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_002A8082;
loc_002A857F:
    v_rsi = v_stack_p50;
    if (v_stack_pD8 != 0) {
        v_rsi = v_stack_p88;
        a3 = v_rsi * 8;
        a2 = v_stack_p70;
        result = memcpy(v_stack_pD8, a2, a3, a4);
        result = v_stack_pE0;
        *(unsigned __int64 *)(result) = v_rsi;
    }
    result = (unsigned int)((v_stack_p90) << (12));
    *(unsigned int *)(v_stack_pE8) = (unsigned int)(result);
    goto loc_002A808F;
loc_002A85DA:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p70, a2, a3, a4);
    goto loc_002A80A0;
}
```

## 5. (Beta) C Style

```c
int64_t NtGetWriteWatch(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6, int64_t Arg7)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m848;
    uint64_t v_stack_m858;
    uint64_t v_stack_m868;
    uint64_t v_stack_m878;
    uint64_t v_stack_m880;
    uint64_t v_stack_m888;
    uint64_t v_stack_m890;
    uint64_t v_stack_m898;
    uint64_t v_stack_m8A0;
    uint64_t v_stack_m8A8;
    uint64_t v_stack_m8C0;
    uint64_t v_stack_m8C8;
    uint64_t v_stack_m8D0;
    uint64_t v_stack_m8D8;
    uint64_t v_stack_m8E0;
    uint64_t v_stack_m8E8;
    uint32_t v_stack_m8F0;
    uint64_t v_stack_m8F8;
    uint64_t v_stack_m900;
    uint32_t v_stack_m908;
    uint64_t v_stack_m910;
    uint64_t v_stack_m918;
    uint32_t v_stack_m920;
    uint8_t v_stack_m928;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (0x930ULL);
    result = (*(uint64_t *)(v_rip + 0xB62A46)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m908 = Arg2;
    v_stack_m898 = Arg1;
    v_stack_m880 = Arg7;
    v_stack_m888 = Arg6;
    v_stack_m890 = Arg5;
    v_stack_m878 = v_xmm0;
    v_stack_m868 = v_xmm0;
    v_stack_m858 = v_xmm0;
    if ((((uint32_t)((uint32_t)(Arg2))) & (0xFFFFFFFEULL)) != 0) goto loc_002A831F;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_002A7DB7;
    v_stack_m8C8 = *(uint64_t *)(arg6);
    goto loc_002A7E51;
loc_002A7DB7:
    if (Arg3 > (*(uint64_t *)(arg6))) goto loc_002A7E29;
    result = (local_rbx) - (Arg3);
    if (result < Arg4) goto loc_002A7E33;
    Arg1 = local_rbx;
    if (Arg6 < local_rbx) { Arg1 = Arg6; }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    v_stack_m8C8 = *(uint64_t *)(arg6);
    if (*(uint64_t *)(arg6) == 0) goto loc_002A7E3D;
    if ((*(uint64_t *)(arg6)) > (*(uint64_t *)(Arg1))) goto loc_002A7E47;
    Arg2 = (*(uint64_t *)(arg6)) << (3);
    result = ProbeForWrite(Arg5, Arg2, 8, Arg5);
    if (Arg7 < local_rbx) { local_rbx = Arg7; }
    *(uint32_t *)(local_rbx) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)));
    goto loc_002A7E51;
loc_002A7E29:
    goto loc_002A80A2;
loc_002A7E33:
    goto loc_002A80A2;
loc_002A7E3D:
    goto loc_002A80A2;
loc_002A7E47:
    goto loc_002A80A2;
loc_002A7E51:
    goto loc_002A7E58;
loc_002A7E58:
    v_stack_m8F8 = v_stack_m848;
    if (v_stack_m8C8 > 256) goto loc_002A8329;
loc_002A7E81:
    v_stack_m8D8 = 1;
    local_r13 = 0;
    v_stack_m8D0 = v_stack_m848;
    result = 0;
    v_stack_m8A0 = 0;
    local_rbx = 0;
    if (Arg1 != -1) goto loc_002A8354;
    v_stack_m8E8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
loc_002A7EB7:
    local_r14 = (Arg3 - 1) + (Arg4);
    if (Arg3 > local_r14) goto loc_002A8398;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != v_stack_m8E8) goto loc_002A83A2;
loc_002A7EE0:
    result = (v_stack_m8E8) + (0x400ULL);
    v_stack_m910 = result;
    local_rdi = (Arg3) >> (9);
    local_rdi = (local_rdi) & (v_stack_m8C8 * 8);
    local_rdi = (local_rdi) + (v_stack_m8E8);
    local_r15 = (local_r14) >> (9);
    local_r15 = (local_r15) & (v_stack_m8C8 * 8);
    local_r15 = (local_r15) + (v_stack_m8E8);
    v_stack_m8A8 = local_r15;
    Arg2 = 0;
    result = MiObtainReferencedVadEx(Arg3, Arg2, v_stack_m920, Arg5);
    if (result == 0) goto loc_002A83BB;
    v_stack_m8A0 = result;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & ((uint32_t)((uint32_t)(0x600000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x600000ULL)))) goto loc_002A83CB;
    Arg1 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    Arg1 = (Arg1) << (12);
    Arg1 = (Arg1) | (0xFFFULL);
    if (local_r14 > Arg1) goto loc_002A83CB;
    result = MiGetVadMandatoryPageSize(result, Arg2, result, (uint32_t)(*(uint32_t *)(result + 0x30)));
    v_stack_m8D8 = result;
    if (result > 1) goto loc_002A83D5;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & ((uint32_t)((uint32_t)(0xA00000ULL))));
    if (((uint32_t)(Arg4)) == ((uint32_t)((uint32_t)(0xA00000ULL)))) goto loc_002A83F2;
loc_002A7FC4:
    v_stack_m8C0 = 1;
    result = MiLocateLockedVadEvent(result, 4, result, Arg4);
    v_stack_m900 = result;
    Arg2 = (*(uint8_t *)(result + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    local_rsi = (Arg3) >> (12);
    local_rsi = (local_rsi) - (Arg2);
    result = MiGetVadMandatoryPageSize(result, Arg2, result, Arg4);
    Arg2 = 0;
    v_stack_m920 = local_rsi;
    result = MiLockWorkingSetShared(v_stack_m910, Arg2, result, Arg4);
    v_stack_m928 = (uint8_t)(result);
    if (local_rdi <= local_r15) goto loc_002A80C6;
loc_002A8027:
    if (v_stack_m918 != 0) goto loc_002A851F;
loc_002A8035:
    if (((0) & (4)) != 0) goto loc_002A8531;
loc_002A803E:
    if (0 != 0) goto loc_002A8544;
loc_002A8047:
    result = MiUnlockWorkingSetShared(v_stack_m910, v_stack_m928, result, Arg4);
    local_rdi = 0;
loc_002A8055:
    if (v_stack_m8A0 != 0) goto loc_002A817A;
loc_002A8066:
    if (((1) & (0)) != 0) goto loc_002A8554;
loc_002A8073:
    if (v_stack_m898 != -1) goto loc_002A8568;
loc_002A8082:
    if (0 == 0) goto loc_002A857F;
loc_002A808A:
loc_002A808F:
    if (v_stack_m8F8 != v_stack_m848) goto loc_002A85DA;
loc_002A80A0:
loc_002A80A2:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m928, result, Arg4);
    local_rsp = (local_rsp) + (0x930ULL);
    return result;
loc_002A80C6:
    result = (v_stack_p68) + (8);
    v_stack_pB8 = result;
loc_002A80D7:
    if (0 != 0) goto loc_002A8414;
    Arg2 = 0;
    result = MiWorkingSetIsContended(v_stack_m910, Arg2, result, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002A843A;
    result = KeShouldYieldProcessor(v_stack_m910, Arg2, result, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002A843A;
loc_002A80FF:
    v_stack_p20 = v_stack_p78;
    result = MiGetNextPageTable(0, local_r15, v_stack_p40, 1);
    if (result != 0) goto loc_002A8187;
loc_002A812B:
    Arg1 = (local_r15 + 8) - (0);
    Arg1 = (Arg1) >> (3);
    Arg2 = 0;
    local_rbx = (uint32_t)((v_stack_m8F8) | (4));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pB8, Arg2, v_stack_p40, 1);
    if (Arg1 != 0) goto loc_002A8453;
    if (0 <= local_r15) goto loc_002A81B0;
loc_002A8170:
    goto loc_002A8027;
loc_002A817A:
    result = MiUnlockAndDereferenceVad(result, Arg2, (uint32_t)(v_stack_p60), 1);
    goto loc_002A8066;
loc_002A8187:
    local_r13 = (result) >> (9);
    local_r13 = (local_r13) & (result);
    local_r13 = (local_r13) + (result);
    goto loc_002A812B;
loc_002A81B0:
    if ((uint32_t)((uint32_t)(v_stack_p78)) != 0) goto loc_002A8479;
    Arg2 = 0;
    v_stack_pB0 = 1;
loc_002A81D2:
    if (0 > local_r15) goto loc_002A8273;
    result = MiGetLeafVa(0, Arg2, 1, 1);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    Arg1 = (condition_is_below) ? 1 : 0;
    if (((uint8_t)(Arg1)) == 1) goto loc_002A84BB;
    local_r14 = 0;
loc_002A8209:
    Arg1 = ((((uint8_t)(*(uint64_t *)(0))) & (66)) != 0) ? 1 : 0;
    result = (((1) & ((uint8_t)(*(uint64_t *)(0)))) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_002A84D5;
    local_rsi = (0) + (8);
    local_r14 = (uint32_t)((local_r14) + (1));
    if (((uint32_t)((uint32_t)(local_r14))) < v_stack_pA8) goto loc_002A8209;
loc_002A8233:
loc_002A824D:
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_002A82CA;
loc_002A8252:
    local_r10 = (v_stack_p48) + (v_stack_pB0);
    v_stack_p48 = local_r10;
    if (((local_rdi + v_stack_pA8 * 8) & (0xFFFULL)) != 0) goto loc_002A81D2;
loc_002A8273:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_pB8, *(uint64_t *)(v_stack_p68 + 0x18), 1, v_stack_pB0);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFBULL));
    result = MiGetLeafVa(local_rdi + v_stack_pA8 * 8, *(uint64_t *)(v_stack_p68 + 0x18), 1, v_stack_pB0);
    local_rdi = (result) >> (9);
    local_rdi = (local_rdi) & (result);
    local_rdi = (local_rdi) + (result);
    if (local_rdi <= v_stack_pC0) goto loc_002A80D7;
    goto loc_002A8027;
loc_002A82CA:
    result = 0;
    Arg1 = (v_stack_p90) << (12);
loc_002A82E6:
    if (0 >= v_stack_pB0) goto loc_002A8252;
    *(uint64_t *)(v_stack_p98) = v_stack_pA8;
    Arg3 = (v_stack_p98) + (8);
    v_stack_p98 = Arg3;
    Arg2 = (v_stack_p88) + (result + 1);
    v_stack_p88 = Arg2;
    if (Arg2 == v_stack_pA0) goto loc_002A8170;
    result = (result) + (result + 1);
    local_r12 = (v_stack_pA8) + (Arg1);
    goto loc_002A82E6;
loc_002A831F:
    goto loc_002A80A2;
loc_002A8329:
    result = MiAllocatePool(65, Arg2, (uint32_t)(0x63476D4DULL), v_stack_pB0);
    v_stack_p70 = result;
    if (result != 0) goto loc_002A7E81;
    goto loc_002A80A2;
loc_002A8354:
    v_stack_p28 = v_stack_p80;
    v_stack_p20 = 0x77576D4DULL;
    result = ObReferenceObjectByHandleWithTag(v_stack_p90, 8, *(uint64_t *)(v_rip + 0xD1E720), (uint8_t)(local_rdi));
    v_stack_p48 = (uint32_t)(result);
    if (sign_flag) goto loc_002A808A;
    goto loc_002A7EB7;
loc_002A8398:
    goto loc_002A8055;
loc_002A83A2:
    Arg2 = 0;
    result = KiStackAttachProcess(v_stack_p90, Arg2, v_stack_pF0, (uint8_t)(local_rdi));
    goto loc_002A7EE0;
loc_002A83BB:
    if (((uint32_t)((uint32_t)(v_stack_p48))) != 0xC00000A0ULL) goto loc_002A8055;
loc_002A83CB:
    goto loc_002A8055;
loc_002A83D5:
    Arg1 = (result) << (12);
    Arg1 = (Arg1) - 1;
    goto loc_002A8055;
loc_002A83F2:
    local_r10 = (local_r10) >> (19);
    local_r10 = (uint32_t)((local_r10) & (3));
    local_r12 = 16;
    if ((*(uint64_t *)(v_rip - 0x293E89 + local_r10 * 8)) != 16) { local_r12 = Arg1; }
    goto loc_002A7FC4;
loc_002A8414:
    result = MiFlushTbList(v_stack_p50, Arg2, v_stack_pF0, (uint8_t)(local_rdi));
    result = MiReleaseProcessorFlushList(v_stack_p50, Arg2, v_stack_pF0, (uint8_t)(local_rdi));
loc_002A843A:
    result = MiUnlockWorkingSetShared(v_stack_p50, v_stack_p40, v_stack_pF0, (uint8_t)(local_rdi));
    result = MiLockWorkingSetShared(v_stack_p50, v_stack_p40, v_stack_pF0, (uint8_t)(local_rdi));
    goto loc_002A80FF;
loc_002A8453:
    result = (condition_is_below) ? 1 : 0;
loc_002A8479:
    Arg1 = (v_stack_pC0) >> (9);
    Arg1 = (Arg1) & (v_stack_pC0);
    Arg1 = (Arg1) + (v_stack_p50);
    Arg2 = (uint32_t)((v_stack_p40) - 1);
loc_002A84BB:
    local_rbx = (uint32_t)((1) | (2));
    if (((v_stack_p60) & (512)) == 0) goto loc_002A824D;
    local_r14 = 0;
loc_002A84D5:
    local_rbx = (uint32_t)((local_rbx) | (2));
    if (((v_stack_p60) & (512)) == 0) goto loc_002A8233;
    result = MiGetProcessorFlushList(Arg1, Arg2, 512, (uint8_t)(local_rdi));
    v_stack_p50 = result;
    v_stack_p20 = 10;
    Arg4 = 0;
    result = MiInitializeTbFlushList(result, v_stack_p58, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
loc_002A851F:
    result = MiFlushTbList(result, v_stack_p58, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    result = MiReleaseProcessorFlushList(result, v_stack_p58, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    goto loc_002A8035;
loc_002A8531:
    Arg1 = (v_stack_p68) + (8);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(Arg1, v_stack_p58, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    goto loc_002A803E;
loc_002A8544:
    result = MiUnlockPageTable(v_stack_p50, local_r13, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    goto loc_002A8047;
loc_002A8554:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF0, Arg2, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    goto loc_002A8073;
loc_002A8568:
    result = ObfDereferenceObjectWithTag(v_stack_p80, (uint32_t)(0x77576D4DULL), (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    goto loc_002A8082;
loc_002A857F:
    local_rsi = v_stack_p50;
    if (v_stack_pD8 != 0) {
        local_rsi = v_stack_p88;
        Arg3 = local_rsi * 8;
        Arg2 = v_stack_p70;
        result = memcpy(v_stack_pD8, Arg2, Arg3, Arg4);
        result = v_stack_pE0;
        *(uint64_t *)(result) = local_rsi;
    }
    result = (uint32_t)((v_stack_p90) << (12));
    *(uint32_t *)(v_stack_pE8) = (uint32_t)(result);
    goto loc_002A808F;
loc_002A85DA:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p70, Arg2, Arg3, Arg4);
    goto loc_002A80A0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A7CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
