# PopPluginUnregisterDevice

- RVA: `0x005D3D40`–`0x005D3D81` (길이 `65` bytes)
- VA: `0x00000001405D3D40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `20`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005D3D5C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005D3D74` → [PopFxBugCheck](../2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)

### Direct callers
- [PopFxUnregisterDevice](../../page/A8/PopFxUnregisterDevice_function_00A8AE84.md) at `0x00A8AFF4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D3D40  40 53                           push rbx
005D3D42  48 83 EC 20                     sub rsp, 0x20
005D3D46  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
005D3D4A  48 8B D9                        mov rbx, rcx
005D3D4D  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
005D3D52  B9 04 00 00 00                  mov ecx, 4
005D3D57  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
005D3D5C  E8 6F 6D 0E 00                  call 0x1406baad0
005D3D61  84 C0                           test al, al
005D3D63  75 15                           jne 0x1405d3d7a
005D3D65  45 33 C9                        xor r9d, r9d
005D3D68  4C 8B C3                        mov r8, rbx
005D3D6B  B9 05 06 00 00                  mov ecx, 0x605
005D3D70  41 8D 51 04                     lea edx, [r9 + 4]
005D3D74  E8 F3 BE CE FF                  call 0x1402bfc6c
005D3D79  CC                              int3
005D3D7A  48 83 C4 20                     add rsp, 0x20
005D3D7E  5B                              pop rbx
005D3D7F  C3                              ret
005D3D80  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPluginUnregisterDevice(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_stack_p8 = a2;
    result = guard_dispatch_icall(4, v_stack_p8, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a4 = 0;
        a3 = a1;
        a1 = 0x605ULL;
        a2 = a4 + 4;
        result = PopFxBugCheck(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPluginUnregisterDevice(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    v_stack_p8 = Arg2;
    result = guard_dispatch_icall(4, v_stack_p8, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        Arg4 = 0;
        Arg3 = Arg1;
        Arg1 = 0x605ULL;
        Arg2 = Arg4 + 4;
        result = PopFxBugCheck(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D3D40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D3D40[BB_005D3D40]
  bb_005D3D65[BB_005D3D65]
  bb_005D3D7A[BB_005D3D7A]
  bb_005D3D80[BB_005D3D80]
  bb_005D3D40 -->|branch| bb_005D3D7A
  bb_005D3D40 -->|fallthrough| bb_005D3D65
  bb_005D3D65 -->|flow| bb_005D3D7A
```
