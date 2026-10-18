# NtManageHotPatch

- RVA: `0x00AF8660`–`0x00AF8DE5` (길이 `1,925` bytes)
- VA: `0x0000000140AF8660`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D86B4`
- 디코드: `458`개 명령, `1,925/1,925` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00AF86C4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF86E4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00AF8763` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF8773` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x00AF877B` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (function, `0x0048FDC0`)
- `0x00AF88AB` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00AF88BE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF88F2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF8980` → [MiQueryProcessActivePatches](../AC/MiQueryProcessActivePatches_function_00AC6164.md) (function, `0x00AC6164`)
- `0x00AF89C5` → [RtlValidSid](../92/RtlValidSid_function_00929710.md) (function, `0x00929710`)
- `0x00AF89F2` → [MiQueryLoadedPatches](../AB/MiQueryLoadedPatches_function_00ABE538.md) (function, `0x00ABE538`)
- `0x00AF8A76` → [RtlDuplicateUnicodeString](../93/RtlDuplicateUnicodeString_function_009321F0.md) (function, `0x009321F0`)
- `0x00AF8AB4` → [RtlDuplicateUnicodeString](../93/RtlDuplicateUnicodeString_function_009321F0.md) (function, `0x009321F0`)
- `0x00AF8AD4` → [RtlValidSid](../92/RtlValidSid_function_00929710.md) (function, `0x00929710`)
- `0x00AF8AF9` → [MiLoadHotPatchForUserSid](../AB/MiLoadHotPatchForUserSid_function_00AB4F08.md) (function, `0x00AB4F08`)
- `0x00AF8B1D` → [MiLoadHotPatch](../AB/MiLoadHotPatch_function_00AB521C.md) (function, `0x00AB521C`)
- `0x00AF8B3D` → [MiLogHotPatchManagement](../80/MiLogHotPatchManagement_function_008046B8.md) (function, `0x008046B8`)
- `0x00AF8B5C` → [MiApplyImageHotPatchRequest](../80/MiApplyImageHotPatchRequest_function_008025AC.md) (function, `0x008025AC`)
- `0x00AF8B77` → [MiLogHotPatchManagement](../80/MiLogHotPatchManagement_function_008046B8.md) (function, `0x008046B8`)
- `0x00AF8C08` → [MiFindHotPatchRecord](../A6/MiFindHotPatchRecord_function_00A6E618.md) (function, `0x00A6E618`)
- `0x00AF8C2A` → [MiCreatePatchSectionRequest](../80/MiCreatePatchSectionRequest_function_008031E0.md) (function, `0x008031E0`)
- `0x00AF8CC4` → [MiQuerySingleLoadedPatch](../A4/MiQuerySingleLoadedPatch_function_00A41EB0.md) (function, `0x00A41EB0`)
- `0x00AF8CFF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF8D2F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF8D7A` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00AF8D8B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF8D9C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF8DAD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF8DBF` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AF8DD8` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AF8DDE` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AF8673` → RVA `0x00E0A740` (`.data`; read)
- `0x00AF870C` → RVA `0x00E375B4` (`.data`; read)
- `0x00AF872E` → RVA `0x00E375A8` (`.data`; read)
- `0x00AF875C` → RVA `0x00FD9B20` (`PAGEDATA`; read)
- `0x00AF8C01` → RVA `0x00E37578` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00AF86C4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF86E4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00AF8773` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGE` → `.text`)
  - `0x00AF877B` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (`PAGE` → `.text`)
  - `0x00AF88BE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF88F2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF8CFF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF8D2F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF8D8B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF8D9C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF8DAD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF8DBF` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF8660  40 53                           push rbx
00AF8662  56                              push rsi
00AF8663  57                              push rdi
00AF8664  41 54                           push r12
00AF8666  41 55                           push r13
00AF8668  41 56                           push r14
00AF866A  41 57                           push r15
00AF866C  48 81 EC 20 01 00 00            sub rsp, 0x120
00AF8673  48 8B 05 C6 20 31 00            mov rax, qword ptr [rip + 0x3120c6]
00AF867A  48 33 C4                        xor rax, rsp
00AF867D  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00AF8685  4D 8B F9                        mov r15, r9
00AF8688  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
00AF868D  45 8B E0                        mov r12d, r8d
00AF8690  4C 8B EA                        mov r13, rdx
00AF8693  8B F1                           mov esi, ecx
00AF8695  4C 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r9
00AF869D  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
00AF86A2  0F 57 C0                        xorps xmm0, xmm0
00AF86A5  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
00AF86AD  33 C0                           xor eax, eax
00AF86AF  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00AF86B6  33 D2                           xor edx, edx
00AF86B8  44 8D 40 64                     lea r8d, [rax + 0x64]
00AF86BC  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00AF86C4  E8 77 E5 BC FF                  call 0x1406c6c40
00AF86C9  33 FF                           xor edi, edi
00AF86CB  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00AF86D0  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00AF86D5  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00AF86DA  33 D2                           xor edx, edx
00AF86DC  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00AF86E4  E8 97 20 93 FF                  call 0x14042a780
00AF86E9  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00AF86ED  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF86F6  8A 98 32 02 00 00               mov bl, byte ptr [rax + 0x232]
00AF86FC  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
00AF8700  88 5C 24 48                     mov byte ptr [rsp + 0x48], bl
00AF8704  C7 44 24 44 01 00 00 C0         mov dword ptr [rsp + 0x44], 0xc0000001
00AF870C  8B 05 A2 EE 33 00               mov eax, dword ptr [rip + 0x33eea2]
00AF8712  A8 01                           test al, 1
00AF8714  75 18                           jne 0x140af872e
00AF8716  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00AF871B  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00AF871F  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
00AF8729  E9 10 06 00 00                  jmp 0x140af8d3e
00AF872E  8A 05 74 EE 33 00               mov al, byte ptr [rip + 0x33ee74]
00AF8734  84 C0                           test al, al
00AF8736  75 07                           jne 0x140af873f
00AF8738  BB A3 00 00 C0                  mov ebx, 0xc00000a3
00AF873D  EB DC                           jmp 0x140af871b
00AF873F  8B CE                           mov ecx, esi
00AF8741  83 E9 07                        sub ecx, 7
00AF8744  74 4A                           je 0x140af8790
00AF8746  83 E9 01                        sub ecx, 1
00AF8749  74 45                           je 0x140af8790
00AF874B  83 E9 01                        sub ecx, 1
00AF874E  74 40                           je 0x140af8790
00AF8750  83 E9 01                        sub ecx, 1
00AF8753  74 3B                           je 0x140af8790
00AF8755  83 F9 01                        cmp ecx, 1
00AF8758  74 36                           je 0x140af8790
00AF875A  8A D3                           mov dl, bl
00AF875C  48 8B 0D BD 13 4E 00            mov rcx, qword ptr [rip + 0x4e13bd]
00AF8763  E8 B8 96 D7 FF                  call 0x140871e20
00AF8768  84 C0                           test al, al
00AF876A  75 07                           jne 0x140af8773
00AF876C  BB 61 00 00 C0                  mov ebx, 0xc0000061
00AF8771  EB A8                           jmp 0x140af871b
00AF8773  E8 98 CF 72 FF                  call 0x140225710
00AF8778  48 8B D8                        mov rbx, rax
00AF877B  E8 40 76 99 FF                  call 0x14048fdc0
00AF8780  48 3B D8                        cmp rbx, rax
00AF8783  74 07                           je 0x140af878c
00AF8785  BB 22 00 00 C0                  mov ebx, 0xc0000022
00AF878A  EB 8F                           jmp 0x140af871b
00AF878C  8A 5C 24 40                     mov bl, byte ptr [rsp + 0x40]
00AF8790  8B D7                           mov edx, edi
00AF8792  89 54 24 5C                     mov dword ptr [rsp + 0x5c], edx
00AF8796  83 FE 06                        cmp esi, 6
00AF8799  7F 41                           jg 0x140af87dc
00AF879B  74 37                           je 0x140af87d4
00AF879D  8B CE                           mov ecx, esi
00AF879F  85 F6                           test esi, esi
00AF87A1  74 29                           je 0x140af87cc
00AF87A3  83 E9 01                        sub ecx, 1
00AF87A6  0F 84 6A FF FF FF               je 0x140af8716
00AF87AC  83 E9 01                        sub ecx, 1
00AF87AF  74 13                           je 0x140af87c4
00AF87B1  83 E9 01                        sub ecx, 1
00AF87B4  74 16                           je 0x140af87cc
00AF87B6  83 E9 01                        sub ecx, 1
00AF87B9  0F 84 57 FF FF FF               je 0x140af8716
00AF87BF  83 F9 01                        cmp ecx, 1
00AF87C2  75 33                           jne 0x140af87f7
00AF87C4  41 BF 60 00 00 00               mov r15d, 0x60
00AF87CA  EB 69                           jmp 0x140af8835
00AF87CC  41 BF 68 00 00 00               mov r15d, 0x68
00AF87D2  EB 61                           jmp 0x140af8835
00AF87D4  41 BF 28 00 00 00               mov r15d, 0x28
00AF87DA  EB 59                           jmp 0x140af8835
00AF87DC  8B CE                           mov ecx, esi
00AF87DE  83 E9 07                        sub ecx, 7
00AF87E1  74 45                           je 0x140af8828
00AF87E3  83 E9 01                        sub ecx, 1
00AF87E6  74 38                           je 0x140af8820
00AF87E8  83 E9 01                        sub ecx, 1
00AF87EB  74 20                           je 0x140af880d
00AF87ED  83 E9 01                        sub ecx, 1
00AF87F0  74 E2                           je 0x140af87d4
00AF87F2  83 F9 01                        cmp ecx, 1
00AF87F5  74 0A                           je 0x140af8801
00AF87F7  BB 03 00 00 C0                  mov ebx, 0xc0000003
00AF87FC  E9 1A FF FF FF                  jmp 0x140af871b
00AF8801  41 BF 14 00 00 00               mov r15d, 0x14
00AF8807  45 8D 47 F0                     lea r8d, [r15 - 0x10]
00AF880B  EB 2E                           jmp 0x140af883b
00AF880D  BA 01 00 00 00                  mov edx, 1
00AF8812  44 8D 7A 07                     lea r15d, [rdx + 7]
00AF8816  44 8D 42 03                     lea r8d, [rdx + 3]
00AF881A  89 54 24 5C                     mov dword ptr [rsp + 0x5c], edx
00AF881E  EB 1B                           jmp 0x140af883b
00AF8820  41 BF 30 00 00 00               mov r15d, 0x30
00AF8826  EB 0D                           jmp 0x140af8835
00AF8828  BA 01 00 00 00                  mov edx, 1
00AF882D  44 8D 7A 1F                     lea r15d, [rdx + 0x1f]
00AF8831  89 54 24 5C                     mov dword ptr [rsp + 0x5c], edx
00AF8835  41 B8 08 00 00 00               mov r8d, 8
00AF883B  45 3B E7                        cmp r12d, r15d
00AF883E  73 18                           jae 0x140af8858
00AF8840  BB 04 00 00 C0                  mov ebx, 0xc0000004
00AF8845  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00AF8849  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
00AF8853  E9 E1 04 00 00                  jmp 0x140af8d39
00AF8858  84 DB                           test bl, bl
00AF885A  0F 84 84 00 00 00               je 0x140af88e4
00AF8860  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
00AF886A  49 8B CE                        mov rcx, r14
00AF886D  4C 39 74 24 50                  cmp qword ptr [rsp + 0x50], r14
00AF8872  48 0F 42 4C 24 50               cmovb rcx, qword ptr [rsp + 0x50]
00AF8878  8B 01                           mov eax, dword ptr [rcx]
00AF887A  89 01                           mov dword ptr [rcx], eax
00AF887C  85 D2                           test edx, edx
00AF887E  74 25                           je 0x140af88a5
00AF8880  45 85 E4                        test r12d, r12d
00AF8883  74 2B                           je 0x140af88b0
00AF8885  41 8D 48 FF                     lea ecx, [r8 - 1]
00AF8889  49 85 CD                        test r13, rcx
00AF888C  0F 85 46 05 00 00               jne 0x140af8dd8
00AF8892  4B 8D 0C 2C                     lea rcx, [r12 + r13]
00AF8896  49 3B CE                        cmp rcx, r14
00AF8899  77 05                           ja 0x140af88a0
00AF889B  49 3B CD                        cmp rcx, r13
00AF889E  73 10                           jae 0x140af88b0
00AF88A0  41 8A 06                        mov al, byte ptr [r14]
00AF88A3  EB 0B                           jmp 0x140af88b0
00AF88A5  49 8B D4                        mov rdx, r12
00AF88A8  49 8B CD                        mov rcx, r13
00AF88AB  E8 10 09 DF FF                  call 0x1408e91c0
00AF88B0  45 8B C7                        mov r8d, r15d
00AF88B3  49 8B D5                        mov rdx, r13
00AF88B6  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00AF88BE  E8 7D DF BC FF                  call 0x1406c6840
00AF88C3  EB 3C                           jmp 0x140af8901
00AF88C5  8B D8                           mov ebx, eax
00AF88C7  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF88CB  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
00AF88D5  40 8A 74 24 48                  mov sil, byte ptr [rsp + 0x48]
00AF88DA  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00AF88DF  E9 5F 04 00 00                  jmp 0x140af8d43
00AF88E4  45 8B C7                        mov r8d, r15d
00AF88E7  49 8B D5                        mov rdx, r13
00AF88EA  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00AF88F2  E8 49 DF BC FF                  call 0x1406c6840
00AF88F7  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
00AF8901  83 FE 07                        cmp esi, 7
00AF8904  0F 8F 7A 02 00 00               jg 0x140af8b84
00AF890A  0F 84 44 02 00 00               je 0x140af8b54
00AF8910  8B CE                           mov ecx, esi
00AF8912  85 F6                           test esi, esi
00AF8914  0F 84 FC 00 00 00               je 0x140af8a16
00AF891A  83 E9 02                        sub ecx, 2
00AF891D  0F 84 88 00 00 00               je 0x140af89ab
00AF8923  83 E9 01                        sub ecx, 1
00AF8926  0F 84 EA 00 00 00               je 0x140af8a16
00AF892C  83 E9 02                        sub ecx, 2
00AF892F  74 7A                           je 0x140af89ab
00AF8931  83 F9 01                        cmp ecx, 1
00AF8934  0F 85 6A 02 00 00               jne 0x140af8ba4
00AF893A  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00AF8941  83 F8 03                        cmp eax, 3
00AF8944  74 18                           je 0x140af895e
00AF8946  83 F8 02                        cmp eax, 2
00AF8949  73 0E                           jae 0x140af8959
00AF894B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AF8950  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00AF8954  E9 E0 03 00 00                  jmp 0x140af8d39
00AF8959  83 F8 03                        cmp eax, 3
00AF895C  77 ED                           ja 0x140af894b
00AF895E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AF8962  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00AF8966  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00AF896B  4D 8B CD                        mov r9, r13
00AF896E  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00AF8973  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00AF8978  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00AF8980  E8 DF D7 FC FF                  call 0x140ac6164
00AF8985  8B D8                           mov ebx, eax
00AF8987  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF898B  85 C0                           test eax, eax
00AF898D  0F 88 A6 03 00 00               js 0x140af8d39
00AF8993  44 39 64 24 58                  cmp dword ptr [rsp + 0x58], r12d
00AF8998  76 07                           jbe 0x140af89a1
00AF899A  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AF899F  EB AF                           jmp 0x140af8950
00AF89A1  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00AF89A6  E9 38 03 00 00                  jmp 0x140af8ce3
00AF89AB  83 BC 24 A0 00 00 00 02         cmp dword ptr [rsp + 0xa0], 2
00AF89B3  75 96                           jne 0x140af894b
00AF89B5  48 8B CF                        mov rcx, rdi
00AF89B8  83 FE 05                        cmp esi, 5
00AF89BB  75 23                           jne 0x140af89e0
00AF89BD  48 8D 8C 24 A4 00 00 00         lea rcx, [rsp + 0xa4]
00AF89C5  E8 46 0D E3 FF                  call 0x140929710
00AF89CA  84 C0                           test al, al
00AF89CC  75 0A                           jne 0x140af89d8
00AF89CE  BB 78 00 00 C0                  mov ebx, 0xc0000078
00AF89D3  E9 78 FF FF FF                  jmp 0x140af8950
00AF89D8  48 8D 8C 24 A4 00 00 00         lea rcx, [rsp + 0xa4]
00AF89E0  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00AF89E5  4D 8B CD                        mov r9, r13
00AF89E8  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00AF89ED  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00AF89F2  E8 41 5B FC FF                  call 0x140abe538
00AF89F7  8B D8                           mov ebx, eax
00AF89F9  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF89FD  85 C0                           test eax, eax
00AF89FF  0F 88 34 03 00 00               js 0x140af8d39
00AF8A05  44 39 64 24 58                  cmp dword ptr [rsp + 0x58], r12d
00AF8A0A  77 8E                           ja 0x140af899a
00AF8A0C  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00AF8A11  E9 CD 02 00 00                  jmp 0x140af8ce3
00AF8A16  83 BC 24 A0 00 00 00 02         cmp dword ptr [rsp + 0xa0], 2
00AF8A1E  0F 85 27 FF FF FF               jne 0x140af894b
00AF8A24  66 39 BC 24 A8 00 00 00         cmp word ptr [rsp + 0xa8], di
00AF8A2C  0F 84 19 FF FF FF               je 0x140af894b
00AF8A32  84 DB                           test bl, bl
00AF8A34  74 6C                           je 0x140af8aa2
00AF8A36  F6 84 24 B0 00 00 00 01         test byte ptr [rsp + 0xb0], 1
00AF8A3E  0F 85 9A 03 00 00               jne 0x140af8dde
00AF8A44  0F B7 94 24 A8 00 00 00         movzx edx, word ptr [rsp + 0xa8]
00AF8A4C  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00AF8A54  48 03 D1                        add rdx, rcx
00AF8A57  49 3B D6                        cmp rdx, r14
00AF8A5A  77 05                           ja 0x140af8a61
00AF8A5C  48 3B D1                        cmp rdx, rcx
00AF8A5F  73 03                           jae 0x140af8a64
00AF8A61  41 8A 06                        mov al, byte ptr [r14]
00AF8A64  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00AF8A6C  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
00AF8A74  33 C9                           xor ecx, ecx
00AF8A76  E8 75 97 E3 FF                  call 0x1409321f0
00AF8A7B  8B D8                           mov ebx, eax
00AF8A7D  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8A81  EB 3C                           jmp 0x140af8abf
00AF8A83  8B D8                           mov ebx, eax
00AF8A85  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8A89  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
00AF8A93  40 8A 74 24 48                  mov sil, byte ptr [rsp + 0x48]
00AF8A98  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00AF8A9D  E9 A1 02 00 00                  jmp 0x140af8d43
00AF8AA2  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00AF8AAA  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
00AF8AB2  33 C9                           xor ecx, ecx
00AF8AB4  E8 37 97 E3 FF                  call 0x1409321f0
00AF8AB9  8B D8                           mov ebx, eax
00AF8ABB  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8ABF  85 DB                           test ebx, ebx
00AF8AC1  0F 88 72 02 00 00               js 0x140af8d39
00AF8AC7  83 FE 03                        cmp esi, 3
00AF8ACA  75 34                           jne 0x140af8b00
00AF8ACC  48 8D 8C 24 B8 00 00 00         lea rcx, [rsp + 0xb8]
00AF8AD4  E8 37 0C E3 FF                  call 0x140929710
00AF8AD9  84 C0                           test al, al
00AF8ADB  0F 84 ED FE FF FF               je 0x140af89ce
00AF8AE1  4C 8D 84 24 FC 00 00 00         lea r8, [rsp + 0xfc]
00AF8AE9  48 8D 94 24 B8 00 00 00         lea rdx, [rsp + 0xb8]
00AF8AF1  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00AF8AF9  E8 0A C4 FB FF                  call 0x140ab4f08
00AF8AFE  EB 22                           jmp 0x140af8b22
00AF8B00  4C 8D 8C 24 00 01 00 00         lea r9, [rsp + 0x100]
00AF8B08  4C 8D 84 24 FC 00 00 00         lea r8, [rsp + 0xfc]
00AF8B10  BA 01 00 00 00                  mov edx, 1
00AF8B15  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00AF8B1D  E8 FA C6 FB FF                  call 0x140ab521c
00AF8B22  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8B26  8B D8                           mov ebx, eax
00AF8B28  44 8B C8                        mov r9d, eax
00AF8B2B  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00AF8B33  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00AF8B3B  8B CE                           mov ecx, esi
00AF8B3D  E8 76 BB D0 FF                  call 0x1408046b8
00AF8B42  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00AF8B4A  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
00AF8B4F  E9 8F 01 00 00                  jmp 0x140af8ce3
00AF8B54  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00AF8B5C  E8 4B 9A D0 FF                  call 0x1408025ac
00AF8B61  8B D8                           mov ebx, eax
00AF8B63  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8B67  44 8B C8                        mov r9d, eax
00AF8B6A  45 33 C0                        xor r8d, r8d
00AF8B6D  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00AF8B75  8B CE                           mov ecx, esi
00AF8B77  E8 3C BB D0 FF                  call 0x1408046b8
00AF8B7C  48 8B D7                        mov rdx, rdi
00AF8B7F  E9 5F 01 00 00                  jmp 0x140af8ce3
00AF8B84  83 EE 08                        sub esi, 8
00AF8B87  0F 84 E5 00 00 00               je 0x140af8c72
00AF8B8D  83 EE 01                        sub esi, 1
00AF8B90  0F 84 B6 00 00 00               je 0x140af8c4c
00AF8B96  83 EE 01                        sub esi, 1
00AF8B99  0F 84 81 00 00 00               je 0x140af8c20
00AF8B9F  83 FE 01                        cmp esi, 1
00AF8BA2  74 0C                           je 0x140af8bb0
00AF8BA4  48 8B D7                        mov rdx, rdi
00AF8BA7  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00AF8BAB  E9 33 01 00 00                  jmp 0x140af8ce3
00AF8BB0  83 BC 24 A0 00 00 00 01         cmp dword ptr [rsp + 0xa0], 1
00AF8BB8  0F 85 8D FD FF FF               jne 0x140af894b
00AF8BBE  39 BC 24 A4 00 00 00            cmp dword ptr [rsp + 0xa4], edi
00AF8BC5  0F 85 80 FD FF FF               jne 0x140af894b
00AF8BCB  39 BC 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], edi
00AF8BD2  0F 85 73 FD FF FF               jne 0x140af894b
00AF8BD8  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AF8BDD  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00AF8BE5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AF8BEA  66 89 7C 24 20                  mov word ptr [rsp + 0x20], di
00AF8BEF  44 8B 8C 24 AC 00 00 00         mov r9d, dword ptr [rsp + 0xac]
00AF8BF7  44 8B 84 24 A8 00 00 00         mov r8d, dword ptr [rsp + 0xa8]
00AF8BFF  33 D2                           xor edx, edx
00AF8C01  48 8D 0D 70 E9 33 00            lea rcx, [rip + 0x33e970]
00AF8C08  E8 0B 5A F7 FF                  call 0x140a6e618
00AF8C0D  8B D8                           mov ebx, eax
00AF8C0F  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8C13  85 C0                           test eax, eax
00AF8C15  0F 88 1E 01 00 00               js 0x140af8d39
00AF8C1B  E9 22 FF FF FF                  jmp 0x140af8b42
00AF8C20  8A D3                           mov dl, bl
00AF8C22  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00AF8C2A  E8 B1 A5 D0 FF                  call 0x1408031e0
00AF8C2F  8B D8                           mov ebx, eax
00AF8C31  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8C35  85 C0                           test eax, eax
00AF8C37  0F 89 05 FF FF FF               jns 0x140af8b42
00AF8C3D  40 8A 74 24 40                  mov sil, byte ptr [rsp + 0x40]
00AF8C42  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00AF8C47  E9 F7 00 00 00                  jmp 0x140af8d43
00AF8C4C  83 BC 24 A0 00 00 00 01         cmp dword ptr [rsp + 0xa0], 1
00AF8C54  0F 85 F1 FC FF FF               jne 0x140af894b
00AF8C5A  39 BC 24 A4 00 00 00            cmp dword ptr [rsp + 0xa4], edi
00AF8C61  0F 85 E4 FC FF FF               jne 0x140af894b
00AF8C67  8B DF                           mov ebx, edi
00AF8C69  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00AF8C6D  E9 0A FF FF FF                  jmp 0x140af8b7c
00AF8C72  83 BC 24 A0 00 00 00 01         cmp dword ptr [rsp + 0xa0], 1
00AF8C7A  0F 85 CB FC FF FF               jne 0x140af894b
00AF8C80  48 83 BC 24 A8 00 00 00 FF      cmp qword ptr [rsp + 0xa8], -1
00AF8C89  0F 85 BC FC FF FF               jne 0x140af894b
00AF8C8F  39 BC 24 B8 00 00 00            cmp dword ptr [rsp + 0xb8], edi
00AF8C96  0F 85 AF FC FF FF               jne 0x140af894b
00AF8C9C  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
00AF8CA4  4D 85 C0                        test r8, r8
00AF8CA7  0F 84 9E FC FF FF               je 0x140af894b
00AF8CAD  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00AF8CB2  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00AF8CB7  45 33 C9                        xor r9d, r9d
00AF8CBA  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00AF8CBF  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00AF8CC4  E8 E7 91 F4 FF                  call 0x140a41eb0
00AF8CC9  8B D8                           mov ebx, eax
00AF8CCB  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8CCF  85 C0                           test eax, eax
00AF8CD1  78 66                           js 0x140af8d39
00AF8CD3  44 39 64 24 58                  cmp dword ptr [rsp + 0x58], r12d
00AF8CD8  0F 87 BC FC FF FF               ja 0x140af899a
00AF8CDE  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00AF8CE3  40 8A 74 24 40                  mov sil, byte ptr [rsp + 0x40]
00AF8CE8  39 7C 24 5C                     cmp dword ptr [rsp + 0x5c], edi
00AF8CEC  0F 85 50 FF FF FF               jne 0x140af8c42
00AF8CF2  40 84 F6                        test sil, sil
00AF8CF5  74 30                           je 0x140af8d27
00AF8CF7  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
00AF8CFC  49 8B CD                        mov rcx, r13
00AF8CFF  E8 3C DB BC FF                  call 0x1406c6840
00AF8D04  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00AF8D09  EB 38                           jmp 0x140af8d43
00AF8D0B  8B D8                           mov ebx, eax
00AF8D0D  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00AF8D11  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
00AF8D1B  40 8A 74 24 48                  mov sil, byte ptr [rsp + 0x48]
00AF8D20  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00AF8D25  EB 1C                           jmp 0x140af8d43
00AF8D27  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
00AF8D2C  49 8B CD                        mov rcx, r13
00AF8D2F  E8 0C DB BC FF                  call 0x1406c6840
00AF8D34  E9 09 FF FF FF                  jmp 0x140af8c42
00AF8D39  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00AF8D3E  40 8A 74 24 40                  mov sil, byte ptr [rsp + 0x40]
00AF8D43  40 84 F6                        test sil, sil
00AF8D46  74 23                           je 0x140af8d6b
00AF8D48  4D 3B FE                        cmp r15, r14
00AF8D4B  4C 0F 42 B4 24 90 00 00 00      cmovb r14, qword ptr [rsp + 0x90]
00AF8D54  41 8B 06                        mov eax, dword ptr [r14]
00AF8D57  41 89 06                        mov dword ptr [r14], eax
00AF8D5A  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00AF8D5E  41 89 07                        mov dword ptr [r15], eax
00AF8D61  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00AF8D65  EB 0B                           jmp 0x140af8d72
00AF8D67  8B D8                           mov ebx, eax
00AF8D69  EB 07                           jmp 0x140af8d72
00AF8D6B  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00AF8D6F  41 89 07                        mov dword ptr [r15], eax
00AF8D72  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00AF8D7A  E8 81 7A EC FF                  call 0x1409c0800
00AF8D7F  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00AF8D84  48 85 C9                        test rcx, rcx
00AF8D87  74 07                           je 0x140af8d90
00AF8D89  33 D2                           xor edx, edx
00AF8D8B  E8 E0 9A 08 00                  call 0x140b82870
00AF8D90  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AF8D95  48 85 C9                        test rcx, rcx
00AF8D98  74 07                           je 0x140af8da1
00AF8D9A  33 D2                           xor edx, edx
00AF8D9C  E8 CF 9A 08 00                  call 0x140b82870
00AF8DA1  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00AF8DA6  48 85 C9                        test rcx, rcx
00AF8DA9  74 07                           je 0x140af8db2
00AF8DAB  33 D2                           xor edx, edx
00AF8DAD  E8 BE 9A 08 00                  call 0x140b82870
00AF8DB2  8B C3                           mov eax, ebx
00AF8DB4  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
00AF8DBC  48 33 CC                        xor rcx, rsp
00AF8DBF  E8 7C 38 BB FF                  call 0x1406ac640
00AF8DC4  48 81 C4 20 01 00 00            add rsp, 0x120
00AF8DCB  41 5F                           pop r15
00AF8DCD  41 5E                           pop r14
00AF8DCF  41 5D                           pop r13
00AF8DD1  41 5C                           pop r12
00AF8DD3  5F                              pop rdi
00AF8DD4  5E                              pop rsi
00AF8DD5  5B                              pop rbx
00AF8DD6  C3                              ret
00AF8DD7  CC                              int3
00AF8DD8  E8 F3 11 DA FF                  call 0x140899fd0
00AF8DDD  90                              nop
00AF8DDE  E8 ED 11 DA FF                  call 0x140899fd0
00AF8DE3  90                              nop
00AF8DE4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtManageHotPatch(int a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int8 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned __int8 v_stack_m118;
    unsigned int v_stack_m128;
    unsigned __int8 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5C;
    unsigned __int64 v_stack_mA0;
    unsigned __int8 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;

    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 3219654)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m108 = a4;
    v_stack_mC8 = a4;
    v_stack_mF8 = a4;
    v_stack_mD8 = v_xmm0;
    result = 0;
    v_stack_mB4 = 0;
    a2 = 0;
    result = memset(v_stack_mB8, a2, result + 100, a4);
    v_rdi = 0;
    v_stack_mF0 = 0;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_mD8, a2, result + 100, a4);
    v_stack_m100 = 0;
    v_stack_m118 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m110 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m114 = 0xC0000001ULL;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3403426)))) & (1)) != 0) goto loc_00AF872E;
loc_00AF8716:
loc_00AF871B:
    v_stack_m114 = (unsigned int)((unsigned int)(0xC00000BBULL));
    goto loc_00AF8D3E;
loc_00AF872E:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3403380)) != 0) goto loc_00AF873F;
    goto loc_00AF871B;
loc_00AF873F:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (7));
    if (condition_is_equal) goto loc_00AF8790;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF8790;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF8790;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF8790;
    if (a1 == 1) goto loc_00AF8790;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5116861), (unsigned __int8)((unsigned int)(0xC00000A3ULL)), result + 100, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AF8773;
    goto loc_00AF871B;
loc_00AF8773:
    result = PsGetCurrentServerSilo(*(unsigned __int64 *)(v_rip + 5116861), (unsigned __int8)((unsigned int)(0xC00000A3ULL)), result + 100, a4);
    result = HalAdjustResourceList(*(unsigned __int64 *)(v_rip + 5116861), (unsigned __int8)((unsigned int)(0xC00000A3ULL)), result + 100, a4);
    if (result == result) goto loc_00AF878C;
    goto loc_00AF871B;
loc_00AF878C:
loc_00AF8790:
    v_stack_mFC = 0;
    if (((unsigned int)((unsigned int)(a1))) > 6) goto loc_00AF87DC;
    if (((unsigned int)((unsigned int)(a1))) == 6) goto loc_00AF87D4;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00AF87CC;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (1));
    if (condition_is_equal) goto loc_00AF8716;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF87C4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF87CC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF8716;
    if (a1 != 1) goto loc_00AF87F7;
loc_00AF87C4:
    goto loc_00AF8835;
loc_00AF87CC:
    goto loc_00AF8835;
loc_00AF87D4:
    goto loc_00AF8835;
loc_00AF87DC:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (7));
    if (condition_is_equal) goto loc_00AF8828;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF8820;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF880D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF87D4;
    if (a1 == 1) goto loc_00AF8801;
loc_00AF87F7:
    goto loc_00AF871B;
loc_00AF8801:
    goto loc_00AF883B;
loc_00AF880D:
    v_stack_mFC = 1;
    goto loc_00AF883B;
loc_00AF8820:
    goto loc_00AF8835;
loc_00AF8828:
    v_stack_mFC = 1;
loc_00AF8835:
loc_00AF883B:
    if (((unsigned int)((unsigned int)(a3))) >= ((unsigned int)(1 + 31))) goto loc_00AF8858;
    v_stack_m114 = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00AF8D39;
loc_00AF8858:
    if ((unsigned __int8)((unsigned int)(0xC0000004ULL)) == 0) goto loc_00AF88E4;
    a1 = v_r14;
    if (v_stack_m108 < v_r14) { a1 = v_stack_m108; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if (1 == 0) goto loc_00AF88A5;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00AF88B0;
    if (((0) & (8 - 1)) != 0) goto loc_00AF8DD8;
    if (((unsigned int)(a3) + a2 * 1) > v_r14) goto loc_00AF88A0;
    if (((unsigned int)(a3) + a2 * 1) >= 0) goto loc_00AF88B0;
loc_00AF88A0:
    goto loc_00AF88B0;
loc_00AF88A5:
    result = ProbeForWrite(0, (unsigned int)(a3), 8, a4);
loc_00AF88B0:
    result = memcpy(v_stack_mB8, 0, (unsigned int)((unsigned int)(1 + 31)), a4);
    goto loc_00AF8901;
loc_00AF88E4:
    result = memcpy(v_stack_mB8, 0, (unsigned int)((unsigned int)(1 + 31)), a4);
loc_00AF8901:
    if (((unsigned int)((unsigned int)(a1))) > 7) goto loc_00AF8B84;
    if (((unsigned int)((unsigned int)(a1))) == 7) goto loc_00AF8B54;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00AF8A16;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (2));
    if (condition_is_equal) goto loc_00AF89AB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF8A16;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AF89AB;
    if (a1 != 1) goto loc_00AF8BA4;
    if (((unsigned int)((unsigned int)(v_stack_mB8))) == 3) goto loc_00AF895E;
    if (((unsigned int)((unsigned int)(v_stack_mB8))) >= 2) goto loc_00AF8959;
loc_00AF894B:
loc_00AF8950:
    v_stack_m114 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00AF8D39;
loc_00AF8959:
    if (((unsigned int)((unsigned int)(v_stack_mB8))) > 3) goto loc_00AF894B;
loc_00AF895E:
    v_stack_m128 = (unsigned int)((unsigned int)(v_stack_mB8));
    v_stack_m130 = (unsigned __int8)((unsigned int)(0xC000000DULL));
    v_stack_m138 = (unsigned int)((unsigned int)(a3));
    result = MiQueryProcessActivePatches(v_stack_mB0, v_stack_mE8, v_stack_m100, 0);
    v_stack_m114 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF8D39;
    if (v_stack_m100 <= ((unsigned int)((unsigned int)(a3)))) goto loc_00AF89A1;
loc_00AF899A:
    goto loc_00AF8950;
loc_00AF89A1:
    goto loc_00AF8CE3;
loc_00AF89AB:
    if (v_stack_mB8 != 2) goto loc_00AF894B;
    if (((unsigned int)((unsigned int)(a1))) != 5) goto loc_00AF89E0;
    result = RtlValidSid(v_stack_mB4, v_stack_mE8, v_stack_m100, 0);
    if ((unsigned __int8)(result) != 0) goto loc_00AF89D8;
loc_00AF89CE:
    goto loc_00AF8950;
loc_00AF89D8:
loc_00AF89E0:
    v_stack_m138 = (unsigned int)((unsigned int)(a3));
    result = MiQueryLoadedPatches(v_stack_mB4, v_stack_mF0, v_stack_m100, 0);
    v_stack_m114 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF8D39;
    if (v_stack_m100 > ((unsigned int)((unsigned int)(a3)))) goto loc_00AF899A;
    goto loc_00AF8CE3;
loc_00AF8A16:
    if (v_stack_mB8 != 2) goto loc_00AF894B;
    if (v_stack_mB0 == 0) goto loc_00AF894B;
    if ((unsigned __int8)((unsigned int)((unsigned int)(result))) == 0) goto loc_00AF8AA2;
    if (((v_stack_mA8) & (1)) != 0) goto loc_00AF8DDE;
    a2 = (v_stack_mB0) + (v_stack_mA8);
    if (a2 > v_r14) goto loc_00AF8A61;
    if (a2 < v_stack_mA8) {
        result = *(unsigned __int8 *)(v_r14);
    }
    a1 = 0;
    result = RtlDuplicateUnicodeString(a1, v_stack_mB0, v_stack_mD8, 0);
    v_stack_m114 = (unsigned int)(result);
    goto loc_00AF8ABF;
loc_00AF8AA2:
    a1 = 0;
    result = RtlDuplicateUnicodeString(a1, v_stack_mB0, v_stack_mD8, 0);
    v_stack_m114 = (unsigned int)(result);
loc_00AF8ABF:
    if (sign_flag) goto loc_00AF8D39;
    if (((unsigned int)((unsigned int)(a1))) != 3) goto loc_00AF8B00;
    result = RtlValidSid(v_stack_mA0, v_stack_mB0, v_stack_mD8, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00AF89CE;
    result = MiLoadHotPatchForUserSid(v_stack_mD8, v_stack_mA0, v_stack_m5C, 0);
    goto loc_00AF8B22;
loc_00AF8B00:
    result = MiLoadHotPatch(v_stack_mD8, 1, v_stack_m5C, v_stack_m58);
loc_00AF8B22:
    v_stack_m114 = (unsigned int)(result);
    result = MiLogHotPatchManagement((unsigned int)((unsigned int)((unsigned int)(a1))), v_stack_mB8, v_stack_mD8, (unsigned int)((unsigned int)(result)));
loc_00AF8B42:
    v_stack_m100 = (unsigned int)(1 + 31);
    goto loc_00AF8CE3;
loc_00AF8B54:
    result = MiApplyImageHotPatchRequest(v_stack_mB8, v_stack_mB8, v_stack_mD8, (unsigned int)((unsigned int)(result)));
    v_stack_m114 = (unsigned int)(result);
    a3 = 0;
    result = MiLogHotPatchManagement((unsigned int)((unsigned int)((unsigned int)(a1))), v_stack_mB8, a3, (unsigned int)((unsigned int)(result)));
loc_00AF8B7C:
    goto loc_00AF8CE3;
loc_00AF8B84:
    v_rsi = (unsigned int)(((unsigned int)(a1)) - (8));
    if (condition_is_equal) goto loc_00AF8C72;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00AF8C4C;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00AF8C20;
    if (((unsigned int)(v_rsi)) == 1) goto loc_00AF8BB0;
loc_00AF8BA4:
    goto loc_00AF8CE3;
loc_00AF8BB0:
    if (v_stack_mB8 != 1) goto loc_00AF894B;
    if (v_stack_mB4 != 0) goto loc_00AF894B;
    if (v_stack_mA8 != 0) goto loc_00AF894B;
    v_stack_m128 = 0;
    v_stack_m130 = v_stack_mA8;
    v_stack_m138 = 0;
    a2 = 0;
    result = MiFindHotPatchRecord(v_rip + 3402096, a2, (unsigned int)(v_stack_mB0), (unsigned int)(v_stack_mAC));
    v_stack_m114 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF8D39;
    goto loc_00AF8B42;
loc_00AF8C20:
    result = MiCreatePatchSectionRequest(v_stack_mB8, (unsigned __int8)((unsigned int)((unsigned int)(result))), (unsigned int)(v_stack_mB0), (unsigned int)(v_stack_mAC));
    v_stack_m114 = (unsigned int)(result);
    if (!sign_flag) goto loc_00AF8B42;
loc_00AF8C42:
    goto loc_00AF8D43;
loc_00AF8C4C:
    if (v_stack_mB8 != 1) goto loc_00AF894B;
    if (v_stack_mB4 != 0) goto loc_00AF894B;
    v_stack_m114 = 0;
    goto loc_00AF8B7C;
loc_00AF8C72:
    if (v_stack_mB8 != 1) goto loc_00AF894B;
    if (v_stack_mB0 != -1) goto loc_00AF894B;
    if (v_stack_mA0 != 0) goto loc_00AF894B;
    if (v_stack_mA8 == 0) goto loc_00AF894B;
    v_stack_m130 = (unsigned int)((unsigned int)(a3));
    v_stack_m138 = 0;
    a4 = 0;
    result = MiQuerySingleLoadedPatch(v_stack_mE0, v_stack_m100, v_stack_mA8, a4);
    v_stack_m114 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF8D39;
    if (v_stack_m100 > ((unsigned int)((unsigned int)(a3)))) goto loc_00AF899A;
loc_00AF8CE3:
    if (v_stack_mFC != 0) goto loc_00AF8C42;
    if ((unsigned __int8)(v_stack_m118) == 0) goto loc_00AF8D27;
    result = memcpy(0, v_stack_mE0, (unsigned int)(v_stack_m100), a4);
    goto loc_00AF8D43;
loc_00AF8D27:
    result = memcpy(0, v_stack_mE0, (unsigned int)(v_stack_m100), a4);
    goto loc_00AF8C42;
loc_00AF8D39:
loc_00AF8D3E:
loc_00AF8D43:
    if ((unsigned __int8)(v_stack_m118) == 0) goto loc_00AF8D6B;
    if (v_stack_m108 < v_r14) { v_r14 = v_stack_mC8; }
    *(unsigned int *)(v_r14) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14)));
    *(unsigned int *)(v_stack_m108) = (unsigned int)((unsigned int)(v_stack_m100));
    goto loc_00AF8D72;
loc_00AF8D6B:
    *(unsigned int *)(v_stack_m108) = (unsigned int)((unsigned int)(v_stack_m100));
loc_00AF8D72:
    result = RtlFreeAnsiString(v_stack_mD8, v_stack_mE0, (unsigned int)(v_stack_m100), a4);
    if (v_stack_mF0 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_mF0, a2, (unsigned int)(v_stack_m100), a4);
    }
    if (v_stack_mE8 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_mE8, a2, (unsigned int)(v_stack_m100), a4);
    }
    if (v_stack_mE0 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_mE0, a2, (unsigned int)(v_stack_m100), a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(v_stack_m100), a4);
    v_rsp = (v_rsp) + (288);
    return result;
loc_00AF8DD8:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned int)(v_stack_m100), a4);
loc_00AF8DDE:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned int)(v_stack_m100), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtManageHotPatch(int32_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint8_t v_stack_m110;
    uint32_t v_stack_m114;
    uint8_t v_stack_m118;
    uint32_t v_stack_m128;
    uint8_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5C;
    uint64_t v_stack_mA0;
    uint8_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;

    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0x3120C6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m108 = Arg4;
    v_stack_mC8 = Arg4;
    v_stack_mF8 = Arg4;
    v_stack_mD8 = v_xmm0;
    result = 0;
    v_stack_mB4 = 0;
    Arg2 = 0;
    result = memset(v_stack_mB8, Arg2, result + 100, Arg4);
    local_rdi = 0;
    v_stack_mF0 = 0;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_mD8, Arg2, result + 100, Arg4);
    v_stack_m100 = 0;
    v_stack_m118 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m110 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m114 = 0xC0000001ULL;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x33EEA2)))) & (1)) != 0) goto loc_00AF872E;
loc_00AF8716:
loc_00AF871B:
    v_stack_m114 = (uint32_t)((uint32_t)(0xC00000BBULL));
    goto loc_00AF8D3E;
loc_00AF872E:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x33EE74)) != 0) goto loc_00AF873F;
    goto loc_00AF871B;
loc_00AF873F:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (7));
    if (condition_is_equal) goto loc_00AF8790;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF8790;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF8790;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF8790;
    if (Arg1 == 1) goto loc_00AF8790;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E13BD), (uint8_t)((uint32_t)(0xC00000A3ULL)), result + 100, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AF8773;
    goto loc_00AF871B;
loc_00AF8773:
    result = PsGetCurrentServerSilo(*(uint64_t *)(v_rip + 0x4E13BD), (uint8_t)((uint32_t)(0xC00000A3ULL)), result + 100, Arg4);
    result = HalAdjustResourceList(*(uint64_t *)(v_rip + 0x4E13BD), (uint8_t)((uint32_t)(0xC00000A3ULL)), result + 100, Arg4);
    if (result == result) goto loc_00AF878C;
    goto loc_00AF871B;
loc_00AF878C:
loc_00AF8790:
    v_stack_mFC = 0;
    if (((uint32_t)((uint32_t)(Arg1))) > 6) goto loc_00AF87DC;
    if (((uint32_t)((uint32_t)(Arg1))) == 6) goto loc_00AF87D4;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00AF87CC;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (1));
    if (condition_is_equal) goto loc_00AF8716;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF87C4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF87CC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF8716;
    if (Arg1 != 1) goto loc_00AF87F7;
loc_00AF87C4:
    goto loc_00AF8835;
loc_00AF87CC:
    goto loc_00AF8835;
loc_00AF87D4:
    goto loc_00AF8835;
loc_00AF87DC:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (7));
    if (condition_is_equal) goto loc_00AF8828;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF8820;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF880D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF87D4;
    if (Arg1 == 1) goto loc_00AF8801;
loc_00AF87F7:
    goto loc_00AF871B;
loc_00AF8801:
    goto loc_00AF883B;
loc_00AF880D:
    v_stack_mFC = 1;
    goto loc_00AF883B;
loc_00AF8820:
    goto loc_00AF8835;
loc_00AF8828:
    v_stack_mFC = 1;
loc_00AF8835:
loc_00AF883B:
    if (((uint32_t)((uint32_t)(Arg3))) >= ((uint32_t)(1 + 31))) goto loc_00AF8858;
    v_stack_m114 = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00AF8D39;
loc_00AF8858:
    if ((uint8_t)((uint32_t)(0xC0000004ULL)) == 0) goto loc_00AF88E4;
    Arg1 = local_r14;
    if (v_stack_m108 < local_r14) { Arg1 = v_stack_m108; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if (1 == 0) goto loc_00AF88A5;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00AF88B0;
    if (((0) & (8 - 1)) != 0) goto loc_00AF8DD8;
    if (((uint32_t)(Arg3) + Arg2 * 1) > local_r14) goto loc_00AF88A0;
    if (((uint32_t)(Arg3) + Arg2 * 1) >= 0) goto loc_00AF88B0;
loc_00AF88A0:
    goto loc_00AF88B0;
loc_00AF88A5:
    result = ProbeForWrite(0, (uint32_t)(Arg3), 8, Arg4);
loc_00AF88B0:
    result = memcpy(v_stack_mB8, 0, (uint32_t)((uint32_t)(1 + 31)), Arg4);
    goto loc_00AF8901;
loc_00AF88E4:
    result = memcpy(v_stack_mB8, 0, (uint32_t)((uint32_t)(1 + 31)), Arg4);
loc_00AF8901:
    if (((uint32_t)((uint32_t)(Arg1))) > 7) goto loc_00AF8B84;
    if (((uint32_t)((uint32_t)(Arg1))) == 7) goto loc_00AF8B54;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00AF8A16;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (2));
    if (condition_is_equal) goto loc_00AF89AB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF8A16;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AF89AB;
    if (Arg1 != 1) goto loc_00AF8BA4;
    if (((uint32_t)((uint32_t)(v_stack_mB8))) == 3) goto loc_00AF895E;
    if (((uint32_t)((uint32_t)(v_stack_mB8))) >= 2) goto loc_00AF8959;
loc_00AF894B:
loc_00AF8950:
    v_stack_m114 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00AF8D39;
loc_00AF8959:
    if (((uint32_t)((uint32_t)(v_stack_mB8))) > 3) goto loc_00AF894B;
loc_00AF895E:
    v_stack_m128 = (uint32_t)((uint32_t)(v_stack_mB8));
    v_stack_m130 = (uint8_t)((uint32_t)(0xC000000DULL));
    v_stack_m138 = (uint32_t)((uint32_t)(Arg3));
    result = MiQueryProcessActivePatches(v_stack_mB0, v_stack_mE8, v_stack_m100, 0);
    v_stack_m114 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF8D39;
    if (v_stack_m100 <= ((uint32_t)((uint32_t)(Arg3)))) goto loc_00AF89A1;
loc_00AF899A:
    goto loc_00AF8950;
loc_00AF89A1:
    goto loc_00AF8CE3;
loc_00AF89AB:
    if (v_stack_mB8 != 2) goto loc_00AF894B;
    if (((uint32_t)((uint32_t)(Arg1))) != 5) goto loc_00AF89E0;
    result = RtlValidSid(v_stack_mB4, v_stack_mE8, v_stack_m100, 0);
    if ((uint8_t)(result) != 0) goto loc_00AF89D8;
loc_00AF89CE:
    goto loc_00AF8950;
loc_00AF89D8:
loc_00AF89E0:
    v_stack_m138 = (uint32_t)((uint32_t)(Arg3));
    result = MiQueryLoadedPatches(v_stack_mB4, v_stack_mF0, v_stack_m100, 0);
    v_stack_m114 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF8D39;
    if (v_stack_m100 > ((uint32_t)((uint32_t)(Arg3)))) goto loc_00AF899A;
    goto loc_00AF8CE3;
loc_00AF8A16:
    if (v_stack_mB8 != 2) goto loc_00AF894B;
    if (v_stack_mB0 == 0) goto loc_00AF894B;
    if ((uint8_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00AF8AA2;
    if (((v_stack_mA8) & (1)) != 0) goto loc_00AF8DDE;
    Arg2 = (v_stack_mB0) + (v_stack_mA8);
    if (Arg2 > local_r14) goto loc_00AF8A61;
    if (Arg2 < v_stack_mA8) {
        result = *(uint8_t *)(local_r14);
    }
    Arg1 = 0;
    result = RtlDuplicateUnicodeString(Arg1, v_stack_mB0, v_stack_mD8, 0);
    v_stack_m114 = (uint32_t)(result);
    goto loc_00AF8ABF;
loc_00AF8AA2:
    Arg1 = 0;
    result = RtlDuplicateUnicodeString(Arg1, v_stack_mB0, v_stack_mD8, 0);
    v_stack_m114 = (uint32_t)(result);
loc_00AF8ABF:
    if (sign_flag) goto loc_00AF8D39;
    if (((uint32_t)((uint32_t)(Arg1))) != 3) goto loc_00AF8B00;
    result = RtlValidSid(v_stack_mA0, v_stack_mB0, v_stack_mD8, 0);
    if ((uint8_t)(result) == 0) goto loc_00AF89CE;
    result = MiLoadHotPatchForUserSid(v_stack_mD8, v_stack_mA0, v_stack_m5C, 0);
    goto loc_00AF8B22;
loc_00AF8B00:
    result = MiLoadHotPatch(v_stack_mD8, 1, v_stack_m5C, v_stack_m58);
loc_00AF8B22:
    v_stack_m114 = (uint32_t)(result);
    result = MiLogHotPatchManagement((uint32_t)((uint32_t)((uint32_t)(Arg1))), v_stack_mB8, v_stack_mD8, (uint32_t)((uint32_t)(result)));
loc_00AF8B42:
    v_stack_m100 = (uint32_t)(1 + 31);
    goto loc_00AF8CE3;
loc_00AF8B54:
    result = MiApplyImageHotPatchRequest(v_stack_mB8, v_stack_mB8, v_stack_mD8, (uint32_t)((uint32_t)(result)));
    v_stack_m114 = (uint32_t)(result);
    Arg3 = 0;
    result = MiLogHotPatchManagement((uint32_t)((uint32_t)((uint32_t)(Arg1))), v_stack_mB8, Arg3, (uint32_t)((uint32_t)(result)));
loc_00AF8B7C:
    goto loc_00AF8CE3;
loc_00AF8B84:
    local_rsi = (uint32_t)(((uint32_t)(Arg1)) - (8));
    if (condition_is_equal) goto loc_00AF8C72;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00AF8C4C;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00AF8C20;
    if (((uint32_t)(local_rsi)) == 1) goto loc_00AF8BB0;
loc_00AF8BA4:
    goto loc_00AF8CE3;
loc_00AF8BB0:
    if (v_stack_mB8 != 1) goto loc_00AF894B;
    if (v_stack_mB4 != 0) goto loc_00AF894B;
    if (v_stack_mA8 != 0) goto loc_00AF894B;
    v_stack_m128 = 0;
    v_stack_m130 = v_stack_mA8;
    v_stack_m138 = 0;
    Arg2 = 0;
    result = MiFindHotPatchRecord(v_rip + 3402096, Arg2, (uint32_t)(v_stack_mB0), (uint32_t)(v_stack_mAC));
    v_stack_m114 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF8D39;
    goto loc_00AF8B42;
loc_00AF8C20:
    result = MiCreatePatchSectionRequest(v_stack_mB8, (uint8_t)((uint32_t)((uint32_t)(result))), (uint32_t)(v_stack_mB0), (uint32_t)(v_stack_mAC));
    v_stack_m114 = (uint32_t)(result);
    if (!sign_flag) goto loc_00AF8B42;
loc_00AF8C42:
    goto loc_00AF8D43;
loc_00AF8C4C:
    if (v_stack_mB8 != 1) goto loc_00AF894B;
    if (v_stack_mB4 != 0) goto loc_00AF894B;
    v_stack_m114 = 0;
    goto loc_00AF8B7C;
loc_00AF8C72:
    if (v_stack_mB8 != 1) goto loc_00AF894B;
    if (v_stack_mB0 != -1) goto loc_00AF894B;
    if (v_stack_mA0 != 0) goto loc_00AF894B;
    if (v_stack_mA8 == 0) goto loc_00AF894B;
    v_stack_m130 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m138 = 0;
    Arg4 = 0;
    result = MiQuerySingleLoadedPatch(v_stack_mE0, v_stack_m100, v_stack_mA8, Arg4);
    v_stack_m114 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF8D39;
    if (v_stack_m100 > ((uint32_t)((uint32_t)(Arg3)))) goto loc_00AF899A;
loc_00AF8CE3:
    if (v_stack_mFC != 0) goto loc_00AF8C42;
    if ((uint8_t)(v_stack_m118) == 0) goto loc_00AF8D27;
    result = memcpy(0, v_stack_mE0, (uint32_t)(v_stack_m100), Arg4);
    goto loc_00AF8D43;
loc_00AF8D27:
    result = memcpy(0, v_stack_mE0, (uint32_t)(v_stack_m100), Arg4);
    goto loc_00AF8C42;
loc_00AF8D39:
loc_00AF8D3E:
loc_00AF8D43:
    if ((uint8_t)(v_stack_m118) == 0) goto loc_00AF8D6B;
    if (v_stack_m108 < local_r14) { local_r14 = v_stack_mC8; }
    *(uint32_t *)(local_r14) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14)));
    *(uint32_t *)(v_stack_m108) = (uint32_t)((uint32_t)(v_stack_m100));
    goto loc_00AF8D72;
loc_00AF8D6B:
    *(uint32_t *)(v_stack_m108) = (uint32_t)((uint32_t)(v_stack_m100));
loc_00AF8D72:
    result = RtlFreeAnsiString(v_stack_mD8, v_stack_mE0, (uint32_t)(v_stack_m100), Arg4);
    if (v_stack_mF0 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_mF0, Arg2, (uint32_t)(v_stack_m100), Arg4);
    }
    if (v_stack_mE8 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_mE8, Arg2, (uint32_t)(v_stack_m100), Arg4);
    }
    if (v_stack_mE0 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_mE0, Arg2, (uint32_t)(v_stack_m100), Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(v_stack_m100), Arg4);
    local_rsp = (local_rsp) + (288);
    return result;
loc_00AF8DD8:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint32_t)(v_stack_m100), Arg4);
loc_00AF8DDE:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint32_t)(v_stack_m100), Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF8660&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
