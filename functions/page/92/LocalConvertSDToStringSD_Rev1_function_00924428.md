# LocalConvertSDToStringSD_Rev1

- RVA: `0x00924428`–`0x00924A62` (길이 `1,594` bytes)
- VA: `0x0000000140924428`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D3D8`
- 디코드: `423`개 명령, `1,594/1,594` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00924503` → [RtlGetDaclSecurityDescriptor](../../text/45/RtlGetDaclSecurityDescriptor_function_00459570.md) (function, `0x00459570`)
- `0x00924517` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00924521` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x0092456D` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x009245A7` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x009245E3` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x009245EC` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x009245F5` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x009245FE` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00924607` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00924610` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00924619` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00924620` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00924656` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x00924693` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x009246C9` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x009246E2` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x00924725` → [SddlpAlloc](SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00924770` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x009247BC` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x0092483F` → [LocalGetStringForSid](../A0/LocalGetStringForSid_function_00A00328.md) (function, `0x00A00328`)
- `0x00924860` → [LocalGetStringForControl](../A5/LocalGetStringForControl_function_00A55674.md) (function, `0x00A55674`)
- `0x0092487A` → [LocalGetStringForControl](../A5/LocalGetStringForControl_function_00A55674.md) (function, `0x00A55674`)
- `0x009248BA` → [LocalConvertAclToString](../A0/LocalConvertAclToString_function_00A00408.md) (function, `0x00A00408`)
- `0x009248FE` → [LocalConvertAclToString](../A0/LocalConvertAclToString_function_00A00408.md) (function, `0x00A00408`)
- `0x0092498E` → [LocalGetStringForSid](../A0/LocalGetStringForSid_function_00A00328.md) (function, `0x00A00328`)
- `0x009249AF` → [SddlFilterSacl](../A7/SddlFilterSacl_function_00A710E0.md) (function, `0x00A710E0`)
- `0x009249B7` → [SddlpAlloc](SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x009249D2` → [SddlFilterSacl](../A7/SddlFilterSacl_function_00A710E0.md) (function, `0x00A710E0`)
- `0x00924A30` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)

### Direct callers
- [AdtpBuildAccessReasonAuditStringInternal](../../text/40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) at `0x0040F745`
- [SeConvertSecurityDescriptorToStringSecurityDescriptor](../../text/4A/SeConvertSecurityDescriptorToStringSecurityDescriptor_function_004A18B0.md) at `0x004A18FA`

### Static image references
- `0x0092453B` → RVA `0x00011D14` (`.rdata`; read)
- `0x0092455E` → RVA `0x00011D18` (`.rdata`; read)
- `0x00924647` → RVA `0x00011D30` (`.rdata`; read)
- `0x00924662` → RVA `0x00011D2C` (`.rdata`; read)
- `0x00924754` → RVA `0x00011D10` (`.rdata`; read)
- `0x0092479A` → RVA `0x00011D0C` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00924503` → [RtlGetDaclSecurityDescriptor](../../text/45/RtlGetDaclSecurityDescriptor_function_00459570.md) (`PAGE` → `.text`)
  - `0x0092456D` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x009245A7` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00924656` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x00924693` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x009246C9` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x009246E2` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x00924770` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x009247BC` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00924428  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
0092442D  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00924432  55                              push rbp
00924433  53                              push rbx
00924434  56                              push rsi
00924435  57                              push rdi
00924436  41 54                           push r12
00924438  41 55                           push r13
0092443A  41 56                           push r14
0092443C  41 57                           push r15
0092443E  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00924443  48 81 EC 98 00 00 00            sub rsp, 0x98
0092444A  33 D2                           xor edx, edx
0092444C  49 8B D9                        mov rbx, r9
0092444F  89 55 67                        mov dword ptr [rbp + 0x67], edx
00924452  44 8B EA                        mov r13d, edx
00924455  48 89 55 F7                     mov qword ptr [rbp - 9], rdx
00924459  8B FA                           mov edi, edx
0092445B  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
0092445F  8B F2                           mov esi, edx
00924461  88 55 57                        mov byte ptr [rbp + 0x57], dl
00924464  44 8B FA                        mov r15d, edx
00924467  88 55 5F                        mov byte ptr [rbp + 0x5f], dl
0092446A  44 8B F2                        mov r14d, edx
0092446D  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
00924471  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
00924475  48 89 55 E7                     mov qword ptr [rbp - 0x19], rdx
00924479  48 89 55 EF                     mov qword ptr [rbp - 0x11], rdx
0092447D  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
00924481  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
00924485  4D 85 C9                        test r9, r9
00924488  0F 84 CA 05 00 00               je 0x140924a58
0092448E  48 39 55 77                     cmp qword ptr [rbp + 0x77], rdx
00924492  0F 84 C0 05 00 00               je 0x140924a58
00924498  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
0092449C  41 F6 C4 01                     test r12b, 1
009244A0  74 21                           je 0x1409244c3
009244A2  41 80 39 01                     cmp byte ptr [r9], 1
009244A6  0F 85 91 01 00 00               jne 0x14092463d
009244AC  66 41 39 51 02                  cmp word ptr [r9 + 2], dx
009244B1  0F 8D 4B 05 00 00               jge 0x140924a02
009244B7  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
009244BB  85 C0                           test eax, eax
009244BD  74 04                           je 0x1409244c3
009244BF  49 8D 34 01                     lea rsi, [r9 + rax]
009244C3  41 F6 C4 02                     test r12b, 2
009244C7  74 21                           je 0x1409244ea
009244C9  41 80 39 01                     cmp byte ptr [r9], 1
009244CD  0F 85 6A 01 00 00               jne 0x14092463d
009244D3  66 41 39 51 02                  cmp word ptr [r9 + 2], dx
009244D8  0F 8D 2D 05 00 00               jge 0x140924a0b
009244DE  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
009244E2  85 C0                           test eax, eax
009244E4  74 04                           je 0x1409244ea
009244E6  4D 8D 3C 01                     lea r15, [r9 + rax]
009244EA  41 F6 C4 04                     test r12b, 4
009244EE  0F 84 43 04 00 00               je 0x140924937
009244F4  4C 8D 4D 4F                     lea r9, [rbp + 0x4f]
009244F8  48 8B CB                        mov rcx, rbx
009244FB  4C 8D 45 F7                     lea r8, [rbp - 9]
009244FF  48 8D 55 5F                     lea rdx, [rbp + 0x5f]
00924503  E8 68 50 B3 FF                  call 0x140459570
00924508  33 D2                           xor edx, edx
0092450A  85 C0                           test eax, eax
0092450C  0F 89 25 04 00 00               jns 0x140924937
00924512  4C 8B E2                        mov r12, rdx
00924515  8B C8                           mov ecx, eax
00924517  E8 24 27 00 00                  call 0x140926c40
0092451C  49 8B CC                        mov rcx, r12
0092451F  8B D8                           mov ebx, eax
00924521  E8 DE DE FA FF                  call 0x1408d2404
00924526  8B C3                           mov eax, ebx
00924528  E9 FB 00 00 00                  jmp 0x140924628
0092452D  03 F1                           add esi, ecx
0092452F  44 38 4D 5F                     cmp byte ptr [rbp + 0x5f], r9b
00924533  0F 84 16 05 00 00               je 0x140924a4f
00924539  8B DE                           mov ebx, esi
0092453B  4C 8D 0D D2 D7 6E FF            lea r9, [rip - 0x91282e]
00924542  4C 2B F3                        sub r14, rbx
00924545  49 8B D6                        mov rdx, r14
00924548  48 8D 0C 58                     lea rcx, [rax + rbx*2]
0092454C  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
00924550  48 85 C0                        test rax, rax
00924553  0F 84 EE 00 00 00               je 0x140924647
00924559  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092455E  4C 8D 05 B3 D7 6E FF            lea r8, [rip - 0x91284d]
00924565  C7 44 24 20 3A 00 00 00         mov dword ptr [rsp + 0x20], 0x3a
0092456D  E8 AE 05 BE FF                  call 0x140504b20
00924572  4C 8B 75 77                     mov r14, qword ptr [rbp + 0x77]
00924576  49 8B CF                        mov rcx, r15
00924579  45 33 C9                        xor r9d, r9d
0092457C  49 8B 06                        mov rax, qword ptr [r14]
0092457F  48 8D 14 58                     lea rdx, [rax + rbx*2]
00924583  48 FF C1                        inc rcx
00924586  66 44 39 0C 4A                  cmp word ptr [rdx + rcx*2], r9w
0092458B  75 F6                           jne 0x140924583
0092458D  4C 8B 45 EF                     mov r8, qword ptr [rbp - 0x11]
00924591  03 F1                           add esi, ecx
00924593  4D 85 C0                        test r8, r8
00924596  74 2D                           je 0x1409245c5
00924598  49 8B D4                        mov rdx, r12
0092459B  8B DE                           mov ebx, esi
0092459D  48 D1 EA                        shr rdx, 1
009245A0  48 8D 0C 70                     lea rcx, [rax + rsi*2]
009245A4  48 2B D3                        sub rdx, rbx
009245A7  E8 04 1F BE FF                  call 0x1405064b0
009245AC  49 8B 06                        mov rax, qword ptr [r14]
009245AF  49 8B CF                        mov rcx, r15
009245B2  45 33 C9                        xor r9d, r9d
009245B5  48 8D 14 70                     lea rdx, [rax + rsi*2]
009245B9  48 FF C1                        inc rcx
009245BC  66 44 39 0C 4A                  cmp word ptr [rdx + rcx*2], r9w
009245C1  75 F6                           jne 0x1409245b9
009245C3  03 F1                           add esi, ecx
009245C5  80 7D 57 00                     cmp byte ptr [rbp + 0x57], 0
009245C9  0F 85 91 00 00 00               jne 0x140924660
009245CF  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
009245D3  48 85 C0                        test rax, rax
009245D6  74 04                           je 0x1409245dc
009245D8  D1 EF                           shr edi, 1
009245DA  89 38                           mov dword ptr [rax], edi
009245DC  48 8B 75 BF                     mov rsi, qword ptr [rbp - 0x41]
009245E0  48 8B CE                        mov rcx, rsi
009245E3  E8 1C DE FA FF                  call 0x1408d2404
009245E8  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
009245EC  E8 13 DE FA FF                  call 0x1408d2404
009245F1  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
009245F5  E8 0A DE FA FF                  call 0x1408d2404
009245FA  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
009245FE  E8 01 DE FA FF                  call 0x1408d2404
00924603  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00924607  E8 F8 DD FA FF                  call 0x1408d2404
0092460C  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
00924610  E8 EF DD FA FF                  call 0x1408d2404
00924615  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00924619  E8 E6 DD FA FF                  call 0x1408d2404
0092461E  33 C9                           xor ecx, ecx
00924620  E8 DF DD FA FF                  call 0x1408d2404
00924625  41 8B C5                        mov eax, r13d
00924628  48 81 C4 98 00 00 00            add rsp, 0x98
0092462F  41 5F                           pop r15
00924631  41 5E                           pop r14
00924633  41 5D                           pop r13
00924635  41 5C                           pop r12
00924637  5F                              pop rdi
00924638  5E                              pop rsi
00924639  5B                              pop rbx
0092463A  5D                              pop rbp
0092463B  C3                              ret
0092463C  CC                              int3
0092463D  B8 58 00 00 C0                  mov eax, 0xc0000058
00924642  E9 CB FE FF FF                  jmp 0x140924512
00924647  4C 8D 05 E2 D6 6E FF            lea r8, [rip - 0x91291e]
0092464E  C7 44 24 20 3A 00 00 00         mov dword ptr [rsp + 0x20], 0x3a
00924656  E8 C5 04 BE FF                  call 0x140504b20
0092465B  E9 12 FF FF FF                  jmp 0x140924572
00924660  8B DE                           mov ebx, esi
00924662  4C 8D 0D C3 D6 6E FF            lea r9, [rip - 0x91293d]
00924669  49 D1 EC                        shr r12, 1
0092466C  49 8B D4                        mov rdx, r12
0092466F  48 2B D3                        sub rdx, rbx
00924672  48 8D 0C 58                     lea rcx, [rax + rbx*2]
00924676  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
0092467A  48 85 C0                        test rax, rax
0092467D  74 54                           je 0x1409246d3
0092467F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00924684  4C 8D 05 8D D6 6E FF            lea r8, [rip - 0x912973]
0092468B  C7 44 24 20 3A 00 00 00         mov dword ptr [rsp + 0x20], 0x3a
00924693  E8 88 04 BE FF                  call 0x140504b20
00924698  4C 8B 45 E7                     mov r8, qword ptr [rbp - 0x19]
0092469C  45 33 C9                        xor r9d, r9d
0092469F  49 8B 0E                        mov rcx, qword ptr [r14]
009246A2  4D 85 C0                        test r8, r8
009246A5  0F 84 24 FF FF FF               je 0x1409245cf
009246AB  48 8D 04 59                     lea rax, [rcx + rbx*2]
009246AF  49 FF C7                        inc r15
009246B2  66 46 39 0C 78                  cmp word ptr [rax + r15*2], r9w
009246B7  75 F6                           jne 0x1409246af
009246B9  44 03 FE                        add r15d, esi
009246BC  41 8B C7                        mov eax, r15d
009246BF  4C 2B E0                        sub r12, rax
009246C2  49 8B D4                        mov rdx, r12
009246C5  4A 8D 0C 79                     lea rcx, [rcx + r15*2]
009246C9  E8 E2 1D BE FF                  call 0x1405064b0
009246CE  E9 FC FE FF FF                  jmp 0x1409245cf
009246D3  4C 8D 05 56 D6 6E FF            lea r8, [rip - 0x9129aa]
009246DA  C7 44 24 20 3A 00 00 00         mov dword ptr [rsp + 0x20], 0x3a
009246E2  E8 39 04 BE FF                  call 0x140504b20
009246E7  EB AF                           jmp 0x140924698
009246E9  8D 3C 47                        lea edi, [rdi + rax*2]
009246EC  83 C7 04                        add edi, 4
009246EF  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
009246F3  48 85 D2                        test rdx, rdx
009246F6  74 13                           je 0x14092470b
009246F8  49 8B C7                        mov rax, r15
009246FB  48 FF C0                        inc rax
009246FE  66 44 39 24 42                  cmp word ptr [rdx + rax*2], r12w
00924703  75 F6                           jne 0x1409246fb
00924705  8D 3C 47                        lea edi, [rdi + rax*2]
00924708  83 C7 04                        add edi, 4
0092470B  84 C9                           test cl, cl
0092470D  0F 85 CE 00 00 00               jne 0x1409247e1
00924713  84 DB                           test bl, bl
00924715  0F 85 EB 00 00 00               jne 0x140924806
0092471B  44 8B E7                        mov r12d, edi
0092471E  49 83 C4 02                     add r12, 2
00924722  49 8B CC                        mov rcx, r12
00924725  E8 5E 18 00 00                  call 0x140925f88
0092472A  48 8B 5D 77                     mov rbx, qword ptr [rbp + 0x77]
0092472E  45 33 C9                        xor r9d, r9d
00924731  48 89 03                        mov qword ptr [rbx], rax
00924734  48 85 C0                        test rax, rax
00924737  0F 84 07 03 00 00               je 0x140924a44
0092473D  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00924741  4D 8B F4                        mov r14, r12
00924744  49 D1 EE                        shr r14, 1
00924747  41 8B F1                        mov esi, r9d
0092474A  48 85 C9                        test rcx, rcx
0092474D  74 39                           je 0x140924788
0092474F  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00924754  4C 8D 0D B5 D5 6E FF            lea r9, [rip - 0x912a4b]
0092475B  48 8B C8                        mov rcx, rax
0092475E  C7 44 24 20 3A 00 00 00         mov dword ptr [rsp + 0x20], 0x3a
00924766  4C 8D 05 AB D5 6E FF            lea r8, [rip - 0x912a55]
0092476D  49 8B D6                        mov rdx, r14
00924770  E8 AB 03 BE FF                  call 0x140504b20
00924775  48 8B 03                        mov rax, qword ptr [rbx]
00924778  45 33 C9                        xor r9d, r9d
0092477B  49 8B F7                        mov rsi, r15
0092477E  48 FF C6                        inc rsi
00924781  66 44 39 0C 70                  cmp word ptr [rax + rsi*2], r9w
00924786  75 F6                           jne 0x14092477e
00924788  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
0092478C  4D 85 C0                        test r8, r8
0092478F  0F 84 9A FD FF FF               je 0x14092452f
00924795  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0092479A  4C 8D 0D 6B D5 6E FF            lea r9, [rip - 0x912a95]
009247A1  8B DE                           mov ebx, esi
009247A3  4C 8D 05 6E D5 6E FF            lea r8, [rip - 0x912a92]
009247AA  49 8B D6                        mov rdx, r14
009247AD  C7 44 24 20 3A 00 00 00         mov dword ptr [rsp + 0x20], 0x3a
009247B5  48 2B D3                        sub rdx, rbx
009247B8  48 8D 0C 58                     lea rcx, [rax + rbx*2]
009247BC  E8 5F 03 BE FF                  call 0x140504b20
009247C1  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
009247C5  45 33 C9                        xor r9d, r9d
009247C8  48 8B 01                        mov rax, qword ptr [rcx]
009247CB  49 8B CF                        mov rcx, r15
009247CE  48 8D 14 58                     lea rdx, [rax + rbx*2]
009247D2  48 FF C1                        inc rcx
009247D5  66 44 39 0C 4A                  cmp word ptr [rdx + rcx*2], r9w
009247DA  75 F6                           jne 0x1409247d2
009247DC  E9 4C FD FF FF                  jmp 0x14092452d
009247E1  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
009247E5  83 C7 04                        add edi, 4
009247E8  48 85 C9                        test rcx, rcx
009247EB  0F 84 22 FF FF FF               je 0x140924713
009247F1  49 8B C7                        mov rax, r15
009247F4  48 FF C0                        inc rax
009247F7  66 44 39 24 41                  cmp word ptr [rcx + rax*2], r12w
009247FC  75 F6                           jne 0x1409247f4
009247FE  8D 3C 47                        lea edi, [rdi + rax*2]
00924801  E9 0D FF FF FF                  jmp 0x140924713
00924806  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
0092480A  83 C7 04                        add edi, 4
0092480D  48 85 C9                        test rcx, rcx
00924810  0F 84 05 FF FF FF               je 0x14092471b
00924816  49 8B C7                        mov rax, r15
00924819  48 FF C0                        inc rax
0092481C  66 44 39 24 41                  cmp word ptr [rcx + rax*2], r12w
00924821  75 F6                           jne 0x140924819
00924823  8D 3C 47                        lea edi, [rdi + rax*2]
00924826  E9 F0 FE FF FF                  jmp 0x14092471b
0092482B  4D 85 FF                        test r15, r15
0092482E  74 1F                           je 0x14092484f
00924830  45 33 C0                        xor r8d, r8d
00924833  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00924838  48 8D 55 CF                     lea rdx, [rbp - 0x31]
0092483C  49 8B CF                        mov rcx, r15
0092483F  E8 E4 BA 0D 00                  call 0x140a00328
00924844  44 8B E8                        mov r13d, eax
00924847  85 C0                           test eax, eax
00924849  0F 85 8D FD FF FF               jne 0x1409245dc
0092484F  66 85 DB                        test bx, bx
00924852  74 36                           je 0x14092488a
00924854  4C 8D 45 DF                     lea r8, [rbp - 0x21]
00924858  BA 01 00 00 00                  mov edx, 1
0092485D  0F B7 CB                        movzx ecx, bx
00924860  E8 0F 0E 13 00                  call 0x140a55674
00924865  44 8B E8                        mov r13d, eax
00924868  85 C0                           test eax, eax
0092486A  0F 85 6C FD FF FF               jne 0x1409245dc
00924870  4C 8D 45 D7                     lea r8, [rbp - 0x29]
00924874  0F B7 CB                        movzx ecx, bx
00924877  8D 50 02                        lea edx, [rax + 2]
0092487A  E8 F5 0D 13 00                  call 0x140a55674
0092487F  44 8B E8                        mov r13d, eax
00924882  85 C0                           test eax, eax
00924884  0F 85 52 FD FF FF               jne 0x1409245dc
0092488A  8A 5D 57                        mov bl, byte ptr [rbp + 0x57]
0092488D  84 DB                           test bl, bl
0092488F  74 3C                           je 0x1409248cd
00924891  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00924896  48 8D 45 67                     lea rax, [rbp + 0x67]
0092489A  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0092489F  4C 8D 4D E7                     lea r9, [rbp - 0x19]
009248A3  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
009248A8  45 33 C0                        xor r8d, r8d
009248AB  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
009248B0  8A D3                           mov dl, bl
009248B2  49 8B CE                        mov rcx, r14
009248B5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009248BA  E8 49 BB 0D 00                  call 0x140a00408
009248BF  44 8B E8                        mov r13d, eax
009248C2  85 C0                           test eax, eax
009248C4  0F 85 12 FD FF FF               jne 0x1409245dc
009248CA  8B 7D 67                        mov edi, dword ptr [rbp + 0x67]
009248CD  8A 4D 5F                        mov cl, byte ptr [rbp + 0x5f]
009248D0  84 C9                           test cl, cl
009248D2  74 40                           je 0x140924914
009248D4  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
009248D9  48 8D 45 67                     lea rax, [rbp + 0x67]
009248DD  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
009248E2  4C 8D 4D EF                     lea r9, [rbp - 0x11]
009248E6  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
009248EB  8A D1                           mov dl, cl
009248ED  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
009248F1  41 B0 01                        mov r8b, 1
009248F4  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
009248F9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009248FE  E8 05 BB 0D 00                  call 0x140a00408
00924903  44 8B E8                        mov r13d, eax
00924906  85 C0                           test eax, eax
00924908  0F 85 CE FC FF FF               jne 0x1409245dc
0092490E  03 7D 67                        add edi, dword ptr [rbp + 0x67]
00924911  8A 4D 5F                        mov cl, byte ptr [rbp + 0x5f]
00924914  48 8B 75 BF                     mov rsi, qword ptr [rbp - 0x41]
00924918  49 83 CF FF                     or r15, 0xffffffffffffffff
0092491C  48 85 F6                        test rsi, rsi
0092491F  0F 84 CA FD FF FF               je 0x1409246ef
00924925  49 8B C7                        mov rax, r15
00924928  48 FF C0                        inc rax
0092492B  66 44 39 24 46                  cmp word ptr [rsi + rax*2], r12w
00924930  75 F6                           jne 0x140924928
00924932  E9 B2 FD FF FF                  jmp 0x1409246e9
00924937  41 81 E4 F8 01 00 00            and r12d, 0x1f8
0092493E  74 23                           je 0x140924963
00924940  80 3B 01                        cmp byte ptr [rbx], 1
00924943  0F 85 E2 00 00 00               jne 0x140924a2b
00924949  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
0092494D  A8 10                           test al, 0x10
0092494F  0F 85 8B 00 00 00               jne 0x1409249e0
00924955  8A CA                           mov cl, dl
00924957  88 55 57                        mov byte ptr [rbp + 0x57], dl
0092495A  84 C9                           test cl, cl
0092495C  74 05                           je 0x140924963
0092495E  4D 85 F6                        test r14, r14
00924961  75 40                           jne 0x1409249a3
00924963  4C 8B E7                        mov r12, rdi
00924966  80 3B 01                        cmp byte ptr [rbx], 1
00924969  0F 85 CB 00 00 00               jne 0x140924a3a
0092496F  0F B7 5B 02                     movzx ebx, word ptr [rbx + 2]
00924973  45 33 E4                        xor r12d, r12d
00924976  48 85 F6                        test rsi, rsi
00924979  0F 84 AC FE FF FF               je 0x14092482b
0092497F  45 33 C0                        xor r8d, r8d
00924982  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00924987  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0092498B  48 8B CE                        mov rcx, rsi
0092498E  E8 95 B9 0D 00                  call 0x140a00328
00924993  44 8B E8                        mov r13d, eax
00924996  85 C0                           test eax, eax
00924998  0F 85 3E FC FF FF               jne 0x1409245dc
0092499E  E9 88 FE FF FF                  jmp 0x14092482b
009249A3  45 8B CC                        mov r9d, r12d
009249A6  4C 8D 45 67                     lea r8, [rbp + 0x67]
009249AA  33 D2                           xor edx, edx
009249AC  49 8B CE                        mov rcx, r14
009249AF  E8 2C C7 14 00                  call 0x140a710e0
009249B4  8B 4D 67                        mov ecx, dword ptr [rbp + 0x67]
009249B7  E8 CC 15 00 00                  call 0x140925f88
009249BC  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
009249C0  48 85 C0                        test rax, rax
009249C3  74 58                           je 0x140924a1d
009249C5  45 8B CC                        mov r9d, r12d
009249C8  4C 8D 45 67                     lea r8, [rbp + 0x67]
009249CC  48 8B D0                        mov rdx, rax
009249CF  49 8B CE                        mov rcx, r14
009249D2  E8 09 C7 14 00                  call 0x140a710e0
009249D7  4C 8B 65 C7                     mov r12, qword ptr [rbp - 0x39]
009249DB  4D 8B F4                        mov r14, r12
009249DE  EB 86                           jmp 0x140924966
009249E0  B1 01                           mov cl, 1
009249E2  88 4D 57                        mov byte ptr [rbp + 0x57], cl
009249E5  66 85 C0                        test ax, ax
009249E8  79 2A                           jns 0x140924a14
009249EA  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
009249ED  85 C0                           test eax, eax
009249EF  74 09                           je 0x1409249fa
009249F1  4C 8D 34 03                     lea r14, [rbx + rax]
009249F5  E9 60 FF FF FF                  jmp 0x14092495a
009249FA  4C 8B F2                        mov r14, rdx
009249FD  E9 58 FF FF FF                  jmp 0x14092495a
00924A02  49 8B 71 08                     mov rsi, qword ptr [r9 + 8]
00924A06  E9 B8 FA FF FF                  jmp 0x1409244c3
00924A0B  4D 8B 79 10                     mov r15, qword ptr [r9 + 0x10]
00924A0F  E9 D6 FA FF FF                  jmp 0x1409244ea
00924A14  4C 8B 73 18                     mov r14, qword ptr [rbx + 0x18]
00924A18  E9 3D FF FF FF                  jmp 0x14092495a
00924A1D  4C 8B 65 C7                     mov r12, qword ptr [rbp - 0x39]
00924A21  B8 17 00 00 C0                  mov eax, 0xc0000017
00924A26  E9 EA FA FF FF                  jmp 0x140924515
00924A2B  B9 58 00 00 C0                  mov ecx, 0xc0000058
00924A30  E8 0B 22 00 00                  call 0x140926c40
00924A35  E9 EE FB FF FF                  jmp 0x140924628
00924A3A  B8 58 00 00 C0                  mov eax, 0xc0000058
00924A3F  E9 D1 FA FF FF                  jmp 0x140924515
00924A44  41 BD 08 00 00 00               mov r13d, 8
00924A4A  E9 91 FB FF FF                  jmp 0x1409245e0
00924A4F  4C 8B 75 77                     mov r14, qword ptr [rbp + 0x77]
00924A53  E9 6D FB FF FF                  jmp 0x1409245c5
00924A58  B8 57 00 00 00                  mov eax, 0x57
00924A5D  E9 C6 FB FF FF                  jmp 0x140924628
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalConvertSDToStringSD_Rev1(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (152);
    a2 = 0;
    v_stack_p20 = 0;
    v_stack_m50 = 0;
    v_stack_m80 = 0;
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    v_stack_m88 = 0;
    v_stack_m78 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    v_stack_m70 = 0;
    if (a4 == 0) goto loc_00924A58;
    if (a6 == 0) goto loc_00924A58;
    if ((((unsigned __int8)((unsigned int)(a5))) & (1)) == 0) goto loc_009244C3;
    if ((*(unsigned __int8 *)(a4)) != 1) goto loc_0092463D;
    if ((*(unsigned __int16 *)(a4 + 2)) >= 0) goto loc_00924A02;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))) != 0) {
        v_rsi = a4 + (unsigned int)(*(unsigned int *)(a4 + 4)) * 1;
    }
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) == 0) goto loc_009244EA;
    if ((*(unsigned __int8 *)(a4)) != 1) goto loc_0092463D;
    if ((*(unsigned __int16 *)(a4 + 2)) >= 0) goto loc_00924A0B;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))) != 0) {
        v_r15 = a4 + (unsigned int)(*(unsigned int *)(a4 + 8)) * 1;
    }
    if ((((unsigned __int8)((unsigned int)(a5))) & (4)) == 0) goto loc_00924937;
    result = RtlGetDaclSecurityDescriptor(a4, v_stack_p18, v_stack_m50, v_stack_p8);
    a2 = 0;
    if (!sign_flag) goto loc_00924937;
loc_00924512:
loc_00924515:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)(result)), a2, v_stack_m50, v_stack_p8);
    result = PdcCloseEvent(0, a2, v_stack_m50, v_stack_p8);
    goto loc_00924628;
loc_0092452D:
    v_rsi = (unsigned int)((v_rsi) + (0));
loc_0092452F:
    if (v_stack_p18 == ((unsigned __int8)(v_stack_p8))) goto loc_00924A4F;
    v_r14 = (0) - ((unsigned int)((unsigned int)(v_rsi)));
    if (v_stack_m68 == 0) goto loc_00924647;
    v_stack_mB0 = v_stack_m68;
    v_stack_mB8 = 58;
    result = swprintf_s((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) + (unsigned int)((unsigned int)(v_rsi)) * 2, v_r14, v_rip - 9513037, v_rip - 9513006);
loc_00924572:
    a4 = 0;
loc_00924583:
    a1 = (v_r15) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a6) + (unsigned int)((unsigned int)(v_rsi)) * 2 + a1 * 2)) != 0) goto loc_00924583;
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(a1)));
    if (v_stack_m58 == 0) goto loc_009245C5;
    a2 = (0) >> (1);
    a2 = (a2) - ((unsigned int)((unsigned int)(v_rsi)));
    result = wcscpy_s(*(unsigned __int64 *)(a6) + v_rsi * 2, a2, v_stack_m58, a4);
    a4 = 0;
loc_009245B9:
    a1 = (v_r15) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a6) + v_rsi * 2 + a1 * 2)) != 0) goto loc_009245B9;
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(a1)));
loc_009245C5:
    if (v_stack_p10 != 0) goto loc_00924660;
loc_009245CF:
    v_rdi = 0;
    if (a7 != 0) {
        v_rdi = (unsigned int)((0) >> (1));
        *(unsigned int *)(a7) = (unsigned int)(v_rdi);
    }
loc_009245E0:
    result = PdcCloseEvent(v_stack_m88, *(unsigned __int64 *)(a6) + v_rsi * 2, v_stack_m58, a4);
    result = PdcCloseEvent(v_stack_m78, *(unsigned __int64 *)(a6) + v_rsi * 2, v_stack_m58, a4);
    result = PdcCloseEvent(v_stack_m60, *(unsigned __int64 *)(a6) + v_rsi * 2, v_stack_m58, a4);
    result = PdcCloseEvent(v_stack_m58, *(unsigned __int64 *)(a6) + v_rsi * 2, v_stack_m58, a4);
    result = PdcCloseEvent(v_stack_m70, *(unsigned __int64 *)(a6) + v_rsi * 2, v_stack_m58, a4);
    result = PdcCloseEvent(v_stack_m68, *(unsigned __int64 *)(a6) + v_rsi * 2, v_stack_m58, a4);
    result = PdcCloseEvent(v_stack_m80, *(unsigned __int64 *)(a6) + v_rsi * 2, v_stack_m58, a4);
    a1 = 0;
    result = PdcCloseEvent(a1, *(unsigned __int64 *)(a6) + v_rsi * 2, v_stack_m58, a4);
loc_00924628:
    v_rsp = (v_rsp) + (152);
    return 0;
loc_0092463D:
    goto loc_00924512;
loc_00924647:
    v_stack_p20 = 58;
    result = swprintf_s(a1, *(unsigned __int64 *)(a6) + v_rsi * 2, v_rip - 9513246, a4);
    goto loc_00924572;
loc_00924660:
    v_r12 = (0) >> (1);
    a2 = (v_r12) - ((unsigned int)((unsigned int)(v_stack_m88)));
    if (v_stack_m70 == 0) goto loc_009246D3;
    v_stack_p28 = v_stack_m70;
    v_stack_p20 = 58;
    result = swprintf_s(result + (unsigned int)((unsigned int)(v_stack_m88)) * 2, a2, v_rip - 9513331, v_rip - 9513277);
loc_00924698:
    a4 = 0;
    if (v_stack_m60 == 0) goto loc_009245CF;
loc_009246AF:
    v_r15 = (v_r15) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a6) + (unsigned int)((unsigned int)(v_stack_m88)) * 2 + v_r15 * 2)) != 0) goto loc_009246AF;
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_stack_m88)));
    v_r12 = (v_r12) - ((unsigned int)((unsigned int)(v_r15)));
    result = wcscpy_s(*(unsigned __int64 *)(a6) + v_r15 * 2, v_r12, v_stack_m60, a4);
    goto loc_009245CF;
loc_009246D3:
    v_stack_p20 = 58;
    result = swprintf_s(*(unsigned __int64 *)(a6) + v_r15 * 2, v_r12, v_rip - 9513386, a4);
    goto loc_00924698;
loc_009246E9:
    v_rdi = (unsigned int)((v_rdi + result * 2) + (4));
loc_009246EF:
    if (v_stack_m78 == 0) goto loc_0092470B;
loc_009246FB:
    result = (v_r15) + 1;
    if ((*(unsigned __int16 *)(v_stack_m78 + result * 2)) != ((unsigned __int16)(v_r12))) goto loc_009246FB;
    v_rdi = (unsigned int)((v_rdi + result * 2) + (4));
loc_0092470B:
    if ((unsigned __int8)(*(unsigned __int64 *)(a6) + v_r15 * 2) != 0) goto loc_009247E1;
loc_00924713:
    if ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_m88))) != 0) goto loc_00924806;
loc_0092471B:
    v_r12 = ((unsigned int)((unsigned int)(v_rdi))) + (2);
    result = SddlpAlloc(v_r12, v_stack_m78, v_rip - 9513386, a4);
    a4 = 0;
    *(unsigned __int64 *)(a6) = result;
    if (result == 0) goto loc_00924A44;
    v_r14 = (v_r12) >> (1);
    if (v_stack_m88 == 0) goto loc_00924788;
    v_stack_p28 = v_stack_m88;
    v_stack_p20 = 58;
    result = swprintf_s(result, v_r14, v_rip - 9513557, v_rip - 9513547);
    a4 = 0;
loc_0092477E:
    v_rsi = (v_r15) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a6) + v_rsi * 2)) != 0) goto loc_0092477E;
loc_00924788:
    if (v_stack_m78 == 0) goto loc_0092452F;
    v_stack_p28 = v_stack_m78;
    v_stack_p20 = 58;
    a2 = (v_r14) - ((unsigned int)((unsigned int)(v_rsi)));
    result = swprintf_s(*(unsigned __int64 *)(a6) + (unsigned int)((unsigned int)(v_rsi)) * 2, a2, v_rip - 9513618, v_rip - 9513621);
    a4 = 0;
loc_009247D2:
    a1 = (v_r15) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a6) + (unsigned int)((unsigned int)(v_rsi)) * 2 + a1 * 2)) != 0) goto loc_009247D2;
    goto loc_0092452D;
loc_009247E1:
    v_rdi = (unsigned int)((v_rdi) + (4));
    if (v_stack_m68 == 0) goto loc_00924713;
loc_009247F4:
    result = (v_r15) + 1;
    if ((*(unsigned __int16 *)(v_stack_m68 + result * 2)) != ((unsigned __int16)(v_r12))) goto loc_009247F4;
    goto loc_00924713;
loc_00924806:
    v_rdi = (unsigned int)((v_rdi + result * 2) + (4));
    if (v_stack_m70 == 0) goto loc_0092471B;
loc_00924819:
    result = (v_r15) + 1;
    if ((*(unsigned __int16 *)(v_stack_m70 + result * 2)) != ((unsigned __int16)(v_r12))) goto loc_00924819;
    goto loc_0092471B;
loc_0092482B:
    if (v_r15 == 0) goto loc_0092484F;
    a3 = 0;
    v_stack_p28 = 1;
    result = LocalGetStringForSid(v_r15, v_stack_m78, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_009245DC;
loc_0092484F:
    if ((unsigned __int16)((unsigned int)((unsigned int)(v_rsi))) == 0) goto loc_0092488A;
    result = LocalGetStringForControl((unsigned __int16)((unsigned int)((unsigned int)(v_rsi))), 1, v_stack_m68, a4);
    if ((unsigned int)(result) != 0) goto loc_009245DC;
    result = LocalGetStringForControl((unsigned __int16)((unsigned int)((unsigned int)(v_rsi))), result + 2, v_stack_m70, a4);
    if ((unsigned int)(result) != 0) goto loc_009245DC;
loc_0092488A:
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_009248CD;
    v_stack_p40 = 1;
    v_stack_p38 = v_r12;
    v_stack_p30 = v_r12;
    a3 = 0;
    v_stack_p28 = v_r12;
    v_stack_p20 = v_stack_p20;
    result = LocalConvertAclToString(v_r14, (unsigned __int8)(v_stack_p10), a3, v_stack_m60);
    if ((unsigned int)(result) != 0) goto loc_009245DC;
loc_009248CD:
    if ((unsigned __int8)(v_stack_p18) == 0) goto loc_00924914;
    v_stack_p40 = 1;
    v_stack_p38 = v_r12;
    v_stack_p30 = v_r12;
    v_stack_p28 = v_r12;
    v_stack_p20 = v_stack_p20;
    result = LocalConvertAclToString(v_stack_m50, (unsigned __int8)(v_stack_p18), 1, v_stack_m58);
    if ((unsigned int)(result) != 0) goto loc_009245DC;
    v_rdi = (unsigned int)(((unsigned int)(v_stack_p20)) + (v_stack_p20));
loc_00924914:
    v_r15 = (v_r15) | (-1);
    if (v_stack_m88 == 0) goto loc_009246EF;
loc_00924928:
    result = (v_r15) + 1;
    if ((*(unsigned __int16 *)(v_stack_m88 + result * 2)) != ((unsigned __int16)(v_r12))) goto loc_00924928;
    goto loc_009246E9;
loc_00924937:
    v_r12 = (unsigned int)((v_r12) & (504));
    if (condition_is_equal) goto loc_00924963;
    if ((*(unsigned __int8 *)(v_stack_p10)) != 1) goto loc_00924A2B;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_p10 + 2))) & (16)) != 0) goto loc_009249E0;
    v_stack_p10 = (unsigned __int8)((unsigned __int8)(v_stack_p18));
loc_0092495A:
    if ((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_stack_p18))) == 0) goto loc_00924963;
    if (v_r14 != 0) goto loc_009249A3;
loc_00924963:
loc_00924966:
    if ((*(unsigned __int8 *)(v_stack_p10)) != 1) goto loc_00924A3A;
    v_r12 = 0;
    if (v_stack_m88 == 0) goto loc_0092482B;
    a3 = 0;
    v_stack_p28 = 1;
    result = LocalGetStringForSid(v_stack_m88, v_stack_m88, a3, v_stack_m58);
    if ((unsigned int)(result) != 0) goto loc_009245DC;
    goto loc_0092482B;
loc_009249A3:
    a2 = 0;
    result = SddlFilterSacl(v_r14, a2, v_stack_p20, 0);
    result = SddlpAlloc((unsigned int)(v_stack_p20), a2, v_stack_p20, 0);
    v_stack_m80 = result;
    if (result == 0) goto loc_00924A1D;
    result = SddlFilterSacl(v_r14, result, v_stack_p20, 0);
    goto loc_00924966;
loc_009249E0:
    v_stack_p10 = 1;
    if (!sign_flag) goto loc_00924A14;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int16 *)(v_stack_p10 + 2) + 12))) == 0) goto loc_009249FA;
    goto loc_0092495A;
loc_009249FA:
    goto loc_0092495A;
loc_00924A02:
    goto loc_009244C3;
loc_00924A0B:
    goto loc_009244EA;
loc_00924A14:
    goto loc_0092495A;
loc_00924A1D:
    goto loc_00924515;
loc_00924A2B:
    result = RtlNtStatusToDosError((unsigned int)(0xC0000058ULL), result, v_stack_p20, 0);
    goto loc_00924628;
loc_00924A3A:
    goto loc_00924515;
loc_00924A44:
    goto loc_009245E0;
loc_00924A4F:
    goto loc_009245C5;
loc_00924A58:
    goto loc_00924628;
}
```

## 5. (Beta) C Style

```c
int64_t LocalConvertSDToStringSD_Rev1(int64_t Arg1, int64_t Arg2, uint8_t Arg3, void *Arg4, uint32_t Arg5, void *Arg6, int64_t Arg7)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m47;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (152);
    Arg2 = 0;
    v_stack_p20 = 0;
    v_stack_m50 = 0;
    v_stack_m80 = 0;
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    v_stack_m88 = 0;
    v_stack_m78 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    v_stack_m70 = 0;
    if (Arg4 == NULL) goto loc_00924A58;
    if (Arg6 == NULL) goto loc_00924A58;
    if ((((uint8_t)((uint32_t)(Arg5))) & (1)) == 0) goto loc_009244C3;
    if ((*(uint8_t *)(arg4)) != 1) goto loc_0092463D;
    if ((*(uint16_t *)(arg4 + 0x2)) >= 0) goto loc_00924A02;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))) != 0) {
        local_rsi = Arg4 + (uint32_t)(*(uint32_t *)(arg4 + 0x4)) * 1;
    }
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) == 0) goto loc_009244EA;
    if ((*(uint8_t *)(arg4)) != 1) goto loc_0092463D;
    if ((*(uint16_t *)(arg4 + 0x2)) >= 0) goto loc_00924A0B;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))) != 0) {
        local_r15 = Arg4 + (uint32_t)(*(uint32_t *)(arg4 + 0x8)) * 1;
    }
    if ((((uint8_t)((uint32_t)(Arg5))) & (4)) == 0) goto loc_00924937;
    result = RtlGetDaclSecurityDescriptor(Arg4, v_stack_p18, v_stack_m50, v_stack_p8);
    Arg2 = 0;
    if (!sign_flag) goto loc_00924937;
loc_00924512:
loc_00924515:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)(result)), Arg2, v_stack_m50, v_stack_p8);
    result = PdcCloseEvent(0, Arg2, v_stack_m50, v_stack_p8);
    goto loc_00924628;
loc_0092452D:
    local_rsi = (uint32_t)((local_rsi) + (0));
loc_0092452F:
    if (v_stack_p18 == ((uint8_t)(v_stack_p8))) goto loc_00924A4F;
    local_r14 = (0) - ((uint32_t)((uint32_t)(local_rsi)));
    if (v_stack_m68 == 0) goto loc_00924647;
    v_stack_mB0 = v_stack_m68;
    v_stack_mB8 = 58;
    result = swprintf_s((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) + (uint32_t)((uint32_t)(local_rsi)) * 2, local_r14, v_rip - 9513037, v_rip - 9513006);
loc_00924572:
    Arg4 = 0;
loc_00924583:
    Arg1 = (local_r15) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg6) + (uint32_t)((uint32_t)(local_rsi)) * 2 + Arg1 * 2)) != 0) goto loc_00924583;
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(Arg1)));
    if (v_stack_m58 == 0) goto loc_009245C5;
    Arg2 = (0) >> (1);
    Arg2 = (Arg2) - ((uint32_t)((uint32_t)(local_rsi)));
    result = wcscpy_s(*(uint64_t *)(arg6) + local_rsi * 2, Arg2, v_stack_m58, Arg4);
    Arg4 = 0;
loc_009245B9:
    Arg1 = (local_r15) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg6) + local_rsi * 2 + Arg1 * 2)) != 0) goto loc_009245B9;
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(Arg1)));
loc_009245C5:
    if (v_stack_p10 != 0) goto loc_00924660;
loc_009245CF:
    local_rdi = 0;
    if (Arg7 != 0) {
        local_rdi = (uint32_t)((0) >> (1));
        *(uint32_t *)(Arg7) = (uint32_t)(local_rdi);
    }
loc_009245E0:
    result = PdcCloseEvent(v_stack_m88, *(uint64_t *)(arg6) + local_rsi * 2, v_stack_m58, Arg4);
    result = PdcCloseEvent(v_stack_m78, *(uint64_t *)(arg6) + local_rsi * 2, v_stack_m58, Arg4);
    result = PdcCloseEvent(v_stack_m60, *(uint64_t *)(arg6) + local_rsi * 2, v_stack_m58, Arg4);
    result = PdcCloseEvent(v_stack_m58, *(uint64_t *)(arg6) + local_rsi * 2, v_stack_m58, Arg4);
    result = PdcCloseEvent(v_stack_m70, *(uint64_t *)(arg6) + local_rsi * 2, v_stack_m58, Arg4);
    result = PdcCloseEvent(v_stack_m68, *(uint64_t *)(arg6) + local_rsi * 2, v_stack_m58, Arg4);
    result = PdcCloseEvent(v_stack_m80, *(uint64_t *)(arg6) + local_rsi * 2, v_stack_m58, Arg4);
    Arg1 = 0;
    result = PdcCloseEvent(Arg1, *(uint64_t *)(arg6) + local_rsi * 2, v_stack_m58, Arg4);
loc_00924628:
    local_rsp = (local_rsp) + (152);
    return 0;
loc_0092463D:
    goto loc_00924512;
loc_00924647:
    v_stack_p20 = 58;
    result = swprintf_s(Arg1, *(uint64_t *)(arg6) + local_rsi * 2, v_rip - 9513246, Arg4);
    goto loc_00924572;
loc_00924660:
    local_r12 = (0) >> (1);
    Arg2 = (local_r12) - ((uint32_t)((uint32_t)(v_stack_m88)));
    if (v_stack_m70 == 0) goto loc_009246D3;
    v_stack_p28 = v_stack_m70;
    v_stack_p20 = 58;
    result = swprintf_s(result + (uint32_t)((uint32_t)(v_stack_m88)) * 2, Arg2, v_rip - 9513331, v_rip - 9513277);
loc_00924698:
    Arg4 = 0;
    if (v_stack_m60 == 0) goto loc_009245CF;
loc_009246AF:
    local_r15 = (local_r15) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg6) + (uint32_t)((uint32_t)(v_stack_m88)) * 2 + local_r15 * 2)) != 0) goto loc_009246AF;
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(v_stack_m88)));
    local_r12 = (local_r12) - ((uint32_t)((uint32_t)(local_r15)));
    result = wcscpy_s(*(uint64_t *)(arg6) + local_r15 * 2, local_r12, v_stack_m60, Arg4);
    goto loc_009245CF;
loc_009246D3:
    v_stack_p20 = 58;
    result = swprintf_s(*(uint64_t *)(arg6) + local_r15 * 2, local_r12, v_rip - 9513386, Arg4);
    goto loc_00924698;
loc_009246E9:
    local_rdi = (uint32_t)((local_rdi + result * 2) + (4));
loc_009246EF:
    if (v_stack_m78 == 0) goto loc_0092470B;
loc_009246FB:
    result = (local_r15) + 1;
    if ((*(uint16_t *)(v_stack_m78 + result * 2)) != ((uint16_t)(local_r12))) goto loc_009246FB;
    local_rdi = (uint32_t)((local_rdi + result * 2) + (4));
loc_0092470B:
    if ((uint8_t)(*(uint64_t *)(arg6) + local_r15 * 2) != 0) goto loc_009247E1;
loc_00924713:
    if ((uint8_t)((uint32_t)((uint32_t)(v_stack_m88))) != 0) goto loc_00924806;
loc_0092471B:
    local_r12 = ((uint32_t)((uint32_t)(local_rdi))) + (2);
    result = SddlpAlloc(local_r12, v_stack_m78, v_rip - 9513386, Arg4);
    Arg4 = 0;
    *(uint64_t *)(arg6) = result;
    if (result == 0) goto loc_00924A44;
    local_r14 = (local_r12) >> (1);
    if (v_stack_m88 == 0) goto loc_00924788;
    v_stack_p28 = v_stack_m88;
    v_stack_p20 = 58;
    result = swprintf_s(result, local_r14, v_rip - 9513557, v_rip - 9513547);
    Arg4 = 0;
loc_0092477E:
    local_rsi = (local_r15) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg6) + local_rsi * 2)) != 0) goto loc_0092477E;
loc_00924788:
    if (v_stack_m78 == 0) goto loc_0092452F;
    v_stack_p28 = v_stack_m78;
    v_stack_p20 = 58;
    Arg2 = (local_r14) - ((uint32_t)((uint32_t)(local_rsi)));
    result = swprintf_s(*(uint64_t *)(arg6) + (uint32_t)((uint32_t)(local_rsi)) * 2, Arg2, v_rip - 9513618, v_rip - 9513621);
    Arg4 = 0;
loc_009247D2:
    Arg1 = (local_r15) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg6) + (uint32_t)((uint32_t)(local_rsi)) * 2 + Arg1 * 2)) != 0) goto loc_009247D2;
    goto loc_0092452D;
loc_009247E1:
    local_rdi = (uint32_t)((local_rdi) + (4));
    if (v_stack_m68 == 0) goto loc_00924713;
loc_009247F4:
    result = (local_r15) + 1;
    if ((*(uint16_t *)(v_stack_m68 + result * 2)) != ((uint16_t)(local_r12))) goto loc_009247F4;
    goto loc_00924713;
loc_00924806:
    local_rdi = (uint32_t)((local_rdi + result * 2) + (4));
    if (v_stack_m70 == 0) goto loc_0092471B;
loc_00924819:
    result = (local_r15) + 1;
    if ((*(uint16_t *)(v_stack_m70 + result * 2)) != ((uint16_t)(local_r12))) goto loc_00924819;
    goto loc_0092471B;
loc_0092482B:
    if (local_r15 == 0) goto loc_0092484F;
    Arg3 = 0;
    v_stack_p28 = 1;
    result = LocalGetStringForSid(local_r15, v_stack_m78, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_009245DC;
loc_0092484F:
    if ((uint16_t)((uint32_t)((uint32_t)(local_rsi))) == 0) goto loc_0092488A;
    result = LocalGetStringForControl((uint16_t)((uint32_t)((uint32_t)(local_rsi))), 1, v_stack_m68, Arg4);
    if ((uint32_t)(result) != 0) goto loc_009245DC;
    result = LocalGetStringForControl((uint16_t)((uint32_t)((uint32_t)(local_rsi))), result + 2, v_stack_m70, Arg4);
    if ((uint32_t)(result) != 0) goto loc_009245DC;
loc_0092488A:
    if ((uint8_t)(v_stack_p10) == 0) goto loc_009248CD;
    v_stack_p40 = 1;
    v_stack_p38 = local_r12;
    v_stack_p30 = local_r12;
    Arg3 = 0;
    v_stack_p28 = local_r12;
    v_stack_p20 = v_stack_p20;
    result = LocalConvertAclToString(local_r14, (uint8_t)(v_stack_p10), Arg3, v_stack_m60);
    if ((uint32_t)(result) != 0) goto loc_009245DC;
loc_009248CD:
    if ((uint8_t)(v_stack_p18) == 0) goto loc_00924914;
    v_stack_p40 = 1;
    v_stack_p38 = local_r12;
    v_stack_p30 = local_r12;
    v_stack_p28 = local_r12;
    v_stack_p20 = v_stack_p20;
    result = LocalConvertAclToString(v_stack_m50, (uint8_t)(v_stack_p18), 1, v_stack_m58);
    if ((uint32_t)(result) != 0) goto loc_009245DC;
    local_rdi = (uint32_t)(((uint32_t)(v_stack_p20)) + (v_stack_p20));
loc_00924914:
    local_r15 = (local_r15) | (-1);
    if (v_stack_m88 == 0) goto loc_009246EF;
loc_00924928:
    result = (local_r15) + 1;
    if ((*(uint16_t *)(v_stack_m88 + result * 2)) != ((uint16_t)(local_r12))) goto loc_00924928;
    goto loc_009246E9;
loc_00924937:
    local_r12 = (uint32_t)((local_r12) & (504));
    if (condition_is_equal) goto loc_00924963;
    if ((*(uint8_t *)(v_stack_p10)) != 1) goto loc_00924A2B;
    if ((((uint8_t)(*(uint16_t *)(v_stack_p10 + 0x2))) & (16)) != 0) goto loc_009249E0;
    v_stack_p10 = (uint8_t)((uint8_t)(v_stack_p18));
loc_0092495A:
    if ((uint8_t)((uint8_t)((uint8_t)(v_stack_p18))) == 0) goto loc_00924963;
    if (local_r14 != 0) goto loc_009249A3;
loc_00924963:
loc_00924966:
    if ((*(uint8_t *)(v_stack_p10)) != 1) goto loc_00924A3A;
    local_r12 = 0;
    if (v_stack_m88 == 0) goto loc_0092482B;
    Arg3 = 0;
    v_stack_p28 = 1;
    result = LocalGetStringForSid(v_stack_m88, v_stack_m88, Arg3, v_stack_m58);
    if ((uint32_t)(result) != 0) goto loc_009245DC;
    goto loc_0092482B;
loc_009249A3:
    Arg2 = 0;
    result = SddlFilterSacl(local_r14, Arg2, v_stack_p20, 0);
    result = SddlpAlloc((uint32_t)(v_stack_p20), Arg2, v_stack_p20, 0);
    v_stack_m80 = result;
    if (result == 0) goto loc_00924A1D;
    result = SddlFilterSacl(local_r14, result, v_stack_p20, 0);
    goto loc_00924966;
loc_009249E0:
    v_stack_p10 = 1;
    if (!sign_flag) goto loc_00924A14;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint16_t *)(v_stack_p10 + 0x2) + 0xC))) == 0) goto loc_009249FA;
    goto loc_0092495A;
loc_009249FA:
    goto loc_0092495A;
loc_00924A02:
    goto loc_009244C3;
loc_00924A0B:
    goto loc_009244EA;
loc_00924A14:
    goto loc_0092495A;
loc_00924A1D:
    goto loc_00924515;
loc_00924A2B:
    result = RtlNtStatusToDosError((uint32_t)(0xC0000058ULL), result, v_stack_p20, 0);
    goto loc_00924628;
loc_00924A3A:
    goto loc_00924515;
loc_00924A44:
    goto loc_009245E0;
loc_00924A4F:
    goto loc_009245C5;
loc_00924A58:
    goto loc_00924628;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `8` | `R` |
| `Arg4` | `+ 0x0 + rax*1` | `64` | `R` |
| `Arg4` | `+ 0x2` | `16` | `R` |
| `Arg4` | `+ 0xC` | `32` | `R` |
| `Arg4` | `+ 0x18` | `64` | `R` |
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00924428&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
