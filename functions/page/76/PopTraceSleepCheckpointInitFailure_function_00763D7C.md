# PopTraceSleepCheckpointInitFailure

- RVA: `0x00763D7C`–`0x00763E0F` (길이 `147` bytes)
- VA: `0x0000000140763D7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000986E4`
- 디코드: `31`개 명령, `147/147` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00763DAC` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00763DF7` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00763E04` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopEnableSystemSleepCheckpoint](../AC/PopEnableSystemSleepCheckpoint_function_00AC4F50.md) at `0x00AC503B`

### Static image references
- `0x00763D80` → RVA `0x00E0A740` (`.data`; read)
- `0x00763D8F` → RVA `0x00E07748` (`.data`; read)
- `0x00763DC4` → RVA `0x0004963C` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00763DAC` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00763DF7` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00763E04` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00763D7C  48 83 EC 78                     sub rsp, 0x78
00763D80  48 8B 05 B9 69 6A 00            mov rax, qword ptr [rip + 0x6a69b9]
00763D87  48 33 C4                        xor rax, rsp
00763D8A  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00763D8F  83 3D B2 39 6A 00 05            cmp dword ptr [rip + 0x6a39b2], 5
00763D96  44 8B C1                        mov r8d, ecx
00763D99  76 61                           jbe 0x140763dfc
00763D9B  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00763DA5  48 8D 0D 9C 39 6A 00            lea rcx, [rip + 0x6a399c]
00763DAC  E8 EF AC CC FF                  call 0x14042eaa0
00763DB1  84 C0                           test al, al
00763DB3  74 47                           je 0x140763dfc
00763DB5  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
00763DBA  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00763DBF  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00763DC4  48 8D 15 71 58 8E FF            lea rdx, [rip - 0x71a78f]
00763DCB  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00763DD0  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
00763DD5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00763DDA  48 8D 0D 67 39 6A 00            lea rcx, [rip + 0x6a3967]
00763DE1  45 33 C9                        xor r9d, r9d
00763DE4  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
00763DEC  45 33 C0                        xor r8d, r8d
00763DEF  C7 44 24 60 04 00 00 00         mov dword ptr [rsp + 0x60], 4
00763DF7  E8 E4 22 CC FF                  call 0x1404260e0
00763DFC  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00763E01  48 33 CC                        xor rcx, rsp
00763E04  E8 37 88 F4 FF                  call 0x1406ac640
00763E09  48 83 C4 78                     add rsp, 0x78
00763E0D  C3                              ret
00763E0E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceSleepCheckpointInitFailure(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 6973881)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned int *)(v_rip + 6961586)) <= 5) goto loc_00763DFC;
    result = tlgKeywordOn(v_rip + 6961564, a2, (unsigned int)(a1), a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        a2 = v_rip - 7448463;
        result = v_stack_m40;
        v_stack_m48 = (unsigned int)((unsigned int)(a1));
        v_stack_m50 = result;
        a1 = v_rip + 6961511;
        a4 = 0;
        v_stack_m58 = 3;
        a3 = 0;
        v_stack_m18 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTraceSleepCheckpointInitFailure(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x6A69B9)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint32_t *)(v_rip + 0x6A39B2)) <= 5) goto loc_00763DFC;
    result = tlgKeywordOn(v_rip + 6961564, Arg2, (uint32_t)(Arg1), Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        Arg2 = v_rip - 7448463;
        result = v_stack_m40;
        v_stack_m48 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m50 = result;
        Arg1 = v_rip + 6961511;
        Arg4 = 0;
        v_stack_m58 = 3;
        Arg3 = 0;
        v_stack_m18 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00763D7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00763D7C[BB_00763D7C]
  bb_00763D9B[BB_00763D9B]
  bb_00763DB5[BB_00763DB5]
  bb_00763DFC[BB_00763DFC]
  bb_00763E0E[BB_00763E0E]
  bb_00763D7C -->|branch| bb_00763DFC
  bb_00763D7C -->|fallthrough| bb_00763D9B
  bb_00763D9B -->|branch| bb_00763DFC
  bb_00763D9B -->|fallthrough| bb_00763DB5
  bb_00763DB5 -->|flow| bb_00763DFC
```
