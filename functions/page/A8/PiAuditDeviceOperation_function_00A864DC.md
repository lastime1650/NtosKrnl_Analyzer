# PiAuditDeviceOperation

- RVA: `0x00A864DC`–`0x00A86B97` (길이 `1,723` bytes)
- VA: `0x0000000140A864DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B7D20`
- 디코드: `415`개 명령, `1,723/1,723` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00A86599` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A865DB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A86631` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A86673` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A866C9` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A86712` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A86768` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A867E7` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A86810` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A86866` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A8688F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A868A7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A868FF` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A86912` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86925` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A86981` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86991` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A869CD` → [SeAuditPlugAndPlay](SeAuditPlugAndPlay_function_00A86BA0.md) (function, `0x00A86BA0`)
- `0x00A869F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86A0A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86A24` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86A3B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86AA1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86AB3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86ADE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86B08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86B1A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86B4E` → [PnpFindAlternateStringData](../A2/PnpFindAlternateStringData_function_00A2D4A8.md) (function, `0x00A2D4A8`)
- `0x00A86B6F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86B7E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A86B8D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiAuditDeviceEnableDisableAction](../74/PiAuditDeviceEnableDisableAction_function_00740A84.md) at `0x00740AA7`
- [PiAuditDeviceEnableDisableRequest](../74/PiAuditDeviceEnableDisableRequest_function_00740AB8.md) at `0x00740AE8`
- [PiAuditDeviceStart](../8F/PiAuditDeviceStart_function_008FCEB4.md) at `0x008FCF48`
- [sub_00B1EBE0](../B1/Unknown_function_00B1EBE0.md) at `0x00B1EEF6`

### Static image references
- `0x00A864FF` → RVA `0x00E0A740` (`.data`; read)
- `0x00A865F4` → RVA `0x00E66398` (`.data`; read)
- `0x00A86620` → RVA `0x00011550` (`.rdata`; read)
- `0x00A866B8` → RVA `0x00011670` (`.rdata`; read)
- `0x00A86757` → RVA `0x0001BD98` (`.rdata`; read)
- `0x00A867D3` → RVA `0x00011688` (`.rdata`; read)
- `0x00A86855` → RVA `0x0001BDB0` (`.rdata`; read)
- `0x00A868DF` → RVA `0x00014080` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x00A86599` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A865DB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A86673` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A86712` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A86810` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8688F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A868A7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A86912` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86925` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A86981` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86991` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A869F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86A0A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86A24` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86A3B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86AA1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86AB3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86ADE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86B08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86B1A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86B6F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86B7E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A86B8D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00A866D8` → [sub_00B44AC4](../B4/Unknown_function_00B44AC4.md) (`tail-transfer`)
  - `0x00A86B3A` → [sub_00B44AC4 + 0x76](../B4/Unknown_function_00B44AC4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A864DC  48 8B C4                        mov rax, rsp
00A864DF  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00A864E3  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00A864E7  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00A864EB  55                              push rbp
00A864EC  41 54                           push r12
00A864EE  41 55                           push r13
00A864F0  41 56                           push r14
00A864F2  41 57                           push r15
00A864F4  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00A864F8  48 81 EC 00 01 00 00            sub rsp, 0x100
00A864FF  48 8B 05 3A 42 38 00            mov rax, qword ptr [rip + 0x38423a]
00A86506  48 33 C4                        xor rax, rsp
00A86509  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
00A8650D  33 FF                           xor edi, edi
00A8650F  44 88 45 A7                     mov byte ptr [rbp - 0x59], r8b
00A86513  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
00A86517  0F 57 C0                        xorps xmm0, xmm0
00A8651A  89 7D A3                        mov dword ptr [rbp - 0x5d], edi
00A8651D  0F 57 C9                        xorps xmm1, xmm1
00A86520  48 89 7D B7                     mov qword ptr [rbp - 0x49], rdi
00A86524  48 8B D9                        mov rbx, rcx
00A86527  89 7D AF                        mov dword ptr [rbp - 0x51], edi
00A8652A  44 8B EF                        mov r13d, edi
00A8652D  89 7D 9B                        mov dword ptr [rbp - 0x65], edi
00A86530  89 7D 9F                        mov dword ptr [rbp - 0x61], edi
00A86533  89 7D B3                        mov dword ptr [rbp - 0x4d], edi
00A86536  89 7D 97                        mov dword ptr [rbp - 0x69], edi
00A86539  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
00A8653D  0F 11 4D 1F                     movups xmmword ptr [rbp + 0x1f], xmm1
00A86541  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00A86545  0F 11 4D D7                     movups xmmword ptr [rbp - 0x29], xmm1
00A86549  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00A8654D  0F 11 4D C7                     movups xmmword ptr [rbp - 0x39], xmm1
00A86551  85 D2                           test edx, edx
00A86553  74 6B                           je 0x140a865c0
00A86555  83 EA 01                        sub edx, 1
00A86558  0F 84 29 05 00 00               je 0x140a86a87
00A8655E  83 EA 01                        sub edx, 1
00A86561  0F 84 15 05 00 00               je 0x140a86a7c
00A86567  83 EA 01                        sub edx, 1
00A8656A  0F 84 01 05 00 00               je 0x140a86a71
00A86570  83 EA 01                        sub edx, 1
00A86573  0F 84 ED 04 00 00               je 0x140a86a66
00A86579  83 EA 01                        sub edx, 1
00A8657C  0F 84 D9 04 00 00               je 0x140a86a5b
00A86582  83 FA 01                        cmp edx, 1
00A86585  0F 84 89 04 00 00               je 0x140a86a14
00A8658B  BB 01 00 00 C0                  mov ebx, 0xc0000001
00A86590  8B C3                           mov eax, ebx
00A86592  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
00A86596  48 33 CC                        xor rcx, rsp
00A86599  E8 A2 60 C2 FF                  call 0x1406ac640
00A8659E  4C 8D 9C 24 00 01 00 00         lea r11, [rsp + 0x100]
00A865A6  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00A865AA  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00A865AE  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00A865B2  49 8B E3                        mov rsp, r11
00A865B5  41 5F                           pop r15
00A865B7  41 5E                           pop r14
00A865B9  41 5D                           pop r13
00A865BB  41 5C                           pop r12
00A865BD  5D                              pop rbp
00A865BE  C3                              ret
00A865BF  CC                              int3
00A865C0  44 8B F7                        mov r14d, edi
00A865C3  BE 00 02 00 00                  mov esi, 0x200
00A865C8  41 BF 50 70 20 20               mov r15d, 0x20207050
00A865CE  89 75 AB                        mov dword ptr [rbp - 0x55], esi
00A865D1  8B D6                           mov edx, esi
00A865D3  45 8B C7                        mov r8d, r15d
00A865D6  B9 00 01 00 00                  mov ecx, 0x100
00A865DB  E8 10 BB 0F 00                  call 0x140b820f0
00A865E0  4C 8B E0                        mov r12, rax
00A865E3  48 85 C0                        test rax, rax
00A865E6  0F 84 A6 04 00 00               je 0x140a86a92
00A865EC  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A865F0  48 8D 45 AB                     lea rax, [rbp - 0x55]
00A865F4  48 8B 0D 9D FD 3D 00            mov rcx, qword ptr [rip + 0x3dfd9d]
00A865FB  45 33 C9                        xor r9d, r9d
00A865FE  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00A86602  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A86607  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00A8660A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A8660E  45 8D 41 01                     lea r8d, [r9 + 1]
00A86612  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00A86617  48 8D 45 97                     lea rax, [rbp - 0x69]
00A8661B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A86620  48 8D 05 29 AF 58 FF            lea rax, [rip - 0xa750d7]
00A86627  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A8662C  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00A86631  E8 4A BB E5 FF                  call 0x1408e2180
00A86636  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A8663B  0F 84 5B 04 00 00               je 0x140a86a9c
00A86641  85 C0                           test eax, eax
00A86643  0F 88 65 04 00 00               js 0x140a86aae
00A86649  81 7D 97 12 20 00 00            cmp dword ptr [rbp - 0x69], 0x2012
00A86650  0F 85 58 04 00 00               jne 0x140a86aae
00A86656  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00A86659  45 8B C7                        mov r8d, r15d
00A8665C  66 89 45 E7                     mov word ptr [rbp - 0x19], ax
00A86660  48 8B D6                        mov rdx, rsi
00A86663  66 89 45 E9                     mov word ptr [rbp - 0x17], ax
00A86667  B9 00 01 00 00                  mov ecx, 0x100
00A8666C  4C 89 65 EF                     mov qword ptr [rbp - 0x11], r12
00A86670  89 75 9B                        mov dword ptr [rbp - 0x65], esi
00A86673  E8 78 BA 0F 00                  call 0x140b820f0
00A86678  4C 8B F8                        mov r15, rax
00A8667B  48 85 C0                        test rax, rax
00A8667E  0F 84 41 04 00 00               je 0x140a86ac5
00A86684  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A86688  48 8D 45 9B                     lea rax, [rbp - 0x65]
00A8668C  48 8B 0D 05 FD 3D 00            mov rcx, qword ptr [rip + 0x3dfd05]
00A86693  45 33 C9                        xor r9d, r9d
00A86696  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00A8669A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A8669F  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00A866A2  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A866A6  45 8D 41 01                     lea r8d, [r9 + 1]
00A866AA  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00A866AF  48 8D 45 97                     lea rax, [rbp - 0x69]
00A866B3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A866B8  48 8D 05 B1 AF 58 FF            lea rax, [rip - 0xa7504f]
00A866BF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A866C4  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00A866C9  E8 B2 BA E5 FF                  call 0x1408e2180
00A866CE  BE 50 70 20 20                  mov esi, 0x20207050
00A866D3  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A866D8  0F 84 E6 E3 0B 00               je 0x140b44ac4
00A866DE  85 C0                           test eax, eax
00A866E0  0F 88 39 03 00 00               js 0x140a86a1f
00A866E6  81 7D 97 12 20 00 00            cmp dword ptr [rbp - 0x69], 0x2012
00A866ED  0F 85 2C 03 00 00               jne 0x140a86a1f
00A866F3  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00A866F6  BA 40 00 00 00                  mov edx, 0x40
00A866FB  66 89 45 D7                     mov word ptr [rbp - 0x29], ax
00A866FF  89 55 9F                        mov dword ptr [rbp - 0x61], edx
00A86702  66 89 45 D9                     mov word ptr [rbp - 0x27], ax
00A86706  4C 89 7D DF                     mov qword ptr [rbp - 0x21], r15
00A8670A  44 8B C6                        mov r8d, esi
00A8670D  B9 00 01 00 00                  mov ecx, 0x100
00A86712  E8 D9 B9 0F 00                  call 0x140b820f0
00A86717  4C 8B E8                        mov r13, rax
00A8671A  48 85 C0                        test rax, rax
00A8671D  0F 84 AC 03 00 00               je 0x140a86acf
00A86723  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A86727  48 8D 45 9F                     lea rax, [rbp - 0x61]
00A8672B  48 8B 0D 66 FC 3D 00            mov rcx, qword ptr [rip + 0x3dfc66]
00A86732  45 33 C9                        xor r9d, r9d
00A86735  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00A86739  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A8673E  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
00A86741  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A86745  45 8D 41 01                     lea r8d, [r9 + 1]
00A86749  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00A8674E  48 8D 45 97                     lea rax, [rbp - 0x69]
00A86752  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A86757  48 8D 05 3A 56 59 FF            lea rax, [rip - 0xa6a9c6]
00A8675E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A86763  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00A86768  E8 13 BA E5 FF                  call 0x1408e2180
00A8676D  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A86772  0F 84 61 03 00 00               je 0x140a86ad9
00A86778  85 C0                           test eax, eax
00A8677A  0F 88 B6 02 00 00               js 0x140a86a36
00A86780  83 7D 97 12                     cmp dword ptr [rbp - 0x69], 0x12
00A86784  0F 85 AC 02 00 00               jne 0x140a86a36
00A8678A  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
00A8678D  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A86791  BE 10 00 00 00                  mov esi, 0x10
00A86796  48 8B 0D FB FB 3D 00            mov rcx, qword ptr [rip + 0x3dfbfb]
00A8679D  45 33 C9                        xor r9d, r9d
00A867A0  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00A867A4  66 89 45 C7                     mov word ptr [rbp - 0x39], ax
00A867A8  66 89 45 C9                     mov word ptr [rbp - 0x37], ax
00A867AC  44 8D 46 F1                     lea r8d, [rsi - 0xf]
00A867B0  48 8D 45 B3                     lea rax, [rbp - 0x4d]
00A867B4  4C 89 6D CF                     mov qword ptr [rbp - 0x31], r13
00A867B8  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A867BD  48 8D 45 1F                     lea rax, [rbp + 0x1f]
00A867C1  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00A867C5  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A867CA  48 8D 45 97                     lea rax, [rbp - 0x69]
00A867CE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A867D3  48 8D 05 AE AE 58 FF            lea rax, [rip - 0xa75152]
00A867DA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A867DF  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00A867E4  89 75 B3                        mov dword ptr [rbp - 0x4d], esi
00A867E7  E8 94 B9 E5 FF                  call 0x1408e2180
00A867EC  85 C0                           test eax, eax
00A867EE  0F 89 F7 02 00 00               jns 0x140a86aeb
00A867F4  0F 57 C0                        xorps xmm0, xmm0
00A867F7  0F 11 45 1F                     movups xmmword ptr [rbp + 0x1f], xmm0
00A867FB  B8 20 00 00 00                  mov eax, 0x20
00A86800  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00A86803  8B D0                           mov edx, eax
00A86805  B9 00 01 00 00                  mov ecx, 0x100
00A8680A  41 B8 50 70 20 20               mov r8d, 0x20207050
00A86810  E8 DB B8 0F 00                  call 0x140b820f0
00A86815  48 8B F0                        mov rsi, rax
00A86818  48 85 C0                        test rax, rax
00A8681B  0F 84 AE 02 00 00               je 0x140a86acf
00A86821  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A86825  48 8D 45 AF                     lea rax, [rbp - 0x51]
00A86829  48 8B 0D 68 FB 3D 00            mov rcx, qword ptr [rip + 0x3dfb68]
00A86830  45 33 C9                        xor r9d, r9d
00A86833  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00A86837  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A8683C  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
00A8683F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A86843  45 8D 41 01                     lea r8d, [r9 + 1]
00A86847  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00A8684C  48 8D 45 97                     lea rax, [rbp - 0x69]
00A86850  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A86855  48 8D 05 54 55 59 FF            lea rax, [rip - 0xa6aaac]
00A8685C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A86861  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00A86866  E8 15 B9 E5 FF                  call 0x1408e2180
00A8686B  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A86870  0F 84 8D 02 00 00               je 0x140a86b03
00A86876  85 C0                           test eax, eax
00A86878  0F 88 97 02 00 00               js 0x140a86b15
00A8687E  83 7D 97 12                     cmp dword ptr [rbp - 0x69], 0x12
00A86882  0F 85 8D 02 00 00               jne 0x140a86b15
00A86888  48 8B D6                        mov rdx, rsi
00A8688B  48 8D 4D FF                     lea rcx, [rbp - 1]
00A8688F  E8 EC 3E 9A FF                  call 0x14042a780
00A86894  BA 20 00 00 00                  mov edx, 0x20
00A86899  B9 00 01 00 00                  mov ecx, 0x100
00A8689E  41 B8 50 70 20 20               mov r8d, 0x20207050
00A868A4  89 55 A3                        mov dword ptr [rbp - 0x5d], edx
00A868A7  E8 44 B8 0F 00                  call 0x140b820f0
00A868AC  48 8B F8                        mov rdi, rax
00A868AF  48 85 C0                        test rax, rax
00A868B2  0F 84 72 02 00 00               je 0x140a86b2a
00A868B8  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00A868BD  48 8D 45 A3                     lea rax, [rbp - 0x5d]
00A868C1  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00A868C5  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A868CA  8B 45 A3                        mov eax, dword ptr [rbp - 0x5d]
00A868CD  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A868D1  48 8D 45 97                     lea rax, [rbp - 0x69]
00A868D5  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00A868DA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A868DF  48 8D 05 9A D7 58 FF            lea rax, [rip - 0xa72866]
00A868E6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A868EB  48 8B 0D A6 FA 3D 00            mov rcx, qword ptr [rip + 0x3dfaa6]
00A868F2  45 33 C9                        xor r9d, r9d
00A868F5  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00A868FB  45 8D 41 01                     lea r8d, [r9 + 1]
00A868FF  E8 7C B8 E5 FF                  call 0x1408e2180
00A86904  8B D8                           mov ebx, eax
00A86906  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A8690B  75 65                           jne 0x140a86972
00A8690D  33 D2                           xor edx, edx
00A8690F  48 8B CF                        mov rcx, rdi
00A86912  E8 59 BF 0F 00                  call 0x140b82870
00A86917  8B 55 A3                        mov edx, dword ptr [rbp - 0x5d]
00A8691A  B9 00 01 00 00                  mov ecx, 0x100
00A8691F  41 B8 50 70 20 20               mov r8d, 0x20207050
00A86925  E8 C6 B7 0F 00                  call 0x140b820f0
00A8692A  48 8B F8                        mov rdi, rax
00A8692D  48 85 C0                        test rax, rax
00A86930  0F 84 F4 01 00 00               je 0x140a86b2a
00A86936  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00A8693B  48 8D 45 A3                     lea rax, [rbp - 0x5d]
00A8693F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A86944  8B 45 A3                        mov eax, dword ptr [rbp - 0x5d]
00A86947  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A8694B  48 8D 45 97                     lea rax, [rbp - 0x69]
00A8694F  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00A86954  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A86959  48 8D 05 20 D7 58 FF            lea rax, [rip - 0xa728e0]
00A86960  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A86965  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00A86969  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00A8696D  E9 79 FF FF FF                  jmp 0x140a868eb
00A86972  85 DB                           test ebx, ebx
00A86974  0F 89 BA 01 00 00               jns 0x140a86b34
00A8697A  33 D2                           xor edx, edx
00A8697C  48 8B CF                        mov rcx, rdi
00A8697F  33 DB                           xor ebx, ebx
00A86981  E8 EA BE 0F 00                  call 0x140b82870
00A86986  21 5D A3                        and dword ptr [rbp - 0x5d], ebx
00A86989  33 FF                           xor edi, edi
00A8698B  33 D2                           xor edx, edx
00A8698D  48 8D 4D 0F                     lea rcx, [rbp + 0xf]
00A86991  E8 EA 3D 9A FF                  call 0x14042a780
00A86996  8A 45 A7                        mov al, byte ptr [rbp - 0x59]
00A86999  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00A8699D  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00A869A1  4C 8D 45 E7                     lea r8, [rbp - 0x19]
00A869A5  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00A869A9  48 8D 55 0F                     lea rdx, [rbp + 0xf]
00A869AD  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00A869B2  48 8D 45 FF                     lea rax, [rbp - 1]
00A869B6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A869BB  48 8D 45 1F                     lea rax, [rbp + 0x1f]
00A869BF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A869C4  48 8D 45 C7                     lea rax, [rbp - 0x39]
00A869C8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A869CD  E8 CE 01 00 00                  call 0x140a86ba0
00A869D2  48 85 FF                        test rdi, rdi
00A869D5  0F 85 8F 01 00 00               jne 0x140a86b6a
00A869DB  48 85 F6                        test rsi, rsi
00A869DE  0F 85 95 01 00 00               jne 0x140a86b79
00A869E4  4D 85 FF                        test r15, r15
00A869E7  0F 85 9B 01 00 00               jne 0x140a86b88
00A869ED  4D 85 E4                        test r12, r12
00A869F0  74 0A                           je 0x140a869fc
00A869F2  33 D2                           xor edx, edx
00A869F4  49 8B CC                        mov rcx, r12
00A869F7  E8 74 BE 0F 00                  call 0x140b82870
00A869FC  4D 85 ED                        test r13, r13
00A869FF  0F 84 8B FB FF FF               je 0x140a86590
00A86A05  33 D2                           xor edx, edx
00A86A07  49 8B CD                        mov rcx, r13
00A86A0A  E8 61 BE 0F 00                  call 0x140b82870
00A86A0F  E9 7C FB FF FF                  jmp 0x140a86590
00A86A14  41 BE 06 00 00 00               mov r14d, 6
00A86A1A  E9 A4 FB FF FF                  jmp 0x140a865c3
00A86A1F  33 D2                           xor edx, edx
00A86A21  49 8B CF                        mov rcx, r15
00A86A24  E8 47 BE 0F 00                  call 0x140b82870
00A86A29  8B C7                           mov eax, edi
00A86A2B  4C 8B FF                        mov r15, rdi
00A86A2E  89 45 9B                        mov dword ptr [rbp - 0x65], eax
00A86A31  E9 C0 FC FF FF                  jmp 0x140a866f6
00A86A36  33 D2                           xor edx, edx
00A86A38  49 8B CD                        mov rcx, r13
00A86A3B  E8 30 BE 0F 00                  call 0x140b82870
00A86A40  8B C7                           mov eax, edi
00A86A42  4C 8B EF                        mov r13, rdi
00A86A45  89 45 9F                        mov dword ptr [rbp - 0x61], eax
00A86A48  E9 40 FD FF FF                  jmp 0x140a8678d
00A86A4D  83 F8 12                        cmp eax, 0x12
00A86A50  0F 84 37 FF FF FF               je 0x140a8698d
00A86A56  E9 1F FF FF FF                  jmp 0x140a8697a
00A86A5B  41 BE 05 00 00 00               mov r14d, 5
00A86A61  E9 5D FB FF FF                  jmp 0x140a865c3
00A86A66  41 BE 04 00 00 00               mov r14d, 4
00A86A6C  E9 52 FB FF FF                  jmp 0x140a865c3
00A86A71  41 BE 03 00 00 00               mov r14d, 3
00A86A77  E9 47 FB FF FF                  jmp 0x140a865c3
00A86A7C  41 BE 02 00 00 00               mov r14d, 2
00A86A82  E9 3C FB FF FF                  jmp 0x140a865c3
00A86A87  41 BE 01 00 00 00               mov r14d, 1
00A86A8D  E9 31 FB FF FF                  jmp 0x140a865c3
00A86A92  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A86A97  E9 F4 FA FF FF                  jmp 0x140a86590
00A86A9C  33 D2                           xor edx, edx
00A86A9E  49 8B CC                        mov rcx, r12
00A86AA1  E8 CA BD 0F 00                  call 0x140b82870
00A86AA6  8B 55 AB                        mov edx, dword ptr [rbp - 0x55]
00A86AA9  E9 25 FB FF FF                  jmp 0x140a865d3
00A86AAE  33 D2                           xor edx, edx
00A86AB0  49 8B CC                        mov rcx, r12
00A86AB3  E8 B8 BD 0F 00                  call 0x140b82870
00A86AB8  8B C7                           mov eax, edi
00A86ABA  4C 8B E7                        mov r12, rdi
00A86ABD  89 45 AB                        mov dword ptr [rbp - 0x55], eax
00A86AC0  E9 94 FB FF FF                  jmp 0x140a86659
00A86AC5  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A86ACA  E9 1E FF FF FF                  jmp 0x140a869ed
00A86ACF  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A86AD4  E9 0B FF FF FF                  jmp 0x140a869e4
00A86AD9  33 D2                           xor edx, edx
00A86ADB  49 8B CD                        mov rcx, r13
00A86ADE  E8 8D BD 0F 00                  call 0x140b82870
00A86AE3  8B 55 9F                        mov edx, dword ptr [rbp - 0x61]
00A86AE6  E9 1F FC FF FF                  jmp 0x140a8670a
00A86AEB  83 7D 97 0D                     cmp dword ptr [rbp - 0x69], 0xd
00A86AEF  0F 85 FF FC FF FF               jne 0x140a867f4
00A86AF5  39 75 B3                        cmp dword ptr [rbp - 0x4d], esi
00A86AF8  0F 84 FD FC FF FF               je 0x140a867fb
00A86AFE  E9 F1 FC FF FF                  jmp 0x140a867f4
00A86B03  33 D2                           xor edx, edx
00A86B05  48 8B CE                        mov rcx, rsi
00A86B08  E8 63 BD 0F 00                  call 0x140b82870
00A86B0D  8B 55 AF                        mov edx, dword ptr [rbp - 0x51]
00A86B10  E9 F0 FC FF FF                  jmp 0x140a86805
00A86B15  33 D2                           xor edx, edx
00A86B17  48 8B CE                        mov rcx, rsi
00A86B1A  E8 51 BD 0F 00                  call 0x140b82870
00A86B1F  48 8B F7                        mov rsi, rdi
00A86B22  89 7D AF                        mov dword ptr [rbp - 0x51], edi
00A86B25  E9 5E FD FF FF                  jmp 0x140a86888
00A86B2A  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A86B2F  E9 A7 FE FF FF                  jmp 0x140a869db
00A86B34  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
00A86B37  83 F8 19                        cmp eax, 0x19
00A86B3A  0F 85 FA DF 0B 00               jne 0x140b44b3a
00A86B40  8B 55 A3                        mov edx, dword ptr [rbp - 0x5d]
00A86B43  4C 8D 4D F7                     lea r9, [rbp - 9]
00A86B47  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00A86B4B  48 8B CF                        mov rcx, rdi
00A86B4E  E8 55 69 FA FF                  call 0x140a2d4a8
00A86B53  85 C0                           test eax, eax
00A86B55  48 8B D7                        mov rdx, rdi
00A86B58  B8 12 00 00 00                  mov eax, 0x12
00A86B5D  48 0F 45 55 B7                  cmovne rdx, qword ptr [rbp - 0x49]
00A86B62  89 45 97                        mov dword ptr [rbp - 0x69], eax
00A86B65  E9 E3 FE FF FF                  jmp 0x140a86a4d
00A86B6A  33 D2                           xor edx, edx
00A86B6C  48 8B CF                        mov rcx, rdi
00A86B6F  E8 FC BC 0F 00                  call 0x140b82870
00A86B74  E9 62 FE FF FF                  jmp 0x140a869db
00A86B79  33 D2                           xor edx, edx
00A86B7B  48 8B CE                        mov rcx, rsi
00A86B7E  E8 ED BC 0F 00                  call 0x140b82870
00A86B83  E9 5C FE FF FF                  jmp 0x140a869e4
00A86B88  33 D2                           xor edx, edx
00A86B8A  49 8B CF                        mov rcx, r15
00A86B8D  E8 DE BC 0F 00                  call 0x140b82870
00A86B92  E9 56 FE FF FF                  jmp 0x140a869ed
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiAuditDeviceOperation(__int64 a1, int a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 3686970)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 47) = result;
    v_rdi = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 89) = a3;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = a1;
    *(unsigned int *)(v_rsp - 95 - 93) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = 0;
    *(unsigned int *)(v_rsp - 95 - 81) = 0;
    *(unsigned int *)(v_rsp - 95 - 101) = 0;
    *(unsigned int *)(v_rsp - 95 - 97) = 0;
    *(unsigned int *)(v_rsp - 95 - 77) = 0;
    *(unsigned int *)(v_rsp - 95 - 105) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 + 31) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = v_xmm1;
    if (a2 == 0) goto loc_00A865C0;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A86A87;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A86A7C;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A86A71;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A86A66;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A86A5B;
    if (a2 == 1) goto loc_00A86A14;
loc_00A86590:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_00A865C0:
loc_00A865C3:
    *(unsigned int *)(v_rsp - 95 - 85) = 512;
loc_00A865D3:
    result = ExAllocatePool2(256, 512, (unsigned int)((unsigned int)((unsigned int)(0x20207050ULL))), a4);
    if (result == 0) goto loc_00A86A92;
    a4 = 0;
    v_stack_mB0 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_mB8 = v_rsp - 95 - 85;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    v_stack_mC8 = result;
    v_stack_mD0 = v_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10965207;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4062621), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8), a4 + 1, a4);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00A86A9C;
    if (sign_flag) goto loc_00A86AAE;
    if ((*(unsigned int *)(v_rsp - 95 - 105)) != 0x2012ULL) goto loc_00A86AAE;
loc_00A86659:
    *(unsigned __int16 *)(v_rsp - 95 - 25) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    *(unsigned __int16 *)(v_rsp - 95 - 23) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    *(unsigned __int64 *)(v_rsp - 95 - 17) = result;
    *(unsigned int *)(v_rsp - 95 - 101) = 512;
    result = ExAllocatePool2(256, 512, (unsigned int)((unsigned int)((unsigned int)(0x20207050ULL))), a4);
    if (result == 0) goto loc_00A86AC5;
    a4 = 0;
    v_stack_mB0 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_mB8 = v_rsp - 95 - 101;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)));
    v_stack_mC8 = result;
    v_stack_mD0 = v_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10965071;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4062469), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8), a4 + 1, a4);
    if (sign_flag) goto loc_00A86A1F;
    if ((*(unsigned int *)(v_rsp - 95 - 105)) != 0x2012ULL) goto loc_00A86A1F;
loc_00A866F6:
    *(unsigned __int16 *)(v_rsp - 95 - 41) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)));
    *(unsigned int *)(v_rsp - 95 - 97) = 64;
    *(unsigned __int16 *)(v_rsp - 95 - 39) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 101)));
    *(unsigned __int64 *)(v_rsp - 95 - 33) = result;
loc_00A8670A:
    result = ExAllocatePool2(256, 64, (unsigned int)((unsigned int)((unsigned int)(0x20207050ULL))), a4);
    if (result == 0) goto loc_00A86ACF;
    a4 = 0;
    v_stack_mB0 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_mB8 = v_rsp - 95 - 97;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97)));
    v_stack_mC8 = result;
    v_stack_mD0 = v_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10922438;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4062310), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8), a4 + 1, a4);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00A86AD9;
    if (sign_flag) goto loc_00A86A36;
    if ((*(unsigned int *)(v_rsp - 95 - 105)) != 18) goto loc_00A86A36;
loc_00A8678D:
    a4 = 0;
    v_stack_mB0 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    *(unsigned __int16 *)(v_rsp - 95 - 57) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97)));
    *(unsigned __int16 *)(v_rsp - 95 - 55) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97)));
    *(unsigned __int64 *)(v_rsp - 95 - 49) = result;
    v_stack_mB8 = v_rsp - 95 - 77;
    v_stack_mC0 = 16;
    v_stack_mC8 = v_rsp - 95 + 31;
    v_stack_mD0 = v_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10965330;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    *(unsigned int *)(v_rsp - 95 - 77) = 16;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4062203), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8), 16 - 15, a4);
    if (!sign_flag) goto loc_00A86AEB;
loc_00A867F4:
    *(unsigned __int64 *)(v_rsp - 95 + 31) = v_xmm0;
loc_00A867FB:
    *(unsigned int *)(v_rsp - 95 - 81) = 32;
loc_00A86805:
    result = ExAllocatePool2(256, 32, (unsigned int)(0x20207050ULL), a4);
    if (result == 0) goto loc_00A86ACF;
    a4 = 0;
    v_stack_mB0 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_mB8 = v_rsp - 95 - 81;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81)));
    v_stack_mC8 = result;
    v_stack_mD0 = v_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10922668;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4062056), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8), a4 + 1, a4);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00A86B03;
    if (sign_flag) goto loc_00A86B15;
    if ((*(unsigned int *)(v_rsp - 95 - 105)) != 18) goto loc_00A86B15;
loc_00A86888:
    result = RtlInitUnicodeString(v_rsp - 95 - 1, result, a4 + 1, a4);
    *(unsigned int *)(v_rsp - 95 - 93) = 32;
    result = ExAllocatePool2(256, 32, (unsigned int)(0x20207050ULL), a4);
    if (result == 0) goto loc_00A86B2A;
    v_stack_mB8 = v_rsp - 95 - 93;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)));
    v_stack_mC8 = result;
    v_stack_mD0 = v_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10954854;
loc_00A868EB:
    a4 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4061862), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8), a4 + 1, a4);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00A86972;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a4 + 1, a4);
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)), (unsigned int)(0x20207050ULL), a4);
    if (result == 0) goto loc_00A86B2A;
    v_stack_mB8 = v_rsp - 95 - 93;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)));
    v_stack_mC8 = result;
    v_stack_mD0 = v_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10954976;
    goto loc_00A868EB;
loc_00A86972:
    if (!sign_flag) goto loc_00A86B34;
loc_00A8697A:
    a2 = 0;
    v_rbx = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x20207050ULL), a4);
    v_rdi = 0;
    a2 = 0;
loc_00A8698D:
    result = RtlInitUnicodeString(v_rsp - 95 + 15, a2, (unsigned int)(0x20207050ULL), a4);
    v_stack_mC0 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 95 - 89));
    v_stack_mC8 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72))));
    v_stack_mD0 = v_rsp - 95 - 1;
    v_stack_mD8 = v_rsp - 95 + 31;
    v_stack_mE0 = v_rsp - 95 - 57;
    result = SeAuditPlugAndPlay(*(unsigned __int64 *)(v_rsp - 95 - 65), v_rsp - 95 + 15, v_rsp - 95 - 25, v_rsp - 95 - 41);
    if (0 != 0) goto loc_00A86B6A;
loc_00A869DB:
    if (result != 0) goto loc_00A86B79;
loc_00A869E4:
    if (result != 0) goto loc_00A86B88;
loc_00A869ED:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    }
    if (result == 0) goto loc_00A86590;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    goto loc_00A86590;
loc_00A86A14:
    goto loc_00A865C3;
loc_00A86A1F:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    *(unsigned int *)(v_rsp - 95 - 101) = 0;
    goto loc_00A866F6;
loc_00A86A36:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    *(unsigned int *)(v_rsp - 95 - 97) = 0;
    goto loc_00A8678D;
loc_00A86A4D:
    if (0 == 18) goto loc_00A8698D;
    goto loc_00A8697A;
loc_00A86A5B:
    goto loc_00A865C3;
loc_00A86A66:
    goto loc_00A865C3;
loc_00A86A71:
    goto loc_00A865C3;
loc_00A86A7C:
    goto loc_00A865C3;
loc_00A86A87:
    goto loc_00A865C3;
loc_00A86A92:
    goto loc_00A86590;
loc_00A86A9C:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    goto loc_00A865D3;
loc_00A86AAE:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    *(unsigned int *)(v_rsp - 95 - 85) = 0;
    goto loc_00A86659;
loc_00A86AC5:
    goto loc_00A869ED;
loc_00A86ACF:
    goto loc_00A869E4;
loc_00A86AD9:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    goto loc_00A8670A;
loc_00A86AEB:
    if ((*(unsigned int *)(v_rsp - 95 - 105)) != 13) goto loc_00A867F4;
    if ((*(unsigned int *)(v_rsp - 95 - 77)) == ((unsigned int)(result))) goto loc_00A867FB;
    goto loc_00A867F4;
loc_00A86B03:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    goto loc_00A86805;
loc_00A86B15:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rsp - 95 - 25, v_rsp - 95 - 41);
    *(unsigned int *)(v_rsp - 95 - 81) = 0;
    goto loc_00A86888;
loc_00A86B2A:
    goto loc_00A869DB;
loc_00A86B34:
    result = PnpFindAlternateStringData(0, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)), v_rsp - 95 - 73, v_rsp - 95 - 9);
    a2 = 0;
    if ((unsigned int)(result) != 0) { a2 = *(unsigned __int64 *)(v_rsp - 95 - 73); }
    *(unsigned int *)(v_rsp - 95 - 105) = 18;
    goto loc_00A86A4D;
loc_00A86B6A:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, v_rsp - 95 - 73, v_rsp - 95 - 9);
    goto loc_00A869DB;
loc_00A86B79:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, v_rsp - 95 - 73, v_rsp - 95 - 9);
    goto loc_00A869E4;
loc_00A86B88:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, v_rsp - 95 - 73, v_rsp - 95 - 9);
    goto loc_00A869ED;
}
```

## 5. (Beta) C Style

```c
int64_t PiAuditDeviceOperation(void *Arg1, int32_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x38423A)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = result;
    local_rdi = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x59) = Arg3;
    *(void **)(local_rsp - 0x5F - 0x41) = Arg1;
    *(uint32_t *)(local_rsp - 0x5F - 0x5D) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x4D) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = v_xmm1;
    if (Arg2 == 0) goto loc_00A865C0;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A86A87;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A86A7C;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A86A71;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A86A66;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A86A5B;
    if (Arg2 == 1) goto loc_00A86A14;
loc_00A86590:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
loc_00A865C0:
loc_00A865C3:
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = 512;
loc_00A865D3:
    result = ExAllocatePool2(256, 512, (uint32_t)((uint32_t)((uint32_t)(0x20207050ULL))), Arg4);
    if (result == 0) goto loc_00A86A92;
    Arg4 = 0;
    v_stack_mB0 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_mB8 = local_rsp - 95 - 85;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    v_stack_mC8 = result;
    v_stack_mD0 = local_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10965207;
    v_stack_mE0 = *(uint64_t *)(v_stack_m28 + 0x48);
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x3DFD9D), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8), Arg4 + 1, Arg4);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00A86A9C;
    if (sign_flag) goto loc_00A86AAE;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x69)) != 0x2012ULL) goto loc_00A86AAE;
loc_00A86659:
    *(uint16_t *)(local_rsp - 0x5F - 0x19) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    *(uint16_t *)(local_rsp - 0x5F - 0x17) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = result;
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = 512;
    result = ExAllocatePool2(256, 512, (uint32_t)((uint32_t)((uint32_t)(0x20207050ULL))), Arg4);
    if (result == 0) goto loc_00A86AC5;
    Arg4 = 0;
    v_stack_mB0 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_mB8 = local_rsp - 95 - 101;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)));
    v_stack_mC8 = result;
    v_stack_mD0 = local_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10965071;
    v_stack_mE0 = *(uint64_t *)(v_stack_m28 + 0x48);
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x3DFD05), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8), Arg4 + 1, Arg4);
    if (sign_flag) goto loc_00A86A1F;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x69)) != 0x2012ULL) goto loc_00A86A1F;
loc_00A866F6:
    *(uint16_t *)(local_rsp - 0x5F - 0x29) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)));
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = 64;
    *(uint16_t *)(local_rsp - 0x5F - 0x27) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x65)));
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = result;
loc_00A8670A:
    result = ExAllocatePool2(256, 64, (uint32_t)((uint32_t)((uint32_t)(0x20207050ULL))), Arg4);
    if (result == 0) goto loc_00A86ACF;
    Arg4 = 0;
    v_stack_mB0 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_mB8 = local_rsp - 95 - 97;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61)));
    v_stack_mC8 = result;
    v_stack_mD0 = local_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10922438;
    v_stack_mE0 = *(uint64_t *)(v_stack_m28 + 0x48);
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x3DFC66), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8), Arg4 + 1, Arg4);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00A86AD9;
    if (sign_flag) goto loc_00A86A36;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x69)) != 18) goto loc_00A86A36;
loc_00A8678D:
    Arg4 = 0;
    v_stack_mB0 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    *(uint16_t *)(local_rsp - 0x5F - 0x39) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61)));
    *(uint16_t *)(local_rsp - 0x5F - 0x37) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61)));
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = result;
    v_stack_mB8 = local_rsp - 95 - 77;
    v_stack_mC0 = 16;
    v_stack_mC8 = local_rsp - 95 + 31;
    v_stack_mD0 = local_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10965330;
    v_stack_mE0 = *(uint64_t *)(v_stack_m28 + 0x48);
    *(uint32_t *)(local_rsp - 0x5F - 0x4D) = 16;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x3DFBFB), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8), 16 - 15, Arg4);
    if (!sign_flag) goto loc_00A86AEB;
loc_00A867F4:
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = v_xmm0;
loc_00A867FB:
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = 32;
loc_00A86805:
    result = ExAllocatePool2(256, 32, (uint32_t)(0x20207050ULL), Arg4);
    if (result == 0) goto loc_00A86ACF;
    Arg4 = 0;
    v_stack_mB0 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_mB8 = local_rsp - 95 - 81;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51)));
    v_stack_mC8 = result;
    v_stack_mD0 = local_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10922668;
    v_stack_mE0 = *(uint64_t *)(v_stack_m28 + 0x48);
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x3DFB68), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8), Arg4 + 1, Arg4);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00A86B03;
    if (sign_flag) goto loc_00A86B15;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x69)) != 18) goto loc_00A86B15;
loc_00A86888:
    result = RtlInitUnicodeString(local_rsp - 95 - 1, result, Arg4 + 1, Arg4);
    *(uint32_t *)(local_rsp - 0x5F - 0x5D) = 32;
    result = ExAllocatePool2(256, 32, (uint32_t)(0x20207050ULL), Arg4);
    if (result == 0) goto loc_00A86B2A;
    v_stack_mB8 = local_rsp - 95 - 93;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)));
    v_stack_mC8 = result;
    v_stack_mD0 = local_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10954854;
loc_00A868EB:
    Arg4 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x3DFAA6), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8), Arg4 + 1, Arg4);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00A86972;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg4 + 1, Arg4);
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)), (uint32_t)(0x20207050ULL), Arg4);
    if (result == 0) goto loc_00A86B2A;
    v_stack_mB8 = local_rsp - 95 - 93;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)));
    v_stack_mC8 = result;
    v_stack_mD0 = local_rsp - 95 - 105;
    v_stack_mD8 = v_rip - 10954976;
    goto loc_00A868EB;
loc_00A86972:
    if (!sign_flag) goto loc_00A86B34;
loc_00A8697A:
    Arg2 = 0;
    local_rbx = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x20207050ULL), Arg4);
    local_rdi = 0;
    Arg2 = 0;
loc_00A8698D:
    result = RtlInitUnicodeString(local_rsp - 95 + 15, Arg2, (uint32_t)(0x20207050ULL), Arg4);
    v_stack_mC0 = (uint8_t)(*(uint8_t *)(local_rsp - 0x5F - 0x59));
    v_stack_mC8 = (uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48))));
    v_stack_mD0 = local_rsp - 95 - 1;
    v_stack_mD8 = local_rsp - 95 + 31;
    v_stack_mE0 = local_rsp - 95 - 57;
    result = SeAuditPlugAndPlay(*(uint64_t *)(local_rsp - 0x5F - 0x41), local_rsp - 95 + 15, local_rsp - 95 - 25, local_rsp - 95 - 41);
    if (0 != 0) goto loc_00A86B6A;
loc_00A869DB:
    if (result != 0) goto loc_00A86B79;
loc_00A869E4:
    if (result != 0) goto loc_00A86B88;
loc_00A869ED:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    }
    if (result == 0) goto loc_00A86590;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    goto loc_00A86590;
loc_00A86A14:
    goto loc_00A865C3;
loc_00A86A1F:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    *(uint32_t *)(local_rsp - 0x5F - 0x65) = 0;
    goto loc_00A866F6;
loc_00A86A36:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = 0;
    goto loc_00A8678D;
loc_00A86A4D:
    if (0 == 18) goto loc_00A8698D;
    goto loc_00A8697A;
loc_00A86A5B:
    goto loc_00A865C3;
loc_00A86A66:
    goto loc_00A865C3;
loc_00A86A71:
    goto loc_00A865C3;
loc_00A86A7C:
    goto loc_00A865C3;
loc_00A86A87:
    goto loc_00A865C3;
loc_00A86A92:
    goto loc_00A86590;
loc_00A86A9C:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    goto loc_00A865D3;
loc_00A86AAE:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = 0;
    goto loc_00A86659;
loc_00A86AC5:
    goto loc_00A869ED;
loc_00A86ACF:
    goto loc_00A869E4;
loc_00A86AD9:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    goto loc_00A8670A;
loc_00A86AEB:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x69)) != 13) goto loc_00A867F4;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x4D)) == ((uint32_t)(result))) goto loc_00A867FB;
    goto loc_00A867F4;
loc_00A86B03:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    goto loc_00A86805;
loc_00A86B15:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, local_rsp - 95 - 25, local_rsp - 95 - 41);
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = 0;
    goto loc_00A86888;
loc_00A86B2A:
    goto loc_00A869DB;
loc_00A86B34:
    result = PnpFindAlternateStringData(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)), local_rsp - 95 - 73, local_rsp - 95 - 9);
    Arg2 = 0;
    if ((uint32_t)(result) != 0) { Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x49); }
    *(uint32_t *)(local_rsp - 0x5F - 0x69) = 18;
    goto loc_00A86A4D;
loc_00A86B6A:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, local_rsp - 95 - 73, local_rsp - 95 - 9);
    goto loc_00A869DB;
loc_00A86B79:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, local_rsp - 95 - 73, local_rsp - 95 - 9);
    goto loc_00A869E4;
loc_00A86B88:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, local_rsp - 95 - 73, local_rsp - 95 - 9);
    goto loc_00A869ED;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A864DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
