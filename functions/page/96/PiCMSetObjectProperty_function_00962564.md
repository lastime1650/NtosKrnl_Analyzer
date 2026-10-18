# PiCMSetObjectProperty

- RVA: `0x00962564`–`0x009628DD` (길이 `889` bytes)
- VA: `0x0000000140962564`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009343C`
- 디코드: `229`개 명령, `889/889` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x009625A8` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009625BD` → [PiCMCapturePropertyInputData](../8E/PiCMCapturePropertyInputData_function_008ED3A0.md) (function, `0x008ED3A0`)
- `0x00962629` → [PiAuDoesClientHaveAccess](PiAuDoesClientHaveAccess_function_00962940.md) (function, `0x00962940`)
- `0x009626AA` → [PiPnpRtlSetObjectProperty](../8F/PiPnpRtlSetObjectProperty_function_008F62A0.md) (function, `0x008F62A0`)
- `0x009626D5` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x009626E2` → [PnpSetDeviceInstancePropertyChangeEventFromDeviceInstance](../../text/49/PnpSetDeviceInstancePropertyChangeEventFromDeviceInstance_function_00493500.md) (function, `0x00493500`)
- `0x00962706` → [PiCMReturnBasicResultData](../8E/PiCMReturnBasicResultData_function_008E86E8.md) (function, `0x008E86E8`)
- `0x00962711` → [PiCMReleasePropertyInputData](PiCMReleasePropertyInputData_function_009628E4.md) (function, `0x009628E4`)
- `0x0096271F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiCMHandleIoctl](../8E/PiCMHandleIoctl_function_008EB880.md) at `0x008EC081`

### Static image references
- `0x0096257D` → RVA `0x00E0A740` (`.data`; read)
- `0x009626A3` → RVA `0x00E66398` (`.data`; read)
- `0x00962751` → RVA `0x00E663D0` (`.data`; read)
- `0x0096275F` → RVA `0x000127A8` (`.rdata`; read)
- `0x0096276B` → RVA `0x000127B0` (`.rdata`; read)
- `0x00962788` → RVA `0x00012790` (`.rdata`; read)
- `0x00962794` → RVA `0x00012798` (`.rdata`; read)
- `0x009627A6` → RVA `0x00012840` (`.rdata`; read)
- `0x009627B2` → RVA `0x00012848` (`.rdata`; read)
- `0x009627FE` → RVA `0x00014098` (`.rdata`; read)
- `0x0096280A` → RVA `0x000140A0` (`.rdata`; read)
- `0x00962864` → RVA `0x00027F20` (`.rdata`; read)
- `0x00962874` → RVA `0x00027F28` (`.rdata`; read)
- `0x0096288C` → RVA `0x00028430` (`.rdata`; read)
- `0x0096289C` → RVA `0x00028438` (`.rdata`; read)
- `0x009628C0` → RVA `0x00014110` (`.rdata`; read)
- `0x009628D1` → RVA `0x00014118` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x009625A8` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009626D5` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x009626E2` → [PnpSetDeviceInstancePropertyChangeEventFromDeviceInstance](../../text/49/PnpSetDeviceInstancePropertyChangeEventFromDeviceInstance_function_00493500.md) (`PAGE` → `.text`)
  - `0x0096271F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x0096286B` → [sub_00B28052](../B2/Unknown_function_00B28052.md) (`tail-transfer`)
  - `0x0096287B` → [sub_00B28052](../B2/Unknown_function_00B28052.md) (`tail-transfer`)
  - `0x00962893` → [sub_00B28052 + 0xE](../B2/Unknown_function_00B28052.md) (`tail-transfer`)
  - `0x009628A3` → [sub_00B28052 + 0xE](../B2/Unknown_function_00B28052.md) (`tail-transfer`)
  - `0x009628C7` → [sub_00B28052 + 0x1C](../B2/Unknown_function_00B28052.md) (`tail-transfer`)
  - `0x009628D8` → [sub_00B28052 + 0x1C](../B2/Unknown_function_00B28052.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00962564  40 55                           push rbp
00962566  53                              push rbx
00962567  56                              push rsi
00962568  57                              push rdi
00962569  41 54                           push r12
0096256B  41 55                           push r13
0096256D  41 56                           push r14
0096256F  41 57                           push r15
00962571  48 8D 6C 24 F1                  lea rbp, [rsp - 0xf]
00962576  48 81 EC D8 00 00 00            sub rsp, 0xd8
0096257D  48 8B 05 BC 81 4A 00            mov rax, qword ptr [rip + 0x4a81bc]
00962584  48 33 C4                        xor rax, rsp
00962587  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0096258B  48 8B 75 7F                     mov rsi, qword ptr [rbp + 0x7f]
0096258F  8B FA                           mov edi, edx
00962591  33 D2                           xor edx, edx
00962593  48 89 75 8F                     mov qword ptr [rbp - 0x71], rsi
00962597  4D 8B F8                        mov r15, r8
0096259A  48 8B D9                        mov rbx, rcx
0096259D  48 8D 4D A7                     lea rcx, [rbp - 0x59]
009625A1  45 8B E1                        mov r12d, r9d
009625A4  44 8D 42 48                     lea r8d, [rdx + 0x48]
009625A8  E8 93 46 D6 FF                  call 0x1406c6c40
009625AD  44 8B 45 77                     mov r8d, dword ptr [rbp + 0x77]
009625B1  4C 8D 4D A7                     lea r9, [rbp - 0x59]
009625B5  83 26 00                        and dword ptr [rsi], 0
009625B8  8B D7                           mov edx, edi
009625BA  48 8B CB                        mov rcx, rbx
009625BD  E8 DE AD F8 FF                  call 0x1408ed3a0
009625C2  8B D8                           mov ebx, eax
009625C4  85 C0                           test eax, eax
009625C6  0F 88 41 01 00 00               js 0x14096270d
009625CC  8B 45 E7                        mov eax, dword ptr [rbp - 0x19]
009625CF  BF 05 00 00 00                  mov edi, 5
009625D4  48 8B 55 D3                     mov rdx, qword ptr [rbp - 0x2d]
009625D8  8B 5D AF                        mov ebx, dword ptr [rbp - 0x51]
009625DB  8B 75 D7                        mov esi, dword ptr [rbp - 0x29]
009625DE  4C 8B 75 B7                     mov r14, qword ptr [rbp - 0x49]
009625E2  4C 8B 6D DF                     mov r13, qword ptr [rbp - 0x21]
009625E6  4C 8B 45 CB                     mov r8, qword ptr [rbp - 0x35]
009625EA  89 45 87                        mov dword ptr [rbp - 0x79], eax
009625ED  48 8B 45 C3                     mov rax, qword ptr [rbp - 0x3d]
009625F1  83 FA 0E                        cmp edx, 0xe
009625F4  0F 84 01 02 00 00               je 0x1409627fb
009625FA  83 FA 03                        cmp edx, 3
009625FD  0F 84 5E 02 00 00               je 0x140962861
00962603  83 FA 04                        cmp edx, 4
00962606  0F 84 79 01 00 00               je 0x140962785
0096260C  83 FA 02                        cmp edx, 2
0096260F  0F 84 47 01 00 00               je 0x14096275c
00962615  3B D7                           cmp edx, edi
00962617  0F 84 89 01 00 00               je 0x1409627a6
0096261D  33 C0                           xor eax, eax
0096261F  F7 D8                           neg eax
00962621  1B C9                           sbb ecx, ecx
00962623  83 E1 3E                        and ecx, 0x3e
00962626  83 C1 02                        add ecx, 2
00962629  E8 12 03 00 00                  call 0x140962940
0096262E  33 C9                           xor ecx, ecx
00962630  84 C0                           test al, al
00962632  0F 84 70 02 00 00               je 0x1409628a8
00962638  4D 85 F6                        test r14, r14
0096263B  0F 84 AC 00 00 00               je 0x1409626ed
00962641  39 4D AB                        cmp dword ptr [rbp - 0x55], ecx
00962644  0F 85 A3 00 00 00               jne 0x1409626ed
0096264A  4D 85 FF                        test r15, r15
0096264D  0F 84 9A 00 00 00               je 0x1409626ed
00962653  41 83 FC 08                     cmp r12d, 8
00962657  0F 82 90 00 00 00               jb 0x1409626ed
0096265D  83 FB 06                        cmp ebx, 6
00962660  0F 8F D3 00 00 00               jg 0x140962739
00962666  0F 84 EB 01 00 00               je 0x140962857
0096266C  83 EB 01                        sub ebx, 1
0096266F  0F 85 4E 01 00 00               jne 0x1409627c3
00962675  8D 79 01                        lea edi, [rcx + 1]
00962678  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
0096267B  45 33 C9                        xor r9d, r9d
0096267E  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00962682  44 8B C7                        mov r8d, edi
00962685  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00962689  49 8B D6                        mov rdx, r14
0096268C  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00962691  48 8D 45 C3                     lea rax, [rbp - 0x3d]
00962695  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00962699  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0096269E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009626A3  48 8B 0D EE 3C 50 00            mov rcx, qword ptr [rip + 0x503cee]
009626AA  E8 F1 3B F9 FF                  call 0x1408f62a0
009626AF  8B D8                           mov ebx, eax
009626B1  8B F0                           mov esi, eax
009626B3  3D 22 00 00 C0                  cmp eax, 0xc0000022
009626B8  0F 84 F4 01 00 00               je 0x1409628b2
009626BE  85 C0                           test eax, eax
009626C0  78 30                           js 0x1409626f2
009626C2  83 FF 01                        cmp edi, 1
009626C5  75 2B                           jne 0x1409626f2
009626C7  0F 57 C0                        xorps xmm0, xmm0
009626CA  48 8D 4D 97                     lea rcx, [rbp - 0x69]
009626CE  49 8B D6                        mov rdx, r14
009626D1  0F 11 45 97                     movups xmmword ptr [rbp - 0x69], xmm0
009626D5  E8 86 12 B0 FF                  call 0x140463960
009626DA  85 C0                           test eax, eax
009626DC  78 14                           js 0x1409626f2
009626DE  48 8D 4D 97                     lea rcx, [rbp - 0x69]
009626E2  E8 19 0E B3 FF                  call 0x140493500
009626E7  EB 09                           jmp 0x1409626f2
009626E9  85 FF                           test edi, edi
009626EB  75 8B                           jne 0x140962678
009626ED  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009626F2  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
009626F6  45 8B CC                        mov r9d, r12d
009626F9  8B 55 EB                        mov edx, dword ptr [rbp - 0x15]
009626FC  4D 8B C7                        mov r8, r15
009626FF  8B CB                           mov ecx, ebx
00962701  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00962706  E8 DD 5F F8 FF                  call 0x1408e86e8
0096270B  8B D8                           mov ebx, eax
0096270D  48 8D 4D A7                     lea rcx, [rbp - 0x59]
00962711  E8 CE 01 00 00                  call 0x1409628e4
00962716  8B C3                           mov eax, ebx
00962718  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
0096271C  48 33 CC                        xor rcx, rsp
0096271F  E8 1C 9F D4 FF                  call 0x1406ac640
00962724  48 81 C4 D8 00 00 00            add rsp, 0xd8
0096272B  41 5F                           pop r15
0096272D  41 5E                           pop r14
0096272F  41 5D                           pop r13
00962731  41 5C                           pop r12
00962733  5F                              pop rdi
00962734  5E                              pop rsi
00962735  5B                              pop rbx
00962736  5D                              pop rbp
00962737  C3                              ret
00962738  CC                              int3
00962739  81 EB 01 00 01 00               sub ebx, 0x10001
0096273F  0F 84 95 00 00 00               je 0x1409627da
00962745  83 EB 01                        sub ebx, 1
00962748  0F 85 96 00 00 00               jne 0x1409627e4
0096274E  8D 7B 08                        lea edi, [rbx + 8]
00962751  48 39 0D 78 3C 50 00            cmp qword ptr [rip + 0x503c78], rcx
00962758  74 93                           je 0x1409626ed
0096275A  EB 8D                           jmp 0x1409626e9
0096275C  48 8B C8                        mov rcx, rax
0096275F  48 2B 0D 42 00 6B FF            sub rcx, qword ptr [rip - 0x94ffbe]
00962766  75 0A                           jne 0x140962772
00962768  49 8B C8                        mov rcx, r8
0096276B  48 2B 0D 3E 00 6B FF            sub rcx, qword ptr [rip - 0x94ffc2]
00962772  48 85 C9                        test rcx, rcx
00962775  0F 85 05 01 00 00               jne 0x140962880
0096277B  B8 01 00 00 00                  mov eax, 1
00962780  E9 9A FE FF FF                  jmp 0x14096261f
00962785  48 8B C8                        mov rcx, rax
00962788  48 2B 0D 01 00 6B FF            sub rcx, qword ptr [rip - 0x94ffff]
0096278F  75 0A                           jne 0x14096279b
00962791  49 8B C8                        mov rcx, r8
00962794  48 2B 0D FD FF 6A FF            sub rcx, qword ptr [rip - 0x950003]
0096279B  48 85 C9                        test rcx, rcx
0096279E  0F 85 68 FE FF FF               jne 0x14096260c
009627A4  EB D5                           jmp 0x14096277b
009627A6  48 2B 05 93 00 6B FF            sub rax, qword ptr [rip - 0x94ff6d]
009627AD  75 0A                           jne 0x1409627b9
009627AF  49 8B C0                        mov rax, r8
009627B2  48 2B 05 8F 00 6B FF            sub rax, qword ptr [rip - 0x94ff71]
009627B9  48 85 C0                        test rax, rax
009627BC  74 BD                           je 0x14096277b
009627BE  E9 5A FE FF FF                  jmp 0x14096261d
009627C3  83 EB 01                        sub ebx, 1
009627C6  74 57                           je 0x14096281f
009627C8  83 EB 01                        sub ebx, 1
009627CB  74 24                           je 0x1409627f1
009627CD  83 EB 01                        sub ebx, 1
009627D0  75 6D                           jne 0x14096283f
009627D2  8D 7B 03                        lea edi, [rbx + 3]
009627D5  E9 9E FE FF FF                  jmp 0x140962678
009627DA  BF 07 00 00 00                  mov edi, 7
009627DF  E9 6D FF FF FF                  jmp 0x140962751
009627E4  83 EB 01                        sub ebx, 1
009627E7  75 40                           jne 0x140962829
009627E9  8D 7B 09                        lea edi, [rbx + 9]
009627EC  E9 60 FF FF FF                  jmp 0x140962751
009627F1  BF 04 00 00 00                  mov edi, 4
009627F6  E9 7D FE FF FF                  jmp 0x140962678
009627FB  48 8B C8                        mov rcx, rax
009627FE  48 2B 0D 93 18 6B FF            sub rcx, qword ptr [rip - 0x94e76d]
00962805  75 0A                           jne 0x140962811
00962807  49 8B C8                        mov rcx, r8
0096280A  48 2B 0D 8F 18 6B FF            sub rcx, qword ptr [rip - 0x94e771]
00962811  48 85 C9                        test rcx, rcx
00962814  0F 85 E0 FD FF FF               jne 0x1409625fa
0096281A  E9 5C FF FF FF                  jmp 0x14096277b
0096281F  BF 02 00 00 00                  mov edi, 2
00962824  E9 4F FE FF FF                  jmp 0x140962678
00962829  83 EB 01                        sub ebx, 1
0096282C  74 1F                           je 0x14096284d
0096282E  83 FB 01                        cmp ebx, 1
00962831  0F 85 B6 FE FF FF               jne 0x1409626ed
00962837  8D 7B 0A                        lea edi, [rbx + 0xa]
0096283A  E9 12 FF FF FF                  jmp 0x140962751
0096283F  83 FB 01                        cmp ebx, 1
00962842  0F 84 30 FE FF FF               je 0x140962678
00962848  E9 A0 FE FF FF                  jmp 0x1409626ed
0096284D  BF 0A 00 00 00                  mov edi, 0xa
00962852  E9 FA FE FF FF                  jmp 0x140962751
00962857  BF 06 00 00 00                  mov edi, 6
0096285C  E9 17 FE FF FF                  jmp 0x140962678
00962861  48 8B C8                        mov rcx, rax
00962864  48 2B 0D B5 56 6C FF            sub rcx, qword ptr [rip - 0x93a94b]
0096286B  0F 85 E1 57 1C 00               jne 0x140b28052
00962871  49 8B C8                        mov rcx, r8
00962874  48 2B 0D AD 56 6C FF            sub rcx, qword ptr [rip - 0x93a953]
0096287B  E9 D2 57 1C 00                  jmp 0x140b28052
00962880  83 FA 02                        cmp edx, 2
00962883  0F 85 8C FD FF FF               jne 0x140962615
00962889  48 8B C8                        mov rcx, rax
0096288C  48 2B 0D 9D 5B 6C FF            sub rcx, qword ptr [rip - 0x93a463]
00962893  0F 85 C7 57 1C 00               jne 0x140b28060
00962899  49 8B C8                        mov rcx, r8
0096289C  48 2B 0D 95 5B 6C FF            sub rcx, qword ptr [rip - 0x93a46b]
009628A3  E9 B8 57 1C 00                  jmp 0x140b28060
009628A8  BB 22 00 00 C0                  mov ebx, 0xc0000022
009628AD  E9 40 FE FF FF                  jmp 0x1409626f2
009628B2  83 7D D3 26                     cmp dword ptr [rbp - 0x2d], 0x26
009628B6  0F 85 36 FE FF FF               jne 0x1409626f2
009628BC  48 8B 45 C3                     mov rax, qword ptr [rbp - 0x3d]
009628C0  48 2B 05 49 18 6B FF            sub rax, qword ptr [rip - 0x94e7b7]
009628C7  0F 85 A1 57 1C 00               jne 0x140b2806e
009628CD  48 8B 45 CB                     mov rax, qword ptr [rbp - 0x35]
009628D1  48 2B 05 40 18 6B FF            sub rax, qword ptr [rip - 0x94e7c0]
009628D8  E9 91 57 1C 00                  jmp 0x140b2806e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCMSetObjectProperty(__int64 a1, int a2, __int64 a3, int a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m4F;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m7C;
    unsigned __int64 v_stack_m84;
    unsigned __int64 v_stack_m8C;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (216);
    result = (*(unsigned __int64 *)(v_rip + 4882876)) ^ (v_rsp);
    v_stack_m58 = result;
    a2 = 0;
    v_stack_mC0 = a6;
    result = memset(v_stack_mA8, a2, a2 + 72, a4);
    result = PiCMCapturePropertyInputData(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)(a5), v_stack_mA8);
    if (sign_flag) goto loc_0096270D;
    v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_m68));
    if (((unsigned int)(v_stack_m7C)) == 14) goto loc_009627FB;
loc_009625FA:
    if (((unsigned int)(v_stack_m7C)) == 3) goto loc_00962861;
    if (((unsigned int)(v_stack_m7C)) == 4) goto loc_00962785;
loc_0096260C:
    if (((unsigned int)(v_stack_m7C)) == 2) goto loc_0096275C;
loc_00962615:
    if (((unsigned int)(v_stack_m7C)) == 5) goto loc_009627A6;
loc_0096261D:
    result = 0;
loc_0096261F:
    result = (unsigned int)(-(result));
    a1 = (unsigned int)((a1) & (62));
    a1 = (unsigned int)((a1) + (2));
    result = PiAuDoesClientHaveAccess(a1, v_stack_m7C, v_stack_m84, v_stack_mA8);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_009628A8;
    if (v_stack_m98 == 0) goto loc_009626ED;
    if (v_stack_mA4 != 0) goto loc_009626ED;
    if (a3 == 0) goto loc_009626ED;
    if (((unsigned int)((unsigned int)(a4))) < 8) goto loc_009626ED;
    if (((unsigned int)((unsigned int)(v_stack_mA0))) > 6) goto loc_00962739;
    if (((unsigned int)((unsigned int)(v_stack_mA0))) == 6) goto loc_00962857;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mA0)) - (1));
    if (condition_is_not_equal) goto loc_009627C3;
loc_00962678:
    a4 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = (unsigned int)((unsigned int)(v_stack_mC8));
    v_stack_mE0 = v_stack_m70;
    v_stack_mE8 = (unsigned int)((unsigned int)(v_stack_m78));
    v_stack_mF0 = v_stack_m8C;
    v_stack_mF8 = 0;
    result = PiPnpRtlSetObjectProperty(*(unsigned __int64 *)(v_rip + 5258478), v_stack_m98, (unsigned int)((unsigned int)(a1 + 1)), a4);
    if (((unsigned int)(result)) == 0xC0000022ULL) goto loc_009628B2;
    if (sign_flag) goto loc_009626F2;
    if (((unsigned int)(a1 + 1)) != 1) goto loc_009626F2;
    v_stack_mB8 = v_xmm0;
    result = RtlInitUnicodeStringEx(v_stack_mB8, v_stack_m98, (unsigned int)((unsigned int)(a1 + 1)), a4);
    if (sign_flag) goto loc_009626F2;
    result = PnpSetDeviceInstancePropertyChangeEventFromDeviceInstance(v_stack_mB8, v_stack_m98, (unsigned int)((unsigned int)(a1 + 1)), a4);
    goto loc_009626F2;
loc_009626E9:
    if ((unsigned int)(a1 + 1) != 0) goto loc_00962678;
loc_009626ED:
loc_009626F2:
    v_stack_mF8 = v_stack_mC0;
    result = PiCMReturnBasicResultData((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), (unsigned int)(v_stack_m64), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
loc_0096270D:
    result = PiCMReleasePropertyInputData(v_stack_mA8, (unsigned int)(v_stack_m64), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(v_stack_m64), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_rsp = (v_rsp) + (216);
    return result;
loc_00962739:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) - (0x10001ULL));
    if (condition_is_equal) goto loc_009627DA;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_009627E4;
loc_00962751:
    if ((*(unsigned __int64 *)(v_rip + 5258360)) == a1) goto loc_009626ED;
    goto loc_009626E9;
loc_0096275C:
    a1 = (result) - (*(unsigned __int64 *)(v_rip - 9764798));
    if (!(condition_is_not_equal)) {
        a1 = a3;
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 9764802));
    }
    if (a1 != 0) goto loc_00962880;
loc_0096277B:
    goto loc_0096261F;
loc_00962785:
    a1 = (1) - (*(unsigned __int64 *)(v_rip - 9764863));
    if (!(condition_is_not_equal)) {
        a1 = a3;
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 9764867));
    }
    if (a1 != 0) goto loc_0096260C;
    goto loc_0096277B;
loc_009627A6:
    result = (1) - (*(unsigned __int64 *)(v_rip - 9764717));
    if (!(condition_is_not_equal)) {
        result = a3;
        result = (result) - (*(unsigned __int64 *)(v_rip - 9764721));
    }
    if (result == 0) goto loc_0096277B;
    goto loc_0096261D;
loc_009627C3:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0096281F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_009627F1;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_0096283F;
    goto loc_00962678;
loc_009627DA:
    goto loc_00962751;
loc_009627E4:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_00962829;
    goto loc_00962751;
loc_009627F1:
    goto loc_00962678;
loc_009627FB:
    a1 = (result) - (*(unsigned __int64 *)(v_rip - 9758573));
    if (!(condition_is_not_equal)) {
        a1 = a3;
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 9758577));
    }
    if (a1 != 0) goto loc_009625FA;
    goto loc_0096277B;
loc_0096281F:
    goto loc_00962678;
loc_00962829:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0096284D;
    if (((unsigned int)(v_rbx)) != 1) goto loc_009626ED;
    goto loc_00962751;
loc_0096283F:
    if (((unsigned int)(v_rbx)) == 1) goto loc_00962678;
    goto loc_009626ED;
loc_0096284D:
    goto loc_00962751;
loc_00962857:
    goto loc_00962678;
loc_00962861:
    a1 = (result) - (*(unsigned __int64 *)(v_rip - 9677131));
    a1 = (a3) - (*(unsigned __int64 *)(v_rip - 9677139));
loc_00962880:
    if (((unsigned int)((unsigned int)(v_stack_m64))) != 2) goto loc_00962615;
    a1 = (result) - (*(unsigned __int64 *)(v_rip - 9675875));
    a1 = (a3) - (*(unsigned __int64 *)(v_rip - 9675883));
loc_009628A8:
    goto loc_009626F2;
loc_009628B2:
    if (v_stack_m7C != 38) goto loc_009626F2;
    result = (v_stack_m8C) - (*(unsigned __int64 *)(v_rip - 9758647));
    result = (v_stack_m84) - (*(unsigned __int64 *)(v_rip - 9758656));
}
```

## 5. (Beta) C Style

```c
int64_t PiCMSetObjectProperty(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m4F;
    uint64_t v_stack_m58;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m7C;
    uint64_t v_stack_m84;
    uint64_t v_stack_m8C;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (216);
    result = (*(uint64_t *)(v_rip + 0x4A81BC)) ^ (local_rsp);
    v_stack_m58 = result;
    Arg2 = 0;
    v_stack_mC0 = Arg6;
    result = memset(v_stack_mA8, Arg2, Arg2 + 72, Arg4);
    result = PiCMCapturePropertyInputData(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)(Arg5), v_stack_mA8);
    if (sign_flag) goto loc_0096270D;
    v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_m68));
    if (((uint32_t)(v_stack_m7C)) == 14) goto loc_009627FB;
loc_009625FA:
    if (((uint32_t)(v_stack_m7C)) == 3) goto loc_00962861;
    if (((uint32_t)(v_stack_m7C)) == 4) goto loc_00962785;
loc_0096260C:
    if (((uint32_t)(v_stack_m7C)) == 2) goto loc_0096275C;
loc_00962615:
    if (((uint32_t)(v_stack_m7C)) == 5) goto loc_009627A6;
loc_0096261D:
    result = 0;
loc_0096261F:
    result = (uint32_t)(-(result));
    Arg1 = (uint32_t)((Arg1) & (62));
    Arg1 = (uint32_t)((Arg1) + (2));
    result = PiAuDoesClientHaveAccess(Arg1, v_stack_m7C, v_stack_m84, v_stack_mA8);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_009628A8;
    if (v_stack_m98 == 0) goto loc_009626ED;
    if (v_stack_mA4 != 0) goto loc_009626ED;
    if (Arg3 == 0) goto loc_009626ED;
    if (((uint32_t)((uint32_t)(Arg4))) < 8) goto loc_009626ED;
    if (((uint32_t)((uint32_t)(v_stack_mA0))) > 6) goto loc_00962739;
    if (((uint32_t)((uint32_t)(v_stack_mA0))) == 6) goto loc_00962857;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mA0)) - (1));
    if (condition_is_not_equal) goto loc_009627C3;
loc_00962678:
    Arg4 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = (uint32_t)((uint32_t)(v_stack_mC8));
    v_stack_mE0 = v_stack_m70;
    v_stack_mE8 = (uint32_t)((uint32_t)(v_stack_m78));
    v_stack_mF0 = v_stack_m8C;
    v_stack_mF8 = 0;
    result = PiPnpRtlSetObjectProperty(*(uint64_t *)(v_rip + 0x503CEE), v_stack_m98, (uint32_t)((uint32_t)(Arg1 + 1)), Arg4);
    if (((uint32_t)(result)) == 0xC0000022ULL) goto loc_009628B2;
    if (sign_flag) goto loc_009626F2;
    if (((uint32_t)(Arg1 + 1)) != 1) goto loc_009626F2;
    v_stack_mB8 = v_xmm0;
    result = RtlInitUnicodeStringEx(v_stack_mB8, v_stack_m98, (uint32_t)((uint32_t)(Arg1 + 1)), Arg4);
    if (sign_flag) goto loc_009626F2;
    result = PnpSetDeviceInstancePropertyChangeEventFromDeviceInstance(v_stack_mB8, v_stack_m98, (uint32_t)((uint32_t)(Arg1 + 1)), Arg4);
    goto loc_009626F2;
loc_009626E9:
    if ((uint32_t)(Arg1 + 1) != 0) goto loc_00962678;
loc_009626ED:
loc_009626F2:
    v_stack_mF8 = v_stack_mC0;
    result = PiCMReturnBasicResultData((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), (uint32_t)(v_stack_m64), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
loc_0096270D:
    result = PiCMReleasePropertyInputData(v_stack_mA8, (uint32_t)(v_stack_m64), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(v_stack_m64), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    local_rsp = (local_rsp) + (216);
    return result;
loc_00962739:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) - (0x10001ULL));
    if (condition_is_equal) goto loc_009627DA;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_009627E4;
loc_00962751:
    if ((*(uint64_t *)(v_rip + 0x503C78)) == Arg1) goto loc_009626ED;
    goto loc_009626E9;
loc_0096275C:
    Arg1 = (result) - (*(uint64_t *)(v_rip - 0x94FFBE));
    if (!(condition_is_not_equal)) {
        Arg1 = Arg3;
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x94FFC2));
    }
    if (Arg1 != 0) goto loc_00962880;
loc_0096277B:
    goto loc_0096261F;
loc_00962785:
    Arg1 = (1) - (*(uint64_t *)(v_rip - 0x94FFFF));
    if (!(condition_is_not_equal)) {
        Arg1 = Arg3;
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x950003));
    }
    if (Arg1 != 0) goto loc_0096260C;
    goto loc_0096277B;
loc_009627A6:
    result = (1) - (*(uint64_t *)(v_rip - 0x94FF6D));
    if (!(condition_is_not_equal)) {
        result = Arg3;
        result = (result) - (*(uint64_t *)(v_rip - 0x94FF71));
    }
    if (result == 0) goto loc_0096277B;
    goto loc_0096261D;
loc_009627C3:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0096281F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_009627F1;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_0096283F;
    goto loc_00962678;
loc_009627DA:
    goto loc_00962751;
loc_009627E4:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_00962829;
    goto loc_00962751;
loc_009627F1:
    goto loc_00962678;
loc_009627FB:
    Arg1 = (result) - (*(uint64_t *)(v_rip - 0x94E76D));
    if (!(condition_is_not_equal)) {
        Arg1 = Arg3;
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x94E771));
    }
    if (Arg1 != 0) goto loc_009625FA;
    goto loc_0096277B;
loc_0096281F:
    goto loc_00962678;
loc_00962829:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0096284D;
    if (((uint32_t)(local_rbx)) != 1) goto loc_009626ED;
    goto loc_00962751;
loc_0096283F:
    if (((uint32_t)(local_rbx)) == 1) goto loc_00962678;
    goto loc_009626ED;
loc_0096284D:
    goto loc_00962751;
loc_00962857:
    goto loc_00962678;
loc_00962861:
    Arg1 = (result) - (*(uint64_t *)(v_rip - 0x93A94B));
    Arg1 = (Arg3) - (*(uint64_t *)(v_rip - 0x93A953));
loc_00962880:
    if (((uint32_t)((uint32_t)(v_stack_m64))) != 2) goto loc_00962615;
    Arg1 = (result) - (*(uint64_t *)(v_rip - 0x93A463));
    Arg1 = (Arg3) - (*(uint64_t *)(v_rip - 0x93A46B));
loc_009628A8:
    goto loc_009626F2;
loc_009628B2:
    if (v_stack_m7C != 38) goto loc_009626F2;
    result = (v_stack_m8C) - (*(uint64_t *)(v_rip - 0x94E7B7));
    result = (v_stack_m84) - (*(uint64_t *)(v_rip - 0x94E7C0));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00962564&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
