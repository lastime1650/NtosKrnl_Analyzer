# TtmiLogQueueDestroyed

- RVA: `0x0077AAD8`–`0x0077AB66` (길이 `142` bytes)
- VA: `0x000000014077AAD8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000986E4`
- 디코드: `31`개 명령, `142/142` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077AB03` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077AB4E` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077AB5B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpDeleteQueue](TtmpDeleteQueue_function_0077DFC0.md) at `0x0077E045`

### Static image references
- `0x0077AADC` → RVA `0x00E0A740` (`.data`; read)
- `0x0077AAEB` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077AB1B` → RVA `0x00052727` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077AB03` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077AB4E` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077AB5B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077AAD8  48 83 EC 78                     sub rsp, 0x78
0077AADC  48 8B 05 5D FC 68 00            mov rax, qword ptr [rip + 0x68fc5d]
0077AAE3  48 33 C4                        xor rax, rsp
0077AAE6  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0077AAEB  83 3D D6 DD 85 00 05            cmp dword ptr [rip + 0x85ddd6], 5
0077AAF2  4C 8B C1                        mov r8, rcx
0077AAF5  76 5C                           jbe 0x14077ab53
0077AAF7  BA 01 00 00 00                  mov edx, 1
0077AAFC  48 8D 0D C5 DD 85 00            lea rcx, [rip + 0x85ddc5]
0077AB03  E8 98 3F CB FF                  call 0x14042eaa0
0077AB08  84 C0                           test al, al
0077AB0A  74 47                           je 0x14077ab53
0077AB0C  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
0077AB11  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0077AB16  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0077AB1B  48 8D 15 05 7C 8D FF            lea rdx, [rip - 0x7283fb]
0077AB22  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0077AB27  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0077AB2C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077AB31  48 8D 0D 90 DD 85 00            lea rcx, [rip + 0x85dd90]
0077AB38  45 33 C9                        xor r9d, r9d
0077AB3B  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
0077AB43  45 33 C0                        xor r8d, r8d
0077AB46  C7 44 24 60 08 00 00 00         mov dword ptr [rsp + 0x60], 8
0077AB4E  E8 8D B5 CA FF                  call 0x1404260e0
0077AB53  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0077AB58  48 33 CC                        xor rcx, rsp
0077AB5B  E8 E0 1A F3 FF                  call 0x1406ac640
0077AB60  48 83 C4 78                     add rsp, 0x78
0077AB64  C3                              ret
0077AB65  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogQueueDestroyed(__int64 a1, __int64 a2, __int64 a3, int a4)
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
    result = (*(unsigned __int64 *)(v_rip + 6880349)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned int *)(v_rip + 8773078)) <= 5) goto loc_0077AB53;
    result = tlgKeywordOn(v_rip + 8773061, 1, a1, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        a2 = v_rip - 7504891;
        result = v_stack_m40;
        v_stack_m48 = a1;
        v_stack_m50 = result;
        a1 = v_rip + 8773008;
        a4 = 0;
        v_stack_m58 = 3;
        a3 = 0;
        v_stack_m18 = 8;
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
int64_t TtmiLogQueueDestroyed(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
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
    result = (*(uint64_t *)(v_rip + 0x68FC5D)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint32_t *)(v_rip + 0x85DDD6)) <= 5) goto loc_0077AB53;
    result = tlgKeywordOn(v_rip + 8773061, 1, Arg1, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        Arg2 = v_rip - 7504891;
        result = v_stack_m40;
        v_stack_m48 = Arg1;
        v_stack_m50 = result;
        Arg1 = v_rip + 8773008;
        Arg4 = 0;
        v_stack_m58 = 3;
        Arg3 = 0;
        v_stack_m18 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077AAD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077AAD8[BB_0077AAD8]
  bb_0077AAF7[BB_0077AAF7]
  bb_0077AB0C[BB_0077AB0C]
  bb_0077AB53[BB_0077AB53]
  bb_0077AB65[BB_0077AB65]
  bb_0077AAD8 -->|branch| bb_0077AB53
  bb_0077AAD8 -->|fallthrough| bb_0077AAF7
  bb_0077AAF7 -->|branch| bb_0077AB53
  bb_0077AAF7 -->|fallthrough| bb_0077AB0C
  bb_0077AB0C -->|flow| bb_0077AB53
```
