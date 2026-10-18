# NtSetInformationKey

- RVA: `0x00843720`–`0x00843FDC` (길이 `2,236` bytes)
- VA: `0x0000000140843720`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000690BC`
- 디코드: `470`개 명령, `2,236/2,236` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00843794` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x008437FA` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00843819` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x00843889` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008438ED` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00843959` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008439BF` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00843A88` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00843AB9` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00843B50` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00843B6A` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00843B7C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00843B96` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x00843BA3` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x00843BB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00843C3F` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00843C56` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00843C90` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00843CC9` → [EtwpTraceRegistry](../86/EtwpTraceRegistry_function_00862980.md) (function, `0x00862980`)
- `0x00843D4B` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00843D79` → [CmpIsSystemEntity](../8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)
- `0x00843DB8` → [CmKeyBodyReplicateToVirtual](CmKeyBodyReplicateToVirtual_function_00843FE4.md) (function, `0x00843FE4`)
- `0x00843DE2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00843E15` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00843E31` → [CmKeyBodyNeedsVirtualImage](CmKeyBodyNeedsVirtualImage_function_00849864.md) (function, `0x00849864`)
- `0x00843E8A` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00843EA5` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00843EF4` → [CmSetLastWriteTimeKey](CmSetLastWriteTimeKey_function_00843368.md) (function, `0x00843368`)
- `0x00843FD2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00843735` → RVA `0x00E0A740` (`.data`; read)
- `0x00843782` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x008438B5` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x0084394C` → RVA `0x00EEFB88` (`.data`; read)
- `0x00843A0E` → RVA `0x00FD8010` (`PAGEDATA`; read)
- `0x00843A62` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00843C9A` → RVA `0x00862980` (`EtwpTraceRegistry`; read)
- `0x00843D53` → RVA `0x00E0ECA0` (`.data`; read)
- `0x00843F54` → RVA `0x00E67B90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00843794` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x008437FA` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x00843819` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x00843889` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00843959` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00843A88` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x00843AB9` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00843B6A` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00843B7C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00843B96` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x00843BA3` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x00843BB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00843C56` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00843C90` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00843DE2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00843EA5` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00843FD2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00843FAC` → [sub_00B16010](../B1/Unknown_function_00B16010.md) (`tail-transfer`)
  - `0x00843FB5` → [sub_00B16010](../B1/Unknown_function_00B16010.md) (`tail-transfer`)
  - `0x00843FBE` → [sub_00B16010](../B1/Unknown_function_00B16010.md) (`tail-transfer`)
  - `0x00843FCD` → [sub_00B16010](../B1/Unknown_function_00B16010.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00843720  4C 8B DC                        mov r11, rsp
00843723  53                              push rbx
00843724  56                              push rsi
00843725  57                              push rdi
00843726  41 54                           push r12
00843728  41 55                           push r13
0084372A  41 56                           push r14
0084372C  41 57                           push r15
0084372E  48 81 EC 70 01 00 00            sub rsp, 0x170
00843735  48 8B 05 04 70 5C 00            mov rax, qword ptr [rip + 0x5c7004]
0084373C  48 33 C4                        xor rax, rsp
0084373F  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
00843747  44 89 4C 24 68                  mov dword ptr [rsp + 0x68], r9d
0084374C  49 8B F0                        mov rsi, r8
0084374F  44 8B FA                        mov r15d, edx
00843752  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00843757  0F 57 C0                        xorps xmm0, xmm0
0084375A  33 C0                           xor eax, eax
0084375C  41 0F 11 43 88                  movups xmmword ptr [r11 - 0x78], xmm0
00843761  49 89 43 98                     mov qword ptr [r11 - 0x68], rax
00843765  33 FF                           xor edi, edi
00843767  89 BC 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edi
0084376E  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00843773  41 0F 11 43 A0                  movups xmmword ptr [r11 - 0x60], xmm0
00843778  41 0F 11 43 B0                  movups xmmword ptr [r11 - 0x50], xmm0
0084377D  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00843782  48 39 05 7F 48 79 00            cmp qword ptr [rip + 0x79487f], rax
00843789  74 0E                           je 0x140843799
0084378B  BA 00 00 02 00                  mov edx, 0x20000
00843790  49 8D 4B A0                     lea rcx, [r11 - 0x60]
00843794  E8 B7 C4 B5 FF                  call 0x14039fc50
00843799  45 32 E4                        xor r12b, r12b
0084379C  44 88 64 24 42                  mov byte ptr [rsp + 0x42], r12b
008437A1  48 8B DF                        mov rbx, rdi
008437A4  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
008437A9  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
008437AD  0F 57 C0                        xorps xmm0, xmm0
008437B0  33 C0                           xor eax, eax
008437B2  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
008437BA  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
008437C2  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
008437CA  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
008437D2  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008437DA  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
008437E2  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008437EA  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008437F2  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
008437FA  E8 71 86 BB FF                  call 0x1403fbe70
008437FF  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
00843803  45 32 F6                        xor r14b, r14b
00843806  0F 57 C0                        xorps xmm0, xmm0
00843809  0F 11 84 24 98 00 00 00         movups xmmword ptr [rsp + 0x98], xmm0
00843811  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
00843819  E8 E2 5B 38 00                  call 0x140bc9400
0084381E  44 0F B6 E8                     movzx r13d, al
00843822  88 44 24 43                     mov byte ptr [rsp + 0x43], al
00843826  84 C0                           test al, al
00843828  0F 84 DE 04 00 00               je 0x140843d0c
0084382E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00843837  44 0F B6 A0 32 02 00 00         movzx r12d, byte ptr [rax + 0x232]
0084383F  41 83 FF 01                     cmp r15d, 1
00843843  0F 85 85 03 00 00               jne 0x140843bce
00843849  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
0084384E  B9 04 00 00 00                  mov ecx, 4
00843853  39 4C 24 68                     cmp dword ptr [rsp + 0x68], ecx
00843857  0F 85 8D 04 00 00               jne 0x140843cea
0084385D  45 84 E4                        test r12b, r12b
00843860  74 1C                           je 0x14084387e
00843862  8B D1                           mov edx, ecx
00843864  48 03 D6                        add rdx, rsi
00843867  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00843871  48 3B D0                        cmp rdx, rax
00843874  77 05                           ja 0x14084387b
00843876  48 3B D6                        cmp rdx, rsi
00843879  73 03                           jae 0x14084387e
0084387B  0F B6 00                        movzx eax, byte ptr [rax]
0084387E  44 8B C1                        mov r8d, ecx
00843881  48 8B D6                        mov rdx, rsi
00843884  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00843889  E8 B2 2F E8 FF                  call 0x1406c6840
0084388E  EB 25                           jmp 0x1408438b5
00843890  8B F0                           mov esi, eax
00843892  33 FF                           xor edi, edi
00843894  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00843899  44 0F B6 6C 24 43               movzx r13d, byte ptr [rsp + 0x43]
0084389F  44 0F B6 FF                     movzx r15d, dil
008438A3  44 0F B6 E7                     movzx r12d, dil
008438A7  44 0F B6 F7                     movzx r14d, dil
008438AB  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
008438B0  E9 50 01 00 00                  jmp 0x140843a05
008438B5  4C 8B 05 04 32 78 00            mov r8, qword ptr [rip + 0x783204]
008438BC  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
008438C4  8B D7                           mov edx, edi
008438C6  B8 02 00 00 00                  mov eax, 2
008438CB  41 83 FF 05                     cmp r15d, 5
008438CF  0F 45 D0                        cmovne edx, eax
008438D2  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
008438D7  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
008438DF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008438E4  45 0F B6 CC                     movzx r9d, r12b
008438E8  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008438ED  E8 BE 54 02 00                  call 0x140868db0
008438F2  8B F0                           mov esi, eax
008438F4  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
008438FC  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00843901  48 8B C3                        mov rax, rbx
00843904  81 FE 22 00 00 C0               cmp esi, 0xc0000022
0084390A  0F 84 28 04 00 00               je 0x140843d38
00843910  32 D2                           xor dl, dl
00843912  44 0F B6 F2                     movzx r14d, dl
00843916  85 F6                           test esi, esi
00843918  0F 88 47 03 00 00               js 0x140843c65
0084391E  48 83 3D E2 46 79 00 00         cmp qword ptr [rip + 0x7946e2], 0
00843926  0F 85 A7 03 00 00               jne 0x140843cd3
0084392C  41 83 FF 05                     cmp r15d, 5
00843930  0F 85 E3 03 00 00               jne 0x140843d19
00843936  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0084393F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00843946  90                              nop
00843947  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
0084394C  83 3D 35 C2 6A 00 00            cmp dword ptr [rip + 0x6ac235], 0
00843953  0F 84 D6 05 00 00               je 0x140843f2f
00843959  E8 1E 31 C1 FF                  call 0x140456a7c
0084395E  85 C0                           test eax, eax
00843960  0F 85 C4 05 00 00               jne 0x140843f2a
00843966  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0084396B  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
00843973  44 89 BC 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r15d
0084397B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00843980  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00843988  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
0084398C  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
00843993  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
0084399B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008439A0  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
008439A5  C7 44 24 20 12 00 00 00         mov dword ptr [rsp + 0x20], 0x12
008439AD  41 B1 01                        mov r9b, 1
008439B0  45 33 C0                        xor r8d, r8d
008439B3  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
008439BB  41 8D 48 03                     lea ecx, [r8 + 3]
008439BF  E8 7C 25 02 00                  call 0x140865f40
008439C4  8B F0                           mov esi, eax
008439C6  85 C0                           test eax, eax
008439C8  0F 88 A2 02 00 00               js 0x140843c70
008439CE  C6 44 24 42 01                  mov byte ptr [rsp + 0x42], 1
008439D3  0F B6 54 24 41                  movzx edx, byte ptr [rsp + 0x41]
008439D8  84 D2                           test dl, dl
008439DA  0F 85 B7 03 00 00               jne 0x140843d97
008439E0  44 0F B6 F2                     movzx r14d, dl
008439E4  41 83 FF 05                     cmp r15d, 5
008439E8  0F 85 F2 04 00 00               jne 0x140843ee0
008439EE  0F B7 44 24 50                  movzx eax, word ptr [rsp + 0x50]
008439F3  66 89 43 32                     mov word ptr [rbx + 0x32], ax
008439F7  8B F7                           mov esi, edi
008439F9  44 0F B6 64 24 42               movzx r12d, byte ptr [rsp + 0x42]
008439FF  44 0F B6 7C 24 40               movzx r15d, byte ptr [rsp + 0x40]
00843A05  45 84 F6                        test r14b, r14b
00843A08  0F 84 95 00 00 00               je 0x140843aa3
00843A0E  83 3D FB 45 79 00 00            cmp dword ptr [rip + 0x7945fb], 0
00843A15  0F 85 1E 05 00 00               jne 0x140843f39
00843A1B  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00843A24  48 8B 92 B8 00 00 00            mov rdx, qword ptr [rdx + 0xb8]
00843A2B  0F 0D 8A 48 02 00 00            prefetchw byte ptr [rdx + 0x248]
00843A32  48 8B 82 48 02 00 00            mov rax, qword ptr [rdx + 0x248]
00843A39  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
00843A41  49 8B C8                        mov rcx, r8
00843A44  48 33 C8                        xor rcx, rax
00843A47  48 83 F9 0F                     cmp rcx, 0xf
00843A4B  0F 83 89 03 00 00               jae 0x140843dda
00843A51  48 8D 48 01                     lea rcx, [rax + 1]
00843A55  F0 48 0F B1 8A 48 02 00 00      lock cmpxchg qword ptr [rdx + 0x248], rcx
00843A5E  75 D9                           jne 0x140843a39
00843A60  8B C7                           mov eax, edi
00843A62  83 3D A7 15 78 00 00            cmp dword ptr [rip + 0x7815a7], 0
00843A69  0F 95 C0                        setne al
00843A6C  85 C0                           test eax, eax
00843A6E  74 1D                           je 0x140843a8d
00843A70  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00843A78  48 83 C1 D0                     add rcx, -0x30
00843A7C  33 D2                           xor edx, edx
00843A7E  41 B9 53 65 53 75               mov r9d, 0x75536553
00843A84  44 8D 42 01                     lea r8d, [rdx + 1]
00843A88  E8 57 CF 9C FF                  call 0x1402109e4
00843A8D  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00843A95  48 85 C9                        test rcx, rcx
00843A98  0F 85 ED 01 00 00               jne 0x140843c8b
00843A9E  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00843AA3  45 84 E4                        test r12b, r12b
00843AA6  0F 84 B0 00 00 00               je 0x140843b5c
00843AAC  83 3D D5 C0 6A 00 00            cmp dword ptr [rip + 0x6ac0d5], 0
00843AB3  0F 84 A3 00 00 00               je 0x140843b5c
00843AB9  E8 BE 2F C1 FF                  call 0x140456a7c
00843ABE  85 C0                           test eax, eax
00843AC0  0F 85 96 00 00 00               jne 0x140843b5c
00843AC6  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00843ACE  48 39 84 24 80 00 00 00         cmp qword ptr [rsp + 0x80], rax
00843AD6  0F 84 80 00 00 00               je 0x140843b5c
00843ADC  89 BC 24 04 01 00 00            mov dword ptr [rsp + 0x104], edi
00843AE3  0F 57 C0                        xorps xmm0, xmm0
00843AE6  F3 0F 7F 84 24 14 01 00 00      movdqu xmmword ptr [rsp + 0x114], xmm0
00843AEF  48 89 BC 24 24 01 00 00         mov qword ptr [rsp + 0x124], rdi
00843AF7  89 BC 24 2C 01 00 00            mov dword ptr [rsp + 0x12c], edi
00843AFE  48 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rbx
00843B06  89 B4 24 00 01 00 00            mov dword ptr [rsp + 0x100], esi
00843B0D  89 B4 24 10 01 00 00            mov dword ptr [rsp + 0x110], esi
00843B14  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00843B1C  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
00843B24  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00843B2C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00843B31  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00843B36  C7 44 24 20 12 00 00 00         mov dword ptr [rsp + 0x20], 0x12
00843B3E  45 33 C9                        xor r9d, r9d
00843B41  45 33 C0                        xor r8d, r8d
00843B44  48 8D 94 24 F8 00 00 00         lea rdx, [rsp + 0xf8]
00843B4C  41 8D 49 12                     lea ecx, [r9 + 0x12]
00843B50  E8 EB 23 02 00                  call 0x140865f40
00843B55  8B B4 24 10 01 00 00            mov esi, dword ptr [rsp + 0x110]
00843B5C  45 84 FF                        test r15b, r15b
00843B5F  74 13                           je 0x140843b74
00843B61  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00843B6A  E8 81 B4 A1 FF                  call 0x14025eff0
00843B6F  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00843B74  48 85 DB                        test rbx, rbx
00843B77  74 08                           je 0x140843b81
00843B79  48 8B CB                        mov rcx, rbx
00843B7C  E8 CF 57 AB FF                  call 0x1402f9350
00843B81  48 8B 05 80 44 79 00            mov rax, qword ptr [rip + 0x794480]
00843B88  48 85 C0                        test rax, rax
00843B8B  0F 85 09 01 00 00               jne 0x140843c9a
00843B91  45 84 ED                        test r13b, r13b
00843B94  74 05                           je 0x140843b9b
00843B96  E8 E5 5C 38 00                  call 0x140bc9880
00843B9B  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00843BA3  E8 A8 C1 BD FF                  call 0x14041fd50
00843BA8  8B C6                           mov eax, esi
00843BAA  48 8B 8C 24 68 01 00 00         mov rcx, qword ptr [rsp + 0x168]
00843BB2  48 33 CC                        xor rcx, rsp
00843BB5  E8 86 8A E6 FF                  call 0x1406ac640
00843BBA  48 81 C4 70 01 00 00            add rsp, 0x170
00843BC1  41 5F                           pop r15
00843BC3  41 5E                           pop r14
00843BC5  41 5D                           pop r13
00843BC7  41 5C                           pop r12
00843BC9  5F                              pop rdi
00843BCA  5E                              pop rsi
00843BCB  5B                              pop rbx
00843BCC  C3                              ret
00843BCD  CC                              int3
00843BCE  41 8B CF                        mov ecx, r15d
00843BD1  45 85 FF                        test r15d, r15d
00843BD4  0F 84 D5 02 00 00               je 0x140843eaf
00843BDA  83 E9 02                        sub ecx, 2
00843BDD  0F 84 BD 03 00 00               je 0x140843fa0
00843BE3  83 E9 01                        sub ecx, 1
00843BE6  0F 84 B4 03 00 00               je 0x140843fa0
00843BEC  83 E9 01                        sub ecx, 1
00843BEF  0F 84 54 FC FF FF               je 0x140843849
00843BF5  83 F9 01                        cmp ecx, 1
00843BF8  0F 84 A2 03 00 00               je 0x140843fa0
00843BFE  48 39 1D 03 44 79 00            cmp qword ptr [rip + 0x794403], rbx
00843C05  74 54                           je 0x140843c5b
00843C07  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00843C0C  48 85 C9                        test rcx, rcx
00843C0F  74 4A                           je 0x140843c5b
00843C11  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00843C1A  44 0F B6 88 32 02 00 00         movzx r9d, byte ptr [rax + 0x232]
00843C22  4C 8B 05 97 2E 78 00            mov r8, qword ptr [rip + 0x782e97]
00843C29  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00843C2E  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00843C33  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00843C38  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00843C3D  33 D2                           xor edx, edx
00843C3F  E8 6C 51 02 00                  call 0x140868db0
00843C44  85 C0                           test eax, eax
00843C46  78 13                           js 0x140843c5b
00843C48  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00843C4D  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00843C51  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00843C56  E8 F5 56 AB FF                  call 0x1402f9350
00843C5B  BE 03 00 00 C0                  mov esi, 0xc0000003
00843C60  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00843C65  45 32 E4                        xor r12b, r12b
00843C68  45 32 FF                        xor r15b, r15b
00843C6B  E9 95 FD FF FF                  jmp 0x140843a05
00843C70  44 0F B6 74 24 41               movzx r14d, byte ptr [rsp + 0x41]
00843C76  8B C7                           mov eax, edi
00843C78  81 FE 03 05 00 C0               cmp esi, 0xc0000503
00843C7E  0F 45 C6                        cmovne eax, esi
00843C81  8B F0                           mov esi, eax
00843C83  45 32 E4                        xor r12b, r12b
00843C86  E9 74 FD FF FF                  jmp 0x1408439ff
00843C8B  BA 53 65 53 75                  mov edx, 0x75536553
00843C90  E8 4B 3C AB FF                  call 0x1402f78e0
00843C95  E9 04 FE FF FF                  jmp 0x140843a9e
00843C9A  48 8D 0D DF EC 01 00            lea rcx, [rip + 0x1ecdf]
00843CA1  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00843CA6  45 33 C9                        xor r9d, r9d
00843CA9  44 8B C6                        mov r8d, esi
00843CAC  48 8D 94 24 48 01 00 00         lea rdx, [rsp + 0x148]
00843CB4  48 3B C1                        cmp rax, rcx
00843CB7  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00843CBC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00843CC1  B1 14                           mov cl, 0x14
00843CC3  0F 85 09 03 00 00               jne 0x140843fd2
00843CC9  E8 B2 EC 01 00                  call 0x140862980
00843CCE  E9 BE FE FF FF                  jmp 0x140843b91
00843CD3  48 85 C0                        test rax, rax
00843CD6  0F 84 50 FC FF FF               je 0x14084392c
00843CDC  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00843CE0  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00843CE5  E9 42 FC FF FF                  jmp 0x14084392c
00843CEA  48 39 1D 17 43 79 00            cmp qword ptr [rip + 0x794317], rbx
00843CF1  0F 85 57 01 00 00               jne 0x140843e4e
00843CF7  BE 04 00 00 C0                  mov esi, 0xc0000004
00843CFC  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00843D01  45 32 E4                        xor r12b, r12b
00843D04  45 32 FF                        xor r15b, r15b
00843D07  E9 F9 FC FF FF                  jmp 0x140843a05
00843D0C  BE 89 01 00 C0                  mov esi, 0xc0000189
00843D11  45 32 FF                        xor r15b, r15b
00843D14  E9 EC FC FF FF                  jmp 0x140843a05
00843D19  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00843D1D  8B 41 08                        mov eax, dword ptr [rcx + 8]
00843D20  84 C0                           test al, al
00843D22  0F 89 DE 01 00 00               jns 0x140843f06
00843D28  BE 22 00 00 C0                  mov esi, 0xc0000022
00843D2D  45 32 E4                        xor r12b, r12b
00843D30  45 32 FF                        xor r15b, r15b
00843D33  E9 CD FC FF FF                  jmp 0x140843a05
00843D38  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
00843D3D  0F 84 7B 01 00 00               je 0x140843ebe
00843D43  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
00843D4B  E8 D0 7A 02 00                  call 0x14086b820
00843D50  41 B6 01                        mov r14b, 1
00843D53  80 3D 46 AF 5C 00 00            cmp byte ptr [rip + 0x5caf46], 0
00843D5A  74 2B                           je 0x140843d87
00843D5C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00843D65  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
00843D6C  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00843D71  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
00843D79  E8 12 11 07 00                  call 0x1408b4e90
00843D7E  84 C0                           test al, al
00843D80  74 6A                           je 0x140843dec
00843D82  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00843D87  BE 22 00 00 C0                  mov esi, 0xc0000022
00843D8C  45 32 E4                        xor r12b, r12b
00843D8F  45 32 FF                        xor r15b, r15b
00843D92  E9 6E FC FF FF                  jmp 0x140843a05
00843D97  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00843D9C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00843DA1  4C 8D 8C 24 98 00 00 00         lea r9, [rsp + 0x98]
00843DA9  41 B8 02 00 00 00               mov r8d, 2
00843DAF  41 0F B6 D4                     movzx edx, r12b
00843DB3  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00843DB8  E8 27 02 00 00                  call 0x140843fe4
00843DBD  8B F0                           mov esi, eax
00843DBF  0F B6 54 24 41                  movzx edx, byte ptr [rsp + 0x41]
00843DC4  44 0F B6 F2                     movzx r14d, dl
00843DC8  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00843DCD  85 C0                           test eax, eax
00843DCF  0F 88 24 FC FF FF               js 0x1408439f9
00843DD5  E9 06 FC FF FF                  jmp 0x1408439e0
00843DDA  BA 53 65 53 75                  mov edx, 0x75536553
00843DDF  49 8B C8                        mov rcx, r8
00843DE2  E8 F9 3A AB FF                  call 0x1402f78e0
00843DE7  E9 A1 FC FF FF                  jmp 0x140843a8d
00843DEC  4C 8B 05 CD 2C 78 00            mov r8, qword ptr [rip + 0x782ccd]
00843DF3  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00843DF8  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00843DFD  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00843E02  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00843E07  45 0F B6 CC                     movzx r9d, r12b
00843E0B  BA 19 00 02 00                  mov edx, 0x20019
00843E10  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00843E15  E8 96 4F 02 00                  call 0x140868db0
00843E1A  8B F0                           mov esi, eax
00843E1C  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00843E21  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00843E26  85 C0                           test eax, eax
00843E28  0F 88 37 FE FF FF               js 0x140843c65
00843E2E  48 8B CB                        mov rcx, rbx
00843E31  E8 2E 5A 00 00                  call 0x140849864
00843E36  84 C0                           test al, al
00843E38  0F 85 90 00 00 00               jne 0x140843ece
00843E3E  BE 22 00 00 C0                  mov esi, 0xc0000022
00843E43  45 32 E4                        xor r12b, r12b
00843E46  45 32 FF                        xor r15b, r15b
00843E49  E9 B7 FB FF FF                  jmp 0x140843a05
00843E4E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00843E53  48 85 C9                        test rcx, rcx
00843E56  0F 84 9B FE FF FF               je 0x140843cf7
00843E5C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00843E65  44 0F B6 88 32 02 00 00         movzx r9d, byte ptr [rax + 0x232]
00843E6D  4C 8B 05 4C 2C 78 00            mov r8, qword ptr [rip + 0x782c4c]
00843E74  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00843E79  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00843E7E  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00843E83  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00843E88  33 D2                           xor edx, edx
00843E8A  E8 21 4F 02 00                  call 0x140868db0
00843E8F  85 C0                           test eax, eax
00843E91  0F 88 60 FE FF FF               js 0x140843cf7
00843E97  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00843E9C  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00843EA0  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00843EA5  E8 A6 54 AB FF                  call 0x1402f9350
00843EAA  E9 48 FE FF FF                  jmp 0x140843cf7
00843EAF  B9 08 00 00 00                  mov ecx, 8
00843EB4  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00843EB9  E9 95 F9 FF FF                  jmp 0x140843853
00843EBE  BE 22 00 00 C0                  mov esi, 0xc0000022
00843EC3  45 32 E4                        xor r12b, r12b
00843EC6  45 32 FF                        xor r15b, r15b
00843EC9  E9 37 FB FF FF                  jmp 0x140843a05
00843ECE  8B F7                           mov esi, edi
00843ED0  41 0F B6 D6                     movzx edx, r14b
00843ED4  88 54 24 41                     mov byte ptr [rsp + 0x41], dl
00843ED8  48 8B C3                        mov rax, rbx
00843EDB  E9 32 FA FF FF                  jmp 0x140843912
00843EE0  41 8B CF                        mov ecx, r15d
00843EE3  45 85 FF                        test r15d, r15d
00843EE6  0F 85 BD 00 00 00               jne 0x140843fa9
00843EEC  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00843EF1  48 8B CB                        mov rcx, rbx
00843EF4  E8 6F F4 FF FF                  call 0x140843368
00843EF9  8B F0                           mov esi, eax
00843EFB  44 0F B6 74 24 41               movzx r14d, byte ptr [rsp + 0x41]
00843F01  E9 F3 FA FF FF                  jmp 0x1408439f9
00843F06  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
00843F0A  F7 80 A0 00 00 00 00 00 10 00   test dword ptr [rax + 0xa0], 0x100000
00843F14  0F 84 1C FA FF FF               je 0x140843936
00843F1A  BE 22 00 00 C0                  mov esi, 0xc0000022
00843F1F  45 32 E4                        xor r12b, r12b
00843F22  45 32 FF                        xor r15b, r15b
00843F25  E9 DB FA FF FF                  jmp 0x140843a05
00843F2A  0F B6 54 24 41                  movzx edx, byte ptr [rsp + 0x41]
00843F2F  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00843F34  E9 9F FA FF FF                  jmp 0x1408439d8
00843F39  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00843F41  48 85 C0                        test rax, rax
00843F44  74 20                           je 0x140843f66
00843F46  48 8B 80 78 04 00 00            mov rax, qword ptr [rax + 0x478]
00843F4D  F0 FF 88 1C 01 00 00            lock dec dword ptr [rax + 0x11c]
00843F54  48 8B 05 35 3C 62 00            mov rax, qword ptr [rip + 0x623c35]
00843F5B  48 39 84 24 A8 00 00 00         cmp qword ptr [rsp + 0xa8], rax
00843F63  75 01                           jne 0x140843f66
00843F65  CC                              int3
00843F66  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00843F6E  48 85 C0                        test rax, rax
00843F71  0F 84 A4 FA FF FF               je 0x140843a1b
00843F77  48 8B 80 78 04 00 00            mov rax, qword ptr [rax + 0x478]
00843F7E  F0 FF 88 1C 01 00 00            lock dec dword ptr [rax + 0x11c]
00843F85  48 8B 05 04 3C 62 00            mov rax, qword ptr [rip + 0x623c04]
00843F8C  48 39 84 24 98 00 00 00         cmp qword ptr [rsp + 0x98], rax
00843F94  0F 85 81 FA FF FF               jne 0x140843a1b
00843F9A  CC                              int3
00843F9B  E9 7B FA FF FF                  jmp 0x140843a1b
00843FA0  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
00843FA4  E9 A5 F8 FF FF                  jmp 0x14084384e
00843FA9  83 E9 01                        sub ecx, 1
00843FAC  0F 84 5E 20 2D 00               je 0x140b16010
00843FB2  83 E9 01                        sub ecx, 1
00843FB5  0F 84 55 20 2D 00               je 0x140b16010
00843FBB  83 E9 01                        sub ecx, 1
00843FBE  0F 84 4C 20 2D 00               je 0x140b16010
00843FC4  83 F9 01                        cmp ecx, 1
00843FC7  0F 85 2C FA FF FF               jne 0x1408439f9
00843FCD  E9 3E 20 2D 00                  jmp 0x140b16010
00843FD2  E8 F9 6A E7 FF                  call 0x1406baad0
00843FD7  E9 B5 FB FF FF                  jmp 0x140843b91
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetInformationKey(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int8 v_stack_m165;
    unsigned __int8 v_stack_m166;
    unsigned __int8 v_stack_m167;
    unsigned __int8 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m84;
    unsigned __int64 v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_p148;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;

    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 6057988)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m140 = a4;
    v_stack_m150 = a1;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    v_rdi = 0;
    v_stack_mF0 = 0;
    v_stack_m158 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    v_stack_m148 = 0;
    if ((*(unsigned __int64 *)(v_rip + 7948415)) != 0) {
        a2 = 0x20000ULL;
        a1 = v_rsp - 96;
        result = EtwGetKernelTraceTimestamp(a1, a2, a3, a4);
    }
    v_r12 = 0;
    v_stack_m166 = 0;
    v_stack_m160 = 0;
    v_stack_m167 = 0;
    result = 0;
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_m120 = v_stack_m128;
    v_stack_m128 = v_stack_m128;
    result = CmpInitializeThreadInfo(v_stack_m78, a2, a3, a4);
    v_stack_m138 = 0;
    v_r14 = 0;
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    result = CmpAcquireShutdownRundown(v_stack_m78, a2, a3, a4);
    v_stack_m165 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00843D0C;
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_00843BCE;
loc_00843849:
    v_stack_m168 = 1;
loc_0084384E:
loc_00843853:
    if (v_stack_m140 != 4) goto loc_00843CEA;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_0084387E;
    a2 = (4) + (a3);
    if (a2 > (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0084387B;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (a2 < a3) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)));
    }
    result = memcpy(v_stack_m158, a3, 4, a4);
    goto loc_008438B5;
loc_008438B5:
    v_stack_m118 = 0;
    a2 = 0;
    if (((unsigned int)((unsigned int)(a2))) != 5) { a2 = 2; }
    v_stack_m180 = 0;
    v_stack_m188 = v_stack_m118;
    result = ObReferenceObjectByHandle(v_stack_m150, a2, *(unsigned __int64 *)(v_rip + 7877124), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m160 = v_stack_m118;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000022ULL) goto loc_00843D38;
    a2 = 0;
loc_00843912:
    if (sign_flag) goto loc_00843C65;
    if ((*(unsigned __int64 *)(v_rip + 7948002)) != 0) goto loc_00843CD3;
loc_0084392C:
    if (((unsigned int)((unsigned int)(a2))) != 5) goto loc_00843D19;
loc_00843936:
    v_stack_m168 = 1;
    if ((*(unsigned int *)(v_rip + 6996533)) == 0) goto loc_00843F2F;
    result = CmpIsRegistryLockAcquired(v_stack_m150, a2, *(unsigned __int64 *)(v_rip + 7877124), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned int)(result) != 0) goto loc_00843F2A;
    v_stack_mE8 = v_stack_m160;
    v_stack_mE0 = (unsigned int)((unsigned int)(a2));
    v_stack_mD8 = v_stack_m158;
    v_stack_mD0 = (unsigned int)((unsigned int)(v_stack_m140));
    v_stack_m178 = v_stack_m128;
    v_stack_m180 = v_stack_m160;
    v_stack_m188 = 18;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 3, v_stack_mE8, a3, 1);
    if (sign_flag) goto loc_00843C70;
    v_stack_m166 = 1;
loc_008439D8:
    if ((unsigned __int8)(v_stack_m167) != 0) goto loc_00843D97;
loc_008439E0:
    if (((unsigned int)((unsigned int)(a2))) != 5) goto loc_00843EE0;
    *(unsigned __int16 *)(v_stack_m160 + 50) = (unsigned __int16)(v_stack_m158);
loc_008439F9:
loc_008439FF:
loc_00843A05:
    if ((unsigned __int8)((unsigned __int8)(v_stack_m167)) == 0) goto loc_00843AA3;
    if ((*(unsigned int *)(v_rip + 7947771)) != 0) goto loc_00843F39;
loc_00843A1B:
loc_00843A39:
    a1 = (v_stack_m100) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 584));
    if (a1 >= 15) goto loc_00843DDA;
    if (a1 != 15) goto loc_00843A39;
    result = ((*(unsigned int *)(v_rip + 7869863)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a1 = v_stack_m100;
        a1 = (a1) + (-48);
        a2 = 0;
        a4 = 0x75536553ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    if (v_stack_m110 != 0) goto loc_00843C8B;
loc_00843A9E:
loc_00843AA3:
    if ((unsigned __int8)(v_stack_m166) == 0) goto loc_00843B5C;
    if ((*(unsigned int *)(v_rip + 6996181)) == 0) goto loc_00843B5C;
    result = CmpIsRegistryLockAcquired(v_stack_m110, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00843B5C;
    result = v_stack_m128;
    v_rsi = 0;
    if (v_stack_m128 != v_stack_m128) {
        v_stack_mA4 = 0;
        v_stack_m94 = v_xmm0;
        v_stack_m84 = 0;
        v_stack_m7C = 0;
        v_stack_mB0 = v_stack_m160;
        v_stack_mA8 = 0;
        v_stack_m98 = 0;
        result = v_stack_mE8;
        v_stack_mA0 = result;
        result = v_stack_m128;
        v_stack_m178 = result;
        v_stack_m180 = v_stack_m160;
        v_stack_m188 = 18;
        a4 = 0;
        a3 = 0;
        a2 = v_stack_mB0;
        a1 = a4 + 18;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rsi = v_stack_m98;
    }
    v_rbx = v_stack_m160;
    if ((unsigned __int8)(v_stack_m168) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, a3, a4);
        v_rbx = v_stack_m160;
    }
    if (v_rbx != 0) {
        a1 = v_rbx;
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rip + 7947392) != 0) goto loc_00843C9A;
loc_00843B91:
    result = *(unsigned __int64 *)(v_rip + 7947392);
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        result = CmpReleaseShutdownRundown(a1, a2, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m78, a2, a3, a4);
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (368);
    return result;
loc_00843BCE:
    if ((unsigned int)(v_stack_m168) == 0) goto loc_00843EAF;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m168))) - (2));
    if (condition_is_equal) goto loc_00843FA0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00843FA0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00843849;
    if (((unsigned int)(a1)) == 1) goto loc_00843FA0;
    if ((*(unsigned __int64 *)(v_rip + 7947267)) == v_rbx) goto loc_00843C5B;
    if (v_stack_p58 == 0) goto loc_00843C5B;
    v_stack_p58 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p58;
    a2 = 0;
    result = ObReferenceObjectByHandle(v_stack_p58, a2, *(unsigned __int64 *)(v_rip + 7876247), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (!(sign_flag)) {
        a1 = v_stack_p58;
        result = *(unsigned __int64 *)(a1 + 8);
        v_stack_p60 = result;
        result = ObfDereferenceObject(a1, a2, *(unsigned __int64 *)(v_rip + 7876247), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    }
loc_00843C65:
    v_r12 = 0;
    v_r15 = 0;
    goto loc_00843A05;
loc_00843C70:
    result = 0;
    if (((unsigned int)((unsigned int)(0xC0000003ULL))) != 0xC0000503ULL) { result = (unsigned int)((unsigned int)(0xC0000003ULL)); }
    v_r12 = 0;
    goto loc_008439FF;
loc_00843C8B:
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x75536553ULL), *(unsigned __int64 *)(v_rip + 7876247), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    goto loc_00843A9E;
loc_00843C9A:
    v_stack_p28 = 0;
    a4 = 0;
    v_stack_p20 = v_stack_p60;
    if (result != (v_rip + 126175)) goto loc_00843FD2;
    result = EtwpTraceRegistry(20, v_stack_p148, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    goto loc_00843B91;
loc_00843CD3:
    if (result == 0) goto loc_0084392C;
    v_stack_p60 = *(unsigned __int64 *)(v_stack_p48 + 8);
    goto loc_0084392C;
loc_00843CEA:
    if ((*(unsigned __int64 *)(v_rip + 7947031)) != v_stack_p48) goto loc_00843E4E;
loc_00843CF7:
    v_r12 = 0;
    v_r15 = 0;
    goto loc_00843A05;
loc_00843D0C:
    v_r15 = 0;
    goto loc_00843A05;
loc_00843D19:
    if (!sign_flag) goto loc_00843F06;
    v_r12 = 0;
    v_r15 = 0;
    goto loc_00843A05;
loc_00843D38:
    if (v_stack_p40 == 0) goto loc_00843EBE;
    result = SeCaptureSubjectContext(v_stack_p98, v_stack_p148, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    if ((*(unsigned __int8 *)(v_rip + 6074182)) == 0) goto loc_00843D87;
    result = CmpIsSystemEntity(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_stack_p98, v_stack_p70, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00843DEC;
loc_00843D87:
    v_r12 = 0;
    v_r15 = 0;
    goto loc_00843A05;
loc_00843D97:
    v_stack_p20 = v_stack_p70;
    result = CmKeyBodyReplicateToVirtual(v_stack_p48, 0, 2, v_stack_p98);
    if (sign_flag) goto loc_008439F9;
    goto loc_008439E0;
loc_00843DDA:
    result = ObfDereferenceObjectWithTag(2, (unsigned int)(0x75536553ULL), 2, v_stack_p98);
    goto loc_00843A8D;
loc_00843DEC:
    v_stack_p78 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p78;
    result = ObReferenceObjectByHandle(v_stack_p58, (unsigned int)(0x20019ULL), *(unsigned __int64 *)(v_rip + 7875789), 0);
    v_stack_p48 = v_stack_p78;
    if (sign_flag) goto loc_00843C65;
    result = CmKeyBodyNeedsVirtualImage(v_stack_p78, (unsigned int)(0x20019ULL), *(unsigned __int64 *)(v_rip + 7875789), 0);
    if ((unsigned __int8)(result) != 0) goto loc_00843ECE;
    v_r12 = 0;
    v_r15 = 0;
    goto loc_00843A05;
loc_00843E4E:
    if (v_stack_p58 == 0) goto loc_00843CF7;
    v_stack_p68 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p68;
    a2 = 0;
    result = ObReferenceObjectByHandle(v_stack_p58, a2, *(unsigned __int64 *)(v_rip + 7875660), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (sign_flag) goto loc_00843CF7;
    v_stack_p60 = *(unsigned __int64 *)(v_stack_p68 + 8);
    result = ObfDereferenceObject(v_stack_p68, a2, *(unsigned __int64 *)(v_rip + 7875660), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    goto loc_00843CF7;
loc_00843EAF:
    v_stack_p40 = 1;
    goto loc_00843853;
loc_00843EBE:
    v_r12 = 0;
    v_r15 = 0;
    goto loc_00843A05;
loc_00843ECE:
    v_stack_p41 = (unsigned __int8)((unsigned __int8)((unsigned __int8)(v_stack_p41)));
    goto loc_00843912;
loc_00843EE0:
    if (0 != 0) goto loc_00843FA9;
    result = CmSetLastWriteTimeKey(v_stack_p78, v_stack_p50, *(unsigned __int64 *)(v_rip + 7875660), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    goto loc_008439F9;
loc_00843F06:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + 32) + 160)) & (0x100000ULL)) == 0) goto loc_00843936;
    v_r12 = 0;
    v_r15 = 0;
    goto loc_00843A05;
loc_00843F2A:
loc_00843F2F:
    goto loc_008439D8;
loc_00843F39:
    if (v_stack_pA8 == 0) goto loc_00843F66;
    if (v_stack_pA8 == (*(unsigned __int64 *)(v_rip + 6437941))) {
    }
    if (v_stack_p98 == 0) goto loc_00843A1B;
    if (v_stack_p98 != (*(unsigned __int64 *)(v_rip + 6437892))) goto loc_00843A1B;
    goto loc_00843A1B;
loc_00843FA0:
    v_stack_p40 = (unsigned __int8)(v_stack_p48);
    goto loc_0084384E;
loc_00843FA9:
    a1 = (unsigned int)((v_stack_p78) - (1));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    if (((unsigned int)(a1)) != 1) goto loc_008439F9;
loc_00843FD2:
    result = guard_dispatch_icall(a1, v_stack_p41, *(unsigned __int64 *)(v_rip + 7875660), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    goto loc_00843B91;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetInformationKey(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint8_t v_stack_m165;
    uint8_t v_stack_m166;
    uint8_t v_stack_m167;
    uint8_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m40;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m84;
    uint64_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_p148;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;

    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x5C7004)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m140 = Arg4;
    v_stack_m150 = Arg1;
    result = 0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    local_rdi = 0;
    v_stack_mF0 = 0;
    v_stack_m158 = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    v_stack_m148 = 0;
    if ((*(uint64_t *)(v_rip + 0x79487F)) != 0) {
        Arg2 = 0x20000ULL;
        Arg1 = local_rsp - 96;
        result = EtwGetKernelTraceTimestamp(Arg1, Arg2, Arg3, Arg4);
    }
    local_r12 = 0;
    v_stack_m166 = 0;
    v_stack_m160 = 0;
    v_stack_m167 = 0;
    result = 0;
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_m120 = v_stack_m128;
    v_stack_m128 = v_stack_m128;
    result = CmpInitializeThreadInfo(v_stack_m78, Arg2, Arg3, Arg4);
    v_stack_m138 = 0;
    local_r14 = 0;
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    result = CmpAcquireShutdownRundown(v_stack_m78, Arg2, Arg3, Arg4);
    v_stack_m165 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00843D0C;
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_00843BCE;
loc_00843849:
    v_stack_m168 = 1;
loc_0084384E:
loc_00843853:
    if (v_stack_m140 != 4) goto loc_00843CEA;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_0084387E;
    Arg2 = (4) + (Arg3);
    if (Arg2 > (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0084387B;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (Arg2 < Arg3) {
        result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)));
    }
    result = memcpy(v_stack_m158, Arg3, 4, Arg4);
    goto loc_008438B5;
loc_008438B5:
    v_stack_m118 = 0;
    Arg2 = 0;
    if (((uint32_t)((uint32_t)(Arg2))) != 5) { Arg2 = 2; }
    v_stack_m180 = 0;
    v_stack_m188 = v_stack_m118;
    result = ObReferenceObjectByHandle(v_stack_m150, Arg2, *(uint64_t *)(v_rip + 0x783204), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m160 = v_stack_m118;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000022ULL) goto loc_00843D38;
    Arg2 = 0;
loc_00843912:
    if (sign_flag) goto loc_00843C65;
    if ((*(uint64_t *)(v_rip + 0x7946E2)) != 0) goto loc_00843CD3;
loc_0084392C:
    if (((uint32_t)((uint32_t)(Arg2))) != 5) goto loc_00843D19;
loc_00843936:
    v_stack_m168 = 1;
    if ((*(uint32_t *)(v_rip + 0x6AC235)) == 0) goto loc_00843F2F;
    result = CmpIsRegistryLockAcquired(v_stack_m150, Arg2, *(uint64_t *)(v_rip + 0x783204), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint32_t)(result) != 0) goto loc_00843F2A;
    v_stack_mE8 = v_stack_m160;
    v_stack_mE0 = (uint32_t)((uint32_t)(Arg2));
    v_stack_mD8 = v_stack_m158;
    v_stack_mD0 = (uint32_t)((uint32_t)(v_stack_m140));
    v_stack_m178 = v_stack_m128;
    v_stack_m180 = v_stack_m160;
    v_stack_m188 = 18;
    Arg3 = 0;
    result = CmpCallCallBacksEx(Arg3 + 3, v_stack_mE8, Arg3, 1);
    if (sign_flag) goto loc_00843C70;
    v_stack_m166 = 1;
loc_008439D8:
    if ((uint8_t)(v_stack_m167) != 0) goto loc_00843D97;
loc_008439E0:
    if (((uint32_t)((uint32_t)(Arg2))) != 5) goto loc_00843EE0;
    *(uint16_t *)(v_stack_m160 + 0x32) = (uint16_t)(v_stack_m158);
loc_008439F9:
loc_008439FF:
loc_00843A05:
    if ((uint8_t)((uint8_t)(v_stack_m167)) == 0) goto loc_00843AA3;
    if ((*(uint32_t *)(v_rip + 0x7945FB)) != 0) goto loc_00843F39;
loc_00843A1B:
loc_00843A39:
    Arg1 = (v_stack_m100) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x248));
    if (Arg1 >= 15) goto loc_00843DDA;
    if (Arg1 != 15) goto loc_00843A39;
    result = ((*(uint32_t *)(v_rip + 0x7815A7)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg1 = v_stack_m100;
        Arg1 = (Arg1) + (-48);
        Arg2 = 0;
        Arg4 = 0x75536553ULL;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m110 != 0) goto loc_00843C8B;
loc_00843A9E:
loc_00843AA3:
    if ((uint8_t)(v_stack_m166) == 0) goto loc_00843B5C;
    if ((*(uint32_t *)(v_rip + 0x6AC0D5)) == 0) goto loc_00843B5C;
    result = CmpIsRegistryLockAcquired(v_stack_m110, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00843B5C;
    result = v_stack_m128;
    local_rsi = 0;
    if (v_stack_m128 != v_stack_m128) {
        v_stack_mA4 = 0;
        v_stack_m94 = v_xmm0;
        v_stack_m84 = 0;
        v_stack_m7C = 0;
        v_stack_mB0 = v_stack_m160;
        v_stack_mA8 = 0;
        v_stack_m98 = 0;
        result = v_stack_mE8;
        v_stack_mA0 = result;
        result = v_stack_m128;
        v_stack_m178 = result;
        v_stack_m180 = v_stack_m160;
        v_stack_m188 = 18;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_stack_mB0;
        Arg1 = Arg4 + 18;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rsi = v_stack_m98;
    }
    local_rbx = v_stack_m160;
    if ((uint8_t)(v_stack_m168) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_m160;
    }
    if (local_rbx != 0) {
        Arg1 = local_rbx;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(v_rip + 0x794480) != 0) goto loc_00843C9A;
loc_00843B91:
    result = *(uint64_t *)(v_rip + 0x794480);
    if ((uint8_t)((uint8_t)(result)) != 0) {
        result = CmpReleaseShutdownRundown(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmCleanupThreadInfo(v_stack_m78, Arg2, Arg3, Arg4);
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (368);
    return result;
loc_00843BCE:
    if ((uint32_t)(v_stack_m168) == 0) goto loc_00843EAF;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m168))) - (2));
    if (condition_is_equal) goto loc_00843FA0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00843FA0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00843849;
    if (((uint32_t)(Arg1)) == 1) goto loc_00843FA0;
    if ((*(uint64_t *)(v_rip + 0x794403)) == local_rbx) goto loc_00843C5B;
    if (v_stack_p58 == 0) goto loc_00843C5B;
    v_stack_p58 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p58;
    Arg2 = 0;
    result = ObReferenceObjectByHandle(v_stack_p58, Arg2, *(uint64_t *)(v_rip + 0x782E97), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (!(sign_flag)) {
        Arg1 = v_stack_p58;
        result = *(uint64_t *)(Arg1 + 0x8);
        v_stack_p60 = result;
        result = ObfDereferenceObject(Arg1, Arg2, *(uint64_t *)(v_rip + 0x782E97), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    }
loc_00843C65:
    local_r12 = 0;
    local_r15 = 0;
    goto loc_00843A05;
loc_00843C70:
    result = 0;
    if (((uint32_t)((uint32_t)(0xC0000003ULL))) != 0xC0000503ULL) { result = (uint32_t)((uint32_t)(0xC0000003ULL)); }
    local_r12 = 0;
    goto loc_008439FF;
loc_00843C8B:
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x75536553ULL), *(uint64_t *)(v_rip + 0x782E97), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    goto loc_00843A9E;
loc_00843C9A:
    v_stack_p28 = 0;
    Arg4 = 0;
    v_stack_p20 = v_stack_p60;
    if (result != (v_rip + 126175)) goto loc_00843FD2;
    result = EtwpTraceRegistry(20, v_stack_p148, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
    goto loc_00843B91;
loc_00843CD3:
    if (result == 0) goto loc_0084392C;
    v_stack_p60 = *(uint64_t *)(v_stack_p48 + 0x8);
    goto loc_0084392C;
loc_00843CEA:
    if ((*(uint64_t *)(v_rip + 0x794317)) != v_stack_p48) goto loc_00843E4E;
loc_00843CF7:
    local_r12 = 0;
    local_r15 = 0;
    goto loc_00843A05;
loc_00843D0C:
    local_r15 = 0;
    goto loc_00843A05;
loc_00843D19:
    if (!sign_flag) goto loc_00843F06;
    local_r12 = 0;
    local_r15 = 0;
    goto loc_00843A05;
loc_00843D38:
    if (v_stack_p40 == 0) goto loc_00843EBE;
    result = SeCaptureSubjectContext(v_stack_p98, v_stack_p148, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
    if ((*(uint8_t *)(v_rip + 0x5CAF46)) == 0) goto loc_00843D87;
    result = CmpIsSystemEntity(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), v_stack_p98, v_stack_p70, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00843DEC;
loc_00843D87:
    local_r12 = 0;
    local_r15 = 0;
    goto loc_00843A05;
loc_00843D97:
    v_stack_p20 = v_stack_p70;
    result = CmKeyBodyReplicateToVirtual(v_stack_p48, 0, 2, v_stack_p98);
    if (sign_flag) goto loc_008439F9;
    goto loc_008439E0;
loc_00843DDA:
    result = ObfDereferenceObjectWithTag(2, (uint32_t)(0x75536553ULL), 2, v_stack_p98);
    goto loc_00843A8D;
loc_00843DEC:
    v_stack_p78 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p78;
    result = ObReferenceObjectByHandle(v_stack_p58, (uint32_t)(0x20019ULL), *(uint64_t *)(v_rip + 0x782CCD), 0);
    v_stack_p48 = v_stack_p78;
    if (sign_flag) goto loc_00843C65;
    result = CmKeyBodyNeedsVirtualImage(v_stack_p78, (uint32_t)(0x20019ULL), *(uint64_t *)(v_rip + 0x782CCD), 0);
    if ((uint8_t)(result) != 0) goto loc_00843ECE;
    local_r12 = 0;
    local_r15 = 0;
    goto loc_00843A05;
loc_00843E4E:
    if (v_stack_p58 == 0) goto loc_00843CF7;
    v_stack_p68 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p68;
    Arg2 = 0;
    result = ObReferenceObjectByHandle(v_stack_p58, Arg2, *(uint64_t *)(v_rip + 0x782C4C), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (sign_flag) goto loc_00843CF7;
    v_stack_p60 = *(uint64_t *)(v_stack_p68 + 0x8);
    result = ObfDereferenceObject(v_stack_p68, Arg2, *(uint64_t *)(v_rip + 0x782C4C), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    goto loc_00843CF7;
loc_00843EAF:
    v_stack_p40 = 1;
    goto loc_00843853;
loc_00843EBE:
    local_r12 = 0;
    local_r15 = 0;
    goto loc_00843A05;
loc_00843ECE:
    v_stack_p41 = (uint8_t)((uint8_t)((uint8_t)(v_stack_p41)));
    goto loc_00843912;
loc_00843EE0:
    if (0 != 0) goto loc_00843FA9;
    result = CmSetLastWriteTimeKey(v_stack_p78, v_stack_p50, *(uint64_t *)(v_rip + 0x782C4C), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    goto loc_008439F9;
loc_00843F06:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p78 + 0x20) + 0xA0)) & (0x100000ULL)) == 0) goto loc_00843936;
    local_r12 = 0;
    local_r15 = 0;
    goto loc_00843A05;
loc_00843F2A:
loc_00843F2F:
    goto loc_008439D8;
loc_00843F39:
    if (v_stack_pA8 == 0) goto loc_00843F66;
    if (v_stack_pA8 == (*(uint64_t *)(v_rip + 0x623C35))) {
    }
    if (v_stack_p98 == 0) goto loc_00843A1B;
    if (v_stack_p98 != (*(uint64_t *)(v_rip + 0x623C04))) goto loc_00843A1B;
    goto loc_00843A1B;
loc_00843FA0:
    v_stack_p40 = (uint8_t)(v_stack_p48);
    goto loc_0084384E;
loc_00843FA9:
    Arg1 = (uint32_t)((v_stack_p78) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (((uint32_t)(Arg1)) != 1) goto loc_008439F9;
loc_00843FD2:
    result = guard_dispatch_icall(Arg1, v_stack_p41, *(uint64_t *)(v_rip + 0x782C4C), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    goto loc_00843B91;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00843720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
