# DbgkpLkmdSnapData

- RVA: `0x0057FDB0`–`0x0057FDCE` (길이 `30` bytes)
- VA: `0x000000014057FDB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `8`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0057FDC3` → [DbgkpLkmdSnapDataEx](DbgkpLkmdSnapDataEx_function_0057FDD4.md) (function, `0x0057FDD4`)

### Direct callers
- [DbgkCaptureLiveDump](../../page/71/DbgkCaptureLiveDump_function_0071113C.md) at `0x0071145D`
- [DbgkCaptureLiveDump](../../page/71/DbgkCaptureLiveDump_function_0071113C.md) at `0x00711471`
- [DbgkpLkmdSnapPendingIrps](../../page/71/DbgkpLkmdSnapPendingIrps_function_00711984.md) at `0x007119D6`
- [DbgkpLkmdSnapPendingIrps](../../page/71/DbgkpLkmdSnapPendingIrps_function_00711984.md) at `0x007119FA`
- [DbgkpLkmdSnapPendingIrps](../../page/71/DbgkpLkmdSnapPendingIrps_function_00711984.md) at `0x00711A2A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057FDB0  48 83 EC 38                     sub rsp, 0x38
0057FDB4  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0057FDBA  45 33 C9                        xor r9d, r9d
0057FDBD  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0057FDC3  E8 0C 00 00 00                  call 0x14057fdd4
0057FDC8  48 83 C4 38                     add rsp, 0x38
0057FDCC  C3                              ret
0057FDCD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DbgkpLkmdSnapData(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    result = DbgkpLkmdSnapDataEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DbgkpLkmdSnapData(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    result = DbgkpLkmdSnapDataEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057FDB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057FDB0[BB_0057FDB0]
  bb_0057FDCD[BB_0057FDCD]
```
