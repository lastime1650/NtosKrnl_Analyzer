# TtmiLogTerminalDestroyed

- RVA: `0x0077BBC0`–`0x0077BC4E` (길이 `142` bytes)
- VA: `0x000000014077BBC0`
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
- `0x0077BBEB` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077BC36` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077BC43` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpDeleteTerminal](TtmpDeleteTerminal_function_0077D420.md) at `0x0077D424`

### Static image references
- `0x0077BBC4` → RVA `0x00E0A740` (`.data`; read)
- `0x0077BBD3` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077BC03` → RVA `0x00052322` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077BBEB` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077BC36` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077BC43` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077BBC0  48 83 EC 78                     sub rsp, 0x78
0077BBC4  48 8B 05 75 EB 68 00            mov rax, qword ptr [rip + 0x68eb75]
0077BBCB  48 33 C4                        xor rax, rsp
0077BBCE  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0077BBD3  83 3D EE CC 85 00 05            cmp dword ptr [rip + 0x85ccee], 5
0077BBDA  4C 8B C1                        mov r8, rcx
0077BBDD  76 5C                           jbe 0x14077bc3b
0077BBDF  BA 01 00 00 00                  mov edx, 1
0077BBE4  48 8D 0D DD CC 85 00            lea rcx, [rip + 0x85ccdd]
0077BBEB  E8 B0 2E CB FF                  call 0x14042eaa0
0077BBF0  84 C0                           test al, al
0077BBF2  74 47                           je 0x14077bc3b
0077BBF4  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
0077BBF9  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0077BBFE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0077BC03  48 8D 15 18 67 8D FF            lea rdx, [rip - 0x7298e8]
0077BC0A  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0077BC0F  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0077BC14  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077BC19  48 8D 0D A8 CC 85 00            lea rcx, [rip + 0x85cca8]
0077BC20  45 33 C9                        xor r9d, r9d
0077BC23  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
0077BC2B  45 33 C0                        xor r8d, r8d
0077BC2E  C7 44 24 60 08 00 00 00         mov dword ptr [rsp + 0x60], 8
0077BC36  E8 A5 A4 CA FF                  call 0x1404260e0
0077BC3B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0077BC40  48 33 CC                        xor rcx, rsp
0077BC43  E8 F8 09 F3 FF                  call 0x1406ac640
0077BC48  48 83 C4 78                     add rsp, 0x78
0077BC4C  C3                              ret
0077BC4D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogTerminalDestroyed(__int64 a1, __int64 a2, __int64 a3, int a4)
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
    result = (*(unsigned __int64 *)(v_rip + 6876021)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned int *)(v_rip + 8768750)) <= 5) goto loc_0077BC3B;
    result = tlgKeywordOn(v_rip + 8768733, 1, a1, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        a2 = v_rip - 7510248;
        result = v_stack_m40;
        v_stack_m48 = a1;
        v_stack_m50 = result;
        a1 = v_rip + 8768680;
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
int64_t TtmiLogTerminalDestroyed(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
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
    result = (*(uint64_t *)(v_rip + 0x68EB75)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint32_t *)(v_rip + 0x85CCEE)) <= 5) goto loc_0077BC3B;
    result = tlgKeywordOn(v_rip + 8768733, 1, Arg1, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        Arg2 = v_rip - 7510248;
        result = v_stack_m40;
        v_stack_m48 = Arg1;
        v_stack_m50 = result;
        Arg1 = v_rip + 8768680;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077BBC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077BBC0[BB_0077BBC0]
  bb_0077BBDF[BB_0077BBDF]
  bb_0077BBF4[BB_0077BBF4]
  bb_0077BC3B[BB_0077BC3B]
  bb_0077BC4D[BB_0077BC4D]
  bb_0077BBC0 -->|branch| bb_0077BC3B
  bb_0077BBC0 -->|fallthrough| bb_0077BBDF
  bb_0077BBDF -->|branch| bb_0077BC3B
  bb_0077BBDF -->|fallthrough| bb_0077BBF4
  bb_0077BBF4 -->|flow| bb_0077BC3B
```
