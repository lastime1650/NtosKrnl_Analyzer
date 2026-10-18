# KiCheckIfStackExpandCalloutActive

- RVA: `0x003564E0`–`0x0035650D` (길이 `45` bytes)
- VA: `0x00000001403564E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `13`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00356501` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [KeTerminateThread](KeTerminateThread_function_00355138.md) at `0x00355162`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003564E0  48 83 EC 38                     sub rsp, 0x38
003564E4  F6 41 7D 01                     test byte ptr [rcx + 0x7d], 1
003564E8  74 1D                           je 0x140356507
003564EA  48 8B D1                        mov rdx, rcx
003564ED  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
003564F6  B9 07 01 00 00                  mov ecx, 0x107
003564FB  45 33 C9                        xor r9d, r9d
003564FE  45 33 C0                        xor r8d, r8d
00356501  E8 5A 71 1A 00                  call 0x1404fd660
00356506  CC                              int3
00356507  48 83 C4 38                     add rsp, 0x38
0035650B  C3                              ret
0035650C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCheckIfStackExpandCalloutActive(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if (((*(unsigned __int8 *)(a1 + 125)) & (1)) != 0) {
        a2 = a1;
        v_stack_m18 = 0;
        a1 = 263;
        a4 = 0;
        a3 = 0;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiCheckIfStackExpandCalloutActive(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if (((*(uint8_t *)(arg1 + 0x7D)) & (1)) != 0) {
        Arg2 = Arg1;
        v_stack_m18 = 0;
        Arg1 = 263;
        Arg4 = 0;
        Arg3 = 0;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x7D` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003564E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003564E0[BB_003564E0]
  bb_003564EA[BB_003564EA]
  bb_00356507[BB_00356507]
  bb_0035650C[BB_0035650C]
  bb_003564E0 -->|branch| bb_00356507
  bb_003564E0 -->|fallthrough| bb_003564EA
  bb_003564EA -->|flow| bb_00356507
```
