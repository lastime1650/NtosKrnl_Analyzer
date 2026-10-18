# HaliQuerySystemInformation

- RVA: `0x00B7A990`–`0x00B7AC8F` (길이 `767` bytes)
- VA: `0x0000000140B7A990`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B8DF4`
- 디코드: `205`개 명령, `767/767` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B7A9CE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B7AA1E` → [HalpTimerQueryClockSourceType](../../text/4B/HalpTimerQueryClockSourceType_function_004BB068.md) (function, `0x004BB068`)
- `0x00B7AA31` → [RtlCopyDeviceMemory](../../text/52/RtlCopyDeviceMemory_function_00522BFC.md) (function, `0x00522BFC`)
- `0x00B7AA3F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00B7AAA9` → [HalpQueryProfileInformation](../../page/AD/HalpQueryProfileInformation_function_00AD621C.md) (function, `0x00AD621C`)
- `0x00B7AB20` → [HalpDpQueryMaxHotPlugMemoryAddress](../../text/54/HalpDpQueryMaxHotPlugMemoryAddress_function_00545E28.md) (function, `0x00545E28`)
- `0x00B7AB2B` → [HalpGetMcaLog](../../page/70/HalpGetMcaLog_function_007072A8.md) (function, `0x007072A8`)
- `0x00B7AB73` → [HalpQueryChannelTopologyInformation](../../init/C2/HalpQueryChannelTopologyInformation_function_00C256F8.md) (function, `0x00C256F8`)
- `0x00B7AB85` → [HalpGetProcessorBrandString](../../page/70/HalpGetProcessorBrandString_function_0070C050.md) (function, `0x0070C050`)
- `0x00B7AB97` → [HalpQueryDebuggerInformation](../../pagekd/B8/HalpQueryDebuggerInformation_function_00B85B70.md) (function, `0x00B85B70`)
- `0x00B7AC0A` → [HalpGetHibernateResumePc](../../text/56/HalpGetHibernateResumePc_function_0056B3E4.md) (function, `0x0056B3E4`)
- `0x00B7AC21` → [HalpQueryPerDeviceMsiLimitInformation](../../page/70/HalpQueryPerDeviceMsiLimitInformation_function_0070786C.md) (function, `0x0070786C`)
- `0x00B7AC52` → [HalpDmaGetRemappingInformation](../../page/70/HalpDmaGetRemappingInformation_function_00709800.md) (function, `0x00709800`)
- `0x00B7AC80` → [HalpHvQueryHyperlaunchEntrypoint](../../text/55/HalpHvQueryHyperlaunchEntrypoint_function_0055A22C.md) (function, `0x0055A22C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B7A9A9` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00B7A9CE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B7AA1E` → [HalpTimerQueryClockSourceType](../../text/4B/HalpTimerQueryClockSourceType_function_004BB068.md) (`PAGELK` → `.text`)
  - `0x00B7AA31` → [RtlCopyDeviceMemory](../../text/52/RtlCopyDeviceMemory_function_00522BFC.md) (`PAGELK` → `.text`)
  - `0x00B7AA3F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
  - `0x00B7AAA9` → [HalpQueryProfileInformation](../../page/AD/HalpQueryProfileInformation_function_00AD621C.md) (`PAGELK` → `PAGE`)
  - `0x00B7AB20` → [HalpDpQueryMaxHotPlugMemoryAddress](../../text/54/HalpDpQueryMaxHotPlugMemoryAddress_function_00545E28.md) (`PAGELK` → `.text`)
  - `0x00B7AB2B` → [HalpGetMcaLog](../../page/70/HalpGetMcaLog_function_007072A8.md) (`PAGELK` → `PAGE`)
  - `0x00B7AB73` → [HalpQueryChannelTopologyInformation](../../init/C2/HalpQueryChannelTopologyInformation_function_00C256F8.md) (`PAGELK` → `INIT`)
  - `0x00B7AB85` → [HalpGetProcessorBrandString](../../page/70/HalpGetProcessorBrandString_function_0070C050.md) (`PAGELK` → `PAGE`)
  - `0x00B7AB97` → [HalpQueryDebuggerInformation](../../pagekd/B8/HalpQueryDebuggerInformation_function_00B85B70.md) (`PAGELK` → `PAGEKD`)
  - `0x00B7AC0A` → [HalpGetHibernateResumePc](../../text/56/HalpGetHibernateResumePc_function_0056B3E4.md) (`PAGELK` → `.text`)
  - `0x00B7AC21` → [HalpQueryPerDeviceMsiLimitInformation](../../page/70/HalpQueryPerDeviceMsiLimitInformation_function_0070786C.md) (`PAGELK` → `PAGE`)
  - `0x00B7AC52` → [HalpDmaGetRemappingInformation](../../page/70/HalpDmaGetRemappingInformation_function_00709800.md) (`PAGELK` → `PAGE`)
  - `0x00B7AC80` → [HalpHvQueryHyperlaunchEntrypoint](../../text/55/HalpHvQueryHyperlaunchEntrypoint_function_0055A22C.md) (`PAGELK` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **20**
  - `0x00B7AAEE` → [sub_00B80AC2 + 0x6C](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AAF7` → [sub_00B80AC2 + 0x37](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AB00` → [sub_00B80AC2 + 0x19](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AB0E` → [sub_00B80AC2](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AB26` → [sub_00B80AC2 + 0x22F](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AB38` → [sub_00B80AC2 + 0x109](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AB41` → [sub_00B80AC2 + 0xE7](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AB4A` → [sub_00B80AC2 + 0xC5](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AB53` → [sub_00B80AC2 + 0x97](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AB5C` → [sub_00B80AC2 + 0x84](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7ABAC` → [sub_00B80AC2 + 0x221](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7ABB5` → [sub_00B80AC2 + 0x1E3](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7ABBE` → [sub_00B80AC2 + 0x1D0](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7ABC7` → [sub_00B80AC2 + 0x1AA](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7ABD0` → [sub_00B80AC2 + 0x197](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7ABD9` → [sub_00B80AC2 + 0x16E](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7ABE2` → [sub_00B80AC2 + 0x12B](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AC10` → [sub_00B80AC2 + 0x22F](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AC45` → [sub_00B80AC2 + 0xA7](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)
  - `0x00B7AC69` → [sub_00B80AC2 + 0x157](../B8/Unknown_function_00B80AC2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B7A990  40 55                           push rbp
00B7A992  53                              push rbx
00B7A993  56                              push rsi
00B7A994  57                              push rdi
00B7A995  41 54                           push r12
00B7A997  41 55                           push r13
00B7A999  41 56                           push r14
00B7A99B  41 57                           push r15
00B7A99D  48 8D 6C 24 C8                  lea rbp, [rsp - 0x38]
00B7A9A2  48 81 EC 38 01 00 00            sub rsp, 0x138
00B7A9A9  48 8B 05 90 FD 28 00            mov rax, qword ptr [rip + 0x28fd90]
00B7A9B0  48 33 C4                        xor rax, rsp
00B7A9B3  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00B7A9B7  4D 8B E0                        mov r12, r8
00B7A9BA  8B F2                           mov esi, edx
00B7A9BC  8B F9                           mov edi, ecx
00B7A9BE  33 D2                           xor edx, edx
00B7A9C0  41 B8 00 01 00 00               mov r8d, 0x100
00B7A9C6  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00B7A9CB  4D 8B F1                        mov r14, r9
00B7A9CE  E8 6D C2 B4 FF                  call 0x1406c6c40
00B7A9D3  45 33 ED                        xor r13d, r13d
00B7A9D6  41 8B DD                        mov ebx, r13d
00B7A9D9  4D 85 F6                        test r14, r14
00B7A9DC  74 03                           je 0x140b7a9e1
00B7A9DE  45 89 2E                        mov dword ptr [r14], r13d
00B7A9E1  83 FF 21                        cmp edi, 0x21
00B7A9E4  7F 73                           jg 0x140b7aa59
00B7A9E6  0F 84 A3 01 00 00               je 0x140b7ab8f
00B7A9EC  83 FF 14                        cmp edi, 0x14
00B7A9EF  0F 8E C7 00 00 00               jle 0x140b7aabc
00B7A9F5  83 EF 17                        sub edi, 0x17
00B7A9F8  0F 84 7F 01 00 00               je 0x140b7ab7d
00B7A9FE  83 EF 02                        sub edi, 2
00B7AA01  0F 85 2E 01 00 00               jne 0x140b7ab35
00B7AA07  BF 0C 00 00 00                  mov edi, 0xc
00B7AA0C  3B F7                           cmp esi, edi
00B7AA0E  0F 82 9E 00 00 00               jb 0x140b7aab2
00B7AA14  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00B7AA19  4C 8D 7C 24 20                  lea r15, [rsp + 0x20]
00B7AA1E  E8 45 06 94 FF                  call 0x1404bb068
00B7AA23  8B D8                           mov ebx, eax
00B7AA25  44 8B C7                        mov r8d, edi
00B7AA28  49 8B D7                        mov rdx, r15
00B7AA2B  49 8B CC                        mov rcx, r12
00B7AA2E  41 89 3E                        mov dword ptr [r14], edi
00B7AA31  E8 C6 81 9A FF                  call 0x140522bfc
00B7AA36  8B C3                           mov eax, ebx
00B7AA38  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00B7AA3C  48 33 CC                        xor rcx, rsp
00B7AA3F  E8 FC 1B B3 FF                  call 0x1406ac640
00B7AA44  48 81 C4 38 01 00 00            add rsp, 0x138
00B7AA4B  41 5F                           pop r15
00B7AA4D  41 5E                           pop r14
00B7AA4F  41 5D                           pop r13
00B7AA51  41 5C                           pop r12
00B7AA53  5F                              pop rdi
00B7AA54  5E                              pop rsi
00B7AA55  5B                              pop rbx
00B7AA56  5D                              pop rbp
00B7AA57  C3                              ret
00B7AA58  CC                              int3
00B7AA59  83 FF 2D                        cmp edi, 0x2d
00B7AA5C  0F 8E 3F 01 00 00               jle 0x140b7aba1
00B7AA62  8B CF                           mov ecx, edi
00B7AA64  83 E9 2E                        sub ecx, 0x2e
00B7AA67  0F 84 01 02 00 00               je 0x140b7ac6e
00B7AA6D  83 E9 01                        sub ecx, 1
00B7AA70  0F 84 E6 01 00 00               je 0x140b7ac5c
00B7AA76  83 E9 01                        sub ecx, 1
00B7AA79  0F 84 CB 01 00 00               je 0x140b7ac4a
00B7AA7F  83 E9 02                        sub ecx, 2
00B7AA82  0F 84 B4 01 00 00               je 0x140b7ac3c
00B7AA88  83 E9 01                        sub ecx, 1
00B7AA8B  0F 84 84 01 00 00               je 0x140b7ac15
00B7AA91  83 E9 01                        sub ecx, 1
00B7AA94  74 09                           je 0x140b7aa9f
00B7AA96  83 E9 01                        sub ecx, 1
00B7AA99  0F 85 57 01 00 00               jne 0x140b7abf6
00B7AA9F  4D 8B CE                        mov r9, r14
00B7AAA2  4D 8B C4                        mov r8, r12
00B7AAA5  8B D6                           mov edx, esi
00B7AAA7  8B CF                           mov ecx, edi
00B7AAA9  E8 6E B7 F5 FF                  call 0x140ad621c
00B7AAAE  8B D8                           mov ebx, eax
00B7AAB0  EB 84                           jmp 0x140b7aa36
00B7AAB2  BB 04 00 00 C0                  mov ebx, 0xc0000004
00B7AAB7  E9 7A FF FF FF                  jmp 0x140b7aa36
00B7AABC  74 E1                           je 0x140b7aa9f
00B7AABE  8B CF                           mov ecx, edi
00B7AAC0  83 E9 01                        sub ecx, 1
00B7AAC3  74 DA                           je 0x140b7aa9f
00B7AAC5  83 E9 06                        sub ecx, 6
00B7AAC8  74 61                           je 0x140b7ab2b
00B7AACA  83 E9 01                        sub ecx, 1
00B7AACD  75 1C                           jne 0x140b7aaeb
00B7AACF  BB 48 01 00 C0                  mov ebx, 0xc0000148
00B7AAD4  E9 5D FF FF FF                  jmp 0x140b7aa36
00B7AAD9  85 FF                           test edi, edi
00B7AADB  0F 84 55 FF FF FF               je 0x140b7aa36
00B7AAE1  3B F7                           cmp esi, edi
00B7AAE3  0F 42 FE                        cmovb edi, esi
00B7AAE6  E9 3A FF FF FF                  jmp 0x140b7aa25
00B7AAEB  83 E9 01                        sub ecx, 1
00B7AAEE  0F 84 3A 60 00 00               je 0x140b80b2e
00B7AAF4  83 E9 02                        sub ecx, 2
00B7AAF7  0F 84 FC 5F 00 00               je 0x140b80af9
00B7AAFD  83 E9 01                        sub ecx, 1
00B7AB00  0F 84 D5 5F 00 00               je 0x140b80adb
00B7AB06  83 E9 01                        sub ecx, 1
00B7AB09  74 20                           je 0x140b7ab2b
00B7AB0B  83 E9 03                        sub ecx, 3
00B7AB0E  0F 84 AE 5F 00 00               je 0x140b80ac2
00B7AB14  83 F9 01                        cmp ecx, 1
00B7AB17  75 B6                           jne 0x140b7aacf
00B7AB19  8D 79 07                        lea edi, [rcx + 7]
00B7AB1C  3B F7                           cmp esi, edi
00B7AB1E  75 92                           jne 0x140b7aab2
00B7AB20  E8 03 B3 9C FF                  call 0x140545e28
00B7AB25  90                              nop
00B7AB26  E9 C6 61 00 00                  jmp 0x140b80cf1
00B7AB2B  E8 78 C7 B8 FF                  call 0x1407072a8
00B7AB30  E9 79 FF FF FF                  jmp 0x140b7aaae
00B7AB35  83 EF 01                        sub edi, 1
00B7AB38  0F 84 8D 60 00 00               je 0x140b80bcb
00B7AB3E  83 EF 01                        sub edi, 1
00B7AB41  0F 84 62 60 00 00               je 0x140b80ba9
00B7AB47  83 EF 01                        sub edi, 1
00B7AB4A  0F 84 37 60 00 00               je 0x140b80b87
00B7AB50  83 EF 01                        sub edi, 1
00B7AB53  0F 84 00 60 00 00               je 0x140b80b59
00B7AB59  83 EF 01                        sub edi, 1
00B7AB5C  0F 84 E4 5F 00 00               je 0x140b80b46
00B7AB62  83 FF 01                        cmp edi, 1
00B7AB65  0F 85 64 FF FF FF               jne 0x140b7aacf
00B7AB6B  4D 8B C6                        mov r8, r14
00B7AB6E  8B D6                           mov edx, esi
00B7AB70  49 8B CC                        mov rcx, r12
00B7AB73  E8 80 AB 0A 00                  call 0x140c256f8
00B7AB78  E9 31 FF FF FF                  jmp 0x140b7aaae
00B7AB7D  4D 8B C6                        mov r8, r14
00B7AB80  49 8B D4                        mov rdx, r12
00B7AB83  8B CE                           mov ecx, esi
00B7AB85  E8 C6 14 B9 FF                  call 0x14070c050
00B7AB8A  E9 1F FF FF FF                  jmp 0x140b7aaae
00B7AB8F  4D 8B C6                        mov r8, r14
00B7AB92  8B D6                           mov edx, esi
00B7AB94  49 8B CC                        mov rcx, r12
00B7AB97  E8 D4 AF 00 00                  call 0x140b85b70
00B7AB9C  E9 0D FF FF FF                  jmp 0x140b7aaae
00B7ABA1  0F 84 F8 FE FF FF               je 0x140b7aa9f
00B7ABA7  8B CF                           mov ecx, edi
00B7ABA9  83 E9 22                        sub ecx, 0x22
00B7ABAC  0F 84 31 61 00 00               je 0x140b80ce3
00B7ABB2  83 E9 01                        sub ecx, 1
00B7ABB5  0F 84 EA 60 00 00               je 0x140b80ca5
00B7ABBB  83 E9 01                        sub ecx, 1
00B7ABBE  0F 84 CE 60 00 00               je 0x140b80c92
00B7ABC4  83 E9 01                        sub ecx, 1
00B7ABC7  0F 84 9F 60 00 00               je 0x140b80c6c
00B7ABCD  83 E9 02                        sub ecx, 2
00B7ABD0  0F 84 83 60 00 00               je 0x140b80c59
00B7ABD6  83 E9 01                        sub ecx, 1
00B7ABD9  0F 84 51 60 00 00               je 0x140b80c30
00B7ABDF  83 E9 03                        sub ecx, 3
00B7ABE2  0F 84 05 60 00 00               je 0x140b80bed
00B7ABE8  83 F9 01                        cmp ecx, 1
00B7ABEB  0F 84 AE FE FF FF               je 0x140b7aa9f
00B7ABF1  E9 D9 FE FF FF                  jmp 0x140b7aacf
00B7ABF6  83 F9 03                        cmp ecx, 3
00B7ABF9  0F 85 D0 FE FF FF               jne 0x140b7aacf
00B7ABFF  8D 79 05                        lea edi, [rcx + 5]
00B7AC02  3B F7                           cmp esi, edi
00B7AC04  0F 85 A8 FE FF FF               jne 0x140b7aab2
00B7AC0A  E8 D5 07 9F FF                  call 0x14056b3e4
00B7AC0F  90                              nop
00B7AC10  E9 DC 60 00 00                  jmp 0x140b80cf1
00B7AC15  83 FE 02                        cmp esi, 2
00B7AC18  0F 82 94 FE FF FF               jb 0x140b7aab2
00B7AC1E  49 8B CC                        mov rcx, r12
00B7AC21  E8 46 CC B8 FF                  call 0x14070786c
00B7AC26  8B D8                           mov ebx, eax
00B7AC28  85 C0                           test eax, eax
00B7AC2A  0F 88 06 FE FF FF               js 0x140b7aa36
00B7AC30  41 C7 06 02 00 00 00            mov dword ptr [r14], 2
00B7AC37  E9 FA FD FF FF                  jmp 0x140b7aa36
00B7AC3C  83 FE 18                        cmp esi, 0x18
00B7AC3F  0F 85 6D FE FF FF               jne 0x140b7aab2
00B7AC45  E9 1F 5F 00 00                  jmp 0x140b80b69
00B7AC4A  4D 8B C4                        mov r8, r12
00B7AC4D  49 8B D6                        mov rdx, r14
00B7AC50  8B CE                           mov ecx, esi
00B7AC52  E8 A9 EB B8 FF                  call 0x140709800
00B7AC57  E9 52 FE FF FF                  jmp 0x140b7aaae
00B7AC5C  BF 04 00 00 00                  mov edi, 4
00B7AC61  3B F7                           cmp esi, edi
00B7AC63  0F 82 49 FE FF FF               jb 0x140b7aab2
00B7AC69  E9 AB 5F 00 00                  jmp 0x140b80c19
00B7AC6E  BF 08 00 00 00                  mov edi, 8
00B7AC73  3B F7                           cmp esi, edi
00B7AC75  0F 85 37 FE FF FF               jne 0x140b7aab2
00B7AC7B  4C 8D 7C 24 20                  lea r15, [rsp + 0x20]
00B7AC80  E8 A7 F5 9D FF                  call 0x14055a22c
00B7AC85  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B7AC8A  E9 96 FD FF FF                  jmp 0x140b7aa25
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HaliQuerySystemInformation(int a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (312);
    result = (*(unsigned __int64 *)(v_rip + 2686352)) ^ (v_rsp);
    v_stack_m58 = result;
    a2 = 0;
    result = memset(v_stack_m158, a2, 256, a4);
    v_r13 = 0;
    if (a4 != 0) {
        *(unsigned int *)(a4) = 0;
    }
    if (((unsigned int)((unsigned int)(a1))) > 33) goto loc_00B7AA59;
    if (((unsigned int)((unsigned int)(a1))) == 33) goto loc_00B7AB8F;
    if (((unsigned int)((unsigned int)(a1))) <= 20) goto loc_00B7AABC;
    v_rdi = (unsigned int)(((unsigned int)(a1)) - (23));
    if (condition_is_equal) goto loc_00B7AB7D;
    v_rdi = (unsigned int)((v_rdi) - (2));
    if (condition_is_not_equal) goto loc_00B7AB35;
    if (((unsigned int)((unsigned int)(a2))) < 12) goto loc_00B7AAB2;
    result = HalpTimerQueryClockSourceType(v_stack_m158, a2, 256, a4);
loc_00B7AA25:
    *(unsigned int *)(a4) = 12;
    result = RtlCopyDeviceMemory(a3, v_stack_m158, 12, a4);
loc_00B7AA36:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m158, 12, a4);
    v_rsp = (v_rsp) + (312);
    return result;
loc_00B7AA59:
    if (12 <= 45) goto loc_00B7ABA1;
    a1 = (unsigned int)((12) - (46));
    if (condition_is_equal) goto loc_00B7AC6E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00B7AC5C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00B7AC4A;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00B7AC3C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00B7AC15;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00B7AA9F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00B7ABF6;
loc_00B7AA9F:
    result = HalpQueryProfileInformation(12, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
loc_00B7AAAE:
    goto loc_00B7AA36;
loc_00B7AAB2:
    goto loc_00B7AA36;
loc_00B7AABC:
    if (condition_is_equal) goto loc_00B7AA9F;
    a1 = (unsigned int)((12) - (1));
    if (condition_is_equal) goto loc_00B7AA9F;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00B7AB2B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00B7AAEB;
loc_00B7AACF:
    goto loc_00B7AA36;
loc_00B7AAEB:
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (2));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00B7AB2B;
    a1 = (unsigned int)((a1) - (3));
    if (a1 != 1) goto loc_00B7AACF;
    if (((unsigned int)((unsigned int)(a2))) != ((unsigned int)(a1 + 7))) goto loc_00B7AAB2;
    result = HalpDpQueryMaxHotPlugMemoryAddress(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
loc_00B7AB2B:
    result = HalpGetMcaLog(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    goto loc_00B7AAAE;
loc_00B7AB35:
    v_rdi = (unsigned int)((a1 + 7) - (1));
    v_rdi = (unsigned int)((v_rdi) - (1));
    v_rdi = (unsigned int)((v_rdi) - (1));
    v_rdi = (unsigned int)((v_rdi) - (1));
    v_rdi = (unsigned int)((v_rdi) - (1));
    if (((unsigned int)(v_rdi)) != 1) goto loc_00B7AACF;
    result = HalpQueryChannelTopologyInformation(a3, (unsigned int)((unsigned int)((unsigned int)(a2))), a4, a4);
    goto loc_00B7AAAE;
loc_00B7AB7D:
    result = HalpGetProcessorBrandString((unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4, a4);
    goto loc_00B7AAAE;
loc_00B7AB8F:
    result = HalpQueryDebuggerInformation(a3, (unsigned int)((unsigned int)((unsigned int)(a2))), a4, a4);
    goto loc_00B7AAAE;
loc_00B7ABA1:
    if (((unsigned int)(v_rdi)) == 1) goto loc_00B7AA9F;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (34));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (2));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (3));
    if (a1 == 1) goto loc_00B7AA9F;
    goto loc_00B7AACF;
loc_00B7ABF6:
    if (a1 != 3) goto loc_00B7AACF;
    if (((unsigned int)((unsigned int)(a2))) != ((unsigned int)(a1 + 5))) goto loc_00B7AAB2;
    result = HalpGetHibernateResumePc(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a4, a4);
loc_00B7AC15:
    if (((unsigned int)((unsigned int)(a2))) < 2) goto loc_00B7AAB2;
    result = HalpQueryPerDeviceMsiLimitInformation(a3, (unsigned int)((unsigned int)((unsigned int)(a2))), a4, a4);
    if (sign_flag) goto loc_00B7AA36;
    *(unsigned int *)(a4) = 2;
    goto loc_00B7AA36;
loc_00B7AC3C:
    if (((unsigned int)((unsigned int)(a2))) != 24) goto loc_00B7AAB2;
loc_00B7AC4A:
    result = HalpDmaGetRemappingInformation((unsigned int)((unsigned int)((unsigned int)(a2))), a4, a3, a4);
    goto loc_00B7AAAE;
loc_00B7AC5C:
    if (((unsigned int)((unsigned int)(a2))) < 4) goto loc_00B7AAB2;
loc_00B7AC6E:
    if (((unsigned int)((unsigned int)(a2))) != 8) goto loc_00B7AAB2;
    result = HalpHvQueryHyperlaunchEntrypoint((unsigned int)((unsigned int)((unsigned int)(a2))), a4, a3, a4);
    v_stack_p20 = result;
    goto loc_00B7AA25;
}
```

## 5. (Beta) C Style

```c
int64_t HaliQuerySystemInformation(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m158;
    uint64_t v_stack_m58;
    uint64_t v_stack_m78;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (312);
    result = (*(uint64_t *)(v_rip + 0x28FD90)) ^ (local_rsp);
    v_stack_m58 = result;
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, 256, Arg4);
    local_r13 = 0;
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = 0;
    }
    if (((uint32_t)((uint32_t)(Arg1))) > 33) goto loc_00B7AA59;
    if (((uint32_t)((uint32_t)(Arg1))) == 33) goto loc_00B7AB8F;
    if (((uint32_t)((uint32_t)(Arg1))) <= 20) goto loc_00B7AABC;
    local_rdi = (uint32_t)(((uint32_t)(Arg1)) - (23));
    if (condition_is_equal) goto loc_00B7AB7D;
    local_rdi = (uint32_t)((local_rdi) - (2));
    if (condition_is_not_equal) goto loc_00B7AB35;
    if (((uint32_t)((uint32_t)(Arg2))) < 12) goto loc_00B7AAB2;
    result = HalpTimerQueryClockSourceType(v_stack_m158, Arg2, 256, Arg4);
loc_00B7AA25:
    *(uint32_t *)(Arg4) = 12;
    result = RtlCopyDeviceMemory(Arg3, v_stack_m158, 12, Arg4);
loc_00B7AA36:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m158, 12, Arg4);
    local_rsp = (local_rsp) + (312);
    return result;
loc_00B7AA59:
    if (12 <= 45) goto loc_00B7ABA1;
    Arg1 = (uint32_t)((12) - (46));
    if (condition_is_equal) goto loc_00B7AC6E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00B7AC5C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00B7AC4A;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00B7AC3C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00B7AC15;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00B7AA9F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00B7ABF6;
loc_00B7AA9F:
    result = HalpQueryProfileInformation(12, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
loc_00B7AAAE:
    goto loc_00B7AA36;
loc_00B7AAB2:
    goto loc_00B7AA36;
loc_00B7AABC:
    if (condition_is_equal) goto loc_00B7AA9F;
    Arg1 = (uint32_t)((12) - (1));
    if (condition_is_equal) goto loc_00B7AA9F;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00B7AB2B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00B7AAEB;
loc_00B7AACF:
    goto loc_00B7AA36;
loc_00B7AAEB:
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (2));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00B7AB2B;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (Arg1 != 1) goto loc_00B7AACF;
    if (((uint32_t)((uint32_t)(Arg2))) != ((uint32_t)(Arg1 + 7))) goto loc_00B7AAB2;
    result = HalpDpQueryMaxHotPlugMemoryAddress(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
loc_00B7AB2B:
    result = HalpGetMcaLog(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    goto loc_00B7AAAE;
loc_00B7AB35:
    local_rdi = (uint32_t)((Arg1 + 7) - (1));
    local_rdi = (uint32_t)((local_rdi) - (1));
    local_rdi = (uint32_t)((local_rdi) - (1));
    local_rdi = (uint32_t)((local_rdi) - (1));
    local_rdi = (uint32_t)((local_rdi) - (1));
    if (((uint32_t)(local_rdi)) != 1) goto loc_00B7AACF;
    result = HalpQueryChannelTopologyInformation(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4, Arg4);
    goto loc_00B7AAAE;
loc_00B7AB7D:
    result = HalpGetProcessorBrandString((uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4, Arg4);
    goto loc_00B7AAAE;
loc_00B7AB8F:
    result = HalpQueryDebuggerInformation(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4, Arg4);
    goto loc_00B7AAAE;
loc_00B7ABA1:
    if (((uint32_t)(local_rdi)) == 1) goto loc_00B7AA9F;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (34));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (2));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (3));
    if (Arg1 == 1) goto loc_00B7AA9F;
    goto loc_00B7AACF;
loc_00B7ABF6:
    if (Arg1 != 3) goto loc_00B7AACF;
    if (((uint32_t)((uint32_t)(Arg2))) != ((uint32_t)(Arg1 + 5))) goto loc_00B7AAB2;
    result = HalpGetHibernateResumePc(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4, Arg4);
loc_00B7AC15:
    if (((uint32_t)((uint32_t)(Arg2))) < 2) goto loc_00B7AAB2;
    result = HalpQueryPerDeviceMsiLimitInformation(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4, Arg4);
    if (sign_flag) goto loc_00B7AA36;
    *(uint32_t *)(Arg4) = 2;
    goto loc_00B7AA36;
loc_00B7AC3C:
    if (((uint32_t)((uint32_t)(Arg2))) != 24) goto loc_00B7AAB2;
loc_00B7AC4A:
    result = HalpDmaGetRemappingInformation((uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4, Arg3, Arg4);
    goto loc_00B7AAAE;
loc_00B7AC5C:
    if (((uint32_t)((uint32_t)(Arg2))) < 4) goto loc_00B7AAB2;
loc_00B7AC6E:
    if (((uint32_t)((uint32_t)(Arg2))) != 8) goto loc_00B7AAB2;
    result = HalpHvQueryHyperlaunchEntrypoint((uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4, Arg3, Arg4);
    v_stack_p20 = result;
    goto loc_00B7AA25;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B7A990&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
