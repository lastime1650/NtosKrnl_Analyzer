# PiDevCfgProcessDevice

- RVA: `0x00976D34`–`0x00977512` (길이 `2,014` bytes)
- VA: `0x0000000140976D34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000966E4`
- 디코드: `439`개 명령, `2,014/2,014` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00976D6A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00976DDB` → [PnpDiagnosticTraceObject](../../text/26/PnpDiagnosticTraceObject_function_0026E834.md) (function, `0x0026E834`)
- `0x00976DEB` → [PiDevCfgInitDeviceContext](PiDevCfgInitDeviceContext_function_00977518.md) (function, `0x00977518`)
- `0x00976E37` → [PiDevCfgFindDeviceDriver](PiDevCfgFindDeviceDriver_function_0097602C.md) (function, `0x0097602C`)
- `0x00976E6B` → [PiDevCfgConfigureDevice](PiDevCfgConfigureDevice_function_00977BB4.md) (function, `0x00977BB4`)
- `0x00976F68` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00976FCA` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00976FDF` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00976FEF` → [PiDevCfgFreeDeviceContext](../70/PiDevCfgFreeDeviceContext_function_00704A00.md) (function, `0x00704A00`)
- `0x00977006` → [PnpDiagnosticTraceObjectWithStatus](../../text/4A/PnpDiagnosticTraceObjectWithStatus_function_004A9F58.md) (function, `0x004A9F58`)
- `0x00977085` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009770BC` → [PiDevCfgLogDeviceConfigured](../AD/PiDevCfgLogDeviceConfigured_function_00ADCDD4.md) (function, `0x00ADCDD4`)
- `0x00977149` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x009771BB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0097721A` → [PiDevCfgQueryObjectProperties](PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00977239` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x009772E7` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x00977332` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00977366` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0097737C` → [PiDevCfgRequestDriverConfigurations](../73/PiDevCfgRequestDriverConfigurations_function_00735778.md) (function, `0x00735778`)
- `0x009774DF` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00977508` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)

### Direct callers
- [PpDevCfgProcessDevice](../AB/PpDevCfgProcessDevice_function_00AB6DB0.md) at `0x00AB6DC8`

### Static image references
- `0x00976DD4` → RVA `0x00012E40` (`.rdata`; read)
- `0x00976EF5` → RVA `0x00E0A9E0` (`.data`; read)
- `0x00976F32` → RVA `0x00E66398` (`.data`; read)
- `0x00976FFC` → RVA `0x00012E30` (`.rdata`; read)
- `0x00977066` → RVA `0x00012F10` (`.rdata`; read)
- `0x00977127` → RVA `0x000116B8` (`.rdata`; read)
- `0x009771D5` → RVA `0x00012E80` (`.rdata`; read)
- `0x009771F8` → RVA `0x00012E50` (`.rdata`; read)
- `0x009772C8` → RVA `0x00012F40` (`.rdata`; read)
- `0x009772FC` → RVA `0x00012F28` (`.rdata`; read)
- `0x009773C4` → RVA `0x00FD8054` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00976D6A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00976DDB` → [PnpDiagnosticTraceObject](../../text/26/PnpDiagnosticTraceObject_function_0026E834.md) (`PAGE` → `.text`)
  - `0x00976FCA` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00976FDF` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00977006` → [PnpDiagnosticTraceObjectWithStatus](../../text/4A/PnpDiagnosticTraceObjectWithStatus_function_004A9F58.md) (`PAGE` → `.text`)
  - `0x009771BB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00977239` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00977366` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **22**
  - `0x00976EC5` → [sub_00B29934 + 0x106](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x00976F9C` → [sub_00B29934 + 0x2A0](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x00976FA4` → [sub_00B29934 + 0x2A0](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x009770CF` → [sub_00B29934 + 0x106](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x0097714F` → [sub_00B29934 + 0x298](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x00977167` → [sub_00B29934 + 0x24E](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x00977174` → [sub_00B29934 + 0x232](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x00977181` → [sub_00B29934 + 0x232](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x0097718D` → [sub_00B29934 + 0x1DF](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x0097719F` → [sub_00B29934 + 0x1E3](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x009773A3` → [sub_00B29934](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x009773B2` → [sub_00B29934](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x009773D9` → [sub_00B29934 + 0x47](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x009773E9` → [sub_00B29934 + 0x47](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x009773F4` → [sub_00B29934 + 0xC2](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x009773FC` → [sub_00B29934 + 0x106](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x0097742C` → [sub_00B29934 + 0x1CF](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x0097743B` → [sub_00B29934 + 0x1CF](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x00977444` → [sub_00B29934 + 0x1CF](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x00977453` → [sub_00B29934 + 0x1CF](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x0097748F` → [sub_00B29934 + 0x28D](../B2/Unknown_function_00B29934.md) (`tail-transfer`)
  - `0x0097749E` → [sub_00B29934 + 0x28D](../B2/Unknown_function_00B29934.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00976D34  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00976D39  55                              push rbp
00976D3A  53                              push rbx
00976D3B  56                              push rsi
00976D3C  57                              push rdi
00976D3D  41 54                           push r12
00976D3F  41 55                           push r13
00976D41  41 56                           push r14
00976D43  41 57                           push r15
00976D45  48 8D AC 24 68 FF FF FF         lea rbp, [rsp - 0x98]
00976D4D  48 81 EC 98 01 00 00            sub rsp, 0x198
00976D54  45 33 F6                        xor r14d, r14d
00976D57  4C 8B E2                        mov r12, rdx
00976D5A  48 8B D9                        mov rbx, rcx
00976D5D  33 D2                           xor edx, edx
00976D5F  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00976D63  45 8B EE                        mov r13d, r14d
00976D66  45 8D 46 58                     lea r8d, [r14 + 0x58]
00976D6A  E8 D1 FE D4 FF                  call 0x1406c6c40
00976D6F  41 8B F6                        mov esi, r14d
00976D72  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
00976D76  41 8A FE                        mov dil, r14b
00976D79  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
00976D7D  45 8B FE                        mov r15d, r14d
00976D80  4C 89 75 B0                     mov qword ptr [rbp - 0x50], r14
00976D84  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
00976D88  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
00976D8D  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
00976D92  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
00976D97  44 88 B5 E0 00 00 00            mov byte ptr [rbp + 0xe0], r14b
00976D9E  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
00976DA3  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
00976DA7  C7 44 24 6C 01 00 00 00         mov dword ptr [rsp + 0x6c], 1
00976DAF  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
00976DB4  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
00976DB8  44 88 B5 F8 00 00 00            mov byte ptr [rbp + 0xf8], r14b
00976DBF  4C 39 73 30                     cmp qword ptr [rbx + 0x30], r14
00976DC3  0F 84 8C 05 00 00               je 0x140977355
00976DC9  4C 8D 6B 28                     lea r13, [rbx + 0x28]
00976DCD  49 8B D5                        mov rdx, r13
00976DD0  4C 89 6D C0                     mov qword ptr [rbp - 0x40], r13
00976DD4  48 8D 0D 65 C0 69 FF            lea rcx, [rip - 0x963f9b]
00976DDB  E8 54 7A 8F FF                  call 0x14026e834
00976DE0  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00976DE4  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00976DE8  49 8B D4                        mov rdx, r12
00976DEB  E8 28 07 00 00                  call 0x140977518
00976DF0  45 33 C0                        xor r8d, r8d
00976DF3  44 8B F0                        mov r14d, eax
00976DF6  85 C0                           test eax, eax
00976DF8  0F 88 B5 01 00 00               js 0x140976fb3
00976DFE  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
00976E01  45 8D 70 01                     lea r14d, [r8 + 1]
00976E05  44 84 B5 F0 00 00 00            test byte ptr [rbp + 0xf0], r14b
00976E0C  0F 85 11 02 00 00               jne 0x140977023
00976E12  4D 85 E4                        test r12, r12
00976E15  4C 0F 44 65 E0                  cmove r12, qword ptr [rbp - 0x20]
00976E1A  4C 89 A5 E8 00 00 00            mov qword ptr [rbp + 0xe8], r12
00976E21  41 84 C6                        test r14b, al
00976E24  0F 84 7A 03 00 00               je 0x1409771a4
00976E2A  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
00976E2E  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00976E33  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00976E37  E8 F0 F1 FF FF                  call 0x14097602c
00976E3C  45 33 C0                        xor r8d, r8d
00976E3F  44 8B F0                        mov r14d, eax
00976E42  85 C0                           test eax, eax
00976E44  78 5E                           js 0x140976ea4
00976E46  4C 39 45 B8                     cmp qword ptr [rbp - 0x48], r8
00976E4A  0F 85 23 05 00 00               jne 0x140977373
00976E50  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00976E55  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00976E5A  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00976E5F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00976E64  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00976E68  48 8B CB                        mov rcx, rbx
00976E6B  E8 44 0D 00 00                  call 0x140977bb4
00976E70  44 8B F0                        mov r14d, eax
00976E73  45 33 C0                        xor r8d, r8d
00976E76  85 C0                           test eax, eax
00976E78  0F 49 74 24 60                  cmovns esi, dword ptr [rsp + 0x60]
00976E7D  C1 E8 1F                        shr eax, 0x1f
00976E80  34 01                           xor al, 1
00976E82  88 85 E0 00 00 00               mov byte ptr [rbp + 0xe0], al
00976E88  41 81 FE 93 04 00 C0            cmp r14d, 0xc0000493
00976E8F  74 13                           je 0x140976ea4
00976E91  88 85 E0 00 00 00               mov byte ptr [rbp + 0xe0], al
00976E97  41 81 FE 95 04 00 C0            cmp r14d, 0xc0000495
00976E9E  0F 85 E8 04 00 00               jne 0x14097738c
00976EA4  4C 39 45 A0                     cmp qword ptr [rbp - 0x60], r8
00976EA8  0F 85 F0 04 00 00               jne 0x14097739e
00976EAE  4C 39 45 B8                     cmp qword ptr [rbp - 0x48], r8
00976EB2  0F 85 F2 00 00 00               jne 0x140976faa
00976EB8  4C 39 45 A0                     cmp qword ptr [rbp - 0x60], r8
00976EBC  0F 85 04 02 00 00               jne 0x1409770c6
00976EC2  40 84 FF                        test dil, dil
00976EC5  0F 85 6F 2B 1B 00               jne 0x140b29a3a
00976ECB  4C 39 44 24 78                  cmp qword ptr [rsp + 0x78], r8
00976ED0  0F 84 E1 04 00 00               je 0x1409773b7
00976ED6  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00976EDB  8B 88 BC 01 00 00               mov ecx, dword ptr [rax + 0x1bc]
00976EE1  85 C9                           test ecx, ecx
00976EE3  0F 88 10 05 00 00               js 0x1409773f9
00976EE9  40 8A BD E0 00 00 00            mov dil, byte ptr [rbp + 0xe0]
00976EF0  40 84 FF                        test dil, dil
00976EF3  74 34                           je 0x140976f29
00976EF5  44 38 05 E4 3A 49 00            cmp byte ptr [rip + 0x493ae4], r8b
00976EFC  0F 85 FF 04 00 00               jne 0x140977401
00976F02  F6 85 F0 00 00 00 02            test byte ptr [rbp + 0xf0], 2
00976F09  0F 85 F2 04 00 00               jne 0x140977401
00976F0F  8B 83 C0 02 00 00               mov eax, dword ptr [rbx + 0x2c0]
00976F15  40 F6 C6 40                     test sil, 0x40
00976F19  74 05                           je 0x140976f20
00976F1B  83 E0 FE                        and eax, 0xfffffffe
00976F1E  EB 03                           jmp 0x140976f23
00976F20  83 C8 01                        or eax, 1
00976F23  89 83 C0 02 00 00               mov dword ptr [rbx + 0x2c0], eax
00976F29  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
00976F2D  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00976F32  48 8B 0D 5F F4 4E 00            mov rcx, qword ptr [rip + 0x4ef45f]
00976F39  41 B9 0B 00 00 00               mov r9d, 0xb
00976F3F  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00976F44  4D 8B C4                        mov r8, r12
00976F47  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00976F4C  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00976F51  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00976F56  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00976F5B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00976F60  C7 44 24 64 04 00 00 00         mov dword ptr [rsp + 0x64], 4
00976F68  E8 03 69 F7 FF                  call 0x1408ed870
00976F6D  45 33 C0                        xor r8d, r8d
00976F70  85 C0                           test eax, eax
00976F72  0F 89 92 04 00 00               jns 0x14097740a
00976F78  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00976F7D  8B 83 8C 01 00 00               mov eax, dword ptr [rbx + 0x18c]
00976F83  25 00 20 00 00                  and eax, 0x2000
00976F88  45 85 F6                        test r14d, r14d
00976F8B  0F 89 43 01 00 00               jns 0x1409770d4
00976F91  85 C0                           test eax, eax
00976F93  0F 85 ED 04 00 00               jne 0x140977486
00976F99  40 84 FF                        test dil, dil
00976F9C  0F 85 32 2C 1B 00               jne 0x140b29bd4
00976FA2  85 F6                           test esi, esi
00976FA4  0F 85 2A 2C 1B 00               jne 0x140b29bd4
00976FAA  44 38 85 F8 00 00 00            cmp byte ptr [rbp + 0xf8], r8b
00976FB1  75 7B                           jne 0x14097702e
00976FB3  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00976FB8  48 85 C9                        test rcx, rcx
00976FBB  0F 85 47 05 00 00               jne 0x140977508
00976FC1  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00976FC5  48 85 C9                        test rcx, rcx
00976FC8  74 0C                           je 0x140976fd6
00976FCA  E8 81 B8 20 00                  call 0x140b82850
00976FCF  0F 57 C0                        xorps xmm0, xmm0
00976FD2  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
00976FD6  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00976FDA  48 85 C9                        test rcx, rcx
00976FDD  74 0C                           je 0x140976feb
00976FDF  E8 6C B8 20 00                  call 0x140b82850
00976FE4  0F 57 C0                        xorps xmm0, xmm0
00976FE7  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00976FEB  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00976FEF  E8 0C DA D8 FF                  call 0x140704a00
00976FF4  4D 85 ED                        test r13, r13
00976FF7  74 12                           je 0x14097700b
00976FF9  45 8B C6                        mov r8d, r14d
00976FFC  48 8D 0D 2D BE 69 FF            lea rcx, [rip - 0x9641d3]
00977003  49 8B D5                        mov rdx, r13
00977006  E8 4D 2F B3 FF                  call 0x1404a9f58
0097700B  41 8B C6                        mov eax, r14d
0097700E  48 81 C4 98 01 00 00            add rsp, 0x198
00977015  41 5F                           pop r15
00977017  41 5E                           pop r14
00977019  41 5D                           pop r13
0097701B  41 5C                           pop r12
0097701D  5F                              pop rdi
0097701E  5E                              pop rsi
0097701F  5B                              pop rbx
00977020  5D                              pop rbp
00977021  C3                              ret
00977022  CC                              int3
00977023  41 0B C6                        or eax, r14d
00977026  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00977029  E9 E4 FD FF FF                  jmp 0x140976e12
0097702E  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
00977032  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00977037  48 8B 0D 5A F3 4E 00            mov rcx, qword ptr [rip + 0x4ef35a]
0097703E  4D 8B CC                        mov r9, r12
00977041  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00977046  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0097704B  48 8D 45 88                     lea rax, [rbp - 0x78]
0097704F  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00977057  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0097705C  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00977061  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00977066  48 8D 05 A3 BE 69 FF            lea rax, [rip - 0x96415d]
0097706D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00977072  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00977077  41 B8 01 00 00 00               mov r8d, 1
0097707D  C7 44 24 64 08 00 00 00         mov dword ptr [rsp + 0x64], 8
00977085  E8 F6 B0 F6 FF                  call 0x1408e2180
0097708A  85 C0                           test eax, eax
0097708C  0F 89 57 04 00 00               jns 0x1409774e9
00977092  33 C0                           xor eax, eax
00977094  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00977098  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
0097709D  48 8D 4D A8                     lea rcx, [rbp - 0x58]
009770A1  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
009770A6  48 8D 55 D0                     lea rdx, [rbp - 0x30]
009770AA  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
009770AF  48 8B CB                        mov rcx, rbx
009770B2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009770B7  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
009770BC  E8 13 5D 16 00                  call 0x140adcdd4
009770C1  E9 ED FE FF FF                  jmp 0x140976fb3
009770C6  40 84 FF                        test dil, dil
009770C9  0F 84 1A FE FF FF               je 0x140976ee9
009770CF  E9 66 29 1B 00                  jmp 0x140b29a3a
009770D4  81 64 24 60 9F FB F7 FF         and dword ptr [rsp + 0x60], 0xfff7fb9f
009770DC  83 E6 DF                        and esi, 0xffffffdf
009770DF  85 C0                           test eax, eax
009770E1  0F 85 3E 03 00 00               jne 0x140977425
009770E7  8B 8B 2C 01 00 00               mov ecx, dword ptr [rbx + 0x12c]
009770ED  8D 81 FD FC FF FF               lea eax, [rcx - 0x303]
009770F3  A9 EE FF FF FF                  test eax, 0xffffffee
009770F8  74 5A                           je 0x140977154
009770FA  44 39 44 24 68                  cmp dword ptr [rsp + 0x68], r8d
009770FF  0F 85 53 03 00 00               jne 0x140977458
00977105  F6 45 D0 01                     test byte ptr [rbp - 0x30], 1
00977109  0F 85 8A FE FF FF               jne 0x140976f99
0097710F  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00977114  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00977119  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0097711E  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00977123  4D 8B 45 08                     mov r8, qword ptr [r13 + 8]
00977127  48 8D 05 8A A5 69 FF            lea rax, [rip - 0x965a76]
0097712E  48 8B 0D 63 F2 4E 00            mov rcx, qword ptr [rip + 0x4ef263]
00977135  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00977139  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0097713E  41 B9 01 00 00 00               mov r9d, 1
00977144  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00977149  E8 02 6A 11 00                  call 0x140a8db50
0097714E  90                              nop
0097714F  E9 78 2A 1B 00                  jmp 0x140b29bcc
00977154  81 F9 13 03 00 00               cmp ecx, 0x313
0097715A  74 9E                           je 0x1409770fa
0097715C  8B 83 8C 01 00 00               mov eax, dword ptr [rbx + 0x18c]
00977162  A9 00 60 00 00                  test eax, 0x6000
00977167  0F 85 15 2A 1B 00               jne 0x140b29b82
0097716D  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00977171  F6 C1 70                        test cl, 0x70
00977174  0F 84 EC 29 1B 00               je 0x140b29b66
0097717A  44 38 05 5F 38 49 00            cmp byte ptr [rip + 0x49385f], r8b
00977181  0F 85 DF 29 1B 00               jne 0x140b29b66
00977187  49 8B C0                        mov rax, r8
0097718A  F6 C1 10                        test cl, 0x10
0097718D  0F 84 80 29 1B 00               je 0x140b29b13
00977193  B8 80 00 00 00                  mov eax, 0x80
00977198  44 8B C0                        mov r8d, eax
0097719B  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0097719F  E9 73 29 1B 00                  jmp 0x140b29b17
009771A4  44 38 05 35 38 49 00            cmp byte ptr [rip + 0x493835], r8b
009771AB  0F 85 79 FC FF FF               jne 0x140976e2a
009771B1  33 D2                           xor edx, edx
009771B3  48 8D 4D 40                     lea rcx, [rbp + 0x40]
009771B7  44 8D 42 50                     lea r8d, [rdx + 0x50]
009771BB  E8 80 FA D4 FF                  call 0x1406c6c40
009771C0  BA 12 20 00 00                  mov edx, 0x2012
009771C5  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
009771CD  B9 06 00 00 00                  mov ecx, 6
009771D2  89 55 48                        mov dword ptr [rbp + 0x48], edx
009771D5  48 8D 05 A4 BC 69 FF            lea rax, [rip - 0x96435c]
009771DC  89 55 70                        mov dword ptr [rbp + 0x70], edx
009771DF  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
009771E3  4D 8B CC                        mov r9, r12
009771E6  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
009771EA  45 8B C6                        mov r8d, r14d
009771ED  48 8D 45 98                     lea rax, [rbp - 0x68]
009771F1  89 4D 5C                        mov dword ptr [rbp + 0x5c], ecx
009771F4  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
009771F8  48 8D 05 51 BC 69 FF            lea rax, [rip - 0x9643af]
009771FF  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
00977203  48 8D 45 B0                     lea rax, [rbp - 0x50]
00977207  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
0097720B  48 8D 45 40                     lea rax, [rbp + 0x40]
0097720F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00977214  89 8D 84 00 00 00               mov dword ptr [rbp + 0x84], ecx
0097721A  E8 4D 05 00 00                  call 0x14097776c
0097721F  45 33 C0                        xor r8d, r8d
00977222  44 8B F0                        mov r14d, eax
00977225  85 C0                           test eax, eax
00977227  0F 88 86 FD FF FF               js 0x140976fb3
0097722D  44 39 45 60                     cmp dword ptr [rbp + 0x60], r8d
00977231  7D 0E                           jge 0x140977241
00977233  33 D2                           xor edx, edx
00977235  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00977239  E8 42 35 AB FF                  call 0x14042a780
0097723E  45 33 C0                        xor r8d, r8d
00977241  44 39 85 88 00 00 00            cmp dword ptr [rbp + 0x88], r8d
00977248  0F 8C 12 01 00 00               jl 0x140977360
0097724E  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00977252  48 85 C9                        test rcx, rcx
00977255  0F 84 CF FB FF FF               je 0x140976e2a
0097725B  66 44 39 01                     cmp word ptr [rcx], r8w
0097725F  0F 85 C5 FB FF FF               jne 0x140976e2a
00977265  40 B7 01                        mov dil, 1
00977268  41 BF 90 04 00 C0               mov r15d, 0xc0000490
0097726E  E9 31 FC FF FF                  jmp 0x140976ea4
00977273  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
00977277  4C 8B A5 E8 00 00 00            mov r12, qword ptr [rbp + 0xe8]
0097727E  44 38 85 E0 00 00 00            cmp byte ptr [rbp + 0xe0], r8b
00977285  0F 84 1F FD FF FF               je 0x140976faa
0097728B  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00977295  4D 8B CC                        mov r9, r12
00977298  48 8B 00                        mov rax, qword ptr [rax]
0097729B  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
0097729F  48 8B 0D F2 F0 4E 00            mov rcx, qword ptr [rip + 0x4ef0f2]
009772A6  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
009772AA  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
009772AD  83 E0 01                        and eax, 1
009772B0  C1 E0 11                        shl eax, 0x11
009772B3  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009772B7  48 8D 45 A8                     lea rax, [rbp - 0x58]
009772BB  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
009772C3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009772C8  48 8D 05 71 BC 69 FF            lea rax, [rip - 0x96438f]
009772CF  C7 44 24 30 10 00 00 00         mov dword ptr [rsp + 0x30], 0x10
009772D7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009772DC  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
009772E1  41 B8 01 00 00 00               mov r8d, 1
009772E7  E8 B4 EF F7 FF                  call 0x1408f62a0
009772EC  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
009772F0  48 8D 44 24 64                  lea rax, [rsp + 0x64]
009772F5  48 8B 0D 9C F0 4E 00            mov rcx, qword ptr [rip + 0x4ef09c]
009772FC  48 8D 35 25 BC 69 FF            lea rsi, [rip - 0x9643db]
00977303  33 FF                           xor edi, edi
00977305  4D 8B CC                        mov r9, r12
00977308  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
0097730C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00977311  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00977316  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
0097731A  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0097731F  44 8D 47 01                     lea r8d, [rdi + 1]
00977323  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00977328  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0097732D  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00977332  E8 49 AE F6 FF                  call 0x1408e2180
00977337  3D 23 00 00 C0                  cmp eax, 0xc0000023
0097733C  0F 85 61 01 00 00               jne 0x1409774a3
00977342  83 7C 24 64 08                  cmp dword ptr [rsp + 0x64], 8
00977347  0F 85 56 01 00 00               jne 0x1409774a3
0097734D  45 33 C0                        xor r8d, r8d
00977350  E9 55 FC FF FF                  jmp 0x140976faa
00977355  41 BE 10 00 00 C0               mov r14d, 0xc0000010
0097735B  E9 8B FC FF FF                  jmp 0x140976feb
00977360  33 D2                           xor edx, edx
00977362  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00977366  E8 15 34 AB FF                  call 0x14042a780
0097736B  45 33 C0                        xor r8d, r8d
0097736E  E9 DB FE FF FF                  jmp 0x14097724e
00977373  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00977378  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0097737C  E8 F7 E3 DB FF                  call 0x140735778
00977381  44 8B F0                        mov r14d, eax
00977384  45 33 C0                        xor r8d, r8d
00977387  E9 18 FB FF FF                  jmp 0x140976ea4
0097738C  C6 85 F8 00 00 00 01            mov byte ptr [rbp + 0xf8], 1
00977393  88 85 E0 00 00 00               mov byte ptr [rbp + 0xe0], al
00977399  E9 06 FB FF FF                  jmp 0x140976ea4
0097739E  4C 39 44 24 78                  cmp qword ptr [rsp + 0x78], r8
009773A3  0F 85 8B 25 1B 00               jne 0x140b29934
009773A9  40 84 FF                        test dil, dil
009773AC  0F 84 FC FA FF FF               je 0x140976eae
009773B2  E9 7D 25 1B 00                  jmp 0x140b29934
009773B7  41 81 FE 90 04 00 C0            cmp r14d, 0xc0000490
009773BE  0F 85 25 FB FF FF               jne 0x140976ee9
009773C4  8B 05 8A 0C 66 00               mov eax, dword ptr [rip + 0x660c8a]
009773CA  A8 02                           test al, 2
009773CC  0F 84 17 FB FF FF               je 0x140976ee9
009773D2  44 38 05 07 36 49 00            cmp byte ptr [rip + 0x493607], r8b
009773D9  0F 84 9C 25 1B 00               je 0x140b2997b
009773DF  F7 83 30 02 00 00 00 01 00 00   test dword ptr [rbx + 0x230], 0x100
009773E9  0F 85 8C 25 1B 00               jne 0x140b2997b
009773EF  BE 20 00 00 00                  mov esi, 0x20
009773F4  E9 FD 25 1B 00                  jmp 0x140b299f6
009773F9  44 8B F9                        mov r15d, ecx
009773FC  E9 39 26 1B 00                  jmp 0x140b29a3a
00977401  0F BA EE 12                     bts esi, 0x12
00977405  E9 05 FB FF FF                  jmp 0x140976f0f
0097740A  83 7C 24 6C 04                  cmp dword ptr [rsp + 0x6c], 4
0097740F  0F 85 63 FB FF FF               jne 0x140976f78
00977415  83 7C 24 64 04                  cmp dword ptr [rsp + 0x64], 4
0097741A  0F 84 5D FB FF FF               je 0x140976f7d
00977420  E9 53 FB FF FF                  jmp 0x140976f78
00977425  83 BB 94 01 00 00 01            cmp dword ptr [rbx + 0x194], 1
0097742C  0F 84 D1 26 1B 00               je 0x140b29b03
00977432  8B 83 94 01 00 00               mov eax, dword ptr [rbx + 0x194]
00977438  83 F8 1C                        cmp eax, 0x1c
0097743B  0F 84 C2 26 1B 00               je 0x140b29b03
00977441  83 F8 12                        cmp eax, 0x12
00977444  0F 84 B9 26 1B 00               je 0x140b29b03
0097744A  83 F8 38                        cmp eax, 0x38
0097744D  0F 85 94 FC FF FF               jne 0x1409770e7
00977453  E9 AB 26 1B 00                  jmp 0x140b29b03
00977458  40 F6 C6 40                     test sil, 0x40
0097745C  0F 84 A3 FC FF FF               je 0x140977105
00977462  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00977467  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0097746C  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
00977474  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00977479  C7 44 24 38 17 00 00 00         mov dword ptr [rsp + 0x38], 0x17
00977481  E9 9D FC FF FF                  jmp 0x140977123
00977486  8B 93 94 01 00 00               mov edx, dword ptr [rbx + 0x194]
0097748C  83 FA 01                        cmp edx, 1
0097748F  0F 84 2C 27 1B 00               je 0x140b29bc1
00977495  83 FA 12                        cmp edx, 0x12
00977498  0F 85 FB FA FF FF               jne 0x140976f99
0097749E  E9 1E 27 1B 00                  jmp 0x140b29bc1
009774A3  4D 8B 45 08                     mov r8, qword ptr [r13 + 8]
009774A7  48 8D 45 A8                     lea rax, [rbp - 0x58]
009774AB  48 8B 0D E6 EE 4E 00            mov rcx, qword ptr [rip + 0x4eeee6]
009774B2  48 8D 55 D0                     lea rdx, [rbp - 0x30]
009774B6  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
009774BA  41 B9 01 00 00 00               mov r9d, 1
009774C0  C7 44 24 48 08 00 00 00         mov dword ptr [rsp + 0x48], 8
009774C8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009774CD  C7 44 24 38 10 00 00 00         mov dword ptr [rsp + 0x38], 0x10
009774D5  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
009774DA  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009774DF  E8 6C 66 11 00                  call 0x140a8db50
009774E4  E9 64 FE FF FF                  jmp 0x14097734d
009774E9  83 7C 24 6C 09                  cmp dword ptr [rsp + 0x6c], 9
009774EE  0F 85 9E FB FF FF               jne 0x140977092
009774F4  83 7C 24 64 08                  cmp dword ptr [rsp + 0x64], 8
009774F9  0F 85 93 FB FF FF               jne 0x140977092
009774FF  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00977503  E9 90 FB FF FF                  jmp 0x140977098
00977508  E8 47 BE DB FF                  call 0x140733354
0097750D  E9 AF FA FF FF                  jmp 0x140976fc1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgProcessDevice(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p64;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (408);
    v_r14 = 0;
    a2 = 0;
    result = memset(v_stack_m108, a2, v_r14 + 88, a4);
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    v_stack_m128 = 0;
    v_stack_m120 = 0;
    v_stack_m160 = 0;
    v_stack_m178 = 0;
    v_stack_m168 = 0;
    v_stack_p8 = 0;
    v_stack_m170 = 0;
    v_stack_m150 = 0;
    v_stack_m16C = 1;
    v_stack_m174 = 0;
    v_stack_m130 = 0;
    v_stack_p20 = 0;
    if ((*(unsigned __int64 *)(a1 + 48)) == 0) goto loc_00977355;
    v_stack_m118 = a1 + 40;
    result = PnpDiagnosticTraceObject(v_rip - 9846683, a1 + 40, v_r14 + 88, a4);
    result = PiDevCfgInitDeviceContext(*(unsigned __int64 *)(a1 + 40 + 8), 0, v_stack_m108, a4);
    a3 = 0;
    if (sign_flag) goto loc_00976FB3;
    if (((v_stack_p18) & ((unsigned __int8)(a3 + 1))) != 0) goto loc_00977023;
loc_00976E12:
    if (0 == 0) { a2 = v_stack_mF8; }
    v_stack_p10 = a2;
    if ((((unsigned __int8)(a3 + 1)) & ((unsigned __int8)((unsigned int)(v_stack_m108)))) == 0) goto loc_009771A4;
loc_00976E2A:
    result = PiDevCfgFindDeviceDriver(v_stack_m108, v_stack_m138, v_stack_m160, a4);
    a3 = 0;
    if (sign_flag) goto loc_00976EA4;
    if (v_stack_m120 != 0) goto loc_00977373;
    v_stack_m1B8 = v_stack_m168;
    result = PiDevCfgConfigureDevice(a1, v_stack_m108, v_stack_m160, v_stack_m178);
    a3 = 0;
    v_rsi = 0;
    if (!sign_flag) { v_rsi = v_stack_m178; }
    result = (unsigned int)((result) >> (31));
    result = (unsigned __int8)((result) ^ (1));
    v_stack_p8 = (unsigned __int8)(result);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000493ULL) goto loc_00976EA4;
    v_stack_p8 = (unsigned __int8)(result);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000495ULL) goto loc_0097738C;
loc_00976EA4:
    if (v_stack_m138 != 0) goto loc_0097739E;
loc_00976EAE:
    if (v_stack_m120 != 0) goto loc_00976FAA;
    if (v_stack_m138 != 0) goto loc_009770C6;
    if (v_stack_m160 == 0) goto loc_009773B7;
    if (sign_flag) goto loc_009773F9;
loc_00976EE9:
    if ((unsigned __int8)(v_stack_p8) == 0) goto loc_00976F29;
    if ((*(unsigned __int8 *)(v_rip + 4799204)) != 0) goto loc_00977401;
    if (((v_stack_p18) & (2)) != 0) goto loc_00977401;
loc_00976F0F:
    if ((((unsigned __int8)(v_rsi)) & (64)) == 0) goto loc_00976F20;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 704))) & (0xFFFFFFFEULL));
    goto loc_00976F23;
loc_00976F20:
    result = (unsigned int)((result) | (1));
loc_00976F23:
    *(unsigned int *)(a1 + 704) = (unsigned int)(result);
loc_00976F29:
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m174;
    v_stack_m1B0 = v_stack_m178;
    v_stack_m1B8 = v_stack_m16C;
    v_stack_m174 = 4;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 5174367), *(unsigned __int64 *)(a1 + 40 + 8), a2, 11);
    a3 = 0;
    if (!sign_flag) goto loc_0097740A;
loc_00976F78:
    v_stack_m178 = 0;
loc_00976F7D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 396))) & (0x2000ULL));
    if (!sign_flag) goto loc_009770D4;
    if ((unsigned int)(result) != 0) goto loc_00977486;
loc_00976F99:
loc_00976FAA:
    if (v_stack_p20 != 0) goto loc_0097702E;
loc_00976FB3:
    if (v_stack_m160 != 0) goto loc_00977508;
loc_00976FC1:
    if (v_stack_m138 != 0) {
        result = ExFreePool(v_stack_m138, *(unsigned __int64 *)(a1 + 40 + 8), a3, 11);
        v_stack_m140 = v_xmm0;
    }
    if (v_stack_m120 != 0) {
        result = ExFreePool(v_stack_m120, *(unsigned __int64 *)(a1 + 40 + 8), a3, 11);
        v_stack_m128 = v_xmm0;
    }
    result = PiDevCfgFreeDeviceContext(v_stack_m108, *(unsigned __int64 *)(a1 + 40 + 8), a3, 11);
    if (a1 + 40 != 0) {
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = v_rip - 9847251;
        a2 = a1 + 40;
        result = PnpDiagnosticTraceObjectWithStatus(a1, a2, a3, 11);
    }
    v_rsp = (v_rsp) + (408);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00977023:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) | ((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_m108 = (unsigned int)(result);
    goto loc_00976E12;
loc_0097702E:
    v_stack_p50 = a3;
    v_stack_p48 = v_stack_p64;
    v_stack_p40 = 8;
    v_stack_p38 = v_stack_m150;
    v_stack_p30 = v_stack_p6C;
    v_stack_p28 = v_rip - 9847133;
    v_stack_p20 = a3;
    v_stack_p64 = 8;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 5174106), *(unsigned __int64 *)(a1 + 40 + 8), 1, a2);
    if (!sign_flag) goto loc_009774E9;
loc_00977092:
    result = 0;
    v_stack_m150 = 0;
loc_00977098:
    v_stack_p30 = v_stack_m130;
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = PiDevCfgLogDeviceConfigured(a1, v_stack_m108, v_stack_p78, (unsigned int)(v_stack_p70));
    goto loc_00976FB3;
loc_009770C6:
    if ((unsigned __int8)(v_stack_p8) == 0) goto loc_00976EE9;
loc_009770D4:
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFDFULL));
    if ((unsigned int)(result) != 0) goto loc_00977425;
loc_009770E7:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)) - 771)) & (0xFFFFFFEEULL)) == 0) goto loc_00977154;
loc_009770FA:
    if (v_stack_p68 != ((unsigned int)(v_stack_p78))) goto loc_00977458;
loc_00977105:
    if (((v_stack_m108) & (1)) != 0) goto loc_00976F99;
    v_stack_p50 = (unsigned int)(v_stack_p78);
    v_stack_p48 = (unsigned int)(v_stack_p78);
    v_stack_p40 = v_stack_p78;
    v_stack_p38 = (unsigned int)(v_stack_p78);
loc_00977123:
    v_stack_p30 = v_rip - 9853558;
    v_stack_p20 = a2;
    result = PiDevCfgSetObjectProperty(*(unsigned __int64 *)(v_rip + 5173859), v_stack_m108, *(unsigned __int64 *)(a1 + 40 + 8), 1);
loc_00977154:
    if (((unsigned int)(*(unsigned __int64 *)(v_rip + 5173859))) == 787) goto loc_009770FA;
    v_stack_m150 = 128;
loc_009771A4:
    if ((*(unsigned __int8 *)(v_rip + 4798517)) != 128) goto loc_00976E2A;
    a2 = 0;
    result = memset(v_stack_m98, a2, a2 + 80, 1);
    v_stack_p28 = 2;
    v_stack_m90 = (unsigned int)((unsigned int)(0x2012ULL));
    v_stack_m68 = (unsigned int)((unsigned int)(0x2012ULL));
    v_stack_m98 = v_rip - 9847644;
    v_stack_m7C = 6;
    v_stack_m88 = v_stack_m140;
    v_stack_m70 = v_rip - 9847727;
    v_stack_m60 = v_stack_m128;
    v_stack_p20 = v_stack_m98;
    v_stack_m54 = 6;
    result = PiDevCfgQueryObjectProperties(6, *(unsigned __int64 *)(a1 + 40 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 0);
    a3 = 0;
    if (sign_flag) goto loc_00976FB3;
    if (v_stack_m78 < 0) {
        a2 = 0;
        a1 = v_stack_m140;
        result = RtlInitUnicodeString(a1, a2, a3, 0);
        a3 = 0;
    }
    if (v_stack_m50 < 0) goto loc_00977360;
loc_0097724E:
    if (v_stack_m138 == 0) goto loc_00976E2A;
    if ((*(unsigned __int16 *)(v_stack_m138)) != 0) goto loc_00976E2A;
    goto loc_00976EA4;
loc_00977355:
    goto loc_00976FEB;
loc_00977360:
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m128, a2, a3, 0);
    a3 = 0;
    goto loc_0097724E;
loc_00977373:
    result = PiDevCfgRequestDriverConfigurations(v_stack_m108, v_stack_p78, a3, 0);
    a3 = 0;
    goto loc_00976EA4;
loc_0097738C:
    v_stack_p20 = 1;
    v_stack_p8 = (unsigned __int8)(result);
    goto loc_00976EA4;
loc_0097739E:
    if (1 == 0) goto loc_00976EAE;
loc_009773B7:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000490ULL) goto loc_00976EE9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6687882)))) & (2)) == 0) goto loc_00976EE9;
loc_009773F9:
loc_00977401:
    goto loc_00976F0F;
loc_0097740A:
    if (v_stack_p6C != 4) goto loc_00976F78;
    if (v_stack_p64 == 4) goto loc_00976F7D;
    goto loc_00976F78;
loc_00977425:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 404)))) != 56) goto loc_009770E7;
loc_00977458:
    if (((32) & (64)) == 0) goto loc_00977105;
    v_stack_p50 = 0;
    v_stack_p48 = 4;
    v_stack_p40 = v_stack_p68;
    v_stack_p38 = 23;
    goto loc_00977123;
loc_00977486:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 404)))) != 18) goto loc_00976F99;
loc_009774E9:
    if (v_stack_p6C != 9) goto loc_00977092;
    if (v_stack_p64 != 8) goto loc_00977092;
    goto loc_00977098;
loc_00977508:
    result = PiDevCfgFreeDriverNode(v_stack_m108, (unsigned int)(*(unsigned int *)(a1 + 404)), a3, 0);
    goto loc_00976FC1;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgProcessDevice(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m150;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p60;
    uint64_t v_stack_p64;
    uint32_t v_stack_p68;
    uint64_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint8_t v_stack_p8;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (408);
    local_r14 = 0;
    Arg2 = 0;
    result = memset(v_stack_m108, Arg2, local_r14 + 88, a4);
    v_stack_m140 = 0;
    v_stack_m138 = 0;
    v_stack_m128 = 0;
    v_stack_m120 = 0;
    v_stack_m160 = 0;
    v_stack_m178 = 0;
    v_stack_m168 = 0;
    v_stack_p8 = 0;
    v_stack_m170 = 0;
    v_stack_m150 = 0;
    v_stack_m16C = 1;
    v_stack_m174 = 0;
    v_stack_m130 = 0;
    v_stack_p20 = 0;
    if ((*(uint64_t *)(arg1 + 0x30)) == 0) goto loc_00977355;
    v_stack_m118 = Arg1 + 40;
    result = PnpDiagnosticTraceObject(v_rip - 9846683, Arg1 + 40, local_r14 + 88, a4);
    result = PiDevCfgInitDeviceContext(*(uint64_t *)(arg1 + 0x28 + 0x8), 0, v_stack_m108, a4);
    Arg3 = 0;
    if (sign_flag) goto loc_00976FB3;
    if (((v_stack_p18) & ((uint8_t)(Arg3 + 1))) != 0) goto loc_00977023;
loc_00976E12:
    if (0 == 0) { Arg2 = v_stack_mF8; }
    v_stack_p10 = Arg2;
    if ((((uint8_t)(Arg3 + 1)) & ((uint8_t)((uint32_t)(v_stack_m108)))) == 0) goto loc_009771A4;
loc_00976E2A:
    result = PiDevCfgFindDeviceDriver(v_stack_m108, v_stack_m138, v_stack_m160, a4);
    Arg3 = 0;
    if (sign_flag) goto loc_00976EA4;
    if (v_stack_m120 != 0) goto loc_00977373;
    v_stack_m1B8 = v_stack_m168;
    result = PiDevCfgConfigureDevice(Arg1, v_stack_m108, v_stack_m160, v_stack_m178);
    Arg3 = 0;
    local_rsi = 0;
    if (!sign_flag) { local_rsi = v_stack_m178; }
    result = (uint32_t)((result) >> (31));
    result = (uint8_t)((result) ^ (1));
    v_stack_p8 = (uint8_t)(result);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000493ULL) goto loc_00976EA4;
    v_stack_p8 = (uint8_t)(result);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000495ULL) goto loc_0097738C;
loc_00976EA4:
    if (v_stack_m138 != 0) goto loc_0097739E;
loc_00976EAE:
    if (v_stack_m120 != 0) goto loc_00976FAA;
    if (v_stack_m138 != 0) goto loc_009770C6;
    if (v_stack_m160 == 0) goto loc_009773B7;
    if (sign_flag) goto loc_009773F9;
loc_00976EE9:
    if ((uint8_t)(v_stack_p8) == 0) goto loc_00976F29;
    if ((*(uint8_t *)(v_rip + 0x493AE4)) != 0) goto loc_00977401;
    if (((v_stack_p18) & (2)) != 0) goto loc_00977401;
loc_00976F0F:
    if ((((uint8_t)(local_rsi)) & (64)) == 0) goto loc_00976F20;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x2C0))) & (0xFFFFFFFEULL));
    goto loc_00976F23;
loc_00976F20:
    result = (uint32_t)((result) | (1));
loc_00976F23:
    *(uint32_t *)(arg1 + 0x2C0) = (uint32_t)(result);
loc_00976F29:
    v_stack_m1A0 = 0;
    v_stack_m1A8 = v_stack_m174;
    v_stack_m1B0 = v_stack_m178;
    v_stack_m1B8 = v_stack_m16C;
    v_stack_m174 = 4;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x4EF45F), *(uint64_t *)(arg1 + 0x28 + 0x8), Arg2, 11);
    Arg3 = 0;
    if (!sign_flag) goto loc_0097740A;
loc_00976F78:
    v_stack_m178 = 0;
loc_00976F7D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18C))) & (0x2000ULL));
    if (!sign_flag) goto loc_009770D4;
    if ((uint32_t)(result) != 0) goto loc_00977486;
loc_00976F99:
loc_00976FAA:
    if (v_stack_p20 != 0) goto loc_0097702E;
loc_00976FB3:
    if (v_stack_m160 != 0) goto loc_00977508;
loc_00976FC1:
    if (v_stack_m138 != 0) {
        result = ExFreePool(v_stack_m138, *(uint64_t *)(arg1 + 0x28 + 0x8), Arg3, 11);
        v_stack_m140 = v_xmm0;
    }
    if (v_stack_m120 != 0) {
        result = ExFreePool(v_stack_m120, *(uint64_t *)(arg1 + 0x28 + 0x8), Arg3, 11);
        v_stack_m128 = v_xmm0;
    }
    result = PiDevCfgFreeDeviceContext(v_stack_m108, *(uint64_t *)(arg1 + 0x28 + 0x8), Arg3, 11);
    if (Arg1 + 40 != 0) {
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = v_rip - 9847251;
        Arg2 = Arg1 + 40;
        result = PnpDiagnosticTraceObjectWithStatus(Arg1, Arg2, Arg3, 11);
    }
    local_rsp = (local_rsp) + (408);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00977023:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) | ((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_m108 = (uint32_t)(result);
    goto loc_00976E12;
loc_0097702E:
    v_stack_p50 = Arg3;
    v_stack_p48 = v_stack_p64;
    v_stack_p40 = 8;
    v_stack_p38 = v_stack_m150;
    v_stack_p30 = v_stack_p6C;
    v_stack_p28 = v_rip - 9847133;
    v_stack_p20 = Arg3;
    v_stack_p64 = 8;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x4EF35A), *(uint64_t *)(arg1 + 0x28 + 0x8), 1, Arg2);
    if (!sign_flag) goto loc_009774E9;
loc_00977092:
    result = 0;
    v_stack_m150 = 0;
loc_00977098:
    v_stack_p30 = v_stack_m130;
    v_stack_p28 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = PiDevCfgLogDeviceConfigured(Arg1, v_stack_m108, v_stack_p78, (uint32_t)(v_stack_p70));
    goto loc_00976FB3;
loc_009770C6:
    if ((uint8_t)(v_stack_p8) == 0) goto loc_00976EE9;
loc_009770D4:
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFDFULL));
    if ((uint32_t)(result) != 0) goto loc_00977425;
loc_009770E7:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)) - 771)) & (0xFFFFFFEEULL)) == 0) goto loc_00977154;
loc_009770FA:
    if (v_stack_p68 != ((uint32_t)(v_stack_p78))) goto loc_00977458;
loc_00977105:
    if (((v_stack_m108) & (1)) != 0) goto loc_00976F99;
    v_stack_p50 = (uint32_t)(v_stack_p78);
    v_stack_p48 = (uint32_t)(v_stack_p78);
    v_stack_p40 = v_stack_p78;
    v_stack_p38 = (uint32_t)(v_stack_p78);
loc_00977123:
    v_stack_p30 = v_rip - 9853558;
    v_stack_p20 = Arg2;
    result = PiDevCfgSetObjectProperty(*(uint64_t *)(v_rip + 0x4EF263), v_stack_m108, *(uint64_t *)(arg1 + 0x28 + 0x8), 1);
loc_00977154:
    if (((uint32_t)(*(uint64_t *)(v_rip + 0x4EF263))) == 787) goto loc_009770FA;
    v_stack_m150 = 128;
loc_009771A4:
    if ((*(uint8_t *)(v_rip + 0x493835)) != 128) goto loc_00976E2A;
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, Arg2 + 80, 1);
    v_stack_p28 = 2;
    v_stack_m90 = (uint32_t)((uint32_t)(0x2012ULL));
    v_stack_m68 = (uint32_t)((uint32_t)(0x2012ULL));
    v_stack_m98 = v_rip - 9847644;
    v_stack_m7C = 6;
    v_stack_m88 = v_stack_m140;
    v_stack_m70 = v_rip - 9847727;
    v_stack_m60 = v_stack_m128;
    v_stack_p20 = v_stack_m98;
    v_stack_m54 = 6;
    result = PiDevCfgQueryObjectProperties(6, *(uint64_t *)(arg1 + 0x28 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 0);
    Arg3 = 0;
    if (sign_flag) goto loc_00976FB3;
    if (v_stack_m78 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m140;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, 0);
        Arg3 = 0;
    }
    if (v_stack_m50 < 0) goto loc_00977360;
loc_0097724E:
    if (v_stack_m138 == 0) goto loc_00976E2A;
    if ((*(uint16_t *)(v_stack_m138)) != 0) goto loc_00976E2A;
    goto loc_00976EA4;
loc_00977355:
    goto loc_00976FEB;
loc_00977360:
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m128, Arg2, Arg3, 0);
    Arg3 = 0;
    goto loc_0097724E;
loc_00977373:
    result = PiDevCfgRequestDriverConfigurations(v_stack_m108, v_stack_p78, Arg3, 0);
    Arg3 = 0;
    goto loc_00976EA4;
loc_0097738C:
    v_stack_p20 = 1;
    v_stack_p8 = (uint8_t)(result);
    goto loc_00976EA4;
loc_0097739E:
    if (1 == 0) goto loc_00976EAE;
loc_009773B7:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000490ULL) goto loc_00976EE9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x660C8A)))) & (2)) == 0) goto loc_00976EE9;
loc_009773F9:
loc_00977401:
    goto loc_00976F0F;
loc_0097740A:
    if (v_stack_p6C != 4) goto loc_00976F78;
    if (v_stack_p64 == 4) goto loc_00976F7D;
    goto loc_00976F78;
loc_00977425:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x194)))) != 56) goto loc_009770E7;
loc_00977458:
    if (((32) & (64)) == 0) goto loc_00977105;
    v_stack_p50 = 0;
    v_stack_p48 = 4;
    v_stack_p40 = v_stack_p68;
    v_stack_p38 = 23;
    goto loc_00977123;
loc_00977486:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x194)))) != 18) goto loc_00976F99;
loc_009774E9:
    if (v_stack_p6C != 9) goto loc_00977092;
    if (v_stack_p64 != 8) goto loc_00977092;
    goto loc_00977098;
loc_00977508:
    result = PiDevCfgFreeDriverNode(v_stack_m108, (uint32_t)(*(uint32_t *)(arg1 + 0x194)), Arg3, 0);
    goto loc_00976FC1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x12C` | `32` | `R` |
| `Arg1` | `+ 0x18C` | `32` | `R` |
| `Arg1` | `+ 0x194` | `32` | `R` |
| `Arg1` | `+ 0x230` | `32` | `R` |
| `Arg1` | `+ 0x2C0` | `32` | `R` |
| `Arg1` | `+ 0x2C0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00976D34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
