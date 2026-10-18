# CmpTraceShutdownFlushStart

- RVA: `0x007E6858`–`0x007E68BD` (길이 `101` bytes)
- VA: `0x00000001407E6858`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060904`
- 디코드: `23`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007E6884` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x007E68A5` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x007E68B2` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmShutdownSystem1](../../text/66/CmShutdownSystem1_function_0066A5B0.md) at `0x0066A751`

### Static image references
- `0x007E685C` → RVA `0x00E0A740` (`.data`; read)
- `0x007E686B` → RVA `0x00022270` (`.rdata`; read)
- `0x007E6872` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007E6884` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x007E68A5` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x007E68B2` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E6858  48 83 EC 58                     sub rsp, 0x58
007E685C  48 8B 05 DD 3E 62 00            mov rax, qword ptr [rip + 0x623edd]
007E6863  48 33 C4                        xor rax, rsp
007E6866  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007E686B  0F 10 05 FE B9 83 FF            movups xmm0, xmmword ptr [rip - 0x7c4602]
007E6872  48 8B 0D 9F 17 7F 00            mov rcx, qword ptr [rip + 0x7f179f]
007E6879  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007E687E  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
007E6884  E8 C7 BB BA FF                  call 0x140392450
007E6889  84 C0                           test al, al
007E688B  74 1D                           je 0x1407e68aa
007E688D  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007E6893  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007E6898  48 8B 0D 79 17 7F 00            mov rcx, qword ptr [rip + 0x7f1779]
007E689F  45 33 C9                        xor r9d, r9d
007E68A2  45 33 C0                        xor r8d, r8d
007E68A5  E8 76 5E C3 FF                  call 0x14041c720
007E68AA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007E68AF  48 33 CC                        xor rcx, rsp
007E68B2  E8 89 5D EC FF                  call 0x1406ac640
007E68B7  48 83 C4 58                     add rsp, 0x58
007E68BB  C3                              ret
007E68BC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceShutdownFlushStart(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 6438621)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8329119), v_stack_m28, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a2 = v_stack_m28;
        a1 = *(unsigned __int64 *)(v_rip + 8329081);
        a4 = 0;
        a3 = 0;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceShutdownFlushStart(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x623EDD)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7F179F), v_stack_m28, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg2 = v_stack_m28;
        Arg1 = *(uint64_t *)(v_rip + 0x7F1779);
        Arg4 = 0;
        Arg3 = 0;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E6858&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E6858[BB_007E6858]
  bb_007E688D[BB_007E688D]
  bb_007E68AA[BB_007E68AA]
  bb_007E68BC[BB_007E68BC]
  bb_007E6858 -->|branch| bb_007E68AA
  bb_007E6858 -->|fallthrough| bb_007E688D
  bb_007E688D -->|flow| bb_007E68AA
```
