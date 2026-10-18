# PiSwPdoPnPDispatch

- RVA: `0x0094DDF0`–`0x0094E2AB` (길이 `1,211` bytes)
- VA: `0x000000014094DDF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000919B4`
- 디코드: `298`개 명령, `1,211/1,211` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0094DE43` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x0094DE7E` → [PnpAllocateMultiSZ](PnpAllocateMultiSZ_function_0094E2B4.md) (function, `0x0094E2B4`)
- `0x0094DEED` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0094DF0B` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0094DF19` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x0094DF52` → [PnpAllocatePWSTR](../8D/PnpAllocatePWSTR_function_008DE620.md) (function, `0x008DE620`)
- `0x0094DF60` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0094DF65` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0094DF72` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x0094DFB9` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x0094DFE4` → [PiSwProcessRemove](PiSwProcessRemove_function_0094E3B8.md) (function, `0x0094E3B8`)
- `0x0094DFEB` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x0094E00A` → [PiSwProcessRemove](PiSwProcessRemove_function_0094E3B8.md) (function, `0x0094E3B8`)
- `0x0094E017` → [PiSwDestroyDeviceObject](PiSwDestroyDeviceObject_function_0094E384.md) (function, `0x0094E384`)
- `0x0094E023` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0094E028` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0094E034` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x0094E0EF` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x0094E107` → [PiSwDeviceInterfacesUpdateState](PiSwDeviceInterfacesUpdateState_function_0094E744.md) (function, `0x0094E744`)
- `0x0094E11E` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x0094E169` → [PiSwCompleteCreate](../8D/PiSwCompleteCreate_function_008DAB90.md) (function, `0x008DAB90`)
- `0x0094E183` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0094E1A7` → [PiSwDeviceMakeCompatibleIds](PiSwDeviceMakeCompatibleIds_function_0094DA8C.md) (function, `0x0094DA8C`)
- `0x0094E1DC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0094E1F8` → [PnpStringFromGuid](../8F/PnpStringFromGuid_function_008F5A2C.md) (function, `0x008F5A2C`)
- `0x0094E223` → [PiSwDeviceInterfacesUpdateState](PiSwDeviceInterfacesUpdateState_function_0094E744.md) (function, `0x0094E744`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0094DF59` → RVA `0x00F8AB20` (`.data`; read)
- `0x0094E047` → RVA `0x0001A390` (`.rdata`; read)
- `0x0094E27E` → RVA `0x000240F8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x0094DEED` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0094DF0B` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0094DF60` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0094DF65` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0094DF72` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (`PAGE` → `.text`)
  - `0x0094E023` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0094E028` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0094E183` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0094E1DC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0094E1E8` → [sub_00B25F74](../B2/Unknown_function_00B25F74.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0094DDF0  48 8B C4                        mov rax, rsp
0094DDF3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0094DDF7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0094DDFB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0094DDFF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0094DE03  41 56                           push r14
0094DE05  48 83 EC 20                     sub rsp, 0x20
0094DE09  48 8B 79 40                     mov rdi, qword ptr [rcx + 0x40]
0094DE0D  48 8B EA                        mov rbp, rdx
0094DE10  8B 5A 30                        mov ebx, dword ptr [rdx + 0x30]
0094DE13  4C 8B F1                        mov r14, rcx
0094DE16  48 8B B2 B8 00 00 00            mov rsi, qword ptr [rdx + 0xb8]
0094DE1D  8B 47 08                        mov eax, dword ptr [rdi + 8]
0094DE20  A8 10                           test al, 0x10
0094DE22  0F 85 DA 03 00 00               jne 0x14094e202
0094DE28  0F B6 4E 01                     movzx ecx, byte ptr [rsi + 1]
0094DE2C  83 F9 09                        cmp ecx, 9
0094DE2F  76 57                           jbe 0x14094de88
0094DE31  83 E9 0C                        sub ecx, 0xc
0094DE34  0F 84 DF 00 00 00               je 0x14094df19
0094DE3A  83 E9 07                        sub ecx, 7
0094DE3D  0F 85 52 01 00 00               jne 0x14094df95
0094DE43  E8 08 9F FA FF                  call 0x1408f7d50
0094DE48  4C 8B 17                        mov r10, qword ptr [rdi]
0094DE4B  4D 85 D2                        test r10, r10
0094DE4E  0F 84 F6 02 00 00               je 0x14094e14a
0094DE54  8B 4E 08                        mov ecx, dword ptr [rsi + 8]
0094DE57  85 C9                           test ecx, ecx
0094DE59  0F 84 82 02 00 00               je 0x14094e0e1
0094DE5F  83 E9 01                        sub ecx, 1
0094DE62  0F 85 33 03 00 00               jne 0x14094e19b
0094DE68  49 8B 4A 18                     mov rcx, qword ptr [r10 + 0x18]
0094DE6C  48 85 C9                        test rcx, rcx
0094DE6F  0F 84 E4 00 00 00               je 0x14094df59
0094DE75  4C 8D 4D 38                     lea r9, [rbp + 0x38]
0094DE79  BA FF FF FF 7F                  mov edx, 0x7fffffff
0094DE7E  E8 31 04 00 00                  call 0x14094e2b4
0094DE83  E9 CF 00 00 00                  jmp 0x14094df57
0094DE88  0F 84 A6 01 00 00               je 0x14094e034
0094DE8E  85 C9                           test ecx, ecx
0094DE90  0F 84 59 02 00 00               je 0x14094e0ef
0094DE96  83 E9 01                        sub ecx, 1
0094DE99  0F 84 8E 01 00 00               je 0x14094e02d
0094DE9F  83 E9 01                        sub ecx, 1
0094DEA2  0F 84 43 01 00 00               je 0x14094dfeb
0094DEA8  83 E9 01                        sub ecx, 1
0094DEAB  0F 84 7C 01 00 00               je 0x14094e02d
0094DEB1  83 E9 01                        sub ecx, 1
0094DEB4  0F 84 73 01 00 00               je 0x14094e02d
0094DEBA  83 E9 01                        sub ecx, 1
0094DEBD  0F 84 6A 01 00 00               je 0x14094e02d
0094DEC3  83 E9 01                        sub ecx, 1
0094DEC6  0F 84 61 01 00 00               je 0x14094e02d
0094DECC  83 F9 01                        cmp ecx, 1
0094DECF  0F 85 95 00 00 00               jne 0x14094df6a
0094DED5  83 7E 08 04                     cmp dword ptr [rsi + 8], 4
0094DED9  0F 85 8B 00 00 00               jne 0x14094df6a
0094DEDF  8D 51 0F                        lea edx, [rcx + 0xf]
0094DEE2  41 B8 50 6E 70 57               mov r8d, 0x57706e50
0094DEE8  B9 00 01 00 00                  mov ecx, 0x100
0094DEED  E8 FE 41 23 00                  call 0x140b820f0
0094DEF2  48 8B D8                        mov rbx, rax
0094DEF5  48 85 C0                        test rax, rax
0094DEF8  0F 84 93 02 00 00               je 0x14094e191
0094DEFE  49 8B CE                        mov rcx, r14
0094DF01  C7 00 01 00 00 00               mov dword ptr [rax], 1
0094DF07  4C 89 70 08                     mov qword ptr [rax + 8], r14
0094DF0B  E8 10 1B 8C FF                  call 0x14020fa20
0094DF10  48 89 5D 38                     mov qword ptr [rbp + 0x38], rbx
0094DF14  E9 14 01 00 00                  jmp 0x14094e02d
0094DF19  E8 32 9E FA FF                  call 0x1408f7d50
0094DF1E  48 8B 17                        mov rdx, qword ptr [rdi]
0094DF21  48 85 D2                        test rdx, rdx
0094DF24  0F 84 20 02 00 00               je 0x14094e14a
0094DF2A  8B 4E 08                        mov ecx, dword ptr [rsi + 8]
0094DF2D  85 C9                           test ecx, ecx
0094DF2F  0F 84 1F 02 00 00               je 0x14094e154
0094DF35  83 F9 01                        cmp ecx, 1
0094DF38  75 1F                           jne 0x14094df59
0094DF3A  48 8B 4A 38                     mov rcx, qword ptr [rdx + 0x38]
0094DF3E  48 85 C9                        test rcx, rcx
0094DF41  74 16                           je 0x14094df59
0094DF43  BA FF FF FF 7F                  mov edx, 0x7fffffff
0094DF48  4C 8D 4D 38                     lea r9, [rbp + 0x38]
0094DF4C  41 B8 50 6E 70 57               mov r8d, 0x57706e50
0094DF52  E8 C9 06 F9 FF                  call 0x1408de620
0094DF57  8B D8                           mov ebx, eax
0094DF59  48 8D 0D C0 CB 63 00            lea rcx, [rip + 0x63cbc0]
0094DF60  E8 AB 1A 91 FF                  call 0x14025fa10
0094DF65  E8 46 F9 90 FF                  call 0x14025d8b0
0094DF6A  33 D2                           xor edx, edx
0094DF6C  89 5D 30                        mov dword ptr [rbp + 0x30], ebx
0094DF6F  48 8B CD                        mov rcx, rbp
0094DF72  E8 49 D6 94 FF                  call 0x14029b5c0
0094DF77  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0094DF7C  8B C3                           mov eax, ebx
0094DF7E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0094DF83  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0094DF88  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
0094DF8D  48 83 C4 20                     add rsp, 0x20
0094DF91  41 5E                           pop r14
0094DF93  C3                              ret
0094DF94  CC                              int3
0094DF95  83 E9 01                        sub ecx, 1
0094DF98  0F 84 80 01 00 00               je 0x14094e11e
0094DF9E  83 E9 01                        sub ecx, 1
0094DFA1  0F 84 CC 01 00 00               je 0x14094e173
0094DFA7  83 E9 01                        sub ecx, 1
0094DFAA  0F 84 BC 02 00 00               je 0x14094e26c
0094DFB0  83 E9 01                        sub ecx, 1
0094DFB3  0F 85 A4 01 00 00               jne 0x14094e15d
0094DFB9  E8 92 9D FA FF                  call 0x1408f7d50
0094DFBE  8B 57 08                        mov edx, dword ptr [rdi + 8]
0094DFC1  83 CA 04                        or edx, 4
0094DFC4  89 57 08                        mov dword ptr [rdi + 8], edx
0094DFC7  8B CA                           mov ecx, edx
0094DFC9  F6 C2 08                        test dl, 8
0094DFCC  0F 85 5B 02 00 00               jne 0x14094e22d
0094DFD2  F6 C1 08                        test cl, 8
0094DFD5  0F 85 7E 02 00 00               jne 0x14094e259
0094DFDB  40 32 F6                        xor sil, sil
0094DFDE  40 8A D6                        mov dl, sil
0094DFE1  49 8B CE                        mov rcx, r14
0094DFE4  E8 CF 03 00 00                  call 0x14094e3b8
0094DFE9  EB 31                           jmp 0x14094e01c
0094DFEB  E8 60 9D FA FF                  call 0x1408f7d50
0094DFF0  8B 47 08                        mov eax, dword ptr [rdi + 8]
0094DFF3  83 C8 02                        or eax, 2
0094DFF6  89 47 08                        mov dword ptr [rdi + 8], eax
0094DFF9  A8 08                           test al, 8
0094DFFB  0F 85 0B 02 00 00               jne 0x14094e20c
0094E001  40 32 F6                        xor sil, sil
0094E004  40 8A D6                        mov dl, sil
0094E007  49 8B CE                        mov rcx, r14
0094E00A  E8 A9 03 00 00                  call 0x14094e3b8
0094E00F  40 84 F6                        test sil, sil
0094E012  75 08                           jne 0x14094e01c
0094E014  49 8B CE                        mov rcx, r14
0094E017  E8 68 03 00 00                  call 0x14094e384
0094E01C  48 8D 0D FD CA 63 00            lea rcx, [rip + 0x63cafd]
0094E023  E8 E8 19 91 FF                  call 0x14025fa10
0094E028  E8 83 F8 90 FF                  call 0x14025d8b0
0094E02D  33 DB                           xor ebx, ebx
0094E02F  E9 36 FF FF FF                  jmp 0x14094df6a
0094E034  E8 17 9D FA FF                  call 0x1408f7d50
0094E039  48 83 3F 00                     cmp qword ptr [rdi], 0
0094E03D  0F 84 07 01 00 00               je 0x14094e14a
0094E043  4C 8B 46 08                     mov r8, qword ptr [rsi + 8]
0094E047  66 0F 6F 05 41 C3 6C FF         movdqa xmm0, xmmword ptr [rip - 0x933cbf]
0094E04F  41 83 60 10 00                  and dword ptr [r8 + 0x10], 0
0094E054  41 C7 40 14 01 00 00 00         mov dword ptr [r8 + 0x14], 1
0094E05C  41 0F 11 40 18                  movups xmmword ptr [r8 + 0x18], xmm0
0094E061  66 41 0F 7E 40 28               movd dword ptr [r8 + 0x28], xmm0
0094E067  41 83 60 2C 00                  and dword ptr [r8 + 0x2c], 0
0094E06C  41 83 60 30 00                  and dword ptr [r8 + 0x30], 0
0094E071  41 8B 48 04                     mov ecx, dword ptr [r8 + 4]
0094E075  81 C9 40 02 00 00               or ecx, 0x240
0094E07B  41 89 48 04                     mov dword ptr [r8 + 4], ecx
0094E07F  48 8B 07                        mov rax, qword ptr [rdi]
0094E082  8B 50 40                        mov edx, dword ptr [rax + 0x40]
0094E085  C1 E2 04                        shl edx, 4
0094E088  33 D1                           xor edx, ecx
0094E08A  83 E2 10                        and edx, 0x10
0094E08D  33 D1                           xor edx, ecx
0094E08F  41 89 50 04                     mov dword ptr [r8 + 4], edx
0094E093  0F BA F2 07                     btr edx, 7
0094E097  48 8B 07                        mov rax, qword ptr [rdi]
0094E09A  8B 48 40                        mov ecx, dword ptr [rax + 0x40]
0094E09D  83 E1 02                        and ecx, 2
0094E0A0  C1 E1 06                        shl ecx, 6
0094E0A3  0B CA                           or ecx, edx
0094E0A5  41 89 48 04                     mov dword ptr [r8 + 4], ecx
0094E0A9  0F BA F1 11                     btr ecx, 0x11
0094E0AD  48 8B 07                        mov rax, qword ptr [rdi]
0094E0B0  8B 50 40                        mov edx, dword ptr [rax + 0x40]
0094E0B3  83 E2 04                        and edx, 4
0094E0B6  C1 E2 0F                        shl edx, 0xf
0094E0B9  0B D1                           or edx, ecx
0094E0BB  41 89 50 04                     mov dword ptr [r8 + 4], edx
0094E0BF  0F BA F2 08                     btr edx, 8
0094E0C3  48 8B 07                        mov rax, qword ptr [rdi]
0094E0C6  8B 48 40                        mov ecx, dword ptr [rax + 0x40]
0094E0C9  C1 E1 05                        shl ecx, 5
0094E0CC  F7 D1                           not ecx
0094E0CE  81 E1 00 01 00 00               and ecx, 0x100
0094E0D4  0B CA                           or ecx, edx
0094E0D6  41 89 48 04                     mov dword ptr [r8 + 4], ecx
0094E0DA  33 DB                           xor ebx, ebx
0094E0DC  E9 78 FE FF FF                  jmp 0x14094df59
0094E0E1  49 8B 4A 08                     mov rcx, qword ptr [r10 + 8]
0094E0E5  BA C8 00 00 00                  mov edx, 0xc8
0094E0EA  E9 59 FE FF FF                  jmp 0x14094df48
0094E0EF  E8 5C 9C FA FF                  call 0x1408f7d50
0094E0F4  8B 47 08                        mov eax, dword ptr [rdi + 8]
0094E0F7  BE 01 00 00 00                  mov esi, 1
0094E0FC  40 84 C6                        test sil, al
0094E0FF  75 D9                           jne 0x14094e0da
0094E101  48 8B 0F                        mov rcx, qword ptr [rdi]
0094E104  40 8A D6                        mov dl, sil
0094E107  E8 38 06 00 00                  call 0x14094e744
0094E10C  8B D8                           mov ebx, eax
0094E10E  85 C0                           test eax, eax
0094E110  0F 88 08 01 00 00               js 0x14094e21e
0094E116  09 77 08                        or dword ptr [rdi + 8], esi
0094E119  E9 3B FE FF FF                  jmp 0x14094df59
0094E11E  E8 2D 9C FA FF                  call 0x1408f7d50
0094E123  48 8B 0F                        mov rcx, qword ptr [rdi]
0094E126  48 85 C9                        test rcx, rcx
0094E129  74 1F                           je 0x14094e14a
0094E12B  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
0094E12F  8B 49 40                        mov ecx, dword ptr [rcx + 0x40]
0094E132  48 8B C2                        mov rax, rdx
0094E135  48 83 E0 FD                     and rax, 0xfffffffffffffffd
0094E139  48 83 CA 02                     or rdx, 2
0094E13D  F6 C1 04                        test cl, 4
0094E140  48 0F 44 D0                     cmove rdx, rax
0094E144  48 89 55 38                     mov qword ptr [rbp + 0x38], rdx
0094E148  EB 90                           jmp 0x14094e0da
0094E14A  BB 0E 00 00 C0                  mov ebx, 0xc000000e
0094E14F  E9 05 FE FF FF                  jmp 0x14094df59
0094E154  48 8B 4A 30                     mov rcx, qword ptr [rdx + 0x30]
0094E158  E9 E1 FD FF FF                  jmp 0x14094df3e
0094E15D  83 F9 02                        cmp ecx, 2
0094E160  0F 85 04 FE FF FF               jne 0x14094df6a
0094E166  49 8B CE                        mov rcx, r14
0094E169  E8 22 CA F8 FF                  call 0x1408dab90
0094E16E  E9 BA FE FF FF                  jmp 0x14094e02d
0094E173  BA 18 00 00 00                  mov edx, 0x18
0094E178  B9 00 01 00 00                  mov ecx, 0x100
0094E17D  41 B8 50 6E 70 57               mov r8d, 0x57706e50
0094E183  E8 68 3F 23 00                  call 0x140b820f0
0094E188  48 85 C0                        test rax, rax
0094E18B  0F 85 ED 00 00 00               jne 0x14094e27e
0094E191  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0094E196  E9 CF FD FF FF                  jmp 0x14094df6a
0094E19B  83 E9 01                        sub ecx, 1
0094E19E  75 11                           jne 0x14094e1b1
0094E1A0  48 8D 55 38                     lea rdx, [rbp + 0x38]
0094E1A4  49 8B CA                        mov rcx, r10
0094E1A7  E8 E0 F8 FF FF                  call 0x14094da8c
0094E1AC  E9 A6 FD FF FF                  jmp 0x14094df57
0094E1B1  83 E9 01                        sub ecx, 1
0094E1B4  0F 84 E3 00 00 00               je 0x14094e29d
0094E1BA  83 F9 02                        cmp ecx, 2
0094E1BD  0F 85 96 FD FF FF               jne 0x14094df59
0094E1C3  49 83 7A 28 00                  cmp qword ptr [r10 + 0x28], 0
0094E1C8  0F 84 8B FD FF FF               je 0x14094df59
0094E1CE  8D 51 4C                        lea edx, [rcx + 0x4c]
0094E1D1  41 B8 50 6E 70 57               mov r8d, 0x57706e50
0094E1D7  B9 00 01 00 00                  mov ecx, 0x100
0094E1DC  E8 0F 3F 23 00                  call 0x140b820f0
0094E1E1  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
0094E1E5  48 85 C0                        test rax, rax
0094E1E8  0F 84 86 7D 1D 00               je 0x140b25f74
0094E1EE  48 8B 0F                        mov rcx, qword ptr [rdi]
0094E1F1  48 8B D0                        mov rdx, rax
0094E1F4  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
0094E1F8  E8 2F 78 FA FF                  call 0x1408f5a2c
0094E1FD  E9 55 FD FF FF                  jmp 0x14094df57
0094E202  BB 0E 00 00 C0                  mov ebx, 0xc000000e
0094E207  E9 5E FD FF FF                  jmp 0x14094df6a
0094E20C  A8 40                           test al, 0x40
0094E20E  0F 85 ED FD FF FF               jne 0x14094e001
0094E214  BE 01 00 00 00                  mov esi, 1
0094E219  E9 E6 FD FF FF                  jmp 0x14094e004
0094E21E  48 8B 0F                        mov rcx, qword ptr [rdi]
0094E221  33 D2                           xor edx, edx
0094E223  E8 1C 05 00 00                  call 0x14094e744
0094E228  E9 2C FD FF FF                  jmp 0x14094df59
0094E22D  48 8B 07                        mov rax, qword ptr [rdi]
0094E230  48 85 C0                        test rax, rax
0094E233  0F 84 99 FD FF FF               je 0x14094dfd2
0094E239  4C 39 70 78                     cmp qword ptr [rax + 0x78], r14
0094E23D  0F 85 8F FD FF FF               jne 0x14094dfd2
0094E243  8B 40 04                        mov eax, dword ptr [rax + 4]
0094E246  A8 02                           test al, 2
0094E248  0F 84 84 FD FF FF               je 0x14094dfd2
0094E24E  83 C9 40                        or ecx, 0x40
0094E251  89 4F 08                        mov dword ptr [rdi + 8], ecx
0094E254  E9 79 FD FF FF                  jmp 0x14094dfd2
0094E259  F6 C1 40                        test cl, 0x40
0094E25C  0F 85 79 FD FF FF               jne 0x14094dfdb
0094E262  BE 01 00 00 00                  mov esi, 1
0094E267  E9 72 FD FF FF                  jmp 0x14094dfde
0094E26C  8A 46 08                        mov al, byte ptr [rsi + 8]
0094E26F  F6 D8                           neg al
0094E271  1B DB                           sbb ebx, ebx
0094E273  81 E3 BB 00 00 C0               and ebx, 0xc00000bb
0094E279  E9 EC FC FF FF                  jmp 0x14094df6a
0094E27E  0F 10 05 73 5E 6D FF            movups xmm0, xmmword ptr [rip - 0x92a18d]
0094E285  83 60 14 00                     and dword ptr [rax + 0x14], 0
0094E289  C7 40 10 0F 00 00 00            mov dword ptr [rax + 0x10], 0xf
0094E290  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
0094E294  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
0094E298  E9 90 FD FF FF                  jmp 0x14094e02d
0094E29D  49 8B 4A 10                     mov rcx, qword ptr [r10 + 0x10]
0094E2A1  BA C8 00 00 00                  mov edx, 0xc8
0094E2A6  E9 9D FC FF FF                  jmp 0x14094df48
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwPdoPnPDispatch(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (32);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 8)))) & (16)) != 0) goto loc_0094E202;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184) + 1))) <= 9) goto loc_0094DE88;
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184) + 1)) - (12));
    if (condition_is_equal) goto loc_0094DF19;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_not_equal) goto loc_0094DF95;
    result = PiSwLock(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) == 0) goto loc_0094E14A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8))) == 0) goto loc_0094E0E1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8))) - (1));
    if (condition_is_not_equal) goto loc_0094E19B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 24) == 0) goto loc_0094DF59;
    result = PnpAllocateMultiSZ(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 24), (unsigned int)(0x7FFFFFFFULL), a3, a2 + 56);
    goto loc_0094DF57;
loc_0094DE88:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 24) == 0) goto loc_0094E034;
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 24)) == 0) goto loc_0094E0EF;
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 24)) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0094DFEB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    if (((unsigned int)(a1)) != 1) goto loc_0094DF6A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8)) != 4) goto loc_0094DF6A;
    result = ExAllocatePool2(256, a1 + 15, (unsigned int)(0x57706E50ULL), a2 + 56);
    if (result == 0) goto loc_0094E191;
    *(unsigned int *)(result) = 1;
    *(unsigned __int64 *)(result + 8) = a1;
    result = ObfReferenceObject(a1, a1 + 15, (unsigned int)(0x57706E50ULL), a2 + 56);
    *(unsigned __int64 *)(a2 + 56) = result;
    goto loc_0094E02D;
loc_0094DF19:
    result = PiSwLock(a1, a1 + 15, (unsigned int)(0x57706E50ULL), a2 + 56);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) == 0) goto loc_0094E14A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8))) == 0) goto loc_0094E154;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8)))) != 1) goto loc_0094DF59;
loc_0094DF3E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 56) == 0) goto loc_0094DF59;
loc_0094DF48:
    result = PnpAllocatePWSTR(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 56), (unsigned int)(0x7FFFFFFFULL), (unsigned int)(0x57706E50ULL), a2 + 56);
loc_0094DF57:
loc_0094DF59:
    result = ExReleaseResourceLite(v_rip + 6540224, (unsigned int)(0x7FFFFFFFULL), (unsigned int)(0x57706E50ULL), a2 + 56);
    result = KeLeaveCriticalRegion(v_rip + 6540224, (unsigned int)(0x7FFFFFFFULL), (unsigned int)(0x57706E50ULL), a2 + 56);
loc_0094DF6A:
    a2 = 0;
    *(unsigned int *)(a2 + 48) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = IofCompleteRequest(0, a2, (unsigned int)(0x57706E50ULL), a2 + 56);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0094DF95:
    a1 = (unsigned int)((0) - (1));
    if (condition_is_equal) goto loc_0094E11E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0094E173;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0094E26C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_0094E15D;
    result = PiSwLock(a1, a2, (unsigned int)(0x57706E50ULL), a2 + 56);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 8))) | (4));
    *(unsigned int *)(v_stack_p20 + 8) = (unsigned int)(a2);
    if ((((unsigned __int8)(a2)) & (8)) != 0) goto loc_0094E22D;
loc_0094DFD2:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(a2)))) & (8)) != 0) goto loc_0094E259;
loc_0094DFDB:
    v_rsi = 0;
loc_0094DFDE:
    result = PiSwProcessRemove(a1, 0, (unsigned int)(0x57706E50ULL), a2 + 56);
    goto loc_0094E01C;
loc_0094DFEB:
    result = PiSwLock(a1, 0, (unsigned int)(0x57706E50ULL), a2 + 56);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 8))) | (2));
    *(unsigned int *)(v_stack_p20 + 8) = (unsigned int)(result);
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0094E20C;
loc_0094E001:
    v_rsi = 0;
loc_0094E004:
    result = PiSwProcessRemove(a1, 0, (unsigned int)(0x57706E50ULL), a2 + 56);
    if (0 == 0) {
        a1 = a1;
        result = PiSwDestroyDeviceObject(a1, 0, (unsigned int)(0x57706E50ULL), a2 + 56);
    }
    result = ExReleaseResourceLite(v_rip + 6540029, 0, (unsigned int)(0x57706E50ULL), a2 + 56);
    result = KeLeaveCriticalRegion(v_rip + 6540029, 0, (unsigned int)(0x57706E50ULL), a2 + 56);
loc_0094E02D:
    v_rbx = 0;
    goto loc_0094DF6A;
loc_0094E034:
    result = PiSwLock(v_rip + 6540029, 0, (unsigned int)(0x57706E50ULL), a2 + 56);
    if ((*(unsigned __int64 *)(v_stack_p20)) == 0) goto loc_0094E14A;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 20) = 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 24) = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 40) = v_xmm0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 4))) | (576));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 4) = (unsigned int)(a1);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20) + 64))) << (4));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) & (16));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 4) = (unsigned int)(a2);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20) + 64))) & (2));
    a1 = (unsigned int)((a1) << (6));
    a1 = (unsigned int)((a1) | ((unsigned int)(a2)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 4) = (unsigned int)(a1);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20) + 64))) & (4));
    a2 = (unsigned int)((a2) << (15));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 4) = (unsigned int)(a2);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20) + 64))) << (5));
    a1 = (unsigned int)(~(a1));
    a1 = (unsigned int)((a1) & (256));
    a1 = (unsigned int)((a1) | ((unsigned int)(a2)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 4) = (unsigned int)(a1);
loc_0094E0DA:
    v_rbx = 0;
    goto loc_0094DF59;
loc_0094E0E1:
    goto loc_0094DF48;
loc_0094E0EF:
    result = PiSwLock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 8), 200, *(unsigned __int64 *)(v_rsi + 8), a2 + 56);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20 + 8))))) != 0) goto loc_0094E0DA;
    result = PiSwDeviceInterfacesUpdateState(*(unsigned __int64 *)(v_stack_p20), 1, *(unsigned __int64 *)(v_rsi + 8), a2 + 56);
    if (sign_flag) goto loc_0094E21E;
    goto loc_0094DF59;
loc_0094E11E:
    result = PiSwLock(*(unsigned __int64 *)(v_stack_p20), 1, *(unsigned __int64 *)(v_rsi + 8), a2 + 56);
    if (*(unsigned __int64 *)(v_stack_p20) == 0) goto loc_0094E14A;
    result = (*(unsigned __int64 *)(v_stack_p10 + 56)) & (-3);
    a2 = (*(unsigned __int64 *)(v_stack_p10 + 56)) | (2);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20) + 64)))) & (4)) == 0) { a2 = result; }
    *(unsigned __int64 *)(v_stack_p10 + 56) = a2;
    goto loc_0094E0DA;
loc_0094E14A:
    goto loc_0094DF59;
loc_0094E154:
    goto loc_0094DF3E;
loc_0094E15D:
    if (((unsigned int)(*(unsigned __int64 *)(a2 + 48))) != 2) goto loc_0094DF6A;
    result = PiSwCompleteCreate(a1, a2, *(unsigned __int64 *)(v_rsi + 8), a2 + 56);
    goto loc_0094E02D;
loc_0094E173:
    result = ExAllocatePool2(256, 24, (unsigned int)(0x57706E50ULL), a2 + 56);
    if (result != 0) goto loc_0094E27E;
loc_0094E191:
    goto loc_0094DF6A;
loc_0094E19B:
    a1 = (unsigned int)((256) - (1));
    if (condition_is_not_equal) goto loc_0094E1B1;
    result = PiSwDeviceMakeCompatibleIds(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)), v_stack_p10 + 56, (unsigned int)(0x57706E50ULL), a2 + 56);
    goto loc_0094DF57;
loc_0094E1B1:
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64))) - (1));
    if (condition_is_equal) goto loc_0094E29D;
    if (((unsigned int)(a1)) != 2) goto loc_0094DF59;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 40)) == 0) goto loc_0094DF59;
    result = ExAllocatePool2(256, a1 + 76, (unsigned int)(0x57706E50ULL), a2 + 56);
    *(unsigned __int64 *)(v_stack_p10 + 56) = result;
    result = PnpStringFromGuid(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20) + 40), result, (unsigned int)(0x57706E50ULL), a2 + 56);
    goto loc_0094DF57;
loc_0094E202:
    goto loc_0094DF6A;
loc_0094E20C:
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_0094E001;
    goto loc_0094E004;
loc_0094E21E:
    a2 = 0;
    result = PiSwDeviceInterfacesUpdateState(*(unsigned __int64 *)(v_stack_p20), a2, (unsigned int)(0x57706E50ULL), a2 + 56);
    goto loc_0094DF59;
loc_0094E22D:
    if (*(unsigned __int64 *)(v_stack_p20) == 0) goto loc_0094DFD2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20) + 120)) != a1) goto loc_0094DFD2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20) + 4)))) & (2)) == 0) goto loc_0094DFD2;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_p20)) | (64));
    *(unsigned int *)(v_stack_p20 + 8) = (unsigned int)(a1);
    goto loc_0094DFD2;
loc_0094E259:
    if ((((unsigned __int8)(a1)) & (64)) != 0) goto loc_0094DFDB;
    goto loc_0094DFDE;
loc_0094E26C:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(1 + 8)));
    v_rbx = (unsigned int)(((unsigned int)(0xC000000EULL)) & (0xC00000BBULL));
    goto loc_0094DF6A;
loc_0094E27E:
    *(unsigned int *)(result + 16) = 15;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(v_stack_p10 + 56) = result;
    goto loc_0094E02D;
loc_0094E29D:
    goto loc_0094DF48;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwPdoPnPDispatch(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (32);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x8)))) & (16)) != 0) goto loc_0094E202;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x1))) <= 9) goto loc_0094DE88;
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x1)) - (12));
    if (condition_is_equal) goto loc_0094DF19;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_not_equal) goto loc_0094DF95;
    result = PiSwLock(Arg1, Arg2, a3, a4);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) == 0) goto loc_0094E14A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8))) == 0) goto loc_0094E0E1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8))) - (1));
    if (condition_is_not_equal) goto loc_0094E19B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x18) == 0) goto loc_0094DF59;
    result = PnpAllocateMultiSZ(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x18), (uint32_t)(0x7FFFFFFFULL), a3, Arg2 + 56);
    goto loc_0094DF57;
loc_0094DE88:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x18) == 0) goto loc_0094E034;
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x18)) == 0) goto loc_0094E0EF;
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x18)) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0094DFEB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0094E02D;
    if (((uint32_t)(Arg1)) != 1) goto loc_0094DF6A;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8)) != 4) goto loc_0094DF6A;
    result = ExAllocatePool2(256, Arg1 + 15, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    if (result == 0) goto loc_0094E191;
    *(uint32_t *)(result) = 1;
    *(void **)(result + 0x8) = Arg1;
    result = ObfReferenceObject(Arg1, Arg1 + 15, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    *(uint64_t *)(arg2 + 0x38) = result;
    goto loc_0094E02D;
loc_0094DF19:
    result = PiSwLock(Arg1, Arg1 + 15, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) == 0) goto loc_0094E14A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8))) == 0) goto loc_0094E154;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8)))) != 1) goto loc_0094DF59;
loc_0094DF3E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x38) == 0) goto loc_0094DF59;
loc_0094DF48:
    result = PnpAllocatePWSTR(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x38), (uint32_t)(0x7FFFFFFFULL), (uint32_t)(0x57706E50ULL), Arg2 + 56);
loc_0094DF57:
loc_0094DF59:
    result = ExReleaseResourceLite(v_rip + 6540224, (uint32_t)(0x7FFFFFFFULL), (uint32_t)(0x57706E50ULL), Arg2 + 56);
    result = KeLeaveCriticalRegion(v_rip + 6540224, (uint32_t)(0x7FFFFFFFULL), (uint32_t)(0x57706E50ULL), Arg2 + 56);
loc_0094DF6A:
    Arg2 = 0;
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = IofCompleteRequest(0, Arg2, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0094DF95:
    Arg1 = (uint32_t)((0) - (1));
    if (condition_is_equal) goto loc_0094E11E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0094E173;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0094E26C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_0094E15D;
    result = PiSwLock(Arg1, Arg2, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8))) | (4));
    *(uint32_t *)(v_stack_p20 + 0x8) = (uint32_t)(Arg2);
    if ((((uint8_t)(Arg2)) & (8)) != 0) goto loc_0094E22D;
loc_0094DFD2:
    if ((((uint8_t)((uint32_t)((uint32_t)(Arg2)))) & (8)) != 0) goto loc_0094E259;
loc_0094DFDB:
    local_rsi = 0;
loc_0094DFDE:
    result = PiSwProcessRemove(Arg1, 0, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    goto loc_0094E01C;
loc_0094DFEB:
    result = PiSwLock(Arg1, 0, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8))) | (2));
    *(uint32_t *)(v_stack_p20 + 0x8) = (uint32_t)(result);
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0094E20C;
loc_0094E001:
    local_rsi = 0;
loc_0094E004:
    result = PiSwProcessRemove(Arg1, 0, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    if (0 == 0) {
        Arg1 = Arg1;
        result = PiSwDestroyDeviceObject(Arg1, 0, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    }
    result = ExReleaseResourceLite(v_rip + 6540029, 0, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    result = KeLeaveCriticalRegion(v_rip + 6540029, 0, (uint32_t)(0x57706E50ULL), Arg2 + 56);
loc_0094E02D:
    local_rbx = 0;
    goto loc_0094DF6A;
loc_0094E034:
    result = PiSwLock(v_rip + 6540029, 0, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    if ((*(uint64_t *)(v_stack_p20)) == 0) goto loc_0094E14A;
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x14) = 1;
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x18) = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x28) = v_xmm0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x4))) | (576));
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x4) = (uint32_t)(Arg1);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20) + 0x40))) << (4));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) & (16));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x4) = (uint32_t)(Arg2);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20) + 0x40))) & (2));
    Arg1 = (uint32_t)((Arg1) << (6));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg2)));
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x4) = (uint32_t)(Arg1);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20) + 0x40))) & (4));
    Arg2 = (uint32_t)((Arg2) << (15));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(Arg1)));
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x4) = (uint32_t)(Arg2);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20) + 0x40))) << (5));
    Arg1 = (uint32_t)(~(Arg1));
    Arg1 = (uint32_t)((Arg1) & (256));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg2)));
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x4) = (uint32_t)(Arg1);
loc_0094E0DA:
    local_rbx = 0;
    goto loc_0094DF59;
loc_0094E0E1:
    goto loc_0094DF48;
loc_0094E0EF:
    result = PiSwLock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x8), 200, *(uint64_t *)(local_rsi + 0x8), Arg2 + 56);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8))))) != 0) goto loc_0094E0DA;
    result = PiSwDeviceInterfacesUpdateState(*(uint64_t *)(v_stack_p20), 1, *(uint64_t *)(local_rsi + 0x8), Arg2 + 56);
    if (sign_flag) goto loc_0094E21E;
    goto loc_0094DF59;
loc_0094E11E:
    result = PiSwLock(*(uint64_t *)(v_stack_p20), 1, *(uint64_t *)(local_rsi + 0x8), Arg2 + 56);
    if (*(uint64_t *)(v_stack_p20) == 0) goto loc_0094E14A;
    result = (*(uint64_t *)(v_stack_p10 + 0x38)) & (-3);
    Arg2 = (*(uint64_t *)(v_stack_p10 + 0x38)) | (2);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20) + 0x40)))) & (4)) == 0) { Arg2 = result; }
    *(void **)(v_stack_p10 + 0x38) = Arg2;
    goto loc_0094E0DA;
loc_0094E14A:
    goto loc_0094DF59;
loc_0094E154:
    goto loc_0094DF3E;
loc_0094E15D:
    if (((uint32_t)(*(uint64_t *)(arg2 + 0x30))) != 2) goto loc_0094DF6A;
    result = PiSwCompleteCreate(Arg1, Arg2, *(uint64_t *)(local_rsi + 0x8), Arg2 + 56);
    goto loc_0094E02D;
loc_0094E173:
    result = ExAllocatePool2(256, 24, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    if (result != 0) goto loc_0094E27E;
loc_0094E191:
    goto loc_0094DF6A;
loc_0094E19B:
    Arg1 = (uint32_t)((256) - (1));
    if (condition_is_not_equal) goto loc_0094E1B1;
    result = PiSwDeviceMakeCompatibleIds(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)), v_stack_p10 + 56, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    goto loc_0094DF57;
loc_0094E1B1:
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x40))) - (1));
    if (condition_is_equal) goto loc_0094E29D;
    if (((uint32_t)(Arg1)) != 2) goto loc_0094DF59;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x28)) == 0) goto loc_0094DF59;
    result = ExAllocatePool2(256, Arg1 + 76, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    *(uint64_t *)(v_stack_p10 + 0x38) = result;
    result = PnpStringFromGuid(*(uint64_t *)(*(uint64_t *)(v_stack_p20) + 0x28), result, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    goto loc_0094DF57;
loc_0094E202:
    goto loc_0094DF6A;
loc_0094E20C:
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_0094E001;
    goto loc_0094E004;
loc_0094E21E:
    Arg2 = 0;
    result = PiSwDeviceInterfacesUpdateState(*(uint64_t *)(v_stack_p20), Arg2, (uint32_t)(0x57706E50ULL), Arg2 + 56);
    goto loc_0094DF59;
loc_0094E22D:
    if (*(uint64_t *)(v_stack_p20) == 0) goto loc_0094DFD2;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20) + 0x78)) != Arg1) goto loc_0094DFD2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20) + 0x4)))) & (2)) == 0) goto loc_0094DFD2;
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_p20)) | (64));
    *(uint32_t *)(v_stack_p20 + 0x8) = (uint32_t)(Arg1);
    goto loc_0094DFD2;
loc_0094E259:
    if ((((uint8_t)(Arg1)) & (64)) != 0) goto loc_0094DFDB;
    goto loc_0094DFDE;
loc_0094E26C:
    result = (uint8_t)(-(*(uint8_t *)(1 + 0x8)));
    local_rbx = (uint32_t)(((uint32_t)(0xC000000EULL)) & (0xC00000BBULL));
    goto loc_0094DF6A;
loc_0094E27E:
    *(uint32_t *)(result + 0x10) = 15;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(v_stack_p10 + 0x38) = result;
    goto loc_0094E02D;
loc_0094E29D:
    goto loc_0094DF48;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x38` | `64` | `W` |
| `Arg2` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094DDF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
