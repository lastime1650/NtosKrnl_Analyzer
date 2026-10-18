# PopDiagTraceSleepReliabilityDiagConfigUpdate

- RVA: `0x007025D8`–`0x0070269B` (길이 `195` bytes)
- VA: `0x00000001407025D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9BCC`
- 디코드: `36`개 명령, `195/195` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00702612` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0070267D` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0070268D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8CAFE`

### Static image references
- `0x007025DF` → RVA `0x00E0A740` (`.data`; read)
- `0x007025F1` → RVA `0x00E07748` (`.data`; read)
- `0x0070262A` → RVA `0x0004B7BD` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00702612` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0070267D` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0070268D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007025D8  48 81 EC 98 00 00 00            sub rsp, 0x98
007025DF  48 8B 05 5A 81 70 00            mov rax, qword ptr [rip + 0x70815a]
007025E6  48 33 C4                        xor rax, rsp
007025E9  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
007025F1  83 3D 50 51 70 00 05            cmp dword ptr [rip + 0x705150], 5
007025F8  44 8A C1                        mov r8b, cl
007025FB  0F 86 81 00 00 00               jbe 0x140702682
00702601  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
0070260B  48 8D 0D 36 51 70 00            lea rcx, [rip + 0x705136]
00702612  E8 89 C4 D2 FF                  call 0x14042eaa0
00702617  84 C0                           test al, al
00702619  74 67                           je 0x140702682
0070261B  83 64 24 6C 00                  and dword ptr [rsp + 0x6c], 0
00702620  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00702625  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
0070262A  48 8D 15 8C 91 94 FF            lea rdx, [rip - 0x6b6e74]
00702631  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00702636  48 8D 0D 0B 51 70 00            lea rcx, [rip + 0x70510b]
0070263D  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00702642  44 88 44 24 30                  mov byte ptr [rsp + 0x30], r8b
00702647  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0070264C  45 33 C9                        xor r9d, r9d
0070264F  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00702654  C7 44 24 68 01 00 00 00         mov dword ptr [rsp + 0x68], 1
0070265C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00702661  45 33 C0                        xor r8d, r8d
00702664  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
0070266C  48 C7 44 24 38 00 00 00 01      mov qword ptr [rsp + 0x38], 0x1000000
00702675  C7 44 24 78 08 00 00 00         mov dword ptr [rsp + 0x78], 8
0070267D  E8 5E 3A D2 FF                  call 0x1404260e0
00702682  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0070268A  48 33 CC                        xor rcx, rsp
0070268D  E8 AE 9F FA FF                  call 0x1406ac640
00702692  48 81 C4 98 00 00 00            add rsp, 0x98
00702699  C3                              ret
0070269A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceSleepReliabilityDiagConfigUpdate(unsigned __int8 a1, __int64 a2, __int64 a3, int a4)
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
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;

    v_rsp = (v_rsp) - (152);
    result = (*(unsigned __int64 *)(v_rip + 7373146)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 7360848)) <= 5) goto loc_00702682;
    result = tlgKeywordOn(v_rip + 7360822, a2, a1, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m68;
        a2 = v_rip - 7040628;
        v_stack_m38 = result;
        a1 = v_rip + 7360779;
        result = v_stack_m60;
        v_stack_m68 = a1;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m58;
        v_stack_m30 = 1;
        v_stack_m70 = result;
        a3 = 0;
        v_stack_m78 = 4;
        v_stack_m60 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (152);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceSleepReliabilityDiagConfigUpdate(uint8_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;

    local_rsp = (local_rsp) - (152);
    result = (*(uint64_t *)(v_rip + 0x70815A)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x705150)) <= 5) goto loc_00702682;
    result = tlgKeywordOn(v_rip + 7360822, Arg2, Arg1, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m68;
        Arg2 = v_rip - 7040628;
        v_stack_m38 = result;
        Arg1 = v_rip + 7360779;
        result = v_stack_m60;
        v_stack_m68 = Arg1;
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m58;
        v_stack_m30 = 1;
        v_stack_m70 = result;
        Arg3 = 0;
        v_stack_m78 = 4;
        v_stack_m60 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (152);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007025D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007025D8[BB_007025D8]
  bb_00702601[BB_00702601]
  bb_0070261B[BB_0070261B]
  bb_00702682[BB_00702682]
  bb_0070269A[BB_0070269A]
  bb_007025D8 -->|branch| bb_00702682
  bb_007025D8 -->|fallthrough| bb_00702601
  bb_00702601 -->|branch| bb_00702682
  bb_00702601 -->|fallthrough| bb_0070261B
  bb_0070261B -->|flow| bb_00702682
```
