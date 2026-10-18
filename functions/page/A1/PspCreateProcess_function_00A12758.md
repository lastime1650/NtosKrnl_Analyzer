# PspCreateProcess

- RVA: `0x00A12758`–`0x00A12D4F` (길이 `1,527` bytes)
- VA: `0x0000000140A12758`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9918`
- 디코드: `330`개 명령, `1,527/1,527` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00A12901` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A1291E` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00A12997` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A129F7` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00A12A1F` → [PspReferenceTokenForNewProcess](PspReferenceTokenForNewProcess_function_00A12D58.md) (function, `0x00A12D58`)
- `0x00A12A7B` → [SeQuerySigningPolicy](SeQuerySigningPolicy_function_00A12F44.md) (function, `0x00A12F44`)
- `0x00A12AF9` → [PspGetProcessProtectionRequirementsFromImage](../A6/PspGetProcessProtectionRequirementsFromImage_function_00A6DCF4.md) (function, `0x00A6DCF4`)
- `0x00A12B7C` → [PsCreateMinimalProcess](../78/PsCreateMinimalProcess_function_00786D14.md) (function, `0x00786D14`)
- `0x00A12C00` → [PspAllocateProcess](PspAllocateProcess_function_00A13B3C.md) (function, `0x00A13B3C`)
- `0x00A12C69` → [PspInsertProcess](../94/PspInsertProcess_function_009472CC.md) (function, `0x009472CC`)
- `0x00A12C8B` → [PspCreateObjectHandle](PspCreateObjectHandle_function_00A1E51C.md) (function, `0x00A1E51C`)
- `0x00A12CCC` → [SeDeleteAccessState](../8C/SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x00A12CDF` → [PspRundownSingleProcess](../90/PspRundownSingleProcess_function_00906D50.md) (function, `0x00906D50`)
- `0x00A12CF1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A12CFE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A12D10` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A12D1D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A12D36` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtCreateProcessEx](../78/NtCreateProcessEx_function_00780AA0.md) at `0x00780B20`
- [PspInitPhase0](../../init/C7/PspInitPhase0_function_00C77E2C.md) at `0x00C788E1`

### Static image references
- `0x00A1276B` → RVA `0x00E0A740` (`.data`; read)
- `0x00A1296B` → RVA `0x00FC6BD8` (`ALMOSTRO`; read)
- `0x00A129C6` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00A12AD1` → RVA `0x00B4AEF7` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00A12901` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A12CF1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A12CFE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A12D10` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A12D1D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A12D36` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A12758  40 53                           push rbx
00A1275A  56                              push rsi
00A1275B  57                              push rdi
00A1275C  41 54                           push r12
00A1275E  41 55                           push r13
00A12760  41 56                           push r14
00A12762  41 57                           push r15
00A12764  48 81 EC 80 02 00 00            sub rsp, 0x280
00A1276B  48 8B 05 CE 7F 3F 00            mov rax, qword ptr [rip + 0x3f7fce]
00A12772  48 33 C4                        xor rax, rsp
00A12775  48 89 84 24 70 02 00 00         mov qword ptr [rsp + 0x270], rax
00A1277D  49 8B F1                        mov rsi, r9
00A12780  4D 8B F8                        mov r15, r8
00A12783  89 94 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edx
00A1278A  48 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rcx
00A12792  48 8B 9C 24 F0 02 00 00         mov rbx, qword ptr [rsp + 0x2f0]
00A1279A  4C 8B 84 24 F8 02 00 00         mov r8, qword ptr [rsp + 0x2f8]
00A127A2  4C 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r8
00A127AA  4C 8B B4 24 00 03 00 00         mov r14, qword ptr [rsp + 0x300]
00A127B2  4C 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r14
00A127BA  33 FF                           xor edi, edi
00A127BC  66 89 BC 24 88 00 00 00         mov word ptr [rsp + 0x88], di
00A127C4  40 88 BC 24 83 00 00 00         mov byte ptr [rsp + 0x83], dil
00A127CC  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
00A127D4  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
00A127DC  40 88 BC 24 80 00 00 00         mov byte ptr [rsp + 0x80], dil
00A127E4  40 88 BC 24 82 00 00 00         mov byte ptr [rsp + 0x82], dil
00A127EC  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
00A127F4  8B 94 24 E8 02 00 00            mov edx, dword ptr [rsp + 0x2e8]
00A127FB  F7 C2 48 40 31 FF               test edx, 0xff314048
00A12801  0F 85 1F 05 00 00               jne 0x140a12d26
00A12807  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A12810  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00A12817  44 8A AC 24 E0 02 00 00         mov r13b, byte ptr [rsp + 0x2e0]
00A1281F  F6 80 FA 05 00 00 07            test byte ptr [rax + 0x5fa], 7
00A12826  76 09                           jbe 0x140a12831
00A12828  45 84 ED                        test r13b, r13b
00A1282B  0F 85 F5 04 00 00               jne 0x140a12d26
00A12831  8B C2                           mov eax, edx
00A12833  25 00 20 00 00                  and eax, 0x2000
00A12838  0F BA E2 0E                     bt edx, 0xe
00A1283C  73 08                           jae 0x140a12846
00A1283E  85 C0                           test eax, eax
00A12840  0F 84 E0 04 00 00               je 0x140a12d26
00A12846  8B CA                           mov ecx, edx
00A12848  81 E1 00 08 00 00               and ecx, 0x800
00A1284E  89 8C 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], ecx
00A12855  85 C0                           test eax, eax
00A12857  74 08                           je 0x140a12861
00A12859  85 C9                           test ecx, ecx
00A1285B  0F 84 C5 04 00 00               je 0x140a12d26
00A12861  85 C9                           test ecx, ecx
00A12863  74 75                           je 0x140a128da
00A12865  45 84 ED                        test r13b, r13b
00A12868  0F 85 B8 04 00 00               jne 0x140a12d26
00A1286E  4D 85 FF                        test r15, r15
00A12871  74 4C                           je 0x140a128bf
00A12873  49 39 7F 08                     cmp qword ptr [r15 + 8], rdi
00A12877  0F 85 A9 04 00 00               jne 0x140a12d26
00A1287D  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
00A12881  48 85 C0                        test rax, rax
00A12884  0F 84 9C 04 00 00               je 0x140a12d26
00A1288A  48 39 78 08                     cmp qword ptr [rax + 8], rdi
00A1288E  0F 84 92 04 00 00               je 0x140a12d26
00A12894  66 39 38                        cmp word ptr [rax], di
00A12897  0F 84 89 04 00 00               je 0x140a12d26
00A1289D  41 81 7F 18 00 02 00 00         cmp dword ptr [r15 + 0x18], 0x200
00A128A5  0F 85 7B 04 00 00               jne 0x140a12d26
00A128AB  49 39 7F 20                     cmp qword ptr [r15 + 0x20], rdi
00A128AF  0F 85 71 04 00 00               jne 0x140a12d26
00A128B5  49 39 7F 28                     cmp qword ptr [r15 + 0x28], rdi
00A128B9  0F 85 67 04 00 00               jne 0x140a12d26
00A128BF  48 85 DB                        test rbx, rbx
00A128C2  0F 85 5E 04 00 00               jne 0x140a12d26
00A128C8  4D 85 C0                        test r8, r8
00A128CB  0F 85 55 04 00 00               jne 0x140a12d26
00A128D1  48 85 F6                        test rsi, rsi
00A128D4  0F 84 4C 04 00 00               je 0x140a12d26
00A128DA  0F BA E2 11                     bt edx, 0x11
00A128DE  73 11                           jae 0x140a128f1
00A128E0  45 84 ED                        test r13b, r13b
00A128E3  0F 85 3D 04 00 00               jne 0x140a12d26
00A128E9  85 C9                           test ecx, ecx
00A128EB  0F 84 35 04 00 00               je 0x140a12d26
00A128F1  33 D2                           xor edx, edx
00A128F3  41 B8 90 01 00 00               mov r8d, 0x190
00A128F9  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00A12901  E8 3A 43 CB FF                  call 0x1406c6c40
00A12906  44 88 AC 24 64 02 00 00         mov byte ptr [rsp + 0x264], r13b
00A1290E  4D 85 FF                        test r15, r15
00A12911  74 53                           je 0x140a12966
00A12913  45 84 ED                        test r13b, r13b
00A12916  74 32                           je 0x140a1294a
00A12918  41 F6 C7 03                     test r15b, 3
00A1291C  74 06                           je 0x140a12924
00A1291E  E8 AD 76 E8 FF                  call 0x140899fd0
00A12923  CC                              int3
00A12924  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00A1292E  4C 3B F8                        cmp r15, rax
00A12931  49 0F 42 C7                     cmovb rax, r15
00A12935  90                              nop
00A12936  8A 00                           mov al, byte ptr [rax]
00A12938  41 8B 47 18                     mov eax, dword ptr [r15 + 0x18]
00A1293C  89 84 24 60 02 00 00            mov dword ptr [rsp + 0x260], eax
00A12943  EB 09                           jmp 0x140a1294e
00A12945  E9 E1 03 00 00                  jmp 0x140a12d2b
00A1294A  41 8B 47 18                     mov eax, dword ptr [r15 + 0x18]
00A1294E  45 84 ED                        test r13b, r13b
00A12951  75 07                           jne 0x140a1295a
00A12953  25 F2 1F 01 00                  and eax, 0x11ff2
00A12958  EB 05                           jmp 0x140a1295f
00A1295A  25 F2 1D 00 00                  and eax, 0x1df2
00A1295F  89 84 24 60 02 00 00            mov dword ptr [rsp + 0x260], eax
00A12966  48 85 DB                        test rbx, rbx
00A12969  74 4B                           je 0x140a129b6
00A1296B  4C 8B 05 66 42 5B 00            mov r8, qword ptr [rip + 0x5b4266]
00A12972  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
00A1297A  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00A1297F  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00A12987  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1298C  45 8A CD                        mov r9b, r13b
00A1298F  BA 08 00 00 00                  mov edx, 8
00A12994  48 8B CB                        mov rcx, rbx
00A12997  E8 14 64 E5 FF                  call 0x140868db0
00A1299C  4C 8B A4 24 B0 00 00 00         mov r12, qword ptr [rsp + 0xb0]
00A129A4  4C 89 A4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r12
00A129AC  85 C0                           test eax, eax
00A129AE  0F 88 77 03 00 00               js 0x140a12d2b
00A129B4  EB 0B                           jmp 0x140a129c1
00A129B6  4C 8B E7                        mov r12, rdi
00A129B9  48 89 BC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdi
00A129C1  48 85 F6                        test rsi, rsi
00A129C4  74 40                           je 0x140a12a06
00A129C6  4C 8B 05 CB 40 5B 00            mov r8, qword ptr [rip + 0x5b40cb]
00A129CD  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00A129D2  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00A129D7  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00A129DF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A129E4  C7 44 24 20 50 73 43 72         mov dword ptr [rsp + 0x20], 0x72437350
00A129EC  45 8A CD                        mov r9b, r13b
00A129EF  BA 80 00 00 00                  mov edx, 0x80
00A129F4  48 8B CE                        mov rcx, rsi
00A129F7  E8 54 6C E5 FF                  call 0x140869650
00A129FC  8B F0                           mov esi, eax
00A129FE  85 C0                           test eax, eax
00A12A00  0F 88 0F 03 00 00               js 0x140a12d15
00A12A06  4C 8D 8C 24 98 00 00 00         lea r9, [rsp + 0x98]
00A12A0E  45 8A C5                        mov r8b, r13b
00A12A11  49 8B D6                        mov rdx, r14
00A12A14  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00A12A1C  49 8B CE                        mov rcx, r14
00A12A1F  E8 34 03 00 00                  call 0x140a12d58
00A12A24  8B F0                           mov esi, eax
00A12A26  85 C0                           test eax, eax
00A12A28  0F 88 D5 02 00 00               js 0x140a12d03
00A12A2E  4D 85 F6                        test r14, r14
00A12A31  0F 84 90 00 00 00               je 0x140a12ac7
00A12A37  4D 85 E4                        test r12, r12
00A12A3A  74 6D                           je 0x140a12aa9
00A12A3C  40 88 BC 24 81 00 00 00         mov byte ptr [rsp + 0x81], dil
00A12A44  48 8D 84 24 81 00 00 00         lea rax, [rsp + 0x81]
00A12A4C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A12A51  48 8D 84 24 82 00 00 00         lea rax, [rsp + 0x82]
00A12A59  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A12A5E  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00A12A66  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A12A6B  44 8A CF                        mov r9b, dil
00A12A6E  45 33 C0                        xor r8d, r8d
00A12A71  33 D2                           xor edx, edx
00A12A73  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00A12A7B  E8 C4 04 00 00                  call 0x140a12f44
00A12A80  8B F0                           mov esi, eax
00A12A82  85 C0                           test eax, eax
00A12A84  0F 88 6C 02 00 00               js 0x140a12cf6
00A12A8A  80 BC 24 80 00 00 00 01         cmp byte ptr [rsp + 0x80], 1
00A12A92  77 0B                           ja 0x140a12a9f
00A12A94  8A 9C 24 81 00 00 00            mov bl, byte ptr [rsp + 0x81]
00A12A9B  84 DB                           test bl, bl
00A12A9D  74 48                           je 0x140a12ae7
00A12A9F  BE BB 00 00 C0                  mov esi, 0xc00000bb
00A12AA4  E9 4D 02 00 00                  jmp 0x140a12cf6
00A12AA9  41 8A 9E FA 05 00 00            mov bl, byte ptr [r14 + 0x5fa]
00A12AB0  41 8A 86 F9 05 00 00            mov al, byte ptr [r14 + 0x5f9]
00A12AB7  41 8A 8E F8 05 00 00            mov cl, byte ptr [r14 + 0x5f8]
00A12ABE  88 8C 24 80 00 00 00            mov byte ptr [rsp + 0x80], cl
00A12AC5  EB 12                           jmp 0x140a12ad9
00A12AC7  B3 72                           mov bl, 0x72
00A12AC9  C6 84 24 80 00 00 00 1E         mov byte ptr [rsp + 0x80], 0x1e
00A12AD1  8A 05 20 84 13 00               mov al, byte ptr [rip + 0x138420]
00A12AD7  0C 10                           or al, 0x10
00A12AD9  88 84 24 82 00 00 00            mov byte ptr [rsp + 0x82], al
00A12AE0  88 9C 24 81 00 00 00            mov byte ptr [rsp + 0x81], bl
00A12AE7  4D 85 E4                        test r12, r12
00A12AEA  74 25                           je 0x140a12b11
00A12AEC  4C 8D 84 24 83 00 00 00         lea r8, [rsp + 0x83]
00A12AF4  8A D3                           mov dl, bl
00A12AF6  49 8B CC                        mov rcx, r12
00A12AF9  E8 F6 B1 05 00                  call 0x140a6dcf4
00A12AFE  8B F0                           mov esi, eax
00A12B00  85 C0                           test eax, eax
00A12B02  0F 88 EE 01 00 00               js 0x140a12cf6
00A12B08  3A 9C 24 83 00 00 00            cmp bl, byte ptr [rsp + 0x83]
00A12B0F  75 8E                           jne 0x140a12a9f
00A12B11  39 BC 24 8C 00 00 00            cmp dword ptr [rsp + 0x8c], edi
00A12B18  74 6E                           je 0x140a12b88
00A12B1A  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A12B22  48 F7 D9                        neg rcx
00A12B25  48 1B C0                        sbb rax, rax
00A12B28  48 23 84 24 98 00 00 00         and rax, qword ptr [rsp + 0x98]
00A12B30  4D 85 FF                        test r15, r15
00A12B33  74 06                           je 0x140a12b3b
00A12B35  49 8B 57 10                     mov rdx, qword ptr [r15 + 0x10]
00A12B39  EB 03                           jmp 0x140a12b3e
00A12B3B  48 8B D7                        mov rdx, rdi
00A12B3E  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00A12B46  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00A12B4B  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00A12B50  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00A12B55  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00A12B5A  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00A12B5F  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00A12B63  8B 8C 24 E8 02 00 00            mov ecx, dword ptr [rsp + 0x2e8]
00A12B6A  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00A12B6E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A12B73  44 8A CB                        mov r9b, bl
00A12B76  45 33 C0                        xor r8d, r8d
00A12B79  49 8B CE                        mov rcx, r14
00A12B7C  E8 93 41 D7 FF                  call 0x140786d14
00A12B81  8B F0                           mov esi, eax
00A12B83  E9 6E 01 00 00                  jmp 0x140a12cf6
00A12B88  8B C7                           mov eax, edi
00A12B8A  48 39 84 24 B8 00 00 00         cmp qword ptr [rsp + 0xb8], rax
00A12B92  0F 95 C0                        setne al
00A12B95  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
00A12B9D  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00A12BA2  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00A12BAA  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00A12BAF  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00A12BB4  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A12BB8  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00A12BBD  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00A12BC1  8B 8C 24 E8 02 00 00            mov ecx, dword ptr [rsp + 0x2e8]
00A12BC8  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00A12BCC  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00A12BD4  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A12BD9  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00A12BDE  8A 84 24 82 00 00 00            mov al, byte ptr [rsp + 0x82]
00A12BE5  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A12BE9  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00A12BF0  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00A12BF4  44 8A CB                        mov r9b, bl
00A12BF7  4D 8B C7                        mov r8, r15
00A12BFA  41 8A D5                        mov dl, r13b
00A12BFD  49 8B CE                        mov rcx, r14
00A12C00  E8 37 0F 00 00                  call 0x140a13b3c
00A12C05  8B F0                           mov esi, eax
00A12C07  85 C0                           test eax, eax
00A12C09  0F 88 E7 00 00 00               js 0x140a12cf6
00A12C0F  8B D8                           mov ebx, eax
00A12C11  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
00A12C18  40 38 BC 24 88 00 00 00         cmp byte ptr [rsp + 0x88], dil
00A12C20  B8 01 00 00 00                  mov eax, 1
00A12C25  8D 48 02                        lea ecx, [rax + 2]
00A12C28  0F 45 C1                        cmovne eax, ecx
00A12C2B  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00A12C33  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A12C38  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00A12C3D  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A12C41  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00A12C49  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A12C4E  44 8B 8C 24 E8 02 00 00         mov r9d, dword ptr [rsp + 0x2e8]
00A12C56  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00A12C5E  49 8B D6                        mov rdx, r14
00A12C61  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00A12C69  E8 5E 46 F3 FF                  call 0x1409472cc
00A12C6E  8B F0                           mov esi, eax
00A12C70  85 C0                           test eax, eax
00A12C72  78 5D                           js 0x140a12cd1
00A12C74  4C 8B 05 1D 3E 5B 00            mov r8, qword ptr [rip + 0x5b3e1d]
00A12C7B  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00A12C83  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00A12C8B  E8 8C B8 00 00                  call 0x140a1e51c
00A12C90  8B F0                           mov esi, eax
00A12C92  85 C0                           test eax, eax
00A12C94  78 2E                           js 0x140a12cc4
00A12C96  48 8B 84 24 68 02 00 00         mov rax, qword ptr [rsp + 0x268]
00A12C9E  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00A12CA6  48 89 01                        mov qword ptr [rcx], rax
00A12CA9  EB 17                           jmp 0x140a12cc2
00A12CAB  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00A12CB3  8B 9C 24 8C 00 00 00            mov ebx, dword ptr [rsp + 0x8c]
00A12CBA  4C 8B A4 24 C8 00 00 00         mov r12, qword ptr [rsp + 0xc8]
00A12CC2  8B F3                           mov esi, ebx
00A12CC4  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00A12CCC  E8 9F 32 EB FF                  call 0x1408c5f70
00A12CD1  85 F6                           test esi, esi
00A12CD3  79 0F                           jns 0x140a12ce4
00A12CD5  33 D2                           xor edx, edx
00A12CD7  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00A12CDF  E8 6C 40 EF FF                  call 0x140906d50
00A12CE4  BA 50 73 43 72                  mov edx, 0x72437350
00A12CE9  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00A12CF1  E8 EA 4B 8E FF                  call 0x1402f78e0
00A12CF6  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00A12CFE  E8 4D 66 8E FF                  call 0x1402f9350
00A12D03  4D 85 F6                        test r14, r14
00A12D06  74 0D                           je 0x140a12d15
00A12D08  BA 50 73 43 72                  mov edx, 0x72437350
00A12D0D  49 8B CE                        mov rcx, r14
00A12D10  E8 CB 4B 8E FF                  call 0x1402f78e0
00A12D15  4D 85 E4                        test r12, r12
00A12D18  74 08                           je 0x140a12d22
00A12D1A  49 8B CC                        mov rcx, r12
00A12D1D  E8 2E 66 8E FF                  call 0x1402f9350
00A12D22  8B C6                           mov eax, esi
00A12D24  EB 05                           jmp 0x140a12d2b
00A12D26  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A12D2B  48 8B 8C 24 70 02 00 00         mov rcx, qword ptr [rsp + 0x270]
00A12D33  48 33 CC                        xor rcx, rsp
00A12D36  E8 05 99 C9 FF                  call 0x1406ac640
00A12D3B  48 81 C4 80 02 00 00            add rsp, 0x280
00A12D42  41 5F                           pop r15
00A12D44  41 5E                           pop r14
00A12D46  41 5D                           pop r13
00A12D48  41 5C                           pop r12
00A12D4A  5F                              pop rdi
00A12D4B  5E                              pop rsi
00A12D4C  5B                              pop rbx
00A12D4D  C3                              ret
00A12D4E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspCreateProcess(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m22C;
    unsigned __int16 v_stack_m230;
    unsigned __int8 v_stack_m235;
    unsigned __int8 v_stack_m236;
    unsigned __int8 v_stack_m237;
    unsigned __int8 v_stack_m238;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int8 v_stack_m54;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (640);
    result = (*(unsigned __int64 *)(v_rip + 4161486)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m218 = a2;
    v_stack_m1F8 = a1;
    v_stack_m1E8 = a8;
    v_stack_m200 = a9;
    v_rdi = 0;
    v_stack_m230 = 0;
    v_stack_m235 = 0;
    v_stack_m210 = 0;
    v_stack_m228 = 0;
    v_stack_m238 = 0;
    v_stack_m236 = 0;
    v_stack_m220 = 0;
    if ((((unsigned int)((unsigned int)(a6))) & (0xFF314048ULL)) != 0) goto loc_00A12D26;
    if (condition_is_below_or_equal) goto loc_00A12831;
    if (a5 != 0) goto loc_00A12D26;
loc_00A12831:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (0x2000ULL));
    if (condition_is_above_or_equal) goto loc_00A12846;
    if ((unsigned int)(result) == 0) goto loc_00A12D26;
loc_00A12846:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (0x800ULL));
    v_stack_m22C = (unsigned int)(a1);
    if ((unsigned int)(result) == 0) goto loc_00A12861;
    if ((unsigned int)(a1) == 0) goto loc_00A12D26;
loc_00A12861:
    if ((unsigned int)(a1) == 0) goto loc_00A128DA;
    if (a5 != 0) goto loc_00A12D26;
    if (a3 == 0) goto loc_00A128BF;
    if ((*(unsigned __int64 *)(a3 + 8)) != 0) goto loc_00A12D26;
    if (*(unsigned __int64 *)(a3 + 16) == 0) goto loc_00A12D26;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 16) + 8)) == 0) goto loc_00A12D26;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 16))) == 0) goto loc_00A12D26;
    if ((*(unsigned int *)(a3 + 24)) != 512) goto loc_00A12D26;
    if ((*(unsigned __int64 *)(a3 + 32)) != 0) goto loc_00A12D26;
    if ((*(unsigned __int64 *)(a3 + 40)) != 0) goto loc_00A12D26;
loc_00A128BF:
    if (a7 != 0) goto loc_00A12D26;
    if (a8 != 0) goto loc_00A12D26;
    if (a4 == 0) goto loc_00A12D26;
loc_00A128DA:
    if (condition_is_above_or_equal) goto loc_00A128F1;
    if (a5 != 0) goto loc_00A12D26;
    if ((unsigned int)(a1) == 0) goto loc_00A12D26;
loc_00A128F1:
    a2 = 0;
    result = memset(v_stack_m1D8, a2, 400, a4);
    v_stack_m54 = a5;
    if (a3 == 0) goto loc_00A12966;
    if (a5 == 0) goto loc_00A1294A;
    if ((((unsigned __int8)(a3)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_m1D8, a2, 400, a4);
    }
    if (a3 < result) { result = a3; }
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 24)));
    goto loc_00A1294E;
loc_00A1294A:
loc_00A1294E:
    if (a5 != 0) goto loc_00A1295A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 24))) & (0x11FF2ULL));
    goto loc_00A1295F;
loc_00A1295A:
    result = (unsigned int)((result) & (0x1DF2ULL));
loc_00A1295F:
    v_stack_m58 = (unsigned int)(result);
loc_00A12966:
    if (a7 == 0) goto loc_00A129B6;
    v_stack_m208 = 0;
    v_stack_m290 = 0;
    v_stack_m298 = v_stack_m208;
    result = ObReferenceObjectByHandle(a7, 8, *(unsigned __int64 *)(v_rip + 5980774), a5);
    v_stack_m1F0 = v_stack_m208;
    if (sign_flag) goto loc_00A12D2B;
    goto loc_00A129C1;
loc_00A129B6:
    v_stack_m1F0 = 0;
loc_00A129C1:
    if (a4 == 0) goto loc_00A12A06;
    v_stack_m280 = 0;
    v_stack_m288 = 0;
    v_stack_m290 = v_stack_m210;
    v_stack_m298 = 0x72437350ULL;
    result = ObpReferenceObjectByHandleWithTag(a4, 128, *(unsigned __int64 *)(v_rip + 5980363), a5);
    if (sign_flag) goto loc_00A12D15;
loc_00A12A06:
    result = PspReferenceTokenForNewProcess(v_stack_m210, a9, a5, v_stack_m220);
    if (sign_flag) goto loc_00A12D03;
    if (v_stack_m210 == 0) goto loc_00A12AC7;
    if (0 == 0) goto loc_00A12AA9;
    v_stack_m237 = 0;
    v_stack_m288 = v_stack_m237;
    v_stack_m290 = v_stack_m236;
    v_stack_m298 = v_stack_m238;
    a3 = 0;
    a2 = 0;
    result = SeQuerySigningPolicy(v_stack_m220, a2, a3, 0);
    if (sign_flag) goto loc_00A12CF6;
    if (v_stack_m238 > 1) goto loc_00A12A9F;
    if ((unsigned __int8)(v_stack_m237) == 0) goto loc_00A12AE7;
loc_00A12A9F:
    goto loc_00A12CF6;
loc_00A12AA9:
    v_stack_m238 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m210 + 1528));
    goto loc_00A12AD9;
loc_00A12AC7:
    v_stack_m238 = 30;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 1279008)) | (16));
loc_00A12AD9:
    v_stack_m236 = (unsigned __int8)(result);
    v_stack_m237 = 114;
loc_00A12AE7:
    if (0 == 0) goto loc_00A12B11;
    result = PspGetProcessProtectionRequirementsFromImage(0, 114, v_stack_m235, 0);
    if (sign_flag) goto loc_00A12CF6;
    if (114 != v_stack_m235) goto loc_00A12A9F;
loc_00A12B11:
    if (v_stack_m22C == 0) goto loc_00A12B88;
    a1 = -(v_stack_m200);
    result = (result) & (v_stack_m220);
    if (0 == 0) goto loc_00A12B3B;
    goto loc_00A12B3E;
loc_00A12B3B:
loc_00A12B3E:
    v_stack_m260 = v_stack_m1F8;
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    v_stack_m280 = 0;
    v_stack_m288 = 0;
    v_stack_m290 = (unsigned int)((unsigned int)(a6));
    v_stack_m298 = result;
    a3 = 0;
    result = PsCreateMinimalProcess(v_stack_m210, 0, a3, 114);
    goto loc_00A12CF6;
loc_00A12B88:
    result = (v_stack_m200 != 0) ? 1 : 0;
    v_stack_m248 = v_stack_m228;
    v_stack_m250 = v_stack_m230;
    v_stack_m258 = 0;
    v_stack_m260 = (unsigned int)(result);
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = (unsigned int)((unsigned int)(a6));
    v_stack_m280 = v_stack_m220;
    v_stack_m288 = 0;
    v_stack_m290 = (unsigned __int8)(v_stack_m236);
    v_stack_m298 = (unsigned __int8)(v_stack_m238);
    result = PspAllocateProcess(v_stack_m210, a5, 0, 114);
    if (sign_flag) goto loc_00A12CF6;
    v_stack_m22C = (unsigned int)(result);
    result = 1;
    if (v_stack_m230 != 0) { result = (unsigned int)(1 + 2); }
    v_stack_m280 = v_stack_m1D8;
    v_stack_m288 = 0;
    v_stack_m290 = (unsigned int)(result);
    v_stack_m298 = v_stack_m1E8;
    result = PspInsertProcess(v_stack_m228, v_stack_m210, (unsigned int)(v_stack_m218), (unsigned int)(a6));
    if (sign_flag) goto loc_00A12CD1;
    result = PspCreateObjectHandle(v_stack_m228, v_stack_m1D8, *(unsigned __int64 *)(v_rip + 5979677), (unsigned int)(a6));
    if (sign_flag) goto loc_00A12CC4;
    *(unsigned __int64 *)(v_stack_m1F8) = v_stack_m50;
    goto loc_00A12CC2;
loc_00A12CC2:
loc_00A12CC4:
    result = SeDeleteAccessState(v_stack_m1D8, v_stack_m1D8, *(unsigned __int64 *)(v_rip + 5979677), (unsigned int)(a6));
loc_00A12CD1:
    if (sign_flag) {
        a2 = 0;
        a1 = v_stack_m228;
        result = PspRundownSingleProcess(a1, a2, *(unsigned __int64 *)(v_rip + 5979677), (unsigned int)(a6));
    }
    result = ObfDereferenceObjectWithTag(v_stack_m228, (unsigned int)(0x72437350ULL), *(unsigned __int64 *)(v_rip + 5979677), (unsigned int)(a6));
loc_00A12CF6:
    result = ObfDereferenceObject(v_stack_m220, (unsigned int)(0x72437350ULL), *(unsigned __int64 *)(v_rip + 5979677), (unsigned int)(a6));
loc_00A12D03:
    if (v_stack_m210 != 0) {
        a2 = 0x72437350ULL;
        a1 = v_stack_m210;
        result = ObfDereferenceObjectWithTag(a1, a2, *(unsigned __int64 *)(v_rip + 5979677), (unsigned int)(a6));
    }
    if (0 != 0) {
        a1 = 0;
        result = ObfDereferenceObject(a1, a2, *(unsigned __int64 *)(v_rip + 5979677), (unsigned int)(a6));
    }
    goto loc_00A12D2B;
loc_00A12D26:
loc_00A12D2B:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_rip + 5979677), (unsigned int)(a6));
    v_rsp = (v_rsp) + (640);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspCreateProcess(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint32_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m22C;
    uint16_t v_stack_m230;
    uint8_t v_stack_m235;
    uint8_t v_stack_m236;
    uint8_t v_stack_m237;
    uint8_t v_stack_m238;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint8_t v_stack_m54;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (640);
    result = (*(uint64_t *)(v_rip + 0x3F7FCE)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m218 = Arg2;
    v_stack_m1F8 = Arg1;
    v_stack_m1E8 = Arg8;
    v_stack_m200 = Arg9;
    local_rdi = 0;
    v_stack_m230 = 0;
    v_stack_m235 = 0;
    v_stack_m210 = 0;
    v_stack_m228 = 0;
    v_stack_m238 = 0;
    v_stack_m236 = 0;
    v_stack_m220 = 0;
    if ((((uint32_t)((uint32_t)(Arg6))) & (0xFF314048ULL)) != 0) goto loc_00A12D26;
    if (condition_is_below_or_equal) goto loc_00A12831;
    if (Arg5 != 0) goto loc_00A12D26;
loc_00A12831:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (0x2000ULL));
    if (condition_is_above_or_equal) goto loc_00A12846;
    if ((uint32_t)(result) == 0) goto loc_00A12D26;
loc_00A12846:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (0x800ULL));
    v_stack_m22C = (uint32_t)(Arg1);
    if ((uint32_t)(result) == 0) goto loc_00A12861;
    if ((uint32_t)(Arg1) == 0) goto loc_00A12D26;
loc_00A12861:
    if ((uint32_t)(Arg1) == 0) goto loc_00A128DA;
    if (Arg5 != 0) goto loc_00A12D26;
    if (Arg3 == 0) goto loc_00A128BF;
    if ((*(uint64_t *)(Arg3 + 0x8)) != 0) goto loc_00A12D26;
    if (*(uint64_t *)(Arg3 + 0x10) == 0) goto loc_00A12D26;
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0x10) + 0x8)) == 0) goto loc_00A12D26;
    if ((*(uint16_t *)(*(uint64_t *)(Arg3 + 0x10))) == 0) goto loc_00A12D26;
    if ((*(uint32_t *)(Arg3 + 0x18)) != 512) goto loc_00A12D26;
    if ((*(uint64_t *)(Arg3 + 0x20)) != 0) goto loc_00A12D26;
    if ((*(uint64_t *)(Arg3 + 0x28)) != 0) goto loc_00A12D26;
loc_00A128BF:
    if (Arg7 != 0) goto loc_00A12D26;
    if (Arg8 != 0) goto loc_00A12D26;
    if (Arg4 == 0) goto loc_00A12D26;
loc_00A128DA:
    if (condition_is_above_or_equal) goto loc_00A128F1;
    if (Arg5 != 0) goto loc_00A12D26;
    if ((uint32_t)(Arg1) == 0) goto loc_00A12D26;
loc_00A128F1:
    Arg2 = 0;
    result = memset(v_stack_m1D8, Arg2, 400, Arg4);
    v_stack_m54 = Arg5;
    if (Arg3 == 0) goto loc_00A12966;
    if (Arg5 == 0) goto loc_00A1294A;
    if ((((uint8_t)(Arg3)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_m1D8, Arg2, 400, Arg4);
    }
    if (Arg3 < result) { result = Arg3; }
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x18)));
    goto loc_00A1294E;
loc_00A1294A:
loc_00A1294E:
    if (Arg5 != 0) goto loc_00A1295A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x18))) & (0x11FF2ULL));
    goto loc_00A1295F;
loc_00A1295A:
    result = (uint32_t)((result) & (0x1DF2ULL));
loc_00A1295F:
    v_stack_m58 = (uint32_t)(result);
loc_00A12966:
    if (Arg7 == 0) goto loc_00A129B6;
    v_stack_m208 = 0;
    v_stack_m290 = 0;
    v_stack_m298 = v_stack_m208;
    result = ObReferenceObjectByHandle(Arg7, 8, *(uint64_t *)(v_rip + 0x5B4266), Arg5);
    v_stack_m1F0 = v_stack_m208;
    if (sign_flag) goto loc_00A12D2B;
    goto loc_00A129C1;
loc_00A129B6:
    v_stack_m1F0 = 0;
loc_00A129C1:
    if (Arg4 == 0) goto loc_00A12A06;
    v_stack_m280 = 0;
    v_stack_m288 = 0;
    v_stack_m290 = v_stack_m210;
    v_stack_m298 = 0x72437350ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg4, 128, *(uint64_t *)(v_rip + 0x5B40CB), Arg5);
    if (sign_flag) goto loc_00A12D15;
loc_00A12A06:
    result = PspReferenceTokenForNewProcess(v_stack_m210, Arg9, Arg5, v_stack_m220);
    if (sign_flag) goto loc_00A12D03;
    if (v_stack_m210 == 0) goto loc_00A12AC7;
    if (0 == 0) goto loc_00A12AA9;
    v_stack_m237 = 0;
    v_stack_m288 = v_stack_m237;
    v_stack_m290 = v_stack_m236;
    v_stack_m298 = v_stack_m238;
    Arg3 = 0;
    Arg2 = 0;
    result = SeQuerySigningPolicy(v_stack_m220, Arg2, Arg3, 0);
    if (sign_flag) goto loc_00A12CF6;
    if (v_stack_m238 > 1) goto loc_00A12A9F;
    if ((uint8_t)(v_stack_m237) == 0) goto loc_00A12AE7;
loc_00A12A9F:
    goto loc_00A12CF6;
loc_00A12AA9:
    v_stack_m238 = (uint8_t)(*(uint8_t *)(v_stack_m210 + 0x5F8));
    goto loc_00A12AD9;
loc_00A12AC7:
    v_stack_m238 = 30;
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x138420)) | (16));
loc_00A12AD9:
    v_stack_m236 = (uint8_t)(result);
    v_stack_m237 = 114;
loc_00A12AE7:
    if (0 == 0) goto loc_00A12B11;
    result = PspGetProcessProtectionRequirementsFromImage(0, 114, v_stack_m235, 0);
    if (sign_flag) goto loc_00A12CF6;
    if (114 != v_stack_m235) goto loc_00A12A9F;
loc_00A12B11:
    if (v_stack_m22C == 0) goto loc_00A12B88;
    Arg1 = -(v_stack_m200);
    result = (result) & (v_stack_m220);
    if (0 == 0) goto loc_00A12B3B;
    goto loc_00A12B3E;
loc_00A12B3B:
loc_00A12B3E:
    v_stack_m260 = v_stack_m1F8;
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    v_stack_m280 = 0;
    v_stack_m288 = 0;
    v_stack_m290 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m298 = result;
    Arg3 = 0;
    result = PsCreateMinimalProcess(v_stack_m210, 0, Arg3, 114);
    goto loc_00A12CF6;
loc_00A12B88:
    result = (v_stack_m200 != 0) ? 1 : 0;
    v_stack_m248 = v_stack_m228;
    v_stack_m250 = v_stack_m230;
    v_stack_m258 = 0;
    v_stack_m260 = (uint32_t)(result);
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m280 = v_stack_m220;
    v_stack_m288 = 0;
    v_stack_m290 = (uint8_t)(v_stack_m236);
    v_stack_m298 = (uint8_t)(v_stack_m238);
    result = PspAllocateProcess(v_stack_m210, Arg5, 0, 114);
    if (sign_flag) goto loc_00A12CF6;
    v_stack_m22C = (uint32_t)(result);
    result = 1;
    if (v_stack_m230 != 0) { result = (uint32_t)(1 + 2); }
    v_stack_m280 = v_stack_m1D8;
    v_stack_m288 = 0;
    v_stack_m290 = (uint32_t)(result);
    v_stack_m298 = v_stack_m1E8;
    result = PspInsertProcess(v_stack_m228, v_stack_m210, (uint32_t)(v_stack_m218), (uint32_t)(Arg6));
    if (sign_flag) goto loc_00A12CD1;
    result = PspCreateObjectHandle(v_stack_m228, v_stack_m1D8, *(uint64_t *)(v_rip + 0x5B3E1D), (uint32_t)(Arg6));
    if (sign_flag) goto loc_00A12CC4;
    *(uint64_t *)(v_stack_m1F8) = v_stack_m50;
    goto loc_00A12CC2;
loc_00A12CC2:
loc_00A12CC4:
    result = SeDeleteAccessState(v_stack_m1D8, v_stack_m1D8, *(uint64_t *)(v_rip + 0x5B3E1D), (uint32_t)(Arg6));
loc_00A12CD1:
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = v_stack_m228;
        result = PspRundownSingleProcess(Arg1, Arg2, *(uint64_t *)(v_rip + 0x5B3E1D), (uint32_t)(Arg6));
    }
    result = ObfDereferenceObjectWithTag(v_stack_m228, (uint32_t)(0x72437350ULL), *(uint64_t *)(v_rip + 0x5B3E1D), (uint32_t)(Arg6));
loc_00A12CF6:
    result = ObfDereferenceObject(v_stack_m220, (uint32_t)(0x72437350ULL), *(uint64_t *)(v_rip + 0x5B3E1D), (uint32_t)(Arg6));
loc_00A12D03:
    if (v_stack_m210 != 0) {
        Arg2 = 0x72437350ULL;
        Arg1 = v_stack_m210;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, *(uint64_t *)(v_rip + 0x5B3E1D), (uint32_t)(Arg6));
    }
    if (0 != 0) {
        Arg1 = 0;
        result = ObfDereferenceObject(Arg1, Arg2, *(uint64_t *)(v_rip + 0x5B3E1D), (uint32_t)(Arg6));
    }
    goto loc_00A12D2B;
loc_00A12D26:
loc_00A12D2B:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(v_rip + 0x5B3E1D), (uint32_t)(Arg6));
    local_rsp = (local_rsp) + (640);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A12758&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
