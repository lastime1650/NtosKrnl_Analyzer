# PopDiagTraceSleepStudyStart

- RVA: `0x00762FC0`–`0x0076311B` (길이 `347` bytes)
- VA: `0x0000000140762FC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC864`
- 디코드: `74`개 명령, `347/347` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00762FFA` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0076304C` → [PopGetModernStandbyTransitionReason](../../text/4B/PopGetModernStandbyTransitionReason_function_004BDF6C.md) (function, `0x004BDF6C`)
- `0x00763100` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x0076310C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopSleepstudyScenarioStopWorker](../AC/PopSleepstudyScenarioStopWorker_function_00AC0100.md) at `0x00AC014D`
- [PopSleepstudyStartNextSession](../AC/PopSleepstudyStartNextSession_function_00AC4720.md) at `0x00AC4C44`

### Static image references
- `0x00762FD1` → RVA `0x00E0A740` (`.data`; read)
- `0x00762FDF` → RVA `0x00E67859` (`.data`; read)
- `0x00762FEC` → RVA `0x00F0B6B8` (`.data`; read)
- `0x00762FF3` → RVA `0x00029808` (`.rdata`; read)
- `0x00763022` → RVA `0x00F0B418` (`.data`; read)
- `0x0076302D` → RVA `0x00F0B410` (`.data`; read)
- `0x0076308D` → RVA `0x00E27D00` (`.data`; read)
- `0x00763098` → RVA `0x00E27DE8` (`.data`; read)
- `0x007630E3` → RVA `0x00E67870` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00762FFA` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x0076304C` → [PopGetModernStandbyTransitionReason](../../text/4B/PopGetModernStandbyTransitionReason_function_004BDF6C.md) (`PAGE` → `.text`)
  - `0x00763100` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x0076310C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00762FC0  88 4C 24 08                     mov byte ptr [rsp + 8], cl
00762FC4  55                              push rbp
00762FC5  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00762FCA  48 81 EC E0 00 00 00            sub rsp, 0xe0
00762FD1  48 8B 05 68 77 6A 00            mov rax, qword ptr [rip + 0x6a7768]
00762FD8  48 33 C4                        xor rax, rsp
00762FDB  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00762FDF  80 3D 73 48 70 00 00            cmp byte ptr [rip + 0x704873], 0
00762FE6  0F 84 19 01 00 00               je 0x140763105
00762FEC  48 8B 0D C5 86 7A 00            mov rcx, qword ptr [rip + 0x7a86c5]
00762FF3  48 8D 15 0E 68 8C FF            lea rdx, [rip - 0x7397f2]
00762FFA  E8 51 F4 C2 FF                  call 0x140392450
00762FFF  84 C0                           test al, al
00763001  0F 84 FE 00 00 00               je 0x140763105
00763007  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00763011  B1 01                           mov cl, 1
00763013  48 8B 00                        mov rax, qword ptr [rax]
00763016  83 65 C3 00                     and dword ptr [rbp - 0x3d], 0
0076301A  83 65 D3 00                     and dword ptr [rbp - 0x2d], 0
0076301E  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00763022  48 8B 05 EF 83 7A 00            mov rax, qword ptr [rip + 0x7a83ef]
00763029  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0076302D  8A 05 DD 83 7A 00               mov al, byte ptr [rip + 0x7a83dd]
00763033  88 45 A7                        mov byte ptr [rbp - 0x59], al
00763036  48 8D 45 A7                     lea rax, [rbp - 0x59]
0076303A  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0076303E  C7 45 BF 10 00 00 00            mov dword ptr [rbp - 0x41], 0x10
00763045  C7 45 CF 01 00 00 00            mov dword ptr [rbp - 0x31], 1
0076304C  E8 1B AF D5 FF                  call 0x1404bdf6c
00763051  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
00763055  48 8D 15 AC 67 8C FF            lea rdx, [rip - 0x739854]
0076305C  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
00763060  41 B8 04 00 00 00               mov r8d, 4
00763066  83 65 03 00                     and dword ptr [rbp + 3], 0
0076306A  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0076306E  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00763072  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00763076  41 8D 48 04                     lea ecx, [r8 + 4]
0076307A  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0076307E  45 8D 48 05                     lea r9d, [r8 + 5]
00763082  89 45 AB                        mov dword ptr [rbp - 0x55], eax
00763085  48 8D 45 AB                     lea rax, [rbp - 0x55]
00763089  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0076308D  48 8D 05 6C 4C 6C 00            lea rax, [rip + 0x6c4c6c]
00763094  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00763098  48 8D 05 49 4D 6C 00            lea rax, [rip + 0x6c4d49]
0076309F  48 89 45 F7                     mov qword ptr [rbp - 9], rax
007630A3  48 8D 05 66 83 7A 00            lea rax, [rip + 0x7a8366]
007630AA  48 89 45 07                     mov qword ptr [rbp + 7], rax
007630AE  48 B8 C4 02 00 00 80 F7 FF FF   movabs rax, 0xfffff780000002c4
007630B8  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007630BC  48 8D 45 AF                     lea rax, [rbp - 0x51]
007630C0  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007630C4  48 8D 45 67                     lea rax, [rbp + 0x67]
007630C8  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
007630CC  48 8D 45 B7                     lea rax, [rbp - 0x49]
007630D0  44 89 45 DF                     mov dword ptr [rbp - 0x21], r8d
007630D4  44 89 45 EF                     mov dword ptr [rbp - 0x11], r8d
007630D8  44 89 45 FF                     mov dword ptr [rbp - 1], r8d
007630DC  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
007630DF  44 89 45 1F                     mov dword ptr [rbp + 0x1f], r8d
007630E3  4C 8D 05 86 47 70 00            lea r8, [rip + 0x704786]
007630EA  89 4D 2F                        mov dword ptr [rbp + 0x2f], ecx
007630ED  48 8B 0D C4 85 7A 00            mov rcx, qword ptr [rip + 0x7a85c4]
007630F4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007630F9  C7 45 3F 01 00 00 00            mov dword ptr [rbp + 0x3f], 1
00763100  E8 1B 96 CB FF                  call 0x14041c720
00763105  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00763109  48 33 CC                        xor rcx, rsp
0076310C  E8 2F 95 F4 FF                  call 0x1406ac640
00763111  48 81 C4 E0 00 00 00            add rsp, 0xe0
00763118  5D                              pop rbp
00763119  C3                              ret
0076311A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceSleepStudyStart(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 6977384)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 7358579)) == 0) goto loc_00763105;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8029893), v_rip - 7575538, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = 1;
        result = *(unsigned __int64 *)(result);
        v_stack_mB0 = result;
        result = *(unsigned __int64 *)(v_rip + 8029167);
        v_stack_mA8 = result;
        result = *(unsigned __int8 *)(v_rip + 8029149);
        v_stack_mB8 = (unsigned __int8)(result);
        result = v_stack_mB8;
        v_stack_m98 = result;
        v_stack_mA0 = 16;
        v_stack_m90 = 1;
        result = PopGetModernStandbyTransitionReason(a1, v_rip - 7575538, a3, a4);
        a2 = v_rip - 7575636;
        a3 = 4;
        a1 = a3 + 4;
        a4 = a3 + 5;
        v_stack_mB4 = (unsigned int)(result);
        result = v_stack_mB4;
        v_stack_m88 = result;
        result = v_rip + 7097452;
        v_stack_m78 = result;
        result = v_rip + 7097673;
        v_stack_m68 = result;
        result = v_rip + 8029030;
        v_stack_m58 = result;
        v_stack_m48 = result;
        result = v_stack_mB0;
        v_stack_m38 = result;
        result = v_stack_p8;
        v_stack_m28 = result;
        result = v_stack_mA8;
        v_stack_m80 = (unsigned int)(a3);
        v_stack_m70 = (unsigned int)(a3);
        v_stack_m60 = (unsigned int)(a3);
        v_stack_m50 = a1;
        v_stack_m40 = (unsigned int)(a3);
        a3 = v_rip + 7358342;
        v_stack_m30 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 8029636);
        v_stack_mC8 = result;
        v_stack_m20 = 1;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceSleepStudyStart(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint8_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x6A7768)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x704873)) == 0) goto loc_00763105;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7A86C5), v_rip - 7575538, a3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = 1;
        result = *(uint64_t *)(result);
        v_stack_mB0 = result;
        result = *(uint64_t *)(v_rip + 0x7A83EF);
        v_stack_mA8 = result;
        result = *(uint8_t *)(v_rip + 0x7A83DD);
        v_stack_mB8 = (uint8_t)(result);
        result = v_stack_mB8;
        v_stack_m98 = result;
        v_stack_mA0 = 16;
        v_stack_m90 = 1;
        result = PopGetModernStandbyTransitionReason(Arg1, v_rip - 7575538, a3, a4);
        a2 = v_rip - 7575636;
        a3 = 4;
        Arg1 = a3 + 4;
        a4 = a3 + 5;
        v_stack_mB4 = (uint32_t)(result);
        result = v_stack_mB4;
        v_stack_m88 = result;
        result = v_rip + 7097452;
        v_stack_m78 = result;
        result = v_rip + 7097673;
        v_stack_m68 = result;
        result = v_rip + 8029030;
        v_stack_m58 = result;
        v_stack_m48 = result;
        result = v_stack_mB0;
        v_stack_m38 = result;
        result = v_stack_p8;
        v_stack_m28 = result;
        result = v_stack_mA8;
        v_stack_m80 = (uint32_t)(a3);
        v_stack_m70 = (uint32_t)(a3);
        v_stack_m60 = (uint32_t)(a3);
        v_stack_m50 = Arg1;
        v_stack_m40 = (uint32_t)(a3);
        a3 = v_rip + 7358342;
        v_stack_m30 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x7A85C4);
        v_stack_mC8 = result;
        v_stack_m20 = 1;
        result = EtwWrite(Arg1, a2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (224);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00762FC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00762FC0[BB_00762FC0]
  bb_00762FEC[BB_00762FEC]
  bb_00763007[BB_00763007]
  bb_00763105[BB_00763105]
  bb_0076311A[BB_0076311A]
  bb_00762FC0 -->|branch| bb_00763105
  bb_00762FC0 -->|fallthrough| bb_00762FEC
  bb_00762FEC -->|branch| bb_00763105
  bb_00762FEC -->|fallthrough| bb_00763007
  bb_00763007 -->|flow| bb_00763105
```
