# NtOpenObjectAuditAlarm

- RVA: `0x00974700`–`0x00974E42` (길이 `1,858` bytes)
- VA: `0x0000000140974700`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00096460`
- 디코드: `387`개 명령, `1,858/1,858` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009747A3` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x009747B3` → [SeCheckAuditPrivilege](SeCheckAuditPrivilege_function_00974E48.md) (function, `0x00974E48`)
- `0x009747EF` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00974844` → [SeCaptureSecurityDescriptor](../92/SeCaptureSecurityDescriptor_function_00929F40.md) (function, `0x00929F40`)
- `0x009748F9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00974920` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00974940` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00974969` → [SepProbeAndCaptureString_U](SepProbeAndCaptureString_U_function_00975070.md) (function, `0x00975070`)
- `0x0097498F` → [SepProbeAndCaptureString_U](SepProbeAndCaptureString_U_function_00975070.md) (function, `0x00975070`)
- `0x009749B5` → [SepProbeAndCaptureString_U](SepProbeAndCaptureString_U_function_00975070.md) (function, `0x00975070`)
- `0x00974A10` → [SeReleaseSecurityDescriptor](SeReleaseSecurityDescriptor_function_00975190.md) (function, `0x00975190`)
- `0x00974A1D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00974A2A` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00974A3D` → [SepAuditFailed](../86/SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)
- `0x00974AE8` → [SepAdtAuditObjectAccessWithContext](../86/SepAdtAuditObjectAccessWithContext_function_0086EEF0.md) (function, `0x0086EEF0`)
- `0x00974B9F` → [SepAdtPrivilegeObjectAuditAlarm](../86/SepAdtPrivilegeObjectAuditAlarm_function_0086E3F0.md) (function, `0x0086E3F0`)
- `0x00974BBA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00974BCE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00974BDD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00974BF1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00974C05` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00974C12` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00974C1F` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00974C46` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00974C58` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00974CB3` → [SeReleaseSecurityDescriptor](SeReleaseSecurityDescriptor_function_00975190.md) (function, `0x00975190`)
- `0x00974CC0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00974CCD` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00974CDD` → [SepAuditFailed](../86/SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)
- `0x00974CF9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00974D06` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00974D16` → [SepAuditFailed](../86/SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)
- `0x00974D79` → [SeExamineSacl](SeExamineSacl_function_00973A30.md) (function, `0x00973A30`)
- `0x00974DAF` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00974DCA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00974DDB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00974DE7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00974DF3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00974DFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009747C0` → RVA `0x00FD8020` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x009748F9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00974920` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00974A1D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00974BBA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00974BCE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00974BDD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00974BF1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00974C05` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00974C12` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00974C46` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00974CC0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00974CF9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00974DCA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00974DDB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00974DE7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00974DF3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00974DFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00974D85` → [sub_00B2983E + 0x12](../B2/Unknown_function_00B2983E.md) (`tail-transfer`)
  - `0x00974D98` → [sub_00B2983E + 0x12](../B2/Unknown_function_00B2983E.md) (`tail-transfer`)
  - `0x00974E0C` → [sub_00B2983E](../B2/Unknown_function_00B2983E.md) (`tail-transfer`)
  - `0x00974E28` → [sub_00B2983E + 0x9](../B2/Unknown_function_00B2983E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00974700  48 8B C4                        mov rax, rsp
00974703  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00974707  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0097470B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0097470F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00974713  53                              push rbx
00974714  56                              push rsi
00974715  57                              push rdi
00974716  41 54                           push r12
00974718  41 55                           push r13
0097471A  41 56                           push r14
0097471C  41 57                           push r15
0097471E  48 81 EC 20 01 00 00            sub rsp, 0x120
00974725  4C 8B E2                        mov r12, rdx
00974728  48 89 94 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdx
00974730  4C 8B B4 24 A0 01 00 00         mov r14, qword ptr [rsp + 0x1a0]
00974738  33 DB                           xor ebx, ebx
0097473A  48 89 98 70 FF FF FF            mov qword ptr [rax - 0x90], rbx
00974741  48 89 98 68 FF FF FF            mov qword ptr [rax - 0x98], rbx
00974748  48 89 98 78 FF FF FF            mov qword ptr [rax - 0x88], rbx
0097474F  48 89 98 58 FF FF FF            mov qword ptr [rax - 0xa8], rbx
00974756  48 89 58 80                     mov qword ptr [rax - 0x80], rbx
0097475A  88 9C 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], bl
00974761  0F 57 C0                        xorps xmm0, xmm0
00974764  0F 11 40 A0                     movups xmmword ptr [rax - 0x60], xmm0
00974768  0F 11 40 B0                     movups xmmword ptr [rax - 0x50], xmm0
0097476C  88 98 49 FF FF FF               mov byte ptr [rax - 0xb7], bl
00974772  88 98 4A FF FF FF               mov byte ptr [rax - 0xb6], bl
00974778  48 89 58 98                     mov qword ptr [rax - 0x68], rbx
0097477C  66 89 98 54 FF FF FF            mov word ptr [rax - 0xac], bx
00974783  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0097478C  44 8A A8 32 02 00 00            mov r13b, byte ptr [rax + 0x232]
00974793  44 88 AC 24 A3 00 00 00         mov byte ptr [rsp + 0xa3], r13b
0097479B  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
009747A3  E8 78 70 EF FF                  call 0x14086b820
009747A8  41 8A D5                        mov dl, r13b
009747AB  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
009747B3  E8 90 06 00 00                  call 0x140974e48
009747B8  84 C0                           test al, al
009747BA  0F 84 DD 05 00 00               je 0x140974d9d
009747C0  4C 8B 05 59 38 66 00            mov r8, qword ptr [rip + 0x663859]
009747C7  48 89 9C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rbx
009747CF  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
009747D4  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
009747DC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009747E1  45 8A CD                        mov r9b, r13b
009747E4  8D 53 08                        lea edx, [rbx + 8]
009747E7  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
009747EF  E8 BC 45 EF FF                  call 0x140868db0
009747F4  8B F8                           mov edi, eax
009747F6  85 C0                           test eax, eax
009747F8  0F 88 A9 05 00 00               js 0x140974da7
009747FE  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
00974806  83 BF C0 00 00 00 02            cmp dword ptr [rdi + 0xc0], 2
0097480D  75 0D                           jne 0x14097481c
0097480F  83 BF C4 00 00 00 01            cmp dword ptr [rdi + 0xc4], 1
00974816  0F 8C 27 04 00 00               jl 0x140974c43
0097481C  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
00974824  48 85 C9                        test rcx, rcx
00974827  0F 84 9A 05 00 00               je 0x140974dc7
0097482D  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00974835  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0097483A  45 33 C9                        xor r9d, r9d
0097483D  45 8D 41 01                     lea r8d, [r9 + 1]
00974841  41 8A D5                        mov dl, r13b
00974844  E8 F7 56 FB FF                  call 0x140929f40
00974849  8B F0                           mov esi, eax
0097484B  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00974852  85 C0                           test eax, eax
00974854  0F 88 9C 04 00 00               js 0x140974cf6
0097485A  48 39 9C 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rbx
00974862  0F 84 8E 04 00 00               je 0x140974cf6
00974868  44 8A BC 24 B0 01 00 00         mov r15b, byte ptr [rsp + 0x1b0]
00974870  45 84 FF                        test r15b, r15b
00974873  0F 84 4F 01 00 00               je 0x1409749c8
00974879  4D 85 F6                        test r14, r14
0097487C  0F 84 46 01 00 00               je 0x1409749c8
00974882  41 F6 C6 03                     test r14b, 3
00974886  0F 85 B4 00 00 00               jne 0x140974940
0097488C  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
00974896  48 8B C7                        mov rax, rdi
00974899  4C 3B F7                        cmp r14, rdi
0097489C  49 0F 42 C6                     cmovb rax, r14
009748A0  90                              nop
009748A1  8A 00                           mov al, byte ptr [rax]
009748A3  41 8B 36                        mov esi, dword ptr [r14]
009748A6  89 B4 24 EC 00 00 00            mov dword ptr [rsp + 0xec], esi
009748AD  83 FE 43                        cmp esi, 0x43
009748B0  0F 83 21 01 00 00               jae 0x1409749d7
009748B6  8D 04 76                        lea eax, [rsi + rsi*2]
009748B9  8D 0C 85 08 00 00 00            lea ecx, [rax*4 + 8]
009748C0  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
009748C7  85 C9                           test ecx, ecx
009748C9  74 17                           je 0x1409748e2
009748CB  8B D1                           mov edx, ecx
009748CD  49 03 D6                        add rdx, r14
009748D0  48 3B D7                        cmp rdx, rdi
009748D3  0F 87 14 01 00 00               ja 0x1409749ed
009748D9  49 3B D6                        cmp rdx, r14
009748DC  0F 82 0B 01 00 00               jb 0x1409749ed
009748E2  8B C1                           mov eax, ecx
009748E4  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
009748EC  41 B8 53 65 50 72               mov r8d, 0x72506553
009748F2  8B D1                           mov edx, ecx
009748F4  B9 00 01 00 00                  mov ecx, 0x100
009748F9  E8 F2 D7 20 00                  call 0x140b820f0
009748FE  4C 8B E0                        mov r12, rax
00974901  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
00974909  48 85 C0                        test rax, rax
0097490C  0F 84 F0 00 00 00               je 0x140974a02
00974912  4C 8B 84 24 18 01 00 00         mov r8, qword ptr [rsp + 0x118]
0097491A  49 8B D6                        mov rdx, r14
0097491D  48 8B C8                        mov rcx, rax
00974920  E8 1B 1F D5 FF                  call 0x1406c6840
00974925  41 89 34 24                     mov dword ptr [r12], esi
00974929  4C 8B A4 24 E0 00 00 00         mov r12, qword ptr [rsp + 0xe0]
00974931  4D 85 E4                        test r12, r12
00974934  74 10                           je 0x140974946
00974936  41 F6 C4 07                     test r12b, 7
0097493A  0F 84 09 01 00 00               je 0x140974a49
00974940  E8 8B 56 F2 FF                  call 0x140899fd0
00974945  CC                              int3
00974946  4C 8B A4 24 B8 01 00 00         mov r12, qword ptr [rsp + 0x1b8]
0097494E  4C 3B E7                        cmp r12, rdi
00974951  49 0F 42 FC                     cmovb rdi, r12
00974955  8A 07                           mov al, byte ptr [rdi]
00974957  88 07                           mov byte ptr [rdi], al
00974959  48 8D 94 24 C8 00 00 00         lea rdx, [rsp + 0xc8]
00974961  48 8B 8C 24 60 01 00 00         mov rcx, qword ptr [rsp + 0x160]
00974969  E8 02 07 00 00                  call 0x140975070
0097496E  8B F8                           mov edi, eax
00974970  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00974977  85 C0                           test eax, eax
00974979  0F 88 E8 00 00 00               js 0x140974a67
0097497F  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
00974987  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
0097498F  E8 DC 06 00 00                  call 0x140975070
00974994  8B F8                           mov edi, eax
00974996  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
0097499D  85 C0                           test eax, eax
0097499F  0F 88 C2 00 00 00               js 0x140974a67
009749A5  48 8D 94 24 D0 00 00 00         lea rdx, [rsp + 0xd0]
009749AD  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
009749B5  E8 B6 06 00 00                  call 0x140975070
009749BA  8B F8                           mov edi, eax
009749BC  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
009749C3  E9 9F 00 00 00                  jmp 0x140974a67
009749C8  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
009749D2  E9 5A FF FF FF                  jmp 0x140974931
009749D7  BF 0D 00 00 C0                  mov edi, 0xc000000d
009749DC  89 BC 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edi
009749E3  4C 8B A4 24 B8 01 00 00         mov r12, qword ptr [rsp + 0x1b8]
009749EB  EB 7A                           jmp 0x140974a67
009749ED  8A 07                           mov al, byte ptr [rdi]
009749EF  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
009749F6  8B B4 24 EC 00 00 00            mov esi, dword ptr [rsp + 0xec]
009749FD  E9 E0 FE FF FF                  jmp 0x1409748e2
00974A02  45 33 C0                        xor r8d, r8d
00974A05  41 8A D5                        mov dl, r13b
00974A08  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00974A10  E8 7B 07 00 00                  call 0x140975190
00974A15  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00974A1D  E8 2E 49 98 FF                  call 0x1402f9350
00974A22  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00974A2A  E8 E1 6C EF FF                  call 0x14086b710
00974A2F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00974A34  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
00974A3B  8B CB                           mov ecx, ebx
00974A3D  E8 DE A3 EF FF                  call 0x14086ee20
00974A42  8B C3                           mov eax, ebx
00974A44  E9 E6 01 00 00                  jmp 0x140974c2f
00974A49  48 8B C7                        mov rax, rdi
00974A4C  4C 3B E7                        cmp r12, rdi
00974A4F  49 0F 42 C4                     cmovb rax, r12
00974A53  90                              nop
00974A54  8A 00                           mov al, byte ptr [rax]
00974A56  49 8B 04 24                     mov rax, qword ptr [r12]
00974A5A  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00974A62  E9 DF FE FF FF                  jmp 0x140974946
00974A67  EB 42                           jmp 0x140974aab
00974A69  8B F8                           mov edi, eax
00974A6B  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00974A72  33 DB                           xor ebx, ebx
00974A74  4C 8B A4 24 B8 01 00 00         mov r12, qword ptr [rsp + 0x1b8]
00974A7C  44 8A BC 24 B0 01 00 00         mov r15b, byte ptr [rsp + 0x1b0]
00974A84  4C 8B B4 24 A0 01 00 00         mov r14, qword ptr [rsp + 0x1a0]
00974A8C  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
00974A94  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00974A9C  44 8A AC 24 A3 00 00 00         mov r13b, byte ptr [rsp + 0xa3]
00974AA4  88 9C 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], bl
00974AAB  85 FF                           test edi, edi
00974AAD  0F 88 AE 01 00 00               js 0x140974c61
00974AB3  45 84 FF                        test r15b, r15b
00974AB6  41 0F 94 C1                     sete r9b
00974ABA  48 8D 84 24 AC 00 00 00         lea rax, [rsp + 0xac]
00974AC2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00974AC7  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00974ACB  48 8D 84 24 F8 00 00 00         lea rax, [rsp + 0xf8]
00974AD3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00974AD8  45 8A C7                        mov r8b, r15b
00974ADB  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
00974AE3  48 8B D6                        mov rdx, rsi
00974AE6  33 C9                           xor ecx, ecx
00974AE8  E8 03 A4 EF FF                  call 0x14086eef0
00974AED  48 8B BC 24 B0 00 00 00         mov rdi, qword ptr [rsp + 0xb0]
00974AF5  84 C0                           test al, al
00974AF7  0F 85 25 02 00 00               jne 0x140974d22
00974AFD  38 9C 24 A1 00 00 00            cmp byte ptr [rsp + 0xa1], bl
00974B04  0F 85 DF 01 00 00               jne 0x140974ce9
00974B0A  38 9C 24 A2 00 00 00            cmp byte ptr [rsp + 0xa2], bl
00974B11  0F 85 D2 01 00 00               jne 0x140974ce9
00974B17  4D 85 F6                        test r14, r14
00974B1A  0F 84 C9 01 00 00               je 0x140974ce9
00974B20  45 84 FF                        test r15b, r15b
00974B23  0F 84 C0 01 00 00               je 0x140974ce9
00974B29  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00974B32  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00974B39  44 88 7C 24 48                  mov byte ptr [rsp + 0x48], r15b
00974B3E  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00974B46  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00974B4B  8B 84 24 90 01 00 00            mov eax, dword ptr [rsp + 0x190]
00974B52  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00974B56  48 8B 81 D0 01 00 00            mov rax, qword ptr [rcx + 0x1d0]
00974B5D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00974B62  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00974B6A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00974B6F  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00974B77  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00974B7C  4C 8B 8C 24 F0 00 00 00         mov r9, qword ptr [rsp + 0xf0]
00974B84  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
00974B8C  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
00974B94  48 8B D6                        mov rdx, rsi
00974B97  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00974B9F  E8 4C 98 EF FF                  call 0x14086e3f0
00974BA4  44 8A F3                        mov r14b, bl
00974BA7  48 8B BC 24 B0 00 00 00         mov rdi, qword ptr [rsp + 0xb0]
00974BAF  41 80 FD 01                     cmp r13b, 1
00974BB3  75 0A                           jne 0x140974bbf
00974BB5  33 D2                           xor edx, edx
00974BB7  48 8B CF                        mov rcx, rdi
00974BBA  E8 B1 DC 20 00                  call 0x140b82870
00974BBF  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00974BC7  48 85 C9                        test rcx, rcx
00974BCA  74 07                           je 0x140974bd3
00974BCC  33 D2                           xor edx, edx
00974BCE  E8 9D DC 20 00                  call 0x140b82870
00974BD3  48 85 F6                        test rsi, rsi
00974BD6  74 0A                           je 0x140974be2
00974BD8  33 D2                           xor edx, edx
00974BDA  48 8B CE                        mov rcx, rsi
00974BDD  E8 8E DC 20 00                  call 0x140b82870
00974BE2  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00974BEA  48 85 C9                        test rcx, rcx
00974BED  74 07                           je 0x140974bf6
00974BEF  33 D2                           xor edx, edx
00974BF1  E8 7A DC 20 00                  call 0x140b82870
00974BF6  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00974BFE  48 85 C9                        test rcx, rcx
00974C01  74 07                           je 0x140974c0a
00974C03  33 D2                           xor edx, edx
00974C05  E8 66 DC 20 00                  call 0x140b82870
00974C0A  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00974C12  E8 39 47 98 FF                  call 0x1402f9350
00974C17  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00974C1F  E8 EC 6A EF FF                  call 0x14086b710
00974C24  90                              nop
00974C25  45 88 34 24                     mov byte ptr [r12], r14b
00974C29  EB 02                           jmp 0x140974c2d
00974C2B  EB 02                           jmp 0x140974c2f
00974C2D  33 C0                           xor eax, eax
00974C2F  48 81 C4 20 01 00 00            add rsp, 0x120
00974C36  41 5F                           pop r15
00974C38  41 5E                           pop r14
00974C3A  41 5D                           pop r13
00974C3C  41 5C                           pop r12
00974C3E  5F                              pop rdi
00974C3F  5E                              pop rsi
00974C40  5B                              pop rbx
00974C41  C3                              ret
00974C42  CC                              int3
00974C43  48 8B CF                        mov rcx, rdi
00974C46  E8 05 47 98 FF                  call 0x1402f9350
00974C4B  BB A5 00 00 C0                  mov ebx, 0xc00000a5
00974C50  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00974C58  E8 B3 6A EF FF                  call 0x14086b710
00974C5D  8B C3                           mov eax, ebx
00974C5F  EB CE                           jmp 0x140974c2f
00974C61  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00974C69  48 85 C9                        test rcx, rcx
00974C6C  0F 85 67 01 00 00               jne 0x140974dd9
00974C72  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00974C7A  48 85 C9                        test rcx, rcx
00974C7D  0F 85 62 01 00 00               jne 0x140974de5
00974C83  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00974C8B  48 85 C9                        test rcx, rcx
00974C8E  0F 85 5D 01 00 00               jne 0x140974df1
00974C94  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00974C9C  48 85 C9                        test rcx, rcx
00974C9F  0F 85 58 01 00 00               jne 0x140974dfd
00974CA5  45 33 C0                        xor r8d, r8d
00974CA8  41 8A D5                        mov dl, r13b
00974CAB  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00974CB3  E8 D8 04 00 00                  call 0x140975190
00974CB8  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00974CC0  E8 8B 46 98 FF                  call 0x1402f9350
00974CC5  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00974CCD  E8 3E 6A EF FF                  call 0x14086b710
00974CD2  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00974CD7  3B FB                           cmp edi, ebx
00974CD9  75 07                           jne 0x140974ce2
00974CDB  8B CB                           mov ecx, ebx
00974CDD  E8 3E A1 EF FF                  call 0x14086ee20
00974CE2  8B C7                           mov eax, edi
00974CE4  E9 46 FF FF FF                  jmp 0x140974c2f
00974CE9  44 8A B4 24 A0 00 00 00         mov r14b, byte ptr [rsp + 0xa0]
00974CF1  E9 B9 FE FF FF                  jmp 0x140974baf
00974CF6  48 8B CF                        mov rcx, rdi
00974CF9  E8 52 46 98 FF                  call 0x1402f9350
00974CFE  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00974D06  E8 05 6A EF FF                  call 0x14086b710
00974D0B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00974D10  3B F3                           cmp esi, ebx
00974D12  75 07                           jne 0x140974d1b
00974D14  8B CB                           mov ecx, ebx
00974D16  E8 05 A1 EF FF                  call 0x14086ee20
00974D1B  8B C6                           mov eax, esi
00974D1D  E9 0D FF FF FF                  jmp 0x140974c2f
00974D22  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00974D26  0F B7 C8                        movzx ecx, ax
00974D29  66 83 E1 10                     and cx, 0x10
00974D2D  0F 85 D6 00 00 00               jne 0x140974e09
00974D33  48 8B D3                        mov rdx, rbx
00974D36  66 85 C9                        test cx, cx
00974D39  0F 85 E6 00 00 00               jne 0x140974e25
00974D3F  48 8B CB                        mov rcx, rbx
00974D42  44 8B 8C 24 90 01 00 00         mov r9d, dword ptr [rsp + 0x190]
00974D4A  44 0B 8C 24 98 01 00 00         or r9d, dword ptr [rsp + 0x198]
00974D52  48 8D 84 24 A2 00 00 00         lea rax, [rsp + 0xa2]
00974D5A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00974D5F  48 8D 84 24 A1 00 00 00         lea rax, [rsp + 0xa1]
00974D67  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00974D6C  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
00974D71  4C 8B 84 24 B8 00 00 00         mov r8, qword ptr [rsp + 0xb8]
00974D79  E8 B2 EC FF FF                  call 0x140973a30
00974D7E  38 9C 24 A1 00 00 00            cmp byte ptr [rsp + 0xa1], bl
00974D85  0F 85 C5 4A 1B 00               jne 0x140b29850
00974D8B  38 9C 24 A2 00 00 00            cmp byte ptr [rsp + 0xa2], bl
00974D92  0F 84 65 FD FF FF               je 0x140974afd
00974D98  E9 B3 4A 1B 00                  jmp 0x140b29850
00974D9D  BB 61 00 00 C0                  mov ebx, 0xc0000061
00974DA2  E9 A9 FE FF FF                  jmp 0x140974c50
00974DA7  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00974DAF  E8 5C 69 EF FF                  call 0x14086b710
00974DB4  81 FF 08 00 00 C0               cmp edi, 0xc0000008
00974DBA  0F 84 22 FF FF FF               je 0x140974ce2
00974DC0  8B CF                           mov ecx, edi
00974DC2  E9 16 FF FF FF                  jmp 0x140974cdd
00974DC7  48 8B CF                        mov rcx, rdi
00974DCA  E8 81 45 98 FF                  call 0x1402f9350
00974DCF  BB 79 00 00 C0                  mov ebx, 0xc0000079
00974DD4  E9 77 FE FF FF                  jmp 0x140974c50
00974DD9  33 D2                           xor edx, edx
00974DDB  E8 90 DA 20 00                  call 0x140b82870
00974DE0  E9 8D FE FF FF                  jmp 0x140974c72
00974DE5  33 D2                           xor edx, edx
00974DE7  E8 84 DA 20 00                  call 0x140b82870
00974DEC  E9 92 FE FF FF                  jmp 0x140974c83
00974DF1  33 D2                           xor edx, edx
00974DF3  E8 78 DA 20 00                  call 0x140b82870
00974DF8  E9 97 FE FF FF                  jmp 0x140974c94
00974DFD  33 D2                           xor edx, edx
00974DFF  E8 6C DA 20 00                  call 0x140b82870
00974E04  E9 9C FE FF FF                  jmp 0x140974ca5
00974E09  66 85 C0                        test ax, ax
00974E0C  0F 89 2C 4A 1B 00               jns 0x140b2983e
00974E12  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
00974E15  85 D2                           test edx, edx
00974E17  0F 84 16 FF FF FF               je 0x140974d33
00974E1D  48 03 D7                        add rdx, rdi
00974E20  E9 11 FF FF FF                  jmp 0x140974d36
00974E25  66 85 C0                        test ax, ax
00974E28  0F 89 19 4A 1B 00               jns 0x140b29847
00974E2E  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
00974E31  85 C0                           test eax, eax
00974E33  0F 84 06 FF FF FF               je 0x140974d3f
00974E39  48 8D 0C 07                     lea rcx, [rdi + rax]
00974E3D  E9 00 FF FF FF                  jmp 0x140974d42
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtOpenObjectAuditAlarm(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, __int64 a9, __int64 a10, unsigned __int8 a11, __int64 a12)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int8 v_stack_mB5;
    unsigned __int8 v_stack_mB6;
    unsigned __int8 v_stack_mB7;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p48;
    unsigned __int8 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_pA0;
    unsigned __int64 v_stack_pA1;
    unsigned __int64 v_stack_pA2;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pF8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (288);
    v_stack_m78 = a2;
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 144) = 0;
    *(unsigned __int64 *)(v_rsp - 152) = 0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    *(unsigned __int64 *)(v_rsp - 168) = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_mB8 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    *(unsigned __int8 *)(v_rsp - 183) = 0;
    *(unsigned __int8 *)(v_rsp - 182) = 0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    *(unsigned __int16 *)(v_rsp - 172) = 0;
    v_stack_mB5 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = SeCaptureSubjectContext(v_stack_m60, a2, a3, a4);
    result = SeCheckAuditPrivilege(v_stack_m60, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00974D9D;
    v_stack_mA0 = 0;
    v_stack_m130 = 0;
    v_stack_m138 = v_stack_mA0;
    result = ObReferenceObjectByHandle(a6, v_rbx + 8, *(unsigned __int64 *)(v_rip + 6699097), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00974DA7;
    if ((*(unsigned int *)(v_stack_mA0 + 192)) != 2) goto loc_0097481C;
    if ((*(unsigned int *)(v_stack_mA0 + 196)) < 1) goto loc_00974C43;
loc_0097481C:
    if (a5 == 0) goto loc_00974DC7;
    v_stack_m138 = v_stack_mA8;
    a4 = 0;
    result = SeCaptureSecurityDescriptor(a5, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4 + 1, a4);
    v_stack_mB0 = (unsigned int)(result);
    if (sign_flag) goto loc_00974CF6;
    if (v_stack_mA8 == 0) goto loc_00974CF6;
    if (a11 == 0) goto loc_009749C8;
    if (a9 == 0) goto loc_009749C8;
    if ((((unsigned __int8)(a9)) & (3)) != 0) goto loc_00974940;
    result = v_stack_mA0;
    if (a9 < v_stack_mA0) { result = a9; }
    v_stack_m6C = (unsigned int)((unsigned int)(*(unsigned int *)(a9)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a9)))) >= 67) goto loc_009749D7;
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(a9)) + (unsigned int)(*(unsigned int *)(a9)) * 2 * 4 + 8);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a9)) + (unsigned int)(*(unsigned int *)(a9)) * 2 * 4 + 8) == 0) goto loc_009748E2;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a9)) + (unsigned int)(*(unsigned int *)(a9)) * 2 * 4 + 8))) + (a9);
    if (a2 > v_stack_mA0) goto loc_009749ED;
    if (a2 < a9) goto loc_009749ED;
loc_009748E2:
    v_stack_m40 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a9)) + (unsigned int)(*(unsigned int *)(a9)) * 2 * 4 + 8));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a9)) + (unsigned int)(*(unsigned int *)(a9)) * 2 * 4 + 8)), (unsigned int)(0x72506553ULL), a4);
    v_stack_m80 = result;
    if (result == 0) goto loc_00974A02;
    result = memcpy(result, a9, v_stack_m40, a4);
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(a9)));
loc_00974931:
    if (v_stack_m78 == 0) goto loc_00974946;
    if ((((unsigned __int8)(v_stack_m78)) & (7)) == 0) goto loc_00974A49;
loc_00974940:
    result = ExRaiseDatatypeMisalignment(result, a9, v_stack_m40, a4);
loc_00974946:
    v_rdi = v_stack_mA0;
    if (a12 < v_stack_mA0) { v_rdi = a12; }
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi));
    result = SepProbeAndCaptureString_U(v_stack_p8, v_stack_m90, v_stack_m40, a4);
    v_stack_mB0 = (unsigned int)(result);
    if (sign_flag) goto loc_00974A67;
    result = SepProbeAndCaptureString_U(v_stack_p18, v_stack_m98, v_stack_m40, a4);
    v_stack_mB0 = (unsigned int)(result);
    if (sign_flag) goto loc_00974A67;
    result = SepProbeAndCaptureString_U(v_stack_p20, v_stack_m88, v_stack_m40, a4);
    v_stack_mB0 = (unsigned int)(result);
    goto loc_00974A67;
loc_009749C8:
    goto loc_00974931;
loc_009749D7:
    v_stack_mB0 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00974A67;
loc_009749ED:
    goto loc_009748E2;
loc_00974A02:
    a3 = 0;
    result = SeReleaseSecurityDescriptor(v_stack_mA8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    result = ObfDereferenceObject(v_stack_mA0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    result = SeReleaseSubjectContext(v_stack_m60, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    v_stack_mB0 = (unsigned int)((unsigned int)(0xC000009AULL));
    result = SepAuditFailed((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    goto loc_00974C2F;
loc_00974A49:
    result = (unsigned int)(0xC000000DULL);
    if (a12 < ((unsigned int)(0xC000000DULL))) { result = a12; }
    v_stack_m68 = *(unsigned __int64 *)(a12);
    goto loc_00974946;
loc_00974A67:
    goto loc_00974AAB;
loc_00974AAB:
    if (sign_flag) goto loc_00974C61;
    a4 = (a11 == 0) ? 1 : 0;
    v_stack_m128 = v_stack_mAC;
    v_stack_m130 = (unsigned __int8)((unsigned int)(0xC000009AULL));
    v_stack_m138 = v_stack_m60;
    a1 = 0;
    result = SepAdtAuditObjectAccessWithContext(a1, v_stack_m98, a11, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00974D22;
loc_00974AFD:
    if (v_stack_mB7 != ((unsigned __int8)((unsigned int)(0xC000009AULL)))) goto loc_00974CE9;
    if (v_stack_mB6 != ((unsigned __int8)((unsigned int)(0xC000009AULL)))) goto loc_00974CE9;
    if (a9 == 0) goto loc_00974CE9;
    if (a11 == 0) goto loc_00974CE9;
    v_stack_m110 = a11;
    v_stack_m118 = v_stack_m80;
    v_stack_m120 = (unsigned int)((unsigned int)(a7));
    v_stack_m128 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464);
    v_stack_m130 = v_stack_m50;
    v_stack_m138 = v_stack_mA0;
    result = SepAdtPrivilegeObjectAuditAlarm(v_stack_m90, v_stack_m98, v_stack_m88, v_stack_m68);
loc_00974BAF:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) == 1) {
        a2 = 0;
        a1 = v_stack_mA8;
        result = ExFreePoolWithTag(a1, a2, v_stack_m88, v_stack_m68);
    }
    if (v_stack_m90 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m90, a2, v_stack_m88, v_stack_m68);
    }
    if (v_stack_m98 != 0) {
        a2 = 0;
        a1 = v_stack_m98;
        result = ExFreePoolWithTag(a1, a2, v_stack_m88, v_stack_m68);
    }
    if (v_stack_m88 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m88, a2, v_stack_m88, v_stack_m68);
    }
    if (v_stack_m80 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m80, a2, v_stack_m88, v_stack_m68);
    }
    result = ObfDereferenceObject(v_stack_mA0, a2, v_stack_m88, v_stack_m68);
    result = SeReleaseSubjectContext(v_stack_m60, a2, v_stack_m88, v_stack_m68);
    *(unsigned __int8 *)(a12) = (unsigned __int8)((unsigned __int8)((unsigned int)(0xC000009AULL)));
    goto loc_00974C2D;
loc_00974C2D:
    result = 0;
loc_00974C2F:
    v_rsp = (v_rsp) + (288);
    return result;
loc_00974C43:
    result = ObfDereferenceObject(v_stack_mA8, a2, v_stack_m88, v_stack_m68);
loc_00974C50:
    result = SeReleaseSubjectContext(v_stack_pF8, a2, v_stack_m88, v_stack_m68);
    goto loc_00974C2F;
loc_00974C61:
    if (v_stack_pC8 != 0) goto loc_00974DD9;
loc_00974C72:
    if (v_stack_pC0 != 0) goto loc_00974DE5;
loc_00974C83:
    if (v_stack_pD0 != 0) goto loc_00974DF1;
loc_00974C94:
    if (v_stack_pD8 != 0) goto loc_00974DFD;
loc_00974CA5:
    a3 = 0;
    result = SeReleaseSecurityDescriptor(v_stack_pB0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_m68);
    result = ObfDereferenceObject(v_stack_pB8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_m68);
    result = SeReleaseSubjectContext(v_stack_pF8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_m68);
    if (((unsigned int)(v_stack_mA8)) != ((unsigned int)((unsigned int)(0xC000009AULL)))) goto loc_00974CE2;
loc_00974CDD:
    result = SepAuditFailed((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_m68);
loc_00974CE2:
    goto loc_00974C2F;
loc_00974CE9:
    goto loc_00974BAF;
loc_00974CF6:
    result = ObfDereferenceObject(v_stack_mA8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_m68);
    result = SeReleaseSubjectContext(v_stack_pF8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_m68);
    if (((unsigned int)(v_stack_m98)) == ((unsigned int)((unsigned int)(0xC000009AULL)))) {
        a1 = (unsigned int)((unsigned int)(0xC000009AULL));
        result = SepAuditFailed(a1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_m68);
    }
    goto loc_00974C2F;
loc_00974D22:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_mA8 + 2))) & (16));
    if (condition_is_not_equal) goto loc_00974E09;
loc_00974D33:
loc_00974D36:
    if ((unsigned __int16)(a1) != 0) goto loc_00974E25;
loc_00974D3F:
loc_00974D42:
    a4 = (unsigned int)(((unsigned int)(a7)) | (a8));
    v_stack_p30 = v_stack_pA2;
    v_stack_p28 = v_stack_pA1;
    v_stack_p20 = a11;
    result = SeExamineSacl((unsigned int)(0xC000009AULL), (unsigned int)(0xC000009AULL), v_stack_pB8, a4);
    if (v_stack_pA2 == ((unsigned __int8)((unsigned int)(0xC000009AULL)))) goto loc_00974AFD;
loc_00974D9D:
    goto loc_00974C50;
loc_00974DA7:
    result = SeReleaseSubjectContext(v_stack_pF8, (unsigned int)(0xC000009AULL), v_stack_pB8, a4);
    if (((unsigned int)(v_stack_mA8)) == 0xC0000008ULL) goto loc_00974CE2;
    goto loc_00974CDD;
loc_00974DC7:
    result = ObfDereferenceObject(v_stack_mA8, (unsigned int)(0xC000009AULL), v_stack_pB8, a4);
    goto loc_00974C50;
loc_00974DD9:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mA8, a2, v_stack_pB8, a4);
    goto loc_00974C72;
loc_00974DE5:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mA8, a2, v_stack_pB8, a4);
    goto loc_00974C83;
loc_00974DF1:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mA8, a2, v_stack_pB8, a4);
    goto loc_00974C94;
loc_00974DFD:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mA8, a2, v_stack_pB8, a4);
    goto loc_00974CA5;
loc_00974E09:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA8 + 12))) == 0) goto loc_00974D33;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_mA8 + 12))) + (v_stack_mA8);
    goto loc_00974D36;
loc_00974E25:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA8 + 12))) == 0) goto loc_00974D3F;
    goto loc_00974D42;
}
```

## 5. (Beta) C Style

```c
int64_t NtOpenObjectAuditAlarm(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, uint32_t Arg8, int64_t Arg9, uint64_t Arg10, uint8_t Arg11, int64_t Arg12)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint8_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint8_t v_stack_mB5;
    uint8_t v_stack_mB6;
    uint8_t v_stack_mB7;
    uint8_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p48;
    uint8_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;
    uint8_t v_stack_pA0;
    uint64_t v_stack_pA1;
    uint64_t v_stack_pA2;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pF8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (288);
    v_stack_m78 = Arg2;
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x90) = 0;
    *(uint64_t *)(local_rsp - 0x98) = 0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    *(uint64_t *)(local_rsp - 0xA8) = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_mB8 = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    *(uint8_t *)(local_rsp - 0xB7) = 0;
    *(uint8_t *)(local_rsp - 0xB6) = 0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    *(uint16_t *)(local_rsp - 0xAC) = 0;
    v_stack_mB5 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = SeCaptureSubjectContext(v_stack_m60, Arg2, Arg3, Arg4);
    result = SeCheckAuditPrivilege(v_stack_m60, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00974D9D;
    v_stack_mA0 = 0;
    v_stack_m130 = 0;
    v_stack_m138 = v_stack_mA0;
    result = ObReferenceObjectByHandle(Arg6, local_rbx + 8, *(uint64_t *)(v_rip + 0x663859), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00974DA7;
    if ((*(uint32_t *)(v_stack_mA0 + 0xC0)) != 2) goto loc_0097481C;
    if ((*(uint32_t *)(v_stack_mA0 + 0xC4)) < 1) goto loc_00974C43;
loc_0097481C:
    if (Arg5 == 0) goto loc_00974DC7;
    v_stack_m138 = v_stack_mA8;
    Arg4 = 0;
    result = SeCaptureSecurityDescriptor(Arg5, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4 + 1, Arg4);
    v_stack_mB0 = (uint32_t)(result);
    if (sign_flag) goto loc_00974CF6;
    if (v_stack_mA8 == 0) goto loc_00974CF6;
    if (Arg11 == 0) goto loc_009749C8;
    if (Arg9 == 0) goto loc_009749C8;
    if ((((uint8_t)(Arg9)) & (3)) != 0) goto loc_00974940;
    result = v_stack_mA0;
    if (Arg9 < v_stack_mA0) { result = Arg9; }
    v_stack_m6C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg9)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg9)))) >= 67) goto loc_009749D7;
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg9)) + (uint32_t)(*(uint32_t *)(Arg9)) * 2 * 4 + 8);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg9)) + (uint32_t)(*(uint32_t *)(Arg9)) * 2 * 4 + 8) == 0) goto loc_009748E2;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg9)) + (uint32_t)(*(uint32_t *)(Arg9)) * 2 * 4 + 8))) + (Arg9);
    if (Arg2 > v_stack_mA0) goto loc_009749ED;
    if (Arg2 < Arg9) goto loc_009749ED;
loc_009748E2:
    v_stack_m40 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg9)) + (uint32_t)(*(uint32_t *)(Arg9)) * 2 * 4 + 8));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg9)) + (uint32_t)(*(uint32_t *)(Arg9)) * 2 * 4 + 8)), (uint32_t)(0x72506553ULL), Arg4);
    v_stack_m80 = result;
    if (result == 0) goto loc_00974A02;
    result = memcpy(result, Arg9, v_stack_m40, Arg4);
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg9)));
loc_00974931:
    if (v_stack_m78 == 0) goto loc_00974946;
    if ((((uint8_t)(v_stack_m78)) & (7)) == 0) goto loc_00974A49;
loc_00974940:
    result = ExRaiseDatatypeMisalignment(result, Arg9, v_stack_m40, Arg4);
loc_00974946:
    local_rdi = v_stack_mA0;
    if (Arg12 < v_stack_mA0) { local_rdi = Arg12; }
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rdi));
    result = SepProbeAndCaptureString_U(v_stack_p8, v_stack_m90, v_stack_m40, Arg4);
    v_stack_mB0 = (uint32_t)(result);
    if (sign_flag) goto loc_00974A67;
    result = SepProbeAndCaptureString_U(v_stack_p18, v_stack_m98, v_stack_m40, Arg4);
    v_stack_mB0 = (uint32_t)(result);
    if (sign_flag) goto loc_00974A67;
    result = SepProbeAndCaptureString_U(v_stack_p20, v_stack_m88, v_stack_m40, Arg4);
    v_stack_mB0 = (uint32_t)(result);
    goto loc_00974A67;
loc_009749C8:
    goto loc_00974931;
loc_009749D7:
    v_stack_mB0 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00974A67;
loc_009749ED:
    goto loc_009748E2;
loc_00974A02:
    Arg3 = 0;
    result = SeReleaseSecurityDescriptor(v_stack_mA8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    result = ObfDereferenceObject(v_stack_mA0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    result = SeReleaseSubjectContext(v_stack_m60, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    v_stack_mB0 = (uint32_t)((uint32_t)(0xC000009AULL));
    result = SepAuditFailed((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    goto loc_00974C2F;
loc_00974A49:
    result = (uint32_t)(0xC000000DULL);
    if (Arg12 < ((uint32_t)(0xC000000DULL))) { result = Arg12; }
    v_stack_m68 = *(uint64_t *)(Arg12);
    goto loc_00974946;
loc_00974A67:
    goto loc_00974AAB;
loc_00974AAB:
    if (sign_flag) goto loc_00974C61;
    Arg4 = (Arg11 == 0) ? 1 : 0;
    v_stack_m128 = v_stack_mAC;
    v_stack_m130 = (uint8_t)((uint32_t)(0xC000009AULL));
    v_stack_m138 = v_stack_m60;
    Arg1 = 0;
    result = SepAdtAuditObjectAccessWithContext(Arg1, v_stack_m98, Arg11, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00974D22;
loc_00974AFD:
    if (v_stack_mB7 != ((uint8_t)((uint32_t)(0xC000009AULL)))) goto loc_00974CE9;
    if (v_stack_mB6 != ((uint8_t)((uint32_t)(0xC000009AULL)))) goto loc_00974CE9;
    if (Arg9 == 0) goto loc_00974CE9;
    if (Arg11 == 0) goto loc_00974CE9;
    v_stack_m110 = Arg11;
    v_stack_m118 = v_stack_m80;
    v_stack_m120 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m128 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0);
    v_stack_m130 = v_stack_m50;
    v_stack_m138 = v_stack_mA0;
    result = SepAdtPrivilegeObjectAuditAlarm(v_stack_m90, v_stack_m98, v_stack_m88, v_stack_m68);
loc_00974BAF:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) == 1) {
        Arg2 = 0;
        Arg1 = v_stack_mA8;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m88, v_stack_m68);
    }
    if (v_stack_m90 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m90, Arg2, v_stack_m88, v_stack_m68);
    }
    if (v_stack_m98 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m98;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m88, v_stack_m68);
    }
    if (v_stack_m88 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m88, Arg2, v_stack_m88, v_stack_m68);
    }
    if (v_stack_m80 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m80, Arg2, v_stack_m88, v_stack_m68);
    }
    result = ObfDereferenceObject(v_stack_mA0, Arg2, v_stack_m88, v_stack_m68);
    result = SeReleaseSubjectContext(v_stack_m60, Arg2, v_stack_m88, v_stack_m68);
    *(uint8_t *)(Arg12) = (uint8_t)((uint8_t)((uint32_t)(0xC000009AULL)));
    goto loc_00974C2D;
loc_00974C2D:
    result = 0;
loc_00974C2F:
    local_rsp = (local_rsp) + (288);
    return result;
loc_00974C43:
    result = ObfDereferenceObject(v_stack_mA8, Arg2, v_stack_m88, v_stack_m68);
loc_00974C50:
    result = SeReleaseSubjectContext(v_stack_pF8, Arg2, v_stack_m88, v_stack_m68);
    goto loc_00974C2F;
loc_00974C61:
    if (v_stack_pC8 != 0) goto loc_00974DD9;
loc_00974C72:
    if (v_stack_pC0 != 0) goto loc_00974DE5;
loc_00974C83:
    if (v_stack_pD0 != 0) goto loc_00974DF1;
loc_00974C94:
    if (v_stack_pD8 != 0) goto loc_00974DFD;
loc_00974CA5:
    Arg3 = 0;
    result = SeReleaseSecurityDescriptor(v_stack_pB0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_m68);
    result = ObfDereferenceObject(v_stack_pB8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_m68);
    result = SeReleaseSubjectContext(v_stack_pF8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_m68);
    if (((uint32_t)(v_stack_mA8)) != ((uint32_t)((uint32_t)(0xC000009AULL)))) goto loc_00974CE2;
loc_00974CDD:
    result = SepAuditFailed((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_m68);
loc_00974CE2:
    goto loc_00974C2F;
loc_00974CE9:
    goto loc_00974BAF;
loc_00974CF6:
    result = ObfDereferenceObject(v_stack_mA8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_m68);
    result = SeReleaseSubjectContext(v_stack_pF8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_m68);
    if (((uint32_t)(v_stack_m98)) == ((uint32_t)((uint32_t)(0xC000009AULL)))) {
        Arg1 = (uint32_t)((uint32_t)(0xC000009AULL));
        result = SepAuditFailed(Arg1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_m68);
    }
    goto loc_00974C2F;
loc_00974D22:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_mA8 + 0x2))) & (16));
    if (condition_is_not_equal) goto loc_00974E09;
loc_00974D33:
loc_00974D36:
    if ((uint16_t)(Arg1) != 0) goto loc_00974E25;
loc_00974D3F:
loc_00974D42:
    Arg4 = (uint32_t)(((uint32_t)(Arg7)) | (Arg8));
    v_stack_p30 = v_stack_pA2;
    v_stack_p28 = v_stack_pA1;
    v_stack_p20 = Arg11;
    result = SeExamineSacl((uint32_t)(0xC000009AULL), (uint32_t)(0xC000009AULL), v_stack_pB8, Arg4);
    if (v_stack_pA2 == ((uint8_t)((uint32_t)(0xC000009AULL)))) goto loc_00974AFD;
loc_00974D9D:
    goto loc_00974C50;
loc_00974DA7:
    result = SeReleaseSubjectContext(v_stack_pF8, (uint32_t)(0xC000009AULL), v_stack_pB8, Arg4);
    if (((uint32_t)(v_stack_mA8)) == 0xC0000008ULL) goto loc_00974CE2;
    goto loc_00974CDD;
loc_00974DC7:
    result = ObfDereferenceObject(v_stack_mA8, (uint32_t)(0xC000009AULL), v_stack_pB8, Arg4);
    goto loc_00974C50;
loc_00974DD9:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mA8, Arg2, v_stack_pB8, Arg4);
    goto loc_00974C72;
loc_00974DE5:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mA8, Arg2, v_stack_pB8, Arg4);
    goto loc_00974C83;
loc_00974DF1:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mA8, Arg2, v_stack_pB8, Arg4);
    goto loc_00974C94;
loc_00974DFD:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mA8, Arg2, v_stack_pB8, Arg4);
    goto loc_00974CA5;
loc_00974E09:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA8 + 0xC))) == 0) goto loc_00974D33;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_mA8 + 0xC))) + (v_stack_mA8);
    goto loc_00974D36;
loc_00974E25:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA8 + 0xC))) == 0) goto loc_00974D3F;
    goto loc_00974D42;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00974700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
