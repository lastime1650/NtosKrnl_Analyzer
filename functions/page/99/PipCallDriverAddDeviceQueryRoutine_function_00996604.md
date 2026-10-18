# PipCallDriverAddDeviceQueryRoutine

- RVA: `0x00996604`–`0x00996AED` (길이 `1,257` bytes)
- VA: `0x0000000140996604`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009925C`
- 디코드: `311`개 명령, `1,257/1,257` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0099666E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0099668F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0099669B` → [IopReferenceDriverObjectByName](IopReferenceDriverObjectByName_function_0099C178.md) (function, `0x0099C178`)
- `0x009966DB` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x0099672F` → [PnpIsLegacyDriver](PnpIsLegacyDriver_function_00996220.md) (function, `0x00996220`)
- `0x0099676C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009967B7` → [PipOpenServiceEnumKeys](PipOpenServiceEnumKeys_function_00998E94.md) (function, `0x00998E94`)
- `0x009967D1` → [IopGetDriverNameFromKeyNode](IopGetDriverNameFromKeyNode_function_00998808.md) (function, `0x00998808`)
- `0x009967F9` → [PnpGetServiceStartType](PnpGetServiceStartType_function_00995D78.md) (function, `0x00995D78`)
- `0x0099681E` → [PpInitGetGroupOrderIndex](../../init/C7/PpInitGetGroupOrderIndex_function_00C77534.md) (function, `0x00C77534`)
- `0x00996832` → [PnpLoadBootFilterDriver](../../init/C7/PnpLoadBootFilterDriver_function_00C77938.md) (function, `0x00C77938`)
- `0x009968A1` → [IopLoadDriver](IopLoadDriver_function_00997B54.md) (function, `0x00997B54`)
- `0x009968CE` → [IopReferenceDriverObjectByName](IopReferenceDriverObjectByName_function_0099C178.md) (function, `0x0099C178`)
- `0x00996919` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00996939` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x0099695F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00996983` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009969CB` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x009969FD` → [PnpCheckPossibleBootStartDriver](../72/PnpCheckPossibleBootStartDriver_function_0072D854.md) (function, `0x0072D854`)
- `0x00996A3C` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00996A52` → [PnpCheckPossibleBootStartDriver](../72/PnpCheckPossibleBootStartDriver_function_0072D854.md) (function, `0x0072D854`)
- `0x00996A97` → [IopCallDriverReinitializationRoutines](../A8/IopCallDriverReinitializationRoutines_function_00A8E39C.md) (function, `0x00A8E39C`)
- `0x00996AB3` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00996AC0` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (function, `0x00470708`)
- `0x00996AD6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00996AE3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [PnpCallDriverQueryServiceHelper](PnpCallDriverQueryServiceHelper_function_00995FB0.md) at `0x009960AD`
- [PnpCallDriverQueryServiceHelper](PnpCallDriverQueryServiceHelper_function_00995FB0.md) at `0x00996197`

### Static image references
- `0x00996625` → RVA `0x00AFC700` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00996813` → RVA `0x00F8C5FA` (`.data`; read)
- `0x009968BE` → RVA `0x00F8C380` (`.data`; read)
- `0x009968DF` → RVA `0x00E0A9E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x0099666E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0099668F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009966DB` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x0099676C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0099681E` → [PpInitGetGroupOrderIndex](../../init/C7/PpInitGetGroupOrderIndex_function_00C77534.md) (`PAGE` → `INIT`)
  - `0x00996832` → [PnpLoadBootFilterDriver](../../init/C7/PnpLoadBootFilterDriver_function_00C77938.md) (`PAGE` → `INIT`)
  - `0x0099695F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00996983` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009969CB` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00996AC0` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (`PAGE` → `.text`)
  - `0x00996AD6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00996AE3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x0099671A` → [sub_00B2C3E8 + 0x6C](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x00996856` → [sub_00B2C3E8 + 0x6C](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x009968F5` → [sub_00B2C3E8 + 0x5D](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x00996909` → [sub_00B2C3E8 + 0x5D](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x009969DD` → [sub_00B2C3E8 + 0x9](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x009969E6` → [sub_00B2C3E8](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x009969F4` → [sub_00B2C3E8](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x00996A04` → [sub_00B2C3E8](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x00996A14` → [sub_00B2C3E8](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x00996A74` → [sub_00B2C3E8 + 0x12](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)
  - `0x00996AA5` → [sub_00B2C3E8 + 0x14F](../B2/Unknown_function_00B2C3E8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00996604  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00996609  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0099660E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00996613  55                              push rbp
00996614  41 54                           push r12
00996616  41 55                           push r13
00996618  41 56                           push r14
0099661A  41 57                           push r15
0099661C  48 8B EC                        mov rbp, rsp
0099661F  48 83 EC 60                     sub rsp, 0x60
00996623  33 C0                           xor eax, eax
00996625  4C 8D 3D D4 60 16 00            lea r15, [rip + 0x1660d4]
0099662C  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
0099662F  0F 57 C0                        xorps xmm0, xmm0
00996632  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00996635  0F 57 C9                        xorps xmm1, xmm1
00996638  88 45 30                        mov byte ptr [rbp + 0x30], al
0099663B  49 8B F9                        mov rdi, r9
0099663E  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00996642  8B F0                           mov esi, eax
00996644  8B D8                           mov ebx, eax
00996646  44 8B E8                        mov r13d, eax
00996649  44 8A E0                        mov r12b, al
0099664C  44 8B F0                        mov r14d, eax
0099664F  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00996653  0F 11 4D F0                     movups xmmword ptr [rbp - 0x10], xmm1
00996657  83 F9 01                        cmp ecx, 1
0099665A  0F 85 92 00 00 00               jne 0x1409966f2
00996660  41 83 F8 02                     cmp r8d, 2
00996664  0F 86 88 00 00 00               jbe 0x1409966f2
0099666A  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0099666E  E8 0D 41 A9 FF                  call 0x14042a780
00996673  4C 8B 45 E8                     mov r8, qword ptr [rbp - 0x18]
00996677  33 C0                           xor eax, eax
00996679  8B C8                           mov ecx, eax
0099667B  41 0F B7 17                     movzx edx, word ptr [r15]
0099667F  66 85 D2                        test dx, dx
00996682  0F 85 FF 00 00 00               jne 0x140996787
00996688  49 8B D0                        mov rdx, r8
0099668B  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0099668F  E8 EC 40 A9 FF                  call 0x14042a780
00996694  41 B7 01                        mov r15b, 1
00996697  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0099669B  E8 D8 5A 00 00                  call 0x14099c178
009966A0  44 8B 65 50                     mov r12d, dword ptr [rbp + 0x50]
009966A4  48 8B F0                        mov rsi, rax
009966A7  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
009966AB  48 85 C0                        test rax, rax
009966AE  75 61                           jne 0x140996711
009966B0  33 DB                           xor ebx, ebx
009966B2  45 84 FF                        test r15b, r15b
009966B5  0F 84 33 01 00 00               je 0x1409967ee
009966BB  BB 01 00 00 C0                  mov ebx, 0xc0000001
009966C0  44 8A 65 30                     mov r12b, byte ptr [rbp + 0x30]
009966C4  4D 85 F6                        test r14, r14
009966C7  0F 85 06 04 00 00               jne 0x140996ad3
009966CD  45 84 E4                        test r12b, r12b
009966D0  74 15                           je 0x1409966e7
009966D2  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
009966D6  48 85 C9                        test rcx, rcx
009966D9  74 0C                           je 0x1409966e7
009966DB  E8 70 C1 1E 00                  call 0x140b82850
009966E0  0F 57 C0                        xorps xmm0, xmm0
009966E3  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
009966E7  48 85 F6                        test rsi, rsi
009966EA  0F 85 F0 03 00 00               jne 0x140996ae0
009966F0  8B C3                           mov eax, ebx
009966F2  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
009966F7  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
009966FB  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
009966FF  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00996703  49 8B E3                        mov rsp, r11
00996706  41 5F                           pop r15
00996708  41 5E                           pop r14
0099670A  41 5D                           pop r13
0099670C  41 5C                           pop r12
0099670E  5D                              pop rbp
0099670F  C3                              ret
00996710  CC                              int3
00996711  41 BF 6C 02 00 C0               mov r15d, 0xc000026c
00996717  48 85 F6                        test rsi, rsi
0099671A  0F 84 34 5D 19 00               je 0x140b2c454
00996720  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
00996723  BA 10 00 00 00                  mov edx, 0x10
00996728  84 C2                           test dl, al
0099672A  74 8F                           je 0x1409966bb
0099672C  48 8B CE                        mov rcx, rsi
0099672F  E8 EC FA FF FF                  call 0x140996220
00996734  85 C0                           test eax, eax
00996736  0F 85 65 03 00 00               jne 0x140996aa1
0099673C  48 8B 07                        mov rax, qword ptr [rdi]
0099673F  8B 88 2C 01 00 00               mov ecx, dword ptr [rax + 0x12c]
00996745  81 E9 03 03 00 00               sub ecx, 0x303
0099674B  83 F9 02                        cmp ecx, 2
0099674E  0F 87 67 FF FF FF               ja 0x1409966bb
00996754  4A 8D 3C E7                     lea rdi, [rdi + r12*8]
00996758  B9 00 01 00 00                  mov ecx, 0x100
0099675D  45 33 E4                        xor r12d, r12d
00996760  41 B8 50 70 65 6E               mov r8d, 0x6e657050
00996766  41 8B DC                        mov ebx, r12d
00996769  48 03 FA                        add rdi, rdx
0099676C  E8 7F B9 1E 00                  call 0x140b820f0
00996771  48 8B C8                        mov rcx, rax
00996774  48 85 C0                        test rax, rax
00996777  0F 85 DE 00 00 00               jne 0x14099685b
0099677D  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00996782  E9 39 FF FF FF                  jmp 0x1409966c0
00996787  8B C1                           mov eax, ecx
00996789  66 41 39 14 40                  cmp word ptr [r8 + rax*2], dx
0099678E  0F 84 F9 01 00 00               je 0x14099698d
00996794  48 8B 07                        mov rax, qword ptr [rdi]
00996797  66 44 39 70 38                  cmp word ptr [rax + 0x38], r14w
0099679C  0F 84 A5 01 00 00               je 0x140996947
009967A2  45 33 C9                        xor r9d, r9d
009967A5  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
009967AA  4C 8D 45 D8                     lea r8, [rbp - 0x28]
009967AE  BA 19 00 02 00                  mov edx, 0x20019
009967B3  48 8D 4D E0                     lea rcx, [rbp - 0x20]
009967B7  E8 D8 26 00 00                  call 0x140998e94
009967BC  8B D8                           mov ebx, eax
009967BE  85 C0                           test eax, eax
009967C0  0F 88 5D 01 00 00               js 0x140996923
009967C6  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
009967CA  48 8D 55 F0                     lea rdx, [rbp - 0x10]
009967CE  49 8B CE                        mov rcx, r14
009967D1  E8 32 20 00 00                  call 0x140998808
009967D6  8B D8                           mov ebx, eax
009967D8  33 C0                           xor eax, eax
009967DA  85 DB                           test ebx, ebx
009967DC  0F 88 2C 01 00 00               js 0x14099690e
009967E2  C6 45 30 01                     mov byte ptr [rbp + 0x30], 1
009967E6  44 8A F8                        mov r15b, al
009967E9  E9 A9 FE FF FF                  jmp 0x140996697
009967EE  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
009967F2  4C 8D 45 D4                     lea r8, [rbp - 0x2c]
009967F6  49 8B D6                        mov rdx, r14
009967F9  E8 7A F5 FF FF                  call 0x140995d78
009967FE  44 8B 7D D4                     mov r15d, dword ptr [rbp - 0x2c]
00996802  85 C0                           test eax, eax
00996804  B9 04 00 00 00                  mov ecx, 4
00996809  44 0F 48 F9                     cmovs r15d, ecx
0099680D  41 83 FC 03                     cmp r12d, 3
00996811  74 66                           je 0x140996879
00996813  38 1D E1 5D 5F 00               cmp byte ptr [rip + 0x5f5de1], bl
00996819  75 5E                           jne 0x140996879
0099681B  49 8B CE                        mov rcx, r14
0099681E  E8 11 0D 2E 00                  call 0x140c77534
00996823  44 0F B7 C0                     movzx r8d, ax
00996827  4C 8D 4D D8                     lea r9, [rbp - 0x28]
0099682B  48 8D 55 F0                     lea rdx, [rbp - 0x10]
0099682F  49 8B CE                        mov rcx, r14
00996832  E8 01 11 2E 00                  call 0x140c77938
00996837  33 F6                           xor esi, esi
00996839  8B D8                           mov ebx, eax
0099683B  85 C0                           test eax, eax
0099683D  0F 88 92 01 00 00               js 0x1409969d5
00996843  48 8B 75 D8                     mov rsi, qword ptr [rbp - 0x28]
00996847  48 85 F6                        test rsi, rsi
0099684A  0F 85 78 01 00 00               jne 0x1409969c8
00996850  41 BF 6C 02 00 C0               mov r15d, 0xc000026c
00996856  E9 F9 5B 19 00                  jmp 0x140b2c454
0099685B  48 89 30                        mov qword ptr [rax], rsi
0099685E  49 8B F4                        mov rsi, r12
00996861  4C 89 60 08                     mov qword ptr [rax + 8], r12
00996865  48 8B 07                        mov rax, qword ptr [rdi]
00996868  48 85 C0                        test rax, rax
0099686B  0F 85 59 02 00 00               jne 0x140996aca
00996871  48 89 0F                        mov qword ptr [rdi], rcx
00996874  E9 47 FE FF FF                  jmp 0x1409966c0
00996879  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0099687D  44 3B 38                        cmp r15d, dword ptr [rax]
00996880  0F 87 93 01 00 00               ja 0x140996a19
00996886  38 58 04                        cmp byte ptr [rax + 4], bl
00996889  0F 84 B7 01 00 00               je 0x140996a46
0099688F  8A 55 58                        mov dl, byte ptr [rbp + 0x58]
00996892  4C 8D 4D D0                     lea r9, [rbp - 0x30]
00996896  41 83 FC 03                     cmp r12d, 3
0099689A  49 8B CE                        mov rcx, r14
0099689D  41 0F 95 C0                     setne r8b
009968A1  E8 AE 12 00 00                  call 0x140997b54
009968A6  33 D2                           xor edx, edx
009968A8  8B D8                           mov ebx, eax
009968AA  44 8B F2                        mov r14d, edx
009968AD  44 8B E8                        mov r13d, eax
009968B0  85 C0                           test eax, eax
009968B2  0F 88 B6 01 00 00               js 0x140996a6e
009968B8  41 BF 6C 02 00 C0               mov r15d, 0xc000026c
009968BE  38 15 BC 5A 5F 00               cmp byte ptr [rip + 0x5f5abc], dl
009968C4  0F 85 CB 01 00 00               jne 0x140996a95
009968CA  48 8D 4D F0                     lea rcx, [rbp - 0x10]
009968CE  E8 A5 58 00 00                  call 0x14099c178
009968D3  48 8B F0                        mov rsi, rax
009968D6  48 85 C0                        test rax, rax
009968D9  0F 85 38 FE FF FF               jne 0x140996717
009968DF  44 38 35 FA 40 47 00            cmp byte ptr [rip + 0x4740fa], r14b
009968E6  0F 84 2B FE FF FF               je 0x140996717
009968EC  8D 83 A1 FC FF 3F               lea eax, [rbx + 0x3ffffca1]
009968F2  83 F8 0D                        cmp eax, 0xd
009968F5  0F 87 4A 5B 19 00               ja 0x140b2c445
009968FB  B9 41 30 00 00                  mov ecx, 0x3041
00996900  0F A3 C1                        bt ecx, eax
00996903  0F 82 0E FE FF FF               jb 0x140996717
00996909  E9 37 5B 19 00                  jmp 0x140b2c445
0099690E  48 8B 0F                        mov rcx, qword ptr [rdi]
00996911  44 8B C3                        mov r8d, ebx
00996914  BA 13 00 00 00                  mov edx, 0x13
00996919  E8 EE 74 F6 FF                  call 0x1408fde0c
0099691E  E9 A1 FD FF FF                  jmp 0x1409966c4
00996923  3D 34 00 00 C0                  cmp eax, 0xc0000034
00996928  0F 84 88 00 00 00               je 0x1409969b6
0099692E  48 8B 0F                        mov rcx, qword ptr [rdi]
00996931  44 8B C0                        mov r8d, eax
00996934  BA 13 00 00 00                  mov edx, 0x13
00996939  E8 CE 74 F6 FF                  call 0x1408fde0c
0099693E  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
00996942  E9 7D FD FF FF                  jmp 0x1409966c4
00996947  0F 10 45 E0                     movups xmm0, xmmword ptr [rbp - 0x20]
0099694B  B9 00 01 00 00                  mov ecx, 0x100
00996950  41 B8 50 6E 70 48               mov r8d, 0x48706e50
00996956  F3 0F 7F 40 38                  movdqu xmmword ptr [rax + 0x38], xmm0
0099695B  0F B7 55 E2                     movzx edx, word ptr [rbp - 0x1e]
0099695F  E8 8C B7 1E 00                  call 0x140b820f0
00996964  48 8B C8                        mov rcx, rax
00996967  48 8B 07                        mov rax, qword ptr [rdi]
0099696A  48 89 48 40                     mov qword ptr [rax + 0x40], rcx
0099696E  48 8B 07                        mov rax, qword ptr [rdi]
00996971  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
00996975  48 85 C9                        test rcx, rcx
00996978  74 1E                           je 0x140996998
0099697A  44 0F B7 45 E2                  movzx r8d, word ptr [rbp - 0x1e]
0099697F  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00996983  E8 B8 FE D2 FF                  call 0x1406c6840
00996988  E9 15 FE FF FF                  jmp 0x1409967a2
0099698D  FF C1                           inc ecx
0099698F  49 83 C7 02                     add r15, 2
00996993  E9 E3 FC FF FF                  jmp 0x14099667b
00996998  66 44 89 70 3A                  mov word ptr [rax + 0x3a], r14w
0099699D  BB 01 00 00 C0                  mov ebx, 0xc0000001
009969A2  48 8B 07                        mov rax, qword ptr [rdi]
009969A5  66 44 89 70 38                  mov word ptr [rax + 0x38], r14w
009969AA  48 8B 07                        mov rax, qword ptr [rdi]
009969AD  4C 89 70 40                     mov qword ptr [rax + 0x40], r14
009969B1  E9 3A FD FF FF                  jmp 0x1409966f0
009969B6  44 39 75 50                     cmp dword ptr [rbp + 0x50], r14d
009969BA  0F 85 6E FF FF FF               jne 0x14099692e
009969C0  41 8B DE                        mov ebx, r14d
009969C3  E9 76 FF FF FF                  jmp 0x14099693e
009969C8  48 8B CE                        mov rcx, rsi
009969CB  E8 50 90 87 FF                  call 0x14020fa20
009969D0  E9 3C FD FF FF                  jmp 0x140996711
009969D5  05 95 FC FF 3F                  add eax, 0x3ffffc95
009969DA  83 F8 01                        cmp eax, 1
009969DD  0F 86 0E 5A 19 00               jbe 0x140b2c3f1
009969E3  45 85 FF                        test r15d, r15d
009969E6  0F 84 FC 59 19 00               je 0x140b2c3e8
009969EC  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009969F0  40 38 70 04                     cmp byte ptr [rax + 4], sil
009969F4  0F 85 EE 59 19 00               jne 0x140b2c3e8
009969FA  49 8B CE                        mov rcx, r14
009969FD  E8 52 6E D9 FF                  call 0x14072d854
00996A02  84 C0                           test al, al
00996A04  0F 85 DE 59 19 00               jne 0x140b2c3e8
00996A0A  48 8B 07                        mov rax, qword ptr [rdi]
00996A0D  C6 80 B0 02 00 00 01            mov byte ptr [rax + 0x2b0], 1
00996A14  E9 CF 59 19 00                  jmp 0x140b2c3e8
00996A19  44 3B F9                        cmp r15d, ecx
00996A1C  0F 85 99 FC FF FF               jne 0x1409966bb
00996A22  48 8B 0F                        mov rcx, qword ptr [rdi]
00996A25  F7 81 8C 01 00 00 00 60 00 00   test dword ptr [rcx + 0x18c], 0x6000
00996A2F  0F 85 86 FC FF FF               jne 0x1409966bb
00996A35  45 33 C0                        xor r8d, r8d
00996A38  41 8D 50 20                     lea edx, [r8 + 0x20]
00996A3C  E8 CB 73 F6 FF                  call 0x1408fde0c
00996A41  E9 75 FC FF FF                  jmp 0x1409966bb
00996A46  45 85 FF                        test r15d, r15d
00996A49  0F 84 6C FC FF FF               je 0x1409966bb
00996A4F  49 8B CE                        mov rcx, r14
00996A52  E8 FD 6D D9 FF                  call 0x14072d854
00996A57  84 C0                           test al, al
00996A59  0F 85 5C FC FF FF               jne 0x1409966bb
00996A5F  48 8B 07                        mov rax, qword ptr [rdi]
00996A62  C6 80 B0 02 00 00 01            mov byte ptr [rax + 0x2b0], 1
00996A69  E9 4D FC FF FF                  jmp 0x1409966bb
00996A6E  81 FB 65 03 00 C0               cmp ebx, 0xc0000365
00996A74  0F 85 80 59 19 00               jne 0x140b2c3fa
00996A7A  B8 9A 00 00 C0                  mov eax, 0xc000009a
00996A7F  41 BF 6C 02 00 C0               mov r15d, 0xc000026c
00996A85  39 45 D0                        cmp dword ptr [rbp - 0x30], eax
00996A88  0F 85 30 FE FF FF               jne 0x1409968be
00996A8E  8B D8                           mov ebx, eax
00996A90  E9 29 FE FF FF                  jmp 0x1409968be
00996A95  33 C9                           xor ecx, ecx
00996A97  E8 00 79 0F 00                  call 0x140a8e39c
00996A9C  E9 29 FE FF FF                  jmp 0x1409968ca
00996AA1  41 83 FC 03                     cmp r12d, 3
00996AA5  0F 85 8C 5A 19 00               jne 0x140b2c537
00996AAB  48 8B 0F                        mov rcx, qword ptr [rdi]
00996AAE  BA 00 10 00 00                  mov edx, 0x1000
00996AB3  E8 90 55 F6 FF                  call 0x1408fc048
00996AB8  48 8B 0F                        mov rcx, qword ptr [rdi]
00996ABB  BA 0A 03 00 00                  mov edx, 0x30a
00996AC0  E8 43 9C AD FF                  call 0x140470708
00996AC5  E9 F1 FB FF FF                  jmp 0x1409966bb
00996ACA  48 8D 78 08                     lea rdi, [rax + 8]
00996ACE  E9 92 FD FF FF                  jmp 0x140996865
00996AD3  49 8B CE                        mov rcx, r14
00996AD6  E8 D5 67 D1 FF                  call 0x1406ad2b0
00996ADB  E9 ED FB FF FF                  jmp 0x1409966cd
00996AE0  48 8B CE                        mov rcx, rsi
00996AE3  E8 68 28 96 FF                  call 0x1402f9350
00996AE8  E9 03 FC FF FF                  jmp 0x1409966f0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipCallDriverAddDeviceQueryRoutine(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int16 v_stack_m46;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_stack_m54 = 0;
    v_stack_m58 = 0;
    v_stack_p8 = 0;
    v_stack_m50 = 0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm1;
    if (a1 != 1) goto loc_009966F2;
    if (a3 <= 2) goto loc_009966F2;
    result = RtlInitUnicodeString(v_stack_m48, a2, a3, a4);
    result = 0;
loc_0099667B:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 1466580)) != 0) goto loc_00996787;
    result = RtlInitUnicodeString(v_stack_m38, v_stack_m40, v_stack_m40, a4);
loc_00996697:
    result = IopReferenceDriverObjectByName(v_stack_m38, v_stack_m40, v_stack_m40, a4);
    v_stack_m50 = result;
    if (result != 0) goto loc_00996711;
    v_rbx = 0;
    if (1 == 0) goto loc_009967EE;
loc_009966BB:
loc_009966C0:
loc_009966C4:
    if (0 != 0) goto loc_00996AD3;
loc_009966CD:
    if ((unsigned __int8)(v_stack_p8) == 0) goto loc_009966E7;
    if (v_stack_m30 != 0) {
        result = ExFreePool(v_stack_m30, v_stack_m40, v_stack_m40, a4);
        v_stack_m38 = v_xmm0;
    }
    if (result != 0) goto loc_00996AE0;
loc_009966F0:
loc_009966F2:
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000001ULL)));
loc_00996711:
loc_00996717:
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 16))))) == 0) goto loc_009966BB;
    result = PnpIsLegacyDriver(*(unsigned __int64 *)(v_stack_m28 + 64), 16, v_stack_m40, a4);
    if ((unsigned int)(result) != 0) goto loc_00996AA1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)) + 300))) - (771));
    if (a1 > 2) goto loc_009966BB;
    v_r12 = 0;
    v_rdi = (*(unsigned __int64 *)(v_stack_m28 + 72) + v_stack_p8 * 8) + (16);
    result = ExAllocatePool2(256, 16, (unsigned int)(0x6E657050ULL), a4);
    if (result != 0) goto loc_0099685B;
    goto loc_009966C0;
loc_00996787:
    if ((*(unsigned __int16 *)((unsigned int)(0x6E657050ULL) + (unsigned int)((unsigned int)(result)) * 2)) == 16) goto loc_0099698D;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi) + 56)) == 0) goto loc_00996947;
loc_009967A2:
    a4 = 0;
    v_stack_m40 = 0;
    result = PipOpenServiceEnumKeys(v_stack_m48, (unsigned int)(0x20019ULL), v_stack_m50, a4);
    if (sign_flag) goto loc_00996923;
    result = IopGetDriverNameFromKeyNode(v_stack_m50, v_stack_m38, v_stack_m50, a4);
    result = 0;
    if (sign_flag) goto loc_0099690E;
    v_stack_p8 = 1;
    goto loc_00996697;
loc_009967EE:
    result = PnpGetServiceStartType(v_stack_m40, v_stack_m50, v_stack_m54, a4);
    v_r15 = (unsigned int)(v_stack_m54);
    if (sign_flag) { v_r15 = 4; }
    if (0 == 3) goto loc_00996879;
    if ((*(unsigned __int8 *)(v_rip + 6249953)) != ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00996879;
    result = PpInitGetGroupOrderIndex(v_stack_m50, v_stack_m50, v_stack_m54, a4);
    result = PnpLoadBootFilterDriver(v_stack_m50, v_stack_m38, (unsigned __int16)(result), v_stack_m50);
    v_rsi = 0;
    if (sign_flag) goto loc_009969D5;
    if (v_stack_m50 != 0) goto loc_009969C8;
loc_0099685B:
    *(unsigned __int64 *)(result) = v_stack_m50;
    *(unsigned __int64 *)(result + 8) = 0;
loc_00996865:
    if (*(unsigned __int64 *)(v_rdi) != 0) goto loc_00996ACA;
    *(unsigned __int64 *)(v_rdi) = v_stack_m50;
    goto loc_009966C0;
loc_00996879:
    if (((unsigned int)((unsigned int)(0xC000026CULL))) > (*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 8)))) goto loc_00996A19;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 8) + 4)) == ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00996A46;
    a3 = (0 != 3) ? 1 : 0;
    result = IopLoadDriver(v_stack_m50, a6, a3, v_stack_m58);
    a2 = 0;
    if (sign_flag) goto loc_00996A6E;
loc_009968BE:
    if ((*(unsigned __int8 *)(v_rip + 6249148)) != 0) goto loc_00996A95;
loc_009968CA:
    result = IopReferenceDriverObjectByName(v_stack_m38, a2, a3, v_stack_m58);
    if (result != 0) goto loc_00996717;
    if ((*(unsigned __int8 *)(v_rip + 4669690)) == 0) goto loc_00996717;
    if (((unsigned int)((unsigned int)((unsigned int)(result)) + 1073740961)) < 13) goto loc_00996717;
loc_0099690E:
    result = PipSetDevNodeProblem(*(unsigned __int64 *)(v_rdi), 19, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m58);
    goto loc_009966C4;
loc_00996923:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_009969B6;
loc_0099692E:
    result = PipSetDevNodeProblem(*(unsigned __int64 *)(v_rdi), 19, (unsigned int)((unsigned int)(result)), v_stack_m58);
loc_0099693E:
    goto loc_009966C4;
loc_00996947:
    *(unsigned __int64 *)(result + 56) = v_xmm0;
    result = ExAllocatePool2(256, v_stack_m46, (unsigned int)(0x48706E50ULL), v_stack_m58);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 64) = result;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 64) == 0) goto loc_00996998;
    result = memcpy(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 64), v_stack_m40, v_stack_m46, v_stack_m58);
    goto loc_009967A2;
loc_0099698D:
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 64)) + 1);
    v_r15 = ((unsigned int)(0xC000026CULL)) + (2);
    goto loc_0099667B;
loc_00996998:
    *(unsigned __int16 *)(result + 58) = (unsigned __int16)(v_stack_m50);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi) + 56) = (unsigned __int16)(v_stack_m50);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 64) = v_stack_m50;
    goto loc_009966F0;
loc_009969B6:
    if (a5 != ((unsigned int)(v_stack_m50))) goto loc_0099692E;
    goto loc_0099693E;
loc_009969C8:
    result = ObfReferenceObject(result, v_stack_m40, v_stack_m46, v_stack_m58);
    goto loc_00996711;
loc_009969D5:
    result = (unsigned int)((result) + (0x3FFFFC95ULL));
    result = PnpCheckPossibleBootStartDriver(v_stack_m50, v_stack_m40, v_stack_m46, v_stack_m58);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi) + 688) = 1;
loc_00996A19:
    if (((unsigned int)(v_r15)) != ((unsigned int)(v_stack_m50))) goto loc_009966BB;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 396)) & (0x6000ULL)) != 0) goto loc_009966BB;
    a3 = 0;
    result = PipSetDevNodeProblem(*(unsigned __int64 *)(v_rdi), a3 + 32, a3, v_stack_m58);
    goto loc_009966BB;
loc_00996A46:
    if ((unsigned int)(v_r15) == 0) goto loc_009966BB;
    result = PnpCheckPossibleBootStartDriver(v_stack_m50, a3 + 32, a3, v_stack_m58);
    if ((unsigned __int8)(result) != 0) goto loc_009966BB;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi) + 688) = 1;
    goto loc_009966BB;
loc_00996A6E:
    if (v_stack_m58 != ((unsigned int)((unsigned int)(0xC000009AULL)))) goto loc_009968BE;
    goto loc_009968BE;
loc_00996A95:
    a1 = 0;
    result = IopCallDriverReinitializationRoutines(a1, a3 + 32, a3, v_stack_m58);
    goto loc_009968CA;
loc_00996AA1:
    result = PipSetDevNodeFlags(*(unsigned __int64 *)(v_rdi), (unsigned int)(0x1000ULL), a3, v_stack_m58);
    result = PipSetDevNodeState(*(unsigned __int64 *)(v_rdi), 778, a3, v_stack_m58);
    goto loc_009966BB;
loc_00996ACA:
    goto loc_00996865;
loc_00996AD3:
    result = ZwClose(v_stack_m50, 778, a3, v_stack_m58);
    goto loc_009966CD;
loc_00996AE0:
    result = ObfDereferenceObject(result, 778, a3, v_stack_m58);
    goto loc_009966F0;
}
```

## 5. (Beta) C Style

```c
int64_t PipCallDriverAddDeviceQueryRoutine(int32_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4, uint32_t Arg5, uint8_t Arg6)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint16_t v_stack_m46;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (96);
    result = 0;
    v_stack_m54 = 0;
    v_stack_m58 = 0;
    v_stack_p8 = 0;
    v_stack_m50 = 0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm1;
    if (Arg1 != 1) goto loc_009966F2;
    if (Arg3 <= 2) goto loc_009966F2;
    result = RtlInitUnicodeString(v_stack_m48, Arg2, Arg3, Arg4);
    result = 0;
loc_0099667B:
    if ((uint16_t)(*(uint16_t *)(v_rip + 0x1660D4)) != 0) goto loc_00996787;
    result = RtlInitUnicodeString(v_stack_m38, v_stack_m40, v_stack_m40, Arg4);
loc_00996697:
    result = IopReferenceDriverObjectByName(v_stack_m38, v_stack_m40, v_stack_m40, Arg4);
    v_stack_m50 = result;
    if (result != 0) goto loc_00996711;
    local_rbx = 0;
    if (1 == 0) goto loc_009967EE;
loc_009966BB:
loc_009966C0:
loc_009966C4:
    if (0 != 0) goto loc_00996AD3;
loc_009966CD:
    if ((uint8_t)(v_stack_p8) == 0) goto loc_009966E7;
    if (v_stack_m30 != 0) {
        result = ExFreePool(v_stack_m30, v_stack_m40, v_stack_m40, Arg4);
        v_stack_m38 = v_xmm0;
    }
    if (result != 0) goto loc_00996AE0;
loc_009966F0:
loc_009966F2:
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000001ULL)));
loc_00996711:
loc_00996717:
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x10))))) == 0) goto loc_009966BB;
    result = PnpIsLegacyDriver(*(uint64_t *)(v_stack_m28 + 0x40), 16, v_stack_m40, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00996AA1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)) + 0x12C))) - (771));
    if (Arg1 > 2) goto loc_009966BB;
    local_r12 = 0;
    local_rdi = (*(uint64_t *)(v_stack_m28 + 0x48) + v_stack_p8 * 8) + (16);
    result = ExAllocatePool2(256, 16, (uint32_t)(0x6E657050ULL), Arg4);
    if (result != 0) goto loc_0099685B;
    goto loc_009966C0;
loc_00996787:
    if ((*(uint16_t *)((uint32_t)(0x6E657050ULL) + (uint32_t)((uint32_t)(result)) * 2)) == 16) goto loc_0099698D;
    if ((*(uint16_t *)(*(uint64_t *)(local_rdi) + 0x38)) == 0) goto loc_00996947;
loc_009967A2:
    Arg4 = 0;
    v_stack_m40 = 0;
    result = PipOpenServiceEnumKeys(v_stack_m48, (uint32_t)(0x20019ULL), v_stack_m50, Arg4);
    if (sign_flag) goto loc_00996923;
    result = IopGetDriverNameFromKeyNode(v_stack_m50, v_stack_m38, v_stack_m50, Arg4);
    result = 0;
    if (sign_flag) goto loc_0099690E;
    v_stack_p8 = 1;
    goto loc_00996697;
loc_009967EE:
    result = PnpGetServiceStartType(v_stack_m40, v_stack_m50, v_stack_m54, Arg4);
    local_r15 = (uint32_t)(v_stack_m54);
    if (sign_flag) { local_r15 = 4; }
    if (0 == 3) goto loc_00996879;
    if ((*(uint8_t *)(v_rip + 0x5F5DE1)) != ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00996879;
    result = PpInitGetGroupOrderIndex(v_stack_m50, v_stack_m50, v_stack_m54, Arg4);
    result = PnpLoadBootFilterDriver(v_stack_m50, v_stack_m38, (uint16_t)(result), v_stack_m50);
    local_rsi = 0;
    if (sign_flag) goto loc_009969D5;
    if (v_stack_m50 != 0) goto loc_009969C8;
loc_0099685B:
    *(uint64_t *)(result) = v_stack_m50;
    *(uint64_t *)(result + 0x8) = 0;
loc_00996865:
    if (*(uint64_t *)(local_rdi) != 0) goto loc_00996ACA;
    *(uint64_t *)(local_rdi) = v_stack_m50;
    goto loc_009966C0;
loc_00996879:
    if (((uint32_t)((uint32_t)(0xC000026CULL))) > (*(uint32_t *)(*(uint64_t *)(local_rdi + 0x8)))) goto loc_00996A19;
    if ((*(uint8_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x4)) == ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00996A46;
    Arg3 = (0 != 3) ? 1 : 0;
    result = IopLoadDriver(v_stack_m50, Arg6, Arg3, v_stack_m58);
    Arg2 = 0;
    if (sign_flag) goto loc_00996A6E;
loc_009968BE:
    if ((*(uint8_t *)(v_rip + 0x5F5ABC)) != 0) goto loc_00996A95;
loc_009968CA:
    result = IopReferenceDriverObjectByName(v_stack_m38, Arg2, Arg3, v_stack_m58);
    if (result != 0) goto loc_00996717;
    if ((*(uint8_t *)(v_rip + 0x4740FA)) == 0) goto loc_00996717;
    if (((uint32_t)((uint32_t)((uint32_t)(result)) + 1073740961)) < 13) goto loc_00996717;
loc_0099690E:
    result = PipSetDevNodeProblem(*(uint64_t *)(local_rdi), 19, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m58);
    goto loc_009966C4;
loc_00996923:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_009969B6;
loc_0099692E:
    result = PipSetDevNodeProblem(*(uint64_t *)(local_rdi), 19, (uint32_t)((uint32_t)(result)), v_stack_m58);
loc_0099693E:
    goto loc_009966C4;
loc_00996947:
    *(uint64_t *)(result + 0x38) = v_xmm0;
    result = ExAllocatePool2(256, v_stack_m46, (uint32_t)(0x48706E50ULL), v_stack_m58);
    *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x40) = result;
    if (*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x40) == 0) goto loc_00996998;
    result = memcpy(*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x40), v_stack_m40, v_stack_m46, v_stack_m58);
    goto loc_009967A2;
loc_0099698D:
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x40)) + 1);
    local_r15 = ((uint32_t)(0xC000026CULL)) + (2);
    goto loc_0099667B;
loc_00996998:
    *(uint16_t *)(result + 0x3A) = (uint16_t)(v_stack_m50);
    *(uint16_t *)(*(uint64_t *)(local_rdi) + 0x38) = (uint16_t)(v_stack_m50);
    *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x40) = v_stack_m50;
    goto loc_009966F0;
loc_009969B6:
    if (Arg5 != ((uint32_t)(v_stack_m50))) goto loc_0099692E;
    goto loc_0099693E;
loc_009969C8:
    result = ObfReferenceObject(result, v_stack_m40, v_stack_m46, v_stack_m58);
    goto loc_00996711;
loc_009969D5:
    result = (uint32_t)((result) + (0x3FFFFC95ULL));
    result = PnpCheckPossibleBootStartDriver(v_stack_m50, v_stack_m40, v_stack_m46, v_stack_m58);
    *(uint8_t *)(*(uint64_t *)(local_rdi) + 0x2B0) = 1;
loc_00996A19:
    if (((uint32_t)(local_r15)) != ((uint32_t)(v_stack_m50))) goto loc_009966BB;
    if (((*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x18C)) & (0x6000ULL)) != 0) goto loc_009966BB;
    Arg3 = 0;
    result = PipSetDevNodeProblem(*(uint64_t *)(local_rdi), Arg3 + 32, Arg3, v_stack_m58);
    goto loc_009966BB;
loc_00996A46:
    if ((uint32_t)(local_r15) == 0) goto loc_009966BB;
    result = PnpCheckPossibleBootStartDriver(v_stack_m50, Arg3 + 32, Arg3, v_stack_m58);
    if ((uint8_t)(result) != 0) goto loc_009966BB;
    *(uint8_t *)(*(uint64_t *)(local_rdi) + 0x2B0) = 1;
    goto loc_009966BB;
loc_00996A6E:
    if (v_stack_m58 != ((uint32_t)((uint32_t)(0xC000009AULL)))) goto loc_009968BE;
    goto loc_009968BE;
loc_00996A95:
    Arg1 = 0;
    result = IopCallDriverReinitializationRoutines(Arg1, Arg3 + 32, Arg3, v_stack_m58);
    goto loc_009968CA;
loc_00996AA1:
    result = PipSetDevNodeFlags(*(uint64_t *)(local_rdi), (uint32_t)(0x1000ULL), Arg3, v_stack_m58);
    result = PipSetDevNodeState(*(uint64_t *)(local_rdi), 778, Arg3, v_stack_m58);
    goto loc_009966BB;
loc_00996ACA:
    goto loc_00996865;
loc_00996AD3:
    result = ZwClose(v_stack_m50, 778, Arg3, v_stack_m58);
    goto loc_009966CD;
loc_00996AE0:
    result = ObfDereferenceObject(result, 778, Arg3, v_stack_m58);
    goto loc_009966F0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0 + r12*8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00996604&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
